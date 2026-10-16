#!/usr/bin/env python3
"""build_explorer.py: phase2_page.md + diagrams + widgets -> phase2_explorer.html, one self-contained file.
Usage: python skills/scripts/build_explorer.py <slug>
Rule: skills/phase_2/VISUALS.md. Reads phase2_page.md, phase1_mindmap.json, phase2_visuals.json (optional),
widgets/<node_id>.html (optional). Writes phase2_explorer.html. Same input, same output.
The page text is rendered as is. This script adds no prose, only captions and control labels."""
import hashlib, html, json, pathlib, re, sys

import markdown

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / ".rules").is_dir())
TAG = re.compile(r"\{([A-Za-z]+\d+[a-z]?)\}")
GRADE = re.compile(r"\[g([1-5])\]")


def find(slug):
    hits = sorted((ROOT / "Artifacts" / "artifacts").glob(f"**/{slug}/phase1_mindmap.json"))
    if not hits:
        sys.exit(f"ERROR: no phase1_mindmap.json for slug {slug!r}")
    return hits[0].parent


def walk(n, out):
    for c in n.get("k", []) if isinstance(n.get("k"), list) else []:
        out.append(c)
        walk(c, out)
    return out


def outside_code(body, fn):
    parts = re.split(r"(<pre>.*?</pre>|<code>.*?</code>)", body, flags=re.S)
    return "".join(p if i % 2 else fn(p) for i, p in enumerate(parts))


def svg_inline(path):
    s = path.read_text(encoding="utf-8")
    s = re.sub(r"<\?xml.*?\?>|<!DOCTYPE.*?>", "", s, flags=re.S).strip()
    return s


def figure(d, folder):
    steps = d.get("steps") or []
    when = d.get("when") or {}
    ctl = []
    if steps:
        ctl.append('<div class="ctl stepper"><button data-act="prev" aria-label="previous step">&#9664;</button>'
                   '<span class="stepno">all</span><button data-act="next" aria-label="next step">&#9654;</button>'
                   '<button data-act="all">all steps</button></div>')
    if when:
        ctl.append('<div class="ctl when" role="group" aria-label="condition">'
                   '<button data-when="applies">applies</button><button data-when="fails">does not apply</button>'
                   '<button data-when="both" aria-pressed="true">both</button></div>')
    when_txt = "".join(f'<p class="whentxt" data-w="{k}"><b>{"applies" if k == "applies" else "does not apply"}:</b> '
                       f'{html.escape(v)}</p>' for k, v in when.items())
    steps_txt = "".join(f"<li>{html.escape(s)}</li>" for s in steps)
    return (f'<figure class="dia" tabindex="0" data-node="{d["node"]}" data-kind="{html.escape(d.get("kind", ""))}" '
            f"data-steps='{html.escape(json.dumps(steps))}'>"
            f'<div class="dia-head"><span class="kind">{html.escape(d.get("kind", ""))}</span>'
            f'<b>{html.escape(d.get("title", ""))}</b><span class="g g{d.get("grade", 3)}">g{d.get("grade", 3)}</span></div>'
            f'{svg_inline(folder / d["file"])}{"".join(ctl)}'
            f'<figcaption><span class="cap">{html.escape(d.get("caption", ""))}</span>'
            f'{when_txt}{f"<ol class=steplist>{steps_txt}</ol>" if steps else ""}</figcaption></figure>')


