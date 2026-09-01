# Chapter map — fixed before the rebuild, and not changed again

44 chapters, three parts. Each row names the file, the title on the card, and
the one visual idea the chapter is built around. The claims themselves are in
`content-ledger.md`, with a page number each.

## PART ONE — THE PAPER  (Dixit 1992, chapters 0–27)

| # | File | Title |
|---|---|---|
| 0 | ch00 | Two things that should not happen |
| 1 | ch01 | What “investment” actually means |
| 2 | ch02 | The textbook rule |
| 3 | ch03 | Three facts that don’t fit |
| 4 | ch04 | The three ingredients |
| 5 | ch05 | Why waiting is worth money |
| 6 | ch06 | So how high is high enough? |
| 7 | ch07 | A right, but not an obligation |
| 8 | ch08 | Putting numbers on it |
| 9 | ch09 | Money later is worth less than money now |
| 10 | ch10 | The textbook’s line, as a sum |
| 11 | ch11 | How the future is modelled |
| 12 | ch12 | The picture the paper draws |
| 13 | ch13 | The one formula in the film |
| 14 | ch14 | How steep is a curve? |
| 15 | ch15 | Why a bend is worth money |
| 16 | ch16 | One small random step |
| 17 | ch17 | The equation the paper actually solves |
| 18 | ch18 | Solving it with a guess |
| 19 | ch19 | Two curves, and where they touch |
| 20 | ch20 | When this is wrong |
| 21 | ch21 | When to give up |
| 22 | ch22 | The zone of inaction |
| 23 | ch23 | Hysteresis |
| 24 | ch24 | Two countries |
| 25 | ch25 | What a whole industry looks like |
| 26 | ch26 | Outside business |
| 27 | ch27 | Everything, in order |

## PART TWO — THE POLICY  (Bowdler & Radia 2012, chapters 28–38)

| # | File | Title |
|---|---|---|
| 28 | ch28 | Money, and who is in charge of it |
| 29 | ch29 | Why cutting the rate was not enough |
| 30 | ch30 | What quantitative easing actually is |
| 31 | ch31 | Three sets of books |
| 32 | ch32 | Channel one: the hot potato |
| 33 | ch33 | Channels two and three |
| 34 | ch34 | Leg two: cheaper money, and feeling richer |
| 35 | ch35 | What banks cannot do with reserves |
| 36 | ch36 | The result that says none of it works |
| 37 | ch37 | The other tools in the drawer |
| 38 | ch38 | The chain |

## PART THREE — THE ARGUMENT  (chapters 39–49)

| # | File | Title |
|---|---|---|
| 39 | ch39 | One sentence, two different kinds of claim |
| 40 | ch40 | The exception on page 613 |
| 41 | ch41 | Bringing Part One back |
| 42 | ch42 | The instrument that fights itself |
| 43 | ch43 | Two different kinds of fear |
| 44 | ch44 | The concession that hurts most |
| 45 | ch45 | The evidence, read twice |
| 46 | ch46 | And the ones that did not come back |
| 47 | ch47 | The rivals Kit cannot beat |
| 48 | ch48 | The management half |
| 49 | ch49 | What is actually being claimed |

## Where everything lives

```
lib/theme.py      3b1b's palette and CMU Serif; the one place colour is decided
lib/stage.py      regions, the caption limit, the legibility floor, his moves
lib/base.py       Chapter: narration, subtitles, staging, the live audit
lib/style.py      his animation vocabulary and the word-colour table
lib/stick.py      the cast
lib/scale.py      the master vertical scale
lib/chain.py      the six-link transmission chain
lib/surface.py    the multiplier sheet, in three dimensions
lib/balance.py    the three T-accounts
lib/widgets.py    buildings, bars, dials, doors, springs, shields, the iron bar
lib/cards.py      definition cards, recap panels, icons, the progress indicator
lib/voice.py      the two voices and the line cache
chapters/chNN.py  one file, one scene, per chapter
pilot/pilot.py    every primitive on one reel, for locking the system
reference/        the first attempt, kept only to check nothing was dropped
tools/            render, assemble, and the six audits
docs/             ledger, fact sheet, glossary, narration, concessions, plans
```
