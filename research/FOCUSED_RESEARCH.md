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
- the full RDF export versus truthy export;
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
