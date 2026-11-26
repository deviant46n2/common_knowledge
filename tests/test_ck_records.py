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



def test_init_creates_valid_record_workspace(tmp_path):
    import subprocess
    import sys

    directory = tmp_path / "new-record"
    result = subprocess.run(
        [
            sys.executable, "-m", "ck_records", "init", str(directory),
            "--id", "urn:ck:test:starter",
            "--title", "Starter record",
            "--statement", "The documented test statement.",
            "--scope", "This statement describes only the supplied test fixture.",
        ],
        capture_output=True, text=True,
        env={"PYTHONPATH": str(FIXTURE.parents[3] / "src")},
    )
    assert result.returncode == 0, result.stderr
    assert (directory / "sources").is_dir()
    record = load(directory / "record.json")
    assert validate(record, directory) == []
    assert record["sources"] == []
    assert record["evidence"] == []
    assert record["assessments"] == []


def test_init_refuses_to_overwrite_existing_directory(tmp_path):
    import subprocess
    import sys

    directory = tmp_path / "existing"
    directory.mkdir()
    sentinel = directory / "keep.txt"
    sentinel.write_text("preserve", encoding="utf-8")
    result = subprocess.run(
        [
            sys.executable, "-m", "ck_records", "init", str(directory),
            "--id", "urn:ck:test:starter",
            "--title", "Starter record",
            "--statement", "The documented test statement.",
            "--scope", "This statement describes only the supplied test fixture.",
        ],
        capture_output=True, text=True,
        env={"PYTHONPATH": str(FIXTURE.parents[3] / "src")},
    )
    assert result.returncode == 1
    assert sentinel.read_text(encoding="utf-8") == "preserve"



def test_non_string_anchor_context_is_reported_without_crashing():
    record = load(FIXTURE)
    record["evidence"][0]["prefix"] = 123
    record["evidence"][1]["suffix"] = ["not", "text"]
    errors = validate(record, FIXTURE.parent)
    assert any("prefix and suffix must be strings" in error for error in errors)



def test_cli_builds_record_from_source_through_assessment(tmp_path):
    import subprocess
    import sys

    directory = tmp_path / "field-record"
    source_file = tmp_path / "field-notes.txt"
    source_file.write_text("Field notebook: The sample measured 12 units at noon.", encoding="utf-8")
    env = {"PYTHONPATH": str(FIXTURE.parents[3] / "src")}

    def run(*args):
        return subprocess.run(
            [sys.executable, "-m", "ck_records", *map(str, args)],
            capture_output=True, text=True, env=env,
        )

    created = run(
        "init", directory, "--id", "urn:ck:test:field",
        "--title", "Field observation",
        "--statement", "The field notebook records a measurement of 12 units.",
        "--scope", "This is a statement about what the notebook records.",
    )
    assert created.returncode == 0, created.stderr

    added_source = run(
        "add-source", directory / "record.json", "--id", "notebook",
        "--title", "Field notebook", "--file", source_file,
    )
    assert added_source.returncode == 0, added_source.stderr

    added_evidence = run(
        "add-evidence", directory / "record.json", "--id", "notebook-line",
        "--source-id", "notebook", "--relation", "supports",
        "--exact", "The sample measured 12 units at noon.",
        "--prefix", "Field notebook: ",
    )
    assert added_evidence.returncode == 0, added_evidence.stderr

    added_assessment = run(
        "add-assessment", directory / "record.json", "--id", "review-1",
        "--author", "Reviewer A",
        "--conclusion", "The notebook supports that this value was recorded.",
        "--method", "Read the cited line in the supplied notebook.",
        "--evidence-id", "notebook-line",
    )
    assert added_assessment.returncode == 0, added_assessment.stderr

    record = load(directory / "record.json")
    assert validate(record, directory) == []
    assert (directory / "sources" / "field-notes.txt").is_file()
    assert len(record["sources"]) == 1
    assert len(record["evidence"]) == 1
    assert len(record["assessments"]) == 1


def test_add_evidence_rejects_unmatched_quote_without_mutating_record(tmp_path):
    import subprocess
    import sys

    directory = tmp_path / "field-record"
    env = {"PYTHONPATH": str(FIXTURE.parents[3] / "src")}
    subprocess.run(
        [
            sys.executable, "-m", "ck_records", "init", str(directory),
            "--id", "urn:ck:test:field", "--title", "Field observation",
            "--statement", "The notebook records a measurement.",
            "--scope", "This describes the notebook only.",
        ],
        check=True, capture_output=True, text=True, env=env,
    )
    record_path = directory / "record.json"
    before = record_path.read_bytes()
    result = subprocess.run(
        [
            sys.executable, "-m", "ck_records", "add-evidence", str(record_path),
            "--id", "e1", "--source-id", "missing", "--relation", "supports",
            "--exact", "not present",
        ],
        capture_output=True, text=True, env=env,
    )
    assert result.returncode == 1
    assert record_path.read_bytes() == before
