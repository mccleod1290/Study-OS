# Paths

`<slug>` is the topic in lowercase words joined by underscores. `AWS OIDC flow` is `aws_oidc_flow`.

```text
study_os/topics/<slug>/INDEX.md
study_os/topics/<slug>/phase_1/
study_os/topics/<slug>/phase_2/
study_os/topics/<slug>/phase_3/
study_os/topics/<slug>/phase_4/DIAGNOSIS.md
```

The phase folders hold symlinks to the real files. Do not move the originals.

Originals stay where their phase wrote them:

```text
skills/phase_1/output/<slug>/         phase 1
skills/phase_2/output/<slug>/         phase 2
skills/phase_3/output/<slug>/         phase 3
```

## Harness

Read, in this order:

1. `Artifacts/sessions/LATEST.md`
2. That session's `meta.json` (`started`, `last_prompt_key`)
3. `tools/ACTIONS.md` and `model/DECISIONS.md`. A line's timestamp is the heading time, the `2026-10-06T10:26:27` form.
4. `Artifacts/sessions/INDEX.md` when the work spans more than one session.
5. `logs/agent-activity/` only when the session ledger has no line for that action.

A later harness is in scope when it appears under `Artifacts/sessions/` or `logs/agent-activity/`. Same rules. Do not hardcode one session id.

## Diagnosis

`study_os/topics/<slug>/phase_4/DIAGNOSIS.md`

```text
root:
pain:
evidence:
- <harness timestamp> <path> <what he did or missed>
remediation:
- <one practical step>
route: skills/phase_1 | skills/phase_2 | skills/phase_3 | none
why:
```
