---
name: academic_paper
description: >-
  phase 3 academic papers. topics come from the phase 1 map. the phase 2
  page has to support the question. 15 MCQs, 4 short answers at 180 words,
  2 essays at 500 words. key stays on disk. use when the user says academic
  paper, MCQ, short answer, essay test, mark my upload, or /academic_paper.
model: inherit
effort: high
---

# academic_paper

read `skills/phase_3/RULES.md`, `skills/phase_3/PATHS.md`, `skills/phase_1/output/<slug>/MAP.md`, and `skills/phase_2/output/<slug>/PAGE.md`. if the map or the page is missing, stop.

every question is a domain on that map. a domain the map dropped is not on the paper. a question the page cannot support is not a question.

## write

three files. no answers on them.

- `MCQ.md` — 15 questions, four options, one of them right. label them A to D.
- `SHORT.md` — 4 questions. each one tells him to write 180 words. the band is 150 to 200. the question needs a mechanism, not a definition he can fake in a line.
- `LONG.md` — 2 essays. each one tells him to write 500 words. the band is 450 to 600. graduation level means he has to argue how it works and what changes when a condition changes.

`KEY.md` holds the MCQ letter, a 5-line point list for each short, and a 8-line point list for each essay. do not put the key on the paper.

render each paper:

```text
python3 skills/scripts/md_to_pdf.py skills/phase_3/output/<slug>/MCQ.md -o skills/phase_3/output/<slug>/MCQ.pdf
```

same for `SHORT.md` and `LONG.md`.

## mark

when `uploads/` has his answers, write `MARK.md`.

for each short, say if the mechanism is there, and if the length is inside 150 to 200. for each essay, say if the argument holds, and if the length is inside 450 to 600. for each MCQ, right or wrong against `KEY.md`.

name the hole. do not rewrite his answer for him.

## output

the three papers, the pdfs, and `KEY.md`. after an upload, `MARK.md`. do not email the key. do not deliver a build brief. practical_build owns that.

## model

model: inherit. no pinned model id.
effort: high. the failure is a question the map did not list, a question the page does not support, or a key left on the printed paper.
