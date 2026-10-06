# Phase 3

**The exam.** Practical build, plus three academic papers. The spar looks for the hole. Phase 2 does not do this.

Topics come from `skills/phase_1/output/<slug>/MAP.md`. The question has to be supported by `skills/phase_2/output/<slug>/PAGE.md`. If either file is missing, this phase does not start. A domain the map dropped is not on the paper and not in the build. The gate is `.grok/rules/study-os-handoff.md`.

```text
phase 1 map
  |
  v
phase 2 page
  |
  v
examiner
  |-- academic_paper     MCQ + short 180 + long 500
  |-- practical_build    the brief, then the judgment of what he uploads
  |-- socratic_spar      one question at a time, in the conversation
  |
  v
email the three papers and the brief
he prints, writes, uploads
```

| Path | Job |
| --- | --- |
| `RULES.md` | The two tracks and the word bands |
| `skills/examiner/` | Runs the weekend paper and the mail |
| `skills/academic_paper/` | The three papers, and the mark after upload |
| `skills/practical_build/` | The brief, and the judgment of the build |
| `skills/socratic_spar/` | The spar. Live. Not a subagent. |

```text
/phase_3
/workflow phase-3 {"slug":"sharepoint_tenants"}
```

Four skills is the set. A fifth examiner would only repeat these.
