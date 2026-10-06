"""Deterministic builder and validator for the phase 1 interactive mind map.
usage: python skills/scripts/build_mindmap.py <slug | folder with mindmap.json>
Same mindmap.json + same template = byte-identical MAP.html. No clock, no randomness."""
import json, sys, pathlib, hashlib, re

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / ".rules").is_dir())
LV = {"foundation": 0, "core": 1, "dive": 2}
MODES = {"audit", "book", "video", "course", "work"}

def validate(d, map_md):
    err, warn = [], []
    for k in ("title", "subtitle", "slug", "study_mode", "sources", "controls", "tree"):
        if k not in d: err.append(f"missing top-level key: {k}")
    if err: return err, warn
    if d["study_mode"] not in MODES: err.append(f"study_mode must be one of {sorted(MODES)}")
    for k, s in d["sources"].items():
        ok = isinstance(s, dict) and s.get("t") and (str(s.get("u", "")).startswith("https://") or s.get("ref"))
        if not ok: err.append(f"source {k}: needs t and either an https u or a ref (chapter, page, timestamp)")
    seen, nodes = set(), []
    def walk(n, depth):
        nid = n.get("id")
        if not nid or not re.fullmatch(r"[a-z0-9_]+", nid): err.append(f"bad id: {nid!r}")
        if nid in seen: err.append(f"duplicate id: {nid}")
        seen.add(nid); nodes.append((n, depth))
        if depth > 0:
            for f in ("t", "s", "lv"):
                if not n.get(f): err.append(f"{nid}: missing {f}")
            if n.get("lv") not in LV: err.append(f"{nid}: lv must be foundation, core or dive")
            if depth >= 2 and not n.get("w"): warn.append(f"{nid}: no 'w' (why it matters)")
        for s in n.get("src", []):
            if s not in d["sources"]: err.append(f"{nid}: unknown source {s}")
        for c in n.get("c", []):
            if c not in d["controls"]: err.append(f"{nid}: unknown anchor {c}")
        if depth >= 2 and not n.get("src") and not n.get("ungrounded") and not n.get("from"):
            warn.append(f"{nid}: no source and not flagged ungrounded")
        kids = n.get("k", [])
        if depth == 1 and not kids: err.append(f"{nid}: domain has no topics")
        if depth >= 2:
            lv = [LV.get(x.get("lv"), 9) for x in kids]
            if lv != sorted(lv): warn.append(f"{nid}: children not ordered foundation, core, dive")
        for k in kids: walk(k, depth + 1)
    walk(d["tree"], 0)
    used = {c for n, _ in nodes for c in n.get("c", [])}
    for c in d["controls"]:
        if c not in used: err.append(f"anchor {c} is covered by no topic")
    doms = [n for n, dep in nodes if dep == 1]
    if map_md:
        m = len(re.findall(r"^\s+\d+\.\s", map_md, flags=re.M))
        if m and m != len(doms): warn.append(f"MAP.md lists {m} domains, mindmap.json has {len(doms)}")
    return err, warn

def build(d, tpl):
    js = json.dumps(d, ensure_ascii=False, sort_keys=True, separators=(",", ":")).replace("</", "<\\/")
    return tpl.replace("/*__DATA__*/", js)

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    slug = args[0] if args else "aws_oidc_flow"
    hits = sorted((ROOT / "Artifacts" / "artifacts").glob("**/" + slug + "/phase1_mindmap.json"))
    art = hits[0].parent if hits else ROOT / "Artifacts" / "artifacts" / slug
    out = pathlib.Path(slug) if pathlib.Path(slug).is_dir() else (art if (art / "phase1_mindmap.json").exists() else ROOT / "skills" / "phase_1" / "output" / slug)
    pre = "phase1_" if (out / "phase1_mindmap.json").exists() else ""
    jn, hn, mn = (pre + "mindmap.json", "phase1_map.html" if pre else "MAP.html", "phase1_map.md" if pre else "MAP.md")
    d = json.loads((out / jn).read_text(encoding="utf-8"))
    mp = out / mn
    err, warn = validate(d, mp.read_text(encoding="utf-8") if mp.exists() else "")
    for w in warn: print("warn:", w)
    if err:
        for e in err: print("ERROR:", e)
        sys.exit(1)
    tpl = (ROOT / "skills" / "scripts" / "mindmap_template.html").read_text(encoding="utf-8")
    a, b = build(d, tpl), build(d, tpl)
    if a != b: print("ERROR: build is not deterministic"); sys.exit(1)
    (out / hn).write_bytes(a.encode("utf-8"))
    print("wrote", out / hn)
    print("sha256", hashlib.sha256(a.encode("utf-8")).hexdigest()[:16], f"nodes={sum(1 for _ in re.finditer(chr(34)+'id'+chr(34), json.dumps(d)))}", f"warnings={len(warn)}")

main()