def insert_after_node(body, node, block):
    m = re.search(rf'data-node="{re.escape(node)}"', body)
    if not m:
        return body, False
    end = re.compile(r"</(p|h2|h3|h4|li|ul|ol|table|blockquote)>").search(body, m.end())
    if not end:
        return body, False
    # an li or a nested list: close the whole list first
    if end.group(1) in ("li",):
        lst = re.compile(r"</(ul|ol)>").search(body, end.end())
        end = lst or end
    return body[:end.end()] + block + body[end.end():], True


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    slug = sys.argv[1]
    folder = find(slug)
    page = folder / "phase2_page.md"
    if not page.is_file():
        sys.exit(f"ERROR: missing {page}")
    src = page.read_text(encoding="utf-8")
    mind = json.loads((folder / "phase1_mindmap.json").read_text(encoding="utf-8"))
    nodes = walk(mind["tree"], [])
    domains = [n for n in mind["tree"].get("k", [])]
    vis_path = folder / "phase2_visuals.json"
    vis = json.loads(vis_path.read_text(encoding="utf-8")) if vis_path.is_file() else {"diagrams": []}

    body = markdown.markdown(src, extensions=["tables", "fenced_code"])
    body = outside_code(body, lambda p: TAG.sub(r'<span class="chip" data-node="\1">\1</span>', p))
    body = outside_code(body, lambda p: GRADE.sub(r'<span class="g g\1">g\1</span>', p))

    # one <section> per h2. a domain h2 with no tag takes its map id by position.
    chunks = re.split(r"(?=<h2>)", body)
    head, secs = chunks[0], chunks[1:]
    out, nav, di = [head], [], 0
    for s in secs:
        h = re.match(r"<h2>(.*?)</h2>", s, re.S)
        title = re.sub(r"<[^>]+>", "", h.group(1)).strip() if h else ""
        tag = re.search(r'data-node="([^"]+)"', h.group(1)) if h else None
        is_ref = title.lower().startswith("references")
        nid = tag.group(1) if tag else (domains[di]["id"] if not is_ref and di < len(domains) else ("refs" if is_ref else f"s{di}"))
        if not is_ref:
            di += 1
        out.append(f'<section id="sec-{nid}" data-node="{nid}">{s}</section>')
        nav.append(f'<a href="#sec-{nid}" data-target="sec-{nid}"><span class="chip">{nid}</span>{html.escape(title)}</a>')
    body = "".join(out)

    placed, missing = [], []
    for d in vis.get("diagrams", []):
        if not (folder / d["file"]).is_file():
            missing.append(d["file"]); continue
        body, ok = insert_after_node(body, d["node"], figure(d, folder))
        (placed if ok else missing).append(d["node"])
    wdir = folder / "widgets"
    for w in sorted(wdir.glob("*.html")) if wdir.is_dir() else []:
        block = f'<div class="widget" data-node="{w.stem}">{w.read_text(encoding="utf-8")}</div>'
        body, ok = insert_after_node(body, w.stem, block)
        (placed if ok else missing).append(f"widget {w.stem}")

    present = set(re.findall(r'data-node="([^"]+)"', body))
    absent = [n["id"] for n in nodes if n["id"] not in present]
    page_hash = hashlib.sha256(page.read_bytes()).hexdigest()
    title = html.escape(mind.get("title", slug))
    doc = TEMPLATE.replace("%TITLE%", title).replace("%NAV%", "".join(nav)).replace("%BODY%", body) \
        .replace("%FOOT%", f"built by build_explorer.py from phase2_page.md sha256 {page_hash[:12]}")
    (folder / "phase2_explorer.html").write_text(doc, encoding="utf-8")
    print(f"wrote {folder / 'phase2_explorer.html'}")
    print(f"placed {len(placed)}  missing {missing or 'none'}  nodes not on page {absent or 'none'}")
    if vis.get("page_hash") and vis["page_hash"] != page_hash:
        print("WARN: phase2_visuals.json page_hash does not match phase2_page.md. visuals are stale.")
    return 1 if missing else 0


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%TITLE%</title>
<style>
:root{--bg:#fbfaf7;--ink:#1d1f23;--muted:#6b6f76;--line:#dedbd3;--card:#fff;--client:#2f6fdb;--server:#1f9d6b;--danger:#d1453b;--accent:#b7791f;
--mono:ui-monospace,SFMono-Regular,Consolas,monospace;--sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#15171a;--ink:#e8e6e1;--muted:#9a9ea6;--line:#2c3036;--card:#1c1f23;--client:#6fa0ff;--server:#4cc99a;--danger:#ff7a6e;--accent:#e3b155}}
:root[data-theme="dark"]{--bg:#15171a;--ink:#e8e6e1;--muted:#9a9ea6;--line:#2c3036;--card:#1c1f23;--client:#6fa0ff;--server:#4cc99a;--danger:#ff7a6e;--accent:#e3b155}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 var(--sans)}
#bar{position:fixed;top:0;left:0;height:3px;background:var(--accent);width:0;z-index:9}
.layout{display:grid;grid-template-columns:260px minmax(0,1fr);max-width:1180px;margin:0 auto}
nav{position:sticky;top:0;height:100vh;overflow:auto;padding:24px 12px;border-right:1px solid var(--line);font-size:14px}
nav a{display:flex;gap:8px;align-items:baseline;padding:6px 8px;border-radius:6px;color:var(--ink);text-decoration:none}
nav a:hover{background:var(--card)}nav a.on{background:var(--card);box-shadow:inset 3px 0 var(--accent)}
nav .tools{display:flex;gap:6px;margin-top:16px}
main{padding:24px 32px 80px;min-width:0;overflow-wrap:anywhere}
h1{font-size:1.9rem;line-height:1.2}h2{margin-top:2.4rem;padding-top:.6rem;border-top:1px solid var(--line)}
a{color:var(--client)}
pre{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px;overflow:auto;font:13px/1.5 var(--mono)}
code{font-family:var(--mono);font-size:.9em}
table{border-collapse:collapse;width:100%;display:block;overflow:auto}th,td{border:1px solid var(--line);padding:6px 8px;vertical-align:top}
blockquote{margin:0;padding:8px 14px;border-left:3px solid var(--accent);background:var(--card);border-radius:0 8px 8px 0}
.chip{display:inline-block;font:11px/1 var(--mono);padding:3px 6px;border-radius:99px;border:1px solid var(--line);color:var(--muted);vertical-align:middle}
.g{display:inline-block;font:11px/1 var(--mono);padding:3px 6px;border-radius:4px;color:#fff;vertical-align:middle}
.g5{background:#1f7a4f}.g4{background:#3f8f5a}.g3{background:#9a7b1c}.g2{background:#b5522f}.g1{background:#8a2a2a}
.dia{margin:20px 0;padding:14px;background:var(--card);border:1px solid var(--line);border-radius:12px}
.dia:focus{outline:2px solid var(--accent)}
.dia-head{display:flex;gap:10px;align-items:center;margin-bottom:8px}.dia-head .kind{font:11px var(--mono);color:var(--muted);text-transform:uppercase}
.dia svg{width:100%;height:auto;max-height:70vh;display:block}
.dia svg [data-step],.dia svg [data-when]{transition:opacity .25s}
.dia svg .dim{opacity:.28}.dia svg .off,.dia svg .whenoff{opacity:.06}.dia svg .focus{filter:drop-shadow(0 0 4px var(--accent))}
.ctl{display:inline-flex;gap:6px;align-items:center;margin:8px 10px 0 0}
button{font:13px var(--sans);color:var(--ink);background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:4px 10px;cursor:pointer}
button:hover{border-color:var(--accent)}button[aria-pressed="true"]{background:var(--accent);color:#fff;border-color:var(--accent)}
.stepno{font:12px var(--mono);min-width:5ch;text-align:center}
figcaption{margin-top:8px;color:var(--muted);font-size:14px}.steplist{display:none}
.whentxt{margin:4px 0}.whentxt[data-w="fails"] b{color:var(--danger)}
.widget{margin:20px 0}
footer{margin-top:48px;color:var(--muted);font:12px var(--mono)}
@media (max-width:820px){.layout{display:block}nav{position:static;height:auto;border:0;border-bottom:1px solid var(--line)}main{padding:16px}}
@media print{nav,#bar,.ctl{display:none}.layout{display:block}main{padding:0}
 .dia svg [data-step],.dia svg [data-when]{opacity:1!important;filter:none!important}.steplist{display:block}
 .dia,pre{break-inside:avoid}body{background:#fff;color:#000}}
</style></head><body>
<div id="bar"></div>
<div class="layout">
<nav aria-label="sections">%NAV%<div class="tools"><button id="theme">theme</button><button onclick="print()">print</button></div></nav>
<main>%BODY%<footer>%FOOT%</footer></main>
</div>
<script>
(function(){
var root=document.documentElement,t=null;try{t=localStorage.getItem('explorer-theme')}catch(e){}
if(t)root.dataset.theme=t;
document.getElementById('theme').onclick=function(){var d=root.dataset.theme==='dark'||(!root.dataset.theme&&matchMedia('(prefers-color-scheme:dark)').matches);
root.dataset.theme=d?'light':'dark';try{localStorage.setItem('explorer-theme',root.dataset.theme)}catch(e){}};
var bar=document.getElementById('bar');addEventListener('scroll',function(){var h=document.body.scrollHeight-innerHeight;bar.style.width=(h>0?scrollY/h*100:0)+'%'});
var links={};document.querySelectorAll('nav a[data-target]').forEach(function(a){links[a.dataset.target]=a});
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){for(var k in links)links[k].classList.remove('on');var a=links[e.target.id];if(a)a.classList.add('on')}})},{rootMargin:'-20% 0px -70% 0px'});
document.querySelectorAll('main section').forEach(function(s){io.observe(s)});
document.querySelectorAll('figure.dia').forEach(function(f){
 var svg=f.querySelector('svg');if(!svg)return;var steps=JSON.parse(f.dataset.steps||'[]');
 var gs=[].slice.call(svg.querySelectorAll('[data-step]')),k=0,cap=f.querySelector('.cap'),base=cap?cap.textContent:'',no=f.querySelector('.stepno');
 function show(n){k=n;gs.forEach(function(g){var s=+g.dataset.step;g.classList.remove('dim','off','focus');
  if(k){if(s<k)g.classList.add('dim');else if(s>k)g.classList.add('off');else g.classList.add('focus')}});
  if(no)no.textContent=k?k+' / '+steps.length:'all';if(cap)cap.textContent=k?steps[k-1]:base}
 f.querySelectorAll('.stepper button').forEach(function(b){b.onclick=function(){var a=b.dataset.act,n=steps.length;
  show(a==='all'?0:a==='next'?(k%n)+1:(k<=1?n:k-1))}});
 f.addEventListener('keydown',function(e){if(!steps.length)return;if(e.key==='ArrowRight'){show((k%steps.length)+1);e.preventDefault()}
  if(e.key==='ArrowLeft'){show(k<=1?steps.length:k-1);e.preventDefault()}if(e.key==='Escape')show(0)});
 var wb=[].slice.call(f.querySelectorAll('.when button'));
 wb.forEach(function(b){b.onclick=function(){var w=b.dataset.when;wb.forEach(function(x){x.setAttribute('aria-pressed',x===b)});
  svg.querySelectorAll('[data-when]').forEach(function(g){g.classList.toggle('whenoff',w!=='both'&&g.dataset.when!==w)});
  f.querySelectorAll('.whentxt').forEach(function(p){p.style.display=(w==='both'||p.dataset.w===w)?'':'none'})}});
});
})();
</script>
</body></html>
"""

if __name__ == "__main__":
    sys.exit(main())
