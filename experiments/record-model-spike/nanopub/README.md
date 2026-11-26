# Nanopublication mapping spike

**Status:** Local unsigned draft only. Nothing in this directory has been signed or published.

This maps the synthetic R-1 case into three nanopublications:
1. Observation: the station's recorded value, scope, two Web Annotation evidence anchors, and separate support/qualification relationships.
2. Assessment 1: a first assessment derived from the observation nanopublication.
3. Assessment 2: an independent assessment, also derived from the observation nanopublication rather than overwriting assessment 1.

Each draft has the four named graphs required by the nanopublication guidelines: head, assertion, provenance, and publication information. The provenance graph refers to its assertion graph; the publication-info graph refers to the nanopublication. Tests check these minimum structural requirements and the source quote anchors.

## Run

From this directory, run: python build_drafts.py
Then run: python -m pytest -q

The builder requires Python 3.11+ and rdflib. Seven tests pass.

## What this demonstrates

Nanopublications naturally support small, immutable contributions. A statement can be published once; multiple assessments can then be separate nanopublications that cite or derive from the statement. A reader or application can aggregate them into a shared view without mutating the original publication or forcing one assessment to replace another.

This is a different revision model from the JSON-LD record experiment: the JSON-LD spike represented version 2 as a new record entity that references two assessments, whereas this spike represents each assessment as its own publication. The aggregation/current-view rules are left to the consuming application or a shared query/view convention.

## Limitations

- The identifiers use example.org and are placeholders, not Trusty URIs.
- These drafts are unsigned. They have not been checked by nanopub-py or nanopub-java, signed, or published.
- The tests check the minimum four-graph structure from the published guidelines and a few expected domain relationships. They are not a full nanopublication validator.
- No key/profile was created; no ORCID identity was used.
- No content was sent to either test or production network.
- A full workflow still needs to test template-based authoring, signatures, retrieval, query behaviour, supersession/retraction, and what the reader sees when several assessments coexist.