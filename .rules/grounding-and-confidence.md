# Rule: ground it, cite it, grade it

Applies to every answer in chat, every lesson, and every deliverable. It exists to cut hallucination.

## 1. Ground

1. A technical claim comes from a source opened in this run. Open the original: the vendor's own documentation, the standard, the RFC, the paper, or the author's repository. Not a blog summary when the original exists.
2. A claim about the case comes from the case document. Name the document and the section. A claim about him comes from his logged words. Quote them and give the prompt number.
3. If no source can be opened, say so in the answer. Do not fill the gap from memory and present it as fact.
4. Do not invent URLs, section names, quotes, API names, limits, prices, or console labels. A procedure the model remembers but did not open is graded 2.
5. Say "I don't know" or "not found in the sources" when that is true. It is a valid answer.
6. When two sources disagree, show both. Do not pick one quietly.

## 2. Cite

- Number the citations in the text: `[1]`. Put a **References** section last.
- Each reference: title, publisher, URL, section or heading, date accessed (ISO date), source type.
- Source types: `official` (vendor docs, standard, RFC), `primary` (the paper, the repo, the author), `case` (his case documents), `log` (his session logs), `secondary` (a blog, a talk, a book chapter about the thing), `memory` (nothing opened).
- Cite near the claim, not only at the end. A paragraph with several claims has several citations.
- In chat, keep it short: the claim, then `[1]`, and a short list of links.

## 3. Confidence score: one rubric, 1 to 5, higher is better, never changed per deliverable

| score | name | meaning | how to earn it |
|---|---|---|---|
| 5 | verified | stated in an official or primary source and checked against the page | opened it this run. the claim matches the passage. cite URL and section |
| 4 | sourced | follows from official or primary sources, with a small step | opened two or more passages and joined them. say which |
| 3 | secondary | only a secondary source says it | opened a blog, talk, or book. no official page found |
| 2 | unverified | plausible, from model memory, no source opened | nothing opened. show it as unverified |
| 1 | conflict or unknown | sources disagree, or none found | show it as an open question. not as a fact |

Rules for the grades:

- Every claim in a deliverable carries a grade, or sits in a section that carries one. Mixed sections grade each claim.
- Never raise a grade without opening a source. Lower it when unsure.
- 2 and 1 are never written as plain fact. They get the badge and the words "not verified" or "open question".
- A deliverable shows its tally: how many claims at each grade. A reader sees the weak spots first.
- In the HTML, the badge is the same everywhere: `5` green, `4` teal, `3` amber, `2` orange, `1` red, with the grade name on hover.
- Lessons from logs (`learn_from_sessions`, expert capture) use the same grades: 5 = three or more instances or confirmed by the person, 4 = two instances, 3 = one strong instance, 2 = a guess, 1 = contradicted by the log.
- A mind map node with `ungrounded: true` is 2. A node with a source is graded by its source.

## 4. Check before delivering

1. Count the claims that have no citation. It must be zero, or each one is marked 2.
2. Open each cited link once more. It must still say what you claimed.
3. Write the tally at the top of the deliverable.
4. Say what you could not verify, in one line, in the chat reply.

## Not allowed

- A reference list that was not opened.
- A grade that was not earned.
- A confident tone on a 2 claim.
