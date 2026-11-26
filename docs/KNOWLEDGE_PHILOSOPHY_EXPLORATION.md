# Knowledge Philosophy Exploration

**Status:** Exploratory working document. It records founder-stated principles and emerging product/knowledge-philosophy directions, not a finalized epistemology, community consensus, or technical specification.

This document captures foundational ideas about how Common Knowledge should represent, organize, navigate, and preserve knowledge. It should evolve as these ideas are tested against real use cases, research, and community input.

## 1. Current understanding and knowledge history

Common Knowledge should distinguish between the current state of knowledge and the historical record of how that understanding developed. These are complementary views of the same evolving body of knowledge.

### Current understanding

A clear, maintained presentation of what the available evidence supports now, what remains uncertain, and where credible disagreement persists. It should help people understand the best-supported picture available today without requiring them to reconstruct years of discussion.

### Knowledge history

A traceable account of how claims and assessments developed, including earlier conclusions, evidence available at the time, corrections, retractions, disagreements, and the reasons for significant changes. It should make it possible to inspect past reasoning and understand why conclusions changed.

### How the views relate

- Current assessments should be traceable to their supporting evidence and relevant history.
- Historical records should clearly indicate when an assessment is no longer current, has been superseded, or has been discredited.
- Preserving an outdated conclusion does not mean presenting it as equally credible to the best-supported current understanding.
- The system should prioritize meaningful changes, decisions, and provenance rather than assuming every transient interaction or submitted byte must be retained forever.

This distinction supports both usability and accountability: people can see what is currently understood and inspect how that understanding came to be.

## 2. Subject-centered and claim-centered organization

Common Knowledge should support both broad exploration of subjects and close inspection of individual claims. These are not separate databases or competing organizing philosophies; they are complementary ways to navigate one connected knowledge system.

### Subject-centered exploration

A person should be able to begin with a topic—such as climate change, biology, economics, or a historical event—and explore its broader body of knowledge: major findings, important claims, evidence, unresolved questions, and competing interpretations.

### Claim-centered inspection

A person should also be able to begin with a specific statement and inspect its meaning and scope, sources, evidence, reasoning, assessments, uncertainty, challenges, and history.

### Connection between the two

- Individual claims, evidence, methods, and assessments should contribute to larger bodies of knowledge.
- Subject pages or subject-level views should link back to the specific claims and evidence that support their summaries.
- A claim should be discoverable in the context of the subjects it relates to.
- People should be able to move from a broad overview to the underlying details, and from a specific piece of evidence back to the wider questions it informs.
- Subject-level summaries should not conceal disagreement or imply stronger certainty than the underlying record supports.

**Emerging principle:** Knowledge should be navigable from the broadest subject down to the smallest inspectable piece of evidence, and back again.

## 3. Related principles and open questions

The following ideas have emerged in the broader founding discussion and should inform future work:

- Competing ideas and interpretations should be representable without forcing artificial consensus.
- Pluralism in representing ideas does not mean treating all claims as equally supported. Evidential strength, methods, assumptions, limitations, and uncertainty should remain visible.
- Sources, evidence anchors, claims or observations, and assessments should be distinguishable. A citation alone does not establish that a source supports a claim.
- Corrections, retractions, and meaningful changes in assessment should be traceable.
- Preservation should be ambitious but not absolute: privacy, consent, safety, security, rights, legal duties, and practical maintenance constraints matter.

Questions still open include:

- What exactly counts as a claim, observation, finding, interpretation, or subject?
- How should subjects be defined, nested, connected, and allowed to overlap?
- Who or what is responsible for writing and maintaining subject-level summaries?
- How should summaries represent uncertainty and disagreement without becoming unreadable?
- How should the system distinguish a source's own statement from evidence extracted from it and from an assessment made by a contributor?
- What history must be retained, and what can reasonably be summarized or removed?
- What interfaces make it easy for readers to move between overview and underlying evidence?

These questions should be explored through concrete examples and product use cases before being turned into a rigid data model.

