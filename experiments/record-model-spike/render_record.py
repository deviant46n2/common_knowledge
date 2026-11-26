"""Render the synthetic JSON-LD knowledge record as a static HTML inspection page."""
from __future__ import annotations

import argparse
from html import escape
from pathlib import Path

from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF

ROOT = Path(__file__).parent
EX = Namespace("https://example.org/ck/vocab/")
OA = Namespace("http://www.w3.org/ns/oa#")
PROV = Namespace("http://www.w3.org/ns/prov#")
DCTERMS = Namespace("http://purl.org/dc/terms/")


def one(graph: Graph, subject, predicate, default="") -> str:
    values = list(graph.objects(subject, predicate))
    return str(values[0]) if values else default


def render(source: Path = ROOT / "record.jsonld") -> str:
    graph = Graph()
    graph.parse(source, format="json-ld")
    statement = URIRef("https://example.org/ck/statement/r1")
    text = one(graph, statement, EX.statementText)
    scope = one(graph, statement, EX.scope)

    evidence_sections = []
    for relation in sorted(graph.subjects(RDF.type, EX.EvidenceRelation), key=str):
        relation_label = one(graph, relation, EX.relationType).replace("_", " ").capitalize()
        evidence = URIRef(one(graph, relation, EX.evidenceItem))
        target = next(graph.objects(evidence, OA.hasTarget))
        source_id = next(graph.objects(target, OA.hasSource))
        selector = next(graph.objects(target, OA.hasSelector))
        quote = one(graph, selector, OA.exact)
        source_title = one(graph, source_id, DCTERMS.title)
        source_path = "station-r1.csv" if source_id.endswith("/csv") else "station-r1-calibration.txt"
        evidence_sections.append(f"""<section class="evidence">
          <p class="relation">{escape(relation_label)}</p>
          <blockquote>{escape(quote)}</blockquote>
          <p class="source">Source: <a href="sources/{escape(source_path)}">{escape(source_title)}</a></p>
        </section>""")

    assessment_sections = []
    for assessment in sorted(graph.subjects(RDF.type, EX.Assessment), key=str):
        conclusion = one(graph, assessment, EX.conclusion)
        method = one(graph, assessment, EX.method)
        activity = URIRef(one(graph, assessment, PROV.wasGeneratedBy))
        agent = next(graph.objects(activity, PROV.wasAssociatedWith))
        agent_description = one(graph, agent, DCTERMS.description)
        reviewer_number = "2" if str(agent).endswith("reviewer-2") else "1"
        assessment_sections.append(f"""<section class="assessment">
          <h3>Independent assessment {reviewer_number}</h3>
          <p>{escape(conclusion)}</p>
          <details><summary>Review method and provenance</summary>
            <p><strong>Method:</strong> {escape(method)}</p>
            <p><strong>Reviewer:</strong> {escape(agent_description)}</p>
          </details>
        </section>""")

    versions = []
    for version in sorted(graph.subjects(RDF.type, EX.KnowledgeRecord), key=str):
        version_id = str(version).rsplit("/", 1)[-1]
        assessment_count = len(list(graph.objects(version, EX.hasAssessment)))
        previous = one(graph, version, PROV.wasRevisionOf)
        relation = "Initial version" if not previous else "Revises version 1"
        versions.append(f"<li><strong>{escape(version_id)}</strong> — {escape(relation)}; {assessment_count} assessment(s)</li>")

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Common Knowledge — Record inspection</title>
<style>
:root {{ color-scheme: light; font-family: system-ui, sans-serif; color: #20252b; background: #f5f6f7; }}
body {{ max-width: 900px; margin: 2rem auto; padding: 0 1rem 3rem; line-height: 1.55; }}
header, main, footer {{ background: white; border: 1px solid #d9dde1; border-radius: 12px; padding: 1.25rem; margin: 1rem 0; }}
h1 {{ margin-top: .25rem; font-size: 1.65rem; }} h2 {{ margin-top: 0; font-size: 1.2rem; }}
.kicker, .relation {{ color: #45515d; font-size: .82rem; font-weight: 700; text-transform: uppercase; letter-spacing: .04em; }}
.evidence, .assessment {{ border-top: 1px solid #e3e6e9; padding: 1rem 0; }}
blockquote {{ margin: .6rem 0; padding: .7rem 1rem; background: #f1f3f5; border-left: 3px solid #77838f; }}
.source, footer {{ color: #59636e; font-size: .9rem; }}
a {{ color: #145a91; }} details {{ margin-top: .75rem; }}
.notice {{ border-left: 4px solid #b47a22; padding-left: .8rem; }}
</style>
</head>
<body>
<header>
  <p class="kicker">Common Knowledge · Experimental record</p>
  <h1>Dissolved oxygen observation at station R-1</h1>
  <p><strong>{escape(text)}</strong></p>
  <p class="notice">Scope: {escape(scope)}</p>
</header>
<main>
  <h2>Evidence and its relationship to the statement</h2>
  {''.join(evidence_sections)}
</main>
<main>
  <h2>Assessments</h2>
  <p>These are separate interpretations, not a single automated truth score.</p>
  {''.join(assessment_sections)}
</main>
<main>
  <h2>Record history</h2>
  <ol>{''.join(versions)}</ol>
</main>
<footer>
  Synthetic example only. All records, source material, and reviewer identities are fictional. The example.org identifiers and experimental vocabulary are placeholders. This page demonstrates inspectability, not truth or scientific validation.
</footer>
</body>
</html>"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "record.html")
    args = parser.parse_args()
    args.output.write_text(render(), encoding="utf-8")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
