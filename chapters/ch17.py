import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter17(Chapter):
    CH = 17
    TITLE = "The equation the paper actually solves"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["scale", "money", "risk", "flow"]

    def body(self):
        # the key to the squiggles, before any of them is used again
        self.symbol_key(["V", "rho", "sigma", "mu"], region=St.FULL, hold=4.0)

        # ------------------------------------------------ a curve near a point
        self.heading("A curve, very close up")
        ax = Axes(x_range=[0, 6, 1], y_range=[0, 5, 1], x_length=6.2, y_length=3.2,
                  axis_config=AXIS)
        St.place(ax, St.STAGE, ay=0.2, fill=False)
        f = lambda x: 0.26 * x ** 2 + 0.5
        curve = ax.plot(f, x_range=[0.4, 5.4], color=WAIT, stroke_width=5)
        x0 = 3.0
        dot = Dot(ax.c2p(x0, f(x0)), radius=0.09, color=TRIGGER)
        tan = ax.plot(lambda x: f(x0) + 0.52 * x0 * (x - x0), x_range=[1.4, 4.6],
                      color=TRIGGER, stroke_width=4)
        with self.narrate("Take the value curve and stand at one point on it. Close up, "
                          "the tangent is a good description of the curve."):
            self.play(Create(ax), run_time=0.8)
            self.play(Create(curve), run_time=1.4)
            self.play(FadeIn(dot), Create(tan), run_time=1.0)

        with self.narrate("But it is not perfect. Move a little way, and the real curve "
                          "has lifted off the tangent — by an amount that depends on "
                          "the bend."):
            gap = DoubleArrow(ax.c2p(4.4, f(x0) + 0.52 * x0 * (4.4 - x0)),
                              ax.c2p(4.4, f(4.4)), color=COST, stroke_width=4,
                              buff=0.02, tip_length=0.14)
            self.play(GrowFromCenter(gap), run_time=0.9)
            gl = St.caption("the bend, again", COST, T_SMALL, width=18)
            gl.next_to(gap, RIGHT, buff=0.25)
            self.play(FadeIn(gl), run_time=0.6)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the expansion
        self.heading("So the expected change has two parts")
        eq = Text("E[dV]  =  V′(R) E[dR]  +  ½ V″(R) E[dR²]",
                  font=FONT, font_size=T_SUB, color=CHALK)
        St.place(eq, St.FULL, ay=0.85)
        with self.narrate("Which gives the line the appendix opens with. The expected "
                          "change in value has two pieces."):
            self.play(Write(eq), run_time=2.4)

        p1 = VGroup(Text("V′(R) E[dR]", font=FONT, font_size=T_BODY, color=TRIGGER),
                    St.caption("the slope, times the step", MUTED, T_SMALL, width=24)
                    ).arrange(DOWN, buff=0.2)
        p2 = VGroup(Text("½ V″(R) E[dR²]", font=FONT, font_size=T_BODY, color=COST),
                    St.caption("the bend, times the squared step", MUTED, T_SMALL,
                               width=26)).arrange(DOWN, buff=0.2)
        parts = VGroup(p1, p2).arrange(RIGHT, buff=1.6)
        St.place(parts, St.FULL, ay=0.0)
        with self.narrate("The first is the tangent's answer: the slope, times how far "
                          "you moved."):
            self.play(FadeIn(p1), run_time=0.9)
        with self.narrate("The second is the correction for the bend: a half of the "
                          "second gradient, times the square of the step. And we know "
                          "what that square is — it is the one thing randomness leaves "
                          "behind."):
            self.play(FadeIn(p2), run_time=0.9)
        self.beat()

        sub = Text("=  V′(R) μR dt  +  ½ V″(R) σ²R² dt", font=FONT,
                   font_size=T_SUB, color=CHALK)
        St.place(sub, St.FULL, ay=-0.75)
        with self.narrate("Put the two facts from the last chapter in, and every piece "
                          "of it is now something we have already built."):
            self.play(Write(sub), run_time=2.2)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the balance
        self.heading("Now the one economic idea")
        left = VGroup(cards.icon("flow", TRIGGER, 1.6),
                      St.caption("what holding it gains you", TRIGGER, T_SMALL,
                                 width=22)).arrange(DOWN, buff=0.3)
        right = VGroup(cards.icon("money", MONEY, 1.6),
                       St.caption("what your money could earn anywhere",
                                  MONEY, T_SMALL, width=24)).arrange(DOWN, buff=0.3)
        pair = VGroup(left, right).arrange(RIGHT, buff=3.2)
        St.place(pair, St.FULL, ay=0.5)
        pivot = Triangle(color=MUTED, stroke_width=3).scale(0.3)
        beam = Line(LEFT * 3.0, RIGHT * 3.0, color=MUTED, stroke_width=5)
        bal = VGroup(beam, pivot.next_to(beam, DOWN, buff=0.0))
        St.place(bal, St.FULL, ay=-0.35, fill=False)
        with self.narrate("The chance to build is an asset you are holding. It pays you "
                          "nothing while you hold it — no rent, no revenue — so all it "
                          "can offer is the gain in its own value."):
            self.play(FadeIn(left), run_time=0.9)
        with self.narrate("And your money could have been earning the ordinary return "
                          "somewhere else. In equilibrium those two must match, or "
                          "nobody would hold it."):
            self.play(FadeIn(right), run_time=0.9)
            self.play(Create(bal), run_time=0.9)
            self.play(S.indicate(bal, TRIGGER))
        self.beat()

        bal_eq = Text("E[dV]  =  ρ V dt", font=FONT, font_size=T_HEAD, color=TRIGGER)
        St.place(bal_eq, St.FOOT, pad=0.06)
        with self.narrate("Expected gain equals the normal return. One line."):
            self.play(Write(bal_eq), run_time=1.6)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the differential equation
        self.heading("Put them together and divide by dt")
        s1 = Text("V′μR dt  +  ½V″σ²R² dt   =   ρV dt", font=FONT, font_size=T_SUB,
                  color=CHALK)
        St.place(s1, St.FULL, ay=0.9)
        self.play(Write(s1), run_time=2.0)
        with self.narrate("Every single term has a d t in it. So divide the whole line "
                          "by d t, and every d t disappears at once."):
            self.play(S.flash_around(s1, TRIGGER, run_time=2.0))
        s2 = Text("½ σ²R² V″(R)  +  μR V′(R)  −  ρV(R)  =  0", font=FONT,
                  font_size=T_SUB, color=TRIGGER)
        St.place(s2, St.FULL, ay=0.15)
        with self.narrate("Tidy it up, bring everything to one side, and this is "
                          "equation A one of the appendix. It is the whole of the "
                          "paper's mathematics in a single line, and you have just "
                          "watched every piece of it being built."):
            self.play(Write(s2), run_time=2.8)
            self.play(S.flash_around(s2, TRIGGER, run_time=2.4))
        self.wait(1.6)

        read = St.points(["a bend term, from the choppiness",
                          "a slope term, from the drift",
                          "and the ordinary return being given up"],
                         colour=CHALK, dot_colour=MUTED, size=T_SMALL, width=34)
        St.place(read, St.FULL, ay=-0.78)
        says = ["Read it left to right. A bend term, carrying the choppiness.",
                "A slope term, carrying the drift.",
                "And the ordinary return being given up by holding on."]
        for i, row in enumerate(read):
            with self.narrate(says[i]):
                self.play(FadeIn(row), run_time=0.7)
        self.beat()

        self.close_chapter([
            "close up, a curve is a tangent plus a bend",
            "so E[dV] has a slope term and a bend term",
            "waiting pays nothing, so gain = normal return",
            "divide by the slice, and the equation is left",
        ])
