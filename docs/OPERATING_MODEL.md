# Common Knowledge Operating Model

**Status:** Proposed operating standard; not a constitution or legal policy  
**Version:** 0.1  
**Proposed:** 26 November 2026  
**Owner:** Founding project steward, pending development of shared governance  
**Review trigger:** Before the first external contribution, public software release, funding acceptance, collection of sensitive data, or other material change in project responsibilities  
**Provenance:** AI-assisted draft; founder review pending

## 1. Purpose

This document describes how Common Knowledge works while it is being established. It is intended to make the project understandable, reviewable, safe to contribute to, and capable of changing its mind when evidence warrants it.

The goal is dependable practice, not bureaucracy. Use the lightest process that adequately protects people, evidence, project integrity, and the mission. Do not create a form, policy, meeting, or document unless it solves a real coordination, accountability, safety, or preservation problem.

This operating model applies to research, software, documentation, external engagement, and project decisions. More specific policies may supplement it. They must not silently contradict the founding principles or this model.

## 2. Four levels of commitment

Not every statement in the repository has the same authority or permanence.

### 2.1 Foundational commitments

The mission and core protections expressed in the founding principles: public benefit, freedom of inquiry, rights-respecting openness, political independence, resistance to capture, fair work, contributor agency, accountability, resilience, and succession.

These are the project's deepest commitments. They are not immutable, but changing them requires an explicit, public proposal; reasons and evidence; consideration of affected people; a record of alternatives and objections; and a deliberate human decision. As a community forms, legitimate changes must include meaningful participation by that community. No AI system, founder, funder, or single contributor should be able to quietly rewrite them.

### 2.2 Protected institutional commitments

Policies that operationalize foundational commitments, including governance, funding, compensation, ownership, licensing, data rights, research independence, and succession.

These require explicit authorization and appropriate expertise. Legal, financial, safety, or rights-affecting changes require qualified advice where appropriate. Until legitimate shared governance exists, the founder may coordinate provisional decisions but must not describe them as community-approved or permanent.

### 2.3 Operating standards

Research methods, evidence records, AI collaboration, code review, security practices, documentation, release procedures, and contribution workflows.

These should be stable enough to create predictable practice and may be revised as experience improves them. Material changes must be recorded with rationale, scope, effective date, and migration implications. Standards should be proportionate to project scale.

### 2.4 Working hypotheses and experiments

Product direction, user assumptions, technical architecture proposals, research questions, prototypes, and organizational possibilities.

These are expected to change. Label them as hypotheses or experiments, define what evidence would support or reject them, and avoid presenting them as established commitments.

## 3. Evidence and claim discipline

Every consequential factual claim should be traceable to evidence appropriate to the claim.

Use these labels in research and decision records where they improve clarity:

- **Observed:** directly inspected or measured by the project; include the object, version, date, and method.
- **Source-reported:** stated by an identifiable source; distinguish the source's claim from our own verification.
- **Reproduced:** independently repeated using recorded inputs, versions, environment, and procedure.
- **User-reported:** described by a participant or practitioner; do not generalize beyond the evidence.
- **Inferred:** reasoned from observations or sources; explain the reasoning and uncertainty.
- **Hypothesis:** plausible but unverified proposition to be tested.
- **Decision:** an authorized choice, with its decision-maker, date, rationale, and scope recorded.

Do not turn a source-reported claim into an observed fact by paraphrasing it. Do not treat search snippets, AI summaries, repository activity, stars, or documentation promises as proof that software works. Repository existence and recent activity do not verify a research report's description of that repository.

For comparisons, record the versions and dates examined. Distinguish feature presence from successful operation, and successful operation from suitability for a user's actual workflow. Record negative results, failures, limitations, and untested dimensions.

For important research conclusions, retain enough information for another person to locate the evidence and understand how the conclusion was reached. Use source registers, experiment records, and claim/evidence tables when useful; do not impose them on trivial notes.

## 4. Provenance and review status of project work

AI assistance is permitted and expected, but authorship, review, and verification must not be conflated.

For substantial public-facing research, policy, product, and technical documents, record a concise provenance/review note. It should identify, as applicable:

- Whether the initial draft was human-written, AI-assisted, or AI-generated.
- Whether a human has read the current version.
- Whether claims and citations have been checked against underlying sources.
- Whether technical behavior has been reproduced independently.
- The date and scope of the latest review.
- Important unresolved limitations.

Use plain status terms:

- **AI-drafted / not human-reviewed**
- **Human-read** — a human has read the current version, not necessarily checked every claim.
- **Source-checked** — material factual claims and citations were checked against the cited sources.
- **Independently reproduced** — the described test or result was repeated by someone other than the original operator, with sufficient details recorded.
- **Community-reviewed** — reviewed by relevant contributors or stakeholders; state who/which group and the scope where disclosure is appropriate.

