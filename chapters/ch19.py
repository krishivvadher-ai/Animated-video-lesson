import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter19(Chapter):
    CH = 19
    TITLE = "Two curves, and where they touch"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["scale", "door", "flow", "money"]

    def body(self):
        # the key to the squiggles, before any of them is used again
        self.symbol_key(["R", "K", "beta", "alpha"], region=St.FULL, hold=4.0)

        # ------------------------------------------------ the second equation
        self.heading("A live project pays you while you hold it")
        wait_ = VGroup(cards.icon("clock", WAIT, 1.6),
                       St.caption("waiting pays nothing", WAIT, T_SMALL, width=20)
                       ).arrange(DOWN, buff=0.28)
        live = VGroup(cards.icon("money", MONEY, 1.6),
                      St.caption("a built project pays R", MONEY, T_SMALL, width=20)
                      ).arrange(DOWN, buff=0.28)
        two = VGroup(wait_, live).arrange(RIGHT, buff=3.0)
        St.place(two, St.FULL, ay=0.55)
        with self.narrate("Everything so far was about the chance to build, which pays "
                          "you nothing while you hold it."):
            self.play(FadeIn(wait_), run_time=0.9)
        with self.narrate("A project that has actually been built is different. It "
                          "hands you the money coming in, every year, while you own "
                          "it. So the balance has one more thing on it."):
            self.play(FadeIn(live), run_time=0.9)

        eq = Text("½σ²R² V₁″  +  μR V₁′  −  ρV₁  +  R  =  0", font=FONT,
                  font_size=T_SUB, color=MONEY)
        St.place(eq, St.FULL, ay=-0.35)
        with self.narrate("Which is the same equation with a single extra R on the "
                          "end — the revenue it pays out. That is equation A five."):
            self.play(Write(eq), run_time=2.2)
        sol = Text("V₁(R)  =  R ÷ (ρ − μ)  +  A R^α", font=FONT, font_size=T_SUB,
                   color=MONEY)
        St.place(sol, St.FOOT, pad=0.06)
        with self.narrate("Its answer is the plain worth of the revenue stream, plus a "
                          "term that is the value of the option to give up. That option "
                          "is worthless when takings are enormous, which is what fixes "
                          "which power survives this time."):
            self.play(Write(sol), run_time=2.2)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the two curves
        self.heading("Now draw both, on one picture")
        ax = Axes(x_range=[0, 6, 1], y_range=[-1, 5, 1], x_length=7.0, y_length=4.0,
                  axis_config=AXIS)
        St.place(ax, St.STAGE, ay=0.0, fill=False)
        xl = Text("money coming in →", font=FONT, font_size=T_TINY, color=MUTED)
        xl.next_to(ax, DOWN, buff=0.18)
        self.play(Create(ax), FadeIn(xl), run_time=0.9)

        v0 = ax.plot(lambda x: 0.055 * x ** 2.6, x_range=[0.2, 4.4], color=WAIT,
                     stroke_width=5)
        v0l = Text("waiting", font=FONT, font_size=T_SMALL, color=WAIT)
        v0l.next_to(ax.c2p(2.2, 0.055 * 2.2 ** 2.6), UP, buff=0.3)
        with self.narrate("Here is what waiting is worth: B times R to the beta, the "
                          "curve we just derived."):
            self.play(Create(v0), FadeIn(v0l), run_time=1.6)

        v1 = ax.plot(lambda x: 1.05 * x - 1.15 - 0.5 / max(x, 0.35),
                     x_range=[0.6, 5.6], color=MONEY, stroke_width=5)
        v1l = Text("built, and running", font=FONT, font_size=T_SMALL, color=MONEY)
        v1l.next_to(ax.c2p(4.9, 1.05 * 4.9 - 1.15 - 0.5 / 4.9), UP, buff=0.3)
        with self.narrate("And here is what a running project is worth, once you allow "
                          "it to be abandoned. Nearly a straight line when takings are "
                          "high, bending away as they fall."):
            self.play(Create(v1), FadeIn(v1l), run_time=1.8)
        self.beat()

        # ------------------------------------------------ value matching
        self.heading("Two conditions, at each end")
        H = 4.1
        dh0 = Dot(ax.c2p(H, 0.055 * H ** 2.6), radius=0.09, color=TRIGGER)
        dh1 = Dot(ax.c2p(H, 1.05 * H - 1.15 - 0.5 / H), radius=0.09, color=TRIGGER)
        gap = DoubleArrow(dh0.get_center(), dh1.get_center(), color=TRIGGER,
                          stroke_width=4, buff=0.02, tip_length=0.14)
        kl = Text("K", font=FONT, font_size=T_SUB, color=TRIGGER)
        kl.next_to(gap, RIGHT, buff=0.2)
        with self.narrate("At the level where she builds, stepping from one curve to "
                          "the other must be worth exactly the cost of building. Not "
                          "more, or she would have built sooner. Not less, or she would "
                          "not build at all."):
            self.play(FadeIn(dh0), FadeIn(dh1), run_time=0.7)
            self.play(GrowFromCenter(gap), FadeIn(kl), run_time=0.9)
        vm = Text("V₁(H) − V₀(H)  =  K", font=FONT, font_size=T_BODY, color=TRIGGER)
        St.place(vm, St.SIDE, ay=0.75)
        self.play(Write(vm), run_time=1.4)
        self.beat()

        sp = Text("V₁′(H) − V₀′(H)  =  0", font=FONT, font_size=T_BODY, color=MONEY)
        St.place(sp, St.SIDE, ay=0.25)
        with self.narrate("And a second condition, which is the subtle one. The two "
                          "curves must not just be the right distance apart — they must "
                          "have the same steepness there. They meet tangentially."):
            self.play(Write(sp), run_time=1.6)

        why = St.caption("a kink would mean money\nleft on the table", MUTED,
                         T_SMALL, width=22)
        St.place(why, St.SIDE, ay=-0.35)
        with self.narrate("Because a corner would mean the trigger was in the wrong "
                          "place: nudge it either way and you would do better. Only "
                          "where the slopes agree is there nothing left to gain."):
            self.play(FadeIn(why), run_time=0.9)
            self.play(S.indicate(sp, MONEY))
        self.beat()
        self.define("smooth pasting", "Where two value curves meet, their slopes "
                    "must agree.", "flow", MONEY, at=DOWN * 2.5, hold=4.2)
        self.clear_stage()

        # ------------------------------------------------ four equations
        self.heading("Four conditions, four unknowns")
        rows = St.points(["V₁(H) − V₀(H) = K", "V₁′(H) − V₀′(H) = 0",
                          "V₁(L) − V₀(L) = 0", "V₁′(L) − V₀′(L) = 0"],
                         colour=CHALK, dot_colour=TRIGGER, size=T_BODY, width=26)
        St.place(rows, St.STAGE, ay=0.1)
        unk = St.points(["A", "B", "H", "L"], colour=MUTED, dot_colour=MUTED,
                        size=T_BODY, width=12)
        St.place(unk, St.SIDE, ay=0.1)
        ul = Text("the unknowns", font=FONT, font_size=T_SMALL, color=MUTED)
        ul.next_to(unk, UP, buff=0.4)
        says = ["At the build line, the step up is worth the cost.",
                "And the slopes agree there.",
                "At the give-up line, the step is worth nothing at all — she simply "
                "walks away.",
                "And the slopes agree there too."]
        for i, row in enumerate(rows):
            with self.narrate(says[i]):
                self.play(FadeIn(row), run_time=0.7)
        with self.narrate("Four conditions. Four unknowns: the two amounts, and the two "
                          "levels."):
            self.play(FadeIn(ul), FadeIn(unk), run_time=0.9)
        self.beat()

        honest = St.caption("no formula exists — it is solved numerically", SUNK,
                            T_SUB, width=48)
        St.place(honest, St.FOOT, pad=0.06)
        with self.narrate("And the paper is honest about what happens next. There is no "
                          "formula. The four have to be solved together on a computer. "
                          "Which is exactly why the two numbers chapter thirteen ended "
                          "on were printed rather than derived: nought point seven two, "
                          "and one point six two."):
            self.play(FadeIn(honest), run_time=1.0)
            self.play(S.flash_around(honest, SUNK, run_time=2.0))
        self.beat()

        self.close_chapter([
            "a running project pays R, so its equation gains +R",
            "at H the step between curves is worth K",
            "and the slopes must agree: smooth pasting",
            "four conditions, four unknowns, solved by computer",
        ])
