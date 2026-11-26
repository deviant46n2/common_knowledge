# Prototype Plan — Research Project Preflight

- **Status:** Initial execution plan
- **Date:** 26 November 2026
- **Current stage:** Fixture and baseline validation, before product implementation

## Guiding rule

Build one complete and inspectable workflow, not a broad feature set. The first deliverable is a trustworthy local inspection report for a deliberately small class of computational research projects.

## Stage 0 — Establish the ground-truth fixture

Create a small, openly licensed synthetic Python research project. It must be safe to inspect and must not require network access or execution of untrusted code.

The fixture should contain:
- a short research question and method;
- a tiny synthetic dataset with documented origin and units;
- source code and declared dependencies;
- a README with run instructions;
- a test suite;
- two recorded example runs with distinct identifiers;
- output tables and a short report with explicit numerical claims;
- citation and license metadata where appropriate;
- a deliberately incomplete variant and a set of known defects.

Known conditions should include a missing dependency declaration or environment detail, a missing referenced artifact, stale or ambiguous run information, incomplete citation or license information, and at least one well-documented condition that should *not* be flagged. Avoid defects that require executing arbitrary code to detect.

**Deliverable:** fixture specification, fixture repository contents, and a ground-truth ledger mapping each condition to expected observations.

## Stage 1 — Baseline existing tools

Use official documentation and safe, disposable environments to test only the relevant tools against the fixture. Initial candidates include:
- roc-validator;
- ro-crate-py and applicable RO-Crate tooling;
- ReproCert;
- reproducible-science;
- runcrate or workflow-specific tools only where the fixture format is supported.

Do not force tools onto inputs they do not claim to support. Record unsupported cases rather than treating them as failures.

For each test record exact versions, commands, environment, inputs, outputs, limitations, installation friction, and whether results can be independently inspected. Never execute arbitrary research repositories on the host.

**Deliverable:** baseline comparison showing which needs are already met and which remain unmet.

## Stage 2 — Define the smallest valuable workflow

Use fixture results to decide the first supported checks. Each check must:
- answer a real handoff question;
- have a deterministic, testable basis;
- point to evidence;
- explain its limits;
- avoid duplicating a mature tool without a clear reason.

**Deliverable:** requirements specification and explicit non-goals.

## Stage 3 — Implement one vertical slice

Provisional interface:
- local command-line entry point;
- local project directory as input;
- static inspection only;
- deterministic finding records;
- readable HTML report plus machine-readable JSON report;
- bundled example and golden expected output.

A command-line plus HTML-report approach is a provisional implementation choice because it can be distributed and demonstrated without hosting a service. Revisit only if hands-on work shows it is unsuitable for the target user.

No code execution, file modification, telemetry, account, or network requirement in this stage.

**Deliverable:** one working end-to-end path from project directory to evidence-linked report.

## Stage 4 — Independent evaluation

Ask people who did not build the tool to:
- install it using only the instructions;
- run the bundled example;
- explain selected findings in their own words;
- identify whether a finding is actionable and accurate;
- compare the report with their existing workflow;
- report confusing, missing, or misleading results.

Record task completion, setup friction, false positives, false negatives against the fixture, comprehension, and whether users would use the workflow again.

Do not describe the product as validated based only on internal tests or friendly reactions.

## Acceptance gate for a public alpha

A public alpha is appropriate only when:
- the supported input scope is explicit;
- all advertised checks have automated tests;
- fixture ground truth is versioned;
- findings cite evidence locations;
- the report says what was not checked;
- no project code is executed;
- no project files are changed;
- installation and example instructions work on a clean environment;
- known limitations and security boundaries are documented;
- the project license and third-party notices have been reviewed and explicitly decided.

## Stop / change-direction conditions

Stop or change direction if:
- existing tools already solve the target workflow with comparable usability;
- the product's value reduces to presenting a checklist or relaying tool output;
- the initial target user cannot be reached or does not experience the problem;
- accurate findings require unsafe execution or invasive access not justified by user value;
- the tool cannot distinguish missing evidence from evidence of absence;
- maintenance burden is disproportionate to the demonstrated benefit.

A negative result is useful research. Do not preserve the product hypothesis at the expense of Common Knowledge's mission.
