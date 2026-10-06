#!/usr/bin/env python3
"""Tidy the Study OS folder per .rules/artifacts-and-sessions.md.
  python skills/scripts/tidy.py            plan only, nothing moves
  python skills/scripts/tidy.py --apply    move files, write a manifest
  python skills/scripts/tidy.py --undo     reverse the last applied run
Never touches: scripts, skills, rules, hooks, phase docs, source case documents, Artifacts/sessions logs.
Moves:
  phase_N/output/<slug>/<file>  -> Artifacts/artifacts/<slug>/phaseN_<lowercase file name>
  loose root files (not index.html) -> Artifacts/artifacts/_unsorted/
  root index.html               -> Artifacts/index.html (links rewritten)
  related topics            -> Artifacts/artifacts/<group>/<topic>/ , groups listed in Artifacts/artifacts/_groups.json
  files in logs/ tools/ model/  -> Artifacts/sessions/_legacy/<dir>/
Same input, same plan. Existing targets are never overwritten: the file is reported as a conflict and skipped."""
from __future__ import annotations
import json, re, shutil, sys
from datetime import datetime
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / ".rules").is_dir())
ART = ROOT / "Artifacts" / "artifacts"
MAN = ROOT / "Artifacts" / "sessions" / ".tidy"
SKIP_EXT = {".pyc"}
KEEP = {"index.html", "REPO_MAP.md", "AGENTS.md", "README.md", "WORKFLOW_STUDY.md", "WORKFLOW_EXPERT_CAPTURE.md"}
GROUPS = ART / "_groups.json"


def groups():
    """topic slug -> group folder, from Artifacts/artifacts/_groups.json {group: [topic, ...]}."""
    if not GROUPS.exists():
        return {}
    g = json.loads(GROUPS.read_text(encoding="utf-8-sig"))
    return {t: grp for grp, ts in sorted(g.items()) for t in ts}


def home(topic):
    grp = groups().get(topic)
    return ART / grp / topic if grp else ART / topic


def plan():
    mv = []
    for ph in sorted(ROOT.glob("skills/phase_[0-9]/output")):
        n = ph.parent.name.split("_")[1]
        for slug in sorted(p for p in ph.iterdir() if p.is_dir()):
            for f in sorted(slug.rglob("*")):
                if f.is_file() and f.suffix not in SKIP_EXT:
                    rel = f.relative_to(slug)
                    name = "_".join(rel.parts[:-1] + (rel.name.lower(),))
                    mv.append((f, home(slug.name) / f"phase{n}_{name}"))
    for topic, grp in sorted(groups().items()):
        old = ART / topic
        if old.is_dir():
            for f in sorted(old.rglob("*")):
                if f.is_file():
                    mv.append((f, ART / grp / topic / f.relative_to(old)))
    for f in sorted(ROOT.iterdir()):
        if f.is_file() and f.name not in KEEP and f.suffix.lower() in {".html", ".pdf", ".md", ".json", ".png", ".txt"}:
            mv.append((f, ART / "_unsorted" / f.name))
    for d in ("logs", "tools", "model"):
        base = ROOT / d
        if base.is_dir():
            for f in sorted(base.rglob("*")):
                if f.is_file():
                    mv.append((f, ROOT / "Artifacts" / "sessions" / "_legacy" / d / f.relative_to(base)))
    return mv


def link_map(mv):
    return {src.relative_to(ROOT).as_posix(): "artifacts/" + dst.relative_to(ART).as_posix() for src, dst in mv}


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "--undo":
        files = sorted(MAN.glob("*.json")) if MAN.exists() else []
        if not files:
            print("nothing to undo"); return 0
        m = json.loads(files[-1].read_text(encoding="utf-8"))
        for s, d in reversed(m["moves"]):
            s, d = ROOT / s, ROOT / d
            if d.exists() and not s.exists():
                s.parent.mkdir(parents=True, exist_ok=True); shutil.move(str(d), str(s))
        if m.get("index_before") is not None:
            (ROOT / "index.html").write_text(m["index_before"], encoding="utf-8")
            (ROOT / "Artifacts" / "index.html").unlink(missing_ok=True)
        files[-1].rename(files[-1].with_suffix(".undone")); print("undone", files[-1].name); return 0
    apply = arg == "--apply"
    mv = plan()
    moves, conflicts = [], []
    for s, d in mv:
        (conflicts if d.exists() else moves).append((s, d))
    for s, d in moves:
        print(("MOVE     " if apply else "would move ") + f"{s.relative_to(ROOT).as_posix()}  ->  {d.relative_to(ROOT).as_posix()}")
    for s, d in conflicts:
        print(f"CONFLICT {s.relative_to(ROOT).as_posix()} -> {d.relative_to(ROOT).as_posix()} exists, skipped")
    idx = ROOT / "index.html"
    before = idx.read_text(encoding="utf-8") if idx.exists() else None
    if not apply:
        print(f"\nplan: {len(moves)} moves, {len(conflicts)} conflicts. add --apply to run."); return 0
    lm = link_map(mv)
    for s, d in moves:
        d.parent.mkdir(parents=True, exist_ok=True); shutil.move(str(s), str(d))
    ai = ROOT / "Artifacts" / "index.html"
    if ai.exists() and before is None:
        txt = ai.read_text(encoding="utf-8")
        for k in sorted(lm, key=len, reverse=True):
            if k.startswith("Artifacts/"):
                txt = txt.replace(k[len("Artifacts/"):], lm[k])
        ai.write_text(txt, encoding="utf-8")
    if before is not None:
        txt = before
        for k in sorted(lm, key=len, reverse=True):
            txt = txt.replace(k, lm[k])
        (ROOT / "Artifacts").mkdir(exist_ok=True)
        (ROOT / "Artifacts" / "index.html").write_text(txt, encoding="utf-8"); idx.unlink()
    for ph in sorted(ROOT.glob("skills/phase_[0-9]/output")):
        for slug in sorted((p for p in ph.iterdir() if p.is_dir()), reverse=True):
            for sub in sorted((p for p in slug.rglob("*") if p.is_dir()), reverse=True):
                try: sub.rmdir()
                except OSError: pass
            try: slug.rmdir()
            except OSError: pass
    for topic in sorted(groups()):
        old = ART / topic
        if old.is_dir():
            for sub_ in sorted((p for p in old.rglob("*") if p.is_dir()), reverse=True):
                try: sub_.rmdir()
                except OSError: pass
            try: old.rmdir()
            except OSError: pass
    MAN.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    (MAN / f"{stamp}.json").write_text(json.dumps({
        "at": stamp, "index_before": before,
        "moves": [[s.relative_to(ROOT).as_posix(), d.relative_to(ROOT).as_posix()] for s, d in moves]}, indent=1), encoding="utf-8")
    print(f"\nmoved {len(moves)}, conflicts {len(conflicts)}. manifest Artifacts/sessions/.tidy/{stamp}.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
