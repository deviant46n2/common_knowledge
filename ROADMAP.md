# Roadmap

This roadmap is a practical sequence, not a promise to build every part of the long-term vision. The immediate goal is to create a useful open-source project that developers can run, inspect, challenge, and improve—and that lays credible foundations for independent knowledge infrastructure.

## Direction

**Open infrastructure for humanity's shared knowledge.**

Common Knowledge should help people and independent groups create, inspect, challenge, exchange, and preserve evidence-linked knowledge. It should not become the sole authority, host, or point of failure for the knowledge it helps steward.

The first community we hope to attract is developers and open-source contributors interested in interoperability, provenance, data portability, digital preservation, security, and public-interest infrastructure. The product must give them something concrete to build and test, while remaining useful to people who produce and examine knowledge.

## Near-term sequence

### 1. Align the project and specify the first product — current priority

- Update the project description and roadmap to reflect the developer-first, open-infrastructure direction.
- Define a narrow first product in [MVP Specification](docs/MVP_SPECIFICATION.md).
- Make founder-led status, project decisions, and financial activity transparent from the beginning through [Transparency](docs/TRANSPARENCY.md).
- Keep institutional governance participatory and proportionate: establish present-day commitments, but do not invent a constitution without a community.
- Preserve existing research and prototypes as evidence; do not treat exploratory spikes as selected architecture.

**Output:** a reviewable MVP proposal, clear transparency commitments, and a small set of open technical questions.

### 2. Select one bounded workflow and technical approach

- Choose a real task that developers can understand and that produces a useful evidence-linked record.
- Compare existing formats, standards, and projects before creating new abstractions.
- Decide the minimum record representation, provenance model, evidence anchoring, validation, and export behavior.
- Record the alternatives and trade-offs in a short architecture decision.
- Keep the first implementation local-first and easy to run unless evidence points elsewhere.

**Output:** a tested sample case, a minimal technical design, and explicit reasons for the choices.

### 3. Build a developer-usable vertical slice

The first implementation should let a developer create, inspect, validate, and export a knowledge record. It should demonstrate source references, precise evidence anchors, distinct assessments, attribution, and revision history.

Prioritize:
- Clear setup and contribution instructions.
- A small reference implementation and command-line or equivalent developer workflow.
- Human-readable inspection and machine-readable export.
- Automated tests and a synthetic fixture.
- Honest limitations and no claims of user validation before it occurs.

**Output:** software another developer can run locally and understand without the founder walking them through it.

### 4. Test with independent developers and prospective users

- Invite developers to inspect the code, run the example, challenge the design, and identify architectural mistakes.
- Ask people who work with evidence to try the record workflow when a concrete use case is ready.
- Observe actual friction and compare with existing tools.
- Record negative feedback and revise the product hypothesis.
- Be willing to integrate upstream, narrow the scope, or stop if an existing project already solves the problem better.

**Output:** external feedback and a reasoned decision about the next iteration.

### 5. Demonstrate independent operation and exchange

- Run compatible instances under separate control.
- Exchange, validate, export, import, and preserve records without requiring a privileged central service.
- Test what happens when an operator disappears, disagrees, changes a record, or refuses participation.
- Evaluate identity, signatures, replication, and federation against a documented threat model rather than adding them speculatively.

**Output:** an independently repeatable interoperability demonstration and a clear account of its guarantees and limits.

### 6. Grow the community and institutional safeguards together

- Invite contributors around working software and open technical questions.
- Let people who use and maintain the system help shape contribution processes and governance.
- Develop stronger financial review, conflict management, decision appeals, and independent stewardship as actual resources and responsibilities emerge.
- Support other implementations and communities rather than requiring them to become subordinate to Common Knowledge.

**Output:** community-shaped practices and a growing ecosystem of independent operators.

## Working constraints

- Build on existing standards and projects wherever practical.
- Keep records portable and inspectable outside the reference application.
- Distinguish source content, statements, evidence relations, assessments, and uncertainty.
- Preserve disagreement and correction history.
- Do not equate confidence labels, popularity, or votes with truth.
- Do not make central hosting, central identity, or founder permission prerequisites for independent preservation.
- Protect privacy, consent, security, rights, and community interests.
- Keep the project and its finances transparent without exposing personal or security-sensitive information.
- Make reversible experiments; explain consequential decisions.
- Do not claim independence, decentralization, auditability, or user validation beyond what has actually been demonstrated.

## Not current priorities

A marketing website, global search engine, universal ontology, large-scale ingestion pipeline, token or reputation economy, production federation, AI agent platform, and detailed institutional constitution are not prerequisites for the first developer-usable product.
