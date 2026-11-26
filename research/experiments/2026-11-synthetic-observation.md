# Synthetic observation — nanopublication shape probe

- **Date:** 26 November 2026
- **Status:** Exploratory local data-model test; not a production schema
- **Source file:** [Two nanopublication-shaped records](2026-11-synthetic-observation-nanopubs.trig)

## Purpose

Test whether a small observation and a separate qualification can be represented as two linked nanopublications without conflating what a source recorded with an assessment of the measurement's reliability.

## Synthetic scenario

- Station R-1's CSV row 42 records dissolved oxygen of 4.2 mg/L at 09:00 UTC on 1 May 2026.
- A separate calibration log says the sensor was overdue for calibration on that date.
- The record therefore distinguishes the statement about what the CSV contains from the assessment that confidence in the physical measurement is limited.

All sources, identifiers, people, and measurements in this fixture are fictional placeholders. No external data or real people are represented.

## Representation tested

The TriG file contains two nanopublication-shaped datasets:

1. **Observation:** assertion graph records the station, property, value, unit, timestamp, and CSV row/column locator. Its provenance graph links the assertion to the CSV source and an extraction activity.
2. **Qualification:** assertion graph records an assessment that qualifies confidence in the measurement, links it to the observation, and records the calibration log as evidence. Its provenance graph links the assessment to the prior observation and review activity.

Each has the nanopublication head, assertion, provenance, and publication-information graphs. The fixture uses PROV-O for activity/source/agent relationships.

## Test performed

- Parsed the serialized TriG using RDFLib 7.5.0.
- Parsed it back into a new RDF Dataset.
- Confirmed that two nanopublication heads were present.
- Confirmed each head links to assertion, provenance, and publication-information graphs.
- Counted 37 quads across the dataset.

**Result:** TriG syntax and this basic graph structure passed the local round-trip parse.

## What this test does not prove

- It does not prove full nanopublication conformance.
- It does not verify Trusty URI generation or cryptographic signatures.
- It does not publish to or retrieve from the nanopublication test network.
- It does not validate the semantics of the custom `ck:` vocabulary.
- It does not show that a human contributor can author or understand the record.
- It does not yet provide durable source versioning or a robust CSV row locator.
- It does not validate the evidence itself; the scenario is fictional.

## Findings

1. **The separation is useful:** a statement about what a source recorded can remain distinct from an assessment about the reliability of the underlying observation.
2. **The relationship is expressible:** the second nanopublication can refer to the first and preserve its own provenance.
3. **The vocabulary remains ours to define:** nanopublications and PROV-O provide structure and lineage, but they do not define the meaning of "qualification", "measurement accuracy uncertain", or the precise source-row locator.
4. **The reader experience is still unknown:** a graph can encode this distinction while still being difficult to inspect. A human-readable interface is essential.
5. **The source anchor needs work:** a CSV row number is not durable if rows are reordered or the file changes. A future experiment should include a source version/content hash and a stable row key, not just row position.

## Next checks

- Run the fixture through an actual nanopublication implementation and the canonical conformance suite.
- Try authoring the same structure through a Nanodash template.
- Test whether a separate reviewer can publish a conflicting or alternative assessment without replacing the observation.
- Test source versioning and row-level anchors against a changed CSV file.


### Additional locator stability check

Two in-memory variants were generated from the fixture:
- **Rows reordered:** the primary-key values remained the same, so the record key still identifies the same measurement even though its row position changed. The file SHA-256 changed to `f797ea05818013a41eecd59bfa7302657e95bc8fb353911e4486ea055b36a7fb`.
- **Measurement value edited from 4.2 to 4.3:** the primary key remained the same but the file SHA-256 changed to `89ef195feb45520c7e9d8a85be722cb4737ce8f63d8f301d72b3997f94a78808`.

This confirms the intended distinction: the primary key tracks the logical row across reordering, while the content digest detects changes to the exact file representation. A changed dataset should receive a new version identity; the digest alone should not be used to silently treat a changed file as the same source version.


## CSVW implementation candidate

A current Python implementation is available in the `cldf/csvw` project. As of this research pass, PyPI reports version **4.2.0**, released 6 November 2026, under Apache-2.0, requiring Python 3.10 or later. It provides `csvwvalidate`, `csvw2json`, and `csvwdescribe` command-line tools.

This is a practical candidate for validating the fixture, but its own README is explicit that it does not implement the full CSVW specification. It reports 269/270 JSON tests, 280/282 validation tests, and 10/18 non-normative tests passing. Its documented limitations should be treated as real; a pass from this implementation is useful validation, not proof of full W3C conformance.

The older `csvwlib` project is explicitly unmaintained and should not be the default choice.

Sources:
- [cldf/csvw README](https://github.com/cldf/csvw)
- [cldf/csvw changelog](https://github.com/cldf/csvw/blob/master/CHANGES)
- [csvw 4.2.0 on PyPI](https://pypi.org/project/csvw/4.2.0/)
- [CSVW tools overview](https://csvw.org/tools.html)

**Execution status:** The `csvwvalidate` CLI was not run in this environment because the package is not installed and package installation is not available in the current runtime. The next local validation should pin `csvw==4.2.0` in a disposable environment and run `csvwvalidate` against the metadata fixture.
