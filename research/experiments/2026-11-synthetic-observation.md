# Synthetic observation — evidence-location and nanopublication probe

- **Date:** 26 November 2026
- **Status:** Exploratory local data-model test; not a production schema
- **Files:** [CSV source](2026-11-station-r1-observations.csv), [CSVW metadata](2026-11-station-r1-observations-metadata.json), [nanopublication-shaped TriG](2026-11-synthetic-observation-nanopubs.trig)

## Purpose

Test whether a source can be identified at both the dataset-version level and the individual-row/column level, while keeping a source observation distinct from a later assessment of its reliability.

## Synthetic scenario

- Station R-1's CSV row with measurement ID `R1-20260501T0900Z` records dissolved oxygen of 4.2 mg/L at 09:00 UTC on 1 May 2026.
- A separate calibration log says the sensor was overdue for calibration on that date.
- The record distinguishes what the CSV records from an assessment of the physical measurement's reliability.

All sources, identifiers, people, and measurements are fictional placeholders.

## Source version and tabular locator

The CSV is assigned a version-specific URI, with a separate series URI in the CSVW metadata. The metadata declares:
- the column names and datatypes;
- `measurement_id` as a primary key;
- an `aboutUrl` template that creates a row URI from that key;
- a version string and series relationship.

The source file's SHA-256 is:

`e9e7a483252cfd45c57ee0fe9ecd9f1f261e33d24ef1c69d53c0bcb892a0021d`

The TriG observation points to the versioned CSV, the measurement key, the evidence column, and the digest.

This is stronger than a row number alone: row order can change while the primary key remains stable, and the digest detects changes to the exact byte representation. It still depends on the publisher preserving the versioned source URI and not reusing the same key for a different measurement.

## Representation

The TriG file contains two nanopublication-shaped datasets:

1. **Observation:** assertion graph records the station, property, value, unit, timestamp, and CSV row/column locator. Its provenance graph links the assertion to the CSV source and an extraction activity.
2. **Qualification:** assertion graph records an assessment that qualifies confidence in the measurement, links it to the observation, and records the calibration log as evidence. Its provenance graph links the assessment to the prior observation and review activity.

Each has the nanopublication head, assertion, provenance, and publication-information graphs. The fixture uses PROV-O for activity/source/agent relationships.

## Tests performed

- Parsed the CSV with Python's CSV parser: **PASS** (2 rows).
- Parsed the CSVW metadata as JSON: **PASS**.
- Checked the declared primary key is unique in the sample: **PASS**.
- Calculated SHA-256 over the exact UTF-8 CSV bytes: **PASS**.
- Parsed an official nanopublication test-suite `valid/plain` TriG example with RDFLib 7.5.0: **PASS** (four named graphs, nine quads).
- Parsed the initial synthetic TriG shape with RDFLib 7.5.0 and round-tripped it through a fresh RDF Dataset: **PASS** (two nanopublication heads, 37 quads).
- Generated two in-memory CSV variants to test locator behavior:
  - **Rows reordered:** primary-key values remained the same, while the file digest changed to `f797ea05818013a41eecd59bfa7302657e95bc8fb353911e4486ea055b36a7fb`.
  - **Measurement value edited from 4.2 to 4.3:** the primary key remained the same, while the file digest changed to `89ef195feb45520c7e9d8a85be722cb4737ce8f63d8f301d72b3997f94a78808`.

**Result:** The local checks demonstrate that the key can continue identifying a logical row across reordering, while the file digest detects a changed byte representation. The initial TriG structure also parsed and round-tripped. These are limited checks, not full standards-conformance tests.

## CSVW implementation candidate

A current Python implementation is maintained in the `cldf/csvw` project. PyPI reports version **4.2.0**, released 6 November 2026, under Apache-2.0, requiring Python 3.10 or later. It provides `csvwvalidate`, `csvw2json`, and `csvwdescribe` command-line tools.

Its own README is explicit that it does not implement the full CSVW specification. It reports 269/270 JSON tests, 280/282 validation tests, and 10/18 non-normative tests passing. It is a useful validation tool, not a perfect standards oracle. The older `csvwlib` project is explicitly unmaintained.

Sources:
- [cldf/csvw README](https://github.com/cldf/csvw)
- [cldf/csvw changelog](https://github.com/cldf/csvw/blob/master/CHANGES)
- [csvw 4.2.0 on PyPI](https://pypi.org/project/csvw/4.2.0/)
- [CSVW tools overview](https://csvw.org/tools.html)

**Execution status:** The `csvwvalidate` CLI was not run because the package is not installed in the current runtime. The revised TriG was not re-run through a nanopublication validator. No Trusty URI, cryptographic signature, or network publication was tested.

## Findings

1. **The separation is useful:** a statement about what a source recorded can remain distinct from an assessment about the reliability of the underlying observation.
2. **The relationship is expressible:** a second nanopublication can refer to the first and preserve its own provenance.
3. **CSVW supplies an existing tabular locator model:** a primary key and URI template are preferable to relying only on row position.
4. **A version URI and digest do different jobs:** the URI names the intended dataset edition; the digest detects byte-level changes. Neither should silently substitute for the other.
5. **The vocabulary remains ours to define:** nanopublications and PROV-O provide structure and lineage, but do not define the meaning of "qualification", "measurement accuracy uncertain", or all evidence relations.
6. **The reader experience is still unknown:** a graph can encode the distinction while still being difficult to inspect. A human-facing interface remains essential.
7. **Locator strength varies:** many real sources lack primary keys or stable versioned URIs. The system will need fallback locators and should expose their limitations.

## What this test does not prove

- Full CSVW or nanopublication conformance.
- Trusty URI generation or cryptographic signature validity.
- Successful publication to or retrieval from the nanopublication test network.
- Correctness of the custom `ck:` vocabulary or any underlying scientific claim.
- That a human contributor can author or understand the record.
- That a CSVW validator or source-preservation strategy works in production.

## Next checks

- Pin `csvw==4.2.0` in a disposable environment and run `csvwvalidate` on the metadata fixture.
- Run the revised TriG through the canonical nanopublication conformance suite and an actual nanopublication implementation.
- Test a conflicting assessment from a second contributor without replacing the original observation.
- Try authoring the same structure through a Nanodash template.
- Test a source with no primary key and a textual source using Web Annotation selectors.
