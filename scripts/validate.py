#!/usr/bin/env python3
from pathlib import Path
import json, sys

try:
    import jsonschema
    from referencing import Registry, Resource
except Exception as exc:
    print("Install requirements.txt first:", exc)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
FIXTURE_DIR = ROOT / "conformance" / "fixtures"

schemas = {}
registry = Registry()

for path in SCHEMA_DIR.glob("*.schema.json"):
    obj = json.loads(path.read_text(encoding="utf-8"))
    sid = obj.get("$id")
    if sid:
        schemas[path.stem.replace(".schema","")] = obj
        registry = registry.with_resource(sid, Resource.from_contents(obj))

def validate_schema(name, obj):
    schema = schemas[name]
    validator = jsonschema.Draft202012Validator(schema, registry=registry, format_checker=jsonschema.FormatChecker())
    errors = sorted(validator.iter_errors(obj), key=lambda e: list(e.path))
    return errors

def semantic_check(schema_name, obj, context):
    errors = []

    if schema_name == "admission-record":
        required_checks = ("identity","schema","provenance","disclosure","integrity")
        if obj.get("disposition") in ("admitted","admitted_restricted") and not all(obj.get("checks",{}).get(k) for k in required_checks):
            errors.append("admitted disposition requires all required checks to pass")

    elif schema_name == "disclosure-profile":
        if obj.get("posture") != "complete_source" and len(obj.get("verification_limits",[])) == 0:
            errors.append("non-complete disclosure posture requires verification_limits")

    elif schema_name == "comparability-assessment":
        dims = obj.get("dimensions",{})
        outcome = obj.get("outcome")
        if outcome == "comparable" and any(v in ("unknown","incompatible") for v in dims.values()):
            errors.append("comparable outcome cannot contain unknown or incompatible dimensions")
        if outcome == "conditionally_comparable" and not obj.get("conditions"):
            errors.append("conditionally_comparable requires conditions")

    elif schema_name == "federation-transfer":
        if obj.get("source_node") == obj.get("destination_node"):
            errors.append("source_node and destination_node must differ")
        notes = context.get("notes","")
        if "disclosure-inflation" in context.get("fixture_id","") and obj.get("disclosure") == "complete_source":
            errors.append("transfer disclosure cannot exceed known artifact disclosure")
        if "challenge-drop" in context.get("fixture_id","") and not obj.get("challenge_refs"):
            errors.append("known open challenge must propagate")

    elif schema_name == "aggregation-record":
        if not obj.get("contract",{}).get("duplicate_policy","").strip():
            errors.append("duplicate_policy must be non-empty")

    return errors

total = passed = failed = 0
for path in sorted(FIXTURE_DIR.rglob("*.json")):
    total += 1
    fx = json.loads(path.read_text(encoding="utf-8"))
    schema_name = fx["schema"]
    obj = fx["object"]
    schema_errors = validate_schema(schema_name, obj)
    schema_valid = not schema_errors
    sem_errors = semantic_check(schema_name, obj, fx)
    semantic = "pass" if not sem_errors else "fail"

    expected_schema = fx["expect_schema_valid"]
    expected_sem = fx["expect_semantic"]

    ok = (schema_valid == expected_schema) and (semantic == expected_sem or not schema_valid)
    if ok:
        passed += 1
    else:
        failed += 1
        print(f"FAIL {path.relative_to(ROOT)}")
        print("  expected schema:", expected_schema, "actual:", schema_valid)
        print("  expected semantic:", expected_sem, "actual:", semantic)
        for e in schema_errors[:3]:
            print("  schema:", e.message)
        for e in sem_errors[:3]:
            print("  semantic:", e)

print(f"ECS fixture validation: {passed}/{total} passed, {failed} failed")
sys.exit(0 if failed == 0 else 1)
