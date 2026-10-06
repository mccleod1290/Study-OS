---
name: practical_build
description: >-
  phase 3 practical exam. the brief is one work item from the phase 1 map,
  aimed at the target. then judges what he uploads. use when the user says
  build brief, practical exam, judge my build, I uploaded the artifact, or
  /practical_build.
model: inherit
effort: high
---

# practical_build

read `skills/phase_3/RULES.md`, `skills/phase_1/output/<slug>/MAP.md`, `skills/phase_1/output/<slug>/TARGET.md`, and the phase 2 page. if the map, the target, or the page is missing, stop.

## brief

write `skills/phase_3/output/<slug>/BUILD.md`.

one work item from the map, aimed at what `TARGET.md` says done looks like. the constraint. what done looks like. small enough for a weekend, large enough that he cannot finish it by copying a paragraph. a domain the map dropped is not the build.

render `BUILD.pdf` with `skills/scripts/md_to_pdf.py`.

do not build it for him.

## judge

when he uploads into `uploads/`, read that work and write `VERDICT.md`.

say what holds, what does not, and the one hole that matters. base it on the page and on what he actually turned in. no score. no praise paragraph.

## output

`BUILD.md`, `BUILD.pdf`, and after an upload `VERDICT.md`. do not deliver the academic papers. do not deliver a spar.

## model

model: inherit. no pinned model id.
effort: high. the failure is a brief he can satisfy by quoting the page, or a verdict that scores a file you did not read.
