# Cross-Workstream Analysis — November 2026

- **Snapshot cutoff:** 26 November 2026
- **Status:** Preliminary synthesis; three workstreams have substantive early findings, none is baseline complete
- **Program:** [Common Knowledge Research Program](../../../PROGRAM.md)

## Purpose

This document synthesizes findings across the workstreams. It identifies dependencies, tensions, shared needs, and opportunities that are difficult to see when each area is examined separately.

This is a living synthesis. Findings are provisional where underlying workstreams remain in progress. It is not a final architecture or institutional recommendation.

## Workstream status

| Workstream | Status | Current synthesis contribution |
|---|---|---|
| [A — Open science and research collaboration](workstreams/A-open-science/README.md) | In progress | Initial ecosystem map and comparative synthesis across repositories, collaboration, workflows, citizen science, and community research |
| [B — Distributed and federated infrastructure](workstreams/B-distributed-infrastructure/README.md) | In progress | Initial landscape of volunteer compute, institutional HTC, multi-cluster orchestration, P2P networking, storage proofs, workload fit, and trust boundaries |
| [C — Reproducibility and research integrity](workstreams/C-reproducibility/README.md) | In progress | Initial frameworks and tools map, research-record proposal, and integrity/correction analysis |
| [D — Human–AI research collaboration](workstreams/D-human-ai-collaboration/README.md) | In progress | Initial evidence on AI research agents, human–AI reproducibility, workflow auditability, and contribution/accountability policies |
| [E — Shared knowledge and preservation](workstreams/E-knowledge-preservation/README.md) | In progress | Initial standards map, identifiers, preservation, community rights, and federated discovery synthesis |
| [F — Governance, economics, and institutional design](workstreams/F-governance-economics/README.md) | In progress | Initial comparison of nonprofit, subsidiary, fiscal-host, and cooperative structures; compensation and funding independence |
| [G — People and research ecosystem needs](workstreams/G-people-and-needs/README.md) | In progress | Initial survey evidence on time, funding, incentives, training, infrastructure, and regional equity; conversation guide prepared, but no direct Common Knowledge interviews yet |

## Emerging cross-cutting themes

### 7. Distributed infrastructure creates reciprocal trust obligations

**Supporting workstreams:** B, C, E.

- Workstream B's BOINC review identifies risks to both volunteers and project operators: malicious or faulty results, unsafe workloads, compromised servers, and participant privacy.
- Workstream C's reproducibility work shows that validation must state its scope and cannot be reduced to a generic verified badge.
- Workstream E's preservation work distinguishes proof of storage, actual retrieval, and long-term stewardship.

**Assessment:** A distributed commons must protect contributors' machines and data while also protecting research outputs from malicious or unreliable workers. Signatures, sandboxing, replication, and storage proofs each establish different properties; none proves overall trustworthiness.

### 9. Human–AI research needs auditability, not just autonomy

**Supporting workstreams:** C, D.

- Workstream C shows that computational reproducibility depends on methods, data, code, environments, and correction history.
- Workstream D's 2026 evidence finds that human–AI teams can perform comparably to human-only teams in one reproduction task, while AI-led teams performed substantially worse; other work identifies hidden methodological flaws in autonomous AI scientist workflows.

**Assessment:** Agent task completion and polished manuscripts are not sufficient evidence of scientific validity. The research record should preserve material workflow artifacts, human decisions, data lineage, and verification scope.

### 11. Legal form does not determine whether power is distributed

**Supporting workstreams:** F, A, E.

- Workstream F's initial comparison shows that nonmember nonprofits can include community-represented trustees while retaining board authority, and that worker cooperatives may democratize workplace control without representing all public beneficiaries.
- Workstream A and E show that community governance, contributor agency, and local stewardship exist in many forms outside a single institution.

**Assessment:** Common Knowledge should specify decision rights, representation, asset control, and accountability before selecting a legal form. “Nonprofit,” “foundation,” or “cooperative” is not a substitute for a governance design.

### 12. Funding independence is a structural requirement

**Supporting workstreams:** F, A, E.

- Workstream F's review of Wikimedia, Mozilla, and fiscal-host models shows different mixes of donations, commercial revenue, investment income, and external legal/financial services.
- Workstreams A and E show that infrastructure and preservation depend on durable funding and custodianship.

**Assessment:** Financial transparency is necessary but insufficient. Donor concentration, restricted funding, commercial dependencies, and host control can shape research priorities and continuity. These dependencies should be disclosed and governed.

