# Workstream E — Initial Field Overview: Shared Knowledge and Preservation

- **Snapshot:** November 2026
- **Research cutoff:** 26 November 2026
- **Status:** Preliminary orientation; not a systematic review
- **Workstream:** [E — Shared knowledge and preservation](README.md)

## 1. Central problem

Human knowledge is distributed across publications, datasets, software, archives, libraries, collections, databases, oral histories, community records, educational materials, and individual expertise. These resources use different formats, identifiers, vocabularies, rights regimes, and preservation arrangements.

A shared knowledge commons must do more than gather documents in one place. It needs to make resources discoverable, distinguishable, attributable, interpretable, linkable, reusable where appropriate, and durable across changes in technology and institutions.

This is not a claim that all knowledge should be centralized. A useful commons may be a network of independently stewarded resources connected by open identifiers, metadata, standards, links, and governance agreements.

## 2. Distinctions that matter

- **Knowledge representation:** How concepts, claims, sources, relationships, uncertainty, and context are expressed.
- **Metadata:** Structured information describing a resource, such as its title, creator, date, format, rights, subject, and relationships.
- **Knowledge organization system (KOS):** A controlled vocabulary, taxonomy, thesaurus, classification scheme, ontology, or related structure used to organize concepts.
- **Knowledge graph:** A graph-shaped representation of entities and relationships; the term covers a range of models and implementations and does not imply quality or truth.
- **Discovery:** Finding relevant resources through search, indexing, catalogues, identifiers, and links.
- **Access:** Being able to retrieve or consult a resource, potentially under authentication, licensing, consent, or community governance conditions.
- **Interoperability:** The ability of separate systems to exchange and meaningfully use information. It includes technical, syntactic, semantic, organizational, and legal dimensions.
- **Preservation:** Maintaining the integrity, authenticity, interpretability, and accessibility of information over time, including the ability to respond to format and technology changes.
- **Stewardship:** Ongoing responsibility for the quality, rights, context, maintenance, and continuity of a resource.

These are related but not interchangeable. A resource can be discoverable but inaccessible, accessible but not reusable, copied but not preserved, preserved but uninterpretable, or technically interoperable while semantically misunderstood.

## 3. A layered knowledge infrastructure

The initial landscape suggests several layers:

1. **Identifiers and authority records:** Persistent identifiers for works, people, organizations, places, concepts, datasets, and versions.
2. **Descriptive metadata:** Common fields and vocabularies for identifying and describing resources.
3. **Semantic organization:** Controlled vocabularies, taxonomies, ontologies, mappings, and multilingual labels.
4. **Aggregation and discovery:** Harvesting, indexing, search, cross-repository discovery, and entity resolution.
5. **Content delivery and annotation:** Access to documents, images, audio, video, manuscripts, datasets, and annotations.
6. **Versioning and provenance:** Links between editions, revisions, sources, transformations, corrections, and contributors.
7. **Preservation and continuity:** Fixity, replication, format migration, audit, custody, rights, and succession.
8. **Governance and rights:** Stewardship, consent, licensing, access restrictions, cultural authority, and dispute resolution.

No single standard covers all layers. The goal is to understand how existing systems fit together and where interoperability breaks down.

## 4. Early standards and infrastructure signals

### Descriptive metadata and knowledge organization

- **Dublin Core Metadata Terms** provide a widely used vocabulary for describing resources, including title, creator, date, format, identifier, language, rights, provenance, and relations.
- **SKOS**, a W3C Recommendation, provides a model for sharing and linking knowledge organization systems such as thesauri, taxonomies, classification schemes, and subject heading systems. It supports concept identifiers, multilingual labels, notes, hierarchies, associations, and mappings.
- **IIIF Presentation API** provides interoperable descriptions for compound digital objects such as books, manuscripts, images, films, and audio collections. It supports structured presentation, multilingual labels, annotations, and links to content services.

### Metadata exchange and aggregation

