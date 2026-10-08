#!/usr/bin/env python3
"""Write `best highlights.txt` inside a session folder. The name does not change.

First prompt of a new session: the previous session folder.
Session end: the session that just ended.

Reads Study OS session files under Artifacts/sessions/, and the workspace
logs/sessions/ trail when that folder is present. Never blocks the agent.
"""
from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import ARTIFACTS, SESSIONS

ROOT = next(p for p in Path(__file__).resolve().parents if (p / ".rules").is_dir())
FILE_NAME = "best highlights.txt"
SECRET = re.compile(
    r"(?i)(AKIA[0-9A-Z]{16}|ASIA[0-9A-Z]{16}|"
    r"(secret|token|password|passwd|api[_-]?key|authorization|session[_-]?token)"
    r"[\"'\s:=]+[^\s\"',}]{6,})"
)
SHELL = {"bash", "powershell", "shell", "run_terminal_command"}
WRITE = {"write", "edit", "notebookedit", "multiedit", "search_replace"}


def redact(text: str) -> str:
    return SECRET.sub(lambda m: (m.group(2) or "key") + "=[REDACTED]", text)


def one_line(text: str, limit: int = 220) -> str:
    s = redact(re.sub(r"\s+", " ", str(text or "")).strip())
    if len(s) <= limit:
        return s
    cut = s[:limit]
    sp = cut.rfind(" ")
    if sp > 40:
        cut = cut[:sp]
    return cut + "..."


def first_paragraph(text: str) -> str:
    clean = redact(str(text or "").replace("\r\n", "\n").strip())
    para = next((p.strip() for p in re.split(r"\n\s*\n", clean) if p.strip()), "")
    return one_line(re.sub(r"\s+", " ", para), 500)


def now() -> str:
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


def read_jsonl(path: Path) -> list:
    if not path.is_file():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except ValueError:
            continue
        if isinstance(row, dict):
            rows.append(row)
    return rows


def load_meta(folder: Path) -> dict:
    p = folder / "meta.json"
    if not p.is_file():
        return {}
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except ValueError:
        return {}
    return data if isinstance(data, dict) else {}


def short_id(sid: str) -> str:
    return re.sub(r"[^A-Za-z0-9]", "", sid or "")[:8]


def workspaces() -> list[Path]:
    found = []
    for key in ("GROK_WORKSPACE_ROOT", "CLAUDE_PROJECT_DIR"):
        raw = os.environ.get(key, "").strip()
        if raw:
            found.append(Path(raw))
    found.append(ROOT)
    found.append(ROOT.parent)
    out = []
    seen = set()
    for p in found:
        try:
            key = str(p.resolve())
        except OSError:
            continue
        if key in seen or not p.is_dir():
            continue
        seen.add(key)
        out.append(p)
    return out


def session_folders() -> list[tuple[Path, dict]]:
    found = []
    seen = set()

    def add(folder: Path) -> None:
        try:
            key = str(folder.resolve())
        except OSError:
            return
        if key in seen or not folder.is_dir():
            return
        if ".tidy" in folder.parts:
            return
        meta = load_meta(folder)
        has_trail = (folder / "tools" / "tools.jsonl").is_file() or (folder / "inputs.md").is_file() or (folder / "prompts.md").is_file() or (folder / "actions.md").is_file()
        if not meta and not has_trail:
            return
        seen.add(key)
        found.append((folder, meta))

    if SESSIONS.is_dir():
        for meta_path in SESSIONS.rglob("meta.json"):
            add(meta_path.parent)
        for name in ("inputs.md", "prompts.md", "actions.md"):
            for p in SESSIONS.rglob(name):
                add(p.parent)
    for ws in workspaces():
        base = ws / "logs" / "sessions"
        if not base.is_dir():
            continue
        for child in base.iterdir():
            if child.name.startswith("."):
                continue
            add(child)
    return found


def belongs(folder: Path, meta: dict, sid: str) -> bool:
    if not sid:
        return False
    short = short_id(sid)
    blob = " ".join([
        folder.name,
        str(meta.get("id") or ""),
        str(meta.get("sid") or ""),
        str(meta.get("short") or ""),
        str(meta.get("dir") or ""),
    ])
    return sid in blob or (short and short in blob)


def stamp(folder: Path, meta: dict) -> str:
    started = str(meta.get("started") or "")
    try:
        mtime = (folder / "meta.json").stat().st_mtime
    except OSError:
        try:
            mtime = folder.stat().st_mtime
        except OSError:
            mtime = 0
    return f"{started}|{mtime:016.3f}"


