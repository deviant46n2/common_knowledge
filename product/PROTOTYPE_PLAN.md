# Prototype Plan — Knowledge-System Vertical Slice

- **Status:** Proposed sequence; research must inform the actual implementation
- **Date:** 26 November 2026

## Guiding rule

Build one complete workflow that a person can use and inspect. Do not build a miniature universal knowledge platform.

## Stage 1 — Understand existing building blocks

Compare a small set of relevant systems and standards against the capabilities required by the candidate workflow:

- structured statements and qualifiers;
- evidence-to-statement relationships;
- source identity and precise evidence locations;
- attribution and provenance;
- uncertainty, disagreement, and correction;
- version history and stable identifiers;
- machine-readable export and independent reuse.

Begin with Wikibase/Wikidata, nanopublications, W3C PROV-O, RDF, and relevant research-knowledge services. Add candidates only when they illuminate a specific requirement. Read primary specifications and test real software rather than relying on feature summaries.

**Deliverable:** a compact comparison and a list of capabilities to reuse, gaps to investigate, and unnecessary complexity to avoid.

## Stage 2 — Select one bounded workflow

Use the comparison and early conversations to choose a domain and user task small enough to represent end-to-end. Prefer a workflow with public, rights-cleared source material and a way to independently check the record.

Do not select a politically charged example just for attention. The first example should make the system's evidence and revision behavior easy to evaluate.

**Deliverable:** one example domain, one user task, and a small set of records with known source material.

## Stage 3 — Define the minimum record

Specify only fields required by the chosen workflow. At minimum, test whether the record needs:
- a stable identifier and version;
- a statement and explicit scope;
- links to sources and precise evidence locations;
- typed relationships between evidence and statement;
- attribution/provenance for creation and review;
- assessment reasoning and uncertainty;
- correction and supersession history;
- rights/access metadata where relevant.

This is a research checklist, not a predetermined schema. Reuse standards and existing data models where possible.

**Deliverable:** a small sample dataset and an export format that another tool can parse.

## Stage 4 — Implement the vertical slice

Possible interface: a local or lightweight web application that can create, inspect, and export the chosen records. Choose the simplest implementation after the workflow and existing tools are understood.

The first slice should not require user accounts, public hosting, telemetry, remote AI services, or distributed infrastructure unless the chosen task demonstrably requires them.

**Deliverable:** one working path from source material to a readable, inspectable, exportable record.

## Stage 5 — Independent evaluation

Ask people who did not build the prototype to:
- create or inspect a record using only the instructions;
- trace a statement to the relevant source passage or data;
- explain the difference between evidence and assessment;
- identify what remains uncertain or disputed;
- inspect a correction or prior version;
- export and reuse the record;
- compare the workflow with tools they already use.

Record setup friction, task completion, errors, comprehension, missing needs, and whether the workflow is worth using again.

## Stop or change direction

Stop building a new application if an existing system already supports the target workflow adequately. Consider contributing upstream, building an adapter, publishing compatible records, or choosing a different problem. A negative result is useful.