These statuses are not a quality ranking and should not imply more than was done. A human reading an AI-generated document does not make its claims verified. An AI reviewing another AI's output is not independent human review.

Do not add review metadata mechanically to every small file. Apply it to documents that influence public claims, consequential decisions, product behavior, research conclusions, or contributor expectations. Keep a lightweight review log when the document changes materially.

## 5. Research and tool evaluation

Before recommending that Common Knowledge build or adopt a tool:

1. State the user, task, and problem being investigated.
2. Identify existing tools, standards, and upstream projects that may already address it.
3. Inspect primary sources and, where feasible, install and exercise relevant tools.
4. Record exact versions, environment, inputs, commands or procedure, outputs, and failures.
5. Use safe, disposable environments for untrusted software; do not run arbitrary research code on a personal or production host.
6. Compare tools against the same representative fixture and ground-truth expectations where possible.
7. Separate what was tested from what was only read about.
8. Document the remaining gap, alternative explanations, and evidence that would change the recommendation.
9. Include the option to contribute upstream, integrate existing tools, defer, or stop.

A synthetic fixture must have an explicit ground-truth record independent of the software being evaluated. Keep expected findings and seeded defects outside the scanned project when their presence could influence the tool. Include both positive and negative cases, ambiguous cases, and known limitations. A tool passing a fixture designed around its current implementation is not meaningful independent validation.

Do not claim user need, adoption, or endorsement without direct evidence. Conversations should focus on actual workflows, recent experiences, failures, workarounds, and unmet needs—not simply whether someone likes the Common Knowledge mission or proposed product.

## 6. Human research and external engagement

Treat conversations, interviews, usability tests, and feedback as interactions with people, not as a source of convenient quotations.

Before collecting information, explain the purpose, intended use, whether notes or recordings will be made, who may access them, and whether attribution is intended. Obtain permission for recording and direct quotations. Do not promise anonymity unless the process can actually provide it. Collect the minimum information needed, restrict access to sensitive notes, and establish retention/deletion expectations.

Do not present informal discovery conversations as representative research, formal peer review, endorsements, or human-subjects research approval. If the work is intended for publication or generalizable research, or involves sensitive populations or information, assess whether ethics review or other oversight is required before proceeding.

Never treat one participant as a representative of an entire discipline, community, or population. Invite disagreement and seek perspectives from people who may be disadvantaged by the proposed work. Respect community authority over knowledge, data, and publication concerning them.

## 7. Technical change and repository practice

- Use a branch for substantial, uncertain, security-sensitive, or externally consequential work. Small, obvious, low-risk corrections may be handled more simply when the reason is clear.
- Keep changes scoped and reviewable. Prefer a small number of coherent commits over activity for its own sake.
- Before editing, inspect the current implementation, relevant documentation, tests, and repository state.
- Add or update tests for behavior changes. Run the relevant checks and report exact commands, environment, and outcomes.
- Distinguish tests written, tests run, tests passed, CI observed, and behavior independently reproduced.
- Do not report CI as passing unless a run and its result have actually been inspected.
- Do not execute untrusted code or scripts without an explicit safety assessment and isolated environment.
- Treat symlinks, path traversal, secrets, absolute-path disclosure, network access, telemetry, and data exfiltration as explicit security/privacy concerns.
- Preserve historical records. Correct errors transparently; do not silently rewrite history to make earlier work appear more accurate.
- Update status documents when implementation changes. The code and observed runtime establish what exists; plans do not.
- Do not add dependencies, telemetry, remote services, or automatic uploads without documenting their purpose and implications. Obtain explicit authorization for material new data flows or permissions.

For consequential technical choices, write a short Architecture Decision Record (ADR) with context, options, decision, consequences, and status. Do not create an ADR for every implementation detail.

## 8. AI collaboration and authority

The [AI Collaboration Protocol](AI_COLLABORATION.md) governs AI-specific conduct and is subordinate to the foundational commitments and legitimate human/community governance.

AI systems may research, draft, code, test, challenge assumptions, and carry out bounded delegated work. They must distinguish evidence from inference, disclose uncertainty, and not claim human review, external validation, or community agreement that did not occur.

AI systems may not independently decide mission, governance, legal form, jurisdiction, licensing, funding, compensation, ownership, contributor rights, or commitments on behalf of people or communities. They may present recommendations, but authorization remains with the appropriate human or legitimate governing body.

