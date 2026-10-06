# Packet

One field list for phase 1. Skills point here.

`<slug>` is lowercase words joined by underscores.

## TARGET.md

The interviewer writes this. The final target.

```text
topic:
slug:
kind: book | course | work
title:
path:            # file path, or missing
done_when:       # what acquire or do means for this material
```

## interview.md

```text
topic:
slug:
mode: zero | known
floor:           # zero mode: computer_literacy
objective:
work_items:
target:          # path of TARGET.md
exposure:        # copy-paste or googling. not competency
transcript:      # known mode only. Q, his answer, gap | hit
stopped:         # not-quizzed | early | cap | time
inferences:      # not facts
```

`mode: zero` means no subject question was asked.

## CONTEXT.md

The clerk writes this. Nothing added.

```text
topic:
slug:
mode:
floor:
objective:
work_items:
target:
from_him:
from_files:
exposure:        # kept, labeled not competency
gaps:            # only misses in the transcript
dropped:
```

## MAP.md

```text
topic:
slug:
target:
domains:
prerequisites:
acquired:        # empty in zero mode unless a file shows the skill
stuck:           # where people usually get stuck, each with a source
order:           # foundation, then adjacent, then the dive
sources:         # claim, url, grounded
ungrounded:
handoff:         # explainer not run
```

## mindmap.json

Source of `MAP.html`. Same domains and order as MAP.md.

```text
title, subtitle, slug, mode
study_mode: audit | book | video | course | work
ui:        optional wording: anchors, anchor, critical, why, feeds, learner, context, labels, prompts
sources:   key -> {t, u | ref}   # u = opened https page. ref = chapter, pages, or timestamp range
controls:  id -> text           # work items the target is judged on
tree:      node
node:      id, t (title), s (summary), w (why it matters),
           lv (foundation | core | dive), c (control ids),
           src (source keys), ungrounded (optional),
           from (case | transcript | repo, optional), k (children)
```
