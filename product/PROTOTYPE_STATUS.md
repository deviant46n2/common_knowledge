# Prototype Status

- **Version:** 0.1.0 prototype
- **Date:** 26 November 2026
- **Status:** Initial static-inspection slice implemented; experimental and not user-validated

## Implemented

- Local project file inventory, excluding common environment and version-control directories.
- Conventional README presence check.
- Relative Markdown link checks for missing local files.
- Experimental narrow check for a bold numerical difference claim linked to a CSV result table with `metric,value,unit` columns.
- HTML and JSON report generation.
- Explicit inspection limits and no-execution statement.
- Synthetic fixture and unit tests.

## Not implemented

- General-purpose research project readiness assessment.
- Broad claim extraction or semantic interpretation.
- Runtime environment or dependency validation.
- RO-Crate generation or validation.
- Integration with external validators.
- Notebook, workflow, or source-code execution.
- User testing or evidence of demand.

## Important limitations

The numerical claim check recognizes only a narrow, explicit Markdown pattern and one CSV metric convention. It is an experiment to test evidence-linking behavior, not a general claim verifier. A result mismatch is a prompt for human review, not proof that the report or result is wrong.

The tool does not execute inspected code, contact network services, modify source project files, or establish scientific validity.

## Run locally from the repository root

```bash
PYTHONPATH=src python -m ck_preflight examples/synthetic-research-project --output /tmp/ck-preflight-demo
```

Run tests:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The automated test suite has been authored but has not yet been executed from a clean checkout. The fixture analysis calculation was independently checked to produce 10.0 mm, 13.0 mm, and a 3.0 mm difference; the narrow claim-matching expression was separately checked against the fixture's report sentence. Full package/runtime testing remains outstanding.

The prototype is not ready to be described as a validated MVP or public alpha.
