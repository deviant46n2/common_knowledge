# Gaps and Opportunities — November 2026

- **Snapshot cutoff:** 26 November 2026
- **Status:** Preliminary candidate register; no opportunity is yet approved for implementation

This document synthesizes evidence from the November 2026 field snapshot. It should not become a list of ideas based only on what Common Knowledge would like to build.

## How to identify a meaningful gap

For each proposed gap, establish:

1. **Need:** What specific difficulty or unmet need exists?
2. **Affected people:** Who experiences it, and in what context?
3. **Evidence:** Which interviews, studies, reports, usage evidence, or documented examples support the claim?
4. **Existing responses:** Who is already addressing it? What works well?
5. **Remaining limitation:** What is still missing, and for whom?
6. **Possible intervention:** Would integration, partnership, better documentation, research, funding, or new software help most?
7. **Risks and trade-offs:** What could a proposed intervention worsen or centralize?
8. **Confidence:** How strong is the evidence, and what remains unknown?

## Candidate gap register

These are research candidates, not confirmed gaps or approved projects. Confidence applies to the existence of the underlying issue in the reviewed examples, not to the proposition that Common Knowledge should solve it.

| Candidate need | Evidence in current snapshot | Existing responses | Remaining question | Confidence |
|---|---|---|---|---|
| Cross-system research interoperability and provenance | A and E identify repositories, workflow platforms, metadata providers, and archives with distinct schemas and responsibilities; C identifies provenance and execution records needed to connect research artifacts | OAI-PMH, APIs, RO-Crate, PROV-O, DataCite, Europeana EDM, repository integrations | Can a small, practical crosswalk preserve source records, rights, versions, and provenance without excessive burden? | Medium |
| AI research workflow auditability | D reviews a 2026 PNAS analysis finding hidden benchmark/data/metric problems in two AI-scientist systems and a human–AI reproducibility experiment; C provides the underlying record concepts | Version control, workflow logs, CRediT, RO-Crate, research repositories, journal AI disclosure policies | What is the minimum useful audit record, and can it be generated automatically while protecting sensitive traces? | Medium |
| Practical computational reproducibility | C's selected studies find code-execution failures, dependency problems, and limited code availability in specific samples | Binder, Whole Tale, Code Ocean, Galaxy, Dataverse, workflow registries, FAIR4RS, TOP | Which barriers are best addressed by standards, training, infrastructure, incentives, or hands-on support? | Medium |
| Rights-aware federation of community knowledge | E reviews CARE, Local Contexts, Mukurtu, and UNESCO guidance; access, preservation, and reuse rights are not interchangeable | Community archives, Local Contexts labels, Mukurtu cultural protocols, repository access controls | How can community-defined protocols and authority survive metadata harvesting, mirrors, and downstream reuse? Requires direct community-led work | Medium |
| Multilingual discovery and inclusive metadata | E's review of UNESCO, Wikidata coverage, linked language data, and metadata professionals identifies uneven language coverage and resource constraints | SKOS, multilingual linked data, Wikidata labels, Europeana metadata, language technologies | How can the commons support language variants, community-approved descriptions, and low-resource languages without treating translation as a substitute for representation? | Medium for uneven coverage in studied systems; low for global prevalence |
| Durable correction and status history | C documents correction/retraction infrastructure and a 2026 Crossref API update incident; E identifies systems that preserve multiple descriptions and versions | Crossref updates, publisher notices, repository versioning, archival systems, Git histories | Can a commons reconcile status from multiple sources, preserve the original state, and avoid false or overconfident labels? | Medium |
| Researcher support beyond software | G's survey sources identify time, funding, training, incentives, infrastructure, and recognition barriers; samples are heterogeneous and often self-selected | Institutional libraries, research support teams, training programs, funder policies, discipline-specific communities | Which needs are shared across settings, and which require local or disciplinary support? Direct interviews are still needed | Medium for barriers in studied samples; low for universal generalization |
| Public-benefit governance and funding independence | F compares nonprofit, fiscal-host, hybrid, and cooperative models; public-benefit status does not itself guarantee distributed power | Nonprofit bylaws, fiscal sponsorship, cooperatives, endowments, audits, conflict policies | What governance and funding controls are credible for a new, global, research-oriented institution? Requires jurisdiction-specific legal review and stakeholder input | Low–medium |
| Safe, useful distributed compute | B finds mature volunteer-compute and institutional HTC systems, with workload-specific validation and security responsibilities | BOINC, HTCondor, Kubernetes multi-cluster, IPFS/Filecoin and institutional HPC | Which real Common Knowledge workload cannot be served adequately by existing compute? No custom network is justified yet | Low as a gap; high confidence that workload fit and trust need testing |
| Service continuity and migration | A's OSF case study shows an established service can preserve public records while retiring active workflows and write APIs under funding pressure | OSF transition guides, repository export APIs, institutional library migration support, DOI redirects | What portability, private-data retention, API deprecation, and service-level commitments should users expect from shared infrastructure? | High that the issue is real in this case; broader prevalence not assessed |

## Cross-cutting observations

### 1. Existing infrastructure already covers much of the landscape

The current evidence does not support the claim that Common Knowledge needs to invent a new repository, volunteer compute network, preservation system, or universal knowledge graph. Many capable projects exist. A useful contribution may be integration, support, governance, research, or funding rather than replacement software.

### 2. Technical availability does not guarantee practical use

A standard, repository, API, or workflow engine may exist while researchers still lack time, training, institutional support, funding, recognition, or safe data-sharing arrangements.

### 3. Openness needs context and governance

Privacy, consent, security, cultural authority, and unequal benefit affect what can responsibly be shared. Preservation, discovery, access, and reuse should be separate decisions.

### 4. A record of claims and workflows may be a cross-cutting opportunity

Workstreams C, D, and E suggest that a durable record connecting sources, claims, methods, data, code, AI tools, versions, corrections, and access conditions could help across research domains. This is only a hypothesis. It must be tested against existing standards and real workflows before any custom implementation is proposed.

### 5. People must shape the opportunity map

Survey findings are useful but not a substitute for direct conversations. Workstream G has prepared a stakeholder conversation guide; no direct Common Knowledge interviews have yet been conducted. No candidate should be promoted to a confirmed need until affected people have been heard, including those outside well-resourced institutions.

## Opportunity assessment

For each well-supported candidate, compare possible responses:

- Do nothing or monitor the area.
- Improve documentation, discovery, or education.
- Integrate existing tools or improve interoperability.
- Support an existing project or community.
- Conduct further research or a pilot.
- Build a new component only if a demonstrated need remains unmet.

## Decisions

Record any recommendation, the evidence behind it, alternatives considered, dissenting views, and what new information would change the conclusion.

No architectural or organizational commitment should be inferred from an exploratory finding alone.

## Change log

- **2026-11-26:** Replaced the empty gap register with preliminary candidates based on Workstreams A–G. All candidates remain provisional and require further validation.
