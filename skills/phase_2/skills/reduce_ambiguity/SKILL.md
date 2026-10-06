---
name: reduce_ambiguity
description: >-
  phase 2 ambiguity pass. finds where a new learner will stumble and adds
  examples, diagrams, flowcharts, svg, sourced images, code, and a reference
  blog. core line: reduce ambiguity by giving as many examples as possible
  to facilitate a smoother learning curve. use when the phase 2 loop fills
  PAGE.md, or the user says reduce ambiguity, flowchart, worked example,
  or /reduce_ambiguity.
model: inherit
effort: high
---

# reduce_ambiguity

**"reduce ambiguity by giving as many examples as possible to facilitate a smoother learning curve."**

prose length stays in brevity_is_the_soul. this skill adds the artifact beside the short gloss. it does not add a paragraph.

## where he will struggle

read `SOURCES.md` and the page. mark a spot when the term is new, the next step is a flow he cannot see, the mechanism is code, or three sentences would still leave a mystery.

## what to add

at each marked spot, as many of these as that spot needs:

- a worked example, with inputs and the result
- a second example that changes one condition, when the first is the happy path
- a flowchart, diagram, or inline svg when the order is the point
- an image from a page you opened, with the url under it
- a short code block when the mechanism is code
- a reference link when mystery remains

do not invent an image url.

each url also goes in the last section, `## references`, one line on what it settles.

do not add a quiz, a workbook, a score, or a question block. phase 2 does not test him. read `skills/phase_2/RULES.md`.

## output

`skills/phase_2/output/<slug>/PAGE.md` with the examples, the pictures, and the reference list. do not deliver a longer explanation. do not deliver a verdict. frugal_judge owns that.

## model

model: inherit. no pinned model id.
effort: high. the failure is a bare section, or a gallery on a term he already knows, or a quiz slipped into the page.