## 4. Relationship to other project documents

- [Governance exploration](GOVERNANCE_EXPLORATION.md) records related founding principles on pluralism, disagreement, and historical preservation.
- [Focused research](../research/FOCUSED_RESEARCH.md) surveys existing knowledge and evidence infrastructure that may inform future design.
- [Product gap analysis](../research/PRODUCT_GAP_ANALYSIS.md) records the current exploratory view of adjacent projects and possible product opportunities.


## 9. A public reference for checking claims

The founder has clarified that Common Knowledge should aspire to become a widely trusted public source of reference: a place people can turn when they hear a claim and want to understand what is supported by the available evidence.

A motivating example is a public official making a factual claim. A person should be able to find the relevant information and inspect the underlying record rather than having to rely on the official's authority, a commentator's interpretation, or Common Knowledge's reputation alone. The same capability should apply beyond politics—to claims by institutions, companies, media organizations, researchers, and other sources.

A useful claim-centered experience may bring together:
- The original statement, speaker or source, date, context, and precise scope.
- Relevant primary sources, datasets, research, records, and other evidence.
- A clear assessment of what the evidence supports, contradicts, or leaves unresolved.
- The methods, assumptions, and limitations behind that assessment.
- The history of changes, corrections, and reassessments.
- Credible challenges and competing interpretations, represented in proportion to their evidential support.

The ambition is not limited to fact-checking isolated statements. Individual claims should connect to broader subjects and bodies of knowledge, so people can understand both the specific question and its wider context.

### Aspiration and humility

The founder describes the ambition as making Common Knowledge a source of truth. This should be understood as a commitment to pursue the most trustworthy understanding possible—not a claim that the institution is infallible or has final authority over truth.

Its credibility should be earned through evidence quality, transparent methods, provenance, independent scrutiny, correction, and openness to challenge. The institution's name or reputation must never substitute for those things. When evidence is incomplete or a question remains unresolved, the system should say so plainly.

**Emerging principle:** Be a public reference people can rely on to investigate what is true, while remaining transparent, corrigible, and humble about the limits of what can be known.


### How knowledge discovery should expand

The founder's current direction is to begin with a deliberately scoped knowledge domain, then expand both the range of subjects and the ways knowledge enters the system.

- **Initial stage:** Concentrate on software project governance and institutional design. Build the collection through focused research and community contributions, while developing and testing the underlying methods.
- **Expansion:** Broaden into related subjects as the infrastructure, standards, and contributor community become capable of supporting them responsibly.
- **Long-term ambition:** Support both community-initiated investigations and proactive research initiated by Common Knowledge—for example, monitoring relevant public information, identifying important unanswered questions, and investigating emerging evidence.

This is a staged direction, not a commitment to monitor every source or investigate every subject. Priorities, capacity, safeguards, and the legitimacy of proactive research will need to be worked out as the institution develops.

**Emerging principle:** Start focused; expand deliberately; ultimately combine community-driven inquiry with proactive, institutionally accountable research.

**Status:** The public-reference ambition and politician-claim example are founder-stated direction. The exact claim intake, context capture, assessment, prioritization, and presentation workflows remain open design questions.


---

*This document is a living exploration, not a promise that every proposed capability is already designed or implemented.*

## 5. Initial scope and long-term breadth

The founder's current direction is for Common Knowledge to begin with a focused set of domains and expand as the software, community, and institutional capacity mature.

### Initial focus

The initial knowledge scope should concentrate on:
- Software projects and the practices, structures, and ecosystems around them.
- Governance: how groups make decisions, distribute authority, resolve disagreement, and remain accountable.
- Institutional design: how institutions are formed, funded, governed, sustained, and protected from capture.

These areas provide a coherent starting point for exploring claims, evidence, competing interpretations, institutional histories, and subject-level synthesis without requiring the project to cover every field immediately.

The project can also use its own development and governance as an early case study, documenting decisions, rationales, changes, and outcomes through the knowledge practices it is developing.

