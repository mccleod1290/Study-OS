---
name: tidy
description: >-
  slash command /tidy. cleans up the study folder. moves every deliverable and stray
  file into Artifacts/artifacts/<topic_slug>/ per .rules/artifacts-and-sessions.md,
  then reports in chat where each file went. use when the user says tidy, clean up,
  organise the folder, or /tidy.
model: inherit
effort: low
---

# /tidy

you run a script. you do not decide where files go. the script does, the same way every time.

1. read `.rules/artifacts-and-sessions.md`.
2. run `python skills/scripts/tidy.py` (plan only). read the plan.
3. group related topics. read the topic folders in `Artifacts/artifacts/` and the plan. when two or more topics belong to one case, course, book, or certification (for example ten AWS topics for case ACN-2026-31070), they go in one group folder: `Artifacts/artifacts/<group>/<topic>/`.
   - group name: lowercase, hyphens, subject then id. `aws-acn-2026-31070`, `web-pentest-book`, `aws-saa-course`.
   - record it in `Artifacts/artifacts/_groups.json` as `{"<group>": ["topic_a", "topic_b"]}`. add to the existing file. never drop an entry.
   - the evidence is `TARGET.md` and `CONTEXT.md` (same case id, same book, same course). do not group on topic names alone. a lone topic stays ungrouped.
   - if unsure, ask the user once. the script does the move, you only write the json.
   - re-running `/tidy` files new topics of a known group into it.
4. if there are conflicts, show them and stop. do not overwrite. ask the user.
5. otherwise run `python skills/scripts/tidy.py --apply`.
6. run `python skills/scripts/build_mindmap.py aws_oidc_flow` and open nothing else, to confirm the map still builds from its new place. a missing json is a failure, report it.
7. run `python skills/scripts/repo_map.py` so `REPO_MAP.md` matches the folders.
8. report in chat. never skip this.

## report shape

one line of totals. then a table, one row per topic folder:

| group | topic | from | to | files |
|---|---|---|---|---|

then: conflicts (if any), what was left alone (source case documents, skills, scripts, phase docs, session logs), and the undo command `python skills/scripts/tidy.py --undo`.

## do not

- move source documents such as `user-input-learning-text/AWS - OIDC Case/`.
- touch `Artifacts/sessions/` logs.
- hand-move files. if the script misses a case, say so and propose a change to `skills/scripts/tidy.py`.
