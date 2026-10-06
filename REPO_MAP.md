# REPO MAP

Read this first. It says where everything is. Regenerate with `python skills/scripts/repo_map.py`. Do not edit by hand.

## Rules of the house

- Rules: `.rules/`. Read `.rules/artifacts-and-sessions.md` before writing any file.
- All AI output goes under `Artifacts/`. Deliverables are HTML. Topic folders have no dates in names.
- Skills live under `skills/`. Scripts live under `skills/scripts/`. Hooks config is `.github/hooks/study-os.json`.
- Source case documents (his input, private) are in `user-input-learning-text/`. Read only. Never move or edit.

## Skills

| skill | path | what it does |
|---|---|---|
| `tidy` | `.github/skills/tidy/SKILL.md` | slash command /tidy. cleans up the study folder. moves every deliverable and stray file into Artifacts/artifacts/<topic_slug>/ per .rules/artifacts-and-sessions.md, then reports in chat where each fil... |
| `karpathy_agents_md` | `skills/misc/karpathy_agents_md/SKILL.md` | misc skill. audits AGENTS.md against the Karpathy-style guidelines (think before acting, simplicity, surgical changes, goal-driven) and rewrites it short and sharp, keeping every project fact. |
| `learn_from_sessions` | `skills/misc/learn_from_sessions/SKILL.md` | misc skill. reads the session logs and documents how the user works with the AI: how he nudges, what he really means, his taste, his expectations, how he gets things done. |
| `skill_creator` | `skills/misc/skill_creator/SKILL.md` | misc skill. creates a new skill, or sharpens an existing one, to our house rules (.rules/skill-authoring.md): snake_case name, description in a >- block with trigger words, model and effort set, fork ... |
| `context_clerk` | `skills/phase_1/skills/context_clerk/SKILL.md` | phase 1 freeze. pulls interview.md into CONTEXT.md and adds nothing. copy-paste exposure stays exposure. |
| `interviewer` | `skills/phase_1/skills/interviewer/SKILL.md` | phase 1 interviewer. takes a book, course, or work material as the target. ground zero and ground minus 100 mean computer literacy only, and copy-paste work is not skill. |
| `madhura-extraction-system` | `skills/phase_1/skills/madhura-extraction-system-v1/skills/madhura-extraction-system/SKILL.md` | Madhura's complete knowledge extraction system for ANY content she wants to process into structured notes. |
| `map_maker` | `skills/phase_1/skills/map_maker/SKILL.md` | phase 1 map maker. maps parts, dependencies, and stuck points from the target and CONTEXT.md. |
| `brevity_is_the_soul` | `skills/phase_2/skills/brevity_is_the_soul/SKILL.md` | phase 2 length pass on PAGE.md. NEVER CONFUSE EXPLANATION WITH FLUFF. a new term gets two or three sentences, what it is and how it works. |
| `frugal_judge` | `skills/phase_2/skills/frugal_judge/SKILL.md` | phase 2 judge. reads RULES.md and CRITERIA.md and writes EVAL.md. checks the page for assimilation, not for a quiz. |
| `ideas_skill` | `skills/phase_2/skills/ideas_skill/SKILL.md` | phase 2 order for a study page. first principles by default. second-order only when the next event is the lesson. |
| `reduce_ambiguity` | `skills/phase_2/skills/reduce_ambiguity/SKILL.md` | phase 2 ambiguity pass. finds where a new learner will stumble and adds examples, diagrams, flowcharts, svg, sourced images, code, and a reference blog. |
| `writer_skill` | `skills/phase_2/skills/writer_skill/SKILL.md` | phase 2 sentences for PAGE.md, in mccleod1290's voice. wording only. does not choose the order. |
| `academic_paper` | `skills/phase_3/skills/academic_paper/SKILL.md` | phase 3 academic papers. topics come from the phase 1 map. the phase 2 page has to support the question. |
| `examiner` | `skills/phase_3/skills/examiner/SKILL.md` | phase 3 examiner. topics come from the phase 1 map, cited from the phase 2 page. three academic papers, one build brief, emails them, and starts a spar only in the live session. |
| `practical_build` | `skills/phase_3/skills/practical_build/SKILL.md` | phase 3 practical exam. the brief is one work item from the phase 1 map, aimed at the target. |
| `socratic_spar` | `skills/phase_3/skills/socratic_spar/SKILL.md` | phase 3 sparring partner. one Socratic question at a time against the phase 2 page, until the hole in his understanding has a name. |
| `diagnostician` | `skills/phase_4/skills/diagnostician/SKILL.md` | phase 4 diagnostician. finds the shared root behind repeated misses in his prompts, the exam, and the spar. |
| `harness_clerk` | `skills/phase_4/skills/harness_clerk/SKILL.md` | phase 4 clerk. does not write the hook log. reads Artifacts/sessions and files the study OS into one topic folder per subject, with harness timestamps. |

