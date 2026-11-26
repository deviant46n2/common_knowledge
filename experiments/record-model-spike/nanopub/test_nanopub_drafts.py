from pathlib import Path

from rdflib import Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF

from build_drafts import build

ROOT = Path(__file__).parent
NP = Namespace("http://www.nanopub.org/nschema#")
PROV = Namespace("http://www.w3.org/ns/prov#")
EX = Namespace("https://example.org/ck/vocab/")
OA = Namespace("http://www.w3.org/ns/oa#")


def test_three_unsigned_drafts_are_well_formed_four_graph_nanopubs():
    dataset, nanopubs = build()
    assert len(nanopubs) == 3
    for np_uri in nanopubs:
        head_graphs = [g for g in dataset.graphs() if (np_uri, RDF.type, NP.Nanopublication) in g]
        assert len(head_graphs) == 1
        head = head_graphs[0]
        assertion_uri = next(head.objects(np_uri, NP.hasAssertion))
        provenance_uri = next(head.objects(np_uri, NP.hasProvenance))
        pubinfo_uri = next(head.objects(np_uri, NP.hasPublicationInfo))
        graph_ids = {np_uri, head.identifier, assertion_uri, provenance_uri, pubinfo_uri}
        assert len(graph_ids) == 5
        provenance = dataset.graph(provenance_uri)
        pubinfo = dataset.graph(pubinfo_uri)
        assert any(provenance.triples((assertion_uri, None, None)))
        assert any(pubinfo.triples((np_uri, None, None)))


def test_assessment_publications_are_distinct_and_derive_from_observation():
    dataset, nanopubs = build()
    observation, assessment_1, assessment_2 = nanopubs
    for assessment_np in [assessment_1, assessment_2]:
        head = next(g for g in dataset.graphs() if (assessment_np, RDF.type, NP.Nanopublication) in g)
        provenance_uri = next(head.objects(assessment_np, NP.hasProvenance))
        provenance = dataset.graph(provenance_uri)
        assertion_uri = next(head.objects(assessment_np, NP.hasAssertion))
        assert (assertion_uri, PROV.wasDerivedFrom, observation) in provenance
    assert assessment_1 != assessment_2


def test_observation_assertion_keeps_support_and_qualification_distinct():
    dataset, nanopubs = build()
    observation = nanopubs[0]
    head = next(g for g in dataset.graphs() if (observation, RDF.type, NP.Nanopublication) in g)
    assertion_uri = next(head.objects(observation, NP.hasAssertion))
    assertion = dataset.graph(assertion_uri)
    values = {str(v) for v in assertion.objects(None, EX.relationType)}
    assert values == {
        "supports_that_station_recorded_value",
        "qualifies_confidence_in_measurement_accuracy",
    }


def test_all_evidence_quote_selectors_match_fixture_sources():
    dataset, nanopubs = build()
    observation = nanopubs[0]
    head = next(g for g in dataset.graphs() if (observation, RDF.type, NP.Nanopublication) in g)
    assertion_uri = next(head.objects(observation, NP.hasAssertion))
    assertion = dataset.graph(assertion_uri)
    source_text = {
        URIRef("https://example.org/ck/source/csv"): (ROOT.parent / "sources/station-r1.csv").read_text(),
        URIRef("https://example.org/ck/source/calibration"): (ROOT.parent / "sources/station-r1-calibration.txt").read_text(),
    }
    for annotation in assertion.subjects(RDF.type, OA.Annotation):
        target = next(assertion.objects(annotation, OA.hasTarget))
        source = next(assertion.objects(target, OA.hasSource))
        selector = next(assertion.objects(target, OA.hasSelector))
        exact = str(next(assertion.objects(selector, OA.exact)))
        assert exact in source_text[source]


def test_draft_uses_placeholders_and_is_not_signed():
    dataset, nanopubs = build()
    assert all(str(uri).startswith("https://example.org/np/") for uri in nanopubs)
    assert not any(str(p).endswith("hasSignature") for _, p, _, _ in dataset.quads((None, None, None, None)))


def test_all_named_graphs_are_unique_and_default_graph_is_empty():
    dataset, nanopubs = build()
    graph_ids = {g.identifier for g in dataset.graphs() if len(g) > 0}
    assert len(graph_ids) == 12
    assert not list(dataset.default_graph)
    assert not (set(nanopubs) & graph_ids)


def test_publication_info_contains_creator_and_creation_time():
    dataset, nanopubs = build()
    for np_uri in nanopubs:
        head = next(g for g in dataset.graphs() if (np_uri, RDF.type, NP.Nanopublication) in g)
        pubinfo_uri = next(head.objects(np_uri, NP.hasPublicationInfo))
        pubinfo = dataset.graph(pubinfo_uri)
        assert list(pubinfo.objects(np_uri, DCTERMS.creator))
        assert list(pubinfo.objects(np_uri, DCTERMS.created))
