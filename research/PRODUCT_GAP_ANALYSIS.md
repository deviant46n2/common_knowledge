# Preliminary Product Gap Analysis

- **Research date:** 26 November 2026
- **Status:** Research synthesis; no user interviews or product validation
- **Purpose:** Translate the adjacent-project landscape into a testable product hypothesis without selecting an architecture.

## 1. The uncomfortable but useful conclusion

The core technical idea behind Common Knowledge is not new.

There are already serious systems for:
- decentralized publication of signed, citable knowledge records (Knowledge Space / nanopublications);
- scientific claims, evidence, and research provenance (MIRA / Discourse Graphs, SciOS RRGI);
- source-linked scientific Q&A and claim/evidence/assessment graphs (Project Delphi / Science Oracle);
- structured scientific claim cards, data-quality findings, disagreement, and graded claim correspondence (The Consilience);
- structured research contributions and comparisons (ORKG);
- archives of published fact-checks (Factiz);
- temporal, sourced fact ledgers (AsOf);
- community fact-checking (Cofacts);
- professional claim monitoring and editorial fact-checking (Full Fact).

Common Knowledge should not claim to be the first project to connect claims, evidence, humans, and AI. The research now shows that much of this work is already being done.

That is good news: the need is real, the field has reusable infrastructure, and we do not have to invent every layer. It also means a new platform would need a much clearer reason to exist.

## 2. What we should not rebuild without a demonstrated gap

| Layer | Existing work | Initial recommendation |
|---|---|---|
| Signed, immutable, citable publication | Nanopublications / Knowledge Space | Do not create a new publication protocol before testing this ecosystem |
| Human/AI identity and provenance | Nanopub trust network; PROV-O; Project Delphi agent/model separation | Reuse established provenance and identity patterns; keep identity trust separate from content correctness |
| Scientific claim/evidence graph | MIRA, SciOS RRGI, Project Delphi | Do not design a new science-only schema from scratch |
| Claim cards and quantitative disagreement | The Consilience templates | Ask about reuse/generalization before creating a competing claim vocabulary |
| Scholarly work discovery | OpenAlex, ORKG | Integrate or link; do not rebuild scholarly indexes |
| Existing fact-check discovery | Factiz, ClaimReview, newsroom archives | Aggregate and attribute existing checks rather than duplicate newsroom work |
| Temporal entity facts | AsOf | Study its valid-time/known-by model; do not assume its confidence/status policy is a universal epistemology |
| Community rumor checking | Cofacts | Learn from its contributor, feedback, and nonprofit model; avoid copying its domain-specific workflow wholesale |
| Claim detection | Full Fact AI and ClaimBuster | Treat as an upstream prioritization task, not a truth-verification engine |

## 3. The possible gap

The most plausible opportunity is not a new universal knowledge graph. It may be a **public-interest reading, contribution, and stewardship layer** that makes existing evidence and knowledge infrastructure useful to ordinary people across domains.

A possible product hypothesis:

> Common Knowledge helps people inspect what is being claimed, what the sources actually say, what evidence supports or challenges it, how the assessment was made, what remains uncertain, and how the record changed—without requiring them to understand the underlying data standards or trust one institution's verdict.

Potentially distinctive elements:

1. **Cross-domain public access:** a coherent reading experience for civic, legal, historical, policy, scientific, and other public knowledge—not just scholarly literature or fact-check articles.
2. **Precise source navigation:** move from a statement to the exact passage, table, dataset row, legal section, or archived source version used as evidence.
3. **Scope and comparability:** make definitions, jurisdiction, time, measurement basis, assumptions, and ambiguity visible so that compatible claims are not falsely presented as contradictions.
4. **Separate assessments:** preserve multiple reviewers, methods, evidence sets, uncertainty, and counterevidence without flattening them into one universal truth score.
5. **Composability:** connect professional fact-checks, research graphs, public datasets, and independently published records; preserve attribution and licenses.
6. **Open public record:** make public records exportable and independently inspectable, with a clear separation between public, restricted, and private material.
7. **Public-interest stewardship:** build long-term independence, safety, correction, contributor rights, and sustainable compensation without donor or founder capture.

