# Wikibase Cloud — live API and query probe

- **Date:** 26 November 2026
- **Status:** Read-only hands-on test against a public Wikibase Cloud instance
- **Instance:** [Beyond Notability](https://beyond-notability.wikibase.cloud/)
- **Entity inspected:** Q106 (public sample item)
- **No records were created or edited.**

## Purpose

Verify that a real Wikibase Cloud instance exposes the documented entity model, statement qualifiers, reference nodes, query service, and revision history through public APIs.

## Requests performed

1. Entity search through `wbsearchentities`.
2. Entity retrieval through `wbgetentities` for Q106, including labels, descriptions, claims, and revision metadata.
3. Revision history through `action=query&prop=revisions`, requesting revision IDs, timestamps, contributor attribution, and comments.
4. SPARQL query against the instance's public query endpoint to find P37 statement nodes carrying P1 time qualifiers and `prov:wasDerivedFrom` reference nodes.
5. A second SPARQL query followed the full qualifier-value node (`pqv:P1`) and read `wikibase:timeValue`, `wikibase:timePrecision`, `wikibase:timeTimezone`, and `wikibase:timeCalendarModel`.

The direct `Special:EntityData/Q106.ttl` route was also attempted with `flavor=simple` and `flavor=full`, but the instance's Anubis anti-bot challenge prevented this retrieval. No direct simple/full Turtle file comparison was completed.

## Observations

### The APIs work on a real hosted instance

The public search and entity endpoints returned labeled items and a structured entity JSON document. Q106 included a large set of claims; the entity response included `lastrevid` and `modified`.

The revision-history endpoint returned revision IDs, parent revision IDs, timestamps, editor attribution, and edit summaries. This demonstrates a real, inspectable edit history, not merely a theoretical MediaWiki feature.

### Qualifiers and references are present in the live data

The SPARQL endpoint returned statement nodes linked from Q106, each with:
- a main statement value;
- a P1 time qualifier;
- a reference node linked by `prov:wasDerivedFrom`.

This confirms that the query service exposes the full statement model and that reference nodes can be retrieved separately from the statement value.

### Precision can be lost if consumers read only the simple value

A year-level qualifier in the entity JSON used a time value like `+1931-00-00T00:00:00Z` with precision code `9` (year).

The SPARQL simple qualifier value was returned as `1931-01-01T00:00:00Z`. The full qualifier-value node also had a `wikibase:timeValue` of `1931-01-01T00:00:00Z`, but crucially retained `wikibase:timePrecision 9` and the calendar model.

**Implication:** A consumer that renders the simple RDF literal as an exact date would silently invent day/month precision. A Common Knowledge importer must read the full value node for time values and preserve the precision field. Similar care is needed for quantities, where full values can carry units and uncertainty bounds.

This is a concrete example of why a data export can be syntactically valid and still lose meaning when a consumer chooses the wrong projection.

### References are not yet evidence passages

The inspected reference nodes contain source metadata such as external URLs, item identifiers, or bibliographic text. This is useful provenance, but it does not automatically identify the exact page, paragraph, table row, or data cell that supports a statement. The Common Knowledge evidence-location layer remains a separate requirement.

## Results

- **Search API:** PASS.
- **Entity JSON retrieval:** PASS.
- **Revision-history retrieval:** PASS.
- **SPARQL statement/qualifier/reference query:** PASS.
- **Full-value time-precision query:** PASS.
- **Direct EntityData Turtle retrieval:** BLOCKED by anti-bot challenge; no conclusion about the instance's RDF export behavior from this request.
- **Editing workflow:** NOT TESTED.
- **User permissions and independent review workflow:** NOT TESTED.
- **Source-passage anchoring:** NOT PROVIDED by the example statements; requires additional modeling.

## Conclusions

1. Wikibase Cloud can be evaluated through live read-only APIs without deploying infrastructure.
2. The JSON API and SPARQL service expose statements, qualifiers, references, and revision history in practice.
3. Time precision is a critical interoperability concern: use full values, not only simple literals.
4. References are bibliographic/source metadata, not necessarily exact evidence locators.
5. This read-only test does not establish whether Wikibase's contributor UI is appropriate for the Common Knowledge workflow. A dedicated synthetic instance is still needed to test creation and editing.

## Reproducible endpoint patterns

- Entity JSON: `/w/api.php?action=wbgetentities&ids=Q106&props=info|labels|descriptions|claims&languages=en&format=json`
- Revision history: `/w/api.php?action=query&prop=revisions&pageids=155&rvprop=ids|timestamp|user|comment&rvlimit=5&format=json`
- Query service: `/query/sparql?query=...`

The sample item and all its contents belong to the public Wikibase instance; this report does not copy its full data.
