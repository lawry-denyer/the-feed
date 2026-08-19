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
```

Section ids and page numbers, in order: `ws` 02, `ls` 03, `moves` 04, `onstream` 05,
`watch` 06, `money` 07, `format` 08. Forecast is 09 and TL;DR is 10; both are built
from `FORECAST` and `TLDR` rather than from `SECTIONS`.

Open on load: the lead, On Stream, One to Watch, the most important number in
The Money, and Format Lab.
