# Discovery Completion — Users, Existing Infrastructure, and First-Workflow Candidates

- **Research date:** 26 November 2026
- **Status:** Desk-research synthesis; outreach and user validation remain outstanding
- **Purpose:** Close the current discovery cycle sufficiently to make an MVP decision.
- **Related work:** [Product Gap Analysis](PRODUCT_GAP_ANALYSIS.md), [Focused Research](FOCUSED_RESEARCH.md), [Product Direction](../product/PRODUCT_DIRECTION.md), [Prototype Plan](../product/PROTOTYPE_PLAN.md)

## Executive conclusion

The broad technical premise is already served by several serious projects. Common Knowledge should not begin by creating another generic claim database, scientific knowledge graph, fact-check archive, or nanopublication network.

The most plausible remaining opportunity is a **public-facing interpretation and evidence-navigation experience that can connect records held by existing systems**. That possibility is not yet validated. It must be tested with people who currently research, verify, curate, or rely on public claims and evidence.

The research phase is ready to transition into MVP discussion, provided the MVP is treated as a hypothesis to test rather than a commitment to build a new platform.

## 1. What the existing landscape already covers

### Publication and shared knowledge infrastructure

**Knowledge Pixels / nanopublications**
- Provides tools to create, sign, publish, browse, query, and collaborate around nanopublications.
- Describes human-facing interfaces and APIs for machines, with AI agents as first-class publishing participants.
- Has an incubator for new use cases and publicly lists team contact routes.
- Implication: do not build a competing publication network or signing layer before testing whether a Common Knowledge use case can be built on this ecosystem.

Sources:
- https://knowledgepixels.com/
- https://github.com/knowledgepixels
- https://nanopub.net/docs/

**MIRA / Discourse Graphs**
- MIRA describes an open, early-stage architecture for modular interoperable research records; it explicitly does not host the graph itself.
- Discourse Graphs describes a tool/ecosystem for modular claims, evidence, questions, and results, with plugins and a tool-agnostic protocol in development.
- Implication: these are especially relevant to researcher workflows and interoperability. Their intended scope, current implementation maturity, extension model, and licensing should be confirmed directly before selecting a research-focused MVP.

Sources:
- https://mira.science/
- https://discoursegraphs.com/

### Scientific claim analysis and evidence assessment

**Project Delphi / Science Oracle**
- Has a public source-linked scientific Q&A experience and a probabilistic knowledge graph ontology.
- Its ontology repository contains vocabulary, examples, nanopublication materials, tests, and pipeline code; it is not a complete export of the changing application dataset.
- Implication: a science-only claim/evidence graph and Q&A interface would overlap substantially. A possible distinction would need to come from cross-domain use, public record stewardship, interoperability, or a reader workflow—not merely adding citations to scientific answers.

Sources:
- https://github.com/fractastical/project-delphi-ontology
- https://scienceoracle.org/

**The Consilience**
- Provides structured scientific claim comparison, graded correspondence, explicit disagreement, and testability analysis. Its public materials describe a deterministic judging layer and disclose evaluation results and limitations.
- It also describes a creator/research desk workflow that segments sources into passages and connects claims to primary sources.
- Implication: do not rebuild scientific comparison or claim-card machinery without a specific need. A broader public reader should preserve the distinction between extracted claim, source passage, comparison method, and human review.

Sources:
- https://theconsilience.io/
- https://theconsilience.io/research/
- https://theconsilience.io/the-verification-gap/

### Civic and public-claim fact-checking

**Factiz**
- Reports an archive of over 100,000 claims checked by hundreds of newsrooms across dozens of languages.
- Groups checks of the same claim, retains each newsroom's own verdict and article link, and documents source and reuse licences.
- It explicitly does not claim to contain every fact-check; inclusion depends on what publishers share under usable terms.
- Implication: a new fact-check archive or universal verdict aggregator would be a poor starting point. A useful complement might connect an existing check to primary documents, precise evidence locations, temporal context, scope, and other independently sourced records.

Sources:
- https://factiz.org/global-fact-check-database/
- https://factiz.org/platform/
- https://factiz.org/sources/

**Google Fact Check Tools API / ClaimReview**
- Provides programmatic search of fact-checked claims and management of ClaimReview markup by authorized publishers.
- Search requires an API key; markup management requires authorization for the publisher's site.
- Implication: ClaimReview can be an upstream discovery/interchange source, not a complete evidence model or a substitute for publisher permission.

