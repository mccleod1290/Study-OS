---
name: karpathy_agents_md
description: >-
  misc skill. audits AGENTS.md against the Karpathy-style guidelines (think before acting,
  simplicity, surgical changes, goal-driven) and rewrites it short and sharp, keeping every
  project fact. use when the user says karpathy, reform agents.md, tighten agents.md,
  audit agents.md, or /karpathy_agents_md.
model: inherit
effort: medium
---

# karpathy_agents_md

Audit `AGENTS.md`. Reform it in the Karpathy style. Keep the project facts. Cut the rest.

## Ground first
1. Open https://github.com/multica-ai/andrej-karpathy-skills (`CLAUDE.md`). Diff it against `references/karpathy-guidelines.md`. If it changed, update the reference and say so.
2. The repo is a secondary source: a community distillation, not Karpathy's own text. Cite it as such, score 3. Do not claim "Karpathy says" without saying that.

## Steps
1. Read `AGENTS.md`, `.github/copilot-instructions.md`, `REPO_MAP.md` header, and `.rules/` file names.
2. Score `AGENTS.md` against the four principles, 1 to 5 each, with the line that earns or loses it:
   - Think before coding: does it make the agent state assumptions and ask when unclear?
   - Simplicity first: any speculative or duplicate rule? any rule the rules files already hold?
   - Surgical changes: does it forbid drive-by edits, and say what the agent must not touch?
   - Goal-driven: does each instruction come with a check? (`repo_map.py --check` is one.)
   - Plain writing: does it point to `.rules/writing-and-web.md`, and is it itself written in plain short sentences?
   - HTML output: does it point to `.rules/html-deliverables.md`?
3. List facts that must survive: paths, commands, consent gate, read-only folders, the pointers to `.rules/`. Nothing here is dropped.
4. Rewrite as a short numbered list. Rules:
   - One line per rule. Imperative. A command or path in backticks.
   - Point to `.rules/` files. Do not copy their text.
   - Add the four principles as four lines, in the project's own words. No quotes of the repo.
   - Add one verify step per instruction where a check exists.
   - Brevity budget: `AGENTS.md` at most 40 lines.
5. Write the new file only after showing a before and after diff summary. Save the old one as `Artifacts/artifacts/agents-md-history/AGENTS.<date>.md`. Never overwrite without that copy.
6. Run `python skills/scripts/repo_map.py` then `--check`. It must print OK.
7. Reply: scores before and after, what was cut, what was kept, the source and its score.

## Do not
- Do not invent rules he did not set. Keep his wording where it is already short.
- Do not touch `.rules/`, skills, or user documents. Only `AGENTS.md`, and `.github/copilot-instructions.md` if it duplicates.
- Do not produce a PDF. If a report is asked for, one short HTML under `Artifacts/artifacts/agents-md-history/`.
