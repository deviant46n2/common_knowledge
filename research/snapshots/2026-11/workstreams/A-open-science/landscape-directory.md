# Workstream A — Open Science and Research Collaboration: Landscape Directory

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Initial, selective directory; not a census or endorsement list
- **Workstream:** [A — Open science and research collaboration](README.md)
- **Field overview:** [Initial field overview](field-overview.md)
- **Source register:** [November 2026 sources](../../sources.md)

## How to read this directory

This directory maps examples by the role they play in the research lifecycle. The categories overlap: a repository may also support collaboration, and a publisher may operate a preprint service.

Inclusion means only that a project is relevant to the landscape. It does not imply endorsement, quality certification, partnership, or a recommendation to use it. A profile indicates that an initial review has been written; an unprofiled entry is a discovery lead that still needs investigation.

## 1. Research planning, project records, and preregistration

| Project / infrastructure | Main role | Initial status |
|---|---|---|
| [Open Science Framework (OSF)](../../projects/osf.md) | Registrations, community-run preprints, links between plans and research outputs; undergoing a major transition away from general project workspaces | Profiled; transition requires continued monitoring |
| OSF Registries | Preregistration and registration records | Candidate for deeper profile |
| [protocols.io](../../projects/protocols-io.md) | Structured, versioned research methods and protocol collaboration | Profiled; current migration offer and deadlines need monitoring |

## 2. Data, software, and research-output repositories

