# Workstream A — Field Overview: Open Science and Research Collaboration

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Initial landscape pass; not comprehensive
- **Workstream brief:** [A — Open science and research collaboration](README.md)
- **Research program:** [Seven-workstream program](../../../../PROGRAM.md)

## Scope

This workstream examines how people and institutions discover, organize, conduct, review, publish, share, and reuse research. It includes formal scholarly research and public, independent, participatory, and community-based research.

"Open science" is not one product category. It includes practices and infrastructure across the research lifecycle: planning and preregistration, methods, collaboration, data collection, analysis, software, peer review, publication, dissemination, reuse, and public participation. Different tools support different parts of this lifecycle.

## Initial landscape model

The following categories are a working map for discovery, not a definitive taxonomy.

| Layer | What it supports | Examples to investigate |
|---|---|---|
| Research planning and project records | Study plans, preregistration, project metadata, persistent records | OSF Registries and other registries |
| Collaboration and working environments | Shared documents, project coordination, lab notebooks, protocols, version control | Discipline-specific and general collaboration tools |
| Data, code, and materials | Deposit, curation, access, citation, and reuse of research outputs | Zenodo, Dryad, institutional and disciplinary repositories |
| Scholarly communication | Preprints, journals, publishing, peer review, editorial workflows | bioRxiv, medRxiv, eLife, PubPub, community-run journals and publishing infrastructure |
| Discovery and aggregation | Search, indexes, catalogs, metadata, and linking between outputs | OpenAlex, scholarly indexes, repository aggregators, project finders |
| Public and participatory research | Volunteer observations, classifications, transcription, community-led research | Zooniverse, SciStarter, iNaturalist, eBird, and local/community platforms |
| Research assessment and integrity | Preregistration, registered reports, review, correction, retraction, research integrity | Registries, journal policies, institutional processes, independent initiatives |
| Public engagement and education | Making research understandable and enabling public participation | Citizen-science networks, science communication, open educational resources |

The categories overlap. A platform may span several layers, and a research team may combine multiple specialized services.

## Initial observations

### 1. The ecosystem is distributed across specialized services

The available landscape includes project registries, repositories, preprint services, citizen-science platforms, scholarly communication infrastructure, and discipline-specific tools. The 2023 ITHAKA S+R landscape review describes scholarly communication as a complex sector supported by shared infrastructure across areas such as discovery, persistent identifiers, preservation, repositories, data curation, publishing, and integrity.

**Assessment:** It is premature to assume that the most useful contribution would be a single replacement platform. Common Knowledge should first understand how existing services connect, where handoffs fail, and what users cannot currently do.

### 2. OSF's role is changing materially in November 2026

The Center for Open Science's current transition documentation says OSF is moving away from functioning as a general project collaboration, data repository, and file-management space. Its stated focus is registrations, community-run preprint services, and linking research plans to outputs hosted in other systems. OSF's transition FAQ says the changes are intended to reduce operational complexity and protect the sustainability of the remaining service. Nature's 2026 reporting describes the financial pressures behind the transition.

**Assessment:** Older references that describe OSF as an all-in-one research workspace must be date-qualified. This transition is a useful case study in the economics and resilience of shared research infrastructure, but it does not by itself establish that the new model will succeed or that users' needs are fully met.

### 3. Citizen-science platforms enable real but bounded forms of participation

Zooniverse connects professional research teams with volunteers who classify, annotate, or transcribe research material. Its platform includes project tutorials, volunteer discussion, project-building tools, and ways for researchers to use resulting data. Peer-reviewed studies examine participant behavior, platform design, and the accuracy of volunteer-generated classifications.

**Assessment:** This is a strong example of public participation in research, but it should not be confused with a general-purpose platform where participants necessarily set research agendas, design studies, or control the full research lifecycle. The degree of participation varies by project.

### 4. Discovery and participation directories are a distinct service

SciStarter helps people discover citizen-science opportunities by topic, activity, and location. It is useful as a discovery and connection layer, but it is not itself equivalent to a complete research-management or scholarly-publishing environment.

