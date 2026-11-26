# Workstream E — Persistent Identifiers and Scholarly Authority Records

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Initial landscape; coverage and governance comparison remains open
- **Workstream:** [E — Shared knowledge and preservation](README.md)

## 1. Why identifiers matter

A title, author name, institution name, or web address is often not enough to identify a resource reliably. Names vary, people share names, organizations change, resources move, and one intellectual work may exist as multiple versions, translations, datasets, software releases, or physical copies.

Persistent identifiers help systems refer to entities consistently. But an identifier is not the entity itself, and persistence is not magic: the identifier's resolution, metadata, governance, and underlying resource still depend on organizations and technical services.

A knowledge commons should distinguish:
- Identifier assignment from metadata quality.
- A persistent identifier from a permanent copy of the resource.
- A work from its editions, manifestations, versions, and individual copies.
- A person from their name strings and claimed affiliations.
- An organization from its names, units, locations, and historical successors.

## 2. DOI infrastructure: Crossref and DataCite

### Crossref

Crossref members register DOIs and deposit or update associated metadata for scholarly and professional research outputs. The public REST API exposes metadata deposited by members and trusted sources, including bibliographic information, funding, licenses, post-publication updates, ORCID and ROR identifiers, and abstracts where available. Crossref's public API requires no sign-up, although rate limits and service tiers apply.

**Role:** A major metadata and linking infrastructure for journal articles, books, proceedings, and other scholarly content. It can provide discovery, citation links, and publication-status information.

**Limits:** Crossref metadata is largely member-deposited, with some augmentation from trusted external sources. A DOI can resolve to a landing page whose content is inaccessible, moved, or changed. The presence of a DOI does not certify peer review, scientific quality, open access, or preservation of underlying data. Crossref covers Crossref-registered DOIs; it is not the only DOI registration agency.

### DataCite

DataCite's metadata schema is designed for identifying, citing, and retrieving research data and other research outputs. Version 4.7 was released on 3 March 2026. The release added resource types including Poster and Presentation, related identifier types including RAiD and SWHID, and additional relation metadata.

DataCite supports describing relationships between outputs and identifiers, including versions, translations, related works, and other resources. Its documentation emphasizes including version information when citing software.

**Role:** Particularly relevant for datasets, software, samples, instruments, and other research outputs that need persistent citation and explicit relationships.

**Limits:** Schema conformance depends on what repositories actually deposit. Metadata completeness and accuracy vary. A DOI is only as useful as its landing page, metadata maintenance, rights, and long-term stewardship.

## 3. Person identifiers: ORCID

ORCID provides persistent identifiers for researchers and a record for connecting people with their research activities and affiliations. ORCID documentation emphasizes authenticated collection of ORCID iDs rather than manually entering an identifier where authentication is possible. Updating a researcher's record through the member API requires the record holder to grant permission.

**Role:** Helps disambiguate people with similar names and supports trusted links between researchers, contributions, and affiliations.

**Limits:** ORCID is not a universal identity system or proof that every item in a record is accurate. Records may be incomplete, and the researcher retains control over permissions. A platform should not treat an ORCID iD as blanket consent to expose or republish personal information.

## 4. Organization identifiers: ROR

The Research Organization Registry (ROR) describes itself as a global, community-led registry of open persistent identifiers for research and funding organizations. ROR records include names and variants, multilingual names, locations, websites, and mappings to other identifiers. ROR data are CC0 and available through a REST API and bulk data dump; updates are curated through a community process and released approximately monthly.

ROR intentionally focuses on broad, inclusive coverage of research organizations rather than detailed internal organizational structures.

**Role:** A useful open authority layer for disambiguating institutional affiliations, funders, and research organizations.

**Limits:** It does not attempt to model every department, laboratory, local community, or complex institutional relationship. Organizational identity and succession can be difficult, and registry records need continuing curation.

## 5. Library authority and bibliographic models: BIBFRAME

The Library of Congress developed BIBFRAME as a linked-data model for bibliographic description and as a transition path from MARC 21. BIBFRAME 2.0 distinguishes three core levels:
- **Work:** the conceptual essence of a resource.
- **Instance:** a particular published form or embodiment.
- **Item:** an actual physical or electronic copy.

The model also includes agents, subjects, and events, with relationships among resources.

**Role:** A mature library-sector effort to represent bibliographic relationships and authority information as linked data. It highlights the importance of distinguishing intellectual works from editions and individual copies.

**Limits:** It is designed for bibliographic description, not a universal scientific knowledge model. Mapping between BIBFRAME, Dublin Core, Schema.org, DataCite, and local cataloguing systems requires care.

## 6. Implications for a federated knowledge commons

A useful record should be able to link to multiple identifiers without assuming they all identify the same kind of thing. For example:
- A research article may have a DOI, Crossref metadata, an ORCID for each contributor, and ROR identifiers for affiliations.
- A dataset may have its own DOI through DataCite, a version relation to earlier deposits, and a link to the article that describes it.
- A software project may have a repository URL, a version-specific release, and a software identifier such as SWHID.
- A book may be represented as a Work, one or more publication Instances, and separate Items held by libraries.

The goal should be to preserve these distinctions and relationships rather than flatten everything into a single generic “document” record.

## 7. Open questions

1. How should Common Knowledge reconcile duplicate or conflicting metadata without silently overwriting source records?
2. How should it represent entities with no established identifier?
3. Which identifier types are persistent at the entity level, and which are version- or manifestation-specific?
4. How should identity links be authenticated, corrected, or disputed?
5. What is the policy for storing locally cached metadata when upstream providers change or disappear?
6. How should identifiers and authority records work for oral histories, community knowledge, Indigenous knowledge, local groups, and non-institutional contributors?
7. What should happen when an organization merges, dissolves, changes names, or disputes an identifier record?

## Sources

See the [November 2026 source register](../../sources.md), entries E-11 onward.

## Change log

- **2026-11-26:** Added an initial comparison of Crossref, DataCite, ORCID, ROR, and BIBFRAME, emphasizing entity distinctions, metadata governance, and limitations of persistent identifiers.
