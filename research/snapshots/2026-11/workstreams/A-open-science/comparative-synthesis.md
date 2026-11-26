# Workstream A — Comparative Synthesis: Repository, Publishing, and Research Environments

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Preliminary synthesis; selective cases, not systematic review
- **Workstream:** [A — Open science and research collaboration](README.md)

## Purpose

This synthesis compares several different forms of research infrastructure. The aim is not to rank services, but to understand which functions they perform, who is responsible for operating them, what kinds of openness they support, and where Common Knowledge might contribute without duplicating existing work.

## 1. Different infrastructure models solve different problems

| Model | Representative examples | Primary responsibility | Key design question |
|---|---|---|---|
| Shared repository software | Dataverse | Software project develops common code; institutions operate installations | How can independent operators share standards and improvements while retaining local stewardship? |
| Hosted repository service | Figshare | Commercial operator provides service; customers and depositors rely on service terms | What guarantees exist for export, preservation, pricing, and exit? |
| Scholarly dissemination repository | arXiv | Specialized repository and moderation system | How can rapid dissemination coexist with moderation, trust, and durable funding? |
| Integrated research environment | Galaxy | Community develops software, tools, training, governance, and public infrastructure | How can execution, provenance, community support, and long-term sustainability be maintained together? |
| Workflow registry | WorkflowHub | Registry makes workflows discoverable and reusable | How can a registry describe a workflow without controlling its execution environment? |
| Specialist methods platform | protocols.io | Hosted service for structured, versioned methods | How can methods remain portable as platforms change? |

A crucial distinction: “open source,” “open access,” “open data,” “publicly funded,” “community governed,” and “decentralized” describe different properties. No one label guarantees the others.

## 2. Shared software plus independent operators is a promising pattern

Dataverse illustrates a federation of institutional repositories built on common software. Each installation can have its own operator, storage, users, curation, and policies, while shared software and standards enable collaboration and interoperability.

This model can distribute operational responsibility and avoid dependence on one global repository. But it also introduces variation: an installation's preservation quality, accessibility, security, and service continuity depend on its host institution and local implementation.

**Implication:** Common Knowledge should distinguish shared protocols and software from the organizations that operate services. A commons could support a network of independent nodes, but it would need transparent minimum expectations, monitoring, and ways to move between operators.

## 3. Hosted services can be useful, but contracts become part of the infrastructure

Figshare demonstrates that a commercially operated service can expose public content and APIs, support identifiers and versioning, and serve institutions. However, public service policies and institutional contracts may differ substantially, particularly for preservation responsibilities.

The practical questions are not answered by a general claim that content is “preserved”:
- Which service and content types are covered?
- What is the preservation term?
- Who pays for it?
- What happens after a contract ends?
- Can an institution export all files, metadata, identifiers, versions, permissions, and relationships?
- Are there fees or technical restrictions on bulk migration?
- Who is responsible for maintaining access to restricted or sensitive content?

**Implication:** Portability and exit plans should be first-class requirements in any Common Knowledge partnership or infrastructure design. They should be tested, not merely promised.

## 4. OSF shows why continuity must include service scope, not only data persistence

The Center for Open Science's November 2026 transition illustrates a distinction between preserving existing public records and continuing to provide an active collaboration service.

- New OSF Projects and child Components stopped being creatable on 16 November 2026.
- Existing Projects are scheduled to become read-only on 19 February 2027.
- Registrations and Preprints continue.
- COS says public Projects will remain accessible at their existing URLs and DOIs and that it will continue to manage storage and preservation.
- Private Projects will remain accessible after the read-only transition to people who already have access on 19 February 2027, but COS anticipates possible future removal with at least 12 months' advance notice.
- Project-creation API endpoints have been disabled; write/update APIs are scheduled to stop with the read-only transition.

The transition is attributed by COS to the cost and complexity of maintaining the broad Projects feature set, funding constraints, and the maturity of specialized repositories and services. COS describes a move toward an integrated model in which OSF focuses on study plans, registrations, preprints, and links to outputs held elsewhere.

**Assessment:** The transition is not simply a platform failure. It is a strategic narrowing of scope intended to preserve selected public infrastructure under financial constraints. However, it creates migration work, changes existing workflows, and highlights the dependence users place on a central operator.

An early Nature report described a different plan for existing private files than the later, more specific COS help guidance. The OSF profile records this discrepancy and follows the latest official operational guidance as of 26 November 2026.

**Implication:** Continuity planning must distinguish:
- Preservation of existing public records.
- Continued editing and collaboration.
- Private data retention and access.
- API compatibility and integrations.
- Migration and identifier redirection.
- The operator's future funding and service commitments.

A platform can preserve a public record while discontinuing the workflow that originally created or maintained it. Both are important forms of continuity.

## 5. Critical scholarly infrastructure can outgrow its original host

