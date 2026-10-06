# Phase 1 rules

> Overrides, from `.rules/`: deliverables are HTML, PDF only on request (`html-deliverables.md`). Every claim is cited and scored 1 to 5 for confidence (`grounding-and-confidence.md`). Where this file says PDF, produce print-ready HTML. Where it says page count, use words.

**Phase 1 finds the target and where he actually stands.** It does not teach. It does not test.

Saraev's interviewer and map maker, from `2026-10-06-study-os/SARAV.md`. The interviewer gets the real goal, the level, and what done looks like, before any teaching. Vague goals fail. The map maker turns a shapeless subject into parts, what depends on what, and where people get stuck. A rough map beats no map.

## The target

The final target is a book, a course, or a work material he is expected to learn, acquire, or do. That material is the benchmark. A topic name alone is not a target.

## Two modes

`zero` when he says ground zero, ground minus 100, from scratch, or that he will fail every question.

Assume basic computer literacy and nothing else. Work he did by figuring it out, copy-paste, googling, or clicking until it ran is exposure, not understanding. It does not go in `acquired`. Do not quiz him.

`known` when he says he knows it, or he has been doing the work and wants the drill.

Drill until the competency is visible. The map may list as acquired only what he could produce in that drill, or what a file he supplied shows. A claim he did not demonstrate is not acquired.

## The interactive mind map

The map maker also produces `MAP.html`, a beautiful, interactive mind map of every core thing he must know. It is required, not optional.

- Each node is one thing to learn, with a summary, why it matters for the target, and a level: foundation, core, or dive.
- Each node can be learned two ways: independently, through an opened source link (grounded only), or with AI help, through a ready prompt (explain, evidence, quiz me, go deeper).
- It must work offline as one self-contained file: pan, zoom, collapse and expand, search, filters, a learning-path view, per-topic status and notes saved in the browser.
- Nodes tied to work items (here: audit controls) show them, and selecting one lights up the topics behind it.
- No source opened means no link. Unverified nodes are flagged, never dressed up as grounded.
- It follows `MAP.md`: same domains, same order. It does not link to phase 2, 3, or 4.
- Guiding principle: do not replicate point to point. Adapt and deliver as per use case and study mode (audit, book, video, course, work). A video is not a 10 branch map. A book has no audit controls.
- Same input, same output. The build validates and is byte-for-byte repeatable.
- Data lives in `mindmap.json`. Build with `python skills/scripts/build_mindmap.py <slug>`.

## After the map

The handoff is `.grok/rules/study-os-handoff.md`.

`MAP.md` and `TARGET.md` are the phase 1 artifact. Phase 2 reads them and does not invent a curriculum. Phase 3 reads them for its topics, and also reads the phase 2 page. A domain that is not on the map is not on the paper and not in the build.

This phase does not read phase 2, phase 3, or phase 4.

`<slug>` is shared. Underscores. `AWS OIDC flow` is `aws_oidc_flow`.
