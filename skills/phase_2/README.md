# Phase 2

**Assimilation.** Depth, breadth, and the possibilities. Enough to do the work alone. Not a test.

The curriculum is `skills/phase_1/output/<slug>/MAP.md` and `TARGET.md`. If either file is missing, this phase does not start. It does not read the exam. The gate is `.grok/rules/study-os-handoff.md`.

The law is `RULES.md`. The judge reads `CRITERIA.md`.

```text
explainer agent
  |
  v
ideas_skill -> writer_skill -> reduce_ambiguity -> brevity_is_the_soul
  |
  v
PAGE.md  PAGE.html  PAGE.pdf     references in the last section
  |
  v
frugal_judge
  |
  +-- satisfied --> stop
  +-- not satisfied --> the four again, cap 3, 4, or 5
```

| Path | Job |
| --- | --- |
| `RULES.md` | Assimilation. No quiz. |
| `CRITERIA.md` | What the judge checks |
| `skills/ideas_skill/` | Depth, breadth, possibilities |
| `skills/writer_skill/` | His sentences |
| `skills/reduce_ambiguity/` | Examples, pictures, links |
| `skills/brevity_is_the_soul/` | Cut fluff, keep the flow |
| `skills/frugal_judge/` | The judge. Not a test of him. |
| `skills/diagrammer/` | Visual pass 1: SVG diagrams, `phase2_visuals.json` |
| `skills/web_builder/` | Visual pass 2: the interactive page, `phase2_explorer.html` |
| `skills/explainer_video/` | Visual pass 3: the narrated film and its wrapper |
| `VISUALS.md` | Shared context for the visual pass: order, files, style, checks |
| `output/<slug>/` | The artifact |

## Visual pass

After the judge says satisfied, the page can go three rungs further, after Karpathy (2026-10-02): diagrams, an interactive page, an explainer video. The page stays the source; nothing here edits it. Order, files and checks: `VISUALS.md`.

```text
SATISFIED -> diagrammer -> web_builder  +  explainer_video -> judge, visual checks
```

The explainer is an agent: `.grok/agents/explainer.md`. It is not a skill.

```text
/workflow phase-2 {"slug":"sharepoint_tenants","topic":"SharePoint tenants"}
```
