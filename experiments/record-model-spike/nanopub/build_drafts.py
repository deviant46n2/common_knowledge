"""Build three unsigned, synthetic nanopublication drafts from the R-1 example."""
from rdflib import BNode, Dataset, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF, XSD

EX = Namespace("https://example.org/ck/vocab/")
OA = Namespace("http://www.w3.org/ns/oa#")
NP = Namespace("http://www.nanopub.org/nschema#")
PROV = Namespace("http://www.w3.org/ns/prov#")

BASE = "https://example.org/np/"
STATEMENT = URIRef("https://example.org/ck/statement/r1")
CSV_SOURCE = URIRef("https://example.org/ck/source/csv")
CAL_SOURCE = URIRef("https://example.org/ck/source/calibration")
CSV_EVIDENCE = URIRef("https://example.org/ck/evidence/csv-row-2")
CAL_EVIDENCE = URIRef("https://example.org/ck/evidence/calibration-entry-2")
AGENT_DATA = URIRef("https://example.org/ck/agent/data-curator")
AGENT_1 = URIRef("https://example.org/ck/agent/reviewer-1")
AGENT_2 = URIRef("https://example.org/ck/agent/reviewer-2")


def add_nanopub(dataset, slug, creator, created, description):
    np_uri = URIRef(BASE + slug)
    head_uri = URIRef(BASE + slug + "#Head")
    assertion_uri = URIRef(BASE + slug + "#assertion")
    provenance_uri = URIRef(BASE + slug + "#provenance")
    pubinfo_uri = URIRef(BASE + slug + "#pubinfo")
    head = dataset.graph(head_uri)
    provenance = dataset.graph(provenance_uri)
    pubinfo = dataset.graph(pubinfo_uri)
    assertion = dataset.graph(assertion_uri)

    head.add((np_uri, RDF.type, NP.Nanopublication))
    head.add((np_uri, NP.hasAssertion, assertion_uri))
    head.add((np_uri, NP.hasProvenance, provenance_uri))
    head.add((np_uri, NP.hasPublicationInfo, pubinfo_uri))
    pubinfo.add((np_uri, DCTERMS.creator, creator))
    pubinfo.add((np_uri, DCTERMS.created, Literal(created, datatype=XSD.dateTime)))
    pubinfo.add((np_uri, DCTERMS.description, Literal(description)))
    provenance.add((assertion_uri, PROV.wasAttributedTo, creator))
    return np_uri, assertion_uri, provenance, assertion


def add_annotation(assertion, evidence_uri, source_uri, exact, prefix, suffix):
    target = BNode()
    selector = BNode()
    assertion.add((evidence_uri, RDF.type, OA.Annotation))
    assertion.add((evidence_uri, OA.hasTarget, target))
    assertion.add((target, RDF.type, OA.SpecificResource))
    assertion.add((target, OA.hasSource, source_uri))
    assertion.add((target, OA.hasSelector, selector))
    assertion.add((selector, RDF.type, OA.TextQuoteSelector))
    assertion.add((selector, OA.exact, Literal(exact)))
    assertion.add((selector, OA.prefix, Literal(prefix)))
    assertion.add((selector, OA.suffix, Literal(suffix)))


