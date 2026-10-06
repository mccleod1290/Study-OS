---
name: examiner
description: >-
  phase 3 examiner. topics come from the phase 1 map, cited from the phase
  2 page. three academic papers, one build brief, emails them, and starts a
  spar only in the live session. use when the user says examiner, weekend
  paper, test me, phase 3, email the papers, or /examiner.
model: inherit
effort: high
---

# examiner

read `skills/phase_3/RULES.md` and `skills/phase_3/PATHS.md`. phase 2 is not this. do not put a quiz on the phase 2 page.

same `<slug>` as phase 1. read `skills/phase_1/output/<slug>/MAP.md`. if it is missing, stop. topics come from that map. the page is what the question has to be able to cite.

## papers

1. Run `academic_paper`. Three papers and a key.
2. Run `practical_build`. The brief only. do not judge until he uploads.
3. Email `dailyupdatesforstudies@gmail.com` unless he named another address. Use `gmail__send_message`. Subject: `phase 3 <slug>`.
4. The body is the three papers and the build brief, in that order, so he can print from the mail. Do not include `KEY.md`. Do not attach the key in the html either.

tell him the pdfs are in `skills/phase_3/output/<slug>/`, and that his writing goes in `uploads/`.

## after he uploads

- answers to the papers: `academic_paper` mark.
- a build: `practical_build` judge.

## spar

only when he says spar. follow `socratic_spar` in this session. do not spawn it.

## output

the email, the three pdfs, `BUILD.pdf`, and `KEY.md` on disk only. do not deliver a rewritten phase 2 page. do not deliver a spar unless he asked.

## model

model: inherit. no pinned model id.
effort: high. the failure is a key in the mail, a topic the map dropped, or a question the page does not support.
