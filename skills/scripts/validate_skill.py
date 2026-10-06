"""validate_skill.py: check a SKILL.md against .rules/skill-authoring.md. Usage: validate_skill.py <skill_dir|SKILL.md> [...]. Exit 1 on any error."""
import re, sys
from pathlib import Path

SPEC = {"name","description","license","compatibility","metadata","allowed-tools"}
CC = {"when_to_use","argument-hint","arguments","disable-model-invocation","user-invocable","disallowed-tools","model","effort","context","agent","background","hooks","paths","shell"}
EFFORT = {"low","medium","high","xhigh","max"}

def parse(fm):
    out, key, mode, buf = {}, None, None, []
    def flush():
        if key is not None:
            out[key] = (" ".join(x.strip() for x in buf if x.strip())) if mode else buf[0] if buf else ""
    for line in fm.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m and not line.startswith(" "):
            flush(); key = m.group(1); v = m.group(2).strip()
            mode = v in (">-", ">", "|", "|-")
            buf = [] if mode else [v]
            out["__style__" + key] = v if mode else "plain"
        elif key is not None:
            buf.append(line)
    flush()
    return out

def check(p):
    p = Path(p); f = p / "SKILL.md" if p.is_dir() else p
    errs, warns = [], []
    t = f.read_text(encoding="utf-8-sig")
    if not t.startswith("---"):
        return ["first line must be ---"], []
    m = re.match(r"^---\r?\n(.*?)\r?\n---", t, re.S)
    if not m: return ["front matter is not closed with ---"], []
    d = parse(m.group(1)); body_lines = len(t.splitlines())
    name = d.get("name", "")
    if not name: errs.append("name missing")
    elif not re.fullmatch(r"[a-z][a-z0-9_]*", name): errs.append(f"name '{name}' must be snake_case")
    elif name != f.parent.name: errs.append(f"name '{name}' must equal folder '{f.parent.name}'")
    desc = d.get("description", "")
    if d.get("__style__description") != ">-": errs.append("description must use 'description: >-'")
    if not desc: errs.append("description missing")
    else:
        if len(desc) > 1024: errs.append(f"description is {len(desc)} chars, max 1024")
        if not re.search(r"\buse when\b", desc, re.I): errs.append("description needs 'use when ...' trigger words")
        if f"/{name}" not in desc: warns.append(f"description should name the slash command /{name}")
    if "model" not in d: errs.append("model missing (use model: inherit)")
    if "effort" not in d: errs.append("effort missing (low|medium|high|xhigh|max)")
    elif d["effort"] not in EFFORT: errs.append(f"effort '{d['effort']}' not in {sorted(EFFORT)}")
    for k in d:
        if k.startswith("__style__"): continue
        if k not in SPEC | CC: errs.append(f"unknown field '{k}' (Claude Code ignores it silently)")
    if d.get("context") == "fork" and "agent" not in d: warns.append("context: fork without agent: uses the default subagent")
    if body_lines > 500: errs.append(f"{body_lines} lines, max 500")
    if re.search(r"\b(MUST|NEVER|ALWAYS)\b", t[m.end():]): warns.append("shouted MUST/NEVER/ALWAYS: explain the reason instead")
    return errs, warns

if __name__ == "__main__":
    bad = 0
    for a in sys.argv[1:] or ["."]:
        e, w = check(a)
        print(("OK   " if not e else "FAIL ") + a)
        for x in e: print("  error:", x)
        for x in w: print("  warn: ", x)
        bad += bool(e)
    sys.exit(1 if bad else 0)
