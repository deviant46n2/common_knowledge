# Development Documentation System

- **Established:** 26 November 2026
- **Status:** Operating standard for product engineering documentation; apply proportionately to the current prototype and any future MVP.
- **Purpose:** Keep development documentation precise, current, reviewable, and aligned with the actual implementation.

## 1. Core rule

The repository's development documentation is the maintained source of truth for intended product behavior and engineering decisions. The code, tests, schemas, and executable configuration remain the authoritative evidence of what the software actually does.

Documentation must never claim a feature is implemented merely because it appears in a plan or design. Every implementation status must be traceable to code, tests, or a verified demonstration.

## 2. Authority and precedence

When records conflict, use this order:

1. **Observed runtime behavior and current code** establish what the software currently does.
2. **Automated tests and reproducible test fixtures** establish the behaviors currently verified.
3. **Versioned interface definitions and schemas** establish machine-readable contracts.
4. **Accepted architecture and decision records** establish intended design and explain why it was chosen.
5. **Requirements and specifications** establish intended product behavior and acceptance criteria.
6. **User documentation** explains how the current released version is used.
7. **Roadmap and planning documents** describe future intentions and are not evidence of implementation.

A discrepancy between code and documentation is a defect to resolve. Do not silently assume either is correct.

## 3. Required document set after MVP selection

The following structure is proposed. Add documents when the product is selected; do not fill them with invented details now.

    docs/
      development/
        README.md                    # This policy and document index
        PRODUCT_SPEC.md              # User, job, workflows, requirements, non-goals
        REQUIREMENTS.md              # Numbered functional and non-functional requirements
        ARCHITECTURE.md              # Current system architecture and boundaries
        DATA_MODEL.md                # Data structures, schemas, ownership, retention
        SECURITY.md                  # Threat model, trust boundaries, permissions, risks
        PRIVACY.md                   # Data flows, collection, storage, deletion, telemetry
        TEST_STRATEGY.md              # Test layers, fixtures, coverage, acceptance gates
        RELEASE_PROCESS.md            # Versioning, build, release, rollback, support
        STATUS.md                     # Current implemented state, known defects, blockers
        decisions/
          README.md                   # Decision index
          0001-example-template.md    # ADR format example, not an accepted decision
        interfaces/
          README.md                   # API/CLI/file format contracts and version policy
        operations/
          README.md                   # Deployment, maintenance, backups, incident handling

The exact set may be reduced for a small local CLI. Do not create empty ceremony or keep duplicated descriptions in multiple documents.

## 4. Requirements discipline

Use explicit, testable requirements when a product or feature has enough scope that informal acceptance criteria become ambiguous. Stable requirement IDs (for example, REQ-F-001 or REQ-S-001) are useful when multiple people, interfaces, or tests need to refer to the same requirement; they are not mandatory for every small prototype change.

A substantive requirement should state its rationale and source of need, priority, acceptance criteria, verification method, and status. Link it to relevant issues, code, tests, and decision records where useful. Avoid vague terms such as “fast,” “secure,” “user-friendly,” or “reproducible” without a defined scope or measurable meaning.

For the current small prototype, concise issue descriptions and tests may be sufficient. Do not create a formal requirements register until it improves coordination or traceability.

## 5. Architecture decision records

Record consequential technical decisions as individual, append-only ADRs.

Each ADR includes:
- ID and title;
- status (Proposed / Accepted / Superseded / Rejected);
- date;
- context and problem;
- constraints and assumptions;
- options considered, including doing nothing;
- decision;
- positive and negative consequences;
- security, privacy, interoperability, licensing, and maintenance implications;
- evidence and references;
- implementation and migration consequences;
- links to related requirements and code.

Do not rewrite history to make an earlier decision appear inevitable. Supersede an ADR with a new record and explain why.

## 6. Architecture documentation requirements

Architecture documents should describe the current system, not only the desired future system.

For every component or boundary, document:
- purpose and responsibility;
- inputs and outputs;
- dependencies and external services;
- data ownership and trust boundaries;
- failure modes and recovery behavior;
- security and privacy implications;
- observability and audit requirements;
- interfaces and versioning;
- deployment and operational burden.

