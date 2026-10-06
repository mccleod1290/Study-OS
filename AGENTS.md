# Agents: start here

0. Rules that bind every answer: `.rules/grounding-and-confidence.md` (cite original documentation, grade every claim 1 to 5) `.rules/html-deliverables.md` (HTML only, PDF only on request), `.rules/brevity.md` (5 to 10 pages at most, lower is better), and `.rules/writing-and-web.md` (plain ASD-STE100-style writing, interactive HTML).
1. Read `REPO_MAP.md`. It says where every skill, script and rule is. Do not search the tree to find a skill.
2. Read `.rules/artifacts-and-sessions.md` before writing any file. All AI output goes under `Artifacts/`.
3. Workflows are in `WORKFLOW_STUDY.md` and `WORKFLOW_EXPERT_CAPTURE.md`. Follow them. Do not capture anyone without the consent gate.
3b. Harness documentation is in `Documentation/study_os_guide.html`. Update it when hooks, skills, or rules change.
3a. To create or change a skill, use `skills/misc/skill_creator` and follow `.rules/skill-authoring.md`.
4. After you add, move or rename a skill or script, run `python skills/scripts/repo_map.py`. `python skills/scripts/repo_map.py --check` must print OK.
5. `user-input-learning-text/` holds his private source documents. Read only. Never move, edit, or commit them.
