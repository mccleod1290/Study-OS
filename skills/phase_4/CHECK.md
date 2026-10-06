# Prompt broken into parts

Source: the phase 4 request. Pass 1 is the list. Pass 2 is filled after the files exist.

## Pass 1

1. Two separate roles. Each is a skill grounded by an agent.
2. Diagnostician reads the prompts he gave.
3. Finds the weakness. Mentor, not a scold.
4. Names the pain point.
5. Gives practical remediation steps.
6. Can send him back through phase 3.
7. Can send him back through phase 2 or phase 1. This is the last phase, so the route can be any earlier phase.
8. Built from Saraev's diagnostician. Same mistake, shared root. Last many sessions. The leap from X to Y because Z is missing. Learn Z once.
9. Clerk does not replace the hooks. The harness already logs.
10. Clerk reads those logs and files the study OS by topic folder.
11. Example shape: AWS OIDC flow is one folder. Artifacts inside it. Timestamps come from the harness.
12. Existing sessions and later sessions use the same rule.
13. Do not mix this clerk with `context_clerk`.
14. Do not put a quiz on the phase 2 page.

## Pass 2

Checked against the files after the build. All 14 lines from pass 1 are in the skills, the rules, or the agents.

1. Met. `diagnostician` and `harness_clerk`, each a skill plus an agent.
2. Met. He reads `model/DECISIONS.md` for the prompts.
3. Met. Shared root, mentor language in `RULES.md`.
4. Met. `pain:` in `DIAGNOSIS.md`.
5. Met. `remediation:` is a concrete step.
6. Met. Route `skills/phase_3` sends him through the exam again.
7. Met. Routes `skills/phase_1` and `skills/phase_2` are in the same table. One route only.
8. Met. Saraev's leap from X to Y because Z is missing. Session count is however many exist, not a fake 100.
9. Met. The clerk does not append to `ACTIONS.md`.
10. Met. `study_os/topics/<slug>/` with symlinks. Originals stay in their phase folders.
11. Met. `aws_oidc_flow`. Time comes from the harness heading or `meta.json`.
12. Met. A later directory under `Artifacts/sessions/` or `logs/agent-activity/` uses the same rule.
13. Met. Named `harness_clerk` so it is not `context_clerk`.
14. Met. Phase 4 does not write a quiz onto the phase 2 page.

Second look, same list. No line was only in the README. The route table is in `RULES.md`. The file shape is in `PATHS.md`. The agents only point at those skills.

## Handoff

The order is logger, then diagnostician, then clerk. The workflow is `.grok/workflows/phase-4.rhai`. The script stops unless the logger read `Artifacts/sessions/LATEST.md` and `skills/phase_1/output/<slug>/MAP.md`. Phase 2 and phase 3 are read when they exist. The chain for all four phases is `.grok/rules/study-os-handoff.md`.

## Path correction

Phase 1 originals are `skills/phase_1/output/<slug>/`. Item 10 still holds: symlinks, and the original stays in the phase folder that wrote it. The earlier line that named `study-os/runs/` is retired.
