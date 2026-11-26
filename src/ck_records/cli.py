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
            try:
                content = (root / source["path"]).resolve().read_text(encoding="utf-8")
                count = content.count(exact)
                if count != 1:
                    errors.append(f"{where}.exact must occur exactly once in source (found {count})")
                else:
                    start = content.index(exact)
                    if prefix and content[max(0, start-len(prefix)):start] != prefix:
                        errors.append(f"{where}.prefix does not match source context")
                    if suffix and content[start+len(exact):start+len(exact)+len(suffix)] != suffix:
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
        elif any(ref not in evidence_ids for ref in refs):
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
    args = parser.parse_args(argv)
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
        target.mkdir(parents=True)
        shutil.copytree(source.parent, target)
        (target / "record.json").write_bytes(canonical(record))
        print(f"EXPORTED PACKAGE: {target}")
    else:
        target = args.output.resolve()
        if target.exists() and not args.overwrite:
            print(f"ERROR: destination exists (use --overwrite): {target}", file=sys.stderr)
            return 1
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source.parent, target)
        print(f"IMPORTED PACKAGE: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