- **OAI-PMH** provides a low-barrier protocol for harvesting structured metadata from repositories. It is an exchange mechanism, not a full-text or arbitrary-file transfer protocol.
- The Open Archives Initiative notes that its specifications continue to be maintained even though it is no longer developing new projects. OAI-PMH remains widely used in library and academic repository contexts.
- Metadata aggregation can improve discovery while also propagating source errors, stale records, duplicate entities, and uneven coverage. A harvested record should preserve its source and retrieval history.

### Digital preservation

- **PREMIS** provides a data dictionary and model for preservation metadata, including Objects, Events, Rights, and Agents.
- **BagIt** supports transfer packages and checksum-based fixity checks, but does not by itself provide a preservation institution or long-term access.
- **LOCKSS** uses distributed copies, audits, and repair among participating nodes to preserve digital content.
- **CLOCKSS** is a library- and publisher-governed nonprofit dark archive based on LOCKSS technology. It preserves scholarly publications and makes content openly available following a defined trigger process.

### Knowledge graphs and community models

- **Wikidata/Wikibase** illustrate collaborative, structured knowledge with identifiers, statements, qualifiers, references, and query tools.
- Wikibase offers flexibility to define local data models, but that flexibility can reduce interoperability when different installations use incompatible schemas or vocabularies.
- A knowledge graph's existence does not guarantee reliable sourcing, balanced coverage, stable governance, or appropriate representation of contested knowledge.

These are initial examples, not a comprehensive map or an endorsement list.

## 5. Preservation is an institutional and social problem as well as a technical one

Copies, checksums, open formats, and redundant storage are important but insufficient. Long-term preservation also requires:
- A custodian with durable responsibility.
- Funding and operational capacity.
- Clear rights to retain, migrate, and provide access.
- Documented formats, dependencies, and technical context.
- Procedures for detecting corruption and repairing copies.
- Plans for organizational closure, transfer, and succession.
- Respect for privacy, consent, cultural authority, and legitimate restrictions.

A decentralized network of copies can reduce dependence on one server, but does not automatically solve legal custody, financial sustainability, or accountability.

## 6. Early implications for Common Knowledge

The strongest early hypothesis is that Common Knowledge should first investigate an **interoperable federation of existing knowledge resources**, not assume that it should build a single master repository or universal knowledge graph.

Potential roles worth investigating:
- Connect records through persistent identifiers and explicit source links.
- Preserve provenance and version history when aggregating metadata.
- Map vocabularies rather than force every contributor into one taxonomy.
- Provide a human-readable path from discovery record to primary source.
- Support multiple formats, languages, and community-defined access conditions.
- Make export, mirroring, and preservation plans explicit.
- Distinguish verified facts, source claims, interpretation, uncertainty, and disagreement.

This is a research hypothesis, not an architectural decision.

## 7. Questions for the next research pass

1. Which identifiers and authority systems provide durable links for works, people, institutions, datasets, concepts, and versions?
2. How do Dublin Core, Schema.org, DataCite, Crossref, BIBFRAME, SKOS, PROV, and RO-Crate map to one another in real systems?
3. How much useful content can be discovered through OAI-PMH, APIs, ResourceSync, and linked-data interfaces, and what remains inaccessible?
4. How do preservation networks differ in governance, trigger rules, funding, rights, and actual coverage?
5. How should a knowledge commons represent conflicting claims, contested classifications, and revisions without flattening disagreement?
6. How can multilingual and low-bandwidth access be supported?
7. What does respectful stewardship require for Indigenous, local, oral, and community-controlled knowledge?
8. Which existing knowledge graph or repository tools have healthy governance, portability, and sustainable communities?

## 8. Scope and limitations

This is a first technical orientation, weighted toward library, scholarly, and web standards. It does not yet adequately cover oral history, Indigenous data sovereignty, community archives, non-written knowledge, accessibility, multilingual discovery, educational knowledge, or preservation of dynamic software and web applications. The November 2026 snapshot must not be treated as a complete census.

## Sources

See the [November 2026 source register](../../sources.md), entries E-01 onward.

## Change log

- **2026-11-26:** Created initial field overview and mapped the first standards and infrastructure layers for metadata, semantic organization, harvesting, digital objects, and preservation.