### 13. Infrastructure needs must be grounded in the people who use and steward it

**Supporting workstreams:** A, B, C, E, F, G.

- Workstream G's initial survey review finds recurring barriers around time, funding, training, incentives, institutional support, and unequal infrastructure capacity. The surveys differ in scope and sampling, and none should be treated as a universal picture.
- Workstreams A, C, and E show that research infrastructure spans repositories, methods, software, preservation, rights, and correction—not just a single platform.
- Workstreams B and F show that distributed compute and institutional sustainability create operational, financial, and governance burdens.

**Assessment:** Common Knowledge should not infer needs from technical possibility. It must learn from researchers, research support staff, communities, contributors, and people affected by research, including those outside well-resourced institutions.

### 14. Data locality can be more important than compute distribution

**Supporting workstreams:** B, C, E.

- Workstream B's workload analysis shows that moving data can dominate execution cost or be prohibited by sensitivity and licensing.
- Workstream C's research-record proposal distinguishes public, controlled-access, and non-shareable inputs.
- Workstream E's community-rights analysis shows that data governance and cultural authority can limit copying and reuse.

**Assessment:** Common Knowledge should consider moving computation to governed data, not assume data should be copied to volunteer machines. This needs workload-specific security and performance testing.

### 1. Federation and interoperability may be more valuable than a new monolithic platform

**Supporting workstreams:** A, C, E.

- Workstream A finds existing systems already support distinct parts of research: Dataverse and Figshare repository services, Galaxy analysis workflows, OSF project coordination, and other specialist tools.
- Workstream E finds mature standards and models for connecting those systems: OAI-PMH, Dublin Core, SKOS, DataCite, BIBFRAME, IIIF, RO-Crate, and PROV.
- Workstream C shows why those connections need provenance, versioning, and explicit execution context.

**Assessment:** A shared layer that helps existing systems interoperate may address a real gap without requiring Common Knowledge to replace them. This remains a hypothesis until tested with actual workflows and users.

### 2. Openness is not the same as unrestricted access

**Supporting workstreams:** A, C, E.

- Workstream A's review of participant-controlled personal data and community science highlights consent and stewardship issues.
- Workstream C's FAIR analysis distinguishes accessibility from unrestricted public download.
- Workstream E's review of CARE, Local Contexts, Mukurtu, and UNESCO guidance shows that community authority and cultural protocols can legitimately govern access and reuse.

**Assessment:** Any shared record model must represent rights and access conditions explicitly. Preservation, discovery, access, and reuse should not be collapsed into a single public/private switch.

### 3. Trust depends on the record around a claim, not only the publication

**Supporting workstreams:** A, C, E.

- Workstream A's Galaxy review highlights the value of workflows, provenance, training, and community governance.
- Workstream C's work on RO-Crate, PROV-O, computational environments, Registered Reports, and correction metadata shows that methods, inputs, software, execution, and post-publication status matter.
- Workstream E's review of Wikidata, Europeana, and identifier registries emphasizes source-level references, metadata provenance, and preserving multiple descriptions.

**Assessment:** Common Knowledge should investigate a research/knowledge record that links claims to sources, methods, inputs, outputs, contributors, versions, and later corrections. It should not imply that the existence of a record proves the claim is true.

### 4. Preservation is an organizational responsibility

**Supporting workstreams:** A, C, E.

- Workstream A's Dataverse and Figshare profiles show that repository software, public services, and institutionally operated services have different custody and continuity responsibilities.
- Workstream C's review of BagIt, PREMIS, OAIS, and CoreTrustSeal distinguishes technical fixity from sustainable preservation operations.
- Workstream E's LOCKSS/CLOCKSS and OAIS review emphasizes custodianship, funding, rights, audit, repair, and succession.

**Assessment:** Backups and mirrors are necessary but insufficient. A credible preservation promise needs named responsibility, resources, rights to preserve and migrate, transparent scope, and a continuity plan.

### 5. Participation quality and knowledge quality are connected

**Supporting workstreams:** A, C, E.

- Workstream A's citizen-science review identifies participation, detectability, sampling, and preference biases in contributory data.
- Workstream C's reproducibility work shows that methods, analysis plans, uncertainty, and correction affect how evidence should be interpreted.
- Workstream E's knowledge-graph and community-archive work shows that classification, attribution, and description are shaped by editorial and cultural authority.

**Assessment:** Participation should not be measured only by contributor counts or data volume. A commons must ask who participates, whose knowledge is missing, how contributions are validated, and how limitations are represented.