Sources:
- https://developers.google.com/fact-check/tools/api/
- https://developers.google.com/fact-check/tools/api/reference/rest/

**AsOf**
- Provides a temporal fact ledger with sources, confidence, valid-time and recorded-time distinctions, change queries, and a public API/MCP interface.
- Its own assertability policy is explicitly defined by its implementation; it should not be treated as a universal epistemology.
- Implication: temporal state and "what was known when" are already being productized. Common Knowledge should only pursue this if user research identifies a distinct need for broader evidence and assessment semantics.

Source:
- https://asof.is/api-docs

**Cofacts / Full Fact**
- Remain relevant examples of community rumor verification and professional claim monitoring, respectively, from the earlier landscape research.
- Implication: learn from established contributor and editorial workflows rather than assume a new community fact-checking process is needed.

Sources:
- https://cofacts.tw/
- https://fullfact.org/

## 2. User problems worth validating

These are candidate jobs inferred from the landscape, not claims established by interviews.

### A. Readers and public-interest researchers
- "I found a claim or fact-check. Show me the original source and the exact passage or data behind it."
- "Are two sources actually disagreeing, or are they using different definitions, periods, populations, or measures?"
- "What changed since this was last checked?"
- "What is still uncertain, and what evidence would resolve it?"

### B. Journalists and fact-checkers
- "Has another newsroom already investigated this claim?"
- "Can I reuse an existing check without losing its original author, verdict, date, or licence?"
- "Can I attach primary evidence and context once, then link it to related claims and later corrections?"
- "How do I avoid repeating work while retaining editorial independence?"

### C. Researchers and evidence-synthesis teams
- "Can I trace each synthesis statement to the exact studies, data, and methods behind it?"
- "Can another reviewer challenge one part without overwriting the original assessment?"
- "Can I preserve competing interpretations and update the synthesis as evidence changes?"

### D. Librarians, archivists, and knowledge stewards
- "Can I preserve the source version and locator that a record depended on?"
- "Can I keep corrections and provenance while making records portable?"
- "Can I distinguish public metadata from material that cannot legally or ethically be republished?"

### E. Public agencies and policy analysts
- "Can I connect a public statement to the underlying statute, budget line, dataset, methodology, and time period?"
- "Can a reader reproduce the calculation and understand the assumptions?"
- "Can the record remain useful after the underlying webpage or administration changes?"

## 3. Candidate first workflows

Scores below are qualitative hypotheses, not measured results. They compare how well a workflow could demonstrate Common Knowledge's proposed value while keeping the first build bounded.

| Candidate workflow | Demonstrable value | Existing overlap | Feasibility with public sources | Main risk |
|---|---|---|---|---|
| Reader for an already fact-checked public claim: connect newsroom checks to primary sources, exact passages, scope, and changes | High | High | High | Could become a thin wrapper around Factiz/ClaimReview |
| Research evidence synthesis record: connect a narrow conclusion to studies, methods, evidence passages, and independent assessments | High | High | Medium | Could duplicate Delphi, MIRA, Consilience, or specialist review tools |
| Public-data/policy claim record: connect a bounded numerical claim to source datasets, definitions, calculations, and time context | High | Medium | High if a well-documented dataset is chosen | Domain complexity and ambiguity in measures |
| Temporal entity fact ledger | Medium | Very high | High | AsOf and other knowledge bases already address much of this |
| General-purpose collaborative knowledge graph | Unclear | Very high | Low | Too broad; no validated user or differentiating workflow |

### What this comparison suggests

The best *test case* may be a bounded public-data or policy claim because the evidence chain can be independently reproduced: source table, definition, calculation, date, and interpretation. It can show why precise evidence anchors and transparent derivations matter.

The best *product-discovery probe* may be an already fact-checked public claim because it lets us test whether a reader gains anything beyond existing fact-check aggregators.

These are not competing final recommendations. One is a tractable technical test; the other is a useful user-value test. We should not select either until the MVP discussion considers actual user access and feedback.

## 4. What the experimental record work establishes—and does not

