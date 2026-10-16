# Visuals: the shared context for the phase 2 visual pass

Source: Karpathy, post of 2026-10-02 (https://x.com/karpathy/status/2105819303471976479, read through api.fxtwitter.com on 2026-10-16). Score 4. He ranks four ways to present a topic, each better than the last: writing in ASD-STE100, diagrams, web pages, explainer videos. Writing is already ours (`.rules/writing-and-web.md`, `writer_skill`). This file adds the other three.

Three skills read this file: `diagrammer`, `web_builder`, `explainer_video`. Each runs in its own agent. They share nothing but the files named here.

## Order

```text
phase2_writer -> phase2_judge  SATISFIED
                     |
                     v
              diagrammer            writes diagrams/ + phase2_visuals.json
                 |        \
                 v         v
          web_builder   explainer_video      both only read; may run in parallel
                 \         /
                  v       v
          phase2_judge, with the visual checks below
```

1. The visual pass starts only when `phase2_eval.md` says SATISFIED. A visual of a page that will change is waste.
2. If the page changes after the visual pass, the visual pass runs again. Old visuals are stale.
3. The page is the source. A visual shows what the page says. It adds no new fact, no new command, no new claim.
4. Nothing in the visual pass edits `phase2_page.*`, phase 1 files, or `.rules/`.

## Files (all in the topic folder)

```text
diagrams/<node_id>.svg         one diagram per node that earns one
phase2_visuals.json            the hand-off. diagrammer writes it. the others read it
phase2_explorer.html           web_builder. the interactive page
video/script.json              explainer_video. narration and beats per scene
video/scenes.py                explainer_video. manim scenes
video/audio/<node_id>.mp3      explainer_video. narration
phase2_video.mp4               explainer_video. the film
phase2_video.html              explainer_video. the wrapper: player, chapters, transcript
```

## phase2_visuals.json

```json
{
  "slug": "<slug>",
  "page_hash": "<sha256 of phase2_page.md when diagrammer ran>",
  "diagrams": [
    {
      "node": "d1",
      "file": "diagrams/d1.svg",
      "kind": "flow | sequence | boundary | state | compare | anatomy",
      "title": "short name",
      "caption": "one sentence: what to see",
      "grade": 4,
      "steps": ["step 1 caption", "step 2 caption"],
      "when": {"applies": "condition", "fails": "when it does not apply"}
    }
  ]
}
```

- `steps` is present when the SVG has groups with `data-step="1"`, `"2"`... in the order of the list.
- `when` is present when the SVG has groups with `data-when="applies"` and `data-when="fails"`.
- `grade` is the lowest grade of the page claims the diagram draws.
- `page_hash` lets the judge see that the visuals match the current page.

## Style (one look for all three)

| token | light | dark | use |
|---|---|---|---|
| `--bg` | `#fbfaf7` | `#15171a` | page |
| `--ink` | `#1d1f23` | `#e8e6e1` | text, lines |
| `--muted` | `#6b6f76` | `#9a9ea6` | captions |
| `--client` | `#2f6fdb` | `#6fa0ff` | browser, user, attacker side |
| `--server` | `#1f9d6b` | `#4cc99a` | app, server side |
| `--danger` | `#d1453b` | `#ff7a6e` | the flaw, the bad path, "fails" |
| `--accent` | `#b7791f` | `#e3b155` | the one thing to look at now |

1. SVG uses these as `var(--token, <light value>)`, so a diagram also reads alone.
2. Text in SVG is `<text>`, never a path. Font is the system stack. Minimum 12 px.
3. Each SVG has `viewBox`, `role="img"`, `<title>` and `<desc>`. No fixed `width` or `height`.
4. Color is never the only signal. The bad path is red and dashed. The step in focus is accent and bold.
5. In video, the same colors on a `--bg` dark background.

## Hard limits

1. Self-contained. No CDN, no web font, no external `src`. Links in text are fine. The one file outside the HTML is `phase2_video.mp4`, beside its wrapper (`.rules/html-deliverables.md` rule 9).
2. Each HTML has `@media print`. Print shows every step and both `when` states, open.
3. Words. The explorer carries the page text and no new prose, apart from captions and the labels on the controls. Video narration: at most 150 words per domain, at most 10 minutes for the whole film.
4. Coverage. Every domain of the map has a diagram. A topic or an anchor gets one only where the order or the shape is the point. Every node of the map is in the explorer, tagged `data-node="<id>"`. Every domain is a chapter in the video.
5. Lab scope. A diagram of an attack names `$TARGET` or a lab host, never a real site.
6. Narration is sent to ElevenLabs. Send only the narration text: no key, no path, no personal data. The key lives in `~/.config/pwnjournal/elevenlabs.env`. Never print it, copy it, or write it to a file in this repo.

## Check

```text
python skills/scripts/check_visuals.py <slug>
```

It must print OK. It checks the json, every SVG, the explorer, and the video wrapper when one exists.

## Judge: the visual checks

Pass these to `phase2_judge` as extra checks, after the visual pass. One line each, pass or fail:

1. `check_visuals.py <slug>` prints OK.
2. `page_hash` in `phase2_visuals.json` equals the sha256 of `phase2_page.md` now.
3. Pick 5 diagrams. Each one draws only what its node says on the page. Name any new fact.
4. Each `steps` list follows the order the page gives.
5. The explorer adds no prose beyond captions and control labels.
6. The narration in `video/script.json` says only what the page says, in ASD-STE100. Grade 2 claims are not narrated as fact.
7. The film is under 10 minutes. Each chapter starts at the time the wrapper says.
