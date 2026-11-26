# Local record tool — developer preview

**Status:** Experimental implementation on a development branch. The record format is provisional, not a Common Knowledge standard.

This is the first runnable slice of the developer-facing product hypothesis. It uses Python's standard library and a small JSON record to test a narrow workflow before selecting a permanent data model or stack.

## Run

From the repository root:

```bash
PYTHONPATH=src python -m ck_records --help
PYTHONPATH=src python -m ck_records init /tmp/new-record \
  --id urn:ck:example:new-record \
  --title "A new record" \
  --statement "The statement being documented." \
  --scope "The exact limits of what this statement claims."
PYTHONPATH=src python -m ck_records add-source /tmp/new-record/record.json \
  --id primary-source --title "Primary source" --file ./source.txt
PYTHONPATH=src python -m ck_records add-evidence /tmp/new-record/record.json \
  --id evidence-1 --source-id primary-source --relation supports \
  --exact "Exact text copied from the source"
PYTHONPATH=src python -m ck_records add-assessment /tmp/new-record/record.json \
  --id assessment-1 --author "Reviewer" \
  --conclusion "What the evidence supports and does not support." \
  --method "Describe the review method." --evidence-id evidence-1
PYTHONPATH=src python -m ck_records validate examples/records/r1/record.json
PYTHONPATH=src python -m ck_records inspect examples/records/r1/record.json
PYTHONPATH=src python -m ck_records export examples/records/r1/record.json /tmp/r1-package
PYTHONPATH=src python -m ck_records import /tmp/r1-package/record.json /tmp/r1-imported-package
```

The example is synthetic. Local source files are included so validation can check exact quotations and their prefix/suffix context. Source paths are restricted to the record directory.

## Create a record

`init` creates a new workspace containing `record.json` and an empty `sources/` directory. It requires an identifier, title, statement, and scope. Add source files under `sources/`, then edit the record to add source entries, evidence anchors, and assessments. Initialization refuses to overwrite an existing directory.

Use `add-source` to copy a source file into the workspace and register it. Use `add-evidence` to attach an exact text passage to a registered source with a typed relationship. Use `add-assessment` to add an attributed assessment that references one or more evidence anchors. Each command validates the resulting record before writing it; a rejected evidence anchor leaves the record unchanged.

## Current checks

- Create a valid empty starter workspace.
- Add source files and register them in the record.
- Add exact evidence anchors with typed relationships.
- Add attributed assessments linked to evidence.
- Format name/version and required fields.
- Unique IDs and valid references.
- Typed evidence relationships: supports, challenges, qualifies, contextualizes.
- Local source files and exact quote/context matching.
- Deterministic JSON export.
- Local import/export of the record document.

## What validation does not establish

A passing result does **not** establish source authenticity, representativeness, whether evidence supports a conclusion, assessment quality, or truth. It does not yet provide signatures, cryptographic integrity, remote sources, revision history, collaborative editing, source-file packaging, or federation.

Import/export currently copies one JSON document; keep the record directory and its relative source files together when moving the example. These limitations are intentional. This is a prototype to learn from, not a production tool or selected architecture.

## Tests

Run with `PYTHONPATH=src python -m pytest -q tests/test_ck_records.py`. The implementation has no runtime dependencies beyond Python 3.11; pytest is needed only for tests.
