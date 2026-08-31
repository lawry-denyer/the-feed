# Writing a content file

One file per issue: `content/YYYY-MM-DD.py`. Pure Python data, no logic, no HTML
document structure. The renderer turns it into the page. **Never edit the design here** —
that lives in `build_feed.py`.

The most recent file in `content/` is always a complete worked example. Copy its shape.

## Rules that the verifier enforces

- `LEAD["headline"]` must be UPPERCASE.
- No `<em>` or `<i>` tags anywhere. No italics.
- Two spaces after every period, question mark and exclamation mark.
- Banned words: programmatic, upfront, flywheel, category mismatch, sponcon, CPM,
  mid-funnel, activation, ideate, leverage as a verb.
- Every `stamps` URL must be real and retrieved. Never invent one.

## Shape

```python
ISSUE = {
  "date_iso":  "2026-08-17",                    # must match the filename
  "kicker":    "Crux Media // Monday 17 August 2026",
  "tagline":   "What brands did on YouTube yesterday, and whether it worked.",
  "pace":      "STEADY",                        # or "LIGHT" on a thin day
  "next_drop": "Next drop: Tuesday, 06:30 MT",
}

LEAD = {
  "headline": "UPPERCASE DISPLAY HEADLINE",
  "deck":     "Two or three sentences.  Punchy.",
  "stamps":   [("YOUTUBE BLOG", "https://..."), ...],   # (label, real url)
  "body":     ["<p>-less paragraph strings.  May contain <mark>...</mark>.", ...],  # 4-6
  "numbers":  [("8,000", "label"), ("20M", "label"), ("10M", "label")],  # exactly 3
  "flagnote": "optional single-source or Crux-client caveat, or omit the key",
  "so_what":  "2-3 plain sentences on the mechanism.",
  "do_this":  "Imperative, specific, doable this week.",
}

SECTIONS = [                    # drop any section with nothing real in it
  {
    "id": "ws", "name": "W'S", "page": "pg. 02",
    "note": "what worked, and the exact reason it worked",
    "tint": "blue",             # "blue" for W'S, "pink" for L'S, else None
    "items": [
      {
        "title": "...", "hook": "One line that makes me want to open it.",
        "open": True,           # optional; open on load
        "stamps": [(...)], "body": [...],
        "numbers": [...],       # optional, max twice per issue including the lead
        "flagnote": "...",      # optional
        "watch": {              # ONE TO WATCH only — the featured video block
          "label": "TOP VIDEO, LAST 3 MONTHS",
          "title": "exact video title",
          "url":   "https://www.youtube.com/watch?v=...",   # verify it resolves
          "meta":  "1,673,726 views · published 26 May 2026 · 2h 45m",
          "note":  "One plain sentence on what it is.",
        },
        "so_what": "...", "do_this": "...",
      },
    ],
  },
]

FORECAST = [                    # 3-5 calls
  {"confidence": "LIKELY",      # LIKELY | WATCH CLOSELY | LONG SHOT
   "window": "by 31 January 2027",
   "headline": "Short headline",
   "body": "A paragraph of reasoning.",
   "do": "Something to do before it happens."},
]

TLDR = [                        # 6-7 complete thoughts: what happened, then what to do
  "...",
]

SHARE = [        # exactly 3, three DIFFERENT stories, always in this order:
  {"who":   "JARED · CEO",   # then "JAMES · CREATIVE DIRECTOR", then
   "angle": "The argument the post makes, in one line.",   # "LAWRY · LEAD VIDEO EDITOR"
   "post":  "Ready-to-paste LinkedIn copy.\n\nBlank lines between paragraphs.",
   "why":   "One line on why this is worth their name on it."},
]
```

`SHARE` is optional. Issues published before 1 September 2026 do not define it and
render exactly as they always did.

## SHARE — the rules that keep it credible

Three people from one company posting daily off one brief will look coordinated
within a fortnight, and a competent post nobody remembers is worse than no post.
These constraints are what stop both.

**Order is fixed: Jared (CEO), then James (Creative Director), then Lawry (Lead
Video Editor).** `who` reads `JARED · CEO`, `JAMES · CREATIVE DIRECTOR`,
`LAWRY · LEAD VIDEO EDITOR`.

### The bar

Every post must contain a claim the reader did not already believe when they
started reading. Not a summary of the news — a reframe of it, or a number that
contradicts something they assume.

The test: **if the reader would have agreed with your last line before reading
your first, kill the post and pick a different story.** "Big number, therefore
this matters" fails. "Everyone read this as X, but the mechanism is actually Y"
passes.

If no story in the issue supports a post that clears this for a given person,
research a fresh one for them. A weak post under a real person's name costs
more than a missing one.

### Shape

- **First two lines are everything.** LinkedIn truncates around 140-200
  characters on mobile. Those lines must state the surprising thing, not set it
  up. No throat-clearing, no "I've been thinking about."
- **One idea.** Not three. Follow it all the way down.
- Short paragraphs, one to three lines, white space between them.
- The number early, sourced in the post, named the way a person says it out
  loud: "figures from Streams Charts", not a citation.
- **End on the real point.** No question begging for comments, no "what do you
  think", no tidy aphorism that restates the middle. A flat ending is better
  than a neat one that says nothing.

### Voice

- First person. Match the person to the story: Jared gets the number a sceptical
  client needs, James gets the campaign learning, Lawry gets the thing only
  someone in an edit suite knows.
- Specifics beat polish. A detail from inside the work — the fridge hum in take
  four, whether a cut lands at three seconds or five — is worth more than any
  well-turned sentence.
- Ambivalence is a human tell. A post allowed to end unresolved reads as real.
  A post that resolves cleanly reads as written by a machine.
- **Never invent biography.** No "in my ten years", no invented war stories, no
  claims about Crux's clients or projects. Write what the person can defend from
  the news plus their own craft. Opinions about the industry, never
  announcements about Crux.
- Banned: hashtag blocks, emoji bullets, engagement bait, one-word lines for
  drama, "Here's the thing", "Let that sink in", "The result?", "And that's when
  it hit me."
- Single spaces after periods inside `post` — that copy gets pasted into
  LinkedIn. House double-space style still applies to `angle` and `why`.

### Other rules

- **Three different stories.** Never three angles on the lead.
- **No pitch.** Never mention Crux, its services, its clients or that it is
  hiring. These earn attention by being worth reading.
- 150-230 words each.
- **Drop a person rather than pad.** Ship two and say so in the report.

Section ids and page numbers, in order: `ws` 02, `ls` 03, `moves` 04, `onstream` 05,
`watch` 06, `money` 07, `format` 08. Forecast is 09, TL;DR is 10 and Share is 11;
all three are built from `FORECAST`, `TLDR` and `SHARE` rather than from `SECTIONS`.

Open on load: the lead, On Stream, One to Watch, the most important number in
The Money, and Format Lab.
