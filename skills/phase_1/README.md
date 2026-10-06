# Phase 1

**The target, then the map.** Two skills. The clerk between them only freezes his words.

```text
book, course, or work material
        |
        v
interviewer
  zero:  no quiz. computer literacy only. copy-paste is not skill
  known: drill, then only what he could produce
        |
        v
context_clerk  ->  CONTEXT.md     adds nothing
        |
        v
map_maker    ->  MAP.md         parts, dependencies, stuck points
             ->  MAP.html       interactive mind map, learn alone or with AI
        |
        v
phase 2 explainer reads MAP.md and TARGET.md
phase 3 exam reads that same map and the phase 2 page
phase 4 logger, then diagnostician, then clerk, reads the phases before it
```

| Path | Job |
| --- | --- |
| `RULES.md` | Saraev's interviewer and map maker, plus the two modes |
| `PACKET.md` | The only field list |
| `skills/interviewer/` | The two modes |
| `skills/context_clerk/` | Freeze. Not a third phase |
| `skills/madhura-extraction-system-v1/` | Intake for book, video, and course modes. Run before `map_maker`. See `map_maker/references/INTAKE.md` |
| `skills/map_maker/` | The map and the interactive mind map |
| `skills/map_maker/references/` | Mind map pattern, study modes, decisions, book and video examples |
| `skills/scripts/build_mindmap.py` | Validates and builds `MAP.html`. Deterministic |

```text
/interviewer
/workflow study-map {"slug":"aws_oidc_flow"}
```
