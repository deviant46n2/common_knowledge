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


def test_cli_round_trips_record_and_source_files(tmp_path):
    import subprocess
    import sys

    package = tmp_path / "package"
    imported = tmp_path / "imported"
    env = {"PYTHONPATH": str(FIXTURE.parents[3] / "src")}
    export_result = subprocess.run(
        [sys.executable, "-m", "ck_records", "export", str(FIXTURE), str(package)],
        capture_output=True, text=True, env=env,
    )
    assert export_result.returncode == 0, export_result.stderr
    assert (package / "record.json").is_file()
    assert (package / "sources" / "station-r1.csv").is_file()
    import_result = subprocess.run(
        [sys.executable, "-m", "ck_records", "import", str(package / "record.json"), str(imported)],
        capture_output=True, text=True, env=env,
    )
    assert import_result.returncode == 0, import_result.stderr
    imported_record = load(imported / "record.json")
    assert validate(imported_record, imported) == []



def test_export_rejects_destination_inside_record_directory(tmp_path):
    import subprocess
    import sys

    destination = FIXTURE.parent / "nested-export"
    result = subprocess.run(
        [sys.executable, "-m", "ck_records", "export", str(FIXTURE), str(destination)],
        capture_output=True, text=True,
        env={"PYTHONPATH": str(FIXTURE.parents[3] / "src")},
    )
    assert result.returncode == 1
    assert "cannot be inside the record directory" in result.stderr
    assert not destination.exists()


def test_import_rejects_destination_that_would_delete_source_package(tmp_path):
    import subprocess
    import sys

    result = subprocess.run(
        [sys.executable, "-m", "ck_records", "import", str(FIXTURE), str(FIXTURE.parent), "--overwrite"],
        capture_output=True, text=True,
        env={"PYTHONPATH": str(FIXTURE.parents[3] / "src")},
    )
    assert result.returncode == 1
    assert "cannot contain or be inside the source package" in result.stderr
    assert FIXTURE.is_file()
