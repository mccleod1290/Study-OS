# Rule: write plain, ship as HTML

Source: two tips from Andrej Karpathy, given by the user in session on 2026-10-06. Source type: log (his words, relayed). Score 3 until the original post is opened and cited.

## 1. Writing: ASD-STE100, 80% of the way
1. Write explanations in the spirit of ASD-STE100 (Simplified Technical English), a controlled language made for aerospace maintenance documents. Official site: https://www.asd-ste100.org/ (source type: official, accessed 2026-10-06). The spec is stringent, so aim for about 80% of it, not 100%.
2. Habits to apply. These are from model memory, score 2, until checked against the spec:
   - Short sentences. About 20 words for steps, 25 for descriptions.
   - One idea per sentence. One topic per paragraph.
   - Active voice. Present tense. Commands for steps.
   - One word, one meaning. Same term for the same thing every time. Prefer the simple word.
   - Keep the technical names (OIDC, IAM, STS) exact. Explain each at first use.
   - No idioms, no filler, no stacked nouns.
3. The ASD-STE100 spec is copyrighted. Do not copy its dictionary or text into this repo. Apply the style, link to the source.
4. This fits the brevity rule. Plain and short are the same goal.
5. Where the rule bends: exam papers, quoted source text, code. Quote exactly. Do not rewrite a quote.

## 2. Web pages: ask for HTML
1. Output is HTML. LLMs are strong at frontend, so use it: clean layout, interactivity, small animations that explain something.
2. Interactivity must help learning: collapse and expand, tabs, progress, quiz, hover definitions. No decoration without a job.
3. One self-contained file. Print stylesheet. Works offline. See `.rules/html-deliverables.md`.
4. Interactive does not mean long. See `.rules/brevity.md`.
