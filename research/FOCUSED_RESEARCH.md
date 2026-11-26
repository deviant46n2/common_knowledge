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
