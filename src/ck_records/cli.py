"""Local-first tools for inspecting and validating portable knowledge records."""
import argparse
import json
import shutil
import sys
from pathlib import Path

VERSION = "0.1"
RELATIONS = {"supports", "challenges", "qualifies", "contextualizes"}


def load(path):
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(str(exc)) from exc
    if not isinstance(value, dict):
        raise ValueError("record root must be an object")
    return value


def validate(record, root):
    errors = []
    def text(obj, key, where):
        value = obj.get(key) if isinstance(obj, dict) else None
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{where}.{key} must be non-empty text")
            return None
        return value

    if record.get("format") != "common-knowledge-record":
        errors.append("format must be common-knowledge-record")
    if record.get("format_version") != VERSION:
        errors.append(f"format_version must be {VERSION}")
    text(record, "id", "record")
    text(record, "title", "record")
    statement = record.get("statement")
    if not isinstance(statement, dict):
        errors.append("statement must be an object")
        statement = {}
    text(statement, "text", "statement")
    text(statement, "scope", "statement")

    sources = record.get("sources")
    if not isinstance(sources, list):
        errors.append("sources must be an array")
        sources = []
    source_map = {}
    for i, source in enumerate(sources):
        where = f"sources[{i}]"
        if not isinstance(source, dict):
            errors.append(f"{where} must be an object")
            continue
        sid = text(source, "id", where)
        text(source, "title", where)
        relpath = text(source, "path", where)
        if sid:
            if sid in source_map:
                errors.append(f"duplicate source id: {sid}")
            source_map[sid] = source
        if relpath:
            candidate = (root / relpath).resolve()
            base = root.resolve()
            if candidate != base and base not in candidate.parents:
                errors.append(f"{where}.path escapes the record directory")
            elif not candidate.is_file():
                errors.append(f"{where}.path does not exist: {relpath}")

    evidence = record.get("evidence")
    if not isinstance(evidence, list):
        errors.append("evidence must be an array")
        evidence = []
    evidence_ids = set()
    for i, item in enumerate(evidence):
        where = f"evidence[{i}]"
        if not isinstance(item, dict):
            errors.append(f"{where} must be an object")
            continue
        eid = text(item, "id", where)
        sid = text(item, "source_id", where)
        relation = text(item, "relation", where)
        exact = text(item, "exact", where)
        prefix, suffix = item.get("prefix", ""), item.get("suffix", "")
        if eid:
            if eid in evidence_ids:
                errors.append(f"duplicate evidence id: {eid}")
            evidence_ids.add(eid)
        if sid and sid not in source_map:
            errors.append(f"{where} references unknown source: {sid}")
        if relation and relation not in RELATIONS:
            errors.append(f"{where}.relation must be one of {', '.join(sorted(RELATIONS))}")
        if not isinstance(prefix, str) or not isinstance(suffix, str):
            errors.append(f"{where}.prefix and suffix must be strings")
        source = source_map.get(sid)
        if source and exact and isinstance(source.get("path"), str):
            candidate = (root / source["path"]).resolve()
            base = root.resolve()
            if candidate != base and base not in candidate.parents:
                continue
            try:
                content = candidate.read_text(encoding="utf-8")
                count = content.count(exact)
                if count != 1:
                    errors.append(f"{where}.exact must occur exactly once in source (found {count})")
                else:
                    start = content.index(exact)
                    if isinstance(prefix, str) and prefix and content[max(0, start-len(prefix)):start] != prefix:
                        errors.append(f"{where}.prefix does not match source context")
                    if isinstance(suffix, str) and suffix and content[start+len(exact):start+len(exact)+len(suffix)] != suffix:
                        errors.append(f"{where}.suffix does not match source context")
            except (OSError, UnicodeError) as exc:
                errors.append(f"{where} source cannot be read: {exc}")

    assessments = record.get("assessments")
    if not isinstance(assessments, list):
        errors.append("assessments must be an array")
        assessments = []
    assessment_ids = set()
    for i, item in enumerate(assessments):
        where = f"assessments[{i}]"
        if not isinstance(item, dict):
            errors.append(f"{where} must be an object")
            continue
        aid = text(item, "id", where)
        text(item, "author", where)
        text(item, "conclusion", where)
        text(item, "method", where)
        if aid:
            if aid in assessment_ids:
                errors.append(f"duplicate assessment id: {aid}")
            assessment_ids.add(aid)
        refs = item.get("evidence_ids")
        if not isinstance(refs, list) or not refs:
            errors.append(f"{where}.evidence_ids must be a non-empty array")
        elif any(not isinstance(ref, str) or ref not in evidence_ids for ref in refs):
            errors.append(f"{where}.evidence_ids contains an unknown evidence id")
    return errors


