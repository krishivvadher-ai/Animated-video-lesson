import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter18(Chapter):
    CH = 18
    TITLE = "Solving it with a guess"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["scale", "flow", "money", "door"]

    def body(self):
        # ------------------------------------------------ why a power
        self.heading("Why guess a power?")
        eq = Text("½ σ²R² V″  +  μR V′  −  ρV  =  0", font=FONT, font_size=T_SUB,
                  color=TRIGGER)
        St.place(eq, St.FULL, ay=0.9)
        self.play(Write(eq), run_time=1.8)

        obs = St.caption("R² sits with V″ · R sits with V′", MUTED, T_BODY, width=34)
        St.place(obs, St.FULL, ay=0.35)
        with self.narrate("Look at the shape of it. Wherever there are two dashes there "
                          "is an R squared, and wherever there is one dash there is a "
                          "single R. Each differentiation is paid for with exactly one "
                          "R."):
            self.play(FadeIn(obs), run_time=0.9)
            self.play(S.indicate(eq, TRIGGER))

        pw = VGroup(
            Text("V = R^x", font=FONT, font_size=T_SUB, color=WAIT),
            Text("V′ = x R^(x−1)", font=FONT, font_size=T_SUB, color=MONEY),
            Text("R V′ = x R^x", font=FONT, font_size=T_SUB, color=MONEY),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        St.place(pw, St.FULL, ay=-0.5)
        with self.narrate("So try a power. Using the rule from chapter fourteen, the "
                          "gradient of R to the x is x times R to the x minus one."):
            self.play(Write(pw[0]), run_time=1.0)
            self.play(Write(pw[1]), run_time=1.4)
        with self.narrate("Multiply that by the R sitting next to it, and the power "
                          "comes straight back to what it was. The shape survives. That "
                          "is why a power is the right guess."):
            self.play(Write(pw[2]), run_time=1.4)
            self.play(S.flash_around(pw[2], MONEY))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ substitute
        self.heading("Substitute, and watch it collapse")
        rows = VGroup(
            Text("V  =  R^x", font=FONT, font_size=T_BODY, color=WAIT),
            Text("R V′  =  x R^x", font=FONT, font_size=T_BODY, color=MONEY),
            Text("R² V″  =  x(x − 1) R^x", font=FONT, font_size=T_BODY, color=COST),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        St.place(rows, St.FULL, ay=0.75)
        says = ["The value itself is R to the x.",
                "R times its gradient is x, times R to the x.",
                "And R squared times the second gradient is x, times x minus one, "
                "times R to the x. Every one of them is the same R to the x, with a "
                "different number in front."]
        for i, row in enumerate(rows):
            with self.narrate(says[i]):
                self.play(Write(row), run_time=1.3)
        self.beat()

        sub = Text("[ ½σ² x(x−1)  +  μx  −  ρ ]  R^x  =  0", font=FONT,
                   font_size=T_SUB, color=CHALK)
        St.place(sub, St.FULL, ay=-0.1)
        with self.narrate("Put them into the equation and the whole R to the x factors "
                          "out of every term."):
            self.play(Write(sub), run_time=2.2)

        quad = Text("½σ² x(x−1)  +  μx  −  ρ  =  0", font=FONT, font_size=T_SUB,
                    color=TRIGGER)
        St.place(quad, St.FULL, ay=-0.75)
        with self.narrate("R to the x is never zero, so the bracket must be. And the "
                          "bracket is a quadratic — the thing you solved at school. "
                          "That is equation A two."):
            self.play(Write(quad), run_time=2.0)
            self.play(S.flash_around(quad, TRIGGER, run_time=2.0))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ two roots
        self.heading("A quadratic has two answers")
        ax = Axes(x_range=[-2, 4, 1], y_range=[-2, 3, 1], x_length=6.4, y_length=3.4,
                  axis_config=AXIS)
        St.place(ax, St.STAGE, ay=0.1, fill=False)
        q = lambda x: 0.5 * 0.04 * x * (x - 1) * 25 - 0.05 * 25
        para = ax.plot(lambda x: 0.42 * (x - 1.0) ** 2 - 1.35, x_range=[-1.6, 3.6],
                       color=WAIT, stroke_width=5)
        self.play(Create(ax), run_time=0.8)
        self.play(Create(para), run_time=1.4)
        r1 = Dot(ax.c2p(-0.79, 0), radius=0.10, color=COST)
        r2 = Dot(ax.c2p(2.79, 0), radius=0.10, color=MONEY)
        la = Text("α", font=FONT, font_size=T_SUB, color=COST)
        la.next_to(r1, DOWN, buff=0.2)
        lb = Text("β", font=FONT, font_size=T_SUB, color=MONEY)
        lb.next_to(r2, DOWN, buff=0.2)
        with self.narrate("A quadratic crosses zero twice. The paper calls the two "
                          "answers alpha and beta. One of them is negative. The other "
                          "is bigger than one."):
            self.play(FadeIn(r1), FadeIn(la), run_time=0.8)
            self.play(FadeIn(r2), FadeIn(lb), run_time=0.8)
        self.beat()

        gen = Text("V(R)  =  A R^α  +  B R^β", font=FONT, font_size=T_SUB, color=CHALK)
        St.place(gen, St.SIDE, ay=0.55)
        with self.narrate("So the general answer is a bit of each, with two unknown "
                          "amounts A and B."):
            self.play(Write(gen), run_time=1.6)

        kill = St.caption("waiting is worth nothing\nwhen there is nothing coming in",
                          COST, T_SMALL, width=24)
        St.place(kill, St.SIDE, ay=-0.35)
        with self.narrate("Now one piece of economics kills half of it. If the money "
                          "coming in falls to nothing, the chance to build is worth "
                          "nothing. But R to a negative power blows up as R goes to "
                          "zero. So A has to be zero."):
            self.play(FadeIn(kill), run_time=0.9)
            strike = Line(gen.get_left() + RIGHT * 2.0, gen.get_left() + RIGHT * 3.5,
                          color=COST, stroke_width=5)
            self.play(Create(strike), run_time=0.9)
        left = Text("V(R)  =  B R^β", font=FONT, font_size=T_SUB, color=TRIGGER)
        St.place(left, St.FOOT, pad=0.06)
        with self.narrate("What is left is the paper's equation two, which chapter "
                          "twelve drew as a curve without ever saying where it came "
                          "from."):
            self.play(Write(left), run_time=1.6)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ completing the square
        self.heading("And with no drift, school algebra finishes it")
        steps = VGroup(
            Text("μ = 0:      ½σ² x(x−1)  =  ρ", font=FONT, font_size=T_BODY,
                 color=CHALK),
            Text("x(x−1)  =  2ρ ÷ σ²", font=FONT, font_size=T_BODY, color=CHALK),
            Text("x² − x  =  2ρ ÷ σ²", font=FONT, font_size=T_BODY, color=CHALK),
            Text("(x − ½)²  =  ¼ + 2ρ ÷ σ²", font=FONT, font_size=T_BODY, color=MONEY),
            Text("(x − ½)²  =  [1 + 8ρ ÷ σ²] ÷ 4", font=FONT, font_size=T_BODY,
                 color=MONEY),
            Text("β  =  ½ [ 1 + √(1 + 8ρ ÷ σ²) ]", font=FONT, font_size=T_SUB,
                 color=TRIGGER),
        ).arrange(DOWN, buff=0.34, aligned_edge=LEFT)
        St.place(steps, St.FULL, ay=0.0)
        says = ["Set the drift to zero, as the main text does.",
                "Divide through by a half sigma squared.",
                "Multiply out the bracket.",
                "Now complete the square — add a quarter to both sides, which is "
                "exactly what you were taught to do.",
                "Tidy the right-hand side over a common denominator of four.",
                "Square-root both sides, take the bigger answer, and there is the "
                "formula from chapter thirteen. Every symbol in it has now been "
                "derived on screen."]
        for i, row in enumerate(steps):
            with self.narrate(says[i]):
                self.play(Write(row), run_time=1.2)
        self.play(S.flash_around(steps[5], TRIGGER, run_time=2.4))
        self.wait(1.6)

        self.close_chapter([
            "each dash is paid for with exactly one R",
            "so a power survives, and R^x factors out",
            "leaving a quadratic with roots α and β",
            "complete the square, and β is the formula",
        ])
