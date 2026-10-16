---
name: web_builder
description: >-
  phase 2 visual pass, step 2. fuses the judged phase 2 page and the
  diagrammer's svgs into one interactive, self-contained web page,
  phase2_explorer.html: section nav, step-through diagrams, an applies or
  does-not-apply toggle, and hand-built widgets where touching the thing
  teaches it. adds no prose. use when the diagrams are done and the user says
  web page, interactive page, explorer, make it interactive, or /web_builder.
model: inherit
effort: high
---

# web_builder

Karpathy's third rung: ask for the answer as an interactive web page. Shared rules, files, style tokens and limits: `skills/phase_2/VISUALS.md`. Read it first.

## Gate

`phase2_visuals.json` exists and `python skills/scripts/check_visuals.py <slug> --stage diagrams` prints OK. If not, build nothing and say so.

## Two layers

1. **The frame is a script.** `python skills/scripts/build_explorer.py <slug>` renders the page text as is, wraps each domain in a section, places each diagram after its node, and adds the nav, the progress bar, the theme toggle, the stepper (buttons and arrow keys), the condition toggle and the print stylesheet. Same input, same output. Do not hand-edit `phase2_explorer.html`. Change the inputs and run it again.
2. **The widgets are yours.** A widget is a small piece of HTML, CSS and JS in `widgets/<node_id>.html`. The script places it after that node. Make one only where doing teaches more than reading:

| the page shows | widget |
|---|---|
| the parts of a request, URL, cookie or token | the real string. hover or tap a part to see its name and role, in the page's words. |
| a parameter that changes the result | a toggle or a field. the shown request and the shown response change, both copied from the page. |
| an encoding or a transform | an input box and the output, computed in the browser. |
| a decision with branches | click a branch to light that path in the diagram. |
| 2011 against 2026 | a switch between the two columns. |

At most one widget per topic. Zero is fine. A widget that is decoration is cut.

## Widget rules

1. Plain JS in one IIFE. No library, no network, no `fetch`, no `eval`. Scope CSS under `.widget[data-node="<id>"]`. Use the tokens in VISUALS.md.
2. Every string and every value comes from the page. The widget computes, it does not claim. A transform runs on the input; it does not invent a server reply.
3. Hosts are `$TARGET` or a lab host.
4. Keyboard works. Every control has a label. It reads in print: give it a `@media print` state that shows the default view.

## Steps

1. Read `phase2_page.md`, `phase2_visuals.json` and the SVGs.
2. Write the widgets.
3. Run `build_explorer.py <slug>`. It must say `missing none` and `nodes not on page none`. Read any WARN.
4. Run `check_visuals.py <slug> --stage explorer`. It must print OK.

## Do not

- Edit `phase2_page.*`, a diagram, or `phase2_visuals.json`. A wrong diagram goes in your reply, for diagrammer.
- Add a paragraph. The explorer carries the page, not a second page.
- Add a quiz, a score or a question block. Phase 2 does not test him.

## Model

model: inherit. effort: high. The failure is a flashy widget that teaches nothing, or a widget that shows a server reply the page never gave.
