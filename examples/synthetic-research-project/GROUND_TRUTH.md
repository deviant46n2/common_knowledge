# Fixture Ground Truth

This file documents expected facts for the synthetic project. It is part of the test fixture, not a claim about real research.

## Known correct facts

- The dataset contains six rows: three control and three treatment observations.
- Control heights are 10, 11, and 9 mm; the mean is 10.0 mm.
- Treatment heights are 13, 14, and 12 mm; the mean is 13.0 mm.
- The treatment-minus-control difference is 3.0 mm.
- Both recorded summaries, run-001 and run-002, contain the same values.
- The analysis script uses only the Python standard library.

## Deliberate defects

1. **Incorrect numerical claim:** report.md states a 4.0 mm difference, but the cited run-001 summary records 3.0 mm.
2. **Broken artifact reference:** report.md links to results/run-003/summary.csv, which does not exist.
3. **Ambiguous sensitivity statement:** report.md calls run-002 a second analysis but does not explain what changed from run-001.

## Expected caution

- A static inspector may verify that the referenced run-001 file exists and that the reported value differs from its recorded value only if it understands the report's claim-to-metric relationship. It must not imply that it has independently reproduced the analysis.
- The existence of two result files does not prove that two distinct computational executions occurred.
- A file reference that resolves does not prove that its contents are scientifically valid.
- The project is intentionally small; absence of a dependency manifest is not a defect because the script uses only the standard library.
