# Rule: deliverables are HTML

1. Every deliverable is a self-contained `.html` file: one file, inline CSS and JS, no network needed to read it. It opens by double click.
2. Deliver only `.html` by default. A PDF is made only when he asks for a PDF, in that request, for that file. Never by default. Never because a skill used to make one. Even then, deliver the HTML first and treat the PDF as an extra. Never in advance "just in case".
3. Print is covered by HTML. Give the page a print stylesheet (`@media print`) so he can print it. Phase 3 papers he must print and write on are print-ready HTML.
4. Markdown (`.md`) and `.json` sources stay beside the HTML in the same topic folder. They are sources, not deliverables.
5. These are not deliverables and stay `.md`: `REPO_MAP.md`, `AGENTS.md`, `WORKFLOW_*.md`, and files under `.rules/`. They are for agents and for him to read in an editor.
6. If an old skill says to make a PDF or a page count from a PDF, this rule wins. Page count falls back to words: at most 2500 words for a lesson and 5000 for a reference, as set in `.rules/brevity.md`.
7. A deliverable without its HTML is not delivered. The `log_deliverables` hook logs it.
8. Length is capped by `.rules/brevity.md`: 5 to 10 pages at most, lower is better.