### 6. Correction and disagreement must be first-class features

**Supporting workstreams:** A, C, E.

- Workstream C documents correction, expression-of-concern, retraction, replication, and honest-error distinctions.
- Workstream E identifies models that retain multiple sourced descriptions and community narratives.
- Workstream A's comparative work highlights the need for transparent governance and correction pathways in shared research systems.

**Assessment:** A knowledge commons should preserve prior versions and correction histories, represent conflicting evidence, and distinguish disagreement from error or misconduct. A single overwritten “current truth” record would be inadequate.

## Cross-cutting tensions to investigate

| Tension | Why it matters | Research still needed |
|---|---|---|
| Federation vs. usability | Interoperability can increase complexity for contributors | User testing across real research workflows |
| Openness vs. rights | Public release can violate privacy, consent, or community authority | Legal, ethical, and community-led requirements |
| Common schema vs. plural knowledge | Standardization can erase local meaning or competing descriptions | Mapping tests and multilingual/community review |
| Preservation vs. withdrawal | Replicas and caches can outlive the original access decision | Retention agreements, revocation propagation, and limits |
| Automation vs. accountability | Automated enrichment or validation can introduce hidden errors | Provenance, human review, and correction mechanisms |
| Scale vs. stewardship | More records can exceed the capacity to curate and preserve them | Cost models, staffing, and sustainable operations |

## Candidate opportunities

Do not promote a candidate opportunity to a recommendation until the underlying need, existing alternatives, affected people, and risks have been investigated.

| Opportunity | Need and evidence | Existing alternatives | Possible response | Open questions |
|---|---|---|---|---|
| Interoperability and provenance bridge | A/C/E: existing tools serve distinct lifecycle functions; standards exist but are fragmented across implementations | OAI-PMH, APIs, RO-Crate, PROV, repository integrations, Europeana EDM | Prototype a small connector and provenance-preserving export between two existing systems | Does it solve a real user problem? How much data is lost? Who maintains mappings? |
| Rights-aware research/knowledge record | C/E: FAIR, CARE, Local Contexts, and repository rights metadata show that openness and authority need structured representation | Repository-specific access controls, rights statements, community labels, consent systems | Test a record model that separates preservation, discovery, access, and reuse | Can community authority travel across downstream copies? What legal mechanisms are required? |
| Durable correction and version history | C/E: correction feeds can fail; records can contain multiple versions and conflicting claims | Crossref updates, publisher notices, Git history, repository versioning, archival systems | Prototype a claim/resource history with source, time, and correction state | How to avoid false status labels? Who can correct or appeal? |

## Questions for the next synthesis cycle

### Research lifecycle and infrastructure

- Which stages of research are well supported, and where do people encounter recurring friction?
- Which needs require shared infrastructure, and which are better served by existing tools or institutions?
- Where does interoperability matter more than centralization or a single unified platform?

### Openness, rights, and responsibility

- How can openness coexist with privacy, consent, safety, intellectual property, and community authority?
- Which forms of openness are meaningful in practice, rather than merely declared?
- Who bears the costs and risks of making research resources open?

### Trust, evidence, and AI

- How should provenance and reproducibility work across human and AI contributions?
- What independent checks are needed for distributed computation and AI-generated results?
- How can corrections, disagreement, and uncertainty remain visible?

### Power, governance, and sustainability

- Where is control concentrated: infrastructure, funding, data, standards, identity, or decision-making?
- Which governance mechanisms meaningfully constrain capture?
- What trade-offs exist between resilience, usability, cost, and accountability?

### People and participation

- Which barriers recur across disciplines and communities?
- Who is missing from the design and governance of existing systems?
- What evidence shows that a proposed opportunity is a real need?

## Change log

- **2026-11-26:** Created the cross-workstream synthesis framework. No comparative findings had yet been recorded.
- **2026-11-26:** Added preliminary themes based on Workstreams A, C, and E. All three remain in progress; these themes are hypotheses to test, not final conclusions.
- **2026-11-26:** Added Workstream B and two cross-cutting themes on reciprocal trust obligations and data locality. Workstream B remains in progress.
- **2026-11-26:** Added Workstream D and a cross-cutting theme on human–AI research auditability. Workstream D remains in progress.
- **2026-11-26:** Added Workstream F and themes on legal form versus power distribution and funding independence. Workstream F remains in progress.
- **2026-11-26:** Added Workstream G and a cross-cutting theme on grounding infrastructure in the needs of researchers, stewards, and affected communities. Workstream G remains in progress.
