# Rule: how we write a skill

Sources: Agent Skills specification https://agentskills.io/specification (official, opened 2026-10-06). Claude Code skills docs https://code.claude.com/docs/en/skills (official, opened 2026-10-06). Anthropic skill-creator https://github.com/anthropics/skills/tree/main/skills/skill-creator (primary, commit 683bc88). House rules 1, 2 and 3 come from the user. Score 3 for the loader claim in rule 2, because it is his observation and not in the docs.

Make skills with `skills/misc/skill_creator`. Check them with `python skills/scripts/validate_skill.py <skill_dir>`.

## Front matter
1. **Name in snake_case.** `name: learn_from_sessions`. Lowercase letters, digits, underscores. Never Title Case. The name equals the folder name. Note: the open spec allows hyphens and no underscores. If a skill is uploaded to claude.ai, the Skills API, or packaged with `package_skill.py`, rename it to hyphens at export. Inside this repo, snake_case wins.
2. **Description always as `description: >-`.** A plain one-line value can load as a single line. The folded block keeps the whole text as one string. Write it as a block every time.
3. **Put trigger words in the description.** Say what the skill does, then `use when the user says ...`, then the slash command (`/skill_name`). Key use case first. Keep it under 1024 characters (spec limit). Claude Code cuts the listing at 1536 characters, so the end of a long one is lost.
4. **Set `model:` and `effort:`.** Both are Claude Code fields in the docs. `model: inherit` unless the job needs a specific one. `effort`: `low`, `medium`, `high`, `xhigh`, or `max`. Use `low` for lookups and filing, `medium` for routine edits, `high` for audits and design.
5. Other Claude Code fields, only when needed: `disable-model-invocation: true`, `user-invocable: false`, `allowed-tools`, `argument-hint`, `context`, `agent`, `paths`. These are not in the open spec. A claude.ai upload rejects them.
6. A field name must match exactly, hyphens included. Claude Code ignores an unknown field without an error. The validator catches the typo.
7. The first line of the file is `---`. Anything before it turns the whole file into body text.

## Fork or inline
1. `context: fork` runs the skill in a new subagent. The subagent does not see the conversation. The skill body is its whole prompt. Set `agent:` to choose the subagent type. (Source: the Claude Code docs, section "Run skills in a subagent".)
2. **Fork when:** the work is noisy (many file reads, long search), independent (a review, an audit, a scan), or must not be biased by the chat. Examples: `learn_from_sessions`, a code review, a repo scan.
3. **Do not fork when:** the skill needs the chat (a skill that continues a discussion), asks the user questions, or is only guidance (a style rule). A forked skill with no concrete task returns nothing useful.
4. A forked skill must stand alone: full paths, the inputs it needs, the exact output and where to save it. Write the output location in the body.
5. When one skill spawns many subagents, give each its own full brief. Subagents share no context with each other. Pass facts by file, not by memory.

## Body
1. Under 500 lines and about 5000 tokens. Move detail to `references/`. Link each reference from `SKILL.md` and say when to read it. One level deep. Give a table of contents to a reference over 300 lines.
2. Imperative sentences. Say why a step matters. A shouted MUST is a sign the reason is missing.
3. Put scripts in `scripts/` for anything that must give the same result each time. Document inputs and outputs. Print clear errors.
4. A skill with side effects (moves files, deletes, sends, publishes) sets `disable-model-invocation: true`, shows a plan first, and offers undo.
5. Say what the skill must not do. Say where it writes: under `Artifacts/` only (`.rules/artifacts-and-sessions.md`).
6. No malware, no data exfiltration, nothing that would surprise the user. Skill folders named `synced` or `anthropic-skills` are reserved.

## Repo rules that apply to every skill
- Outputs are HTML, not PDF (`html-deliverables.md`). Short (`brevity.md`). Plain writing (`writing-and-web.md`). Cited and scored 1 to 5 (`grounding-and-confidence.md`).
- The skill text is plain too: short sentences, one idea each.
- A skill that quotes an outside source names it, gives the commit or date, and a score.
- Location: `skills/<group>/<name>/SKILL.md`. Phase skills sit in `skills/phase_N/skills/`. Slash commands for the app sit in `.github/skills/`.

## Test and register
1. Run the validator. It must print OK.
2. Write 2 or 3 real prompts. Run them with the skill and without it. Compare. Objective skills get assertions. Taste skills get a human look.
3. Run `python skills/scripts/repo_map.py`, then `--check`. It must print OK.
