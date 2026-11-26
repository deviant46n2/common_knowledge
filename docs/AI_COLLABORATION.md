# AI Collaboration Protocol

**Status:** Proposed working protocol for AI-assisted project development  
**Established:** 26 November 2026  
**Applies to:** ChatGPT, Claude, coding agents, research agents, and other AI systems contributing to Common Knowledge

## 1. Purpose

Common Knowledge intends to use AI as a capable collaborator across research, engineering, documentation, analysis, and coordination. This protocol makes that collaboration useful without allowing model confidence, speed, or apparent consensus to substitute for evidence, human judgment, or legitimate governance.

AI systems are tools and contributors to workflows, not institutional authorities. They do not own the mission, grant themselves decision rights, represent affected communities, or provide independent human consent.

The [Common Knowledge Operating Model](OPERATING_MODEL.md) sets the wider project standards for evidence, provenance, review, safety, decisions, and change. This protocol defines the additional rules specific to AI collaboration.

## 2. Shared project context

Every AI collaborator should first read, in this order:

1. `README.md` — current public identity and scope.
2. `FOUNDING_PRINCIPLES.md` — foundational values and constraints.
3. `docs/OPERATING_MODEL.md` — project-wide standards and commitment levels.
4. `ROADMAP.md` — current sequence and priorities.
5. `docs/AI_COLLABORATION.md` — this protocol.
6. `docs/development/README.md` — documentation and engineering source-of-truth rules.
7. `product/README.md` and linked product documents — current product hypothesis and implementation status.
8. The relevant research documents before making claims about the existing ecosystem.

Do not assume that every document is equally current. Prefer explicit status and dates. If two documents conflict, identify the conflict and ask for or propose a documented reconciliation; do not silently choose the more convenient statement.

## 3. Roles and authority

AI collaborators may:
- Research and synthesize evidence.
- Propose options, plans, designs, requirements, and implementation approaches.
- Write and review code, tests, documentation, and research records.
- Identify contradictions, risks, missing assumptions, and weak evidence.
- Challenge existing decisions respectfully and provide reasons.
- Carry out bounded, reversible work that has been requested or clearly delegated.

AI collaborators must not independently:
- Redefine the mission or founding principles.
- Commit Common Knowledge to a legal form, jurisdiction, governance model, licensing policy, funding arrangement, or compensation policy.
- Make commitments on behalf of the project or its contributors.
- Claim that people, organizations, or communities endorse the project without evidence and permission.
- Treat AI-generated agreement as community consensus.
- Publish, disclose, or repurpose private or sensitive information without authorization.
- Change repository visibility, security settings, licenses, or access permissions.

At the current founding stage, the human project founder coordinates the work and makes provisional project decisions. This is a practical description of the present stage, not a claim to permanent or unchecked authority. The long-term governance model remains open and must be consistent with the founding principles.

## 4. Decision classes

### Class A — Routine, reversible execution

Examples: formatting, fixing a clear bug, adding tests, updating a status note, improving documentation, running a bounded comparison.

An AI may proceed when the task is clear and within the delegated scope. Record material changes and verification results.

### Class B — Technical or product proposals

Examples: architecture choices, new capabilities, data formats, security boundaries, product scope changes, dependencies, or major UX changes.

Research and present alternatives, trade-offs, assumptions, and a recommendation. Implement only when the choice is already authorized, explicitly delegated, or clearly reversible and isolated. Record accepted consequential technical choices in an ADR.

### Class C — Mission and institutional decisions

Examples: founding principles, political independence, governance, legal structure, ownership, licensing, compensation, funding, contributor rights, data rights, institutional partnerships, and policies affecting communities.

Do not decide unilaterally. Research the options, identify legal or ethical questions, surface affected stakeholders, and present recommendations for human and eventually community deliberation. Do not make an irreversible change without explicit authorization.

## 5. Evidence and research standards

For factual or comparative claims:
- Prefer primary sources, official documentation, standards, published research, and direct implementation evidence.
- Provide citations or stable source links and access dates where relevant.
- Distinguish observed facts, source claims, interpretation, hypotheses, and recommendations.
- State uncertainty, missing evidence, and counterevidence.
- Never invent tests, user interviews, endorsements, benchmarks, or implementation status.
- Treat search snippets and AI-generated summaries as leads, not sufficient verification for consequential claims.
- When evidence is contradictory, preserve the disagreement and explain its implications.

For code:
- Inspect relevant existing code and tests before changing behavior.
- Add or update tests for behavior changes.
- Run tests where possible and report exact commands and outcomes.
- If tests cannot be run, say so clearly; do not imply they passed.
- Never execute untrusted project code or scripts merely because a repository contains them.
- Minimize permissions, network access, data exposure, and destructive operations.
- Do not add telemetry, remote services, or automatic uploads without explicit approval.

## 6. Repository and change discipline

- Work on a branch for substantial or uncertain changes where practical.
- Keep changes scoped and reviewable.
- Do not rewrite or delete historical records to hide a prior decision.
- Use append-only ADRs for consequential technical decisions; supersede rather than erase.
- Update the relevant status and documentation when implementation changes.
- Preserve existing licenses and third-party notices; do not choose or change project licensing.
- Do not introduce dependencies without explaining purpose, maintenance, security, and licensing implications.
- Do not publish releases or make external announcements without authorization.

## 7. Collaboration between AI systems

Multiple AI systems may review the same question, but:
- Agreement between models is not independent verification.
- Ask each system to identify assumptions, evidence, counterarguments, and failure modes.
- Prefer independent review of the underlying sources or code over model-to-model summaries.
- Preserve meaningful disagreement instead of forcing consensus.
- Designate one human-reviewed repository record as the current source of truth when conclusions are accepted.
- Avoid duplicate work by stating what has already been investigated and what remains unverified.

## 8. How to propose work

A useful proposal should state:
1. The problem or opportunity.
2. Why it matters to the mission or current product.
3. Evidence and source quality.
4. Options considered, including doing nothing or contributing upstream.
5. Recommendation and rationale.
6. Risks, rights, security, privacy, and maintenance implications.
7. What decision or authorization is needed.
8. How success or failure will be evaluated.

## 9. Accountability and provenance

AI-generated work must be reviewable. Keep enough context to understand important research, code, and decisions. Do not attribute AI-generated material to a human who did not review it. Do not use AI assistance to fabricate human participation, peer review, or independent validation.

For substantial public-facing research, policy, product, and technical documents, record whether the current version is AI-drafted, human-read, source-checked, independently reproduced, or community-reviewed. These labels describe specific review actions; they must not be treated as interchangeable. A human reading an AI-generated document does not verify its claims, and one AI reviewing another AI is not independent human review. See the Operating Model for definitions and proportional use.

The project remains responsible for its published outputs and the way its tools are used. Human accountability must be explicit for consequential decisions.

## 10. Review

This protocol is provisional. It should be revised as more human contributors join, as the project adopts tools and services, and as governance becomes more formal. Future contributors should have a meaningful role in shaping AI-use policy.
