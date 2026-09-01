import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter15(Chapter):
    CH = 15
    TITLE = "Why a bend is worth money"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["scale", "risk", "money", "fog"]

    def body(self):
        # ------------------------------------------------ the gradient of the gradient
        self.heading("Do it twice")
        ax = Axes(x_range=[0, 6, 1], y_range=[0, 5, 1], x_length=6.4, y_length=3.4,
                  axis_config=AXIS)
        St.place(ax, St.STAGE, ay=0.15, fill=False)
        f = lambda x: 0.26 * x ** 2 + 0.4
        curve = ax.plot(f, x_range=[0.2, 5.6], color=WAIT, stroke_width=5)
        self.play(Create(ax), run_time=0.8)
        self.play(Create(curve), run_time=1.4)

        t = ValueTracker(0.8)
        tan = always_redraw(lambda: ax.plot(
            lambda x: f(t.get_value()) + 0.52 * t.get_value() * (x - t.get_value()),
            x_range=[max(0.2, t.get_value() - 1.3), min(5.6, t.get_value() + 1.3)],
            color=TRIGGER, stroke_width=5))
        moving = always_redraw(lambda: Dot(ax.c2p(t.get_value(), f(t.get_value())),
                                           radius=0.09, color=TRIGGER))
        with self.narrate("Here is the tangent again, and here it is walking along the "
                          "curve. Watch the tangent itself, not the point."):
            self.add(tan, moving)
            self.play(FadeIn(moving), run_time=0.4)
            self.play(t.animate.set_value(5.0), run_time=4.0,
                      rate_func=rate_functions.ease_in_out_sine)
        turn = St.caption("the gradient is itself changing", TRIGGER, T_BODY, width=22)
        St.place(turn, St.SIDE, ay=0.6)
        with self.narrate("It is turning. The gradient is not a fixed number: it has a "
                          "gradient of its own."):
            self.play(FadeIn(turn), run_time=0.8)
        self.beat()
        self.remove(tan, moving)

        self.define("the second gradient", "How fast the steepness itself is changing.",
                    "risk", COST, at=DOWN * 2.6, hold=4.4)
        nota = VGroup(
            Text("V′(R)", font=FONT, font_size=T_SUB, color=TRIGGER),
            Text("→", font=FONT, font_size=T_SUB, color=MUTED),
            Text("V″(R)", font=FONT, font_size=T_SUB, color=COST)).arrange(RIGHT, buff=0.5)
        St.place(nota, St.SIDE, ay=-0.35)
        with self.narrate("One dash for the steepness. Two dashes for how fast the "
                          "steepness is changing. That is all the second one means."):
            self.play(FadeIn(nota), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the bend pays
        self.heading("And here is why that matters")
        ax2 = Axes(x_range=[0, 6, 1], y_range=[0, 6, 1], x_length=6.6, y_length=3.8,
                   axis_config=AXIS)
        St.place(ax2, St.STAGE, ay=0.15, fill=False)
        g = lambda x: 0.30 * x ** 2 + 0.3
        curve2 = ax2.plot(g, x_range=[0.3, 5.4], color=WAIT, stroke_width=5)
        yl = Text("value", font=FONT, font_size=T_TINY, color=MUTED)
        yl.next_to(ax2, UP, buff=0.14).align_to(ax2, LEFT)
        self.play(Create(ax2), FadeIn(yl), run_time=0.8)
        self.play(Create(curve2), run_time=1.4)

        lo, mid, hi = 1.4, 3.0, 4.6
        d_lo = Dot(ax2.c2p(lo, g(lo)), radius=0.09, color=COST)
        d_hi = Dot(ax2.c2p(hi, g(hi)), radius=0.09, color=MONEY)
        d_mid = Dot(ax2.c2p(mid, g(mid)), radius=0.09, color=TRIGGER)
        with self.narrate("Two futures, equally likely. One bad, one good, the same "
                          "distance either side of where we are now."):
            self.play(FadeIn(d_lo), FadeIn(d_hi), run_time=0.8)
            self.play(FadeIn(d_mid), run_time=0.5)

        chord = Line(ax2.c2p(lo, g(lo)), ax2.c2p(hi, g(hi)), color=MONEY,
                     stroke_width=4)
        avg_y = (g(lo) + g(hi)) / 2
        d_avg = Dot(ax2.c2p(mid, avg_y), radius=0.10, color=MONEY)
        with self.narrate("Join them. The middle of that line is the average of the two "
                          "values — what you get on average if the future goes one way "
                          "or the other."):
            self.play(Create(chord), run_time=1.0)
            self.play(FadeIn(d_avg), run_time=0.6)

        gap = DoubleArrow(ax2.c2p(mid, g(mid)), ax2.c2p(mid, avg_y), color=TRIGGER,
                          stroke_width=5, buff=0.02, tip_length=0.16)
        gl = St.caption("the bend is worth this much", TRIGGER, T_SMALL, width=22)
        gl.next_to(gap, RIGHT, buff=0.3)
        with self.narrate("And it is higher than the curve. The average of the two "
                          "values beats the value at the average. The gap is pure "
                          "bend — and it is exactly the gap chapter five was about."):
            self.play(GrowFromCenter(gap), run_time=0.9)
            self.play(FadeIn(gl), run_time=0.7)
            self.play(S.flash_around(gap, TRIGGER, run_time=2.0))
        self.beat()

        rule = St.caption("bends upwards → uncertainty adds value", MONEY,
                          T_SUB, width=44)
        St.place(rule, St.FOOT, pad=0.06)
        with self.narrate("So a value that bends upwards is worth more when the future "
                          "is uncertain than when it is not. That is the whole reason "
                          "the second gradient appears at all."):
            self.play(FadeIn(rule), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the other way
        self.heading("And the other way round")
        ax3 = Axes(x_range=[0, 6, 1], y_range=[0, 4, 1], x_length=5.4, y_length=2.8,
                   axis_config=AXIS)
        St.place(ax3, St.STAGE, ay=0.2, fill=False)
        h = lambda x: 3.4 - 0.10 * (x - 0.4) ** 2
        c3 = ax3.plot(h, x_range=[0.4, 5.6], color=COST, stroke_width=5)
        self.play(Create(ax3), run_time=0.7)
        self.play(Create(c3), run_time=1.2)
        ch2 = Line(ax3.c2p(1.4, h(1.4)), ax3.c2p(4.6, h(4.6)), color=MUTED,
                   stroke_width=4)
        with self.narrate("A curve that bends the other way loses by the same argument. "
                          "The chord sits below it, so uncertainty costs rather than "
                          "pays."):
            self.play(Create(ch2), run_time=1.0)
        both = St.points(["bends up → uncertainty pays",
                          "bends down → uncertainty costs",
                          "straight → uncertainty does nothing"],
                         colour=CHALK, dot_colour=TRIGGER, size=T_BODY, width=26)
        St.place(both, St.SIDE, ay=0.0)
        says = ["Bending up, uncertainty pays.",
                "Bending down, it costs.",
                "And a straight line — no bend at all — is the one case where "
                "uncertainty makes no difference whatsoever. Which is precisely why "
                "the textbook, which draws straight lines, never sees any of this."]
        for i, row in enumerate(both):
            with self.narrate(says[i]):
                self.play(FadeIn(row), run_time=0.7)
        self.beat()

        self.close_chapter([
            "two dashes: how fast the steepness changes",
            "a bend up puts the average above the curve",
            "so uncertainty adds value to a bent thing",
            "and does nothing at all to a straight one",
        ])
