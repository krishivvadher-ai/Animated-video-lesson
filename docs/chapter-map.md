# Chapter map — fixed before the rebuild, and not changed again

44 chapters, three parts. Each row names the file, the title on the card, and
the one visual idea the chapter is built around. The claims themselves are in
`content-ledger.md`, with a page number each.

## PART ONE — THE PAPER  (Dixit 1992, chapters 0–21)

| # | File | Title | The picture it is built on |
|---|---|---|---|
| 0 | ch00 | Two things that should not happen | a farmer's losses stacking up; an empty plot |
| 1 | ch01 | What “investment” actually means | money flowing in one side of a factory and out the other |
| 2 | ch02 | The textbook rule | the master scale, with two lines almost touching |
| 3 | ch03 | Three facts that don’t fit | two bars, a farm income chart, the dollar-and-imports graph |
| 4 | ch04 | The three ingredients | a slab that cannot be sold back; fog thinning; a door staying open |
| 5 | ch05 | Why waiting is worth money | five futures fanning out from one point |
| 6 | ch06 | So how high is high enough? | the textbook line staying put while the real one slides up |
| 7 | ch07 | A right, but not an obligation | a voucher, used and thrown away |
| 8 | ch08 | Putting numbers on it | two dials feeding a sealed machine, and a 3-D sheet |
| 9 | ch09 | Money later is worth less than money now | 24 bars shrinking away to nothing |
| 10 | ch10 | The textbook’s line, as a sum | two blocks, one subtracted from the other |
| 11 | ch11 | How the future is modelled | a binomial lattice fanning out, then a spread |
| 12 | ch12 | The picture the paper draws | his Figure 2: a line and a curve that touch |
| 13 | ch13 | The one formula in the film | a square root worked out on screen |
| 14 | ch14 | When this is wrong | a rival through the door; a crowd bunching |
| 15 | ch15 | When to give up | the four levels on the master scale |
| 16 | ch16 | The zone of inaction | a narrow band widening to a wide one |
| 17 | ch17 | Hysteresis | a path up through the band and back down |
| 18 | ch18 | Two countries | a lopsided distribution with its bad half cut off |
| 19 | ch19 | What a whole industry looks like | a crowd entering and leaving between two lines |
| 20 | ch20 | Outside business | two flats, and a signal not sent |
| 21 | ch21 | Everything, in order | the ladder, then the master scale in its final form |

## PART TWO — THE POLICY  (Bowdler & Radia 2012, chapters 22–32)

| # | File | Title | The picture it is built on |
|---|---|---|---|
| 22 | ch22 | Money, and who is in charge of it | a lever pushed down until it hits the floor |
| 23 | ch23 | Why cutting the rate was not enough | a wedge opening between two arrows |
| 24 | ch24 | What quantitative easing actually is | a government, a saver, a ticket, coupons arriving |
| 25 | ch25 | Three balance sheets | three T-accounts filling in |
| 26 | ch26 | Channel one: the hot potato | a ladder of assets, and money passed along a row |
| 27 | ch27 | Channels two and three | waves leaving the Governor; a frozen market thawing |
| 28 | ch28 | Leg two: cheaper money, and feeling richer | three shields on one half of a sentence |
| 29 | ch29 | Money, and what banks can’t do with reserves | a tall bar that should have grown, and did not |
| 30 | ch30 | The result that says none of it works | risk moving to the state and back through taxes |
| 31 | ch31 | The other tools in the drawer | a rate path held flat by an announcement |
| 32 | ch32 | The chain | six links, and the one nobody examines |

## PART THREE — THE ARGUMENT  (chapters 33–43)

| # | File | Title | The picture it is built on |
|---|---|---|---|
| 33 | ch33 | One sentence, two different kinds of claim | three shields on one half, none on the other |
| 34 | ch34 | The exception on page 613 | money arriving and nothing happening |
| 35 | ch35 | Bringing Part One back | the 3-D sheet, walked across in the wrong direction |
| 36 | ch36 | The instrument that fights itself | two arrows on one bar, pulling opposite ways |
| 37 | ch37 | Two different kinds of fear | a spring squeezed; a thought bubble untouched |
| 38 | ch38 | The concession that hurts most | the good half of the distribution, boxed |
| 39 | ch39 | The evidence, read twice | a verdict, then a two-row table |
| 40 | ch40 | And the ones that did not come back | a path down through the quit line, and no return |
| 41 | ch41 | The rivals Kit cannot beat | four doors, each left standing open |
| 42 | ch42 | The management half | a queue of projects at a boardroom door |
| 43 | ch43 | What is actually being claimed | the chain, marked up, and the whole cast |

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
