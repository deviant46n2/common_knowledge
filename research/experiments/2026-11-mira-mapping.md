# MIRA mapping probe — synthetic observation and calibration evidence

- **Date:** 26 November 2026
- **Status:** Conceptual schema mapping; not a validated MIRA instance
- **Scenario:** The same fictional Station R-1 CSV observation used in the nanopublication and CSVW experiments
- **Purpose:** Determine whether the current MIRA schema already covers the essential claim/evidence relationships and identify the smallest gaps.

## Scenario

1. A versioned CSV contains a row with measurement ID `R1-20260501T0900Z`, station R-1, timestamp 09:00 UTC on 1 May 2026, dissolved oxygen 4.2 mg/L, sensor S-77.
2. A separate calibration log says sensor S-77 was overdue for calibration on that date.
3. The important distinction is between what the CSV records and whether the underlying physical measurement is accurate.

## Candidate MIRA representation

| Record | MIRA class | Main content | Relationships |
|---|---|---|---|
| Q1 | Question | What was the dissolved oxygen level at station R-1 at 09:00 UTC? | — |
| C1 | Claim | The versioned CSV records 4.2 mg/L for measurement R1-20260501T0900Z. | `addresses Q1` |
| E1 | Evidence | The specific CSV row and dissolved-oxygen column containing 4.2. | `supports C1`; `observationBase` points to the CSVW row URI; `sourceDocument` points to the versioned CSV |
| C2 | Claim | The physical dissolved-oxygen measurement was accurately captured by sensor S-77. | `addresses Q1` |
| E2 | Evidence | The calibration log entry showing S-77 was overdue for calibration. | `opposes C2`; `observationBase` points to the log-entry URI; `sourceDocument` points to the versioned calibration log |
| S1 | Study | The measurement activity that generated the observation. | `grounds E1`; may `follow P1` |
| P1 | Protocol | The measurement procedure used by the station. | `follows` from S1 |
| D1 | SourceDocument | Versioned CSV dataset. | `sourceDocument` from E1 |
| D2 | SourceDocument | Versioned calibration log. | `sourceDocument` from E2 |

This mapping uses the current MIRA classes and slots: Question, Claim, Evidence, Study, Protocol, SourceDocument, `addresses`, `supports`, `opposes`, `grounds`, `follows`, `observationBase`, `observationOriginActivity`, `observationStatement`, and `sourceDocument`.

## What maps well

1. **Claims and evidence are separate.** MIRA directly models a Claim as an assertion and Evidence as an empirical observation.
2. **Support and opposition are first-class relationships.** The CSV row can support the claim about what was recorded; the calibration entry can oppose a separate claim about measurement accuracy.
3. **Research lineage has useful structure.** Study and Protocol represent the activity and method behind an observation.
4. **The source and observation base are distinct.** `sourceDocument` can identify the versioned file; `observationBase` can point to the specific row URI produced from the CSVW primary key.
5. **Questions organize inquiry.** Claims can explicitly address a question rather than existing as an unstructured list.

## Gaps revealed by this example

### 1. No first-class source selector

MIRA's `observationBase` has range `prov:Entity`, so it can point to a row-level URI. The CSVW `aboutUrl` can supply a stable row identifier. However, MIRA does not itself define how to encode:
- exact row/column or cell coordinates;
- an exact text quotation and surrounding context;
- PDF page/paragraph/table locations;
- a source snapshot hash or retrieval representation.

This can be solved through interoperable source-specific identifiers and Web Annotation/CSVW mappings, but it is not defined by the current MIRA schema.

### 2. No explicit assessment/review object

MIRA's `supports` and `opposes` relations let Evidence and Claims act as arguments. That is useful, but the current schema does not define a distinct assessment record with:
- the exact target claim and scope assessed;
- reviewer role or qualifications;
- assessment method and criteria;
- reasoning and limitations;
- confidence/uncertainty;
- date and version of the review process;
- a `qualifies` relation distinct from support/opposition.

An assessment could be represented as another Claim or Evidence node, but that would be a convention rather than a clearly defined first-class structure.

### 3. The evidence definition is research-specific

MIRA defines Evidence as a specific empirical observation from a particular application of a research method. This is a natural fit for experimental science, but may not cover all Common Knowledge sources without extensions: legislation, court records, historical documents, official statements, testimony, policy analyses, and other documentary evidence.

### 4. No general claim-scope model

The current Claim class inherits title/content/description and has an `addresses` relation. It does not define explicit scope fields such as:
- jurisdiction or geographic extent;
- valid-from / valid-through time;
- population or entity class;
- units, thresholds, or comparison baseline;
- definitions and assumptions.

These can be expressed in the text or with new terms, but the schema does not yet standardize them.

### 5. Schema and licensing maturity

The repository describes itself as a working version. Its SHACL shapes for Claim and Evidence are closed shapes, which means new properties need to be introduced deliberately through schema changes or additional shapes. The repository review found no license file or repository license metadata. Clarify licensing and extension policy with maintainers before reusing the schema or generated artifacts.

## Result

**MIRA can already express the core scientific pattern of questions, claims, empirical evidence, support, opposition, studies, protocols, and source documents.** That is a substantial head start over designing those concepts from scratch.

It does not yet provide the complete general-purpose record Common Knowledge is considering. The biggest gaps for our intended scope are exact source selectors, general documentary evidence, explicit assessment/review records, and claim scope/uncertainty.

## Next step

Do not fork or extend the schema unilaterally. Ask MIRA maintainers whether these are recognized gaps, what extension mechanism they intend, and whether they want to support non-scientific domains. If the answers are positive, propose a small interoperable extension or mapping rather than creating a parallel vocabulary.