These are possible differentiators, not proven market gaps. Knowledge Pixels' unfunded broader proposal already overlaps with some of them, and Project Delphi has a live source-linked scientific Q&A application. We need conversations and user research before claiming uniqueness.

## 4. What the civic stress test taught us

The fictional budget example showed why a public knowledge service needs more than a fact-check verdict:
- nominal appropriations can rise while real appropriations fall;
- two claims can both be correct under different measurement bases;
- an underspecified statement is not automatically false;
- a calculation is a derived activity with its own method and provenance;
- readers need to see the source rows and definitions used.

The existing Consilience measured-claim and disagreement templates already cover quantities, units, conditions, dimensions, and testability in a scientific context. The opportunity may be to generalize those patterns to public budgets and other civic domains, not replace them.

## 5. A possible first product workflow

A deliberately bounded workflow could be:

1. A reader enters a public claim or opens a claim already checked by a newsroom.
2. Common Knowledge finds existing fact-checks (for example, through Factiz/ClaimReview) and preserves each publisher's own verdict and link.
3. It identifies the original statement, its claimant, date, scope, and context.
4. It links primary source documents and exact evidence locations.
5. It separates source statements, extracted evidence, derived calculations, and independent assessments.
6. It explains whether apparent disagreement reflects contradiction, qualification, different definitions, different periods, or insufficient scope.
7. It exposes evidence gaps and what would resolve them.
8. It preserves corrections, dissenting assessments, and provenance.
9. It exports the record in portable formats and, where useful, publishes compatible nanopublications.

This is only a candidate workflow. It may be too broad for an MVP and must be tested against real user needs.

## 6. Recommended next actions

### A. Ask existing maintainers before choosing a stack

- **Knowledge Pixels:** What is the current Nanoarguments roadmap? Is the broader human/AI claims layer still intended? Could a public civic-knowledge application interoperate?
- **MIRA / Discourse Graphs:** Is the schema intended to extend beyond research? What is its license and extension process?
- **SciOS:** Is RRGI's API and application source available? How does RRGI relate to MIRA, and what is the intended civic-domain scope?
- **Project Delphi:** Is its ontology intended to be domain-general? What parts of the public corpus and source excerpts can be exported? How are source locators represented?
- **The Consilience:** Can its claim-card and disagreement templates be generalized to policy and civic claims?
- **Factiz / Full Fact / Cofacts:** What data, APIs, or resolver protocols can be used, and where should Common Knowledge complement rather than duplicate their work?

No outreach has been sent.

### B. Pick one real, bounded claim

Prefer a claim that:
- has already been checked by at least two independent newsrooms or researchers;
- has publicly accessible primary sources;
- has clear but nontrivial scope/definitions;
- can be independently checked by a knowledgeable reviewer;
- does not require sensitive personal data or a politically provocative example for attention.

### C. Build an adapter/prototype before a new platform

Try to assemble one record using existing source data, a current claim template, exact source anchors, and an existing publication format. A lightweight interface may be enough. Do not start with a new graph database, protocol, or global crawler.

### D. Test with people outside the project

Ask a small number of journalists, librarians, policy researchers, subject experts, and ordinary readers to inspect the record without coaching. Measure whether they can:
- identify exactly what is claimed;
- find the evidence and original source;
- distinguish a source statement from an assessment;
- understand uncertainty and disagreement;
- identify what would change the conclusion;
- reuse or export the record.

If existing tools already do this adequately, contribute upstream or stop building a duplicate.

## 7. Decision still open

This research does not select:
- a technology stack;
- a record schema;
- a primary domain;
- a hosting or federation model;
- a legal form or governance structure;
- a license, funding model, or ownership structure.

The immediate decision is smaller: **should Common Knowledge pursue conversations and a small interoperability prototype with existing projects, or continue designing an independent product?**

The evidence currently favors talking to maintainers and testing one real workflow before writing substantial new software.
