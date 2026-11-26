# Product Direction — Evidence-Linked Knowledge Records

- **Status:** Working hypothesis for focused research and prototyping
- **Date:** 26 November 2026
- **Decision type:** Reversible; not a validated MVP selection

## Product in one sentence

A small, inspectable system for creating, connecting, reviewing, and preserving knowledge records whose statements can be traced to evidence, sources, provenance, uncertainty, and revision history.

## Why this is the current hypothesis

The long-term Common Knowledge vision depends on more than collecting documents or indexing websites. It requires a way to preserve the relationship between what is being said, why it is said, where the supporting material came from, who assessed it, and how the record changes when new evidence appears.

The first demonstrator should test that foundation in a narrow setting.

## Initial user and task hypotheses

Potential early users include people who maintain structured reference knowledge, research evidence syntheses, public-interest data, technical documentation, or carefully sourced explanations.

The first target user and domain are not yet selected. Research and conversations should identify a bounded workflow where evidence traceability and change history solve a real problem.

## Candidate workflow

A person creates or imports a knowledge record, states its scope, attaches one or more sources or observations, identifies how each item relates to the statement (for example supports, challenges, or provides context), and records the reasoning and limitations of an assessment.

Another person can inspect the record, follow the evidence, submit a correction or alternative interpretation, and see the record's history. The record can be exported without requiring access to a Common Knowledge service.

This is an illustrative workflow, not a final schema.

## Product boundaries to investigate

- **Statement and scope:** distinguish a concise statement from its subject, definitions, time period, jurisdiction, population, conditions, and other qualifiers.
- **Evidence and sources:** distinguish a source document from the specific passage, dataset, observation, or result used as evidence.
- **Relationships:** represent support, contradiction, qualification, derivation, and contextual relevance without forcing all evidence into a binary true/false verdict.
- **Provenance:** record who or what created, transformed, reviewed, or changed a record, with enough detail to audit consequential steps.
- **Assessment:** keep methods, reasoning, uncertainty, reviewer perspective, and unresolved disagreement inspectable.
- **History:** preserve versions and corrections; do not silently overwrite a previously published assessment.
- **Interoperability:** reuse existing identifiers, vocabularies, and export formats where they fit.
- **Rights and safety:** track relevant access restrictions and avoid publishing sensitive information simply because it is technically possible.

## Non-goals for the first slice

- Representing all forms of human knowledge.
- Automatically determining truth.
- Replacing scientific journals, libraries, archives, reference works, Wikidata, or specialist databases.
- A universal ontology or exhaustive semantic model.
- A global crawler or ingestion pipeline.
- A centralized social network or reputation system.
- AI agents making authoritative assessments without accountable review.
- Federation, distributed consensus, or large-scale hosting before a concrete need is demonstrated.

## Success criteria to test

The demonstrator is worth continuing if an independent user can:
1. understand what a record asserts and the conditions under which it applies;
2. inspect the sources and the specific evidence connected to it;
3. distinguish source material from the project's interpretation of that material;
4. understand what is uncertain, disputed, or not checked;
5. see who contributed and how the record changed;
6. export the record and its links in a usable, documented form;
7. explain why this workflow is more useful than their current approach.

These criteria are hypotheses for evaluation, not claims that the system can already do these things.

## Decision rule

Do not build a new platform merely because the vision is ambitious. If an existing system already supports the needed workflow, investigate extending it, contributing upstream, or publishing compatible data. Continue with a new implementation only when research and user evidence establish a meaningful gap.
