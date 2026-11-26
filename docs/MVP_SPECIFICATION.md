# MVP Specification

**Status:** Working proposal for review; not an approved architecture or release commitment.  
**Purpose:** Turn the current project direction into a small, testable developer-facing product.

## Product statement

Common Knowledge is exploring **open infrastructure for humanity's shared knowledge**: tools and standards that let people and independent groups create, inspect, challenge, exchange, and preserve evidence-linked knowledge without depending on one platform or institution.

The first product should give open-source developers something real to run, inspect, test, and improve. It should also create a credible foundation for later use by researchers, journalists, libraries, and public-interest organizations.

## The first problem

Knowledge records are difficult to reuse when their meaning, evidence, origin, revision history, and disagreements are trapped in a particular application or controlled by one operator.

We want to test whether a small, portable record workflow can make those elements independently inspectable and exchangeable.

This is a problem hypothesis, not a claim that existing projects cannot do it. The implementation should reuse established standards and integrate with adjacent projects wherever that is better than creating new infrastructure.

## Initial users

**Primary: open-source developers and technically curious contributors** interested in knowledge representation, provenance, data portability, digital preservation, interoperability, security, and public-interest infrastructure.

**Secondary: people who create or examine evidence-linked records**, including researchers, fact-checkers, librarians, archivists, and public-interest research groups. Their real workflows should shape the first use case; we should not assume developer enthusiasm alone validates end-user value.

## Proposed first product

A small, local-first reference implementation with a developer-friendly interface (likely a CLI plus a simple human-readable inspection view). The precise language, framework, storage engine, and serialization format remain open pending a focused technical decision.

A contributor should be able to:

1. Create a knowledge record with a clearly scoped statement or observation.
2. Attach source references and precise evidence locations.
3. describe how each evidence item relates to the statement (for example supports, challenges, qualifies, or contextualizes).
4. Add an attributed assessment that explains its method, conclusion, and limitations.
5. Add a separate assessment without overwriting the original record or another contributor's assessment.
6. Inspect provenance and revision history.
7. Validate and export the record in a documented, portable format.
8. Re-import an export and recover the same meaningful content.

The product should include a small synthetic example and, once a suitable case is selected, one real bounded example using material that can responsibly be reused.

## What the first demonstrator must prove

- **Legibility:** A person can understand what a record asserts and what it does not assert.
- **Evidence traceability:** Evidence links lead to identifiable source material and a specific location or selection.
- **Provenance:** The origin of records, assessments, and revisions is inspectable.
- **Contestability:** Independent assessments can coexist; disagreement is not silently overwritten or reduced to a popularity vote.
- **Portability:** Records can be exported, inspected outside the application, and re-imported.
- **Developer usability:** A new developer can install or run the project, create or inspect the example, run tests, and understand where to contribute.

## Independence as a design constraint

The first release does not need production federation. It must, however, avoid choices that make central control inevitable.

- Do not make a Common Knowledge-hosted service the only place records can exist.
- Do not require central permission to read, export, validate, or preserve a record.
- Keep the record format documented and implementation-independent.
- Preserve original contributions and make changes attributable.
- Make it feasible for another operator to run compatible software independently.
- Treat independent exchange between two separately controlled instances as an early architecture test, not a prerequisite for the first local prototype.

A future network should be plural: multiple operators and communities can maintain compatible infrastructure, challenge one another's records, and preserve independent copies. Common Knowledge itself should not become the sole authority or point of failure.

## Transparency and project practice

The development process should model the values the software is intended to support:

- Public issues, design discussions, roadmap changes, and decision rationales.
- Clear labels distinguishing proposals, implemented behavior, tested behavior, user-tested behavior, and released software.
- Public disclosure of project funding, project spending, and compensation paid from project funds, with privacy and security protections.
- Founder disclosures about relevant conflicts of interest, material commitments, and significant changes in direction.
- Corrections and failed experiments recorded rather than hidden.

See [Transparency](TRANSPARENCY.md). These are practices to begin now, not claims that independent oversight, audits, or formal governance already exist.

## Explicitly out of scope for the first MVP

- A universal ontology or claim vocabulary.
- A global knowledge graph, search engine, or ingestion pipeline.
- A social network, token, reputation score, or vote-based truth mechanism.
- A centralized account or identity authority.
- Production-grade federation, distributed consensus, or a global registry.
- A complete legal structure, constitution, membership system, or governance platform.
- AI agents with authority to publish or adjudicate knowledge autonomously.
- A public marketing website as a substitute for working software.

Security, privacy, rights, and safety are not out of scope. They must inform what examples and data we use, even if a complete operational security program is beyond the prototype.

## Technical decision gates

Before selecting a stack or final record format, compare the smallest plausible options against:

- Existing standards and adjacent projects identified in the research.
- Human readability and machine processability.
- Stable identifiers and source/evidence anchoring.
- Provenance and revision semantics.
- Portability, export, and re-import.
- Ease of local operation and contribution.
- Testability and long-term maintainability.
- Ability to support independent implementations.

Do not create a new standard merely because it is convenient for the first implementation. If a new extension is necessary, document the gap, alternatives, compatibility strategy, and migration risk.

## Success criteria

The first MVP is worth building upon when:

1. A developer unfamiliar with the code can follow the setup instructions and run the example.
2. The example clearly distinguishes a source's content, the statement being made, evidence relations, and an assessor's interpretation.
3. Two distinct assessments can be added and inspected without overwriting one another.
4. Automated tests verify the documented record and export behavior.
5. An exported record can be inspected without the original application and successfully re-imported.
6. A second independently run instance can, in a later integration test, import and validate the same record without contacting a privileged central service.
7. At least a few people outside the founding effort can try it and give concrete feedback. Their experience—not internal enthusiasm—determines whether to continue, narrow, integrate upstream, or stop.

Passing these criteria would validate a demonstrator, not prove institutional trustworthiness or broad user demand.

## Immediate work sequence

1. Review this specification and resolve its open assumptions.
2. Choose one bounded real-world workflow and sample case.
3. Compare candidate record representations and implementation approaches against the decision gates.
4. Write a short architecture decision with alternatives and trade-offs.
5. Implement the smallest complete local workflow with tests and documentation.
6. Test it with developers outside the project.
7. Use those results to prioritize independent-instance exchange and the next release.

## Open questions

- Which recurring developer task should the first tool make easier: authoring, validation, inspection, conversion, or exchange?
- Which real-world example can be used without rights, privacy, or safety complications?
- Which existing format or project can we extend or interoperate with rather than compete with?
- What is the minimum identity/provenance model that is useful without creating a central identity authority?
- Which integrity guarantees are needed for the first prototype, and which require a later threat model?
