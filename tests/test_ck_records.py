import json
from pathlib import Path

from ck_records.cli import canonical, load, validate

FIXTURE = Path(__file__).parent.parent / "examples" / "records" / "r1" / "record.json"


def test_example_has_two_distinct_assessments():
    record = load(FIXTURE)
    assert validate(record, FIXTURE.parent) == []
    assert len(record["assessments"]) == 2
    assert record["assessments"][0]["id"] != record["assessments"][1]["id"]


def test_quote_must_match_exactly_once():
    record = load(FIXTURE)
    record["evidence"][0]["exact"] = "not present"
    assert any("occur exactly once" in e for e in validate(record, FIXTURE.parent))


def test_prefix_context_is_checked():
    record = load(FIXTURE)
    record["evidence"][0]["prefix"] = "wrong context"
    assert any("prefix does not match" in e for e in validate(record, FIXTURE.parent))


def test_source_path_cannot_escape_record_directory():
    record = load(FIXTURE)
    record["sources"][0]["path"] = "../../outside.csv"
    assert any("escapes the record directory" in e for e in validate(record, FIXTURE.parent))


def test_unknown_references_are_rejected():
    record = load(FIXTURE)
    record["evidence"][0]["source_id"] = "missing"
    record["assessments"][0]["evidence_ids"] = ["missing"]
    errors = validate(record, FIXTURE.parent)
    assert any("unknown source" in e for e in errors)
    assert any("unknown evidence id" in e for e in errors)


def test_duplicate_assessment_ids_are_rejected():
    record = load(FIXTURE)
    record["assessments"][1]["id"] = record["assessments"][0]["id"]
    assert any("duplicate assessment id" in e for e in validate(record, FIXTURE.parent))


def test_export_is_deterministic():
    record = load(FIXTURE)
    assert canonical(record) == canonical(json.loads(canonical(record)))


def test_unknown_format_version_is_rejected():
    record = load(FIXTURE)
    record["format_version"] = "99"
    assert any("format_version" in e for e in validate(record, FIXTURE.parent))
