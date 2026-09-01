import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter14(Chapter):
    CH = 14
    TITLE = "How steep is a curve?"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["scale", "flow", "clock", "money"]

    def body(self):
        # the key to the squiggles, before any of them is used again
        self.symbol_key(["V", "R"], region=St.FULL, hold=4.0)

        # ------------------------------------------------ gradient you know
        self.heading("You already know this bit")
        ax = Axes(x_range=[0, 6, 1], y_range=[0, 4, 1], x_length=6.4, y_length=3.4,
                  axis_config=AXIS)
        St.place(ax, St.STAGE, ay=0.1, fill=False)
        line = ax.plot(lambda x: 0.5 + 0.5 * x, x_range=[0, 6], color=WAIT,
                       stroke_width=5)
        with self.narrate("Start with a straight line, which you met at school. Its "
                          "steepness is one number, and it is the same everywhere "
                          "along it."):
            self.play(Create(ax), run_time=1.0)
            self.play(Create(line), run_time=1.4)

        a, b = 1.0, 4.0
        pa, pb = ax.c2p(a, 0.5 + 0.5 * a), ax.c2p(b, 0.5 + 0.5 * b)
        run = Line(pa, [pb[0], pa[1], 0], color=MUTED, stroke_width=4)
        rise = Line([pb[0], pa[1], 0], pb, color=TRIGGER, stroke_width=4)
        rl = Text("along", font=FONT, font_size=T_SMALL, color=MUTED)
        rl.next_to(run, DOWN, buff=0.18)
        ul = Text("up", font=FONT, font_size=T_SMALL, color=TRIGGER)
        ul.next_to(rise, RIGHT, buff=0.18)
        with self.narrate("Go along, and go up. Steepness is the up divided by the "
                          "along. Nothing more than that."):
            self.play(Create(run), FadeIn(rl), run_time=0.8)
            self.play(Create(rise), FadeIn(ul), run_time=0.8)
        frac = VGroup(Text("up", font=FONT, font_size=T_SUB, color=TRIGGER),
                      Line(LEFT * 0.7, RIGHT * 0.7, color=CHALK, stroke_width=3),
                      Text("along", font=FONT, font_size=T_SUB, color=MUTED)
                      ).arrange(DOWN, buff=0.18)
        St.place(frac, St.SIDE, ay=0.35)
        self.play(FadeIn(frac), run_time=0.8)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ a curve has no one answer
        self.heading("A curve has a different answer everywhere")
        ax2 = Axes(x_range=[0, 6, 1], y_range=[0, 5, 1], x_length=6.6, y_length=3.6,
                   axis_config=AXIS)
        St.place(ax2, St.STAGE, ay=0.1, fill=False)
        f = lambda x: 0.28 * x ** 2 + 0.3
        curve = ax2.plot(f, x_range=[0.2, 5.6], color=WAIT, stroke_width=5)
        with self.narrate("Now bend it. A curve is not equally steep everywhere. Down "
                          "here it is gentle. Up there it is steep."):
            self.play(Create(ax2), run_time=0.9)
            self.play(Create(curve), run_time=1.6)
        g1 = Line(ax2.c2p(0.6, f(0.6)) + LEFT * 0.5 + DOWN * 0.28,
                  ax2.c2p(0.6, f(0.6)) + RIGHT * 0.5 + UP * 0.28,
                  color=MONEY, stroke_width=5)
        g2 = Line(ax2.c2p(4.8, f(4.8)) + LEFT * 0.4 + DOWN * 1.05,
                  ax2.c2p(4.8, f(4.8)) + RIGHT * 0.4 + UP * 1.05,
                  color=COST, stroke_width=5)
        self.play(Create(g1), run_time=0.7)
        self.play(Create(g2), run_time=0.7)
        self.beat()

        # ------------------------------------------------ the chord collapses
        self.heading("So ask at one point only")
        self.play(FadeOut(g1), FadeOut(g2), run_time=0.4)
        x0 = 3.0
        dot = Dot(ax2.c2p(x0, f(x0)), radius=0.09, color=TRIGGER)
        h = ValueTracker(2.2)
        chord = always_redraw(lambda: Line(
            ax2.c2p(x0, f(x0)),
            ax2.c2p(x0 + h.get_value(), f(x0 + h.get_value())),
            color=MONEY, stroke_width=5))
        second = always_redraw(lambda: Dot(
            ax2.c2p(x0 + h.get_value(), f(x0 + h.get_value())),
            radius=0.08, color=MONEY))
        with self.narrate("Take the point you care about, and a second point further "
                          "along. Join them. That line has a steepness you can work "
                          "out — up over along, exactly as before."):
            self.play(FadeIn(dot), run_time=0.5)
            self.add(chord, second)
            self.play(FadeIn(second), run_time=0.5)
        self.beat()

        note = St.caption("now slide the second point in", TRIGGER, T_BODY, width=22)
        St.place(note, St.SIDE, ay=0.6)
        with self.narrate("Now slide the second point towards the first, and watch what "
                          "that line does."):
            self.play(FadeIn(note), run_time=0.6)
            self.play(h.animate.set_value(0.05), run_time=4.0,
                      rate_func=rate_functions.ease_in_out_sine)
        self.beat()

        tan = ax2.plot(lambda x: f(x0) + 0.56 * x0 * (x - x0), x_range=[1.4, 4.6],
                       color=TRIGGER, stroke_width=5)
        with self.narrate("It settles on one line: the line that just touches the curve "
                          "at that point, and does not cross it. That is the steepness "
                          "of the curve, there."):
            self.remove(chord, second)
            self.play(Create(tan), run_time=1.2)
            self.play(S.indicate(tan, TRIGGER))
        self.beat()

        self.define("the gradient", "How steep a curve is at one single point on it.",
                    "flow", TRIGGER, at=DOWN * 2.6, hold=4.2)
        self.clear_stage()

        # ------------------------------------------------ notation
        self.heading("And a shorthand for it")
        v = Text("V(R)", font=FONT, font_size=T_HEAD, color=WAIT)
        arrow = Arrow(LEFT * 0.7, RIGHT * 0.7, color=MUTED, stroke_width=5, buff=0)
        vp = Text("V′(R)", font=FONT, font_size=T_HEAD, color=TRIGGER)
        row = VGroup(v, arrow, vp).arrange(RIGHT, buff=0.7)
        St.place(row, St.FULL, ay=0.6)
        under = VGroup(
            St.caption("the value, at a level of takings", WAIT, T_SMALL, width=26),
            St.caption("how fast that value changes", TRIGGER, T_SMALL, width=26))
        under[0].next_to(v, DOWN, buff=0.45)
        under[1].next_to(vp, DOWN, buff=0.45)
        with self.narrate("Write the value of something as V of R — the value, when the "
                          "money coming in is R."):
            self.play(Write(v), run_time=1.0)
            self.play(FadeIn(under[0]), run_time=0.6)
        with self.narrate("Then V, with a dash, means its gradient: how fast that value "
                          "changes as the money coming in changes. A dash is the whole "
                          "of the notation. There is nothing else to learn."):
            self.play(GrowArrow(arrow), run_time=0.5)
            self.play(Write(vp), run_time=1.0)
            self.play(FadeIn(under[1]), run_time=0.6)
        self.beat()

        ex = VGroup(
            Text("R²", font=FONT, font_size=T_SUB, color=WAIT),
            Text("→", font=FONT, font_size=T_SUB, color=MUTED),
            Text("2R", font=FONT, font_size=T_SUB, color=TRIGGER)).arrange(RIGHT, buff=0.5)
        ex2 = VGroup(
            Text("R³", font=FONT, font_size=T_SUB, color=WAIT),
            Text("→", font=FONT, font_size=T_SUB, color=MUTED),
            Text("3R²", font=FONT, font_size=T_SUB, color=TRIGGER)).arrange(RIGHT, buff=0.5)
        exs = VGroup(ex, ex2).arrange(DOWN, buff=0.5)
        St.place(exs, St.FULL, ay=-0.6)
        with self.narrate("And one fact you will need, which you can take on trust or "
                          "check on paper. R squared has gradient two R. R cubed has "
                          "gradient three R squared."):
            self.play(FadeIn(ex), run_time=0.8)
            self.play(FadeIn(ex2), run_time=0.8)
        gen = Text("R^x   →   x R^(x−1)", font=FONT, font_size=T_SUB, color=MONEY)
        St.place(gen, St.FOOT, pad=0.06)
        with self.narrate("In general: bring the power down in front, and knock one off "
                          "it. That single rule is all the calculus this film needs."):
            self.play(Write(gen), run_time=1.6)
            self.play(S.flash_around(gen, MONEY, run_time=2.0))
        self.beat()

        self.close_chapter([
            "steepness of a line: up over along",
            "a curve is a different steepness everywhere",
            "slide two points together → the tangent",
            "and the rule: R^x has gradient x R^(x−1)",
        ])
