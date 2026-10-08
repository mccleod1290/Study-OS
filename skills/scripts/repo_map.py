#!/usr/bin/env python3
"""Regenerate REPO_MAP.md: where every skill, script, rule and artifact lives.
python skills/scripts/repo_map.py            write REPO_MAP.md
python skills/scripts/repo_map.py --check    exit 1 if REPO_MAP.md is stale
Deterministic: sorted, no clock. Run after adding, moving or renaming a skill or script."""
from __future__ import annotations
import ast, re, sys
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / ".rules").is_dir())
SKIPDIR = {".git", "sessions", "user-input-learning-text", "__pycache__", "node_modules"}


def noise(name: str) -> bool:
    return name.endswith(":Zone.Identifier")


def rel(p):
    return p.relative_to(ROOT).as_posix()


def walk(base, pattern):
    out = []
    for p in sorted(base.rglob(pattern)):
        if noise(p.name):
            continue
        if not any(x in SKIPDIR for x in p.relative_to(ROOT).parts) and "Artifacts" not in p.relative_to(ROOT).parts[:1]:
            out.append(p)
    return out


def front(p):
    t = p.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"---\s*\n(.*?)\n---", t, re.S)
    name, desc = p.parent.name, ""
    if m:
        fm = m.group(1).splitlines()
        for i, l in enumerate(fm):
            if l.startswith("name:"):
                name = l.split(":", 1)[1].strip()
            if l.startswith("description:"):
                rest = l.split(":", 1)[1].strip()
                if rest in (">", ">-", "|", "|-", ""):
                    parts = []
                    for l2 in fm[i + 1:]:
                        if l2.startswith((" ", "\t")):
                            parts.append(l2.strip())
                        else:
                            break
                    rest = " ".join(parts)
                desc = " ".join(rest.split()).strip(">").strip()
    first = ""
    for s in re.split(r"(?<=[.])\s", desc):
        first = (first + " " + s).strip()
        if len(first) >= 90:
            break
    return name, (first[:200] + "..." if len(first) > 200 else first).replace("|", "/")


def doc1(p):
    m = re.search(r'^(?:#!.*\n)?\s*(?:"""|\'\'\')\s*(.+)', p.read_text(encoding="utf-8"), re.M)
    return m.group(1).replace('"""', "").strip().replace("|", "/") if m else ""


def build():
    L = ["# REPO MAP", "",
         "Read this first. It says where everything is. Regenerate with `python skills/scripts/repo_map.py`. Do not edit by hand.", "",
         "## Rules of the house", "",
         "- Rules: `.rules/`. Read `.rules/artifacts-and-sessions.md` before writing any file.",
         "- All AI output goes under `Artifacts/`. Deliverables are HTML. Topic folders have no dates in names.",
         "- Skills live under `skills/`. Scripts live under `skills/scripts/`. Hooks config is `.github/hooks/study-os.json`.",
         "- Source case documents (his input, private) are in `user-input-learning-text/`. Read only. Never move or edit.", ""]
    L += ["## Skills", "", "| skill | path | what it does |", "|---|---|---|"]
    sk = [p for p in walk(ROOT / "skills", "SKILL.md")] + walk(ROOT / ".github", "SKILL.md")
    for p in sorted(sk, key=lambda q: rel(q)):
        n, d = front(p)
        L.append(f"| `{n}` | `{rel(p)}` | {d} |")
    L += ["", "## Workflows", "", "- `WORKFLOW_STUDY.md`: the four phase study, for one learner and one topic.", "- `WORKFLOW_EXPERT_CAPTURE.md`: learn from experts through their consented session logs, then make a study topic.", ""]
    L += ["## Documentation", "", "- `Documentation/study_os_guide.html`: how to use, extend and understand the harness. Not a study deliverable. Hand-written, kept outside `Artifacts/`.", ""]
    L += ["", "## Skill groups", ""]
    for g in sorted((ROOT / "skills").iterdir()):
        if g.is_dir():
            subs = sorted(q.name for q in (g / "skills").iterdir() if q.is_dir()) if (g / "skills").is_dir() else sorted(q.name for q in g.iterdir() if q.is_dir() and (q / "SKILL.md").exists())
            top = sorted(q.name for q in g.iterdir() if q.is_file() and not noise(q.name))
            L.append(f"- `{rel(g)}/`" + (f" skills: {', '.join(subs)}" if subs else "") + (f". files: {', '.join(top)}" if top else ""))
    L += ["", "## Scripts", "", "| script | path | what it does |", "|---|---|---|"]
    for p in walk(ROOT / "skills" / "scripts", "*.py"):
        L.append(f"| `{p.name}` | `{rel(p)}` | {doc1(p)} |")
    for p in walk(ROOT / "skills" / "scripts", "*.html"):
        L.append(f"| `{p.name}` | `{rel(p)}` | template |")
    L += ["", "## Hooks and rules", ""]
    for p in sorted((ROOT / ".github" / "hooks").glob("*.json")):
        L.append(f"- hooks config `{rel(p)}`")
    for p in sorted((ROOT / ".rules").glob("*")):
        if noise(p.name):
            continue
        L.append(f"- rule `{rel(p)}`")
    L += ["", "## Where deliverables are", ""]
    art = ROOT / "Artifacts" / "artifacts"
    if art.exists():
        for g in sorted(art.iterdir()):
            if g.is_dir():
                kids = sorted(q.name for q in g.iterdir() if q.is_dir())
                L.append(f"- `Artifacts/artifacts/{g.name}/`" + (f" group of: {', '.join(kids)}" if kids else ""))
    L += ["- session logs: `Artifacts/sessions/<YYYY>/<DD-MM>/<HH-MM-SS>_<id>/`", ""]
    L += ["## Common jobs", "",
          "| I want to | do this |", "|---|---|",
          "| build or check a mind map | `python skills/scripts/build_mindmap.py <topic_slug>` |",
          "| tidy the folder | `/tidy` or `python skills/scripts/tidy.py` |",
          "| review how he uses the AI | `skills/misc/learn_from_sessions`, then `python skills/scripts/learn_due.py` |",
          "| turn markdown into HTML or PDF | `python skills/scripts/md_to_pdf.py` |",
          "| refresh this map | `python skills/scripts/repo_map.py` |", ""]
    return "\n".join(L)


def main():
    text = build()
    out = ROOT / "REPO_MAP.md"
    if "--check" in sys.argv:
        ok = out.exists() and out.read_text(encoding="utf-8") == text
        print("OK" if ok else "STALE")
        return 0 if ok else 1
    out.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
