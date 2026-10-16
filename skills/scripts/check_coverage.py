#!/usr/bin/env python3
"""check_coverage.py: does phase2_page.md cover every node of phase1_mindmap.json?
Usage: python skills/scripts/check_coverage.py <slug>
Rule: .rules/phase-order-and-coverage.md. Exit 1 on any missing or unknown id, or wrong order.
Tags in the page are node ids in curly braces: {d1}, {d1a}, {H1}."""
import json, re, sys, pathlib

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / ".rules").is_dir())

def nodes(n, out):
    for c in n.get("k", []):
        out.append(c["id"]); nodes(c, out)
    return out

def main():
    slug = sys.argv[1] if len(sys.argv) > 1 else ""
    hits = sorted((ROOT / "Artifacts" / "artifacts").glob("**/" + slug + "/phase1_mindmap.json")) if slug else []
    if not hits:
        print("ERROR: no phase1_mindmap.json for slug", repr(slug)); return 1
    folder = hits[0].parent
    page = folder / "phase2_page.md"
    if not page.is_file():
        print("ERROR: missing", page); return 1
    m = json.loads(hits[0].read_text(encoding="utf-8"))
    ids = nodes(m["tree"], [])
    anchors = list(m.get("controls", {}))
    text = re.sub(r"```.*?```", "", page.read_text(encoding="utf-8"), flags=re.S)
    tags = re.findall(r"\{([A-Za-z]+\d+[a-z]?)\}", text)
    seen = set(tags)
    missing = [i for i in ids + anchors if i not in seen]
    unknown = sorted(seen - set(ids) - set(anchors))
    first = {}
    for pos, t in enumerate(tags):
        first.setdefault(t, pos)
    order = [i for i in ids if i in first]
    bad_order = [b for a, b in zip(order, order[1:]) if first[b] < first[a]]
    for x in missing: print("MISSING", x)
    for x in unknown: print("UNKNOWN", x)
    for x in bad_order: print("ORDER  ", x, "appears before an earlier node")
    if missing or unknown or bad_order:
        print(f"FAIL  {len(missing)} missing, {len(unknown)} unknown, {len(bad_order)} out of order"); return 1
    print(f"OK  {len(ids)} nodes and {len(anchors)} anchors covered, in map order")
    return 0

if __name__ == "__main__":
    sys.exit(main())