def previous_session(sid: str):
    rows = [(f, m) for f, m in session_folders() if not belongs(f, m, sid)]
    rows.sort(key=lambda item: stamp(*item))
    return rows[-1] if rows else None


def self_session(sid: str):
    rows = [(f, m) for f, m in session_folders() if belongs(f, m, sid)]
    rows.sort(key=lambda item: stamp(*item))
    return rows[-1] if rows else None


def uniq(items: list[str]) -> list[str]:
    out = []
    seen = set()
    for item in items:
        key = item.lower()
        if not item or key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def collect_ledger(folder: Path) -> dict:
    tools = read_jsonl(folder / "tools" / "tools.jsonl")
    decisions = read_jsonl(folder / "model" / "decisions.jsonl")
    prompts, failures, writes, shells, bullets = [], [], [], [], []
    final = ""
    for rec in tools:
        if rec.get("event") == "UserPromptSubmit" and rec.get("prompt"):
            prompts.append(one_line(rec["prompt"], 300))
        if rec.get("event") == "PostToolUseFailure":
            failures.append(one_line(f"{rec.get('tool') or 'tool'} failed: {rec.get('error') or 'no error text'}"))
        if rec.get("event") == "PermissionDenied":
            failures.append(one_line(f"denied {rec.get('tool') or 'tool'}: {rec.get('reason') or ''}"))
        if rec.get("event") == "PostToolUse":
            result = str(rec.get("result") or "")
            if result.startswith("ERROR"):
                failures.append(one_line(f"{rec.get('tool') or 'tool'}: {result}"))
            changed = rec.get("file_changed")
            if changed and str(rec.get("tool") or "").lower() in WRITE:
                writes.append(str(changed))
        if rec.get("event") == "PreToolUse" and str(rec.get("tool") or "").lower() in SHELL:
            desc = (rec.get("input") or {}).get("description") or ""
            if desc:
                shells.append(one_line(desc, 180))
    for rec in decisions:
        if rec.get("decision_kind") == "USER_GOAL" and rec.get("prompt"):
            prompts.append(one_line(rec["prompt"], 300))
        kind = str(rec.get("decision_kind") or "")
        if (kind == "FINAL" or kind.startswith("STOP")) and rec.get("last_assistant_message"):
            final = str(rec["last_assistant_message"])
    if final:
        for line in final.splitlines():
            t = line.strip()
            if t.startswith("- "):
                bullets.append(one_line(t[2:], 300))
    return {
        "prompts": uniq(prompts),
        "failures": uniq(failures),
        "writes": uniq(writes),
        "shells": uniq(shells),
        "bullets": uniq(bullets),
        "final": final,
        "deliverables": [],
    }


def md_blocks(path: Path) -> list[str]:
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8", errors="replace")
    parts = re.split(r"\n## ", text)
    bodies = []
    for part in parts[1:]:
        body = part.split("\n", 1)[1] if "\n" in part else ""
        body = body.strip()
        if body:
            bodies.append(body)
    return bodies


def collect_study(folder: Path) -> dict:
    prompts = []
    for row in read_jsonl(folder / "inputs.jsonl"):
        if row.get("text"):
            prompts.append(one_line(row["text"], 300))
    if not prompts:
        for body in md_blocks(folder / "prompts.md") + md_blocks(folder / "inputs.md"):
            prompts.append(one_line(body, 300))
    failures = []
    for body in md_blocks(folder / "actions.md"):
        if "ERROR" in body[:80]:
            failures.append(one_line(body, 300))
    deliverables = []
    dfile = folder / "deliverables.md"
    if dfile.is_file():
        for line in dfile.read_text(encoding="utf-8", errors="replace").splitlines():
            if "`" in line and line.strip().startswith("-"):
                deliverables.append(one_line(line.strip().lstrip("- ").strip(), 300))
    return {
        "prompts": uniq(prompts),
        "failures": uniq(failures),
        "writes": [],
        "shells": [],
        "bullets": [],
        "final": "",
        "deliverables": uniq(deliverables),
    }


def collect(folder: Path) -> dict:
    if (folder / "tools" / "tools.jsonl").is_file() or (folder / "model" / "decisions.jsonl").is_file():
        bag = collect_ledger(folder)
        if bag["prompts"] or bag["final"] or bag["writes"] or bag["failures"]:
            return bag
    return collect_study(folder)


