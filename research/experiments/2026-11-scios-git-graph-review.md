# SciOS Git-based discourse graph — read-only review

- **Date:** 26 November 2026
- **Repository:** [jring-o/rdf](https://github.com/jring-o/rdf)
- **Status:** Read-only inspection of schema, contribution guide, README, and selected graph nodes
- **No files were changed in the external repository.**

## Purpose

Inspect a real, small, public claim/evidence graph to see how its node model, source references, and contribution workflow work in practice.

## Files inspected

- `SCHEMA.md`
- `CONTRIBUTING.md`
- `README.md`
- `graph/claims/C-0001.md`
- `graph/claims/C-0002.md`
- `graph/evidence/E-0001.md`
- `graph/evidence/E-0002.md`
- `graph/sources/S-0001.md`

The README reports 349 nodes in the current graph. The selected sample nodes are part of a whitepaper argument about research-data preservation.

## What works well

### Small, self-contained nodes

Each Question, Claim, Evidence, Method, and Source is an individual Markdown file with YAML frontmatter and a 50–250 word standalone body. A contributor can understand a node without loading the whole whitepaper. This is an approachable authoring and review format.

### Disagreement is additive

Counterclaims and counter-evidence are new nodes linked with `opposes`; they do not overwrite the original. The contribution guide distinguishes wording/clarity edits from substantive changes that deserve a separate claim. This is a good correction principle.

### The graph is understandable

The five node types (Q/C/E/S/M) and small edge vocabulary (`addresses`, `supports`, `opposes`, `derivedFrom`, `usesMethod`, `informs`) make the graph relatively easy to inspect. The repository includes a linter for schema and edge integrity.

### Contribution is possible without a bespoke platform

A browser form creates a pre-filled pull request; contributors can also edit files directly in Git. Discussions are attached to individual nodes through GitHub issues. The README describes this as a low-friction contribution path.

## Limitations observed in the sample

### Evidence is summarized, not precisely anchored

The inspected evidence nodes contain prose summaries and numeric findings, and link to a Source node. The inspected Source node contains a bibliographic citation, study type, method, and key findings. In the selected sample:
- the source node does not include a DOI or direct URL;
- evidence nodes do not identify an exact quotation, page, table, figure, dataset row, or cell;
- the evidence text paraphrases and interprets the source rather than preserving a passage selector.

This is not a claim that no node anywhere in the repository has a URL or passage anchor; it is what was observed in the selected sample. It shows why Common Knowledge should distinguish a bibliographic reference from the exact source location used as evidence.

### The graph's status field is workflow state

The sample nodes are marked `status: draft`. The repository schema defines `draft`, `review`, and `merged` as contribution lifecycle states. They are not epistemic verdicts or confidence levels. A reader must not interpret "merged" as "true" or "review" as "uncertain."

### The evidence granularity is deliberately pragmatic

The schema allows one Evidence node to contain multiple points from the same source when they are usually cited together. It proposes splitting only when a contributor needs to dispute one sub-point. This keeps the graph manageable, but it means a single evidence node can bundle several measurements or findings.

### Review authority is concentrated in this instance

The contribution guide says every pull request requires approval from a GRAPHOWNER, currently the repository owner. This is understandable for a single research argument graph, but it is not a scalable neutral review process for a general public knowledge service.

## Licensing and provenance

The repository states:
- content is CC BY 4.0;
- code is MIT.

The schema follows the Discourse Graphs Q/C/E/S model and adds Method. Verify the upstream schema's licensing and attribution requirements before reusing the schema itself.

## Implications for Common Knowledge

1. A file-based graph can be a useful first demonstrator; a large graph database is not a prerequisite.
2. Standalone nodes and additive counterclaims are strong human-review patterns.
3. The system needs stronger evidence anchoring than the inspected sample: source version, stable locator, exact quote/data region, and integrity metadata where possible.
4. Contribution status must be separate from evidence assessment and claim status.
5. A single maintainer can launch a small graph, but Common Knowledge's long-term model must support distributed review and correction without giving one person permanent epistemic authority.

## Limitations of this review

This was a small read-only sample, not a full graph audit. We did not run the external linter, inspect every node, test the contribution form, or verify the source claims against the cited papers. The repository's own README says the graph was manually reviewed by one person with LLM assistance; that is a project statement, not an independent evaluation.
