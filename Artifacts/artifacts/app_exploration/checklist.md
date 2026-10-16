# app_exploration: build checklist

goal: one skill that takes a complex web app apart into its functions, and each function into its HTTP requests and parameters. understanding, not attack. no payloads, no fuzzing.
source: his 6 videos, `Digital-Twin/app exploration/` (5 sub recon, 6 intro, 7 basic exploration, 8 exploration, 9 more exploration, 10 conclusion).
started 2026-10-16.

## tools
- [x] ralph-loop plugin (1.0.0) + jq 1.8.2 for its stop hook
- [x] watch plugin (claude-video 0.3.2), WhisperX local transcription (videos have no captions)
- [x] WhisperX on CUDA: torch 2.8.0+cu128 in `~/.cache/watch/whisperx-venv`, model large-v3-turbo float16, saved in `~/.config/watch/.env`. turbo model fetched without symlinks (Windows blocks them without Developer Mode). about 20x faster than CPU small
- [x] babysitter plugin (a5c.ai 6.0.3) + CLI 6.0.0, Node 24
- [x] pinchtab 0.15.2 (npm), skill copied to `~/.claude/skills/pinchtab`
- [x] pinchtab network capture proven on httpbin.org (GET + Fetch). fields: url method status resourceType requestHeaders mimeType. quirks: `--clear` did not clear, `--type a,b` takes one type, `server stop/restart` fail on Windows (they call `ps`): kill the process tree. request bodies not seen yet (no POST sent)
- [x] CDP fallback recorder `scripts/cdp_capture.mjs` written
- [x] CDP fallback proven: records a tab driven by someone else (pinchtab --server or manual clicks). captured both documents + favicon on httpbin. self-drive --open dropped (flaky headless); recorder records, does not drive.

## source
- [x] transcript 5 sub recon
- [x] transcript 6 intro
- [x] transcript 7 basic exploration
- [x] transcript 8 exploration
- [x] transcript 9 more exploration
- [x] transcript 10 conclusion
- [ ] cue frames pulled where he says "look here" or shows a tool
- [x] `source_notes.md` (736 notes, 15 note-taker subagents): his method, per video, with timestamps
- [x] re check 1 (6 videos full length, 0 gaps >60s): `python twin/transcript_coverage.py <runs>`: every video full length, every gap > 60s looked at in frames
- [x] re check 2 (every 5-min window cited, 736 notes): `python twin/transcript_coverage.py <runs> source_notes.md`: every 5 min window cited or skipped with a reason
- [ ] re check 3: each subagent's notes diffed against its transcript: what it left out, listed and fixed

## build team (even slices, no context rot)
- [x] transcripts cut into even ~4000-word chunks (15 slices), one note-taker subagent per chunk, notes by file
- [ ] technique list merged from all chunk notes; every note lands in a technique card (no orphan notes)
- [x] card writers: 8 subagents, 2-3 cards each 2-3 techniques each, balanced by note volume

## skill
- [ ] `/app_exploration` -> lead agent `app_exploration_lead` -> worker agents, 2-3 techniques per worker
- [x] `references/techniques/*.md`: 17 cards written (8-worker team): one card per technique from the videos
- [x] orphan check: 736/736 notes cited (2 consolidation subagents) every note line id cited by a card
- [x] `scripts/norm.py`: captures -> endpoints.md (tested on made-up captures, both formats)
- [ ] `SKILL.md` (inline: gate + questions), `references/method.md`, `references/map_checklist.md`
- [ ] agent `.claude/agents/app_explorer.md`
- [ ] AGENTS.md command table row for `/app_exploration`
- [ ] `python twin/check.py` OK

## reviews
- [x] review 2: babysitter run (gate + adversarial reviewer). 77 -> fixed 6 findings -> 88, converged. +2 post-review fixes (card 13 reframe, POST-body redaction)
- [x] review 3: ralph loop (max 2) + fresh adversarial gate. iter1 86 (2 MED) -> fixed -> iter2 93, no HIGH/MED, all checks pass. promise APP_EXPLORATION_FINAL_CLEAN
- [x] progress.md side note, memory
