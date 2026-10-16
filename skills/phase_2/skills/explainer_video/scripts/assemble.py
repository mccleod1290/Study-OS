#!/usr/bin/env python3
"""assemble.py: render each manim scene, lay its narration under it, join them, write the HTML wrapper.
Usage: python assemble.py <topic_folder> [--quality l|m|h] [--wrapper-only]
Reads video/script.json (with seconds from narrate.py), video/scenes.py, video/audio/<node>.mp3.
Writes video/media/ (manim output), video/clips/<node>.mp4, phase2_video.mp4, phase2_video.html.
Needs manim (pip) and ffmpeg plus ffprobe on PATH. Rule: skills/phase_2/VISUALS.md."""
import html, json, pathlib, shutil, subprocess, sys


def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"ERROR: {' '.join(map(str, cmd[:4]))} ...\n{r.stderr[-2000:]}")
    return r.stdout


def dur(f):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]).strip())


def render(folder, scene, q):
    v = folder / "video"
    run([sys.executable, "-m", "manim", "render", f"-q{q}", "--media_dir", str(v / "media"),
         "--disable_caching", str(v / "scenes.py"), scene["class"]], cwd=v)
    hits = sorted((v / "media" / "videos" / "scenes").glob(f"*/{scene['class']}.mp4"), key=lambda p: p.stat().st_mtime)
    if not hits:
        sys.exit(f"ERROR: no render for {scene['class']}")
    clip = v / "clips" / f"{scene['node']}.mp4"
    clip.parent.mkdir(exist_ok=True)
    mp3 = v / "audio" / f"{scene['node']}.mp3"
    if mp3.is_file():
        # pad the picture with its last frame if the voice runs longer. never cut the voice.
        run(["ffmpeg", "-y", "-i", str(hits[-1]), "-i", str(mp3), "-filter_complex",
             f"[0:v]tpad=stop_mode=clone:stop_duration={max(0.0, dur(mp3) - dur(hits[-1])) + 0.4:.2f}[v]",
             "-map", "[v]", "-map", "1:a", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
             "-ar", "44100", str(clip)])
    else:
        run(["ffmpeg", "-y", "-i", str(hits[-1]), "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-shortest",
             "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", str(clip)])
    return clip


def wrapper(folder, script, starts):
    title = html.escape(script.get("title", folder.name))
    chap = "".join(f'<li><button data-t="{t:.2f}" data-node="{s["node"]}"><span class="ts">{int(t // 60)}:{int(t % 60):02d}</span>'
                   f'{html.escape(s.get("title", s["node"]))}</button></li>' for s, t in zip(script["scenes"], starts))
    trans = "".join(f'<section data-node="{s["node"]}"><h3>{html.escape(s.get("title", s["node"]))} '
                    f'<span class="chip">{s["node"]}</span></h3><p>{html.escape(s["narration"])}</p></section>'
                    for s in script["scenes"])
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>
:root{{--bg:#fbfaf7;--ink:#1d1f23;--muted:#6b6f76;--line:#dedbd3;--card:#fff;--accent:#b7791f}}
@media (prefers-color-scheme:dark){{:root{{--bg:#15171a;--ink:#e8e6e1;--muted:#9a9ea6;--line:#2c3036;--card:#1c1f23;--accent:#e3b155}}}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 system-ui,-apple-system,"Segoe UI",sans-serif}}
main{{max-width:1000px;margin:0 auto;padding:24px 16px}}video{{width:100%;border-radius:12px;background:#000}}
ol{{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:6px}}button{{font:inherit;font-size:14px;color:var(--ink);background:var(--card);
border:1px solid var(--line);border-radius:8px;padding:6px 10px;cursor:pointer}}button.on{{border-color:var(--accent);box-shadow:inset 0 -2px var(--accent)}}
.ts{{font:12px ui-monospace,Consolas,monospace;color:var(--muted);margin-right:6px}}
.chip{{font:11px ui-monospace,Consolas,monospace;border:1px solid var(--line);border-radius:99px;padding:2px 6px;color:var(--muted)}}
section{{border-top:1px solid var(--line);padding-top:4px}}
@media print{{video,ol{{display:none}}body{{background:#fff;color:#000}}}}
</style></head><body><main><h1>{title}</h1>
<video id="v" controls preload="metadata" src="phase2_video.mp4"></video>
<h2>chapters</h2><ol id="ch">{chap}</ol><h2>transcript</h2>{trans}</main>
<script>(function(){{var v=document.getElementById('v'),b=[].slice.call(document.querySelectorAll('#ch button'));
b.forEach(function(x){{x.onclick=function(){{v.currentTime=+x.dataset.t;v.play()}}}});
v.addEventListener('timeupdate',function(){{var t=v.currentTime,i=-1;b.forEach(function(x,j){{if(+x.dataset.t<=t+0.05)i=j}});
b.forEach(function(x,j){{x.classList.toggle('on',j===i)}})}});}})();</script></body></html>"""


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    folder = pathlib.Path(args[0]).resolve()
    q = args[args.index("--quality") + 1] if "--quality" in args else "h"
    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            sys.exit(f"ERROR: {tool} not on PATH")
    sp = folder / "video" / "script.json"
    script = json.loads(sp.read_text(encoding="utf-8"))
    clips = [folder / "video" / "clips" / f"{s['node']}.mp4" for s in script["scenes"]]
    if "--wrapper-only" not in args:
        clips = [render(folder, s, q) for s in script["scenes"]]
        lst = folder / "video" / "clips" / "list.txt"
        lst.write_text("".join(f"file '{c.name}'\n" for c in clips), encoding="utf-8")
        run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy",
             "-movflags", "+faststart", str(folder / "phase2_video.mp4")])
    starts, t = [], 0.0
    for c in clips:
        starts.append(t); t += dur(c)
    for s, c in zip(script["scenes"], clips):
        s["seconds"] = round(dur(c), 2)
    sp.write_text(json.dumps(script, indent=1, ensure_ascii=False), encoding="utf-8")
    (folder / "phase2_video.html").write_text(wrapper(folder, script, starts), encoding="utf-8")
    print(f"wrote phase2_video.mp4 ({t:.1f} s, {len(clips)} chapters) and phase2_video.html")
    return 1 if t > 600 else 0


if __name__ == "__main__":
    sys.exit(main())
