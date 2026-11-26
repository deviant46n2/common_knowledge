# Product Development

**Status:** Developer-first product direction proposed; first MVP not yet selected or implemented.

Common Knowledge aims to build **open infrastructure for humanity's shared knowledge**. This directory tracks the first practical software slice: something developers can run, inspect, challenge, and improve, while laying foundations for independent groups to exchange and preserve evidence-linked knowledge.

## First product hypothesis

A small, local-first reference implementation with a developer-friendly workflow (potentially a CLI plus a human-readable inspection view). It should let a contributor create, inspect, validate, and export a knowledge record containing:

- A clearly scoped statement or observation.
- Sources and precise evidence locations.
- Explicit relationships between evidence and the statement.
- One or more attributed assessments, with method and limitations.
- Provenance and revision history.
- A documented, portable export.

Independent assessments should coexist rather than silently overwrite one another. A record should remain inspectable and preservable outside the original application.

This is a working hypothesis, not a selected architecture, schema, language, framework, or storage system. The first implementation should reuse established standards and integrate with existing projects where practical.

## First community

The initial community we hope to attract is open-source developers and technically curious contributors interested in knowledge representation, provenance, interoperability, digital preservation, security, data portability, and public-interest infrastructure.

Developers are the first intended contributors, not the only eventual users. The product must ultimately solve a real task for people who create or examine knowledge. We should test that value rather than assume it from developer interest.

## Product integrity and independence

- Common Knowledge should be infrastructure for independent operators, not the sole authority or required host.
- Reading, validating, exporting, and preserving records should not depend on permission from a central service.
- The format and behavior should be documented well enough for independent implementations.
- Provenance and revision history should make changes attributable.
- Disagreement should remain inspectable; no universal truth score or popularity vote.
- Privacy, rights, consent, and safety constrain what can be published.

The first local prototype need not implement production federation. Independent-instance exchange is an early architecture test.

## Product documents

- [MVP Specification](../docs/MVP_SPECIFICATION.md) — proposed first product, scope, decision gates, and success criteria.
- [Experience principles](EXPERIENCE_AND_VISUAL_IDENTITY.md)
- [Prototype plan](PROTOTYPE_PLAN.md)
- [Prototype status](PROTOTYPE_STATUS.md) — includes the earlier preflight experiment for historical context.

## Related project commitments

- [Roadmap](../ROADMAP.md)
- [Founding Principles](../FOUNDING_PRINCIPLES.md)
- [Transparency](../docs/TRANSPARENCY.md)

No product architecture, data model, hosting model, or software license has been selected. Exploratory record-model and nanopublication work remains a feasibility experiment, not an approved standard or architecture.
