# Rebuild plan

## What went wrong the first time, in my own words

These are the mistakes this rebuild exists to prevent. Each one has a
countermeasure that is enforced by code, not by my remembering.

| # | Mistake | Countermeasure |
|---|---|---|
| 1 | I wrote scenes as prose and then stripped the prose out. 407 long strings had to be shortened after the fact. | Scenes are authored through a staging API that **cannot** place a paragraph. A caption over 60 characters raises at build time. |
| 2 | I renumbered the chapters three times, which invalidated every render. | The chapter map is fixed in `docs/chapter-map.md` before a line is written and never changes. |
| 3 | I changed the palette, typeface and animation defaults *after* writing 44 chapters, forcing two full re-renders. | The visual system is frozen and proved on a pilot **first**. Nothing global changes after that. |
| 4 | Rendering was serial, so a full pass cost an hour and a half. | Four-way parallel, audio pre-warmed, cache writes atomic. A full pass is ~35 min. |
| 5 | Layout collisions were found only after rendering. | Every scene is placed into named regions that cannot overlap by construction, and the live audit still checks. |
| 6 | Text was silently auto-shrunk below legibility to make it fit. | The staging API refuses to scale text below the readable minimum; it raises instead. |

## What is kept

Proven and reused unchanged:

- `lib/theme.py` — 3Blue1Brown's published palette and CMU Serif, verified on screen.
- `lib/style.py` — his animation vocabulary and the word-colouring table.
- `lib/voice.py` + `audio/lines/` — 699 narrated lines already generated and cached.
- `lib/stick.py` — the cast, with a real walk cycle and five moods.
- `lib/scale.py`, `chain.py`, `surface.py`, `balance.py`, `widgets.py`, `cards.py`.
- `tools/` — parallel render, assembly, the five audits, the score.
- `docs/content-ledger.md`, `fact-sheet.md`, `concessions.md` — every claim already
  checked against the papers, and the numbers already verified by grep.
- `source/` and the extracted text of all three papers.

## What is rebuilt

Every scene. `chapters/` is written again from the ledger, through a new
staging API, with the visual designed first and the words fitted to it.

## The new staging API — `lib/stage.py`

A scene is composed of **regions**, and a region is a rectangle that no other
region overlaps:

```
TITLE   the top strip, for the section heading and its underline
STAGE   the main area, for the diagram or the acted scene
SIDE    the right-hand column, for a running commentary of short labels
FOOT    the bottom strip, for one short line at a time
```

Placing something into a region fits it to that region. Two things cannot
collide, because two regions cannot overlap and a region holds one thing.

Rules the API enforces, by raising rather than by shrinking:

1. A caption is at most 60 characters. Longer text belongs in the narration.
2. Text is never scaled below the readable minimum.
3. Nothing is drawn into the caption band at the foot of the frame.
4. Every beat has something moving: a beat with no animation raises.

## Order of work

1. **Freeze the system.** Write `lib/stage.py`, render a pilot that exercises
   every primitive, look at the frames, lock it.
2. **Fix the chapter map.** 44 chapters, three parts, written down once.
3. **Rebuild the chapters**, in batches, rendering each batch at draft quality
   as it is written so mistakes are caught in minutes rather than hours.
4. **Render** all 44 in parallel at 1920x1080, 30fps.
5. **Audit** — layout, frames, prose, terms, numbers, sync, silence, loudness.
6. **Assemble** — concat, subtitle, score, mix, deliver.

## What the rebuild found

Four defects turned up during the rebuild that no amount of care would have
caught by reading, because in each case the code was quietly wrong rather than
loudly broken. They are recorded here because each one had been silently
distorting the film for some time before anything noticed.

**1. `LaggedStartMap` splats a group into its children.**
Manim's helper passes each submobject to the animation constructor as `*args`.
A `Mobject` is iterable, so a group is unpacked. `FadeIn` takes `*mobjects`
and so survives this; `Restore` takes exactly one, so `Restore(bar)` silently
became `Restore(bar.rect)` -- restoring a rectangle whose state had never been
saved. Replaced everywhere by `style.lag_map`, which builds the animations one
at a time.

**2. The legibility check counted every shrink twice.**
Manim derives `Text.font_size` from the mobject's current height, so it already
reflects every `scale()` applied to it. The checker multiplied that by its own
record of the staging scale, so a caption rendered at 22.6 was reported as 14
and rejected. Every layout that passed was genuinely legible, so nothing bad
shipped -- but the film was being squeezed into a bar far tighter than the one
it was supposed to meet.

**3. Nothing checked that a thing was inside the picture.**
The auditor measured overlap and legibility and text height, and never once
asked whether a mobject was on screen. A dial's label sat at x = -7.36 and was
cut in half, in a chapter reporting zero problems. The check now records
anything reaching past the frame, and found four chapters doing it.

**4. Verification that never ran.**
`verify.py` referenced an undefined name in its second check, so every run
crashed after the first one and the crash looked like the end of the output.
It also matched excluded author names as substrings -- "Farmers absorb years of
losses" reading as the economist Farmer -- and compared permitted verbatim
quotations against text whose spacing Manim had stripped, so all four hinge
quotations looked like forbidden paragraphs.

The lesson each of them shares: a check that cannot fail is worse than no check,
because it is mistaken for one.

**5. Verification that stopped halfway.**
`verify.py`'s run block sat above the functions it called, so `check_durations`
raised `NameError` and the last three checks -- durations, scripted silences
and loudness -- had never run once. The block now sits at the end of the file.
Same lesson as the other four: a check that cannot fail is worse than no check.
