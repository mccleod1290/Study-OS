# Criteria

The frugal judge reads this file and no other rubric. Each line is pass or fail. No scores. No test of the reader.

The page limit lives here.

## pages

Read `pages.txt`. It is the PDF page count.

Fail if the count is over 10. Fail if the count is under 5.

5 through 10 can pass. Prefer the smaller count. Do not pad.

## words

Count words in `PAGE.md` outside fenced code.

Fail if that count is over 2000.

## references

The last section of `PAGE.md` is the reference list. Each item is a url that was opened, with one line on what it settles.

Fail if that section is missing. Fail if a factual claim has no url in it.

## depth

Each section shows the parts the result depends on, the condition, and when it does not apply, before the procedure.

Fail if a section opens with the steps.

## breadth

The page shows what the topic touches, not only the one happy path.

Fail if the page is a single procedure with no adjacent possibility.

## possibilities

A reader who has the page can see how to start the work alone.

Fail if the page never shows a use.

## first_principles

The order is parts, conditions, when it does not apply, then how.

Fail if that order is missing.

## second_order

A next-event line appears only where the next event is the lesson.

Fail if every section has one bolted on.

## brevity

A subtype does not get its own paragraph. A new term is at most three sentences. Explanation is not fluff.

Fail if a term owns a page of its own.

## ambiguity

A term that would stop the reader has an example, a picture, or a link in the flow.

Fail if a section is only bare sentences and the term is new.

## flow

The page can be read straight through. A side term does not open a second essay.

Fail if the reader has to leave the point to learn a word.

## plain_language

Sentences are simple. Jargon that has no gloss fails.

## voice

Sentences are his. The voice spec is `.grok/skills/writer-skill/references/PERSONAL_LANGUAGE_SKILL.md`.

Fail if the page is a vendor abstract.

## not_a_test

The page has no quiz, no workbook, no score, and no question block.

Fail if any of those are present.

## budget

After the first check, set the cap from the fail count.

| Fails | Cap |
| --- | --- |
| 0 | stop |
| 1 or 2 | 3 |
| 3 or 4 | 4 |
| 5 or more | 5 |

Stop when every check passes. Stop at the cap even if a line still fails. Write the unmet lines. Do not start a sixth pass.
