# Focused Research — Knowledge Records, Evidence, and Provenance

- **Research started:** 26 November 2026
- **Status:** Initial desk research; partial and not independently reviewed
- **Purpose:** Inform the first Common Knowledge knowledge-system demonstrator.

## Working question

What is the smallest useful, interoperable way to represent a knowledge statement together with its scope, evidence, sources, provenance, uncertainty, disagreement, and revision history—and what existing systems already do this well?

This document records a first pass through selected primary documentation. It is not a comprehensive survey and does not establish that a product gap exists.

## Initial findings

### 1. Structured statements with references and qualifiers already exist

Wikidata statements are not just bare subject–predicate–object assertions. A statement can include a value, qualifiers that contextualize it, references, and a rank. Wikidata also distinguishes unknown values from explicit absence and warns that some qualifiers change the scope or applicability of a statement.

**Implication:** Common Knowledge should not invent a simplistic claim/value/source schema without studying Wikibase's data model. Scope, time, place, and unknown-versus-no-value distinctions are important.

Sources:
- Wikidata, [Help:Statements](https://www.wikidata.org/wiki/Help:Statements)
- Wikidata, [Data model](https://www.wikidata.org/wiki/Wikidata:Data_model)

### 2. Provenance has a mature, general-purpose standard

W3C PROV-O models provenance through three central concepts: Entity, Activity, and Agent. It can describe what was used, what was generated, how entities were derived, and which agents were associated with activities or attributed to entities. It is intentionally extensible and can be adopted incrementally.

**Implication:** Common Knowledge should investigate mapping its record history and contribution trail to PROV-O rather than designing a proprietary provenance vocabulary by default. PROV-O does not, by itself, define a complete knowledge-record or evidence-assessment model.

Source:
- W3C, [PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/)

### 3. Nanopublications package small assertions with provenance

The nanopublication model separates an assertion graph, provenance graph, publication-information graph, and a head graph linking them. The guidelines describe small, citable structured assertions and preserve the provenance of the assertion separately from the provenance of the publication object.

**Implication:** This is a particularly relevant candidate for testing small, independently citable knowledge contributions. We need hands-on tests of authoring, identifiers, signatures, querying, updates, and long-term availability before deciding whether it fits a human-friendly product workflow. A nanopublication is a packaging model, not a complete public knowledge institution.

Sources:
- Nanopublications, [Guidelines](https://nanopub.net/docs/guidelines/)
- Nanopublications, [Handbook: Nanopublication](https://nanopub.net/docs/handbook/nanopublication/)

### 4. RDF and SKOS provide useful interoperability building blocks

RDF provides a graph-based data model based on subject–predicate–object triples. SKOS provides a lightweight model for concepts, multilingual labels, definitions, hierarchical and associative relationships, and mappings between concept schemes.

**Implication:** RDF and SKOS may help represent links and controlled vocabularies, but adopting RDF does not automatically solve evidence quality, usability, version history, or governance. We should test only the portions that serve the chosen workflow.

Sources:
- W3C, [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf-concepts/)
- W3C, [SKOS Reference](https://www.w3.org/TR/skos-reference/)

### 5. Existing scholarly knowledge graphs are large and useful, but serve a different purpose

OpenAlex describes a connected graph of scholarly works, authors, sources, institutions, topics, funders, and related entities, with an API and downloadable data. Its records and curation connect the scholarly ecosystem at scale.

**Implication:** Common Knowledge should not attempt to recreate a scholarly index. OpenAlex may be an upstream source for research objects and identifiers, but it is not a general-purpose system for preserving evidence-to-statement assessments, competing interpretations, or a transparent history of public knowledge records.

Sources:
- OpenAlex, [API reference](https://help.openalex.org/api/)
- OpenAlex, [Data reference](https://help.openalex.org/data/)
- OpenAlex, [How it's built](https://help.openalex.org/data/how-its-built/)

### 6. Fact-checking markup is narrower than the wider knowledge-system problem

Schema.org's ClaimReview describes a fact-check review of claims made or reported in another work. Google's documentation says support for ClaimReview markup in Google Search is being phased out, while it remains supported in Factcheck Explorer.

**Implication:** ClaimReview is worth understanding as an interchange format for a specific kind of claim review, but it is not an adequate foundation for the entire Common Knowledge data model. We should avoid defining the product as a political fact-checking site.

Sources:
- Schema.org, [ClaimReview](https://schema.org/ClaimReview)
- Google Search Central, [Fact check structured data](https://developers.google.com/search/docs/appearance/structured-data/factcheck)

## Preliminary synthesis

The initial sources point toward a layered approach rather than a single all-purpose schema:

- A human-readable record with explicit statement and scope.
- Distinct source objects and evidence locations.
- Typed relationships between evidence and statements.
- An assessment layer that records method, reasoning, uncertainty, and authorship.
- Provenance for the creation and transformation of records.
- Versioning and correction history.
- Export or mapping to established formats where possible.

This is a working synthesis, not a chosen architecture. Wikibase, nanopublications, RDF/PROV-O, and domain-specific knowledge bases solve overlapping but different problems. Their practical usability and interoperability need to be tested.

## Important unknowns

- Can Wikibase support the desired workflow without extensive customization?
- Are nanopublications practical for human authoring and review, or mainly for machine-oriented publication?
- How should evidence passages and dataset observations be identified durably?
- How should multiple assessments coexist without creating an unhelpful proliferation of duplicate records?
- What revision and correction model best preserves history while allowing straightforward updates?
- Which parts should be structured as RDF, and which are better represented in ordinary documents or relational data?
- What real user group has this problem urgently enough to use an early tool?

## Next research actions

1. Build one example record in Wikibase or a Wikibase test instance and inspect its export/API representation.
2. Create and publish a tiny nanopublication using the documented tooling; test its identifiers, provenance, signature, and retrieval.
3. Map the same example into a simple PROV-O model and note what PROV-O does not express.
4. Compare what a human can understand and edit in each representation without specialist semantic-web knowledge.
5. Identify one real workflow and speak with people who currently perform it.
6. Only then propose the minimum record format and prototype architecture.

## Scope and limitations

This first pass used selected official documentation and did not run software, interview users, inspect all relevant projects, or independently validate every implementation claim. The descriptions above are summaries of what the cited sources document, not claims that the systems were tested. Research cutoff: 26 November 2026.


## Deeper comparison: practical strengths and cautions

### Wikibase is a mature collaborative editing system, but its RDF export has important semantics

The Wikibase REST API supports retrieving and editing Items, Properties, and Statements. Its data model is JSON-based and includes references, qualifiers, and ranks. MediaWiki provides page revision histories with timestamps, contributors, diffs, and the ability to view or compare earlier revisions.

However, the RDF export distinguishes a simplified "truthy" view from full statements. The truthy view selects the best non-deprecated rank and ignores qualifiers. Consumers who need the complete context must use the full statement representation.

**Implication:** Wikibase is a serious candidate for a working prototype or integration, especially if collaborative editing and revision history matter. But Common Knowledge must not mistake its simplified RDF projection for the complete semantics of a scoped statement. Test the actual export and API data before designing around it.

Sources:
- Wikidata, [REST API](https://www.wikidata.org/wiki/Wikidata:REST_API)
- MediaWiki, [Help:History](https://www.mediawiki.org/wiki/Help:History)
- MediaWiki, [Wikibase RDF dump format](https://www.mediawiki.org/wiki/Wikibase/Indexing/RDF_Dump_Format)
- MediaWiki, [Wikibase FAQ](https://www.mediawiki.org/wiki/Wikibase/FAQ/en)

### Nanopublications already provide a substantial end-to-end ecosystem

The current Nanopublications documentation describes more than a data format. It includes:
- Nanodash, a browser interface for reading, searching, and publishing with templates;
- command-line tooling for checking, signing, publishing, retracting, and querying;
- Java, Python, JavaScript/TypeScript, and Rust libraries;
- a decentralized registry and query architecture;
- a separate test network for experimentation.

Nanopublications are immutable and use content-derived Trusty URIs; revised or withdrawn content is handled through new publications and explicit superseding or retraction relationships. The current ecosystem also supports signatures.

**Implication:** This is not merely an academic format to cite. It is an existing, functioning candidate ecosystem that Common Knowledge should test hands-on before writing a competing publishing layer. Its immutability and small assertion units may be valuable for preserving evidence-linked contributions, while its human authoring workflow, discoverability, and suitability for broader non-scientific knowledge need evaluation.

Sources:
- Nanopublications, [Tools](https://nanopub.net/docs/tools/)
- Nanopublications, [Technical Architecture](https://nanopub.net/docs/architecture/)
- Nanopublications, [Nanopublication structure and identifiers](https://nanopub.net/docs/guidelines/)
- Nanopublications, [Handbook: Nanopublication](https://nanopub.net/docs/handbook/nanopublication/)

### Identity trust and content assessment are separate problems

The Nanopublications trust documentation explicitly separates identity verification from content evaluation. A signature establishes that content was signed with a particular key; a trust network's approvals establish whether that key is accepted as belonging to the named person or agent. Neither mechanism determines whether the published assertion is correct.

**Implication:** This distinction is foundational for Common Knowledge. Authentication, authorization, contributor reputation, source credibility, and evidential support must not be collapsed into one trust score. A verified identity does not make a claim true, and an unknown contributor's evidence should not be discarded solely because their identity is not yet trusted.

Source:
- Nanopublications, [Trust and approval](https://nanopub.net/docs/handbook/trust-and-approval/)

## Updated preliminary comparison

| Candidate | Strong fit | Important limitation or question |
|---|---|---|
| Wikibase | Structured statements, qualifiers, references, collaborative editing, revision history, APIs | How well does its item/property model support evidence assessments and competing interpretations? Beware simplified RDF exports that omit qualifiers |
| Nanopublications | Small citable assertions, immutable identifiers, signatures, provenance, decentralized publication and query tools | Is the authoring/review experience approachable for ordinary contributors and non-specialist domains? |
| RDF + PROV-O | Interoperable graph representation and general provenance vocabulary | Requires an application-specific model and user experience; standards do not supply product workflows |
| SKOS | Concepts, multilingual labels, definitions, and mappings between vocabularies | Not a claim/evidence assessment model |
| OpenAlex | Large-scale scholarly entity graph and open API/data | Research-indexing and entity-linking focus, not general public knowledge assessment |
| ClaimReview | Interchange metadata for a fact-check review | Narrow review type; not a general-purpose knowledge model |

This comparison is qualitative and based on documentation, not a benchmark or hands-on evaluation.


## Wikibase deep dive — data model, operations, and fit

**Research date:** 26 November 2026  
**Method:** Official documentation review, including the conceptual data model, RDF export documentation, REST API documentation, permissions, installation, and maintenance guides. No Wikibase instance has yet been deployed or exercised.

### Data model: stronger than a simple triple store

Wikibase statements have a main snak, optional qualifier snaks, zero or more reference records, and a rank. A snak can express:
- a concrete property value;
- an explicit no-value assertion (the property really has no value);
- an unknown/some-value assertion (a value exists but is not known).

This distinction is valuable for epistemic records: omitted data, unknown data, and an asserted absence should not be conflated. Qualifiers can encode contextual details such as a validity period. References are structured records, not limited to a single URL; they can include several source attributes such as title, author, publisher, and page/chapter.

A statement has one main value, but can have multiple qualifiers and references. This is useful for cataloguing sourced facts, but it does not natively provide a rich model for a single claim being supported by one evidence passage, challenged by another, and assessed by multiple independent reviewers. Those relationships would need to be modeled through additional entities/properties or an application layer.

Sources:
- MediaWiki, [Wikibase Data Model](https://www.mediawiki.org/wiki/Wikibase/DataModel)
- MediaWiki, [Wikibase RDF Dump Format](https://www.mediawiki.org/wiki/Wikibase/Indexing/RDF_Dump_Format/en)

### RDF export: two materially different views

Wikibase's RDF export has a simplified truthy view and a full statement view:
- The truthy view selects the best non-deprecated rank for each property (preferred statements when present, otherwise normal statements) and ignores qualifiers.
- The full view represents statements as separate nodes and includes rank, qualifiers, and references.
- Statement identifiers in the RDF mapping are not guaranteed to have a stable semantic format.

This is not a minor serialization detail. A consumer using only truthy triples can lose the time, place, or other qualifiers that make a statement accurate. Any Common Knowledge integration must explicitly choose the full representation when preserving context, and should test whether exported statement identifiers are suitable for long-lived external references rather than assuming they are.

Source:
- MediaWiki, [Wikibase RDF Dump Format](https://www.mediawiki.org/wiki/Wikibase/Indexing/RDF_Dump_Format/en)

### APIs and query access

The Wikibase REST API is an OpenAPI-described interface for retrieving and editing Items, Properties, and Statements. Wikidata exposes it under `/w/rest.php/wikibase/v1`. The documentation says the REST API is still being actively improved; Wikidata intends it to functionally replace the older Action API for Wikibase-specific use cases. For large result sets, bulk data dumps are preferable; search and SPARQL query services are better suited to discovery and query workloads.

This suggests a clean division of responsibilities is possible: use entity APIs for editing and retrieval, a query service for graph-style exploration, and dumps for bulk export. But these are separate operational pieces, not one turnkey API/database.

Sources:
- Wikidata, [REST API](https://www.wikidata.org/wiki/Wikidata:REST_API/en)
- Wikidata, [Data access](https://www.wikidata.org/wiki/Wikidata:Data_access/en)

### Revision history and permissions

Wikibase runs on MediaWiki, so it inherits MediaWiki's page revision model: edits create revisions with timestamps and actors, and prior revisions can be inspected and compared. Wikibase also has fine-grained rights for operations such as editing entities, creating properties, editing terms, merging items, and redirecting entities. Rights are assigned to user groups and can be configured by the site operator.

This is a strong foundation for collaborative editing and accountable change history. It is not, however, equivalent to a dedicated scientific review workflow: revision authorship says who changed a record, not who independently reviewed its evidence or what review method they used. A product built on Wikibase would need to make those distinctions explicit.

Sources:
- MediaWiki, [Help:History](https://www.mediawiki.org/wiki/Help:History)
- MediaWiki, [Wikibase Permissions](https://www.mediawiki.org/wiki/Wikibase/Permissions)
- MediaWiki, [Revision table](https://www.mediawiki.org/wiki/Manual:Revision_table/en)

### Deployment and operational burden

Wikibase is an extension to MediaWiki, with Repository and Client components. A basic installation requires MediaWiki and the Wikibase extension; a fuller suite can add a query service, Elasticsearch, QuickStatements, and related services. The official maintenance guide lists separate containers/services for Wikibase/MediaWiki, MariaDB, Elasticsearch, QuickStatements, and the WDQS stack/proxy/frontend.

A Docker suite makes evaluation approachable, but the complete stack is not a tiny application to operate. The official quick-start guide itself describes the broader suite as complex to install and manage. A hosted Wikibase option exists, but availability and terms need to be checked at the time of any actual evaluation.

Sources:
- MediaWiki, [Wikibase Quick start](https://www.mediawiki.org/wiki/Wikibase/Quick_start)
- MediaWiki, [Wikibase Maintaining](https://www.mediawiki.org/wiki/Wikibase/Maintaining)
- MediaWiki, [Wikibase extension overview](https://www.mediawiki.org/wiki/Extension:Wikibase)

### Maintenance and licensing observations

The Wikibase Repository and Client extensions are documented as GPL-2.0-or-later. The Wikibase FAQ identifies Wikimedia Deutschland as the primary maintainer of the extension, while noting that several surrounding suite components are maintained by other parties. This means the core project has an identifiable institutional maintainer, but operating the full stack still means depending on multiple components and release/compatibility practices.

Sources:
- MediaWiki, [Wikibase Repository extension](https://www.mediawiki.org/wiki/Extension:Wikibase_Repository)
- MediaWiki, [Wikibase Client extension](https://www.mediawiki.org/wiki/Extension:Wikibase_Client)
- MediaWiki, [Wikibase FAQ](https://www.mediawiki.org/wiki/Wikibase/FAQ)

### Fit assessment for Common Knowledge

**What Wikibase could plausibly provide without rebuilding it:**
- collaborative editing of structured entities and statements;
- a mature model for qualifiers, references, ranks, and unknown/no-value distinctions;
- revision history, contributor attribution, diffs, and configurable permissions;
- APIs and RDF exports for interoperability.

**What it does not provide as a complete out-of-the-box solution:**
- a first-class evidence-passage model with precise quotation/page/line/data-cell anchors;
- explicit support/challenge/qualification relationships between evidence and a claim;
- independent assessments with method, reasoning, uncertainty, and reviewer role;
- a public-facing explanation of why a claim is assessed a particular way;
- an assurance that rank or reference presence corresponds to evidential quality.

**Current conclusion:** Wikibase remains a credible candidate for the structured record and collaborative editing layer, but it is not yet demonstrated to be the whole product. The main risk is that Common Knowledge would need to build a substantial evidence-assessment and user-experience layer around it, while also operating or paying for a fairly involved MediaWiki stack. We should not reject it without a small hands-on trial.

### Proposed hands-on test

Use one deliberately small, synthetic example with:
1. a scoped statement (including a time qualifier);
2. two sources with distinct bibliographic metadata;
3. one explicit unknown or no-value case;
4. two competing or qualifying pieces of evidence;
5. a revision that changes the assessment without erasing the earlier version.

Then inspect:
- the authoring experience for a non-specialist;
- the entity JSON and REST API responses;
- the RDF entity's direct truthy predicates versus its linked full statement nodes;
- how revisions and contributor identities appear;
- how much custom modeling is required to represent evidence relations and separate assessments.

Do not publish experimental material to Wikidata. Use a local or disposable test instance if proceeding.


## Nanopublications deep dive — publication, collaboration, identity, and correction

**Research date:** 26 November 2026  
**Method:** Official guidelines and handbook, ecosystem architecture/tool documentation, and public library repository metadata reviewed. No nanopublication has been published by this project, including on the test network.

### Formal structure and identifiers

A nanopublication is an RDF dataset divided into four named graphs:
1. **Assertion graph:** the content being asserted.
2. **Provenance graph:** how the assertion came about, referring to the assertion graph.
3. **Publication information graph:** metadata about the publication itself, such as creator and creation time.
4. **Head graph:** connects the nanopublication to the other three graphs.

The guidelines define well-formedness constraints and recommend TriG serialization. A Trusty URI includes a cryptographic hash derived from the nanopublication content, allowing a consumer with the content to verify that it matches the identifier. The current ecosystem signs nanopublications with a creator's key.

This gives a useful distinction between the provenance of the assertion and metadata about the act of publishing it. However, the four-graph structure does not prescribe what a good evidence assessment looks like; the assertion vocabulary and the relations to sources still need to be designed.

Sources:
- Nanopublications, [Guidelines](https://nanopub.net/docs/guidelines/)
- Nanopublications, [Handbook: Nanopublication](https://nanopub.net/docs/handbook/nanopublication/)

### Authoring and reusable templates

Nanodash is a browser interface for browsing, searching, and publishing nanopublications. Templates are themselves nanopublications that describe the expected structure and placeholders for an assertion, provenance, or publication-info graph. Nanodash turns them into forms and records which template was used.

Templates can be versioned, and a space can maintain a template so that any eligible member can publish its next version. This is a meaningful response to the human-authoring problem: contributors do not necessarily need to write RDF manually, and a community can share a structured form.

This could support a Common Knowledge workflow if we can express the record and evidence-assessment fields in templates. The open question is how much complexity is exposed to a contributor and whether the form system can express the richer review process we need without becoming cumbersome.

Sources:
- Nanopublications, [Tools](https://nanopub.net/docs/tools/)
- Nanopublications, [Nanopublication template](https://nanopub.net/docs/handbook/nanopublication-template/)

### Spaces: collaborative resources and roles

A Space is a collaborative unit represented on the network. It can maintain resources such as vocabularies, documentation, collections, templates, and views. Membership and role grants are themselves recorded as nanopublications. The documented role tiers are admin, maintainer, member, and observer; roles determine which actions and contributions count in a space.

The system's own handbook documentation is an example: its paragraphs are separate nanopublications, assembled into pages through queries, with member contributions and version history.

This is a substantial feature for Common Knowledge's eventual community contribution model. It offers an existing pattern for community-maintained definitions and documentation without requiring a single shared database record to be mutable in place.

There is also a governance caveat worth noting, without treating it as a reason to reject the technology: the handbook says the admins named in a space's founding definition cannot be removed, even by themselves. Later admins can be removed by another admin. This is a particular authority model embedded in the space mechanism; Common Knowledge should not assume it matches its own eventual community principles.

Sources:
- Nanopublications, [Space](https://nanopub.net/docs/handbook/space/)
- Nanopublications, [Space member role](https://nanopub.net/docs/handbook/space-member-role/)
- Nanopublications, [Documentation topic](https://nanopub.net/docs/handbook/documentation-topic/)

### Identity, signatures, and trust

A signature proves that a publication was signed by a particular private key. It does not, by itself, prove who controls that key. The network uses introductions and approvals to associate keys with identities; the documented person identity uses ORCID, while keys are separate credentials. A new key can publish while pending, but it does not count for member-restricted content or roles until an approval chain reaches it.

The trust model is explicitly about identity, not the correctness, usefulness, or appropriateness of content. Content curation is left to spaces and their members.

This is a strong conceptual separation for Common Knowledge: authentication and provenance can establish who submitted something and preserve what they said, while evidence evaluation remains a separate process. The network's approval of a key must never be presented as approval of its assertions.

A practical key-management issue remains. Nanodash-managed keys are kept with the account/instance; command-line keys are local files. The handbook warns that losing a command-line key makes its signed publications impossible to supersede or retract through the normal same-key mechanism. Backups and key recovery/rotation procedures therefore matter.

Sources:
- Nanopublications, [Trust and approval](https://nanopub.net/docs/handbook/trust-and-approval/)
- Nanopublications, [Person](https://nanopub.net/docs/handbook/person/)

### Immutability, versions, retractions, and disagreement

Published nanopublications cannot be edited or deleted. A correction is a new nanopublication that supersedes the old one; a withdrawal is a retraction nanopublication. Both preserve the original content and allow old citations to remain inspectable.

The same-key rule is important: a supersession or retraction only takes effect when signed by the key that signed the original. If that key is lost, the original cannot be superseded or retracted through this mechanism. Another person can derive a new publication from it, or override shared resources where a space's conventions allow the new version to take effect.

This supports durable citation and an auditable history, but it is not a complete answer to the problem of correcting someone else's false or harmful publication. Derivation preserves the original and creates a distinct work; override is governed by the community context in which a resource is displayed. A published record remains on the network, even after retraction, so sensitive personal data or material that must be removed should not be published there in the first place.

Forks are another edge case: if two versions independently supersede the same earlier version, the version chain branches and tools cannot automatically know which is current. The handbook recommends checking the current version before superseding and repairing a fork with a new version that supersedes both heads.

Sources:
- Nanopublications, [Versions and retractions](https://nanopub.net/docs/handbook/nanopublication-versions-and-retractions/)
- Nanopublications, [Handbook: Nanopublication](https://nanopub.net/docs/handbook/nanopublication/)

### Network and query architecture

The current ecosystem uses multiple registry services that replicate publications between peers. A publisher sends a nanopublication to one registry; peers are documented to pick it up within minutes. Nanopub Query provides query services over different subsets/aspects of the network, including SPARQL endpoints. Nanodash provides the human-facing interface and can also act as an API/intermediary. A monitor tracks service health; a vocabulary index supports autocomplete; nanopub-http exposes library functions over HTTP.

A separate test network exists. Its publications do not flow to the real network and are intended for experimentation. The handbook explicitly says publication to the real network is final.

This architecture is more resilient and interoperable than a single central database, but it creates dependencies on the availability, indexing, and query behaviour of external network services. Common Knowledge would need a preservation/retrieval strategy that does not assume one web interface or query endpoint will exist forever.

Sources:
- Nanopublications, [Technical Architecture](https://nanopub.net/docs/architecture/)
- Nanopublications, [Handbook: Nanopublication](https://nanopub.net/docs/handbook/nanopublication/)

### Libraries and licensing

The official tools page lists Java, Python, JavaScript/TypeScript, and Rust implementations capable of signing, verifying, and publishing nanopublications. Public repository metadata currently identifies nanopub-java as MIT-licensed and nanopub-py as Apache-2.0-licensed. The ecosystem is therefore accessible from a Python-oriented prototype, though dependencies and the exact current release/API should be checked before adoption.

Sources:
- Nanopublications, [Tools](https://nanopub.net/docs/tools/)
- GitHub, [nanopub-java](https://github.com/Nanopublication/nanopub-java)
- GitHub, [nanopub-py](https://github.com/Nanopublication/nanopub-py)

### Fit assessment for Common Knowledge

**What nanopublications could plausibly provide:**
- small independently citable assertion units;
- explicit separation of assertion provenance and publication metadata;
- content-derived identifiers and signed immutable publications;
- version and retraction relationships that preserve historical citations;
- reusable authoring templates;
- community-maintained resources, vocabularies, and documentation through Spaces;
- a decentralized publication and query ecosystem.

**What remains unproven or incomplete for our use:**
- whether the authoring UX is accessible to ordinary non-specialists at scale;
- whether the model can express precise evidence passages, dataset observations, and competing assessments in a clear way;
- how a reader navigates from an assertion to its evidence and from conflicting evidence to multiple assessments;
- how to handle key loss, harmful or legally sensitive content, and correction of another person's publication;
- whether the existing registry/query network meets long-term availability and preservation requirements for a public reference service;
- whether a space's authority model can be used without importing governance assumptions Common Knowledge has not chosen.

**Current conclusion:** Nanopublications are a strong candidate for the *publication/interchange layer* and possibly for community-maintained vocabularies or documentation. They are not yet proven to be the full authoring, review, and discovery product. They merit a hands-on test before Common Knowledge builds its own publication protocol.

### Proposed hands-on test

On the separate test network only:
1. Create a tiny synthetic assertion with an explicit source and provenance.
2. Generate and verify its Trusty URI and signature.
3. Publish it and retrieve it through both Nanodash and a client library.
4. Create a template that turns a small evidence-record structure into a contributor form.
5. Publish a second version and a retraction; inspect how the old and new records appear.
6. Create a derived publication signed by a different key to test how an independent challenge or alternative assessment can be represented.
7. Check whether the query API can retrieve the complete evidence/provenance graph in a form a simple Common Knowledge interface could render.

Do not publish project research, personal information, or any experimental record to the real network without an explicit separate decision.


## RDF, PROV-O, SHACL, JSON-LD, and Web Annotation — deeper standards review

**Research date:** 26 November 2026  
**Method:** W3C Recommendations and specifications reviewed. No application implementation or interoperability test has yet been run.

### RDF: useful data model, but named graphs need careful interpretation

RDF represents information as triples (subject, predicate, object), grouped into graphs. An RDF dataset contains one default graph and zero or more named graphs. This makes RDF suitable for expressing linked records and for exchanging graph data across systems.

An important subtlety: RDF 1.1 defines the syntax of datasets but does not provide one agreed formal semantics for what graph names mean or how named graphs should be interpreted as a whole. A graph name does not automatically prove who asserted the graph, that the graph is endorsed, or that all its triples should be treated as globally true. Systems need explicit conventions and metadata for those meanings.

This matters directly to Common Knowledge. We may want to preserve competing assessments or quote an external graph without endorsing it. Named graphs can help organize that material, but the application must explicitly represent attribution, endorsement, and assessment rather than relying on graph boundaries alone.

Sources:
- W3C, [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/)
- W3C, [RDF 1.1 Primer](https://www.w3.org/TR/rdf11-primer/)
- W3C, [On Semantics of RDF Datasets](https://www.w3.org/TR/rdf11-datasets/)

### PROV-O: describe how records were produced, not whether they are correct

PROV-O provides a general vocabulary for provenance. Its central classes are Entity, Activity, and Agent. It can express that an activity used a source, generated a record, was associated with an agent, or that one entity was derived from another. Qualified relations allow additional details to be attached to an influence, usage, derivation, attribution, or association.

For Common Knowledge, this maps naturally to workflows such as:
- a source document was used by an extraction activity;
- an evidence passage was generated or identified by an annotation activity;
- an assessment record was generated by a review activity;
- a human or software agent was associated with that activity;
- a later record was derived from an earlier record.

PROV-O does not prescribe the semantics of a scientific review, the criteria for weighing evidence, or the meaning of a conclusion. It can preserve the lineage of an assessment, but an application-specific vocabulary is still needed to describe what was assessed and how.

Source:
- W3C, [PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/)

### SHACL: validate record structure, not epistemic validity

SHACL validates an RDF data graph against a shapes graph and produces a validation report. It can enforce requirements such as:
- a record has exactly one primary statement;
- a statement has a scope or an explicit scope status;
- every evidence item links to a source;
- a source has a locator or a reason why one is unavailable;
- an assessment has an author/agent and a method;
- relationship types come from an allowed vocabulary.

SHACL conformance means the data meets the specified structural constraints. It does not mean the claim is true, the source is reliable, the quotation is interpreted correctly, or the assessment is scientifically sound. A well-formed false assertion can conform perfectly.

This is a good fit for automated quality gates and exchange validation, provided the UI never presents SHACL conformance as evidence of truth.

Source:
- W3C, [Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/)

### JSON-LD: practical bridge between web JSON and linked data

JSON-LD is a W3C Recommendation that serializes Linked Data in JSON. It is designed to integrate with existing web systems and JSON-based storage or APIs, while allowing terms and relationships to map to shared IRIs.

This could let Common Knowledge expose an approachable JSON API and still provide a standard linked-data representation. JSON-LD is a serialization, not a data model or assessment framework; it does not remove the need to define stable terms, identifiers, and semantics.

Source:
- W3C, [JSON-LD 1.1](https://www.w3.org/TR/json-ld11/)

### Web Annotation: a promising way to identify precise evidence passages

The W3C Web Annotation Data Model describes annotations on web resources and supports selectors that identify parts of a source. Particularly relevant are:
- **TextQuoteSelector:** records the exact selected text plus surrounding prefix and suffix, helping locate a passage even if repeated text occurs elsewhere.
- **TextPositionSelector:** records start and end character positions. It avoids copying the passage, but is brittle if the source changes.
- **Fragment, CSS, XPath, and other selectors:** can target supported regions of HTML, PDF, CSV, images, and other media types.

The specification notes that position selectors are fragile when source content changes and recommends using state information to identify the relevant representation. Quote selectors can be more robust but may require storing text from the source, which raises copyright and access considerations. The data model supports combining selectors to narrow a selection.

This is a strong candidate for evidence anchors. A Common Knowledge evidence record could identify a source version and use a quote selector (with prefix/suffix), optionally paired with a position or fragment selector. We would still need to store retrieval metadata and handle sources that move, disappear, are access-restricted, or are revised.

Source:
- W3C, [Web Annotation Data Model](https://www.w3.org/TR/annotation-model/)

### Standards synthesis for a small demonstrator

The standards appear complementary rather than competing:
- **RDF:** graph data model and linked identifiers.
- **JSON-LD:** web-friendly JSON serialization of linked data.
- **PROV-O:** lineage of records, activities, and agents.
- **SHACL:** machine-checkable structural constraints.
- **Web Annotation:** precise selectors for evidence within source resources.

A practical prototype should not implement all of these merely because they exist. The likely smallest useful experiment is a simple internal record model with a JSON representation, plus a test mapping of source/evidence anchors to Web Annotation and record history to PROV-O. SHACL can validate the sample records. Only if the mapping proves useful should we commit to RDF/JSON-LD as a primary storage or interchange format.

### Key caution

These standards improve interoperability and auditability, but they do not provide a shared epistemology. They cannot tell us whether two sources are independent, whether a study is methodologically sound, whether a quote supports a claim, or how uncertainty should be summarized. Those are product and domain-method questions that require explicit, inspectable design and expert/user feedback.


## OpenAlex deep dive — upstream data, curation, identity, and operational fit

**Research date:** 26 November 2026  
**Method:** Official OpenAlex data, API, snapshot, curation, and correction documentation reviewed. No API queries or snapshot downloads have been performed in this research pass.

### Data gathering and source provenance

OpenAlex continuously gathers records from Crossref, DataCite, ORCID, ROR, PubMed, PubMed Central, DOAJ, ISSN International Centre, repositories such as HAL/arXiv/Zenodo/OSTI/RePEc, thousands of institutional repositories, publisher feeds, and parsing of 70M+ open-access PDFs and landing pages. It records the external indexes a record can come from. Community corrections are also an input.

The catalog was seeded with the final open Microsoft Academic Graph dataset in 2021. This is a useful lineage fact: OpenAlex is a large aggregation and enrichment of other indexes, not an independent primary source for every bibliographic fact.

OpenAlex preserves raw author-name and affiliation strings in authorship data while also attaching resolved author and institution entities. That is valuable because the original text can be inspected alongside the system's interpretation. However, the documentation describes source/index lineage at the record level and does not establish a complete field-by-field provenance chain for every attribute.

Sources:
- OpenAlex, [How it's built](https://help.openalex.org/data/how-its-built/)
- OpenAlex, [Authorships](https://help.openalex.org/data/authorships/)

### Entity identity and matching are editorial decisions

OpenAlex distinguishes native entities, for which it mints IDs after making fuzzy matching decisions, from vocabulary entities that correspond to already well-defined concepts or identifiers. Native entity IDs can be wrong and are explicitly described as curatable. External identifiers such as DOI, ORCID, ISSN-L, and ROR should be retained alongside OpenAlex IDs when long-term identity matters.

Works are built from locations: a publisher page, preprint, repository copy, and PubMed record may all refer to one work. Persistent identifiers and declared links provide the strongest matching path; otherwise trained matchers compare candidates. The documentation says uncertain matches may be left separate rather than forcing a merge.

Author disambiguation has changed over time. Different groups of works were assigned by different models, older works were not all globally re-matched, and a roughly four-million-work ingestion gap in late 2025 left many author entries without a profile. The current documentation reports estimated precision and recall for the overall profile corpus, but the estimates are based on model judgments, not human judgments. Known failure modes include splits, false merges, and entries with no author profile.

This is a useful example of a system that exposes its matching method and known failure modes. It also reinforces why Common Knowledge should preserve raw source identifiers/strings and distinguish original data from inferred entity resolution.

Sources:
- OpenAlex, [Data reference](https://help.openalex.org/data/)
- OpenAlex, [Works overview](https://help.openalex.org/data/works/)
- OpenAlex, [Matching and merging works](https://help.openalex.org/data/works/matching/)
- OpenAlex, [Author disambiguation](https://help.openalex.org/data/authors/disambiguation/)
- OpenAlex, [Authors overview](https://help.openalex.org/data/authors/)

### Community correction mechanisms

OpenAlex has user-submitted curations that record what was changed, who submitted it, when, and the review/application state. Its documented public self-service curation workflow is currently centered on author-profile corrections: claiming works, removing misattributed works, and changing profile names. Site-wide curators can correct additional work fields, and some other corrections go through support tickets.

Corrections are applied through a nightly data refresh and may take one to two days to appear consistently across the API, search, and website. The correction mechanism is useful but narrow: it is not an open review process for evaluating whether a research finding is supported, and the curation audit trail is not fully exposed in the public read API.

Source:
- OpenAlex, [Curations](https://help.openalex.org/data/curations/)
- OpenAlex, [When corrections go live](https://help.openalex.org/how-to/when-corrections-go-live/)

### Citations and metrics are useful, but not ground truth

OpenAlex builds citation links by extracting reference lists from upstream metadata and, for open-access works, sometimes from PDFs. References with persistent IDs can be linked by ID; others are matched from text. OpenAlex's November 2026 documentation reports an estimated 82% coverage of references whose cited work is in OpenAlex and an estimated 96% correctness for citations it serves, based on its own sampled evaluation. It also explains why a work's linked references can be shorter than its printed bibliography.

These are useful signals for discovery and research mapping, but they are not a substitute for reading the cited source. A citation link does not show whether the citing paper supports, disputes, or merely mentions the cited work. Citation counts and field-normalized metrics also depend on the completeness and classification decisions of the underlying corpus.

Source:
- OpenAlex, [Citations and references](https://help.openalex.org/data/works/citations/)

### Identifiers, merges, and deletions

OpenAlex entities can be merged when two IDs are found to represent the same real-world object. API requests for merged IDs usually resolve to the surviving entity, but OpenAlex explicitly describes redirects as best-effort rather than a permanence guarantee. Deleted IDs return 404. Snapshot releases now include merge ledgers for works, authors, sources, and institutions, plus a deletion log for works; other entity types do not yet have equivalent deletion logs.

A Common Knowledge record should therefore store durable external identifiers (DOI, ORCID, ROR, etc.) where available, plus the OpenAlex ID and the retrieval date/version. It should not rely on an OpenAlex ID redirect as its only permanent reference.

Sources:
- OpenAlex, [Merged entities and deletions](https://help.openalex.org/access/sync/)
- OpenAlex, [Get single entities](https://help.openalex.org/api/get-single-entities/)

### Access, licensing, and reproducibility

OpenAlex states that its data is released under CC0. The public full snapshot is free to download without an AWS account, in JSON Lines or Parquet. The September 2026 release contained about 626 million records and was approximately 745 GB compressed in JSON Lines or 770 GB in Parquet. This is not a sensible default download for an early Common Knowledge prototype.

The public full snapshot is quarterly and replaces the current bucket contents in place. The documentation recommends archiving a dated snapshot/manifest if reproducibility against a point-in-time corpus matters. Daily snapshots and API sync filters are paid services. The API itself supports casual keyless access; a free API key increases the daily budget and is needed for cursor pagination beyond the first page. Rate and budget limits should be respected in any automated ingestion.

CC0 applies to OpenAlex's database, not automatically to the underlying papers or full-text files it indexes. Source works may retain publisher or author licenses and access restrictions. Common Knowledge must evaluate rights at the level of each source object and content item rather than infer that a record being present in OpenAlex makes its underlying text freely reusable.

Sources:
- OpenAlex, [Snapshot](https://help.openalex.org/access/snapshot/)
- OpenAlex, [Sync](https://help.openalex.org/access/sync/)
- OpenAlex, [Authentication and rate limits](https://help.openalex.org/api/authentication/)
- OpenAlex, [How it's built](https://help.openalex.org/data/how-its-built/)

### Fit assessment for Common Knowledge

**What OpenAlex could provide:**
- scholarly work discovery and bibliographic metadata;
- DOI, ORCID, ROR, ISSN-L and other identifier mappings;
- links among works, authors, institutions, sources, funders, and topics;
- citation-network discovery;
- a large, openly licensed research index;
- useful examples of raw-input preservation, matching disclosure, and correction workflows.

**What it does not provide:**
- source-specific evidence passages or claim-to-evidence relations;
- assessment of whether a study's result is valid or whether it supports a particular claim;
- multiple transparent interpretations of the same evidence;
- a full provenance chain for every metadata field;
- a general-purpose community review process for scientific conclusions.

**Current conclusion:** OpenAlex is an excellent candidate upstream integration, not a candidate foundation for the Common Knowledge knowledge record itself. Use it to locate and enrich scholarly source records, but retain the original DOI/ORCID/ROR and source metadata, make retrieval dates explicit, and link to the source itself. Do not treat citation counts, author matching, or topic classifications as epistemic verdicts.

### Proposed lightweight API evaluation

Before integrating it, make a small, bounded API sample:
1. Retrieve a handful of works by DOI and inspect the raw JSON fields, including locations, authorships, source IDs, references, and updated_date.
2. Compare an OpenAlex work record with its Crossref or DataCite source record to see which attributes are inherited, enriched, or inferred.
3. Inspect one author profile and its raw authorship strings to understand what identity-resolution information survives.
4. Query a known merged ID and record how the API reports the surviving ID.
5. Save the query, retrieval timestamp, API response, and relevant identifiers as a dated test fixture.

Do not download the full snapshot or build a continuous sync pipeline unless a real product workflow demonstrates that it is needed.


## Source-code and package metadata spot-check

**Research date:** 26 November 2026  
**Method:** Read selected current repository manifests and READMEs through GitHub: Wikibase extension composer/extension metadata, nanopub-py project metadata and README, and nanopub-js package metadata. This is a targeted spot-check, not a full code audit or security review.

### Wikibase

The current Wikibase extension manifest identifies the package as a MediaWiki extension and declares GPL-2.0-or-later. Its repository extension metadata currently requires MediaWiki 1.48.0 or later. The Composer manifest shows a substantial PHP dependency set, and the extension manifest exposes many Action API modules for entity retrieval and editing.

This confirms that Wikibase is not a standalone library or database that can simply be embedded in a small Python application. It is an extension integrated into a specific MediaWiki version and runtime, with its own dependency and upgrade compatibility requirements.

Files inspected:
- https://github.com/wikimedia/mediawiki-extensions-Wikibase/blob/master/composer.json
- https://github.com/wikimedia/mediawiki-extensions-Wikibase/blob/master/extension-repo.json

### Nanopublication Python and JavaScript libraries

The current nanopub-py project metadata inspected identifies version 2.2.2, Python 3.12 or later, Apache-2.0, and dependencies including RDFLib, requests, Typer, PySHACL, and SPARQLWrapper. Its README documents a high-level API for constructing, publishing, searching, fetching, and inspecting nanopublications. It also demonstrates an explicit test-server configuration flag in its quick-start example. The project includes test markers for network-dependent tests and a test-suite connector dependency.

The current nanopub-js package metadata inspected identifies version 0.7.0, MIT, browser and Node entry points, and package scripts for building and running tests. This supports the claim that the ecosystem can be integrated into either a Python-oriented or JavaScript-oriented prototype, though version compatibility and runtime behaviour still need hands-on testing.

Files inspected:
- https://github.com/Nanopublication/nanopub-py/blob/main/pyproject.toml
- https://github.com/Nanopublication/nanopub-py/blob/main/README.md
- https://github.com/Nanopublication/nanopub-js/blob/main/package.json

### Limits of this inspection

No source files beyond these manifests/READMEs were audited, no package was installed, and no automated tests were run. The package metadata is a snapshot of the repositories at the time of inspection; it should be rechecked before selecting versions or depending on specific APIs.

## Same-example comparison across the candidate approaches

To avoid comparing each technology against a different imagined use case, use one synthetic example:

> **Synthetic observation:** A fictional monitoring station R-1 recorded dissolved oxygen of 4.2 mg/L at 09:00 UTC on 1 May 2026. The cited CSV row is the observation source. A separate calibration log says the sensor was overdue for calibration. The observation may be authentic as a recorded measurement while its accuracy remains uncertain.

This example deliberately separates (a) what a source recorded from (b) whether that record is a reliable measurement and (c) what conclusion, if any, follows from it.

| Need in the example | Wikibase | Nanopublications | RDF / PROV-O / SHACL / Web Annotation | OpenAlex |
|---|---|---|---|---|
| Represent station, property, value, unit, time | Native structured entity and statement model; qualifiers can carry context | RDF assertion graph can express it; vocabulary must be chosen | Directly representable in RDF with an application vocabulary | Not its purpose; may index a cited dataset as a scholarly work |
| Identify source and exact CSV row | Reference records can store source metadata, but a robust row/cell anchor needs a convention or extension | Provenance graph can link the source; exact row selector must be modeled | Web Annotation provides selectors; CSV row/cell semantics may still need an application-specific convention | Can help discover dataset metadata/DOI, not identify the exact row as evidence |
| Preserve calibration concern | Could model as another entity/statement and link it to the observation | Could publish a separate assertion and link/derive from the first | Separate evidence and assessment nodes/graphs with explicit relations | Not a review or measurement-validity model |
| Record who extracted/reviewed it and how | Revision history records edits; a distinct review activity/method needs extra modeling | Provenance and publication metadata, signed by a key; detailed review method needs a vocabulary | PROV-O can model activities, entities, agents, and derivations | Records some contributor/curation activity, not the review of the observation |
| Preserve uncertainty and competing assessments | Possible with custom entities/properties; no complete assessment workflow by default | Possible as separate nanopublications; query/view conventions determine presentation | Flexible, but all assessment semantics must be designed | Not a core capability |
| Correct the record while preserving history | MediaWiki revisions and diffs | Immutable publication plus supersession/retraction/derivation | Depends on the application and storage/version model | Curations update index records; not a general claim revision model |
| Validate required fields | Some constraints/extensions exist; exact behaviour needs a trial | Can use SHACL tooling in the ecosystem; template validation also applies | SHACL directly validates graph shape | API schema and record pipeline, not a user-defined knowledge-record validator |
| Ordinary contributor experience | Mature wiki editing patterns, but entity modeling is specialized | Nanodash templates turn RDF into forms; usability still needs user testing | Not a user interface by itself | Strong discovery/API experience for scholarly records |

### What this comparison teaches us

1. The source object, evidence anchor, observation/assertion, and assessment should be distinct concepts. One source can contain many evidence locations; one evidence location can be relevant to multiple assertions; and one assertion can receive multiple assessments.
2. A source citation is not the same thing as evidence. A durable record needs to identify what part of the source is being relied on and what it is said to show.
3. The observation itself may be well-established even when its interpretation or measurement reliability is uncertain. The system should preserve those separate judgments rather than flatten them into one truth score.
4. No candidate supplies the complete workflow. Wikibase and nanopublications are the most relevant candidates for the contribution/publishing layer; RDF standards provide interoperability components; OpenAlex is an upstream scholarly index.
5. We should test a complete contributor-to-reader workflow before selecting a storage architecture. A standards-compliant data model that ordinary people cannot author or inspect is not a successful product.

## Current comparative position (not a technology decision)

The research so far supports the following provisional roles:
- **Wikibase:** strongest existing candidate for a collaborative structured-data repository with familiar revision history and permissions.
- **Nanopublications:** strongest existing candidate for immutable, independently citable publication and community-maintained semantic resources.
- **RDF + PROV-O + SHACL + Web Annotation:** strongest standards toolkit for interoperable records, provenance, structural checks, and precise evidence anchors; requires a product implementation.
- **OpenAlex:** upstream scholarly discovery and metadata enrichment only.

These roles can be combined. For example, a product could use a contributor-friendly relational/JSON model internally, publish selected assertions as nanopublications, map provenance to PROV-O, expose JSON-LD/RDF exports, validate exports with SHACL, use Web Annotation for source anchors, and query OpenAlex for scholarly metadata. That is an architectural possibility, not a recommendation to implement all these pieces now.

**Next decision should be driven by a hands-on prototype and a real user workflow**, not by the theoretical completeness of any standard or platform.


## Hands-on record-model spike — first result

**Research date:** 26 November 2026  
**Code review:** [PR #3 — experimental evidence-linked record model spike](https://github.com/deviant46n2/common_knowledge/pull/3)

A disposable JSON-LD fixture was created around a fictional water-quality monitoring record. It deliberately separates:
- the statement that station R-1 recorded 4.2 mg/L at a specified time;
- the exact CSV row containing that recorded value;
- a separate calibration-log passage stating calibration was overdue;
- the distinct relationships of the CSV row (supports what was recorded) and calibration entry (qualifies confidence in measurement accuracy);
- an assessment with method and limitations;
- a PROV-O review activity associated with a reviewer agent and using both evidence items.

The evidence passages are represented as Web Annotation TextQuoteSelector targets with exact text, prefix, and suffix. Local fixture files are included so the selector can be checked against the source text rather than merely checking that the JSON parses.

**Observed test result:** Eight pytest checks passed using RDFLib after extending the fixture with a second independent assessment, a second record version, and a static HTML reader. The tests cover JSON-LD parsing, preservation of separate evidence-relation types, annotation/source/selector links, PROV-O activity and agent links, exact quote/prefix/suffix matching against the fixture sources, coexistence of two assessments, version lineage, and reader output.

**Useful failure found:** The first iteration used a compact JSON-LD key for hasTarget without mapping it to oa:hasTarget. The JSON document parsed, but the expected annotation target was absent from the RDF graph. The failing test exposed this silent semantic loss. The context was corrected and the five tests then passed. This is direct evidence that valid JSON is not enough; the export needs semantic tests.

**What this does not establish:** It does not establish truth, source authenticity, the quality of the assessment, SHACL conformance, a user-friendly authoring workflow, version/correction semantics, or whether JSON-LD should be canonical. It is not a selected schema or architecture. All IDs use the reserved example.org domain and all data/agents are synthetic.

**Additional result:** The second review is represented as a separate assessment with its own PROV-O activity and agent. A new record version links to the prior version with prov:wasRevisionOf and references both assessments; the earlier version still references only the initial assessment. Tests confirm that the two assessments coexist and have distinct reviewer agents. A basic static HTML reader now presents the evidence relationships, both assessments, method/reviewer details, and version history. This is a small inspectability demonstration, not a complete authoring or review workflow. See [PR #3](https://github.com/deviant46n2/common_knowledge/pull/3).

**Next experiment:** Compare the same contribution workflow with a nanopublication on its isolated test network (never the real network) and with a small Wikibase test instance if setup cost is reasonable. Next, test the authoring path and compare this representation with a nanopublication on its isolated test network (never the real network) and with a small Wikibase test instance if setup cost is reasonable. The current reader is developer-generated HTML, not evidence of non-specialist usability.


## Live nanopublication test-network inspection

**Research date:** 26 November 2026  
**Method:** Read-only live inspection of Nanodash, both generations of nanopublication test services, the current nanopub-py source/configuration, and the Nanodash Docker configuration. A read-only SPARQL ASK query was executed in the test query editor. No profile was created and no nanopublication was signed or published.

### The current second-generation test services are live

The current test registry is:
- Registry: https://test.registry.knowledgepixels.com/
- Query service: https://test.query.knowledgepixels.com/
- Full-repository SPARQL endpoint: https://test.query.knowledgepixels.com/repo/full
- SPARQL editor: https://test.query.knowledgepixels.com/tools/full/sparql-editor.html

At inspection time, the registry homepage reported **11,841 nanopublications**, ready status, coverage of all types, and trust calculation disabled. The separate test query service exposed its repository pages and SPARQL editor. A read-only query, ASK { ?s ?p ?o }, ran successfully and returned boolean true. The table view showed a client-side JavaScript error after execution, but the response view contained the successful result.

This is stronger evidence than relying on a stale setup guide: the isolated second-generation registry and SPARQL query service are reachable and contain data.

Sources:
- Nanopub Registry test instance: https://test.registry.knowledgepixels.com/
- Nanopub Query test instance: https://test.query.knowledgepixels.com/
- Nanopub Query full repository page: https://test.query.knowledgepixels.com/page/full
- Nanopub Query editor: https://test.query.knowledgepixels.com/tools/full/sparql-editor.html

### Two different test-server generations appear in the ecosystem

The older host https://np.test.knowledgepixels.com/ is still documented by nanopub-py, but it identifies itself as a legacy Nanopub Server and, at inspection time, contained 19 nanopublications. The newer second-generation registry at https://test.registry.knowledgepixels.com/ is the more relevant target for current development and had 11,841 publications.

Do not confuse these endpoints or copy a test URL from an older guide without checking which generation a tool uses.

Sources:
- nanopub-py, [test server guide](https://github.com/Nanopublication/nanopub-py/blob/main/docs/getting-started/test-server.md)
- Nanopub Registry, [current test instance](https://test.registry.knowledgepixels.com/)

### A Python client configuration mismatch to account for

The current nanopub-py source (version 2.2.2, Python >=3.12) sets:
- TEST_NANOPUB_REGISTRY_URL to https://test.registry.knowledgepixels.com/np/;
- TEST_NANOPUB_QUERY_URL to https://query.knowledgepixels.com/api/, with a source comment saying a test query server is not yet available.

The live test query service now exists and exposes a SPARQL repository endpoint, but it is not the same thing as the query-template API path used by nanopub-py's NanopubClient. Thus, the current Python client can direct publication and fetching to the new test registry, but its built-in text/pattern search path is not fully isolated: it points at the production query-template API. Direct SPARQL against the test query endpoint is available and was smoke-tested separately.

This is not necessarily a bug in the client's supported API: the test query service may not expose the same query-template API as production. It is nevertheless a concrete integration limitation for our test plan. We should use direct test SPARQL or fetch by known test-registry URI when inspecting experimental publications, and never assume NanopubClient(use_test_server=True) makes every operation isolated.

Sources:
- nanopub-py, [definitions.py](https://github.com/Nanopublication/nanopub-py/blob/main/nanopub/definitions.py)
- nanopub-py, [client.py](https://github.com/Nanopublication/nanopub-py/blob/main/nanopub/client.py)
- Nanopub Query, [test full repository](https://test.query.knowledgepixels.com/page/full)

### Nanodash: use a local instance to target the test services

The public Nanodash site is connected to the production network and offers ORCID login; its homepage says users log in with ORCID to publish. We should not use that production-facing UI for experiments.

The current Nanodash Docker configuration exposes NANODASH_MAIN_REGISTRY and NANODASH_MAIN_QUERY, allowing a local instance to be pointed at the test registry and test query service. It also has an NANODASH_ORCID_LOGIN_MODE setting. The source indicates ORCID login mode defaults to false; in that mode a local profile can be used rather than an ORCID OAuth flow. The Nanodash app itself is AGPL-3.0 licensed.

This suggests a safer hands-on path:
1. Run a local Nanodash instance.
2. Configure its main registry and query URLs to the test endpoints above.
3. Keep ORCID login mode off for the isolated local experiment.
4. Create a local-only synthetic agent profile/key, if the profile flow permits it, and explicitly decline profile publication until the publication test is approved.
5. Use the local UI to inspect templates, authoring, preview, signing, and publishing controls before any publication.

The Nanodash installation requires Docker. Docker is not installed in the current research container, so this local UI test has not yet been run. The current container also has no outbound package-index access, so nanopub-py 2.2.2 could not be installed for a live Python-client test. These are environment limitations, not evidence that the software itself cannot run.

Sources:
- Knowledge Pixels, [Nanodash repository and license](https://github.com/knowledgepixels/nanodash)
- Nanodash, [Docker Compose configuration](https://github.com/knowledgepixels/nanodash/blob/master/docker-compose.override.yml.template)
- Nanodash, [Docker installation](https://github.com/knowledgepixels/nanodash/blob/master/INSTALL-with-Docker.md)
- Nanodash, [NanodashPreferences source](https://github.com/knowledgepixels/nanodash/blob/master/src/main/java/com/knowledgepixels/nanodash/NanodashPreferences.java)

### Updated test plan

Before publishing anything, first prepare a local draft nanopublication for the synthetic R-1 example and validate its four graphs and signature locally. Then use a local Nanodash instance configured to the isolated test registry/query services. Publishing even to the test network is a separate explicit action because nanopublications are immutable and the test network is public, even though it is isolated from production.

For the test-network round trip, verify:
- the publication appears at the direct registry URL returned by the registry;
- its Trusty URI validates against the content;
- all four graphs can be fetched and parsed;
- the test SPARQL endpoint can retrieve the assertion and provenance;
- the second assessment can be published as a distinct contribution;
- a supersession/retraction behaves as documented, with the original signer key retained securely.

Do not rely on the test query-template API until its availability is independently confirmed.


### Unsigned nanopublication mapping experiment

A local TriG draft was built for the same synthetic R-1 example. It contains three separate nanopublications:
1. an observation publication with the statement, scope, two Web Annotation evidence anchors, and distinct support/qualification relationships;
2. a first assessment publication derived from the observation publication;
3. a second independent assessment publication, also derived from the observation publication.

Each draft has four distinct named graphs (head, assertion, provenance, publication information). The provenance graph refers to its assertion graph; the publication-information graph refers to the nanopublication. The assessment publications are separate contributions rather than updates to the observation publication. Each review activity explicitly records its associated reviewer and the two evidence items it used.

**Observed test result:** Eight local RDFLib tests passed for the nanopublication drafts. Together with the eight record-model/reader tests, the experiment now has 16 passing local checks. Tests cover the minimum four-graph structure from the official guidelines, graph/identifier separation, required graph references, creator/creation metadata, distinct assessment publications, derivation from the observation, explicit PROV-O review activities and reviewer agents, separate evidence relationships, and evidence quote matching against the fixture files.

**Architectural insight:** Nanopublications encourage an append-only contribution model: the observation can remain immutable while multiple assessment publications are added. That fits independent review and durable citation. However, the application must assemble a useful current view from multiple publications and decide how to display competing or superseding assessments. The JSON-LD spike instead represented a later record version that references both assessments. Neither experiment has yet tested how an ordinary reader understands these models in a real interface.

**Limits:** The drafts use example.org placeholder identifiers and are unsigned. They have not been validated by the official nanopub-py or nanopub-java implementation, signed, or published to the test registry. No key/profile was created. These tests establish only a basic structural mapping, not full compliance, content validity, or publication-network behaviour.

Code and tests are in [PR #3](https://github.com/deviant46n2/common_knowledge/pull/3), under experiments/record-model-spike/nanopub/.


### Nanodash public-interface inspection

A read-only browser inspection of https://nanodash.knowledgepixels.com/ found that an unauthenticated visitor can browse:
- recent nanopublications and their detail pages;
- public user and software-agent profiles;
- Spaces and their resources;
- saved queries and search;
- public publishing templates, including popular and all-template lists;
- community resources and events.

The homepage explicitly tells visitors to log in with ORCID to see their own nanopublications and publish new ones. The publishing/template area is visible, but the actual contribution workflow is gated behind authentication. We did not sign in or create a profile, so the actual authoring form and preview experience remain untested.

This is a positive sign for public inspectability and discoverability: the network's content, contributor identities, spaces, and templates are browsable without an account. It also reveals a barrier for contributors who do not already have ORCID, at least on the public hosted instance. The local Nanodash configuration has a non-ORCID-login mode, but its local profile/key workflow still needs to be tested before we know how usable that path is.

Source:
- Nanodash public instance: https://nanodash.knowledgepixels.com/
- Nanodash repository and local deployment configuration: https://github.com/knowledgepixels/nanodash


### Nanodash nanopublication detail-page inspection

A read-only inspection of one public ontology-definition nanopublication showed how the current reader renders an individual publication:
- the assertion appears as structured triples with human-readable predicate labels and clickable terms;
- provenance appears in a separate section, including derived-from links;
- publication metadata shows creation date, license, creator, template links, and a latest-version indicator;
- signature metadata is inspectable, including target, algorithm, public key, signature, and signer;
- readers can expand raw-format downloads for the full nanopublication or assertion in multiple RDF serializations;
- the action menu includes commenting, approval/disapproval, and creating derived or overriding nanopublications.

This is a strong baseline for inspectability and raw-data access. It also shows the gap Common Knowledge may need to fill: the page presents the semantic graph faithfully, but it does not automatically turn arbitrary assertions and evidence into a domain-specific explanation of what a source passage supports, what it qualifies, and how independent assessments differ. Our small reader prototype is deliberately more opinionated about those relationships. The inspected item was an ontology-definition publication, not a scientific evidence assessment, so this is a UI observation rather than a comprehensive usability evaluation.

Example inspected:
- https://nanodash.knowledgepixels.com/RA3VxrEoZyRPd8ZwOvIpPGlRf2kVmNW1-nlVU55s7t8AI


## Live Wikibase sandbox inspection

**Research date:** 26 November 2026  
**Method:** Read-only inspection of the public test.wikidata.org API and a sandbox entity's JSON and RDF exports. No edits or account actions were performed.

The test Wikidata API is reachable and reports a current MediaWiki 1.48.0 test instance. Searching its API for “sandbox” returned a dedicated Wikidata Sandbox item, Q213542. Its JSON entity response provides a concrete example of the data model in use:
- one property has six version statements;
- five earlier/alternate version values have normal rank and one version has preferred rank;
- each version statement carries a publication-date qualifier;
- each statement carries a reference record with URL, title, and retrieval date;
- a second statement for the preferred version exists at normal rank, demonstrating that rank is per statement and not a guarantee that duplicate-looking statements disappear.

The default RDF export for Q213542 includes both the direct truthy shortcut predicates and full statement nodes. For the version property, the direct wdt: predicate exposes only the preferred value 1.0.5. The p: statement links retain all six individual statement nodes; those nodes preserve their rank, pq: date qualifier, and prov:wasDerivedFrom reference links. The flavor=dump export also contains the full statement nodes. An attempted flavor=truthy request returned HTTP 400; the RDF mapping documentation describes truthy and full statements as two representations in the RDF graph, not as two interchangeable URL flavor parameters.

This live example confirms two practical points:
1. Wikibase's JSON data model and full statement representation can preserve multiple sourced, qualified statements for one property.
2. Consumers that use only the direct truthy predicates lose the contextual statement-level detail. A Common Knowledge adapter must retain the full statement nodes and references.

This is a particularly useful real-world check because it verifies the data model with an actual API response, rather than only reading the documentation. The test item is intentionally messy and synthetic; it is not evidence of Wikibase's usability for a scientific review workflow.

Sources:
- Test Wikidata API search: https://test.wikidata.org/w/api.php?action=wbsearchentities&search=sandbox&language=en&format=json
- Test Wikidata sandbox entity JSON: https://test.wikidata.org/wiki/Special:EntityData/Q213542.json
- Test Wikidata sandbox entity RDF: https://test.wikidata.org/wiki/Special:EntityData/Q213542.ttl
- W3C-compatible Wikibase RDF mapping documentation: https://www.mediawiki.org/wiki/Wikibase/Indexing/RDF_Dump_Format


### Wikibase reader-interface inspection

A read-only browser inspection of the same test item showed how the standard Wikibase interface presents the underlying structure:
- statements are grouped by property, with each value displayed as a separate row;
- preferred/normal/deprecated ranks are indicated mainly by visual icons;
- qualifiers appear nested under the particular value they qualify;
- references appear as collapsed, expandable citation blocks, with URL/title/retrieval metadata visible after expansion;
- property IDs and labels are both shown, and linked item values are clickable;
- constraint warnings can appear beside statements.

This is a mature, usable structured-data interface and demonstrates that qualifiers and references can be exposed to readers without custom UI. It also has limitations for our use case:
- reference details are collapsed by default, so readers must expand them;
- rank is a curation signal, not an explanation of evidential strength or truth;
- references are attached to a statement but do not inherently identify the exact passage in a source or explain what that passage supports;
- the interface presents properties and values, not a full narrative of independent assessments and competing interpretations.

The public test instance is useful for inspection, but it is not a dedicated scientific evidence-review product. No edits were made.

Source:
- Test Wikidata sandbox item: https://test.wikidata.org/wiki/Q213542


### Current Wikibase REST API smoke test

The same test entity was fetched through the newer Wikibase REST API at:
https://test.wikidata.org/w/rest.php/wikibase/v1/entities/items/Q213542

The REST response groups statements by property and gives each statement a consistent object with:
- a statement ID and rank;
- a property ID and data type;
- a typed value;
- a list of qualifiers, each with its property and typed value;
- a list of references, each with a hash and its structured parts.

The version property response preserved all six values, including the preferred and normal-ranked 1.0.5 statements, each publication-date qualifier, and the reference parts (URL, title, retrieval date). This is much easier to consume than the nested Action API shape while retaining the details needed for a faithful adapter.

The separate /statements endpoint returned the same grouped statement structure. This confirms the REST API is reachable on the current test instance and is a promising interface for a Wikibase integration. This was a read-only GET test; no authentication, writes, or API editing were attempted.

Sources:
- Wikibase REST API entity: https://test.wikidata.org/w/rest.php/wikibase/v1/entities/items/Q213542
- Wikibase REST API statements: https://test.wikidata.org/w/rest.php/wikibase/v1/entities/items/Q213542/statements
- Official REST API documentation: https://www.wikidata.org/wiki/Wikidata:REST_API


## OpenAlex live API smoke test and source comparison

**Research date:** 26 November 2026  
**Method:** Read-only OpenAlex Work API query for DOI 10.48550/arXiv.1706.03762, comparison with DataCite DOI metadata, and resolver checks for selected alternate locations. No API key, snapshot download, or account was used.

### One record shows why raw metadata and resolved identity must coexist

OpenAlex returned Work W2626778328, “Attention Is All You Need” (2017), with an updated_date of 2026-11-26T09:34:50.682384. The response includes:
- resolved author IDs and display names, alongside raw_author_name strings;
- resolved institution IDs and names, alongside raw_affiliation_strings and per-affiliation raw strings;
- DOI, arXiv, and MAG identifiers;
- several locations, including a NeurIPS proceedings location marked publishedVersion and an arXiv repository location marked submittedVersion;
- a list of referenced-work IDs.

The raw and resolved fields are not identical in every case. For example, one raw author string is “Aidan N.Gomez” while the resolved display name contains a space after the initial. Raw affiliation strings include “Google Brain” and publisher-style affiliation text, while the resolved institution is a Google entity. This is useful enrichment, but the resolved entity is an OpenAlex matching decision, not a replacement for the original source string.

### DOI registration source matters

A direct Crossref API request for 10.48550/arXiv.1706.03762 returned 404. The DataCite API returned a full DOI record:
- publisher: arXiv;
- title and creator list;
- resource type: preprint;
- version 7;
- an arXiv non-exclusive distribution license;
- submitted and updated dates for successive versions.

This is an expected example of why a DOI lookup must not assume Crossref is the only registration agency. Common Knowledge should record the registration source and preserve the DOI itself, not interpret a Crossref 404 as a nonexistent DOI.

### Additional locations need independent verification

The OpenAlex response includes multiple locations for the work, among them the conference and arXiv locations, a historical MAG location, and several additional DOI-based locations with no source metadata attached in the response. Two sampled additional DOIs under prefix 10.65215 returned 404 from both the DOI resolver and DataCite API at inspection time.

This does not prove why OpenAlex associated those locations with the work; they may be stale, misidentified, or registered through another route not checked here. It does demonstrate that the existence of a location entry in an aggregated scholarly index is not sufficient proof that the referenced location is currently resolvable or correctly matched. A source-integrity workflow should preserve the raw location and identifier, test resolution, and flag the match for review rather than silently discarding or endorsing it.

### Practical integration implications

1. Query OpenAlex by DOI and retain the raw API response with retrieval timestamp and OpenAlex updated_date.
2. Store DOI, arXiv ID, ORCID, and ROR identifiers independently of OpenAlex IDs.
3. Preserve raw author and affiliation strings beside resolved identities.
4. Treat each location as a distinct manifestation/version with its own URL, version, access status, license, and source metadata.
5. Verify resolver status and registration-agency metadata for important identifiers.
6. Treat referenced_works as discovery links, not as evidence that the citing work supports or disputes the cited work.

Sources:
- OpenAlex Work API record: https://api.openalex.org/works/https://doi.org/10.48550/arXiv.1706.03762?select=id,doi,title,publication_year,authorships,locations,referenced_works,updated_date,ids,type
- Crossref DOI lookup (404 at inspection time): https://api.crossref.org/works/10.48550/arXiv.1706.03762
- DataCite DOI record: https://api.datacite.org/dois/10.48550/arXiv.1706.03762
- Sample unresolved location: https://doi.org/10.65215/r5bs2d54


## Hands-on follow-up — live API sample and testability corrections

**Research date:** 26 November 2026  
**Method:** One live OpenAlex API request and one Crossref DOI metadata request were fetched and compared. Current Wikibase Suite and nanopublication test documentation were rechecked. This is a bounded API observation, not a full data-quality audit.

### Live OpenAlex sample: one DOI

A single work was retrieved by DOI:

- DOI: `10.1038/s41586-020-2649-2`
- Title returned: *Array programming with NumPy*
- OpenAlex work ID: `W3035965352`
- Publication year: 2020
- API request: `GET /works?filter=doi:...&select=id,doi,title,publication_year,authorships,locations,referenced_works,updated_date&per_page=1`
- API result: one matching work; reported request cost was $0.0001.
- OpenAlex `updated_date` in the returned record: `2026-11-26T09:34:50.682384` (UTC).

The record contained 18 authorship entries. In this sample:
- Several authors had ORCID values but a null OpenAlex author ID.
- Some authors had neither a resolved OpenAlex author ID nor an ORCID.
- Raw author-name strings were retained.
- Raw affiliation strings were retained alongside normalized institution links.
- One author had multiple raw affiliation strings and multiple resolved institution links.
- The work exposed multiple locations/repository records, with varying OA and license metadata.
- The work included a list of linked referenced works.

A Crossref record for the same DOI supplied publisher-deposited metadata, including the title, publication date, journal/issue information, author strings, links to publisher full text, and a reference list. It was not a one-to-one duplicate of OpenAlex: OpenAlex had enriched authorship/institution mappings and a location list, while Crossref supplied the deposited bibliographic/reference metadata. The two should be treated as distinct source records with distinct update histories, not merged into one unquestioned canonical object.

**Observed implication:** OpenAlex does preserve useful raw strings, but it can also leave author identities unresolved even where ORCID data is present. Common Knowledge should retain source-level metadata and identifiers separately from any resolved person or institution entity. It should also store which index supplied each imported attribute when that is available, rather than silently treating the enriched value as the original source assertion.

**Limitations:** One selected DOI cannot establish corpus-wide precision, completeness, bias, or coverage. We did not verify the paper's content, inspect the publisher PDF, validate every reference, or assess the correctness of any author/institution match.

Sources:
- OpenAlex API record: https://api.openalex.org/works/W3035965352
- Crossref API record: https://api.crossref.org/works/10.1038/s41586-020-2649-2
- OpenAlex, [API reference](https://help.openalex.org/api/)
- Crossref, [REST API](https://api.crossref.org/)

### Nanopublication test network and conformance tests

The test network is not merely a suggested configuration flag. The current handbook describes a separate registry/query environment; test publications do not reach the real network. The Python client supports `use_test_server=True`, and the JavaScript library documents a test registry URL. The test network's Trusty/purl identifier does not automatically resolve through the production purl redirect; the test server's own returned URL should be used to fetch the test publication.

The ecosystem also publishes a canonical nanopublication test suite with valid and invalid examples, including plain, signed, and Trusty-URI cases, plus transform fixtures for signing. A JavaScript connector can download the official suite and access these cases; Python and Java equivalents are listed by the project. This creates a practical offline conformance test path before attempting network publication.

The next nanopublication experiment should therefore be staged:
1. Validate candidate RDF against the canonical test suite locally.
2. Construct and sign a synthetic nanopublication locally with a throwaway test key.
3. Publish only to `https://test.registry.knowledgepixels.com/`.
4. Retrieve it from `https://test.query.knowledgepixels.com/` or the test registry's direct URL.
5. Verify signature, Trusty URI, graph contents, and test-network isolation.
6. Do not reuse the test key or publish the synthetic record to production.

Sources:
- Nanopublications, [Test network and nanopublication handbook](https://nanopub.net/docs/handbook/nanopublication/)
- Nanopub Python, [Getting started](https://nanopublication.github.io/nanopub-py/)
- Nanopub JavaScript, [Repository and test-registry example](https://github.com/Nanopublication/nanopub-js)
- Nanopublication, [Canonical test suite connector](https://github.com/Nanopublication/nanopub-testsuite-connector-js)
- Nanopublications, [Query endpoints and repositories](https://nanopub.net/docs/handbook/query-endpoints-and-repositories/)

### Wikibase deployment clarification

The generic Wikibase Quick start page describes Docker images that can be run locally for a test drive. However, the current maintained Wikibase Suite repository describes its supported Docker Compose deployment as intended for a publicly accessible server, with a domain and TLS setup. It bundles Wikibase/MediaWiki, a job runner, MariaDB, OpenSearch, a SPARQL query service and updater, a query frontend, QuickStatements, and Traefik.

These are not necessarily contradictory: a basic/dev Docker environment and the supported production-oriented Wikibase Suite are different deployment targets. The earlier note should not be read as proof that the supported full suite is a lightweight local-only setup. For a Common Knowledge evaluation, we should either use an existing hosted instance, use the basic/dev route after checking its current maintenance status, or defer deployment until a concrete test justifies it.

Sources:
- MediaWiki, [Wikibase Quick start](https://www.mediawiki.org/wiki/Wikibase/Quick_start)
- Wikimedia Deutschland, [Wikibase Suite repository](https://github.com/wmde/wikibase-suite)
- MediaWiki, [Wikibase Docker](https://www.mediawiki.org/wiki/Wikibase/Docker/en)

## Updated experiment status

| Experiment | Status | What it establishes | What it does not establish |
|---|---|---|---|
| OpenAlex single-DOI API retrieval | **Performed** | A live API query returns bibliographic data, raw authorship strings, unresolved identities, institution links, locations, and references | General accuracy or whether OpenAlex is a suitable core |
| Crossref comparison for same DOI | **Performed** | Upstream bibliographic metadata differs in scope and structure from OpenAlex enrichment | That either source is fully correct or complete |
| Wikibase data-model and deployment review | **Documentation review only** | Main statement model, export caveat, revision model, and deployment distinction | Real authoring UX, API behavior in our instance, or resource requirements |
| Nanopublication test-suite review | **Documentation/repository review only** | An official conformance fixture suite and isolated test network exist | Our implementation passes the suite or can publish/retrieve correctly |
| Nanopublication publish/verify round trip | **Not yet performed** | — | Signature, Trusty URI, registry, and query behavior in practice |
| End-to-end human contributor workflow | **Not yet performed** | — | Whether a non-specialist can create, challenge, and inspect a record |

The next work should be a small reproducible prototype/test, not more broad candidate surveying. Keep the synthetic example, fixtures, commands, exact software versions, and results together so that someone else can repeat the experiment.


## Practical probe — synthetic observation as linked nanopublications

A small local data-model probe now exists in [research/experiments/2026-11-synthetic-observation.md](experiments/2026-11-synthetic-observation.md), with the corresponding [TriG fixture](experiments/2026-11-synthetic-observation-nanopubs.trig).

The fictional example separates:
- a nanopublication asserting what a CSV row records (4.2 mg/L dissolved oxygen at station R-1, at a stated time and row/column);
- a second nanopublication qualifying confidence in the physical measurement based on a separate calibration log.

**Test performed:** the TriG was parsed and round-tripped with RDFLib 7.5.0. Two nanopublication heads were found, each linking to its assertion, provenance, and publication-information graphs; the dataset contained 37 quads. This verifies only TriG syntax and the basic graph structure. It is not a full nanopublication conformance, signature, Trusty URI, or network test.

The main conceptual result is useful: what a source recorded can remain distinct from an assessment of the underlying measurement's reliability. The main modeling gap is also visible: the custom vocabulary and source locator still need definition, and a CSV row number alone is not durable if the file changes or rows are reordered.

### Updated hands-on status

| Experiment | Status | Result |
|---|---|---|
| OpenAlex single-DOI API retrieval | **Performed** | One live record inspected; unresolved author identities and retained raw affiliation strings observed |
| Crossref comparison for same DOI | **Performed** | Publisher metadata and OpenAlex enrichment differ in scope and representation |
| Synthetic nanopublication-shaped TriG | **Performed** | RDFLib 7.5.0 parsed and round-tripped two linked four-graph records (37 quads) |
| Canonical nanopublication conformance suite | **Reviewed, not executed** | Official valid/invalid and transform fixtures exist; actual nanopub implementation not yet run |
| Nanopublication signature / Trusty URI / test-network round trip | **Not yet performed** | — |
| Wikibase instance authoring and export | **Not yet performed** | — |
| Independent human workflow evaluation | **Not yet performed** | — |

This probe is a learning artifact only. It does not select nanopublications or RDF as the Common Knowledge storage architecture.


## Evidence locator research — CSVW, versioned datasets, and Web Annotation

The first synthetic source used a row number as its locator. That is not sufficient for durable evidence: row positions can change when data is inserted, filtered, sorted, or republished.

### CSVW provides a relevant tabular model

The W3C CSV on the Web Recommendations define an annotated tabular data model with metadata for table groups, tables, rows, columns, and cells. The companion metadata vocabulary is JSON-based and supports column datatypes, required fields, primary keys, and URI templates.

Particularly useful details:
- Rows can have a **primary key** made from one or more cells; CSVW validators must check uniqueness of the indicated key combination.
- An `aboutUrl` URI template can generate a stable URI for each row from its key values, rather than using a row position.
- URI templates also expose row and source-row positions, column names and column numbers when needed.
- Cell annotations preserve the original string value and parsed semantic value, and can carry additional application-specific annotations.
- CSVW explicitly does not define a universal method for all possible row/cell annotations, such as evidence certainty or provenance. It supplies a tabular representation and metadata mechanism, not a claim-evaluation model.

Sources:
- W3C, [Model for Tabular Data and Metadata on the Web](https://www.w3.org/TR/2015/REC-tabular-data-model-20151217/)
- W3C, [Metadata Vocabulary for Tabular Data](https://www.w3.org/TR/tabular-metadata/)

### Dataset versioning and preservation

W3C Data on the Web Best Practices recommends:
- a version number or date for each dataset;
- version history;
- persistent URIs for datasets and for individual versions;
- a stable series URI that points to the latest version, while version-specific URIs remain fixed;
- Memento as one way to express and access temporal versions.

The standard notes that version boundaries depend on the publisher's context, but even small corrections should not be made without updating the version indicator. A versioned URI provides a stable citation target. Memento can help discover which resource state was current at a given time.

Memento should not be mistaken for byte-perfect preservation. RFC 7089 notes that archived representations may be transformed for preservation or archive presentation. If exact source bytes matter, the evidence record should additionally retain a cryptographic digest and, where rights permit, a preserved copy or a durable repository identifier.

Sources:
- W3C, [Data on the Web Best Practices — Data Versioning](https://www.w3.org/TR/dwbp/#dataVersioning)
- W3C, [Data on the Web Best Practices — Dataset Version URIs](https://www.w3.org/TR/dwbp/#URIversioning)
- IETF, [RFC 7089 — Memento](https://www.rfc-editor.org/rfc/rfc7089)

### Web Annotation complements rather than replaces CSVW

Web Annotation offers selectors for text quotations, character positions, byte positions, fragments, and other media-specific regions. It also has a State model, including a Time State, for identifying which representation of a changing resource is relevant to an annotation.

This is useful for passages in HTML/PDF-like resources. For structured tabular data, CSVW is more specific about rows and cells. A Common Knowledge record could therefore use CSVW for table/row/cell identity and Web Annotation for textual or media passages. These are complementary tools, not competing locator schemes.

Sources:
- W3C, [Web Annotation Data Model](https://www.w3.org/TR/annotation-model/)
- W3C, [CSVW Model](https://www.w3.org/TR/2015/REC-tabular-data-model-20151217/)

### Small practical fixture added

The synthetic observation experiment now includes:
- a version-specific CSV source file;
- a CSVW JSON metadata file declaring a unique `measurement_id` primary key and an `aboutUrl` row URI template;
- a SHA-256 digest of the exact UTF-8 source bytes;
- a nanopublication-shaped observation that points to the versioned source URI, stable row key, evidence column, and digest;
- a separate qualification record based on the calibration log.

See [the experiment report](experiments/2026-11-synthetic-observation.md), [CSV source](experiments/2026-11-station-r1-observations.csv), [CSVW metadata](experiments/2026-11-station-r1-observations-metadata.json), and [TriG fixture](experiments/2026-11-synthetic-observation-nanopubs.trig).

**Tests performed:** Python's CSV parser read the two rows; JSON parsing succeeded; a manual uniqueness check passed for the declared primary key; SHA-256 was calculated; and the earlier TriG shape was round-tripped with RDFLib 7.5.0. The revised TriG has not yet been re-run through a nanopublication validator, and no CSVW-specific validator is installed in this environment. These are limited fixture checks, not full standards-conformance tests.

### Current design implication

A useful evidence locator should identify at least:
1. the source resource;
2. the specific version/representation of that source;
3. the region within that version (page, passage, table, row, cell, time interval, etc.);
4. a locator method appropriate to the source type;
5. a digest or other integrity check when exact source bytes are available;
6. a fallback and an explicit locator-quality status when the source has no stable key or version.

This should be a source-type-aware design. We should not force every kind of evidence into one universal offset field.


### CSVW implementation status

A current Python implementation is maintained in [cldf/csvw](https://github.com/cldf/csvw). PyPI reports version 4.2.0, released 6 November 2026, Apache-2.0, Python 3.10+. It supplies `csvwvalidate`, `csvw2json`, and `csvwdescribe` commands. The project README is candid that it does not implement the full CSVW specification and reports 269/270 JSON tests, 280/282 validation tests, and 10/18 non-normative tests passing. This is a useful validation tool, not a perfect standards oracle. The older `csvwlib` implementation is explicitly unmaintained.

Sources:
- [cldf/csvw](https://github.com/cldf/csvw)
- [csvw 4.2.0 on PyPI](https://pypi.org/project/csvw/4.2.0/)
- [CSVW tools](https://csvw.org/tools.html)

We have not run the `csvwvalidate` CLI because the package is not installed in the current runtime. The experiment report records this limitation and a pinned-version next step.


### Wikibase Cloud: a lower-friction evaluation route is now available

The current Wikibase Cloud homepage advertises an Open Beta and a free hosted Wikibase service, with European data centers and no hardware requirement. This changes the practical evaluation picture: we do not need to deploy the full self-hosted Wikibase Suite merely to try the editing workflow. The service itself warns that beta availability may not be 100%.

The hosted service has important constraints:
- A user account and a newly created wiki are required; this is not a disposable local demo.
- Official first-steps guidance says each instance should publish terms of use and an imprint, and notes that the service is hosted in Germany.
- The Cloud FAQ says the default site language cannot be changed.
- The Cloud FAQ says data is backed up daily with seven days of backups, while the current homepage advertises 30 days of guaranteed backups. These official pages conflict, so backup retention must be confirmed with the provider rather than assumed.
- The self-hosted Wikibase FAQ says Wikibase does not currently support hiding individual items or properties in an instance. Treat any hosted test instance as public-facing unless current Cloud documentation confirms otherwise; only synthetic, non-sensitive test data should be used.

Sources:
- Wikibase Cloud, [current homepage / Open Beta](https://www.wikibase.cloud/)
- MediaWiki, [Wikibase Cloud first steps](https://www.mediawiki.org/wiki/Wikibase/Wikibase.cloud/First_steps/en)
- MediaWiki, [Wikibase Cloud FAQ](https://www.mediawiki.org/wiki/Wikibase/Wikibase.cloud/FAQ)
- MediaWiki, [Wikibase FAQ](https://www.mediawiki.org/wiki/Wikibase/FAQ)

**Practical implication:** Wikibase is now feasible to evaluate without self-hosting, but the test should be done in a dedicated instance using fictional public data. Creating that instance requires a user account, email verification, and the instance's own setup steps. No account or wiki has been created by this project.


### Nanodash source and deployment spot-check

A targeted review of the current Nanodash repository README and Docker Compose file adds several practical details:
- There are multiple hosted instances; login is through ORCID.
- The built-in privacy notice explicitly describes ORCID login, a signing key held server-side, and publication as public and permanent.
- A local Docker deployment is supported and persists its Nanopub account data under a mounted `local-data` directory.
- A site can be configured in "space mode": the space becomes the home page/context and can supply its own name, logo, and stylesheet. This is a possible way to present a community-specific knowledge collection without building every browse/publish UI component from scratch.
- The current repository is licensed AGPL-3.0-or-later.
- The repository had commits on 23 November 2026, so the project is actively changing at the time of this review.

The hosted signing-key model is convenient but means the online Nanodash operator holds the key material used for publishing. This should be distinguished from command-line publication where the contributor keeps a local key file. Neither arrangement proves the truth of a publication; it changes the operational trust and recovery assumptions.

Sources:
- [Nanodash repository and README](https://github.com/knowledgepixels/nanodash)
- [Nanodash Docker Compose](https://github.com/knowledgepixels/nanodash/blob/master/docker-compose.yml)
- [Nanodash installation instructions](https://github.com/knowledgepixels/nanodash/blob/master/INSTALL-with-Docker.md)

**Limitations:** This was a repository/documentation review only. No hosted account was created, no local Nanodash instance was launched, and no user experience was tested. The local Docker route is not currently available in our execution environment because Docker is not installed.
