# Mind map: pattern, principle, and determinism

## Guiding principle

**You should not replicate point to point, but adapt and deliver as per use case and study mode.**

The audit map (`skills/phase_1/output/aws_oidc_flow/`) is the reference, not a mold. Copy what serves the learner in this mode. Rename, drop, or replace the rest. See `MODES.md`.

## Keep: what he liked, and why it works

| # | Feature | Why it earns its place | Keep when |
| --- | --- | --- | --- |
| 1 | Interactive single-file HTML | Works offline, no install, he can pan, search, collapse | always |
| 2 | Learning path as 5 to 10 branches | A shapeless subject becomes a sequence | the subject has 5+ parts. A 3-part video gets 2 or 3 branches, not 10 |
| 3 | Anchors (audit controls) linked to topics | Learning is tied to the work he is judged on | the target has a checklist, labs, claims, or exam objectives. No anchors, no tab |
| 4 | Level split: foundation, core, deep dive; anchor-critical badge | He sees what to do first and what to skip | always |
| 5 | Per-topic status: To learn, Learning, Got it | He owns the progress, nothing is scored by us | always |
| 6 | Mind-map view with collapse and search | One picture of the whole target | always |
| 7 | Overall percent ring | Motivation, honest count | always |
| 8 | Learn it yourself (opened sources) plus Learn with AI (four prompts) plus My notes | A topic is complete: read, ask, write | always. This is the core feature |

## Adapt: what changes by mode

Set these in `mindmap.json` `ui`. The template reads them. No template edit needed.

- `anchors`, `anchor`, `critical`: what the gold badge means (audit controls, labs, key claims, exam objectives).
- `why`: the heading over the "why it matters" line.
- `learner`, `context`: who is asking and about what. Goes into every prompt.
- `prompts` and `labels`: the four AI prompts (explain, evidence, challenge, deeper). Rewrite them for the mode. Keep four, in that role order.
- sources: a link (`u`, https, opened) or a reference (`ref`: chapter and pages, or a timestamp range).

## Deterministic contract

Same inputs, same `MAP.html`, byte for byte.

1. All content lives in `mindmap.json`. The template has no content.
2. `python skills/scripts/build_mindmap.py <slug>` validates, then builds twice and compares. It exits 1 on any error. It prints a sha256. Same json plus same template gives the same hash.
3. No clock, no random ids, no network at build or run time.
4. Node ids are lowercase `d1`, `d1a`, `d1b`. Domains are `d1..dN` in `MAP.md` order. Topics are letters in learning order.
5. Order inside a domain is foundation, then core, then dive. Order across domains is the `MAP.md` order.
6. Authoring rules for the json, so two runs write the same file: one `s` (summary) of at most two sentences. One `w` (why) of one sentence. A topic name is a noun phrase, 1 to 5 words. A source is linked only if it was opened.
7. `ungrounded: true` when no source was opened. `from: "case"` or `"transcript"` when the node comes from his own files.
8. The validator is the eval. There is no eval agent, because a script gives the same verdict every time. Fix every ERROR. Read every warn.

## Check before you hand it over

1. Validator exit code 0, warnings read.
2. Build twice. Same sha256.
3. Open `MAP.html`. Click a node. Press Copy prompt. Change a status. Reload. The status stays.
4. The domain count equals the count in `MAP.md`.
5. No link to phase 2, 3, or 4.
