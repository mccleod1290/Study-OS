# Phase 2 rules

> Overrides, from `.rules/`: deliverables are HTML, PDF only on request (`html-deliverables.md`). Every claim is cited and scored 1 to 5 for confidence (`grounding-and-confidence.md`). Where this file says PDF, produce print-ready HTML. Where it says page count, use words.

**Phase 2 is assimilation.**

The page is how he comes to understand a topic. Depth is how the thing works. Breadth is what it touches. Possibilities are what he can do with it once he sees both. The aim is enough familiarity to do independent work.

The field keeps moving. A page that only quizzes him is useless the month the tool changes. A page that shows the mechanism, the edges, and the ways through is how he stays able to work.

Phase 2 does not test him. No quiz. No workbook. No score. No question block. No check of his fluency.

## What the page is for

- See the depth of the concept.
- See the breadth around it.
- See the possibilities well enough to start the work alone.
- Keep the references, so a later change in the field has a door back to the source.

## What the page must be

- 5 to 10 pages. Smaller inside that band is better. The numbers live in `CRITERIA.md`.
- References in the last section. A link may also sit where a term would stop him.
- Free of ambiguity. A new term is explained in the flow, or it has an example, a picture, or a link.
- Free of jargon that has no gloss.
- First principles. Second-order only when the next event is the lesson.
- Brevity is the soul. Explanation is not fluff. The flow does not stop.
- Simple language. His writing. The voice spec is `.grok/skills/writer-skill/references/PERSONAL_LANGUAGE_SKILL.md`.

## Where the page comes from

The handoff is `.grok/rules/study-os-handoff.md`.

This phase relies on phase 1. It starts only when `skills/phase_1/output/<slug>/MAP.md` and `TARGET.md` are on disk. Section order is the map order. A domain the map dropped does not get a section. The target is the book, the course, or the work material in `TARGET.md`.

This phase does not read the exam. If the map is missing, stop. Do not invent a curriculum.

## Who does the work

The explainer is an agent. It is not a skill. It runs four agents, in this order, each pass:

1. `ideas_skill` — depth, breadth, possibilities
2. `writer_skill` — his sentences, simple language
3. `reduce_ambiguity` — examples, pictures, links
4. `brevity_is_the_soul` — cut the fluff, keep the flow

Then `frugal_judge` reads `CRITERIA.md` and writes `EVAL.md`. It does not teach, and it does not test him.

If the judge is not satisfied, the explainer runs the four again. No sixth pass.

A quiz, a paper, a build brief, or a spar belongs in `skills/phase_3/`. Not here.