The synthetic record experiment (tracked separately in PR #3) is a useful proof of representation feasibility:
- distinguishes an observation from an assessment of its accuracy;
- anchors evidence to a source location;
- represents different evidence relationships;
- records multiple assessments and provenance without overwriting them;
- demonstrates a second version and an unsigned nanopublication mapping;
- includes automated structural tests using RDFLib.

It does **not** establish:
- that the model is the right one;
- that a non-specialist can create or understand a record;
- that the proposed interface solves a real user problem;
- that the nanopublication drafts pass official validation or have been published;
- that a new platform is necessary.

This is enough to support product conversations and a small prototype decision, not enough to declare an architecture.

## 5. Maintainer outreach: who to ask and what to learn

No outreach has been sent. The following is a proposed order, not a claim of relationship or commitment.

1. **Knowledge Pixels** — ask whether a cross-domain public-facing evidence reader could be built using its existing publication/query infrastructure; what contribution and incubator paths exist; what user workflows they most need.
   - Public route: info@knowledgepixels.com; https://knowledgepixels.com/
2. **Project Delphi** — ask which parts of the ontology and application data are reusable/exportable; how they represent source locators and public/private records; whether cross-domain use is in scope.
   - Public route: https://github.com/fractastical/project-delphi-ontology
3. **MIRA / Discourse Graphs** — ask about current schema maturity, extension and contribution process, supported tools, interoperability, licensing, and whether civic/policy knowledge is within intended scope.
   - Public routes: https://mira.science/ and https://discoursegraphs.com/
4. **The Consilience** — ask which components/templates are reusable, whether its source-to-passage workflow is available independently, and what it sees as out of scope for its scientific comparison engine.
   - Public route: https://theconsilience.io/
5. **Factiz** — ask about data access, update cadence, grouping/identity of repeated claims, licence boundaries, and where an evidence-navigation layer could complement rather than duplicate its archive.
   - Public routes: https://factiz.org/platform/ and https://factiz.org/sources/

### Suggested questions for every maintainer

- What user task does your system solve particularly well today?
- Which adjacent task do users repeatedly ask for that you do not intend to solve?
- What data, APIs, identifiers, or exports can an independent application reuse?
- What are the licensing, attribution, privacy, and rate-limit conditions?
- What is the recommended way to contribute improvements upstream?
- What would make a Common Knowledge integration useful rather than duplicative?
- Are there known failure modes or design choices we should avoid?

## 6. User discovery: minimum useful conversations

Before committing to an MVP, aim for a small set of focused conversations across at least three roles: people who produce or curate evidence, people who consume it professionally, and ordinary readers/researchers.

Ask about a recent real task, not whether they like the Common Knowledge mission:
- Show me the last time you had to verify or trace a consequential claim.
- What sources and tools did you use, and in what order?
- Where did you lose time or confidence?
- How did you handle conflicting sources, definitions, or corrections?
- What did you need to preserve for another person to reproduce your work?
- What did your current tools fail to do?
- Would you use a small tool for this task next month? What would it have to replace or fit alongside?
- What information could not be made public?

Do not lead with the proposed product or ask only hypothetical feature questions. Record the task, workaround, frequency, consequences, existing tools, and evidence of willingness to use a better workflow.

## 7. Remaining research boundary

The following are not completed and should remain explicit:
- no maintainer has been contacted;
- no user interviews or independent usability sessions have occurred;
- no access or integration commitments have been obtained;
- no rights review has been completed for a selected real-world case;
- no first user group or domain has been selected;
- no MVP or architecture has been approved.

These gaps cannot be closed by more desk research alone. They require human conversations and a deliberate product choice.

## 8. Recommendation: close broad research and move to MVP discussion

The current research is sufficient to stop expanding the landscape survey. The next decision should be made in an MVP discussion using:
1. the user problem we most want to serve first;
2. the workflow that makes that problem concrete;
3. the existing systems we would integrate with or build upon;
4. the smallest demonstrator that can test the value;
5. the people who can evaluate it independently.

If those discussions reveal a factual gap, do a narrow research task to answer it. Otherwise, begin the MVP definition. Do not delay roadmap design for another general technology survey.

## Source and evidence notes

This document combines the current project research with a focused review of the official public materials linked above. Public product descriptions are evidence of stated capabilities, not independent validation of reliability, user adoption, or product-market fit. The qualitative workflow comparison is the authors' synthesis and should be revised in light of maintainer and user conversations.