### Long-term ambition

The long-term ambition remains open-ended: support knowledge across all fields of human inquiry, subject to legitimate safety, rights, and practical constraints. The initial scope is a starting boundary for focus, not a permanent limit on what Common Knowledge may contain.

### Design implication

A narrow initial domain should not result in a knowledge model that is fundamentally limited to software, governance, or institutional design. The underlying concepts and infrastructure should be as general as reasonably possible, while the initial interfaces, examples, workflows, and community activity can be tailored to the starting domains.

**Status:** Initial domains and the ambition to expand broadly are founder-stated direction. The exact first collection of topics, admission criteria, sequencing, and expansion process remain open.

## 6. Open proposals and reviewed knowledge

The founder proposes an approach inspired by open-source pull requests: contributions should be publicly inspectable as proposals before they are integrated into the maintained knowledge collection.

The important distinction is between **public visibility** and **recognition as part of the maintained body of knowledge**.

- Anyone should be able to propose a claim, source, evidence, correction, challenge, or interpretation without first obtaining institutional permission.
- A proposal can be publicly viewed and discussed, including its supporting material, author, status, and review history.
- While pending, a proposal should not be presented or indexed as established knowledge, nor appear in ordinary knowledge search results as though it had been accepted.
- Review should be transparent and collaborative: reviewers can ask questions, identify problems, suggest revisions, and explain their assessments.
- Once accepted, the contribution can be integrated into the maintained knowledge collection with its provenance and review history intact.
- A proposal that is declined, withdrawn, or left unresolved may still have a useful public history, subject to safety, privacy, rights, and abuse policies. Its status must remain clear.

This is a working direction, not a finalized workflow. It raises important design questions: how proposals are discovered and discussed; whether some pending proposals should be discoverable in a separate proposals area; how urgent corrections are handled; what happens when review stalls; how appeals work; and how to prevent review from becoming an opaque or inaccessible gatekeeping process.

The model should also distinguish review of knowledge quality from moderation for spam, abuse, privacy, safety, and unlawful material. Those are different responsibilities and may require different processes.

**Emerging principle:** Open proposals, transparent review, and explicit acceptance before integration into maintained knowledge.


## 7. Evidence-first purpose and the boundary between proposals and knowledge

The founder's central concern is that Common Knowledge should make truth-seeking, evidence, and reasoned assessment the norm. It should not become a venue whose main activity is endless argument about identity, belief, or partisan politics.

This does not require pretending that every question has a simple factual answer. It requires being disciplined about what kind of question is being asked and what evidence can establish.

### Evidence should determine the standing of factual claims

- Factual and empirical claims should be assessed against relevant evidence, source quality, methods, reproducibility where applicable, context, and uncertainty.
- The system should communicate the weight of evidence clearly. It should not give unsupported or discredited claims equal standing merely because someone disputes the accepted assessment.
- Reviewers should explain the basis and limits of an assessment, not merely attach a verdict or appeal to authority.
- Confidence should be calibrated to the evidence; the system should not promise certainty where the evidence does not provide it.

### Distinguish different kinds of disagreement

A disagreement may concern empirical facts, the meaning or scope of a claim, definitions, methods, interpretation, predictions, or values and priorities. These should not be collapsed into one generic debate.

Evidence can often resolve or narrow factual disputes. It can inform value-based decisions and reveal their likely consequences, but it cannot by itself settle every question about what people ought to value or prioritize. Common Knowledge should identify that boundary honestly rather than disguising value judgments as scientific conclusions or treating empirical findings as mere opinions.

### Proposals are not yet maintained knowledge

The pull-request-like model is intended to protect both openness and the integrity of the main knowledge collection:
- Contributions can be visible as proposals, with discussion and review history.
- Pending proposals should not be represented as established knowledge or mixed into ordinary search results for accepted knowledge.
- The maintained collection and its search experience should foreground material that has passed the relevant review and assessment process, with its status and uncertainty visible.
- A separate proposals view may allow people to discover and help review work in progress without confusing it with maintained knowledge.
- Acceptance should not imply permanent or unquestionable truth; accepted material remains open to correction, challenge, and reassessment.

