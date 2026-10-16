# Rule: one skill, one context window

Applies to every multi-step run. Set by him on 2026-10-12. Source type: log (his words). Reason: when many phases and skills run in one chat, context rots. The later steps read a thick, stale window and drift.

1. Each phase and each judge runs in its own subagent, with its own fresh context window. The subagent is a physical file in `.claude/agents/`, not a prompt pasted each time. The twin's agents: `phase1_mapper`, `phase2_writer`, `phase2_judge`, `phase2_diagrammer`, `phase2_web_builder`, `phase2_video_maker`, `lab_debriefer`, `hunter`.
2. A skill that must ask him a question stays inline for the questions only (a forked agent cannot ask; `.rules/skill-authoring.md`). It then spawns the agent for the heavy work.
3. The orchestrating skill and the chat keep only paths, verdicts and one short reply per agent. They do not copy page text, source text or logs into the chat.
4. Hand-off is by file, never by memory. An agent reads its inputs from disk and writes its outputs to disk. The files are the memory.
5. The writer is never the judge. The judge never edits the page.
6. An agent file says: what it reads, what it writes, what it must not do, and its reply shape (under 150 words). A new skill that does heavy work gets an agent file in the same change.
7. `python twin/check.py` fails if an agent file is malformed, or a twin skill names an agent that does not exist.
