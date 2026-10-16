#!/usr/bin/env python3
"""narrate.py: video/script.json -> video/audio/<node>.mp3 through ElevenLabs text to speech.
Usage: python narrate.py <topic_folder>            dry run: prints characters per scene, sends nothing
       python narrate.py <topic_folder> --send     calls the API, writes mp3s, writes seconds into script.json
Key: ELEVENLABS_API_KEY in ~/.config/pwnjournal/elevenlabs.env. Optional there: ELEVENLABS_VOICE_ID, ELEVENLABS_MODEL_ID.
API: POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}, header xi-api-key, body {text, model_id}
(elevenlabs.io/docs/api-reference/text-to-speech/convert, opened 2026-10-16, score 5).
A scene whose narration has not changed since its mp3 was made is skipped, so a rerun costs nothing.
The key is never printed and never written anywhere."""
import hashlib, json, pathlib, shutil, subprocess, sys, urllib.error, urllib.request

ENV = pathlib.Path.home() / ".config" / "pwnjournal" / "elevenlabs.env"
DEFAULT_VOICE = "JBFqnCBsd6RMkjVDRZzb"  # the example voice in the ElevenLabs docs
DEFAULT_MODEL = "eleven_multilingual_v2"  # the documented default model


def env():
    if not ENV.is_file():
        sys.exit(f"ERROR: {ENV} not found. put ELEVENLABS_API_KEY=... in it.")
    out = {}
    for line in ENV.read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            k, v = line.split("=", 1)
            out[k.strip()] = v.strip().strip('"').strip("'")
    if not out.get("ELEVENLABS_API_KEY"):
        sys.exit(f"ERROR: ELEVENLABS_API_KEY missing in {ENV}")
    return out


def seconds(mp3):
    probe = shutil.which("ffprobe")
    if not probe:
        sys.exit("ERROR: ffprobe not on PATH. install ffmpeg.")
    r = subprocess.run([probe, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp3)],
                       capture_output=True, text=True, check=True)
    return round(float(r.stdout.strip()), 2)


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    folder = pathlib.Path(args[0])
    send = "--send" in args
    sp = folder / "video" / "script.json"
    script = json.loads(sp.read_text(encoding="utf-8"))
    audio = folder / "video" / "audio"
    todo, total = [], 0
    for s in script["scenes"]:
        text = s["narration"].strip()
        sha = hashlib.sha256(text.encode()).hexdigest()[:16]
        mp3 = audio / f"{s['node']}.mp3"
        fresh = mp3.is_file() and s.get("narration_sha") == sha
        print(f"{s['node']:>6}  {len(text):5d} chars  {len(text.split()):4d} words  {'cached' if fresh else 'to send'}")
        if not fresh:
            todo.append((s, text, sha, mp3)); total += len(text)
    print(f"to send: {len(todo)} scenes, {total} characters")
    if not send:
        print("dry run. add --send to call ElevenLabs.")
        return 0
    cfg = env()
    voice = cfg.get("ELEVENLABS_VOICE_ID") or script.get("voice_id") or DEFAULT_VOICE
    model = cfg.get("ELEVENLABS_MODEL_ID") or DEFAULT_MODEL
    audio.mkdir(parents=True, exist_ok=True)
    for s, text, sha, mp3 in todo:
        req = urllib.request.Request(
            f"https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128",
            data=json.dumps({"text": text, "model_id": model}).encode(),
            headers={"xi-api-key": cfg["ELEVENLABS_API_KEY"], "Content-Type": "application/json", "Accept": "audio/mpeg"},
            method="POST")
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                mp3.write_bytes(r.read())
        except urllib.error.HTTPError as e:
            sys.exit(f"ERROR: scene {s['node']}: HTTP {e.code} {e.read()[:300].decode(errors='replace')}")
        s["narration_sha"] = sha
        print(f"wrote {mp3.name}")
    for s in script["scenes"]:
        mp3 = audio / f"{s['node']}.mp3"
        if mp3.is_file():
            s["seconds"] = seconds(mp3)
    sp.write_text(json.dumps(script, indent=1, ensure_ascii=False), encoding="utf-8")
    print("seconds:", {s["node"]: s.get("seconds") for s in script["scenes"]},
          "total", round(sum(s.get("seconds") or 0 for s in script["scenes"]), 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
