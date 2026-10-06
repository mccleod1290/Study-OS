# Study modes

Pick the mode from `TARGET.md` `kind` and the material. Set `study_mode` in `mindmap.json`. Then adapt, do not replicate. Allowed values: `audit`, `book`, `video`, `course`, `work`.

| | audit | book | video | course | work |
| --- | --- | --- | --- | --- | --- |
| Material | case files, controls | a book | one video or a few, as transcript | syllabus with modules | a task, system, or codebase |
| Domains | one per control family or concept layer | chapters grouped into 5 to 8 parts | 2 to 4 segments of the argument | modules | areas of the system |
| Typical size | 40 to 70 nodes | 20 to 60 | 6 to 20 | 20 to 50 | 15 to 40 |
| Anchors | audit controls | labs, exercises, chapter goals | key claims | exam objectives | acceptance items |
| Evidence prompt becomes | how to collect audit evidence, pass or fail, finding line | a safe lab exercise | where is this said (timestamp), who else agrees | a practice task | how to show it works |
| Sources | opened docs (`u`) | chapter and pages (`ref`) plus an opened page where one exists | timestamp range (`ref`) | module and lesson (`ref`) | files and docs (`ref` or `u`) |
| `from` | `case` | none | `transcript` | none | `repo` |

## audit

Reference: `skills/phase_1/output/aws_oidc_flow/mindmap.json`. Use when he must judge a system against controls. Anchors are the controls. The "why" line says how it affects the audit. Keep all 8 features.

## book (example: reading a web pentest book)

Example: `examples/book_web_pentest/`.

- Domains are parts of the book, not chapters one for one. Group chapters that depend on each other.
- A node is an idea the chapter needs him to hold, not a chapter title.
- `ref` carries chapter and page. Add an opened page (OWASP, vendor docs) as a second source where one exists. Never invent a page number. If you have only the table of contents, use the chapter.
- Anchors are the labs or end-of-chapter goals. Keep the gold badge, it ties reading to doing.
- Prompts: the evidence prompt becomes a safe, legal lab exercise on his own machine. Say so in the prompt.
- Drop: the audit wording, "finding", "control".

## video or transcript (example: a lecture, talk, or tutorial)

Example: `examples/video_transcript/`. Input: the transcript file from his extraction pipeline. Put its path in `TARGET.md` `path`. Read it. Do not guess what the video says.

- Few domains. A 20 minute video gets 2 to 4 branches, not 10. Size follows the material.
- Segment by what the speaker argues, not by clock time. Each node carries a timestamp range in `ref`.
- Every node from the transcript gets `from: "transcript"`. Anything you add from outside is marked `ungrounded` until a page was opened.
- Always add one dive node, "What the speaker did not prove", flagged ungrounded. A video is one voice.
- Anchors are the speaker's key claims. If there are none, leave `controls` empty. The tab and the badge hide themselves.
- Prompts: the evidence prompt becomes "where is this said, quote the line, who else agrees". The AI must say what it added beyond the transcript.
- Drop: the learning-path overkill, audit wording.

## course

Domains are modules. Anchors are exam objectives. `ref` is module and lesson. Keep the status tracker and the percent ring, they matter most here because it runs for weeks.

## work

For a task, a system, or a codebase he must own. Anchors are acceptance items. Sources are the repo files and docs (`ref`), plus an opened page where one exists. The evidence prompt becomes "how do I show this works".

## Rules for every mode

- Keep all four prompts and the notes box. This is the core feature.
- Size follows the material. Never pad to 10 domains.
- A link is opened or it is not a link. Use `ref` for what he owns but you cannot open.
- A node that no source backs is `ungrounded`. Say so on the node.
- The map does not teach and does not quiz. It points, and it gives him the prompt.
