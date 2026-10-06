# Decisions behind the mind map

Written from the session that built it. Hooks were not firing in this folder (`logs/`, `tools/`, `model/` stayed empty), so these come from the session transcript, not the logs. Re-check when the hooks work.

| Decision | Prompt or finding that led to it | Result |
| --- | --- | --- |
| Interactive HTML mind map is required in phase 1 | "interactive beautiful mind map that lets me know all core things... learn independently or with AI help" | `MAP.html` plus `mindmap.json`, rule in `RULES.md` |
| Data in json, template separate | Hand-written HTML would differ on every run | `build_mindmap.py` injects json into one template |
| Only opened sources become links | Phase 1 audit found three doubtful template checks with no opened page | `ungrounded` flag, `from` marker, validator warnings |
| Per-topic AI prompts, four roles | He called the AI prompt plus notes the core feature | Explain, Evidence, Quiz me, Go deeper, plus notes |
| Anchors tie topics to controls | He called the learning path to controls link "genius" | `c` on nodes, Controls tab, highlight |
| Validator instead of an eval agent | Need the same verdict every run | `build_mindmap.py` exits 1 on error, builds twice, prints sha256 |
| `sort_keys` on json | Same json must give the same bytes | Prompt tab order is fixed in the template, not by key order |
| Template must not say AWS or audit | Reuse for a book or a video | All wording in `ui` |
| Guiding principle: adapt, do not replicate | His instruction | `MINDMAP.md`, `MODES.md`, two small examples |

## Known gaps

- Hooks not confirmed loading. Until they do, this file is the only decision log.
- The book and video examples use placeholder chapters and timestamps. They show shape, not content.
- No transcript pipeline was available here, so the video mode is untested on a real transcript.