Use diagrams only when they clarify boundaries or flows. Keep diagram source in the repository and test or review it when architecture changes.

## 7. Change synchronization rules

A code change is not complete until affected documentation is updated.

| Change | Required documentation review |
|---|---|
| New or changed user-visible behavior | Product spec, user docs, requirements, tests, status |
| New module or service | Architecture, interfaces, security/privacy, tests |
| Data model or file format change | Data model, schema/interface docs, migration notes, tests |
| New external API/provider | Architecture, security, privacy, failure behavior, configuration docs |
| New permission or execution capability | Threat model, privacy/data flow, user consent, tests |
| Dependency or runtime change | Build/setup docs, compatibility matrix, release notes |
| Bug fix | Regression test; known issue/status updates if relevant |
| Release | Changelog, release notes, supported versions, verified status |
| Deferred or removed feature | Requirements status, roadmap, user docs, migration/deprecation notes |

The pull request or commit description should identify which documents were reviewed. A documentation update must not be used to conceal an unimplemented feature.

## 8. Status vocabulary

Use these labels consistently:
- **Proposed:** under consideration; not approved.
- **Accepted:** approved design or requirement; not necessarily implemented.
- **In progress:** active implementation work.
- **Implemented:** code exists; not yet fully verified.
- **Verified:** acceptance criteria passed with recorded evidence.
- **Released:** included in a tagged, reproducible release.
- **Deferred:** intentionally postponed.
- **Rejected:** considered and not selected.
- **Superseded:** replaced by a later decision; preserve history.

For a feature, never collapse Implemented, Verified, and Released into one “done” status.

## 9. Testing and evidence

Tests should be connected to requirements and report what they prove.

Distinguish:
- unit tests;
- integration tests;
- end-to-end tests;
- security and privacy tests;
- compatibility tests;
- usability tests with actual users;
- reproducibility tests on clean environments;
- independent verification.

A passing test proves only the behavior it exercises under its conditions. Record environment, versions, fixture provenance, and known limitations for important verification claims.

## 10. Release and maintenance records

For every release, record:
- exact version and source commit;
- build instructions and environment;
- dependency lock state;
- test results and known failures;
- supported platforms;
- data/schema migrations;
- security and privacy changes;
- release artifacts and checksums where appropriate;
- rollback or recovery guidance;
- known limitations and next steps.

Do not claim reproducible builds until they have been tested.

## 11. Keeping records current

- Update status when work changes, not weeks later.
- Prefer one authoritative location per fact; link rather than copy.
- Add dates to research snapshots and records where time matters.
- Mark stale information visibly and schedule re-verification for external dependencies.
- Preserve superseded decisions and released specifications.
- Keep a concise current-state summary for each new development session.
- Use automated checks for links, schemas, documentation structure, and requirement-to-test references when justified by product size.
- Do not allow a roadmap to become a substitute for implementation tracking.

## 12. Current state

A reversible working product direction and an initial static-inspection prototype exist under `product/` and `src/ck_preflight/`. No validated MVP or accepted product architecture has been selected. Product requirements and implementation records must distinguish hypotheses, accepted decisions, implemented behavior, and verified behavior. Apply this documentation system proportionately: the current small prototype does not need a full enterprise-style specification set or formal requirement IDs for every change.

This document is subordinate to the [Common Knowledge Operating Model](../OPERATING_MODEL.md), which defines project-wide standards for evidence, review, safety, decisions, and change. See the [AI Collaboration Protocol](../AI_COLLABORATION.md) for AI-specific authority and conduct, and [Institutional Design](../INSTITUTIONAL_DESIGN.md) for unresolved organizational questions.

## Change log

- **2026-11-26:** Established the proposed documentation system and authority rules before product implementation. No technical architecture decisions were made.
- **2026-11-26:** Updated current-state note to reflect the provisional product direction and initial prototype; added links to AI collaboration and institutional-design guidance.
- **2026-11-26:** Added the project Operating Model as the higher-level standard and clarified that formal requirement IDs should be used only when they improve traceability at the project's current scale.
