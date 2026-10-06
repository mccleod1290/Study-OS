# Karpathy-style guidelines (reference copy)

Source: multica-ai/andrej-karpathy-skills, `CLAUDE.md` and `skills/karpathy-guidelines/SKILL.md`
https://github.com/multica-ai/andrej-karpathy-skills (commit 2c606141936f1eeef17fa3043a72095b4765b9c2, accessed 2026-10-06).
Source type: secondary. It is a community distillation of Andrej Karpathy's public remarks on LLM coding pitfalls. It is not written by him.
Confidence 3 for "this is what Karpathy said". Confidence 5 for "this is what the repo says".
Re-open the repo and diff against this copy before each run. Update this file if it changed.

## 1. Think Before Coding
Don't assume. Don't hide confusion. Surface tradeoffs.
- State assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them. Don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what is confusing. Ask.

## 2. Simplicity First
Minimum code that solves the problem. Nothing speculative.
- No features beyond what was asked.
- No abstractions for single-use code.
- No flexibility or configurability that was not requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

## 3. Surgical Changes
Touch only what you must. Clean up only your own mess.
- Don't improve adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style.
- Mention unrelated dead code. Don't delete it.
- Remove imports, variables, functions that YOUR change orphaned.
- Test: every changed line traces to the request.

## 4. Goal-Driven Execution
Define success criteria. Loop until verified.
- "Add validation" becomes "write tests for invalid inputs, then make them pass".
- "Fix the bug" becomes "write a test that reproduces it, then make it pass".
- For multi-step tasks, state a short plan: step, then verify.
- Weak criteria ("make it work") force constant clarification.

Working signs: fewer unnecessary changes in diffs, fewer rewrites from overcomplication, clarifying questions before implementation.

## 5. Writing (from the user, relayed)
Ask for explanations in ASD-STE100, or "80% of the way" there. Full rule: `.rules/writing-and-web.md`.

## 6. Web pages (from the user, relayed)
Ask for output in HTML for a clean interactive page. Full rule: `.rules/html-deliverables.md`.
