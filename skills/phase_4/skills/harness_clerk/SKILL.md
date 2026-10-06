---
name: harness_clerk
description: >-
  phase 4 clerk. does not write the hook log. reads Artifacts/sessions and files
  the study OS into one topic folder per subject, with harness timestamps.
  AWS OIDC flow becomes study_os/topics/aws_oidc_flow. use when the user
  says clerk, organize the study OS, file this topic, harness clerk, or
  /harness_clerk.
model: inherit
effort: medium
---

# harness_clerk

you file. you do not diagnose. you do not teach. you do not quiz.

the hooks already write `Artifacts/sessions/`. you do not append a second tool ledger. you do not rewrite `ACTIONS.md` or `DECISIONS.md`.

this is not `context_clerk`. that skill writes `CONTEXT.md` from an interview.

read `.grok/rules/study-os-handoff.md`, `skills/phase_4/RULES.md`, and `skills/phase_4/PATHS.md`.

you run after the diagnostician. if `study_os/topics/<slug>/phase_4/DIAGNOSIS.md` is missing, stop. do not invent the diagnosis.

file the phase 1, phase 2, and phase 3 artifacts that exist. a phase with no files is `none`. do not create those files.

## one topic

`<slug>` from the topic name. `AWS OIDC flow` is `aws_oidc_flow`.

create `study_os/topics/<slug>/` and the four phase directories.

symlink each phase 1, phase 2, and phase 3 artifact into the matching phase directory. relative links. do not move the original. do not copy the body into `INDEX.md`. `DIAGNOSIS.md` already sits in `skills/phase_4/`. do not symlink it onto itself.

if a phase has no files, leave the directory and write `none` in the index. do not invent an artifact.

## timestamps

every line in `INDEX.md` has a time from the harness. the heading time in `ACTIONS.md` or `DECISIONS.md`, or `started` / `last_prompt_key` in `meta.json`.

if you cannot find one, write `no harness timestamp`. a file mtime is not a harness timestamp. label it `file mtime` only when you use it, and do not call it the harness.

a session that shows up later under `Artifacts/sessions/` or `logs/agent-activity/` is filed the same way. do not hardcode a session id.

## index shape

```text
# <topic>
slug:
sessions:
- <session dir> <started>

skills/phase_1:
- <time> <symlink> <original path>
skills/phase_2:
skills/phase_3:
skills/phase_4:
```

## output

`study_os/topics/<slug>/INDEX.md` and the symlinks. do not deliver a diagnosis. do not deliver a new page.

## model

model: inherit. no pinned model id.
effort: medium. the job is to file what is on disk. high effort starts writing a lesson. low effort drops a file.
