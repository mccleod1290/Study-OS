---
name: learn_from_sessions
description: >-
  misc skill. reads the session logs and documents how the user works with the AI:
  how he nudges, what he really means, his taste, his expectations, how he gets things done.
  then proposes new skills or sharper existing ones. use when the user says learn from
  sessions, review my usage, how do I use you, self learning, or /learn_from_sessions.
  also run it about every 7 to 10 days. remind him when it is due.
model: inherit
effort: high
---

# learn_from_sessions

you study him, not the topic. the goal is lessons he can use: better prompts, new skills, sharper skills.

## when

run `python skills/scripts/learn_due.py`. it prints DUE or OK. if DUE, tell him at the start of the session: "your usage review is due. about every 7 days, or 10 at most." do not run it unasked, offer it. after a finished review run `python skills/scripts/learn_due.py --mark`.

## read, in this order

1. `Artifacts/sessions/<YYYY>/<DD-MM>/*/inputs.md` and `prompts.md`. his words, verbatim.
2. `actions.md` in the same folders. what the AI did after each prompt.
3. `deliverables.md` and `Artifacts/artifacts/*/HISTORY.md`. what was delivered, and how often a file was redone.
4. the prior review, `Artifacts/artifacts/self_learning/`. do not repeat it. update it.
5. if the hooks are empty or thin, use the host session store: `~/.copilot/session-state/<id>/events.jsonl` has the user and assistant messages and the tool calls. the session_store_sql tool reads the same history. say which source you used.

read the raw logs yourself. a compaction summary is not evidence. never rely on memory of a conversation.

## method

work in this order. do not skip the check.

1. **inventory.** sessions, prompts, date range, deliverables. a line of numbers.
2. **tag every prompt.** one primary tag each: `ask` (new work), `nudge` (steer, tweak, fix), `taste` (says what he likes or dislikes), `rule` (a standing instruction), `question` (understanding), `escalate` (not working, why), `scope` (change the target), `meta` (about the process itself).
3. **intent behind the prompt.** for each recurring pattern write what he said, then what he meant, then what the AI should have inferred. the gap is the lesson. quote the prompt and give its number.
4. **nudge patterns.** how does he correct? short or long, early or late, with a screenshot or a file, a why-question, a praise-then-extend. what did the AI do just before each nudge? count a nudge that repeats as a miss in an existing skill.
5. **taste, dissected.** from his own words: what he praised (and the exact feature), what he rejected, the quality bar (for example "finest", "beautiful", "deterministic"), the format he wants (HTML), the tone (short), the structure he likes (layered levels, trackers, prompts you can paste). list the evidence for each.
6. **expectations.** what does he assume without saying? (a result is verified, a file is logged, a rule is written down, a summary in chat). note each time one was unmet.
7. **how he gets things done.** the loop: how he starts, how he iterates, when he steps in, how he ends. his decision style (picks the recommended option, asks for a choice, delegates). where time was lost.
8. **double check.** reread the raw log for every claim. keep only what has two or more instances or one very strong signal. drop the rest, or mark it `weak`. write one counter-example you looked for. do not write flattering or invented traits. no claim without a quote.
9. **interesting behaviour.** pick the three to five most useful. interesting means: it repeats, it costs him effort, or a skill could remove it.

## output

folder `Artifacts/artifacts/self_learning/` (a topic folder, no dates in names). deliver HTML plus its markdown source:

- `misc_usage_lessons.html` and `.md`. one living document, updated each review. sections: 1) profile in five lines, 2) nudge patterns, 3) intent gaps, 4) taste and bar, 5) expectations, 6) how he works, 7) interesting behaviours, 8) proposals, 9) evidence index, with prompt ids and session folders.
- each lesson has: claim, evidence (quote and id), confidence (strong, medium, weak), and what to do.
- put the review date inside the document and in a `Reviews` table. never in the file name.

## proposals

end with a table. every row is one of two kinds:

| lesson | kind | target | change |
|---|---|---|---|
| he asks for the same layout in every map | sharpen | `skills/phase_1/skills/map_maker` | add rule X |
| he re-explains audit context each session | new skill | `skills/misc/<name>` | purpose, inputs, output |

rules for proposals:
- a **sharpen** names the file and the exact line to add or change.
- a **new skill** names the folder, the trigger, and the output, in two sentences.
- prefer sharpening. a new skill needs a pattern that no existing skill covers.
- do not edit any skill in this run. ask which proposals to apply, then apply the chosen ones.
- if a proposal would only restate a rule in `.rules/`, drop it.

## tone and limits

- plain and kind. this is a study of a work style, not a verdict on a person.
- redact secrets and anything personal that is not about how he works. never quote account ids or keys.
- if there are fewer than about 10 prompts, say so and keep everything `weak`.
- log nothing about his health, family, or employer beyond what the work needs.
