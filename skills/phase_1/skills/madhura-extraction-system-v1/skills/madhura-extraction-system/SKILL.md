---
name: madhura-extraction-system
description: >
  Madhura's complete knowledge extraction system for ANY content she wants to process into structured notes. ALWAYS trigger this skill when Madhura shares: a YouTube URL or transcript, a pasted article or writeup, a blog post, a conference talk transcript, a bug bounty writeup, a security research paper, a self-help video, a technical tutorial, or ANY content she says "extract", "break down", "process", "learn from", "study this", or "what's in this". Also trigger when she pastes raw text without explanation — she wants it processed. This skill OWNS content intake — turning raw material into structured knowledge. Do NOT use this skill for active learning sessions where Madhura is working through concepts with Claude (that's the study-partner skill). The boundary: extraction = processing content INTO notes; study-partner = working through concepts WITH Claude.
---

# Madhura's Knowledge Extraction System

> Turn any content into intel you can act on and skills you can build.

## Step 0 — Acquire the Content

### YouTube URL provided

Extract the video ID (the part after `v=` or after `youtu.be/`), then run:

```bash
pip install youtube-transcript-api --break-system-packages -q && python3 -c "
from youtube_transcript_api import YouTubeTranscriptApi
import sys
video_id = 'VIDEO_ID_HERE'
ytt = YouTubeTranscriptApi()
try:
    transcript = ytt.fetch(video_id)
    text = ' '.join([s.text for s in transcript.snippets])
    print(text)
except Exception as e:
    print(f'ERROR: {e}', file=sys.stderr)
"
```

If that fails, tell Madhura:
> "Transcript isn't available automatically. On YouTube: click `…` below the video → 'Show transcript' → copy all text and paste it here."

### Transcript, article, or writeup pasted directly

Use it as-is. Proceed to Step 1.

---

## Step 1 — Classify the Content

Before writing anything, internally determine:

**Content type** (pick one):
| Type | Signals |
|---|---|
| `hacking-talk` | Conference presentation, live hacking demo, CTF walkthrough, security demo |
| `bug-bounty-writeup` | Reports a specific vulnerability with reproduction steps |
| `security-article` | Teaches a technique, methodology, or research finding in security |
| `self-improvement` | Habits, mindset, productivity, life advice, podcast, interview about growth |
| `technical-learning` | Azure/GCP/cloud, LLM internals, JavaScript, programming concepts |
| `research-paper` | Academic or industry research with citations and methodology |
| `interview` | Guest questioned about their work, philosophy, or domain expertise |

**Domain:** Bug Bounty / LLM Hacking / Cloud Security / Web Security / Self-Improvement / Technical Learning / General

**Signal density (be honest):** Low / Medium / High / Exceptional

---

## Step 2 — Choose Extraction Mode

### Quick Mode
**Use when:** Madhura says "quick", "just the key points", "TL;DR", content is under 15 minutes, OR signal density is Low.

Pipeline: `youtube/00` (section breakdown) → comprehension check. That's it. Three steps, done.

The section breakdown's "Honest Verdict" will tell Madhura whether deeper extraction is worth it. If she wants more, she'll ask.

### Full Mode (Default)
**Use when:** No mode specified and signal density is Medium or higher.

**For VIDEO content:**

| Content Type | Core Pipeline (always run) | Enrichment (run if High/Exceptional density) |
|---|---|---|
| Hacking talk | `youtube/00` → `youtube/02` | `youtube/03` (alpha ideas), `youtube/05` (abstract builder) |
| Bug bounty talk / demo | `youtube/00` → `youtube/02` | `youtube/03` |
| Self-improvement | `youtube/00` → `youtube/01` → `youtube/02` | — |
| Azure / Cloud / Technical | `youtube/00` → `youtube/04` (concept map) | `youtube/02` if concept map reveals depth |
| LLM internals / AI security | `youtube/00` → `youtube/02` → `youtube/04` | `youtube/03`, `youtube/05` |
| Research paper (presented) | `youtube/00` → `youtube/02` | `youtube/03` |
| Interview | `youtube/00` → `youtube/01` → `youtube/02` | `youtube/05` |

**For WRITTEN content:**

| Content Type | Core Pipeline | Enrichment |
|---|---|---|
| Bug bounty writeup | `writeups/01` (reverse engineer) → `writeups/02` | `writeups/03` |
| Security article / blog | `writeups/00` → `writeups/01` | `writeups/02` |
| Technical blog / tutorial | `writeups/00` | `writeups/01`, `writeups/02` |
| Research paper (text) | `writeups/00` → `writeups/01` | `youtube/03` (alpha ideas) |

### Deep Mode
**Use when:** Madhura says "deep", "everything", "full treatment", or signal density is Exceptional.

Run the full mode pipeline PLUS all enrichment steps. End with the infographic (`youtube/06`) automatically — don't wait for Madhura to ask.

---

## Step 3 — Read the Reference File and Execute

For each step in the pipeline, read the corresponding `.md` file from this skill's directory using the `view` tool, then follow those instructions against the content.

**File locations:**
- YouTube pipeline: `/youtube/00-section-breakdown.md` through `/youtube/07-comprehension-check.md`
- Written pipeline: `/writeups/00-article-extraction.md` through `/writeups/03-comprehension-check.md`

---

## Step 4 — Finish Every Session

- **Video content** → Always end with `youtube/07-comprehension-check.md`
- **Written content** → Always end with `writeups/03-comprehension-check.md`
- **High/Exceptional density in Deep mode** → Also run `youtube/06-infographic-prompt.md` automatically
- **If Madhura asks for a visual at any point** → Run `youtube/06-infographic-prompt.md` on the extraction output

---

## Step 5 — Bridge to Study Partner (Optional)

After extraction, if the content contains concepts Madhura should actively learn (not just know about), suggest:

> "This extraction has [N] concepts worth working through actively. Want me to switch to study mode and teach you [specific concept]?"

This bridges extraction (intake) to study-partner (learning). Don't force it — offer it.

---

## Quality Rules (apply to every extraction)

- **Specificity over volume.** 10 specific bullets beat 30 vague ones. Every time.
- **No padding.** If the content is thin, say so. Don't inflate a 5-minute video into a dissertation.
- **Preserve qualifications.** "This worked for me" ≠ universal prescription. Flag the difference.
- **Flag speculation vs. evidence.** "I believe" and "studies show" are different claims. Label them.
- **Honest signal density.** If a 60-minute talk has 8 minutes of insight, say so and point to the 8 minutes.
- **The comprehension check is not optional.** The discomfort of not answering clearly IS the learning.
- **Writeups are for reverse engineering.** Not for reading. Always run the reverse engineer step.
- **Save resurface prompts.** Set calendar reminders — 2 weeks, 4 weeks, 8 weeks. Paste cold. Don't re-read first.
