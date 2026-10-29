#!/usr/bin/env python3
"""Strict ordered ten-key contract; standard library only, no image evaluation."""
import json
from pathlib import Path
import sys

KEYS = ["Subject", "Clothing", "Pose", "Setting", "Camera Settings", "Lighting", "Effects", "Background", "Details", "Quality"]

def unique(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"Duplicate key: {key}")
        out[key] = value
    return out

def reject_constant(value):
    raise ValueError(f"Invalid JSON constant: {value}")

def validate_text(text):
    try:
        obj = json.loads(text, object_pairs_hook=unique, parse_constant=reject_constant)
    except (ValueError, TypeError) as exc:
        return [str(exc)]
    if not isinstance(obj, dict):
        return ["Output must be an object."]
    errors = []
    if list(obj) != KEYS:
        errors.append("Keys must match the ten-field contract and its exact order.")
    if any(not isinstance(value, str) for value in obj.values()):
        errors.append("Every value must be a string.")
    return errors

if __name__ == "__main__":
    try:
        if len(sys.argv) > 2:
            raise ValueError("Use validate_json.py [raw-json-file], or stdin.")
        text = Path(sys.argv[1]).read_text(encoding="utf-8") if len(sys.argv) == 2 else sys.stdin.read()
        errors = validate_text(text)
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    for error in errors:
        print(f"ERROR: {error}")
    if not errors:
        print("OK: ordered JSON contract. Language and visual fidelity not evaluated.")
    sys.exit(bool(errors))
