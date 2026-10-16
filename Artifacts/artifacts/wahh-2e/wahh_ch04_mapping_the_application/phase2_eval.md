# phase2_eval — wahh_ch04_mapping_the_application

Fresh judgement of the rewritten page (every node now carries its {id} tag). This overwrites the old iteration-2 eval of the prior page.

iteration: 1 (fresh page)
verdict: SATISFIED
fails: 0
cap: stop (0 fails)

## CRITERIA, line by line

| line | result | deciding line |
| --- | --- | --- |
| pages | pass | largest section is "2. Discovering hidden content" at 412 words outside code (< 2500/section) |
| words | pass | every section 169-412 words outside fenced code; my count, not pages.txt |
| coverage | pass | `check_coverage.py`: `OK  47 nodes and 17 anchors covered, in map order` |
| references | pass | last section is `references`; each item is a URL opened with one line on what it settles; every factual claim carries [ref] or an explicit "not verified" |
| depth | pass | each section opens with **Parts/Condition/When not** before any command (e.g. d2 header) |
| breadth | pass | shows adjacent routes: GraphQL, OpenAPI, archives, OAST, OSV, not one happy path |
| possibilities | pass | each node gives a runnable 2026 command the reader can start alone |
| first_principles | pass | order is parts, conditions, when-not, then how, throughout |
| second_order | pass | next-event lines only where they are the lesson (e.g. d2g "archived but 404 live is a route the app once served") |
| brevity | pass | trio format; no subtype owns a paragraph; new terms kept short |
| ambiguity | pass | SSO, OAST, OAD, purl all glossed in flow |
| flow | pass | reads straight through; side terms do not open an essay |
| plain_language | pass | short active sentences; jargon glossed at first use |
| voice | pass | his terse "2011 / broke / 2026 way" cadence, not a vendor abstract |
| not_a_test | pass | Q1-Q5 are the book's review questions answered inline, not a quiz posed to the reader; no workbook, score, or question block |
| budget | pass | 0 fails -> cap is stop |

## Extra checks (spawn prompt)

1. Tags at the explanation site, not a bare heading: PASS. Domain tags {d1}-{d7} sit on section heads with the explained nodes under them; every topic tag ({d1a}..{d7f}, H1-H12, Q1-Q5) sits inline on the sentence that explains that node.
2. Every g2 item says "not verified": PASS. All 8 g2 nodes carry the words — d1g, d2a, d2h, d4a, d5b, d5d, d6c, d7c.
3. `python twin/check.py`: PASS — `OK  3 skills, 8 agents, deliverables within budget`.

## Standing extra checks

- 10 riskiest flags re-opened against docs: ffuf `-ac -fs -rate -e -mc -fc` confirmed; katana `-rl -jc -kf -jsl -cos -em -d` confirmed (`-cos` = crawl-out-scope, correct for excluding logout/delete/admin); nuclei `-as`, httpx `-td -sc -title -rl`, nikto `-404string -404code -Pause`, arjun `--stable` all confirmed.
- 3 "what broke" claims re-opened: Google operators page omits link:/related:/cache: (confirmed), Nikto `-404` replaced by `-404string`/`-404code` (confirmed), ZAP left OWASP 2023 (confirmed, "since August 2023").
- Commands target $TARGET / rate-limited: all scanning commands against $TARGET carry a rate flag (katana -rl, ffuf -rate, nuclei -rl, httpx -rl, nikto -Pause, arjun --stable) EXCEPT feroxbuster. gau/waybackurls/osv/graphql hit passive archives or a vuln DB, not the target.
- HTML: no external `src`; no external `href` (only in-page `#` anchors; reference URLs are plain text); `@media print` present; badge tally g5 26 / g4 6 / g3 3 / g2 8 / g1 0 matches my own count exactly.

## Flags that did not verify

- feroxbuster rate flag. The page says "its rate flag was not in the README (not verified)". feroxbuster does have `--rate-limit` (default 150 rps per its docs). The claim is contradicted, but it is hedged as g3/not verified, so it does not break grounding.

## Fixes (non-blocking; verdict stays SATISFIED)

1. d2e: add `--rate-limit 20` to the feroxbuster command and correct the note — the rate flag exists (`--rate-limit`). This also closes the one scanning command that targets $TARGET without a rate limit.

No node may be cut. The page is SATISFIED; the one fix is an accuracy and safety improvement, not a blocking fail.