### Avoid turning disagreement into the product

Common Knowledge should be designed around understanding, evidence inspection, synthesis, and correction—not engagement-driven controversy. Disagreement is worth representing when it helps explain uncertainty, competing interpretations, or limitations in the evidence. It should not be amplified simply because it is contentious.

**Emerging principle:** Make the best-supported understanding easy to find; make the evidence, uncertainty, and history behind it inspectable; keep unreviewed proposals distinct from maintained knowledge; and distinguish empirical questions from value judgments.

**Status:** This section records the founder's stated aspiration and an emerging design direction. Exact assessment standards, review thresholds, search behavior, and treatment of normative questions remain open and require careful development.

## 8. Human-led beginnings and increasing automation

The founder's current direction is for knowledge assessment and curation to be strongly human-driven in the early stages, with automation increasing as the system, evidence base, and methods mature.

This is a directional aspiration, not a fixed timetable or commitment to fully autonomous knowledge governance.

### Early stage: human-led, AI-assisted

People should lead contribution, review, interpretation, and consequential assessment. AI tools may assist with research, source discovery, extraction, organization, comparison, citation checking, and drafting, but their outputs should be identifiable and reviewable.

### Growing capability: progressively automated assistance

As workflows and quality controls become better understood, automation may take on more routine tasks: monitoring sources for updates, detecting possible contradictions, identifying missing references, checking structured records, suggesting links, and preparing candidate revisions or assessments for review.

### Mature capability: automation with accountable oversight

A more mature system may automate substantial parts of routine evidence processing and maintenance. Human attention can then focus on novel or consequential questions, contested assessments, methodological oversight, appeals, and auditing automated processes.

### Safeguards that should survive increasing automation

- Automation should not make its outputs appear human-reviewed when they have not been.
- The system should preserve provenance: which people, models, tools, source versions, and methods contributed to an assessment or change, to the extent appropriate and safe.
- Automated conclusions should carry calibrated uncertainty and expose supporting evidence and reasoning paths that can be inspected.
- Models and workflows should be tested, monitored, and independently auditable; model confidence alone is not evidence of correctness.
- Consequential, novel, disputed, or high-risk decisions should have appropriate human review and appeal mechanisms.
- Automation should remain replaceable. The knowledge record must not depend on one model, vendor, or proprietary system.
- Human oversight should be meaningful rather than ceremonial: people need the information, authority, and time to challenge automated outputs.

**Emerging principle:** Human-led at the beginning, increasingly AI-assisted and automated over time, without surrendering traceability, contestability, or accountability.


### How automation authority may evolve

The founder's current position is that Common Knowledge should begin with a human-in-the-loop approach. How much authority automated systems receive later should evolve alongside model capabilities, demonstrated reliability, and the maturity of the surrounding safeguards; it should not be fixed in advance.

A useful working direction is **oversight proportional to consequence**:
- Routine, low-consequence, readily reversible maintenance may become eligible for automation earlier, provided changes are logged and can be inspected or reversed.
- Changes that materially affect factual assessments may require stronger validation, monitoring, and clear disclosure of their automated status.
- High-consequence, novel, contested, or difficult-to-reverse changes should retain stronger human review and meaningful avenues for challenge and appeal.

These are illustrative categories for future exploration, not adopted thresholds or a finalized permission system. Greater model capability alone should not automatically confer authority. Delegation should be earned through demonstrated performance, independent evaluation, transparent rules, and the ability to correct failures.

**Working principle:** Start with human oversight; expand automation as reliability is demonstrated, with oversight proportional to the consequences of being wrong.

**Status:** The human-to-automation direction is founder-stated. The division of authority between people and automated systems, review thresholds, audit standards, and acceptable autonomous actions remain open questions.
