---
name: ideas_skill
description: >-
  phase 2 order for a study page. first principles by default. second-order
  only when the next event is the lesson. use when the phase 2 loop builds
  PAGE.md, or the user says ideas_skill, first principles on this page, or
  /ideas_skill.
model: inherit
effort: high
---

# ideas_skill

this is the phase 2 pass. the approach file stays `.grok/skills/ideas-skill/references/APPROACH.md`. read it. do not copy it into this file.

## what you write

read `skills/phase_1/output/<slug>/MAP.md` first. if it is missing, stop and write nothing.

read every node of `phase1_mindmap.json`. each domain, topic and anchor gets a place on the page, tagged with its id in curly braces (`{d1}`, `{d1a}`, `{H1}`). a topic can be one line. it cannot be missing. rule: `.rules/phase-order-and-coverage.md`.

the order of `skills/phase_2/output/<slug>/PAGE.md` is the map order, in the blocks in `skills/phase_2/PATHS.md`. a domain the map dropped does not get a section. do not reteach an acquired skill as if it were missing. exposure is not acquired.

each learning section: the parts the result depends on, the condition, when it does not apply, then how.

second-order only in a section where the next event is the lesson.

show the depth, the breadth, and the possibilities. not a second essay. do not add a quiz, a workbook, or a question block. read `skills/phase_2/RULES.md`.

claims come from `SOURCES.md`. a line with no opened url does not go on the page.

## output

`skills/phase_2/output/<slug>/PAGE.md`, the order and the mechanism only. do not deliver the final sentences, the cut, or the examples. writer_skill, brevity_is_the_soul, and reduce_ambiguity own those.

## model

model: inherit. no pinned model id.
effort: high. the failure is a section that starts with the procedure, or a next-event line on every section.