| Project / infrastructure | Main role | Initial status |
|---|---|---|
| [Zenodo](../../projects/zenodo.md) | Multidisciplinary repository for publications, datasets, software, and other research outputs; DOI versioning and GitHub integration | Profiled |
| [Dryad](../../projects/dryad.md) | Curated research data publication, DOI assignment, preservation, and reuse | Profiled |
| [Dataverse](https://dataverse.org/) | Open-source repository software deployed by institutions and consortia to share, preserve, cite, and manage research datasets | Discovery lead; strong candidate for profile |
| [Figshare](https://info.figshare.com/about/) | Commercial repository infrastructure used by researchers and institutions; open APIs and persistent identifiers | Discovery lead; business model and portability merit comparison |
| Disciplinary repositories | Specialized archives for fields such as genomics, ecology, earth science, social science, and clinical research | Broad category requiring systematic mapping |
| Institutional repositories | Institutionally operated repositories for articles, theses, data, and other outputs | Broad category requiring mapping by region and discipline |

Repository selection must be fit to the data, discipline, funder, access requirements, and preservation needs. A generalist repository is not automatically appropriate for sensitive or highly specialized data.

## 3. Preprints, journals, and scholarly publishing

| Project / infrastructure | Main role | Initial status |
|---|---|---|
| [bioRxiv](../../projects/biorxiv.md) | Life-sciences preprint distribution and screening | Profiled |
| [medRxiv](../../projects/medrxiv.md) | Health and clinical preprint distribution with additional risk communication and screening | Profiled |
| [arXiv](https://arxiv.org/) | Long-running disciplinary preprint and e-print archive for physics, mathematics, computer science, and related fields | Discovery lead; high-priority profile |
| [eLife](../../projects/elife.md) | Reviewed Preprint model with public reviews and editorial assessment | Profiled |
| [PubPub](../../projects/pubpub.md) | Community-oriented publishing and collaborative editorial workflows | Profiled |
| Diamond open-access journals and university presses | Publishing models where readers and authors are not charged publication fees, with costs supported by institutions or communities | Broad category requiring comparative research |
| Overlay journals and review services | Editorial review and publication layered over openly accessible repositories or preprints | Discovery category; investigate examples such as Episciences |

Preprint posting, editorial screening, peer review, and publication are different events. Records should make those distinctions visible.

## 4. Scholarly discovery, identity, and metadata infrastructure

| Project / infrastructure | Main role | Initial status |
|---|---|---|
| [OpenAlex](../../projects/openalex.md) | Open scholarly catalog and knowledge graph aggregating metadata about works, authors, institutions, and sources | Profiled |
| [Crossref](https://www.crossref.org/) | DOI registration and scholarly metadata infrastructure, particularly for publications | Standards map started |
| [DataCite](https://datacite.org/) | DOI registration and metadata infrastructure for datasets and other research outputs | Standards map started |
| [ORCID](https://orcid.org/) | Persistent researcher identifiers and connected researcher records | Standards map started |
| [Research Organization Registry (ROR)](https://ror.org/) | Open identifiers for research organizations | Standards map started |
| [OAI-PMH](https://www.openarchives.org/pmh/) | Protocol for harvesting metadata from repositories and archives | Standards map started |
| [re3data](https://www.re3data.org/) | Registry for discovering research data repositories | Discovery lead; profile or standards note needed |

These services do not all host research. Some provide identifiers, metadata, discovery, or exchange mechanisms that let independently operated systems connect.

## 5. Computational workflows, methods, and analysis

| Project / infrastructure | Main role | Initial status |
|---|---|---|
| [WorkflowHub](../../projects/workflowhub.md) | Registry for describing, sharing, publishing, and discovering computational workflows | Profiled |
| [Galaxy](https://galaxyproject.org/) | Open web-based environment for accessible, reproducible computational research and analysis | Discovery lead; high-priority profile |
| [protocols.io](../../projects/protocols-io.md) | Structured experimental and computational methods | Profiled |
| Jupyter and JupyterHub | Interactive computational notebooks and multi-user notebook environments | Discovery lead; distinguish software from hosted services |
| Workflow languages and execution ecosystems | Portable descriptions and execution of workflows, including CWL and related tools | Covered in part by standards map; requires deeper technical comparison |

A workflow registry, workflow language, execution engine, notebook environment, and compute provider solve different problems. They should not be treated as interchangeable.

## 6. Public, participatory, and community-led research

| Project / infrastructure | Main role | Initial status |
|---|---|---|
| [Zooniverse](../../projects/zooniverse.md) | Volunteer classification, transcription, and annotation for research projects | Profiled |
| [SciStarter](../../projects/scistarter.md) | Discovery and recruitment for citizen-science projects | Profiled |
| [iNaturalist](../../projects/inaturalist.md) | Community biodiversity observations, identification, and eligible data export | Profiled |
| [eBird](https://ebird.org/) | Bird observation contributions and biodiversity data infrastructure | Discovery lead |
| [Public Lab](../../projects/public-lab.md) | Community-led environmental monitoring, open tools, and grassroots research | Profiled; current operating status uncertain |
| [Open Humans](../../projects/open-humans.md) | Participant-controlled personal data, self-research, and community research activities | Profiled |
| [Humanitarian OpenStreetMap Team](https://www.hotosm.org/) | Community mapping and open geospatial data for humanitarian use | Discovery lead |
| GLOBE Program, CitSci, Anecdata, FieldScope, and related platforms | Citizen and community science data collection, project hosting, and education | Discovery leads; compare by task and community |

Public participation ranges from contributing a bounded observation or classification to helping define research questions, methods, and priorities. These forms of participation should not be conflated.

## 7. Preservation, access, and continuity

Preservation is not a single product category. It is a set of responsibilities that may be distributed across repositories, libraries, institutional archives, software services, and community networks.

Research questions include:

- What exactly is preserved: files, metadata, software dependencies, execution environments, documentation, or all of these?
- For how long, under what funding and governance arrangements?
- What happens if an operator closes, changes its business model, or withdraws a service?
- Can contributors export their records and move to another provider without losing identifiers, relationships, version history, or attribution?
- Are there independent mirrors, succession plans, or trusted institutional commitments?

## Preliminary patterns

1. **Specialization is normal.** Research planning, methods, data, publishing, discovery, and public participation are served by different kinds of infrastructure.
2. **Interconnection may be more valuable than replacement.** Identifiers, APIs, metadata standards, exports, and stable links are what let the ecosystem function as a whole.
3. **A public interface does not establish public governance.** Services differ in ownership, funding, code openness, membership, and community influence.
4. **Free to use does not mean costless to sustain.** Preservation, curation, moderation, security, support, and migration all require durable resources.
5. **Openness requires boundaries.** Personal data, sensitive ecological locations, and community-controlled knowledge may need access controls or restrictions.
6. **Service continuity is part of scientific integrity.** Research records must remain interpretable and traceable as platforms and organizations change.

## Priority for the next research pass

1. Profile Dataverse, Figshare, and arXiv using primary technical, policy, and governance sources.
2. Investigate Galaxy and Jupyter-based research environments, distinguishing reusable workflows from execution infrastructure.
3. Compare eBird, iNaturalist, Zooniverse, and community-led projects on participant roles, data quality, licensing, and bias.
4. Examine repository exit plans, preservation commitments, and institutional versus commercial governance.
5. Gather independent researcher and community experiences; platform documentation alone cannot establish whether tools meet real needs.

## Limitations

This is a selective map based on initial research. It is weighted toward visible English-language services and does not yet adequately represent regional, multilingual, disciplinary, Global South, Indigenous, or community-governed infrastructures. It is not a systematic review, a complete census, or a recommendation list.

## Change log

- **2026-11-26:** Created an initial categorized directory from the current Workstream A profiles, standards map, and source register. Added discovery leads for the next investigation pass.
