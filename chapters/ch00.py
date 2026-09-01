import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter00(Chapter):
    CH = 0
    TITLE = "Two things that should not happen"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["people", "money", "door"]

    def body(self):
        # ------------------------------------------------ the farmer
        self.heading("A farmer who will not stop")
        farmer = stick.StickFigure("A farmer", CHALK, hat="flat", scale=1.05)
        St.place(farmer, St.STAGE, ax=-0.30, ay=-0.10)
        field = Line(LEFT * 2.4, RIGHT * 2.4, color=MUTED, stroke_width=3)
        field.next_to(farmer, DOWN, buff=0.32)

        with self.narrate("Here is a farmer. For four years running, his farm has "
                          "lost money."):
            self.play(FadeIn(farmer), Create(field), run_time=1.2)
            self.play(FadeIn(farmer.label()), run_time=0.5)

        bars = VGroup()
        for i, h in enumerate([0.8, 1.1, 1.5, 1.9]):
            b = Rectangle(width=0.72, height=h, color=COST, stroke_width=3,
                          fill_color=COST, fill_opacity=0.30)
            lab = Text(f"year {i + 1}", font=FONT, font_size=T_TINY, color=MUTED)
            g = VGroup(b, lab)
            lab.next_to(b, DOWN, buff=0.18)
            bars.add(g)
        bars.arrange(RIGHT, buff=0.5, aligned_edge=DOWN)
        St.place(bars, St.SIDE, ay=-0.1)
        St.collapse_bars(VGroup(*[g[0] for g in bars]))

        with self.narrate("Every year, more money went out of the farm than came in. "
                          "And every year the hole got deeper."):
            self.play(LaggedStartMap(FadeIn, VGroup(*[g[1] for g in bars]),
                                     lag_ratio=0.2), run_time=1.0)
            self.play(St.grow_bars(VGroup(*[g[0] for g in bars])))
            self.play(farmer.mood("worried"), run_time=0.4)

        with self.narrate("Anybody watching would tell him to stop. He does not stop. "
                          "He keeps farming."):
            self.play(farmer.pace(2, run_time=2.2))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the owner
        self.heading("An owner who will not build")
        nell = stick.nell(scale=1.1)
        St.place(nell, St.STAGE, ax=-0.45, ay=-0.10)
        plot = DashedLine(LEFT * 1.5, RIGHT * 1.5, color=MUTED, stroke_width=4)
        plotl = Text("empty ground", font=FONT, font_size=T_SMALL, color=MUTED)
        plot_g = VGroup(plot, plotl)
        plotl.next_to(plot, DOWN, buff=0.22)
        St.place(plot_g, St.STAGE, ax=0.62, ay=-0.35)

        with self.narrate("And here is Nell. Nell owns a small factory, and she has "
                          "the chance to build a second one."):
            self.play(FadeIn(nell), FadeIn(nell.label()), run_time=0.9)
            self.play(Create(plot), FadeIn(plotl), run_time=0.9)

        sums = St.caption("the sums say yes", MONEY, T_SUB, width=20)
        St.place(sums, St.SIDE, ay=0.45)
        with self.narrate("The sums say the new factory would earn her far more than "
                          "her money is costing her. On paper, she should build it "
                          "tomorrow."):
            self.play(nell.mood("thinking"), run_time=0.4)
            self.play(FadeIn(sums), run_time=0.8)
            self.play(S.flash_around(sums, MONEY))

        no = St.caption("not yet", COST, T_SUB, width=20)
        St.place(no, St.SIDE, ay=-0.25)
        with self.narrate("She refuses. Not this year. Perhaps not next year either."):
            self.play(FadeIn(no), run_time=0.7)
            self.play(nell.shrug(), run_time=1.0)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the claim
        self.drop_heading()
        claim = St.points([
            "both look irrational",
            "both are, in fact, correct",
            "by the end you will know why",
        ], colour=CHALK, dot_colour=TRIGGER, size=T_SUB, width=30)
        St.place(claim, St.WIDE)
        says = ["Both of them look irrational.",
                "Both of them are, in fact, behaving correctly.",
                "And by the end of this film, you will be able to say exactly why — "
                "in your own words."]
        for i, row in enumerate(claim):
            with self.narrate(says[i]):
                self.play(FadeIn(row), run_time=0.8)
            self.beat(0.4)
        self.play(FadeOut(claim), run_time=0.6)

        # ------------------------------------------------ the cast
        self.heading("The people it happens to")
        n = stick.nell(scale=1.0)
        m = stick.marshall(scale=1.0)
        a = stick.ava(scale=1.0)
        row = VGroup(n, m, a).arrange(RIGHT, buff=2.4)
        St.place(row, St.FULL, ay=-0.05)
        ln, lm, la = n.label(), m.label(), a.label()

        with self.narrate("Nell makes the decisions. She owns the factory. Every "
                          "choice in this film is hers, and she is sensible — not "
                          "timid."):
            self.play(FadeIn(n), FadeIn(ln), run_time=0.8)
            self.play(n.nod(), run_time=0.8)

        with self.narrate("Marshall carries the textbook. He always gives the standard "
                          "answer. He is right when the world is calm, and badly wrong "
                          "when it is not."):
            self.play(FadeIn(m), FadeIn(lm), run_time=0.8)
            b = m.say("The rule is simple.", direction=UP, width=3.0)
            self.play(FadeIn(b), run_time=0.5)
            self.play(FadeOut(b), run_time=0.4)

        with self.narrate("And Ava asks the questions you would ask. She never lets "
                          "Marshall get away with anything.", v="c"):
            self.play(FadeIn(a), FadeIn(la), run_time=0.8)
            q = a.say("Hang on. Why?", direction=UP, width=2.6)
            self.play(FadeIn(q), a.mood("thinking"), run_time=0.5)
            self.play(FadeOut(q), run_time=0.4)

        with self.narrate("We start from nothing at all. No economics is assumed. "
                          "Not one word of it."):
            self.play(*[f.nod() for f in (n, m, a)], run_time=0.9)
        self.beat()

        self.close_chapter([
            "a farmer absorbs losses, and will not shut",
            "an owner refuses a project the sums approve",
            "both are correct — that is the film",
        ])