### 5. Open access does not automatically mean equitable participation

A 2025 scoping review of open-science impacts reports positive and mixed effects across areas such as open access, citizen science, and open/FAIR data, while also identifying unintended negative effects involving equity, diversity, and inclusion. It identifies lack of skills, resources, and infrastructure as barriers to reusing and building on research.

**Assessment:** Access to an output is only one part of openness. Participation also depends on skills, time, equipment, language, disability access, institutional status, funding, and whether contributors receive recognition and meaningful influence.


### 6. Repositories provide distinct preservation, citation, and curation services

Zenodo and Dryad illustrate different general-purpose repository approaches. Zenodo supports a broad range of research outputs, DOI assignment, versioning, restricted records, and GitHub integration. Its DOI model distinguishes a specific version from the concept spanning versions. Dryad focuses on data publication and describes curator checks, DOI assignment, checksums, replicated storage, and succession planning.

**Assessment:** A repository is not just a file host. Metadata, versioning, curation, rights checks, preservation, and succession all shape whether research outputs remain usable. These functions are related but not interchangeable: a technical file check does not validate scientific claims, and a DOI does not guarantee that a dataset is ethically or legally shareable.

### 7. Discovery infrastructure connects records without necessarily hosting the research

OpenAlex describes itself as an open catalog and knowledge graph that aggregates metadata from sources such as Crossref, DataCite, PubMed, and repositories. Its work model can connect multiple locations or manifestations of a scholarly work, such as a preprint, journal article, and repository copy.

**Assessment:** Discovery and hosting are separate layers. A knowledge commons may gain more by connecting to existing catalogs and improving traceability than by trying to build a complete scholarly index from scratch. Aggregation also introduces its own problems: source coverage, duplicate matching, metadata quality, correction, and update delays.

### 8. Publishing communities can own more of the communication workflow

PubPub presents a community-oriented publishing platform with collaborative authoring, submissions and review, discussions, DOI support, typed content relationships, and exports to multiple formats. It supports a wide range of community publications rather than only conventional journals.

**Assessment:** Publishing can be treated as community infrastructure, not solely as a service controlled by large commercial publishers. However, the existence of flexible publishing software does not resolve questions about editorial independence, governance, funding, recognition, or long-term preservation.

### 9. Peer review models can expose evaluation rather than hide it behind a binary label

eLife's current Reviewed Preprint model publishes manuscripts selected for expert review alongside public reviews and an editorial assessment. Authors may revise and later choose to finalize a Version of Record. This makes some of the evaluation process visible to readers rather than treating acceptance as the only public signal.

**Assessment:** This is a useful example of peer review as a transparent, documented process. It does not eliminate editorial selection or settle how institutions should evaluate research, and its effects should be studied rather than assumed.

### 10. Preprint dissemination needs explicit status and risk communication

bioRxiv and medRxiv distribute manuscripts before peer review. Both describe screening before posting, but explicitly distinguish screening from endorsement or scientific validation. medRxiv adds health-specific warnings and screening around ethical oversight, identifiable participant information, and potential public-health risks.

**Assessment:** Open dissemination does not mean every item should be presented as equally established. Research records need visible status, provenance, version history, and links to subsequent review, correction, or publication. Sensitive domains may require additional safeguards and careful communication.


### 11. Workflow registries make computational methods discoverable research objects

WorkflowHub describes itself as a registry for sharing and publishing workflows across disciplines, using standards including CWL, RO-Crate, Bioschemas, and the GA4GH TRS API.

**Assessment:** This is a useful example of modular infrastructure: a registry can improve discovery and reuse without having to become the execution engine for every workflow. But a registry record alone does not guarantee that a workflow is runnable, maintained, secure, or scientifically valid.

### 12. Protocol infrastructure is distinct from project management and data repositories

protocols.io supports structured, versioned, collaborative research methods. Its current migration messaging is also relevant to the OSF transition: it is promoting migration of methods and active project materials, with OSF Projects scheduled to become read-only on 19 February 2027.

