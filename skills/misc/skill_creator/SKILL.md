---
name: skill_creator
description: >-
  misc skill. creates a new skill, or sharpens an existing one, to our house rules
  (.rules/skill-authoring.md): snake_case name, description in a >- block with trigger words,
  model and effort set, fork only when it helps, short body, tested. cloned from Anthropic
  skill-creator and adapted. use when the user says create a skill, make a skill, new skill,
  turn this into a skill, improve this skill, fix skill triggering, test a skill, validate a skill,
  or /skill_creator.
model: inherit
effort: high
---

# skill_creator

Make or improve one skill. Follow `.rules/skill-authoring.md`. Check with `python skills/scripts/validate_skill.py <skill_dir>`.

Origin: Anthropic `skill-creator`, commit 683bc88 (Apache 2.0, `LICENSE.txt` kept). Changes are in `references/CHANGES.md`. The full upstream text is `references/upstream_SKILL.md`. Read it when you run evals or tune triggering.

## Steps

1. **Capture intent.** If the chat already holds a workflow he wants kept, pull the steps, the corrections he made, and the output format from it first. Then confirm four things: what it does, what he says to trigger it, what it outputs, and whether it needs test cases. Ask one question at a time.
2. **Find the home.** Pick the folder from the rule: `skills/misc/<name>/`, `skills/phase_N/skills/<name>/`, or `.github/skills/<name>/` for an app slash command. Name it in snake_case. Check `REPO_MAP.md` first. Do not duplicate a skill that exists. Extend it.
3. **Ground it.** If the skill depends on an outside tool, API, or spec, open the original documentation now. Cite it in the skill with a date and a score 1 to 5 (`.rules/grounding-and-confidence.md`).
4. **Choose fork or inline.**
   - Fork (`context: fork`, plus `agent:`) when the work is noisy, independent, or must not be biased by the chat. The subagent sees none of the conversation, so the body must hold every path, input, and output location.
   - Inline when the skill needs the chat, asks questions, or is only guidance.
   - Side effects (move, delete, send) get `disable-model-invocation: true`, a plan first, and undo.
5. **Write `SKILL.md`.**
   - Front matter: `name`, `description: >-` with trigger words and `/name`, `model`, `effort`.
   - Body: under 500 lines. Imperative. Say why. Say what not to do. Say where output goes (`Artifacts/` only, HTML only).
   - Heavy detail goes to `references/`. Repeated deterministic work goes to `scripts/`.
   - Template: `assets/skill_template.md`.
6. **Validate.** `python skills/scripts/validate_skill.py <skill_dir>` must print OK. Fix every error. Read each warning.
7. **Test.** Write 2 or 3 real prompts, the kind he would type. Save them in `evals/evals.json` inside the skill folder. Run each with the skill and without it, as separate forked subagents with full briefs, in the same turn. Compare. Objective skills get assertions. Taste skills get his eyes. Details: `references/upstream_SKILL.md`, sections on running, grading, and the viewer.
8. **Improve.** Generalize from the failures. Do not overfit to the test prompts. Cut what does not earn its place. If every test run wrote the same helper script, move it to `scripts/`.
9. **Tune triggering.** If it does not fire, add the words he actually used to the description. Lean a little pushy. Upstream has `scripts/improve_description.py` and `run_loop.py` for an eval loop. They need the `claude` CLI.
10. **Register.** Run `python skills/scripts/repo_map.py`, then `--check`. It must print OK.
11. **Report in chat.** Path, the trigger words, fork or inline and why, validator result, what the tests showed, what is unverified. Short.

## Use upstream scripts with care

- `scripts/quick_validate.py` and `scripts/package_skill.py` enforce the open spec: hyphen names and a short list of fields. Our rule uses snake_case. Use `validate_skill.py` here. Use `package_skill.py` only to export for claude.ai or the API, after renaming the skill to hyphens and removing the Claude Code only fields.
- `eval-viewer/generate_review.py` makes the review page. Use `--static <path>` when no browser opens. The viewer is a tool, not a deliverable. It stays under the skill's workspace folder.
- Put eval workspaces in `Artifacts/artifacts/<skill_name>-workspace/`, not next to the skill.

## Do not

- Do not use Title Case names, a one-line description, or a missing `model` and `effort`.
- Do not fork a skill that needs the conversation.
- Do not write a skill longer than it needs. Brevity applies (`.rules/brevity.md`).
- Do not touch other skills while making one. Mention a problem you see. Do not fix it unasked.
