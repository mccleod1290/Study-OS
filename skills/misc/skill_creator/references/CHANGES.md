# Changes from upstream

Upstream: https://github.com/anthropics/skills/tree/main/skills/skill-creator, commit 683bc88e56f3e09ba94f7055977f3d3aa499f202, Apache 2.0 (see `../LICENSE.txt`). Cloned 2026-10-06.

Changed:
- `SKILL.md` is rewritten. The original is `upstream_SKILL.md`, unchanged.
- Name is snake_case (`skill_creator`). Description is a `>-` block with trigger words. `model` and `effort` are set.
- Adds the house rules in `.rules/skill-authoring.md`: fork or inline, snake_case, folded description, size limits, side-effect guard.
- Adds `assets/skill_template.md` and `skills/scripts/validate_skill.py`.
- Output rules: HTML only, `Artifacts/` only, brief, cited and scored.
- Eval workspaces move to `Artifacts/`.

Not changed: `agents/`, `eval-viewer/`, `scripts/`, `references/schemas.md`, `assets/eval_review.html`.
Known gap: `scripts/quick_validate.py` and `package_skill.py` still enforce hyphen names. Use `validate_skill.py` in this repo.
