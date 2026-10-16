---
name: explainer_video
description: >-
  phase 2 visual pass, step 3. turns the judged phase 2 page and the
  diagrammer's diagrams into a narrated explainer film in the 3Blue1Brown
  manner: one manim scene per domain, ElevenLabs narration in ASD-STE100,
  joined into phase2_video.mp4 with an HTML wrapper that has chapters and a
  transcript. sends narration text to ElevenLabs, which costs credits. use
  when the diagrams are done and the user says explainer video, make a
  video, animate it, 3blue1brown, or /explainer_video.
disable-model-invocation: true
model: inherit
effort: high
---

# explainer_video

Karpathy's fourth rung, the one he rates highest: a custom explainer video on any topic, in the 3Blue1Brown manner, with a voice. Shared rules, files, style tokens and limits: `skills/phase_2/VISUALS.md`. Read it first.

Tools: manim Community (`python -m manim`, https://docs.manim.community, opened 2026-10-16, score 5), ffmpeg and ffprobe on PATH, ElevenLabs text to speech through `scripts/narrate.py` (score 5, source in its docstring).

## Gate

`check_visuals.py <slug> --stage diagrams` prints OK. `python -m manim --version` and `ffmpeg -version` run. If not, make nothing and say which one is missing.

## Why this shape

A 3Blue1Brown film shows one idea at a time and moves the picture as the voice speaks. The picture carries the mechanism; the voice says only what the picture cannot. So: few words, one moving diagram, and the next step appears only when the voice reaches it.

## Steps

1. **Script.** Write `video/script.json`:
   ```json
   {"title": "...", "scenes": [{"node": "d1", "class": "D1", "title": "...",
     "narration": "ASD-STE100 text, at most 150 words", "beats": ["what moves, in order"]}]}
   ```
   One scene per domain, in map order. Narration says only what the page says. Short sentences, one idea each, active voice, the same term for the same thing. A grade 2 claim is not said as fact: say "not verified" or leave it out. Lead with the parts and the condition, then the steps.
2. **Voice, dry run.** `python <this skill>/scripts/narrate.py <topic_folder>`. Read the character count. Then `--send`. It writes `video/audio/<node>.mp3` and the `seconds` of each scene into `script.json`. A rerun sends only the scenes whose narration changed.
3. **Scenes.** Write `video/scenes.py`. One `Scene` class per scene, named as in `class`. Rules:
   - Build from the domain's SVG: rebuild its boxes, arrows and labels as manim objects (`RoundedRectangle`, `Arrow`, `Text`). Same layout, same colors as VISUALS.md, dark background `#15171a`.
   - `Text` only. No `Tex` or `MathTex`: there is no LaTeX on this machine.
   - One beat per `self.play`. Time the beats to the voice: read `seconds` from `script.json` and split it over the beats, so the picture moves when the words reach it. End with `self.wait` to fill the rest.
   - Lab hosts only: `$TARGET`. Code on screen is a short line copied from the page, in a monospace `Text`.
   - At most about 12 objects on screen. Fade out what is done.
4. **Assemble.** `python <this skill>/scripts/assemble.py <topic_folder> --quality l` for a fast draft. Fix any render error. Then `--quality h`. It writes `phase2_video.mp4` and `phase2_video.html` (player, chapters, transcript).
5. **Check.** `python skills/scripts/check_visuals.py <slug> --stage video` prints OK. Total under 10 minutes.

## Do not

- Send anything to ElevenLabs but the narration text. Never print, copy or write the key.
- Run `--send` before the dry run, or send the same scene twice for no change.
- Edit the page, the diagrams or `phase2_visuals.json`.
- Embed the mp4 in the HTML as base64. It sits beside the wrapper (`.rules/html-deliverables.md` rule 9).

## Model

model: inherit. effort: high. The failure is a film that reads the page aloud over a still picture, or a voice that says a fact the page does not.