## Workflows

- `WORKFLOW_STUDY.md`: the four phase study, for one learner and one topic.
- `WORKFLOW_EXPERT_CAPTURE.md`: learn from experts through their consented session logs, then make a study topic.

## Documentation

- `Documentation/study_os_guide.html`: how to use, extend and understand the harness. Not a study deliverable. Hand-written, kept outside `Artifacts/`.


## Skill groups

- `skills/misc/` skills: karpathy_agents_md, learn_from_sessions, skill_creator
- `skills/phase_1/` skills: context_clerk, interviewer, madhura-extraction-system-v1, map_maker. files: CHECK.md, PACKET.md, PATHS.md, README.md, RULES.md
- `skills/phase_2/` skills: brevity_is_the_soul, frugal_judge, ideas_skill, reduce_ambiguity, writer_skill. files: CRITERIA.md, PATHS.md, README.md, RULES.md
- `skills/phase_3/` skills: academic_paper, examiner, practical_build, socratic_spar. files: PATHS.md, README.md, RULES.md
- `skills/phase_4/` skills: diagnostician, harness_clerk. files: CHECK.md, PATHS.md, README.md, RULES.md
- `skills/scripts/`. files: build_mindmap.py, learn_due.py, md_to_pdf.py, mindmap_template.html, repo_map.py, send_notes_email.py, tidy.py, validate_skill.py

## Scripts

| script | path | what it does |
|---|---|---|
| `build_mindmap.py` | `skills/scripts/build_mindmap.py` |  |
| `log_deliverables.py` | `skills/scripts/hooks/log_deliverables.py` | Hook: log each deliverable delivered per run (a run = one session). |
| `log_user_inputs.py` | `skills/scripts/hooks/log_user_inputs.py` | Hook: log every user input, verbatim, in one place. |
| `paths.py` | `skills/scripts/hooks/paths.py` | Shared layout for the Study OS hooks. See .rules/artifacts-and-sessions.md. |
| `study_os_hook.py` | `skills/scripts/hooks/study_os_hook.py` | Study OS harness hook. Usage: study_os_hook.py <event>  (JSON payload on stdin). |
| `learn_due.py` | `skills/scripts/learn_due.py` | Is a usage review due? python skills/scripts/learn_due.py [--mark] |
| `md_to_pdf.py` | `skills/scripts/md_to_pdf.py` | Markdown → PDF for Notes vault (WeasyPrint). Usage: md_to_pdf.py IN.md -o OUT.pdf |
| `repo_map.py` | `skills/scripts/repo_map.py` | Regenerate REPO_MAP.md: where every skill, script, rule and artifact lives. |
| `send_notes_email.py` | `skills/scripts/send_notes_email.py` | Email Notes deliverables. Prefer ~/.config/pwnjournal/smtp.env; fallback CVE-brief config.json. |
| `tidy.py` | `skills/scripts/tidy.py` | Tidy the Study OS folder per .rules/artifacts-and-sessions.md. |
| `validate_skill.py` | `skills/scripts/validate_skill.py` | validate_skill.py: check a SKILL.md against .rules/skill-authoring.md. Usage: validate_skill.py <skill_dir/SKILL.md> [...]. Exit 1 on any error. |
| `mindmap_template.html` | `skills/scripts/mindmap_template.html` | template |

## Hooks and rules

- hooks config `.github/hooks/study-os.json`
- rule `.rules/artifacts-and-sessions.md`
- rule `.rules/brevity.md`
- rule `.rules/grounding-and-confidence.md`
- rule `.rules/html-deliverables.md`
- rule `.rules/skill-authoring.md`
- rule `.rules/writing-and-web.md`

## Where deliverables are

- `Artifacts/artifacts/aws-acn-2026-31070/` group of: aws_oidc_flow, identity_and_credentials
- `Artifacts/artifacts/aws_oidc_flow/`
- `Artifacts/artifacts/demo_topic/`
- `Artifacts/artifacts/identity_and_credentials/`
- session logs: `Artifacts/sessions/<YYYY>/<DD-MM>/<HH-MM-SS>_<id>/`

## Common jobs

| I want to | do this |
|---|---|
| build or check a mind map | `python skills/scripts/build_mindmap.py <topic_slug>` |
| tidy the folder | `/tidy` or `python skills/scripts/tidy.py` |
| review how he uses the AI | `skills/misc/learn_from_sessions`, then `python skills/scripts/learn_due.py` |
| turn markdown into HTML or PDF | `python skills/scripts/md_to_pdf.py` |
| refresh this map | `python skills/scripts/repo_map.py` |
