#!/usr/bin/env python3
"""Study OS harness hook. Usage: study_os_hook.py <event>  (JSON payload on stdin).

Writes the ledger the phase 4 skills read:
  logs/sessions/LATEST.md, INDEX.md, <id>/meta.json
  tools/ACTIONS.md      tool trail   (heading = local ISO time)
  model/DECISIONS.md    his prompts  (heading = local ISO time)
  logs/agent-activity/  raw event lines, one file per session
Never blocks the agent: every error is swallowed, exit code is always 0.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import session_dir

ROOT = next(p for p in Path(__file__).resolve().parents if (p / ".rules").is_dir())
SESSIONS = ROOT / "Artifacts" / "sessions"
ACTIVITY = ROOT / "logs" / "agent-activity"
ACTIONS = ROOT / "tools" / "ACTIONS.md"
DECISIONS = ROOT / "model" / "DECISIONS.md"

SECRET = re.compile(
    r"(?i)(AKIA[0-9A-Z]{16}|ASIA[0-9A-Z]{16}|"
    r"(secret|token|password|passwd|api[_-]?key|authorization|session[_-]?token)"
    r"[\"'\s:=]+[^\s\"',}]{6,})"
)


def now() -> str:
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


def redact(text: str) -> str:
    return SECRET.sub(lambda m: (m.group(2) or "key") + "=[REDACTED]", text)


def short(value, limit=300) -> str:
    text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)
    text = redact(" ".join(text.split()))
    return text if len(text) <= limit else text[:limit] + "..."


def pick(payload: dict, *keys, default=""):
    for k in keys:
        if payload.get(k) not in (None, ""):
            return payload[k]
    return default


def append(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(text)


def session_id(payload: dict, event: str) -> str:
    sid = str(pick(payload, "sessionId", "session_id"))
    current = SESSIONS / ".current"
    if sid:
        return sid
    if event == "sessionstart" or not current.exists():
        sid = "session-" + datetime.now().strftime("%Y%m%d-%H%M%S")
        current.parent.mkdir(parents=True, exist_ok=True)
        current.write_text(sid, encoding="utf-8")
        return sid
    return current.read_text(encoding="utf-8").strip()


def read_meta(sid: str) -> dict:
    p = session_dir(sid) / "meta.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except ValueError:
            pass
    return {"id": sid, "started": now(), "prompts": 0, "actions": 0, "last_prompt_key": ""}


def write_meta(meta: dict) -> None:
    p = session_dir(meta["id"]) / "meta.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    (SESSIONS / "LATEST.md").write_text(
        f"# Latest session\n\nid: {meta['id']}\nstarted: {meta['started']}\n"
        f"last_event: {meta.get('last_event', '')}\n"
        f"prompts: {meta['prompts']}\nactions: {meta['actions']}\n"
        f"last_prompt_key: {meta['last_prompt_key']}\n"
        f"meta: {session_dir(meta['id']).relative_to(ROOT).as_posix()}/meta.json\n",
        encoding="utf-8",
    )


def index_line(meta: dict) -> None:
    idx = SESSIONS / "INDEX.md"
    if not idx.exists() or f"`{meta['id']}`" not in idx.read_text(encoding="utf-8"):
        append(idx, f"- {meta['started']} `{meta['id']}`\n" if idx.exists()
               else f"# Sessions\n\n- {meta['started']} `{meta['id']}`\n")


def main() -> int:
    event = (sys.argv[1] if len(sys.argv) > 1 else "unknown")
    ev = event.lower()
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
        if not isinstance(payload, dict):
            payload = {}
    except ValueError:
        payload = {}
    try:
        sid = session_id(payload, ev)
        meta = read_meta(sid)
        sd = session_dir(sid)
        ts = now()
        meta["last_event"] = f"{event} {ts}"

        if ev == "sessionstart":
            index_line(meta)
            first = pick(payload, "initialPrompt", "initial_prompt")
            if first:
                append(sd / 'prompts.md', f"\n## {ts} (session start)\n\n{redact(str(first))}\n")
        elif ev in ("userpromptsubmitted", "userpromptsubmit"):
            prompt = str(pick(payload, "prompt", "user_prompt"))
            meta["prompts"] += 1
            meta["last_prompt_key"] = f"{ts} p{meta['prompts']}"
            append(sd / 'prompts.md', f"\n## {ts} [{sid}] p{meta['prompts']}\n\n{redact(prompt)}\n")
        elif ev == "posttooluse":
            name = pick(payload, "toolName", "tool_name", default="?")
            args = pick(payload, "toolArgs", "tool_input", "tool_args", default="")
            result = payload.get("toolResult") or payload.get("tool_response") or {}
            status = result.get("resultType", "") if isinstance(result, dict) else ""
            meta["actions"] += 1
            append(sd / 'actions.md', f"\n## {ts} [{sid}] {name} {status}\n\n`{short(args)}`\n")
        elif ev == "errorOccurred".lower():
            err = pick(payload, "error", default=payload)
            append(sd / 'actions.md', f"\n## {ts} [{sid}] ERROR\n\n`{short(err)}`\n")
        elif ev == "sessionend":
            meta["ended"] = ts
            meta["end_reason"] = str(pick(payload, "reason", default=""))

        append(sd / "events.jsonl",
               json.dumps({"t": ts, "event": event, "keys": sorted(payload)}) + "\n")
        write_meta(meta)
    except Exception as exc:  # hooks must never break the agent
        try:
            append(ACTIVITY / "hook_errors.log", f"{now()} {event} {exc!r}\n")
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

