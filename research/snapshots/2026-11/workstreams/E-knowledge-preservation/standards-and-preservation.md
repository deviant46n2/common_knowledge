# Workstream E — Metadata, Interoperability, and Preservation Standards

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Initial standards map; implementation and adoption evidence still needed
- **Workstream:** [E — Shared knowledge and preservation](README.md)

## 1. Descriptive metadata: Dublin Core

The Dublin Core Metadata Initiative maintains a vocabulary of metadata terms, including title, creator, subject, description, publisher, date, type, format, identifier, language, rights, provenance, and relationships such as isPartOf, hasPart, isVersionOf, and references.

**Role:** A general-purpose descriptive vocabulary that can help systems exchange a basic description of resources.

**Limits:** A vocabulary is not a complete application profile. Different systems may select different fields, interpret them differently, or omit important domain-specific context. Dublin Core alone does not express a full scholarly, archival, scientific, or cultural record.

## 2. Semantic organization: SKOS

The W3C Simple Knowledge Organization System (SKOS) is a data model for sharing and linking knowledge organization systems. It supports concept URIs, preferred and alternative labels, multilingual labels, definitions and notes, broader/narrower relationships, associative links, collections, and mappings between concept schemes.

**Role:** A practical bridge for publishing and connecting taxonomies and thesauri without requiring every vocabulary to become a formal ontology.

**Limits:** SKOS can express concept relationships but does not automatically settle conceptual disagreements, guarantee translation quality, or define a universal classification. Different communities may legitimately organize knowledge differently.

## 3. Repository metadata exchange: OAI-PMH

OAI-PMH 2.0 defines an application-independent framework for metadata harvesting. Data providers expose structured metadata; service providers harvest it to build discovery or other services. The protocol defines six verbs and uses HTTP.

The OAI FAQ makes an important boundary explicit: OAI-PMH harvests XML-formatted metadata. It does not itself provide a general mechanism for harvesting arbitrary associated content. Repositories can include links from metadata records to content.

**Role:** A mature, relatively low-barrier mechanism for aggregating records across repositories.

**Limits:** Harvesting can be incomplete, delayed, or inconsistent. The protocol does not guarantee the quality of metadata, full-text access, file preservation, or semantic equivalence. Harvesters must handle deletions, resumption tokens, datestamps, and provider-specific behavior carefully.

The OAI website states that no new OAI projects are being developed, while the existing specifications and site continue to be maintained. OAI-PMH remains widely used in library and academic settings. This distinction matters when evaluating future evolution and maintenance.

## 4. Digital-object presentation: IIIF

The International Image Interoperability Framework (IIIF) publishes APIs for interoperable access to digital objects. The Presentation API describes compound objects such as books, manuscripts, collections, films, and audio works for rich viewers; the Image API standardizes image requests. The current API index identifies version 3.0.0 for both Image and Presentation APIs.

**Role:** An example of domain-focused interoperability that makes high-resolution images and complex objects usable across institutions and viewers. Presentation API 3.0 includes multilingual labels, structural ranges, annotations, and links to services.

**Limits:** IIIF is specialized for digital object presentation and related services, not a universal knowledge graph, metadata schema, or preservation system. Access control, licensing, and rights remain the responsibility of the service and its institutions.

## 5. Preservation metadata: PREMIS

The Library of Congress describes PREMIS as a comprehensive resource for implementing preservation metadata in digital archiving systems. PREMIS 3.0 defines four entities: Objects, Events, Rights, and Agents. It is intended to capture information needed to support the long-term preservation of digital materials.

**Role:** A preservation-focused model for documenting what is preserved, what preservation events occurred, who or what performed them, and the rights relevant to preservation actions.

**Limits:** PREMIS is a metadata model and data dictionary, not a preservation service, repository, funding model, or guarantee that an object will remain usable. Implementations must decide which semantic units and events are necessary.

## 6. Distributed preservation: LOCKSS and CLOCKSS

### LOCKSS

The LOCKSS Program describes a distributed preservation system in which participating nodes ingest content, audit copies, compare holdings, and repair damaged or missing content from other nodes. It supports multiple ingest mechanisms, including OAI-PMH, BagIt, publisher harvesting, and other routes. Different LOCKSS networks can have different participation and access models.

### CLOCKSS

CLOCKSS is an independent nonprofit archive governed by libraries and publishers and built on LOCKSS technology. Its 12 nodes are hosted at major academic libraries. Content is preserved in a dark archive and released after a defined trigger event and board decision. CLOCKSS documentation says that when a correction or retraction is communicated by a publisher, the updated article or a tombstone notice is captured while the original remains preserved in the archive.

**Assessment:** These systems show that preservation can be federated across institutions with shared audit and repair, while governance and access policies remain explicit. CLOCKSS's dark-archive trigger model is different from an always-open mirror. The distinction between preservation copy and public access is fundamental.

**Limits and questions:** Published descriptions are primarily operator sources. The snapshot has not yet independently audited holdings, coverage, financial reserves, trigger decisions, or service continuity. Preservation networks may cover particular classes of content and not the entire research record.

## 7. Wikidata and Wikibase: collaborative structured knowledge

Wikidata provides a public collaborative knowledge base. Wikibase is software for operating structured knowledge repositories. The Wikibase documentation explains that instances can define their own data models and connect properties across vocabularies, but warns that a lack of a shared ontology can make interoperability harder.

**Role:** A useful example of entity-centered knowledge records, references, qualifiers, community editing, identifiers, and queryable data. It demonstrates both the power and governance challenges of collaborative knowledge graphs.

**Limits:** A flexible knowledge graph can become an isolated schema ecosystem. Data quality, source quality, coverage, editor participation, dispute resolution, and governance need separate assessment. Not all knowledge is suitable for representation as public, decontextualized statements.

## 8. Emerging synthesis: standards should be composed, not confused

A plausible stack for a distributed knowledge commons may include:

| Need | Candidate standards / infrastructure | What it does not solve alone |
|---|---|---|
| Basic description | Dublin Core, Schema.org, domain metadata | Full semantic context or quality |
| Concept organization | SKOS, domain ontologies | Contested meaning or universal classification |
| Record exchange | OAI-PMH, APIs, ResourceSync | Full content transfer or preservation |
| Scholarly identity and links | DOI, ORCID, ROR, DataCite, Crossref | Correctness of the linked resource |
| Digital-object presentation | IIIF | General knowledge representation or archival custody |
| Research-object context | RO-Crate, PROV | Long-term storage or correctness |
| Preservation events and rights | PREMIS | Preservation operations and sustainable funding |
| Package integrity | BagIt, checksums | Authenticity, custody, interpretability |
| Distributed preservation | LOCKSS, CLOCKSS | Universal coverage or all access rights |

This table is an orientation, not a final architecture. Standards may overlap and can be combined. Their actual compatibility and implementation costs need to be tested.

## 9. Design questions

1. Can a record be exported in a form that preserves identifiers, sources, rights, language, version history, and relationships?
2. Can an independent system reconstruct a useful view without depending on one vendor's API?
3. How are provenance and metadata corrections propagated to aggregators?
4. Can a system preserve multiple valid labels and classifications without forcing one authoritative taxonomy?
5. Can restricted resources remain discoverable without exposing protected content?
6. Can preservation obligations and exit procedures be verified rather than merely promised?

## Sources

See the [November 2026 source register](../../sources.md), entries E-01 onward.

## Change log

- **2026-11-26:** Added first-pass descriptions and limitations for Dublin Core, SKOS, OAI-PMH, IIIF, PREMIS, LOCKSS/CLOCKSS, and Wikidata/Wikibase.
