from pathlib import Path
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF

ROOT = Path(__file__).parent
EX = Namespace("https://example.org/ck/vocab/")
OA = Namespace("http://www.w3.org/ns/oa#")
PROV = Namespace("http://www.w3.org/ns/prov#")


def graph():
    result = Graph()
    result.parse(ROOT / "record.jsonld", format="json-ld")
    return result


def test_jsonld_parses_and_types_statement_and_assessment():
    g = graph()
    assert (URIRef("https://example.org/ck/statement/r1"), RDF.type, EX.Statement) in g
    assert (URIRef("https://example.org/ck/assessment/initial"), RDF.type, EX.Assessment) in g


def test_support_and_qualification_are_separate_relations():
    values = {str(x) for x in graph().objects(None, EX.relationType)}
    assert values == {"supports_that_station_recorded_value", "qualifies_confidence_in_measurement_accuracy"}


def test_annotations_have_exact_quote_selectors_and_source_links():
    g = graph()
    annotations = list(g.subjects(RDF.type, OA.Annotation))
    assert len(annotations) == 2
    for item in annotations:
        target = next(g.objects(item, OA.hasTarget))
        selector = next(g.objects(target, OA.hasSelector))
        assert (target, OA.hasSource, None) in g
        assert (selector, RDF.type, OA.TextQuoteSelector) in g
        assert (selector, OA.exact, None) in g


def test_review_provenance_links_agent_and_both_evidence_items():
    g = graph()
    activity = URIRef("https://example.org/ck/activity/review-1")
    assert (activity, RDF.type, PROV.Activity) in g
    assert (activity, PROV.wasAssociatedWith, URIRef("https://example.org/ck/agent/reviewer-1")) in g
    assert len(list(g.objects(activity, PROV.used))) == 2


def test_quote_prefix_suffix_match_local_source_fixtures():
    g = graph()
    source_text = {
        URIRef("https://example.org/ck/source/csv"): (ROOT / "sources/station-r1.csv").read_text(),
        URIRef("https://example.org/ck/source/calibration"): (ROOT / "sources/station-r1-calibration.txt").read_text(),
    }
    for item in g.subjects(RDF.type, OA.Annotation):
        target = next(g.objects(item, OA.hasTarget))
        source = next(g.objects(target, OA.hasSource))
        selector = next(g.objects(target, OA.hasSelector))
        exact = str(next(g.objects(selector, OA.exact)))
        prefix = str(next(g.objects(selector, OA.prefix)))
        suffix = str(next(g.objects(selector, OA.suffix)))
        text = source_text[source]
        start = text.index(exact)
        assert text[max(0, start - len(prefix)):start] == prefix
        assert text[start + len(exact):start + len(exact) + len(suffix)] == suffix


def test_two_assessments_coexist_on_a_new_record_version():
    g = graph()
    statement = URIRef("https://example.org/ck/statement/r1")
    assessments = list(g.subjects(EX.assessmentOf, statement))
    assert len(assessments) == 2
    v1 = URIRef("https://example.org/ck/record/r1")
    v2 = URIRef("https://example.org/ck/record/r1/v2")
    assert (v2, PROV.wasRevisionOf, v1) in g
    assert set(g.objects(v2, EX.hasAssessment)) == set(assessments)
    assert len(set(g.objects(v1, EX.hasAssessment))) == 1


def test_independent_assessments_have_distinct_review_agents():
    g = graph()
    agents = {
        next(g.objects(URIRef("https://example.org/ck/activity/review-1"), PROV.wasAssociatedWith)),
        next(g.objects(URIRef("https://example.org/ck/activity/review-2"), PROV.wasAssociatedWith)),
    }
    assert len(agents) == 2


def test_static_reader_exposes_both_assessments_and_history():
    from render_record import render

    page = render()
    assert "Independent assessment 1" in page
    assert "Independent assessment 2" in page
    assert "Revises version 1" in page
    assert "Supports that station recorded value" in page
    assert "Qualifies confidence in measurement accuracy" in page
