# Workstream A — Standards and Interoperability: Initial Map

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Initial orientation; standards coverage is not exhaustive
- **Workstream:** [A — Open science and research collaboration](README.md)
- **Related field overview:** [Open science and research collaboration](field-overview.md)
- **Source register:** [November 2026 sources](../../sources.md), entries A-31 through A-38

## Why this matters

Research outputs are distributed across repositories, journals, preprint servers, institutional systems, and personal or community websites. A commons that tries to connect them needs reliable ways to identify people, organizations, works, versions, and relationships between research objects.

Interoperability is not achieved simply by making everything available online. Systems need shared identifiers, structured metadata, stable relationships, machine-readable interfaces, and clear rights and access information.

This is an initial map of standards and infrastructure that appear repeatedly in the services reviewed so far. It is not a complete technical specification or recommendation to adopt every standard.

## 1. FAIR Guiding Principles

The FAIR principles—Findable, Accessible, Interoperable, and Reusable—were published in 2016 as guidance for scientific data management and stewardship. The original paper emphasizes both human and machine discovery and reuse, and explicitly applies the principles not only to data but also to algorithms, tools, and workflows.

Important distinctions:

- **Findable** means objects and their metadata can be discovered, including through persistent identifiers and indexing.
- **Accessible** means there is a defined, standardized way to retrieve an object or its metadata. FAIR does not mean every object must be openly downloadable without restriction.
- **Interoperable** means metadata and data can be integrated with other systems using shared representations and vocabularies.
- **Reusable** means sufficient description, provenance, license, and context exist to support responsible reuse.

**Assessment:** FAIR is a useful design framework, but FAIRness is not equivalent to openness, scientific validity, ethical legitimacy, or quality. An identifiable human-subject dataset may be FAIR in the sense that its metadata are findable and access conditions are clear, while the data themselves remain restricted.

## 2. Persistent identifiers and metadata

### DOI, Crossref, and DataCite

DOIs provide persistent identifiers for scholarly outputs. Crossref and DataCite are major DOI registration agencies with different areas of emphasis and overlapping research-output use cases.

- Crossref exposes metadata deposited by members and trusted sources through a public REST API. Records can include titles, contributors, references, funding, license information, ORCID iDs, ROR IDs, and post-publication updates.
- DataCite maintains a metadata schema designed to identify, cite, and retrieve research resources. Schema 4.7 was released on 3 March 2026.
- DataCite guidance distinguishes minor metadata/content updates from major versions and recommends linking major versions using related identifiers.
- Related identifiers can express relationships such as IsNewVersionOf, IsPreviousVersionOf, HasVersion, and IsVersionOf.

**Assessment:** A persistent identifier should identify a clearly defined object or version, and metadata should make relationships between related objects explicit. A DOI is not a guarantee of permanent file availability, scientific quality, or unrestricted access.

### ORCID

ORCID provides persistent identifiers for individual researchers and a registry that can be integrated into research systems. Its public API allows non-member organizations to authenticate ORCID iDs, retrieve public record data, and search public registry records. Additional write and update capabilities are restricted to member API arrangements and user permission.

**Assessment:** Authenticated researcher identifiers can reduce name ambiguity and help connect people to works and contributions. They should remain optional and should not become a barrier to participation for people who do not have or cannot use an ORCID iD.

### ROR

The Research Organization Registry is a community-led registry of open persistent identifiers for research organizations. Its CC0 data are available through a REST API and public data dump. ROR is designed to disambiguate institutions and is supported in Crossref, DataCite, and ORCID metadata workflows.

**Assessment:** ROR demonstrates the value of a shared, open organizational identifier rather than each platform inventing its own institution directory. Its community curation process and governance are worth examining further.

## 3. Metadata harvesting and APIs

### Crossref and OpenAlex APIs

Crossref and OpenAlex provide machine-readable access to large bodies of scholarly metadata. Their records and data models are not identical: Crossref exposes metadata deposited by its members and trusted sources, while OpenAlex aggregates from Crossref, DataCite, PubMed, repositories, and other sources, then attempts to connect records representing the same scholarly work.

**Assessment:** These are complementary discovery resources, not universal or infallible sources of truth. A consumer should retain source attribution, provenance, timestamps, and original identifiers, and should not silently overwrite one source's assertion with an aggregated interpretation.

