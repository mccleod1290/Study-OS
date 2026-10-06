#!/usr/bin/env python3
"""Is a usage review due? python skills/scripts/learn_due.py [--mark]
Prints DUE or OK. Cadence: 7 days. --mark records today as the last review."""
import json, sys
from datetime import date
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / ".rules").is_dir())
ST = ROOT / "Artifacts" / "artifacts" / "self_learning" / "_state.json"
DAYS = 7
if "--mark" in sys.argv:
    ST.parent.mkdir(parents=True, exist_ok=True)
    ST.write_text(json.dumps({"last_review": date.today().isoformat()}), encoding="utf-8")
    print("marked", date.today().isoformat())
else:
    last = json.loads(ST.read_text(encoding="utf-8"))["last_review"] if ST.exists() else None
    if not last:
        print("DUE: never reviewed")
    else:
        age = (date.today() - date.fromisoformat(last)).days
        print(f"DUE: last review {last}, {age} days ago" if age >= DAYS else f"OK: last review {last}, {age} days ago")