def build():
    dataset = Dataset()
    dataset.bind("ex", EX)
    dataset.bind("oa", OA)
    dataset.bind("np", NP)
    dataset.bind("prov", PROV)
    dataset.bind("dct", DCTERMS)

    np_obs, graph_obs, prov_obs, assertion_obs = add_nanopub(
        dataset, "observation-r1", AGENT_DATA, "2026-11-26T12:00:00Z",
        "Synthetic observation statement with two source-specific evidence anchors."
    )
    assertion_obs.add((STATEMENT, RDF.type, EX.Statement))
    assertion_obs.add((STATEMENT, EX.statementText, Literal(
        "Monitoring station R-1 recorded dissolved oxygen of 4.2 mg/L at 09:00 UTC on 1 May 2026."
    )))
    assertion_obs.add((STATEMENT, EX.scope, Literal(
        "This concerns what the station log recorded, not whether the sensor accurately measured ambient dissolved oxygen."
    )))
    add_annotation(
        assertion_obs, CSV_EVIDENCE, CSV_SOURCE,
        "R-1,2026-05-01T09:00:00Z,dissolved_oxygen,4.2,mg/L",
        "station_id,timestamp,parameter,value,unit\n",
        "\nR-1,2026-05-01T10:00:00Z,dissolved_oxygen,4.0,mg/L"
    )
    add_annotation(
        assertion_obs, CAL_EVIDENCE, CAL_SOURCE,
        "2026-04-20 | Calibration due | Not completed",
        "2026-01-20 | Calibration completed | Passed\n",
        "\n2026-05-03 | Maintenance visit | Sensor cleaned"
    )
    relation_csv = URIRef("https://example.org/ck/relation/csv")
    relation_cal = URIRef("https://example.org/ck/relation/calibration")
    assertion_obs.add((relation_csv, RDF.type, EX.EvidenceRelation))
    assertion_obs.add((relation_csv, EX.relationType, Literal("supports_that_station_recorded_value")))
    assertion_obs.add((relation_csv, EX.targetStatement, STATEMENT))
    assertion_obs.add((relation_csv, EX.evidenceItem, CSV_EVIDENCE))
    assertion_obs.add((relation_cal, RDF.type, EX.EvidenceRelation))
    assertion_obs.add((relation_cal, EX.relationType, Literal("qualifies_confidence_in_measurement_accuracy")))
    assertion_obs.add((relation_cal, EX.targetStatement, STATEMENT))
    assertion_obs.add((relation_cal, EX.evidenceItem, CAL_EVIDENCE))
    prov_obs.add((graph_obs, PROV.wasDerivedFrom, CSV_SOURCE))
    prov_obs.add((graph_obs, PROV.wasDerivedFrom, CAL_SOURCE))

    np_a1, graph_a1, prov_a1, assertion_a1 = add_nanopub(
        dataset, "assessment-r1-review-1", AGENT_1, "2026-11-26T12:05:00Z",
        "First synthetic assessment of the R-1 observation."
    )
    assessment_1 = URIRef("https://example.org/ck/assessment/initial")
    assertion_a1.add((assessment_1, RDF.type, EX.Assessment))
    assertion_a1.add((assessment_1, EX.assessmentOf, STATEMENT))
    assertion_a1.add((assessment_1, EX.conclusion, Literal(
        "The CSV supports that the station recorded 4.2 mg/L. The overdue calibration entry qualifies confidence in measurement accuracy. The evidence does not establish the true ambient concentration."
    )))
    assertion_a1.add((assessment_1, EX.method, Literal(
        "Compared the cited CSV row with the calibration-log entry; no independent instrument validation or statistical analysis was performed."
    )))
    assertion_a1.add((assessment_1, EX.usedEvidence, CSV_EVIDENCE))
    assertion_a1.add((assessment_1, EX.usedEvidence, CAL_EVIDENCE))
    prov_a1.add((graph_a1, PROV.wasDerivedFrom, np_obs))
    prov_a1.add((assessment_1, PROV.wasGeneratedBy, URIRef("https://example.org/ck/activity/review-1")))

    np_a2, graph_a2, prov_a2, assertion_a2 = add_nanopub(
        dataset, "assessment-r1-review-2", AGENT_2, "2026-11-26T12:10:00Z",
        "Second independent synthetic assessment of the R-1 observation."
    )
    assessment_2 = URIRef("https://example.org/ck/assessment/independent-review")
    assertion_a2.add((assessment_2, RDF.type, EX.Assessment))
    assertion_a2.add((assessment_2, EX.assessmentOf, STATEMENT))
    assertion_a2.add((assessment_2, EX.conclusion, Literal(
        "The CSV row is direct evidence of the value entered in the station log. The overdue calibration entry means accuracy is unverified, but it does not by itself show that the reported value is wrong. No conclusion about ambient concentration is warranted from these two excerpts alone."
    )))
    assertion_a2.add((assessment_2, EX.method, Literal(
        "Independently reviewed the same two source excerpts, distinguishing evidence of the logged value from evidence about instrument calibration."
    )))
    assertion_a2.add((assessment_2, EX.usedEvidence, CSV_EVIDENCE))
    assertion_a2.add((assessment_2, EX.usedEvidence, CAL_EVIDENCE))
    prov_a2.add((graph_a2, PROV.wasDerivedFrom, np_obs))
    prov_a2.add((assessment_2, PROV.wasGeneratedBy, URIRef("https://example.org/ck/activity/review-2")))

    return dataset, [np_obs, np_a1, np_a2]


if __name__ == "__main__":
    dataset, nanopubs = build()
    output = __import__("pathlib").Path(__file__).parent / "drafts.trig"
    dataset.serialize(destination=output, format="trig")
    print(f"Wrote {len(nanopubs)} unsigned nanopublication drafts to {output}")
