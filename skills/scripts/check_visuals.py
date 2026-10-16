#!/usr/bin/env python3
"""check_visuals.py: is the phase 2 visual pass sound?
Usage: python skills/scripts/check_visuals.py <slug> [--stage diagrams|explorer|video|all]
Rule: skills/phase_2/VISUALS.md. Default stage is all: it checks each part that exists.
Exit 1 on any error."""
import hashlib, json, pathlib, re, sys
import xml.etree.ElementTree as ET

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / ".rules").is_dir())
KINDS = {"flow", "sequence", "boundary", "state", "compare", "anatomy"}
EXTERNAL = re.compile(r"""(?:src|href)\s*=\s*["'](?:https?:)?//""", re.I)
SVGNS = "{http://www.w3.org/2000/svg}"


def walk(n, out):
    for c in n.get("k", []) if isinstance(n.get("k"), list) else []:
        out.append(c["id"]); walk(c, out)
    return out


def check_diagrams(folder, mind, bad):
    p = folder / "phase2_visuals.json"
    if not p.is_file():
        bad.append("missing phase2_visuals.json"); return
    try:
        vis = json.loads(p.read_text(encoding="utf-8"))
    except ValueError as e:
        bad.append(f"phase2_visuals.json: {e}"); return
    ids = set(walk(mind["tree"], [])) | set(mind.get("controls", {}))
    page = folder / "phase2_page.md"
    if vis.get("page_hash") != hashlib.sha256(page.read_bytes()).hexdigest():
        bad.append("page_hash does not match phase2_page.md: visuals are stale")
    have = set()
    for d in vis.get("diagrams", []):
        n = d.get("node", "?")
        have.add(n)
        if n not in ids: bad.append(f"{n}: node not in map")
        if d.get("kind") not in KINDS: bad.append(f"{n}: kind {d.get('kind')!r} not in {sorted(KINDS)}")
        if d.get("grade") not in (1, 2, 3, 4, 5): bad.append(f"{n}: grade must be 1 to 5")
        if not d.get("caption"): bad.append(f"{n}: no caption")
        f = folder / d.get("file", "")
        if not f.is_file():
            bad.append(f"{n}: missing {d.get('file')}"); continue
        text = f.read_text(encoding="utf-8")
        try:
            svg = ET.fromstring(text)
        except ET.ParseError as e:
            bad.append(f"{d['file']}: not valid xml: {e}"); continue
        if svg.tag not in ("svg", SVGNS + "svg"): bad.append(f"{d['file']}: root is not svg")
        if "viewBox" not in svg.attrib: bad.append(f"{d['file']}: no viewBox")
        if svg.attrib.get("role") != "img": bad.append(f"{d['file']}: role is not img")
        for t in ("title", "desc"):
            if svg.find(t) is None and svg.find(SVGNS + t) is None: bad.append(f"{d['file']}: no <{t}>")
        if EXTERNAL.search(text): bad.append(f"{d['file']}: external src or href")
        if re.search(r"<(script|image|foreignObject)\b", text): bad.append(f"{d['file']}: script, image or foreignObject")
        steps = sorted(int(s) for s in re.findall(r'data-step="(\d+)"', text))
        want = list(range(1, len(d.get("steps") or []) + 1))
        if sorted(set(steps)) != want: bad.append(f"{d['file']}: data-step groups {sorted(set(steps))} do not match steps list {want}")
        whens = set(re.findall(r'data-when="(\w+)"', text))
        if set(d.get("when") or {}) != whens: bad.append(f"{d['file']}: data-when groups {sorted(whens)} do not match when keys")
    for dom in mind["tree"].get("k", []):
        if dom["id"] not in have: bad.append(f"domain {dom['id']} has no diagram")


def check_html(f, bad, allow_src=()):
    text = f.read_text(encoding="utf-8")
    for m in re.finditer(r"""src\s*=\s*["']([^"']+)["']""", text, re.I):
        if m.group(1) not in allow_src: bad.append(f"{f.name}: src {m.group(1)!r}")
    if re.search(r"<link\b[^>]*stylesheet", text, re.I): bad.append(f"{f.name}: external stylesheet")
    if "@media print" not in text: bad.append(f"{f.name}: no @media print")
    return text


def check_explorer(folder, mind, bad):
    f = folder / "phase2_explorer.html"
    if not f.is_file():
        bad.append("missing phase2_explorer.html"); return
    text = check_html(f, bad)
    present = set(re.findall(r'data-node="([^"]+)"', text))
    for i in walk(mind["tree"], []):
        if i not in present: bad.append(f"explorer: node {i} not tagged")


def check_video(folder, mind, bad):
    f = folder / "phase2_video.html"
    if not f.is_file():
        bad.append("missing phase2_video.html"); return
    check_html(f, bad, allow_src=("phase2_video.mp4",))
    if not (folder / "phase2_video.mp4").is_file(): bad.append("missing phase2_video.mp4")
    sp = folder / "video" / "script.json"
    if not sp.is_file():
        bad.append("missing video/script.json"); return
    scenes = json.loads(sp.read_text(encoding="utf-8")).get("scenes", [])
    have = {s.get("node") for s in scenes}
    for dom in mind["tree"].get("k", []):
        if dom["id"] not in have: bad.append(f"video: domain {dom['id']} has no scene")
    total = 0.0
    for s in scenes:
        w = len(s.get("narration", "").split())
        if w > 150: bad.append(f"video: scene {s.get('node')} narration {w} words, limit 150")
        total += float(s.get("seconds") or 0)
    if total > 600: bad.append(f"video: {total:.0f} s, limit 600")


def main():
    args = sys.argv[1:]
    if not args: sys.exit(__doc__)
    slug = args[0]
    stage = args[args.index("--stage") + 1] if "--stage" in args else "all"
    hits = sorted((ROOT / "Artifacts" / "artifacts").glob(f"**/{slug}/phase1_mindmap.json"))
    if not hits:
        print("ERROR: no phase1_mindmap.json for slug", repr(slug)); return 1
    folder = hits[0].parent
    mind = json.loads(hits[0].read_text(encoding="utf-8"))
    bad = []
    if stage in ("diagrams", "all"): check_diagrams(folder, mind, bad)
    if stage == "explorer" or (stage == "all" and (folder / "phase2_explorer.html").exists()): check_explorer(folder, mind, bad)
    if stage == "video" or (stage == "all" and (folder / "phase2_video.html").exists()): check_video(folder, mind, bad)
    for b in bad: print("FAIL", b)
    if bad: return 1
    print(f"OK  {slug}  stage {stage}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