def artifact_lines(meta: dict, sid_hint: str) -> list[str]:
    if not ARTIFACTS.is_dir():
        return []
    needle = sid_hint or str(meta.get("id") or meta.get("short") or "")
    if not needle:
        return []
    lines = []
    for hist in ARTIFACTS.rglob("HISTORY.md"):
        try:
            text = hist.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for line in text.splitlines():
            if needle[:8] and needle[:8] in line:
                lines.append(one_line(line.lstrip("- ").strip(), 300))
    return uniq(lines)


def build_also(bag: dict, best: str, artifacts: list[str]) -> list[str]:
    best_key = best.lower()
    rows = []
    seen = set()

    def push(line: str) -> None:
        text = one_line(line, 300)
        if not text:
            return
        key = text.lower()
        if key in seen or key == best_key:
            return
        seen.add(key)
        rows.append(text)

    for p in bag["prompts"]:
        push(f"Prompt: {p}")
    for f in bag["failures"]:
        push(f)
    for b in bag["bullets"]:
        push(b)
    for w in bag["writes"]:
        if "/logs/" in w.replace("\\", "/"):
            continue
        push(f"Wrote {w}")
    for d in bag["deliverables"]:
        push(f"Deliverable {d}")
    for a in artifacts:
        push(f"Deliverable {a}")
    if len(rows) < 3:
        for sh in bag["shells"]:
            if len(rows) >= 7:
                break
            push(sh)
    return rows[:7]


def render(folder: Path, meta: dict, bag: dict, artifacts: list[str]) -> str:
    title = str(meta.get("title") or folder.name)
    best = first_paragraph(bag["final"])
    if not best and bag["deliverables"]:
        best = bag["deliverables"][-1]
    if not best and bag["writes"]:
        best = f"Wrote {bag['writes'][-1]}"
    if not best and artifacts:
        best = artifacts[-1]
    if not best and bag["prompts"]:
        best = bag["prompts"][-1]
    if not best:
        best = "No prompt and no closing text in this session."
    also = build_also(bag, best, artifacts)
    lines = [
        "best highlights",
        f"session: {meta.get('dir') or folder.name}",
        f"title: {one_line(title, 200)}",
        f"started: {meta.get('started') or ''}",
        f"workspace: {meta.get('cwd') or ''}",
        "",
        "best",
        best,
        "",
        "also",
    ]
    if not also:
        lines.append("1. No other beats on disk.")
    else:
        lines.extend(f"{i}. {row}" for i, row in enumerate(also, 1))
    lines.append("")
    return "\n".join(lines)


def write_highlights(folder: Path, meta: dict, sid_hint: str = "") -> None:
    bag = collect(folder)
    artifacts = artifact_lines(meta, sid_hint or str(meta.get("sid") or meta.get("id") or ""))
    text = render(folder, meta, bag, artifacts)
    (folder / FILE_NAME).write_text(text, encoding="utf-8")


def event_name(payload: dict) -> str:
    if len(sys.argv) > 1 and sys.argv[1].strip():
        raw = sys.argv[1]
    else:
        raw = str(payload.get("hook_event_name") or payload.get("hookEventName") or os.environ.get("GROK_HOOK_EVENT") or "")
    return re.sub(r"[\s_-]", "", raw).lower()


def is_child(payload: dict) -> bool:
    for key in ("subagentType", "subagent_type", "agentType", "agent_type"):
        val = payload.get(key)
        if isinstance(val, str) and val.strip() and val.strip() != "main":
            return True
    return False


def marker(sid: str) -> Path:
    return SESSIONS / f".highlights_done_{short_id(sid) or 'unknown'}"


def note_error(exc: BaseException) -> None:
    try:
        SESSIONS.mkdir(parents=True, exist_ok=True)
        with (SESSIONS / "hook_errors.log").open("a", encoding="utf-8") as fh:
            fh.write(f"{now()} best_highlights {exc!r}\n")
    except OSError:
        pass


def main() -> int:
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
        if not isinstance(payload, dict):
            payload = {}
    except ValueError:
        payload = {}
    try:
        if is_child(payload):
            return 0
        event = event_name(payload)
        sid = str(payload.get("sessionId") or payload.get("session_id") or os.environ.get("GROK_SESSION_ID") or "")
        if event == "sessionend":
            found = self_session(sid)
            if found:
                write_highlights(found[0], found[1], sid)
            return 0
        if event not in ("userpromptsubmit", "userpromptsubmitted"):
            return 0
        flag = marker(sid)
        if flag.exists():
            return 0
        prev = previous_session(sid)
        if prev:
            write_highlights(prev[0], prev[1], sid)
        flag.parent.mkdir(parents=True, exist_ok=True)
        flag.write_text(f"{prev[0] if prev else ''}\n", encoding="utf-8")
    except Exception as exc:
        note_error(exc)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