arXiv's 2026 transition toward an independent nonprofit is a particularly useful institutional case. Cornell's announcement describes the financial and logistical pressure of maintaining a large repository and the need for more stable support and organizational flexibility.

This is not evidence that nonprofit status alone solves sustainability. The new organization's governance, funding diversity, board accountability, and service commitments will matter.

**Implication:** Mission-critical knowledge infrastructure needs an explicit succession plan. A founder, university, donor, company, or single grant should not be an irreplaceable point of failure.

## 6. Reproducibility is a whole-system property

Galaxy combines tools, execution, workflow construction, recorded analysis histories, public infrastructure, training, and community governance. WorkflowHub provides a more focused registry role. Dataverse can preserve datasets and related materials. These functions complement one another.

A reproducible research record may need:
- Research question and protocol.
- Data provenance, license, and access conditions.
- Code, tools, workflow definitions, and version identifiers.
- Software and environment dependencies.
- Parameters, execution history, and logs.
- Output artifacts and their checksums.
- Human decisions, exclusions, and deviations.
- Clear limitations and known sources of uncertainty.

No single repository or workflow engine necessarily preserves all of these. A paper plus a dataset DOI is not automatically enough to reconstruct a computational result.

**Implication:** Common Knowledge should investigate interoperable research records and provenance rather than build a universal analysis platform. Existing tools can remain specialized if their outputs can be linked and interpreted.

## 7. Community science requires attention to who participates and what the data represent

iNaturalist and eBird show that public contributions can become valuable research resources. They also show why volume and openness are not equivalent to representativeness.

Research on contributory biodiversity data identifies multiple filters shaping observations: who can participate, what can be detected, where people sample, and what people prefer to record. Studies of eBird have found uneven geographic coverage associated with social and economic factors in particular settings.

These biases do not make the data useless. They mean that data must be interpreted in relation to the question, sampling design, and population being represented. In some cases, structured sampling or targeted community partnerships are necessary.

**Implication:** Common Knowledge should record how data were generated, who is missing, what the sampling process was, and which inferences the data can or cannot support. Participation should include influence over research questions where appropriate, not merely a request to contribute data.

## 7. Preliminary design principles for Common Knowledge

The evidence supports investigating the following requirements:

1. **Federation before centralization:** connect independent repositories and research environments where possible.
2. **Portability by design:** make complete export, migration, and independent mirroring testable requirements.
3. **Interoperable provenance:** connect datasets, methods, workflows, software, outputs, people, and versions with stable identifiers and machine-readable metadata.
4. **Local stewardship:** allow communities and institutions to operate infrastructure under shared technical and ethical expectations.
5. **Transparent governance:** disclose who operates each service, who funds it, who makes decisions, and how users can challenge those decisions.
6. **Preservation as an operational commitment:** document responsibility, redundancy, fixity, succession, and funding.
7. **Openness with rights-based protections:** do not expose sensitive personal, Indigenous, or ecological data merely because a project is publicly funded.
8. **Evidence-aware participation:** preserve sampling methods, contributor context, uncertainty, and known biases.
9. **People and support are infrastructure:** training, curation, moderation, documentation, accessibility, and community care require sustained resources.
10. **No automatic platform-building:** use existing services until a demonstrated need and a credible maintenance plan justify new software.

These are working hypotheses derived from a selective review, not finalized architecture or policy.

## 8. Questions that remain open

- Which metadata and provenance standards provide the best cross-disciplinary minimum without imposing a burdensome universal schema?
- What level of federation is practical for identity, authorization, discovery, and data movement?
- Which repository services have credible independent preservation arrangements and tested exit procedures?
- How do researchers experience the actual usability and costs of Dataverse, Figshare, and institutional repositories?
- What governance models give contributors and affected communities meaningful influence?
- How should Common Knowledge represent contested findings, corrections, negative results, and unresolved disagreement?
- What is the smallest useful interoperability demonstration that could be tested with existing systems?

## 9. Next research actions

1. Complete a technical comparison of repository metadata, identifiers, APIs, exports, and versioning.
2. Investigate preservation certification and trusted digital repository practice, including CoreTrustSeal and the TRUST principles.
3. Review arXiv's nonprofit transition when formal governance and financial documents are available.
4. Compare Galaxy and WorkflowHub with Jupyter-based environments and workflow execution standards.
5. Conduct structured conversations with researchers, data librarians, research software engineers, and community-science organizers.
6. Use findings to decide whether Workstream A is ready for a bounded synthesis or needs another focused pass.

## Limitations

This synthesis is based on a small, deliberately varied sample and public documentation plus selected peer-reviewed literature. Several claims about service policies come from the operators themselves. It does not include a systematic review of user experience, audited finances, contracts, or independent security and preservation assessments. The sample remains weighted toward English-language and North American/European infrastructure.

## Change log

- **2026-11-26:** Initial comparison of Dataverse, Figshare, arXiv, Galaxy, WorkflowHub, protocols.io, and participatory biodiversity platforms.
