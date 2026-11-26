# Knowledge record model spike

**Status:** Disposable experiment, not a selected schema or production prototype.

This tests whether a small JSON-LD graph can distinguish a statement about what a source recorded, precise evidence passages, typed evidence relationships, and a separate assessment with provenance.

The synthetic case uses a fictional monitoring station R-1. Its CSV row records dissolved oxygen of 4.2 mg/L at 09:00 UTC on 1 May 2026. A separate calibration log says the sensor was overdue. The first source supports what the station recorded; the second qualifies confidence in measurement accuracy. They are not contradictory.

All source files are fictional fixtures.

## Files

- `record.jsonld`: JSON-LD using PROV-O and Web Annotation terms plus a provisional example vocabulary.
- `sources/`: the source fixtures targeted by quote selectors.
- `test_record.py`: smoke tests for parsing, evidence relations, provenance, exact quote matching, independent assessments, version history, and reader output.
- `render_record.py`: creates a local static HTML page for inspecting the record.
- `nanopub/`: builds three unsigned nanopublication drafts (one observation and two separate assessments) and tests their four-graph structure.

## Run

Requires Python 3.11+, rdflib, and pytest:

```bash
python -m pip install rdflib pytest
python -m pytest -q
python render_record.py
cd nanopub && python build_drafts.py && python -m pytest -q
```

Eight record-model tests and seven nanopublication-structure tests pass (15 total). The nanopublication spike represents the observation and each independent assessment as separate four-graph drafts. The assessment publications derive from the observation publication, so neither assessment overwrites the other. The fixture now includes two independent assessments of the same statement and a version 2 record that retains both assessments while linking back to version 1 with PROV-O wasRevisionOf. An earlier test run exposed a missing JSON-LD mapping for `oa:hasTarget`; the compact-IRI version in this experiment avoids that aliasing mistake. This demonstrates why semantic round-trip tests matter in addition to JSON syntax validation.

## Limitations

- `https://example.org/ck/` identifiers are placeholders, not production identifiers.
- The `ex:` vocabulary and relation labels are provisional.
- Passing tests establish graph structure and selector matching only, not truth, source authenticity, or assessment quality.
- This does not test SHACL, Wikibase, nanopublication signing or publication to the test network, interactive authoring, a complete correction workflow, or non-specialist usability.
- Selectors are checked against exact fixture text. Real sources need version capture, normalization, and recovery behaviour when content changes.
- No real or external content is included or published.

The static reader is intentionally basic; it is a first inspectability test, not a polished user interface. The nanopublication drafts are unsigned and unpublished; the test network was inspected read-only, but no external publication has been made. The next step is to validate the draft with the official library or CLI and then, with explicit approval, publish only to the isolated test registry.
