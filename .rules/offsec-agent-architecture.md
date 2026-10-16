# Rule: how to build anything in offensive security

Applies to every offsec build, plan or design: hackbots, skills, agents, harnesses. Set by him on 2026-10-16. Source type: log (his words). It has two principles. Both are hard rules.

## Principle 1: one big agent calls many small agents

1. Build as a tree. One lead agent (a slash command or skill) owns the goal and the order of work. It calls 3 to 6 sub agents. It does the work of none of them.
2. Each sub agent is tightly scoped on three things: its tools, its skill, and its context. A sub agent gets only the tools its job needs. It carries one skill. It starts with a clean context window (a forked context), not the chat.
3. Example: hunt for SSRF. The lead agent does not hunt. It calls one sub agent for each micro job (find URL-taking parameters, test one fetch path, test the filters, test the redirects, check the response). Each one works alone, or the lead merges their results.
4. Hand-off between agents is by file or a short result, never by a shared long chat.
5. Do not build one agent that does the whole job. One agent with all the tools and the whole task drifts, loses context and fails quietly.
6. Not every job needs an agent. One prompted call (a "bot": a system prompt and one LLM call) is right for a single-shot job such as subdomain permutations, XSS bypass lists, password mutations. Use an agent only for multi-step methodology or tool calling.

## Principle 2: AI does 90 to 95 percent, the human does 5 to 10 percent

1. The human is a bottleneck when put inside the loop. Do not put him there.
2. For each finding, the agents do their best effort to the end: pivot on coverage, chase the breadcrumbs, validate, write the evidence.
3. The human does two things only: review the finished finding, and give the idea or the next direction.
4. Design for this split: the agents carry validation and the "stay on the rails" checks themselves (scope, rate, stop rules), so the human is not a gate in the middle.

## Limits that do not change

- Scope and authorization stay first: labs, his own machine, or an in-scope program. Agents get the scope as a hard input, and a check that stops any request outside it. That is a design part of the agents, not a human gate.
- The course teaches human-in-the-loop for coverage pivoting, breadcrumb chasing, validation, context engineering and rail monitoring. His view differs. Notes keep the course claim and mark his rule beside it.
- "90 to 95 percent" is his target, not a measured result (grade 1). Test it in the build.
