# intake for book, video, and course maps

for `study_mode` book, video, or course the material is not yet text the map can cite. run Madhura's extraction first. do not edit her skill. it lives at `skills/phase_1/skills/madhura-extraction-system-v1/skills/madhura-extraction-system/`.

## order

1. `interviewer`, then `context_clerk`, as always. `CONTEXT.md` fixes the mode and what he already knows.
2. extraction. read her `SKILL.md`, classify the content, run the pipeline her table names. save each step as a file in `skills/phase_1/output/<slug>/extraction/`, named like her step (`00-section-breakdown.md`, `04-concept-map.md`).
3. `map_maker` reads those files. it does not re-extract.

## what feeds the map

| her step | becomes |
|---|---|
| video `00` section breakdown | domains, in the speaker order. timestamp ranges become `ref` on sources |
| video `01` core message | the root `subtitle` and the first topic of the first domain |
| video `02` full extraction | topic `s` lines and `w` |
| video `03` alpha ideas | `lv: core` or `dive` topics. mark `from: transcript` |
| video `04` concept map | parent and child shape of `tree` |
| video `05` abstract builder | the `deeper` prompt text in `ui.prompts` |
| video `07` and writeup `03` comprehension check | the `challenge` prompt. never drop it. her rule: the check is not optional |
| writeup `01` reverse engineer | `lv: core` topics for how the finding works |
| her honest verdict or signal density | map size. low density gives a small map. do not pad |

her flags carry over. speculation stays labelled. a claim the speaker did not prove gets `ungrounded: true`.

## limits

- her transcript fetch is YouTube only. other sources need his own transcript pipeline. paste the text. do not guess.
- audit mode skips extraction. the case documents are the sources.
- she writes for security content and one learner. her `Step 5` bridge to a study partner is replaced here by phase 2 and 3.
- do not ship her output as the map. the map adds levels, the learning path, status, and the four prompts.
