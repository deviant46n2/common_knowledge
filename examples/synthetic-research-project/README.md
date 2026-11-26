# Synthetic Plant Growth Study

This is a deliberately small, entirely synthetic computational research project used to test Common Knowledge's research-project preflight prototype.

## Research question

In this invented dataset, how does simulated light exposure relate to plant height after a fixed observation period?

## Method

The dataset contains six synthetic observations: three in a control group and three in a simulated treatment group. The analysis script calculates group means and their difference. No real plants, people, or external datasets are involved.

## Structure

- `data/measurements.csv`: synthetic observations.
- `src/analyze.py`: standard-library-only analysis script.
- `results/run-001/summary.csv`: first recorded result.
- `results/run-002/summary.csv`: second recorded result.
- `report.md`: short narrative report.

## Re-run

From the project root:

```bash
python src/analyze.py
```

The script prints the group means and difference. It does not overwrite the recorded result files.

## Scope and limitations

This fixture is intentionally tiny and synthetic. It is not a scientific study and its values have no empirical meaning. Some inconsistencies and missing references are intentional test conditions documented in `GROUND_TRUTH.md` at the repository level.
