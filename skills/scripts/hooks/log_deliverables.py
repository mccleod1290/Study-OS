#!/usr/bin/env python3
"""Hook: log each deliverable delivered per run (a run = one session).
Events: postToolUse, sessionEnd (JSON on stdin).
Tool-agnostic: it diffs deliverable files on disk against a manifest, so files made by
create/edit/python/powershell are all caught.
Deliverable = .html .pdf .md .json under Artifacts/artifacts/ and legacy phase_*/output/, plus root index.html.
Writes deliverables.md inside the session folder.
Never blocks the agent: exit code is always 0."""
from __future__ import annotations
import hashlib, json, sys
from datetime import datetime
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import session_dir, ARTIFACTS

ROOT = next(p for p in Path(__file__).resolve().parents if (p / ".rules").is_dir())
OUT = ROOT / "Artifacts" / "sessions"
MANIFEST = OUT / ".deliverables_manifest.json"
EXT = {".html", ".pdf", ".md", ".json"}


def candidates():
    for base in sorted(ROOT.glob("skills/phase_*/output")):
        for p in sorted(base.rglob("*")):
            if p.is_file() and p.suffix.lower() in EXT:
                yield p
    if ARTIFACTS.exists():
        for q in sorted(ARTIFACTS.rglob("*")):
            if q.is_file() and q.suffix.lower() in EXT and q.name not in ("HISTORY.md", "_groups.json"):
                yield q
    idx = ROOT / "index.html"
    if idx.exists():
        yield idx


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def main() -> int:
    try:
        raw = sys.stdin.read()
        p = json.loads(raw) if raw.strip() else {}
        p = p if isinstance(p, dict) else {}
        event = sys.argv[1] if len(sys.argv) > 1 else "unknown"
        sid = str(p.get("sessionId") or p.get("session_id") or "unknown")
        OUT.mkdir(parents=True, exist_ok=True)
        old = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
        new, lines = dict(old), []
        for f in candidates():
            rel = f.relative_to(ROOT).as_posix()
            h = sha(f)
            if old.get(rel) != h:
                kind = "new" if rel not in old else "updated"
                lines.append(f"- {kind} `{rel}` {f.stat().st_size} bytes sha {h}")
                new[rel] = h
                top = Path(rel).parts
                gf = ARTIFACTS / "_groups.json"
                grp = json.loads(gf.read_text(encoding="utf-8-sig")) if gf.exists() else {}
                if top[:2] == ("Artifacts", "artifacts") and len(top) > 3:
                    if top[2] in grp and len(top) > 4:
                        top = top[:2] + (top[2] + "/" + top[3],) + top[4:]
                    hist = ROOT / "Artifacts" / "artifacts" / top[2] / "HISTORY.md"
                    with hist.open("a", encoding="utf-8") as hf:
                        if hist.stat().st_size == 0:
                            hf.write(f"# {top[2]} history\n\nOne line per change. Time is inside the log, never in a file name.\n\n")
                        hf.write(f"- {datetime.now():%Y-%m-%dT%H:%M:%S} {kind} `{Path(*top[3:]).as_posix()}` run {sid}\n")
        if lines:
            ts = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            md = session_dir(sid) / "deliverables.md"
            with md.open("a", encoding="utf-8") as fh:
                if not md.exists() or md.stat().st_size == 0:
                    fh.write("# Deliverables per run\n\nOne block per change. run = session id.\n")
                fh.write(f"\n## {ts} run [{sid}] ({event})\n\n" + "\n".join(lines) + "\n")
            MANIFEST.write_text(json.dumps(new, indent=1, sort_keys=True), encoding="utf-8")
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
