# Investment, Hysteresis and Quantitative Easing — an animated film in three parts

A narrated, animated explainer built with **Manim Community Edition**, in the
visual language of 3Blue1Brown: a dark stage, one idea at a time, diagrams built
up live element by element, words written on rather than pasted up, objects that
morph into one another, camera pushes on the moments that matter, and one
genuinely three-dimensional object where three dimensions are the honest way to
show the thing.

The film assumes **no economics, no finance, no management and no mathematics
beyond percentages**. Every technical term gets a definition card before it is
used in a sentence, and nothing is used before it is built.

| Part | Chapters | What it teaches |
|---|---|---|
| **One — The Paper** | 0–16 | Avinash Dixit, *Investment and Hysteresis*, JEP 6(1), 1992, in full |
| **Two — The Policy** | 17–27 | Bowdler & Radia, *Unconventional monetary policy: the assessment*, OxREP 28(4), 2012, in full |
| **Three — The Argument** | 28–38 | The author's own argument, built on those two papers plus Martin & Milas (2012) |

## Deliverables

```
final/part-one.mp4                  Part One, scored and mixed
final/part-two.mp4                  Part Two
final/part-three.mp4                Part Three
final/film-complete.mp4             all three, joined
final/*.srt                         clean subtitles, one per part
final/*-subtitled.mp4               burned-in subtitle cuts
final/film-complete-subtitled.mp4   the whole film, burned-in
build/media/videos/chNN/1080p30/    every chapter as its own file
```

## How to re-render

```bash
python3 -m venv .venv && .venv/bin/pip install "manim>=0.18" sherpa-onnx numpy scipy
sudo apt-get install -y ffmpeg libcairo2-dev libpango1.0-dev poppler-utils

# one chapter, fast draft
.venv/bin/manim -ql --media_dir build/media -o ch12.mp4 chapters/ch12.py Chapter12

# one chapter, final quality
.venv/bin/manim -r 1920,1080 --fps 30 --media_dir build/media -o ch12.mp4 chapters/ch12.py Chapter12

# the whole film
bash tools/render_all.sh          # every chapter and title card at 1080p30
.venv/bin/python tools/make_music.py   # regenerate the six score cues
.venv/bin/python tools/assemble.py     # concat, subtitle, score, mix, join
.venv/bin/python tools/verify.py       # the audits in section 9 of the brief
.venv/bin/python tools/make_docs.py    # regenerate glossary.md and narration.md
```

## How to change a chapter

Chapters are one file each, `chapters/chNN.py`, one `Scene` subclass each. They
import everything from `lib/` and add nothing to it, so a change to a colour, a
figure or the master diagram propagates everywhere at once.

```
lib/theme.py     colours, type sizes, timing — the single source of truth
lib/stick.py     the StickFigure class: walk cycle, five moods, speech, thought
lib/scale.py     the master vertical revenue scale (chs 2,6,10,11,12,13,14,16,30,31,35)
lib/chain.py     the six-link transmission chain (chs 27,28,38)
lib/surface.py   the multiplier surface, in 3D (chs 8, 30)
lib/balance.py   the three T-accounts (ch 20)
lib/widgets.py   shops, bars, dials, doors, springs, shields, the iron bar
lib/cards.py     definition cards, quote cards, recap panels, icons, progress
lib/voice.py     the speech service and the two voices
lib/base.py      the Chapter base: narration, subtitles, camera, house style
```

Narration lives inside the chapter files, in `self.narrate(...)` calls, so the
script and the animation can never drift apart. `docs/narration.md` is generated
from them.

## How to swap the music

`tools/make_music.py` writes six cues into `audio/music/` — `open`, `build`,
`turn`, `policy`, `doubt`, `close`. Every note is synthesised from scratch with
numpy; nothing is sampled, downloaded or licensed. Change `MOTIF`, `cue(...)` or
the partial mix in `note(...)` and re-run it, then re-run `tools/assemble.py`.
The `close` cue deliberately returns to the `open` motif and resolves.

Three moments are scored as **silence** and must stay that way: the value of
waiting landing (ch 5), the revenue path falling back without a closure (ch 12),
and Kit waiting for a third shield that never comes (ch 28).

## The voices

The brief asks for `edge-tts`. This environment's egress proxy refuses
`speech.platform.bing.com` (HTTP 403 on the websocket), so the film falls one
step down the brief's own fallback list to **piper** — the same class of neural
voice, run offline through `sherpa-onnx`:

- **Narrator** — `en_GB-alan-medium`, British male, slowed to about 128 words a
  minute.
- **Character** — `en_GB-cori-high`, British female, a little quicker, used for
  Ava's and Kit's interruptions.

Every line is cached in `audio/lines/` keyed by a hash of its text and voice, so
re-rendering never regenerates audio. Pronunciations that the synthesiser gets
wrong are respelled in `lib/voice.py`; Greek letters are never read aloud.

## Accuracy

- `docs/content-ledger.md` — every claim the film makes, in chapter order, with
  its source and page.
- `docs/fact-sheet.md` — every number, marked **printed** (an author prints it)
  or **derived** (the film computed it, and says so on screen).
- `docs/glossary.md` — every term, its on-screen definition, and its chapter.
- `docs/narration.md` — the full spoken script.

Part One adds no economics from outside Dixit's paper. Part Two adds none from
outside Bowdler & Radia. Only three articles are named in the whole film, plus
Bernanke, and only ever as *"Dixit, quoting Bernanke"*. `tools/verify.py`
checks that automatically.
