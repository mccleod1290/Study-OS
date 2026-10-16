# Rule: phase 1 first, then phase 2, and phase 2 covers the whole map

Applies to every study run. Set by him on 2026-10-12. Source type: log (his words).

## 1. Order: phase 1 finishes before phase 2 starts

1. Phase 2 reads the phase 1 map. A map that is still being written is not a map. Phase 2 started early invents a curriculum.
2. When he asks for both phases at once ("spawn both", "run in parallel", "do phase 1 and 2"), start phase 1 only. Wait until it is complete. Then start phase 2. Never run the two in parallel.
3. Phase 1 is complete when all three are true: `phase1_map.md` and `phase1_mindmap.json` exist, `python skills/scripts/build_mindmap.py <slug>` exits 0 with warnings read, and the agent that built it has reported done.
4. Each phase runs in its own subagent. The judge runs in a third one. The agent that wrote the page does not judge it.
5. If the map changes after phase 2 ran, phase 2 runs again. The old page is stale.

## 2. Coverage: every node of the map is on the page

1. Every domain and every topic in `phase1_mindmap.json` has its own place on the page. Every anchor (`controls`, for example H1 to H12 and Q1 to Q5) is covered too. A topic can be one line. It cannot be missing.
2. Tag each one in `phase2_page.md` with its node id in curly braces: `{d1}` on a domain heading, `{d1a}` on its topic, `{H1}` where the hack step is covered. The HTML shows each tag as a small chip.
3. Order follows the map: domains in map order, topics in map order inside the domain.
4. A node the map marks `ungrounded` is still covered. It carries grade 2 and the words "not verified".
5. The check is a script, not a reader: `python skills/scripts/check_coverage.py <slug>`. It must print OK. It lists every missing id and every id that is not in the map.
6. Never cut a node to save words. Cut prose around it (`.rules/brevity.md`, rule 4).

## 3. Length when the map is large

1. The ceiling applies per sub heading (one domain of the map), not per page: 2500 words outside fenced code for each domain section, as in `.rules/brevity.md` rule 10. The whole page has no ceiling. Commands and sample output sit in fenced code.
2. A large map stays one page, with one section per domain. Do not split it to fit a ceiling. Each domain section carries its own word count. Set by him on 2026-10-12, replacing the earlier split-into-two-pages rule.
