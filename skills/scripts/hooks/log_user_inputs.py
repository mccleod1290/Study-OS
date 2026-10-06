#!/usr/bin/env python3
"""Hook: log every user input, verbatim, in one place.
Event: userPromptSubmitted (JSON on stdin).
Writes logs/inputs/INPUTS.md (all sessions) and logs/inputs/<session>.jsonl.
Only redacts credentials. Never blocks the agent: exit code is always 0."""
from __future__ import annotations
import json, re, sys
from datetime import datetime
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import session_dir

ROOT = next(p for p in Path(__file__).resolve().parents if (p / ".rules").is_dir())
OUT = ROOT / "Artifacts" / "sessions"
SECRET = re.compile(r"(?i)(AKIA[0-9A-Z]{16}|ASIA[0-9A-Z]{16}|(secret|token|password|passwd|api[_-]?key|authorization|session[_-]?token)[\"'\s:=]+[^\s\"',}]{6,})")


def main() -> int:
    try:
        raw = sys.stdin.read()
        p = json.loads(raw) if raw.strip() else {}
        p = p if isinstance(p, dict) else {}
        text = str(p.get("prompt") or p.get("user_prompt") or "")
        sid = str(p.get("sessionId") or p.get("session_id") or "unknown")
        if not text.strip():
            return 0
        text = SECRET.sub(lambda m: (m.group(2) or "key") + "=[REDACTED]", text)
        ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        d = session_dir(sid)
        md = d / "inputs.md"
        n = 1
        if md.exists():
            n = md.read_text(encoding="utf-8").count("\n## ") + 1
        with md.open("a", encoding="utf-8") as f:
            if n == 1:
                f.write("# User inputs\n\nVerbatim. One entry per prompt, oldest first.\n")
            f.write(f"\n## #{n} {ts} [{sid}]\n\n{text}\n")
        with (d / "inputs.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps({"n": n, "t": ts, "chars": len(text), "text": text}, ensure_ascii=False) + "\n")
    except Exception as exc:
        try:
            OUT.mkdir(parents=True, exist_ok=True)
            with (OUT / "hook_errors.log").open("a", encoding="utf-8") as f:
                f.write(f"{datetime.now().isoformat()} {exc!r}\n")
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
