"""Analyze the tiny synthetic plant-growth fixture using only Python's stdlib."""

import csv
from pathlib import Path
from statistics import mean

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_ROOT / "data" / "measurements.csv"


def main() -> None:
    groups: dict[str, list[float]] = {"control": [], "treatment": []}
    with DATA_FILE.open(newline="", encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            groups[row["group"]].append(float(row["height_mm"]))

    control_mean = mean(groups["control"])
    treatment_mean = mean(groups["treatment"])
    difference = treatment_mean - control_mean

    print(f"control_mean_mm={control_mean:.1f}")
    print(f"treatment_mean_mm={treatment_mean:.1f}")
    print(f"difference_mm={difference:.1f}")


if __name__ == "__main__":
    main()