Agreement among AI systems is not independent verification. A human decision-maker should be given the substantive disagreement, evidence, options, and trade-offs—not merely a vote count or consensus summary.

## 9. Decisions and changes to commitments

Record a decision when it materially affects mission interpretation, user promises, product scope, architecture, security/privacy boundaries, research conclusions, external commitments, or the rights and responsibilities of contributors.

A useful decision record states:

- The question and why it matters.
- The evidence available and important uncertainties.
- Options considered, including doing nothing or contributing upstream.
- The decision and who authorized it.
- Rationale, trade-offs, and affected parties.
- Revisit conditions or a review date if appropriate.

For changes to foundational or protected commitments, additionally record the proposal, notice, consultation, objections, and how those objections were addressed. Do not treat silence as consent.

Correct factual errors promptly and visibly. Changes of judgment should preserve the earlier rationale and explain what new evidence or reasoning changed the decision.

## 10. External contributions, licensing, and public releases

The repository currently has no selected project license. Do not imply that the code or other material is available for unrestricted reuse, and do not choose a license by default. Before soliciting or accepting substantive external code contributions, decide how licensing, contributor permissions, attribution, third-party material, and any contributor agreement will work. Obtain qualified advice where necessary.

Before the first public software release or a materially expanded public service, review at minimum:

- License and third-party notices.
- Installation and supported environment.
- Security and privacy risks, including local data handling.
- Test and CI results, with exact scope.
- Known limitations and unsupported use cases.
- Data flows, network behavior, telemetry, and permissions.
- Accessibility and documentation.
- Maintenance owner and issue-reporting path.
- Release notes and a rollback or withdrawal plan.

A public repository is not by itself a supported product release. A prototype must be labelled as such, with known limitations and no unsupported assurance claims.

## 11. Handover and governance transition triggers

The current founder-led coordination is provisional. Before any of the following events, pause and review whether additional governance, consent, legal advice, security, or accountability arrangements are required:

- The first external contributor is invited to make a substantive contribution.
- The first public software release or hosted service is offered under the Common Knowledge name.
- The project accepts money, grants, sponsorship, donated assets, or material in-kind support.
- The project hires, pays, or formally directs another person.
- The project collects, stores, or processes personal, confidential, sensitive, or community-controlled data.
- The project enters an institutional partnership or makes a commitment on behalf of others.
- The project controls infrastructure, funds, or shared assets on which others depend.
- A decision could materially affect contributor rights, research independence, or the public mission.

A trigger does not automatically prohibit the activity. It requires a documented readiness review before proceeding. The review should identify who is affected, who has authority, what safeguards are missing, and whether qualified advice or broader consultation is needed.

## 12. Security, privacy, and responsible openness

Openness is a default, not an excuse to expose people or create foreseeable harm. Apply data minimization, least privilege, secure defaults, explicit consent, and proportionate access controls.

Do not publish secrets, personal data, private correspondence, confidential research, sensitive locations, or community-controlled knowledge without a legitimate basis and appropriate authorization. Do not collect data merely because it may be useful later.

Security and privacy claims must be scoped. For example, "local-first" does not by itself prove that a tool never accesses the network, reads outside a selected directory, or exposes sensitive paths. Test and document actual behavior.

For dual-use or otherwise harmful research, do not resolve the issue through a blanket slogan. Assess the specific capability, foreseeable misuse, affected parties, benefits, mitigations, access options, and proportionality. Preserve legitimate inquiry while taking concrete harm and rights seriously. Record difficult decisions and provide a route for review.

## 13. Review and improvement of this model

This is a proposed operating standard, not an immutable constitution. Review it when a trigger in section 11 occurs, when experience exposes a gap, or when contributors reasonably request reconsideration.

A material revision should include:
- What problem the current rule caused or failed to prevent.
- The proposed change and who it affects.
- Evidence, alternatives, and foreseeable risks.
- The decision-maker and consultation undertaken.
- Effective date and any transition needed.

Prefer simplifying a rule when its burden exceeds its value. Do not weaken protections merely to make growth, fundraising, or delivery easier. As the project develops shared governance, authority to maintain this model should transition to a legitimate, accountable process involving contributors and affected stakeholders.

---

## Current implementation status

As of the proposal date, this operating model is not yet fully implemented. In particular:

- The repository has not yet adopted a consistent provenance/review record for substantial documents.
- Research coverage and tool testing remain incomplete; existing research records must be interpreted according to their stated scope.
- External user conversations have not yet been completed.
- The repository has no selected license or formal external contribution policy.
- No legal entity or shared governance structure has been selected.
- The current prototype has not been cleared for public release.

This section should be updated as practices are actually adopted and verified.
