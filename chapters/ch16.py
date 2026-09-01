import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter16(Chapter):
    CH = 16
    TITLE = "One small random step"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["fog", "clock", "risk", "scale"]

    def body(self):
        # the key to the squiggles, before any of them is used again
        self.symbol_key(["R", "sigma", "mu", "dt", "dR"], region=St.FULL, hold=4.0)

        # ------------------------------------------------ the step
        self.heading("A tiny slice of time")
        ax = Axes(x_range=[0, 6, 1], y_range=[0, 4, 1], x_length=6.6, y_length=3.2,
                  axis_config=AXIS)
        St.place(ax, St.STAGE, ay=0.15, fill=False)
        path = ax.plot_line_graph(
            x_values=[0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0],
            y_values=[2.0, 2.3, 2.1, 2.5, 2.35, 2.7, 2.55],
            line_color=WAIT, add_vertex_dots=False, stroke_width=4)
        with self.narrate("Here is the money coming in, wandering about as it does. Cut "
                          "out one tiny slice of time from it."):
            self.play(Create(ax), run_time=0.8)
            self.play(Create(path), run_time=1.6)

        band = Rectangle(width=0.7, height=2.4, color=TRIGGER, stroke_width=3,
                         fill_color=TRIGGER, fill_opacity=0.12)
        band.move_to(ax.c2p(3.0, 2.0))
        dt = Text("dt", font=FONT, font_size=T_SUB, color=TRIGGER)
        dt.next_to(band, DOWN, buff=0.25)
        with self.narrate("Call the length of that slice d t. The d is just shorthand "
                          "for a change in something, so d t is a change in time — a "
                          "very small one."):
            self.play(FadeIn(band), FadeIn(dt), run_time=0.9)
        self.beat()

        dr = VGroup(Text("dR", font=FONT, font_size=T_SUB, color=WAIT),
                    St.caption("the change in the money\ncoming in, over that slice",
                               MUTED, T_SMALL, width=24)).arrange(DOWN, buff=0.25)
        St.place(dr, St.SIDE, ay=0.4)
        with self.narrate("And d R is the change in the money coming in over that same "
                          "slice. Nobody knows which way it will go."):
            self.play(FadeIn(dr), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ two facts
        self.heading("Two facts about that step")
        one = VGroup(
            Text("E[dR]  =  μ R dt", font=FONT, font_size=T_SUB, color=MONEY),
            St.caption("on average it drifts, at rate μ", MUTED, T_SMALL, width=30),
        ).arrange(DOWN, buff=0.22)
        two = VGroup(
            Text("Var[dR]  =  σ² R² dt", font=FONT, font_size=T_SUB, color=COST),
            St.caption("and it scatters, by the choppiness σ", MUTED, T_SMALL, width=32),
        ).arrange(DOWN, buff=0.22)
        both = VGroup(one, two).arrange(DOWN, buff=0.9)
        St.place(both, St.FULL, ay=0.35)
        with self.narrate("The paper writes down two facts about it. E square brackets "
                          "means on average. On average, the money drifts by a rate "
                          "called the drift, times where it is now, times the length "
                          "of the slice."):
            self.play(Write(one[0]), run_time=1.6)
            self.play(FadeIn(one[1]), run_time=0.6)
        self.beat()
        with self.narrate("And around that average it scatters. The scatter is measured "
                          "by the choppiness from chapter eleven, squared, "
                          "times where it is now, squared, times the slice."):
            self.play(Write(two[0]), run_time=1.6)
            self.play(FadeIn(two[1]), run_time=0.6)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ why the square survives
        self.heading("Why the square does not cancel")
        up = VGroup(Text("+2", font=FONT, font_size=T_HEAD, color=MONEY),
                    Text("−2", font=FONT, font_size=T_HEAD, color=COST)
                    ).arrange(RIGHT, buff=1.4)
        St.place(up, St.STAGE, ay=0.85)
        avg1 = Text("average  =  0", font=FONT, font_size=T_SUB, color=MUTED)
        avg1.next_to(up, DOWN, buff=0.5)
        with self.narrate("Here is the thing that makes all of this work. Take a step "
                          "up and a step down, equally likely. Add them and average. "
                          "They cancel to nothing."):
            self.play(FadeIn(up), run_time=0.8)
            self.play(Write(avg1), run_time=1.0)
        self.beat()

        sq = VGroup(Text("(+2)² = 4", font=FONT, font_size=T_HEAD, color=MONEY),
                    Text("(−2)² = 4", font=FONT, font_size=T_HEAD, color=MONEY)
                    ).arrange(RIGHT, buff=1.0)
        St.place(sq, St.STAGE, ay=-0.35)
        avg2 = Text("average  =  4", font=FONT, font_size=T_SUB, color=TRIGGER)
        avg2.next_to(sq, DOWN, buff=0.5)
        with self.narrate("Now square them first. Minus two squared is four, the same "
                          "as plus two squared. Squaring throws the minus sign away, so "
                          "the average of the squares is not nothing at all."):
            self.play(FadeIn(sq), run_time=1.0)
            self.play(Write(avg2), run_time=1.0)
            self.play(S.indicate(avg2, TRIGGER))
        self.beat()

        key = St.caption("randomness vanishes on average — but not when squared",
                         TRIGGER, T_SUB, width=54)
        St.place(key, St.FOOT, pad=0.06)
        with self.narrate("Randomness disappears when you average it, and survives when "
                          "you square it first. That is the whole reason a second "
                          "gradient — which multiplies a square — has anything to say "
                          "here."):
            self.play(FadeIn(key), run_time=1.0)
            self.play(S.flash_around(key, TRIGGER, run_time=2.0))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ E[dR^2]
        self.heading("So work out the square")
        l1 = Text("E[dR²]  =  (E[dR])²  +  Var[dR]", font=FONT, font_size=T_SUB,
                  color=CHALK)
        l2 = Text("=  μ²R² dt²  +  σ²R² dt", font=FONT, font_size=T_SUB, color=CHALK)
        l3 = Text("≈  σ²R² dt", font=FONT, font_size=T_SUB, color=TRIGGER)
        lines = VGroup(l1, l2, l3).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        St.place(lines, St.FULL, ay=0.25)
        with self.narrate("The average of the square is the square of the average, plus "
                          "the scatter. That is a standard fact about averages, and it "
                          "is the only one we borrow."):
            self.play(Write(l1), run_time=1.8)
        with self.narrate("Put the two facts in, and you get a d t squared term and a d "
                          "t term."):
            self.play(Write(l2), run_time=1.8)
        self.beat()

        tiny = St.caption("dt is tiny — so dt² is tinier still", MUTED, T_BODY, width=34)
        St.place(tiny, St.FOOT, pad=0.06)
        with self.narrate("And now the step that makes the whole thing tractable. If d "
                          "t is a hundredth, d t squared is a ten-thousandth. Make the "
                          "slice small enough and the squared term is nothing next to "
                          "the other one. So drop it."):
            self.play(FadeIn(tiny), run_time=0.9)
            strike = Line(l2.get_left() + RIGHT * 1.15, l2.get_left() + RIGHT * 3.4,
                          color=COST, stroke_width=4)
            self.play(Create(strike), run_time=0.8)
            self.play(Write(l3), run_time=1.4)
            self.play(S.flash_around(l3, TRIGGER))
        self.beat()

        self.close_chapter([
            "dt is a tiny slice of time; dR the change in it",
            "on average it drifts; around that it scatters",
            "a square keeps what an average throws away",
            "so the squared step survives, and nothing else does",
        ])
