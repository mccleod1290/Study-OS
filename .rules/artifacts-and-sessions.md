# Rule: artifacts and sessions

Everything the AI produces or logs lives under one root folder: `Artifacts/`. Nothing else is a home for AI output.

```text
Artifacts/
  sessions/                                 logs, one folder per session
    <YYYY>/
      <DD-MM>/                              exactly one folder per day
        <HH-MM-SS>_<session id>/            one folder per session
          inputs.md  inputs.jsonl           every user prompt, verbatim
          prompts.md                        numbered prompt ledger
          actions.md                        every tool call by the agent
          deliverables.md                   files delivered in this run
          meta.json  events.jsonl
    LATEST.md  .index.json                  pointers, written by the hooks
  artifacts/                                deliverables, by topic
    _groups.json                            which topics belong to which group
    <group>/                                optional. related topics, e.g. aws-acn-2026-31070
      <topic_slug>/                         one folder per topic, for its whole life
    <topic_slug>/                           an ungrouped topic
      <phase>_<what>.<ext>
      HISTORY.md                            dated change log, written by the hook
```

## Rules

1. One root. All AI output goes under `Artifacts/`. Scripts, rules and skills stay where they are.
2. Sessions are dated: year, then `DD-MM`, then session. One folder per day, many sessions inside it. Never a second folder for the same day. The hooks create these. Do not hand-make them.
3. Artifacts are not dated. A topic can take weeks or months, so the folder and file names carry no date, no `final`, no `v2`. Dates live inside `HISTORY.md` and the session logs.
4. The artifact folder is the topic slug, lowercase with underscores: `aws_oidc_flow`, `identity_and_credentials`, `web_pentest_book`. The file inside says the phase and kind: `phase1_mindmap.html`, `phase2_identity_and_credentials.html`, `phase3_exam.html`. A change overwrites the same file. The history keeps the record.
5. Related topics are grouped. Ten AWS topics for one case sit in one group folder, `Artifacts/artifacts/aws-acn-2026-31070/<topic_slug>/`. The group name is lowercase with hyphens: subject, then case or course id. The groups are listed in `Artifacts/artifacts/_groups.json`. Group on a shared case, book, or course, never on names alone. `/tidy` does the filing.
6. Exception: `Documentation/` holds guides about the harness itself (HTML, hand-kept). `/tidy` does not touch it. Everything else the AI makes goes under `Artifacts/`.
7. Every deliverable is HTML, never PDF unless he asks. See `.rules/html-deliverables.md`. Source files (`.md`, `.json`) sit beside it in the same topic folder. Grounding and the confidence grades are in `.rules/grounding-and-confidence.md`.
8. The `log_deliverables` hook logs each new or changed file in that run's `deliverables.md` and in the topic's `HISTORY.md`. If a file is not logged, it was not delivered.
9. A session log is never edited or deleted by the AI. Compaction and sub-agent summaries do not replace it. When a summary is unclear, read the session folder.
10. Skills write to `Artifacts/artifacts/<topic_slug>/`. `harness_clerk` reads `Artifacts/sessions/` and files by topic.

## Where things live

Skills are under `skills/`, scripts under `skills/scripts/`. `REPO_MAP.md` lists them. `AGENTS.md` tells every agent to read it. Private source documents are in `user-input-learning-text/` and are git-ignored.

## Hooks that enforce this

`.github/hooks/study-os.json` runs `skills/scripts/hooks/study_os_hook.py` (events, prompts, tool calls), `log_user_inputs.py` and `log_deliverables.py`. `skills/scripts/hooks/paths.py` holds the layout.

## Limits

- Hooks log tool calls and prompts. Hook events do not carry the model's reasoning text. Decisions show only as the actions taken.
- Existing outputs under `phase_N/output/<slug>/` stay where they are. The deliverables hook still watches them. New work goes under `Artifacts/artifacts/<topic_slug>/`.
