"""Shared layout for the Study OS hooks. See .rules/artifacts-and-sessions.md.
Artifacts/sessions/<YYYY>/<DD-MM>/<HH-MM-SS>_<session id>/   one folder per session
Artifacts/artifacts/<topic_slug>/                              deliverables, no dates in names
"""
from __future__ import annotations
import json, re
from datetime import datetime
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / ".rules").is_dir())
BASE = ROOT / "Artifacts"
SESSIONS = BASE / "sessions"
ARTIFACTS = BASE / "artifacts"
INDEX = SESSIONS / ".index.json"


def session_dir(sid: str) -> Path:
    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", sid)[:48] or "unknown"
    idx = json.loads(INDEX.read_text(encoding="utf-8")) if INDEX.exists() else {}
    if safe not in idx:
        n = datetime.now()
        idx[safe] = f"{n:%Y}/{n:%d-%m}/{n:%H-%M-%S}_{safe}"
        INDEX.parent.mkdir(parents=True, exist_ok=True)
        INDEX.write_text(json.dumps(idx, indent=1, sort_keys=True), encoding="utf-8")
    d = SESSIONS / idx[safe]
    d.mkdir(parents=True, exist_ok=True)
    return d
