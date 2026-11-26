# Prototype Status — Earlier Research Preflight Experiment

- **Status:** Historical experiment; not the current Common Knowledge product direction
- **Date:** 26 November 2026
- **Version:** 0.1.0 prototype

## What exists

The repository contains an initial static-inspection prototype under `src/ck_preflight/` and a synthetic computational research project under `examples/synthetic-research-project/`.

The prototype was intended to explore whether a local tool could identify a few handoff issues and present evidence-linked findings.

Implemented in that experiment:
- local project file inventory;
- README presence check;
- relative Markdown link checks;
- a narrow experimental numerical-claim-to-CSV check;
- HTML and JSON report generation;
- a synthetic fixture and unit tests.

## What it does not establish

This experiment is not a knowledge record system, general claim verifier, scientific validity checker, or validated MVP. The numerical matching logic is narrow and should not be treated as a reliable general-purpose verifier.

The recorded test suite had not been run from a clean checkout when this status was last assessed. No independent user validation or evidence of demand was recorded.

## How to run the experiment

From the repository root:

```bash
PYTHONPATH=src python -m ck_preflight examples/synthetic-research-project --output /tmp/ck-preflight-demo
PYTHONPATH=src python -m unittest discover -s tests -v
```

These commands are preserved for anyone wishing to inspect the experiment; their current success has not been reverified as part of the direction change.

## Disposition

Do not extend this prototype merely because it exists. Reuse any code, interface ideas, or test fixtures only if they prove useful to the new knowledge-system work. Preserve it as an experiment and revisit it only when there is a concrete reason.