### OAI-PMH

The Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) is a longstanding protocol for exposing repository metadata to service providers. The Open Archives Initiative notes that OAI-PMH remains widely used in library and academic communities, although the initiative itself is no longer developing new projects.

**Assessment:** OAI-PMH is relevant to repository aggregation and legacy interoperability. It should be assessed alongside contemporary APIs, webhooks, export formats, and notification approaches rather than assumed to be sufficient for every integration.

## 4. Principles for open scholarly infrastructure

The Principles of Open Scholarly Infrastructure (POSI) provide a community-developed framework for evaluating the governance and sustainability of scholarly infrastructure. Version 2.0 was released in October 2025. It includes principles concerning governance, stakeholder representation, participation, and the institutional characteristics of infrastructure.

**Assessment:** POSI is not a technical interoperability standard and does not certify an organization. It is a useful framework for asking whether infrastructure is governed in the public interest and designed for long-term community stewardship. Its principles should be examined critically and applied in context.

## 5. Preliminary interoperability lessons

1. **Preserve original identifiers.** When importing records, retain DOIs, ORCID iDs, ROR IDs, repository identifiers, and source URLs rather than replacing them with local IDs alone.
2. **Represent relationships explicitly.** A preprint, reviewed preprint, version of record, dataset, software release, review, correction, and retraction may all be related but are not interchangeable objects.
3. **Keep provenance.** Record where metadata came from, when it was retrieved, what transformations were applied, and whether a relationship was asserted by a source or inferred by a matching algorithm.
4. **Do not collapse access into openness.** Store access status, license, consent conditions, and restrictions as distinct metadata.
5. **Support export and re-use.** Interoperability requires usable machine-readable exports and documented APIs, not just a search interface.
6. **Treat identifiers as links, not proof.** An identifier helps disambiguate an object; it does not certify the object's correctness or quality.
7. **Expect incomplete metadata.** Missing ORCID iDs, ROR IDs, license fields, abstracts, or version links should be visible as gaps, not silently fabricated.
8. **Design for correction.** Imported metadata and entity matches can be wrong. Users need a way to report errors and trace corrections back to sources.

## 6. Implications for Common Knowledge

At this stage, the most defensible direction is to investigate an interoperability-first approach:

- Reuse established persistent identifiers and metadata standards.
- Link to repositories and publishers rather than assume Common Knowledge should host every research object.
- Maintain a local, auditable layer for relationships, provenance, review status, and corrections where existing systems do not provide adequate cross-platform context.
- Preserve links to exact versions of research objects and their associated data, code, methods, reviews, and corrections.
- Make the data model exportable and document it publicly.
- Avoid requiring institutional affiliation or a specific researcher identifier as a condition of participation.
- Distinguish machine-readable access from legal and ethical permission to reuse content.

This is a research direction, not an architectural decision. It needs validation against actual researcher workflows, disciplinary requirements, and the capabilities and limitations of existing systems.

## 7. Questions still open

1. Which metadata fields are essential for a minimal cross-disciplinary research record?
2. Which identifier schemes are widely adopted beyond conventional academic publishing?
3. How should Common Knowledge represent a work with multiple preprint, accepted-manuscript, published, corrected, and retracted versions?
4. How can source assertions be distinguished from algorithmically inferred links?
5. Which standards are most appropriate for research software, workflows, instruments, samples, and AI-generated artifacts?
6. What repository notification or synchronization mechanisms are used in practice?
7. How should access conditions, licenses, consent, and community authority be represented in machine-readable form?
8. What are the practical limits of FAIR and POSI, and where do communities need complementary safeguards?

## Sources

- A-31 — Wilkinson et al. (2016), FAIR Guiding Principles.
- A-32 — DataCite Metadata Schema 4.7.
- A-33 — DataCite versioning guidance.
- A-34 — Crossref REST API documentation.
- A-35 — ORCID Public API documentation.
- A-36 — Research Organization Registry (ROR).
- A-37 — Open Archives Initiative specifications.
- A-38 — Principles of Open Scholarly Infrastructure, version 2.0.

## Change log

- **2026-11-26:** Created initial standards and interoperability map from primary standards and infrastructure documentation. Further implementation-level and disciplinary review remains necessary.
