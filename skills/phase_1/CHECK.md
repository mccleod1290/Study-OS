# Prompt broken into parts

Source: the phase 1 request. Checked against `RULES.md`, `PACKET.md`, the two skills, the clerk, and the later phases that have to read the map.

## Pass 1

1. Two skills: interviewer and map maker.
2. The target is a book, a course, or a work material he is expected to learn, acquire, or do.
3. Ground zero or ground minus 100 means computer literacy only.
4. Figuring it out, copy-paste, googling, or clicking until it ran is exposure, not understanding. Azure done that way is the same case.
5. If he says he knows it, drill until the competency is visible.
6. The map lists as acquired only what that drill produced, or what a file he supplied shows.
7. Phase 2, the explainer, is based on this map. It does not invent a curriculum.
8. Phase 3, the exam, takes its topics from this map.
9. Saraev interviewer: real goal, current level, and what has to be true, before teaching. A vague goal fails.
10. Saraev map maker: main parts, what depends on what, where people usually get stuck. A rough map beats no map.

## Pass 2

1. Met. `skills/interviewer/` and `skills/map_maker/`. `context_clerk` only freezes his words. It is not a third phase. `README.md` says so.
2. Met. `RULES.md` and `TARGET.md` in `PACKET.md`. Kind is book, course, or work. A topic name alone is not a target.
3. Met. Mode `zero` in the interviewer skill. No subject question. Floor is `computer_literacy`.
4. Met. That work goes under `exposure`. The map maker does not promote it into `acquired`.
5. Met. Known mode drills in batches of 3, cap 12, stretch 15, 20 minutes. A miss is a gap. No lecture.
6. Met. `map_maker` acquired rule. Zero mode stays empty unless a file shows the skill.
7. Met. `skills/phase_2/RULES.md`, `.grok/agents/explainer.md`, and `ideas_skill` stop when `MAP.md` is missing. Section order is the map order.
8. Met. `skills/phase_3/RULES.md`. Papers, the build brief, and the spar stop when the map is missing. A dropped domain is not a question and not the build.
9. Met. Interviewer skill, from `2026-10-06-study-os/SARAV.md`. "Learn coding" is not the goal if the goal is a timed interview in three weeks.
10. Met. Map maker skill. Stuck points need a source. An unopened claim stays `ungrounded`.

Second look. The two modes are in the skill, not only in the README. The field list is only in `PACKET.md`. Phase 2 and phase 3 name `skills/phase_1/output/<slug>/MAP.md`.

## Handoff

The chain is `.grok/rules/study-os-handoff.md`. Phase 1 `MAP.md` and `TARGET.md` feed phase 2 and phase 3. The explainer reads phase 1. The exam reads phase 1 and `skills/phase_2/output/<slug>/PAGE.md`. Phase 4 is logger, then diagnostician, then clerk, and it reads the phases before it. Each workflow returns `blocked` unless the required file is on disk. The prompt is not the gate.
