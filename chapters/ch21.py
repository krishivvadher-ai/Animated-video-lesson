import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.scale import MasterScale
from lib.theme import *


class Chapter21(Chapter):
    CH = 21
    TITLE = "When to give up"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["slab", "door", "scale", "clock"]

    def body(self):
        # ------------------------------------------------ suspend vs abandon
        self.heading("Two words that are not the same")
        self.define("suspending", "Stopping for a while, meaning to start again.",
                    "clock", WAIT, at=LEFT * 3.3 + UP * 0.5, hold=3.4)
        self.define("abandoning", "Stopping for good.", "door", COST,
                    at=RIGHT * 3.3 + UP * 0.5, hold=3.0)

        rust = St.caption("idle machinery rusts — totally, at once", SUNK, T_SUB,
                          width=34)
        St.place(rust, St.FULL, ay=0.1)
        with self.narrate("To make the point sharp, the paper assumes that idle "
                          "machinery rusts. Totally, and immediately. So pausing and "
                          "quitting become the same thing, and starting again means "
                          "paying the whole sunk cost over again."):
            self.play(FadeIn(rust), run_time=1.0)
        self.beat()
        with self.narrate("And the paper flags that itself, as a deliberate "
                          "simplification. Where a firm really can mothball a factory "
                          "and restart it cheaply, this half of the argument gets "
                          "weaker. Hold on to that — Part Three needs it."):
            self.foot("the paper flags this as a simplification", MUTED)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the mirror argument
        self.heading("Why she absorbs losses first")
        nell = stick.nell(scale=0.9)
        St.place(nell, St.STAGE, ax=-0.8, ay=-0.3)
        self.play(FadeIn(nell), nell.mood("worried"), run_time=0.7)
        self.side(["losing money this month",
                   "closing is final",
                   "staying keeps recovery alive",
                   "so she absorbs real losses"],
                  colour=CHALK, dot_colour=TRIGGER, width=20,
                  spoken=["Nell is losing money this month.",
                          "If she closes, she can never get the chance back without "
                          "paying for it all over again.",
                          "Staying open keeps alive the chance that trade recovers.",
                          "And that chance is worth something. So she should absorb "
                          "real losses before she shuts."])
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the four levels
        self.heading("Four levels, in his own example")
        sc = MasterScale(x=-4.4, y=-0.45, height=4.6)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), FadeIn(sc.title), run_time=1.0)
        units = St.caption("running cost 1 · sunk cost 2", MUTED, T_BODY, width=20)
        St.place(units, St.SIDE, ay=0.75)
        self.play(FadeIn(units), run_time=0.6)

        lv = [("L", 0.72, "0.72  give up", TRIGGER, 5),
              ("C", 1.00, "1.00  day-to-day cost", SUNK, 3),
              ("M", 1.10, "1.10  textbook", COST, 3),
              ("H", 1.62, "1.62  really build", TRIGGER, 5)]
        says = ["Down here, at nought point seven two, she finally gives up. That is "
                "the real quit-line.",
                "At one, her day-to-day costs are exactly covered. That is where the "
                "textbook says stop.",
                "At one point one, the textbook says build — day-to-day costs plus the "
                "normal return on the money sunk in.",
                "And at one point six two, she should actually build."]
        objs = []
        for (k, v, t, c, sw), say in zip(lv, says):
            g = sc.add_level(k, v, t, c, width=2.6, sw=sw)
            objs.append(g)
            with self.narrate(say):
                self.play(Create(g[0]), FadeIn(g[1]), run_time=1.1)
            self.beat(0.4)

        self.play(FadeOut(units), run_time=0.3)
        obs = St.points(["profit 0.62 at H — over 6× the normal return",
                         "at L: losses near a third of running cost"],
                        colour=TRIGGER, dot_colour=TRIGGER, size=T_BODY, width=20)
        St.place(obs, St.SIDE, ay=0.5)
        says2 = ["At the true build point her operating profit is nought point six two "
                 "— more than six times the normal return on the money she has sunk in.",
                 "And at the quit point she is absorbing losses of nearly a third of "
                 "her day-to-day costs, month after month, before she gives up."]
        for i, row in enumerate(obs):
            with self.narrate(says2[i]):
                self.play(FadeIn(row), run_time=0.9)
        self.beat()
        self.play(FadeOut(obs), run_time=0.4)

        # ------------------------------------------------ comparative statics
        self.heading("Now move one thing at a time")
        bigger = St.caption("a bigger sunk cost", SUNK, T_SUB, width=18)
        St.place(bigger, St.SIDE, ay=0.7)
        with self.narrate("Suppose the building costs more to put up. A bigger sunk "
                          "cost. What happens to the two lines?"):
            self.play(FadeIn(bigger), run_time=0.7)

        hnew = sc.level_line(1.85, TRIGGER, width=2.6, sw=5)
        lnew = sc.level_line(0.60, TRIGGER, width=2.6, sw=5)
        with self.narrate("The build-line goes up. She is more reluctant to start."):
            self.play(TransformFromCopy(objs[3][0], hnew), run_time=1.3)
        with self.narrate("And the quit-line goes down. She is more reluctant to stop."):
            self.play(TransformFromCopy(objs[0][0], lnew), run_time=1.3)
        self.beat()
        twice = St.caption("slower to start AND slower to stop", SUNK, T_BODY, width=20)
        St.place(twice, St.SIDE, ay=0.1)
        with self.narrate("Say that one twice, because it is not obvious. A bigger "
                          "stake to keep alive makes her slower to start and slower to "
                          "stop. Both at once, and for the same reason — there is more "
                          "to protect."):
            self.play(FadeIn(twice), run_time=0.9)
            self.play(S.flash_around(twice, SUNK))
        self.beat()
        self.play(FadeOut(bigger), FadeOut(twice), FadeOut(hnew), FadeOut(lnew),
                  run_time=0.5)

        exit_ = St.caption("costly to leave → build-line higher still", COST, T_BODY,
                           width=20)
        St.place(exit_, St.SIDE, ay=0.5)
        with self.narrate("One more. If leaving is itself expensive — redundancy "
                          "payments, restoring the site of a mine — then the build-line "
                          "rises further still. She is more cautious about entering "
                          "something she may have to pay to escape."):
            self.play(FadeIn(exit_), run_time=0.9)
        self.beat()

        self.close_chapter([
            "stopping = ruin, a flagged simplification",
            "staying keeps recovery alive, so losses are absorbed",
            "0.72 · 1.00 · 1.10 · 1.62",
            "a bigger sunk cost slows her both ways",
        ])
