# Phase 4

Two roles. They do not share a job.

```text
phase 1 map, phase 2 page, phase 3 exam
        |
        v
logger            reads the harness. writes nothing
        |
        v
diagnostician     shared root, mentor, one route back
        |
        v
harness_clerk     files the artifacts that exist
```

| Path | Job |
| --- | --- |
| `RULES.md` | Mentor and filer. Saraev's root-mistake rule. |
| `skills/diagnostician/` | The skill |
| `skills/harness_clerk/` | The skill. Not `context_clerk`. |
| `.grok/agents/diagnostician.md` | The agent |
| `.grok/agents/harness_clerk.md` | The agent |
| `study_os/topics/<slug>/` | The topic folder the clerk keeps |

```text
/workflow phase-4 {"slug":"aws_oidc_flow"}
```

`CHECK.md` is the request, split into parts, checked twice.