**Assessment:** The transition illustrates why portability and exit paths matter. A migration offer from one vendor should not be mistaken for a neutral sector-wide recommendation; researchers need clear exports, alternative destinations, and preservation plans.

### 13. Participant-controlled data platforms raise a different model of openness

Open Humans enables people to explore personal data and selectively share it with research activities. Its community guidelines explicitly discuss identifiability, data minimization, and participant exit.

**Assessment:** Research participation should not reduce people to data providers. Personal-data research requires granular consent, meaningful participant agency, careful security, and clear downstream-use explanations. “Open by default” is not an appropriate rule for identifiable or sensitive personal data.

### 14. Community-led science can begin with affected communities' own questions

Public Lab's history and external community-science descriptions emphasize low-cost environmental tools, peer learning, and community-led investigation. Its public website currently identifies itself as a static read-only archive, so present operational status remains an open question.

**Assessment:** The model broadens the meaning of research collaboration beyond academic institutions and volunteer task platforms. It also demonstrates that community capacity, local knowledge, education, and practical tools are part of research infrastructure.

### 15. Community-generated observations can become reusable scientific datasets

iNaturalist combines public biodiversity observations with community identification and an explicit Research Grade classification. Eligible observations with qualifying licenses are exported to GBIF.

**Assessment:** This is a strong domain-specific example of public contribution, community review, quality labels, and downstream reuse. Research Grade is not a universal guarantee of correctness; sampling bias, observer expertise, licensing, and sensitive location data remain important.

## Questions for the next research pass

1. Which parts of the research lifecycle are underserved across disciplines, and which are already well served by specialist infrastructure?
2. What interoperability standards and persistent identifiers connect the layers?
3. How do researchers experience transitions between project management, data repositories, preprints, journals, and archives?
4. What evidence exists about the quality, recognition, retention, and influence of public contributors?
5. How do independent researchers and people outside universities gain access to tools, mentorship, funding, and publication?
6. Which open-science practices have evidence of improving reproducibility or research quality, and under what conditions?
7. What are the costs and funding models behind infrastructure that appears free to researchers?
8. How are community-led and Indigenous research priorities represented and protected?
9. How are repository records, preprints, peer-reviewed articles, datasets, and software linked across services?
10. How do different services handle versions, corrections, withdrawals, retractions, and records that should no longer be publicly accessible?
11. What are the actual preservation guarantees, succession arrangements, and costs of major repositories?
12. How are peer-review reports, editorial assessments, and contributor identities governed and credited?
13. What standards and APIs make research records portable between repositories, indexes, publishers, and institutional systems?

## Coverage and limitations

This is a first-pass orientation based on selected primary platform documentation, a scholarly infrastructure landscape review, peer-reviewed citizen-science research, and a recent open-science scoping review. It now includes initial profiles of OSF, Zooniverse, SciStarter, Zenodo, Dryad, OpenAlex, PubPub, eLife, bioRxiv, medRxiv, WorkflowHub, protocols.io, Open Humans, Public Lab, and iNaturalist. It is not a comprehensive census, systematic review, or independent audit of the platforms mentioned.

The current sample is English-language and weighted toward visible online infrastructure. It does not yet adequately cover disciplinary repositories, regional and multilingual networks, research in the Global South, community-controlled knowledge systems, or the full range of institutional and independent research practices.

## Sources

See the [November 2026 source register](../../sources.md), especially entries A-01 through A-47.

## Change log

- **2026-11-26:** Added initial field map and preliminary observations from selected sources. Further project mapping, source verification, and stakeholder research remain necessary.
- **2026-11-26:** Expanded the map to cover repositories, scholarly discovery, community publishing, reviewed preprints, and discipline-specific preprint servers. Added profiles for Zenodo, Dryad, OpenAlex, PubPub, eLife, bioRxiv, and medRxiv, and extended the source register through A-30.
- **2026-11-26:** Added workflow registry, protocol management, participant-controlled personal-data research, community-led environmental science, and biodiversity observation cases. Added profiles for WorkflowHub, protocols.io, Open Humans, Public Lab, and iNaturalist; extended the source register through A-47.