def canonical(record):
    return (json.dumps(record, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def main(argv=None):
    parser = argparse.ArgumentParser(prog="ck-record")
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("validate", "inspect"):
        cmd = commands.add_parser(name)
        cmd.add_argument("record", type=Path)
    export = commands.add_parser("export")
    export.add_argument("record", type=Path, help="path to record.json")
    export.add_argument("output", type=Path, help="new package directory")
    imp = commands.add_parser("import")
    imp.add_argument("record", type=Path, help="path to record.json inside an exported package")
    imp.add_argument("output", type=Path, help="destination package directory")
    imp.add_argument("--overwrite", action="store_true")
    init = commands.add_parser("init", help="create a new empty record workspace")
    init.add_argument("directory", type=Path, help="new record directory")
    init.add_argument("--id", required=True, help="stable identifier for the record")
    init.add_argument("--title", required=True, help="short record title")
    init.add_argument("--statement", required=True, help="the precisely scoped statement")
    init.add_argument("--scope", required=True, help="what the statement does and does not claim")
    add_source = commands.add_parser("add-source", help="copy a source into a record workspace")
    add_source.add_argument("record", type=Path, help="path to record.json")
    add_source.add_argument("--id", required=True)
    add_source.add_argument("--title", required=True)
    add_source.add_argument("--file", required=True, type=Path)
    add_evidence = commands.add_parser("add-evidence", help="anchor an exact passage in a registered source")
    add_evidence.add_argument("record", type=Path, help="path to record.json")
    add_evidence.add_argument("--id", required=True)
    add_evidence.add_argument("--source-id", required=True)
    add_evidence.add_argument("--relation", required=True, choices=sorted(RELATIONS))
    add_evidence.add_argument("--exact", required=True)
    add_evidence.add_argument("--prefix", default="")
    add_evidence.add_argument("--suffix", default="")
    add_assessment = commands.add_parser("add-assessment", help="append an independently attributed assessment")
    add_assessment.add_argument("record", type=Path, help="path to record.json")
    add_assessment.add_argument("--id", required=True)
    add_assessment.add_argument("--author", required=True)
    add_assessment.add_argument("--conclusion", required=True)
    add_assessment.add_argument("--method", required=True)
    add_assessment.add_argument("--evidence-id", action="append", required=True, dest="evidence_ids")
    args = parser.parse_args(argv)
    if args.command == "init":
        target = args.directory.resolve()
        if target.exists():
            print(f"ERROR: destination already exists: {target}", file=sys.stderr)
            return 1
        record = {
            "format": "common-knowledge-record",
            "format_version": VERSION,
            "id": args.id,
            "title": args.title,
            "statement": {"text": args.statement, "scope": args.scope},
            "sources": [],
            "evidence": [],
            "assessments": [],
        }
        target.mkdir(parents=True)
        (target / "sources").mkdir()
        (target / "record.json").write_bytes(canonical(record))
        print(f"CREATED RECORD: {target / 'record.json'}")
        return 0
    source = args.record.resolve()
    try:
        record = load(source)
        errors = validate(record, source.parent)
    except ValueError as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if args.command == "add-source":
        if any(item.get("id") == args.id for item in record["sources"] if isinstance(item, dict)):
            print(f"ERROR: duplicate source id: {args.id}", file=sys.stderr)
            return 1
        source_file = args.file.resolve()
        if not source_file.is_file():
            print(f"ERROR: source file does not exist or is not a file: {source_file}", file=sys.stderr)
            return 1
        source_dir = source.parent / "sources"
        try:
            source_dir.mkdir(exist_ok=True)
            destination = source_dir / source_file.name
            resolved_destination = destination.resolve()
            if source.parent not in resolved_destination.parents:
                print("ERROR: sources directory resolves outside the record directory", file=sys.stderr)
                return 1
            if destination.exists() and destination.resolve() != source_file:
                print(f"ERROR: source filename already exists in record: {destination.name}", file=sys.stderr)
                return 1
            copied = destination.resolve() != source_file
            if copied:
                shutil.copy2(source_file, destination)
            record["sources"].append({"id": args.id, "title": args.title, "path": f"sources/{source_file.name}"})
            new_errors = validate(record, source.parent)
            if new_errors:
                if copied:
                    destination.unlink(missing_ok=True)
                for error in new_errors:
                    print(f"ERROR: {error}", file=sys.stderr)
                return 1
            source.write_bytes(canonical(record))
        except OSError as exc:
            print(f"ERROR: could not add source: {exc}", file=sys.stderr)
            return 1
        print(f"ADDED SOURCE: {args.id} ({source_file.name})")
        return 0
    if args.command == "add-evidence":
        if any(item.get("id") == args.id for item in record["evidence"] if isinstance(item, dict)):
            print(f"ERROR: duplicate evidence id: {args.id}", file=sys.stderr)
            return 1
        record["evidence"].append({
            "id": args.id, "source_id": args.source_id, "relation": args.relation,
            "exact": args.exact, "prefix": args.prefix, "suffix": args.suffix,
        })
        new_errors = validate(record, source.parent)
        if new_errors:
            for error in new_errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        source.write_bytes(canonical(record))
        print(f"ADDED EVIDENCE: {args.id}")
        return 0
    if args.command == "add-assessment":
        if any(item.get("id") == args.id for item in record["assessments"] if isinstance(item, dict)):
            print(f"ERROR: duplicate assessment id: {args.id}", file=sys.stderr)
            return 1
        record["assessments"].append({
            "id": args.id, "author": args.author, "conclusion": args.conclusion,
            "method": args.method, "evidence_ids": args.evidence_ids,
        })
        new_errors = validate(record, source.parent)
        if new_errors:
            for error in new_errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        source.write_bytes(canonical(record))
        print(f"ADDED ASSESSMENT: {args.id}")
        return 0
    if args.command == "validate":
        print(f"VALID: {record['id']} (format {VERSION})")
        print("Structural and local text-anchor checks passed; truth and source authenticity were not assessed.")
    elif args.command == "inspect":
        statement = record["statement"]
        print(f"{record['title']} [{record['id']}]\n\nSTATEMENT\n{statement['text']}\n\nSCOPE\n{statement['scope']}")
        print("\nEVIDENCE")
        for item in record["evidence"]:
            print(f"- {item['relation']}: {item['exact']} (source: {item['source_id']})")
        print("\nASSESSMENTS")
        for item in record["assessments"]:
            print(f"- {item['id']} — {item['author']}\n  {item['conclusion']}\n  Method: {item['method']}")
    elif args.command == "export":
        target = args.output.resolve()
        if target.exists():
            print(f"ERROR: destination already exists: {target}", file=sys.stderr)
            return 1
        if target == source.parent or source.parent in target.parents:
            print("ERROR: export destination cannot be inside the record directory", file=sys.stderr)
            return 1
        shutil.copytree(source.parent, target)
        (target / "record.json").write_bytes(canonical(record))
        print(f"EXPORTED PACKAGE: {target}")
    else:
        target = args.output.resolve()
        package_root = source.parent
        if target == package_root or target in package_root.parents or package_root in target.parents:
            print("ERROR: import destination cannot contain or be inside the source package", file=sys.stderr)
            return 1
        if target.exists() and not args.overwrite:
            print(f"ERROR: destination exists (use --overwrite): {target}", file=sys.stderr)
            return 1
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(package_root, target)
        print(f"IMPORTED PACKAGE: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
