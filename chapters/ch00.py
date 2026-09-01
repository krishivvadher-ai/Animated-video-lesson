import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.theme import *


class Chapter00(Chapter):
    CH = 0
    TITLE = "Two things that should not happen"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ['people', 'money', 'door']

    def body(self):
        # ---------------------------------------------------- the farmer
        farmer = stick.StickFigure("A farmer", CHALK, hat="flat", scale=1.15)
        farmer.shift(LEFT * 4.2 + DOWN * 0.6)
        flabel = farmer.label()
        field = VGroup(*[Line(LEFT * 0.5, RIGHT * 0.5, color=MUTED, stroke_width=3)
                         .shift(DOWN * 1.9 + RIGHT * x) for x in np.linspace(-1.2, 5.6, 8)])

        with self.narrate("Here is a farmer. For four years running, his farm has "
                          "lost money."):
            self.play(FadeIn(farmer), FadeIn(flabel), Create(field), run_time=1.6)

        years = VGroup()
        for i, y in enumerate(["Year 1", "Year 2", "Year 3", "Year 4"]):
            bar = Rectangle(width=0.8, height=0.9, color=COST, stroke_width=3,
                            fill_color=COST, fill_opacity=0.25)
            bar.move_to(RIGHT * (0.4 + i * 1.35) + UP * 0.4)
            lab = Text(y, font=FONT, font_size=T_SMALL, color=MUTED)
            lab.next_to(bar, DOWN, buff=0.20)
            amt = Text("loss", font=FONT, font_size=T_SMALL, color=COST)
            amt.next_to(bar, UP, buff=0.14)
            years.add(VGroup(bar, lab, amt))

        with self.narrate("Every year, more money went out of the farm than came in."):
            for y in years:
                self.play(FadeIn(y, shift=UP * 0.2), run_time=0.45)
            self.play(farmer.mood("worried"), run_time=0.4)

        with self.narrate("Anybody watching would tell him to stop. He does not stop. "
                          "He keeps farming."):
            self.play(farmer.pace(2, run_time=2.4))

        self.play(FadeOut(years), FadeOut(field), run_time=0.6)
        self.play(farmer.animate.shift(LEFT * 0.6).scale(0.75), FadeOut(flabel),
                  run_time=0.6)

        # ---------------------------------------------------- the owner
        nell = stick.nell(scale=1.2).shift(RIGHT * 1.6 + DOWN * 0.6)
        nlab = nell.label()
        plot = DashedLine(RIGHT * 3.8 + DOWN * 1.7, RIGHT * 6.2 + DOWN * 1.7,
                          color=MUTED, stroke_width=3)
        empty = Text("empty ground", font=FONT, font_size=T_SMALL, color=MUTED)
        empty.next_to(plot, DOWN, buff=0.2)

        with self.narrate("And here is Nell. Nell owns a small factory, and she has "
                          "the chance to build a second one."):
            self.play(FadeIn(nell), FadeIn(nlab), run_time=1.0)
            self.play(Create(plot), FadeIn(empty), run_time=0.9)

        with self.narrate("The sums say the new factory would earn her far more than "
                          "her money is costing her. On paper, she should build it "
                          "tomorrow."):
            th = nell.think("The sums say yes.", direction=UP)
            self.play(FadeIn(th), nell.mood("thinking"), run_time=0.8)
            self.wait(1.2)
            self.play(FadeOut(th), run_time=0.4)

        with self.narrate("She refuses. Not this year. Perhaps not next year either."):
            no = nell.say("Not yet.", direction=UP)
            self.play(FadeIn(no), run_time=0.6)
            self.wait(1.0)
            self.play(FadeOut(no), run_time=0.4)

        # ---------------------------------------------------- the claim
        self.clear_stage()
        claim = cards.bullet_list([
            "Both of them look irrational.",
            "Both are, in fact, correct.",
            "By the end you will know why.",
        ], width=44)
        claim.move_to(ORIGIN)
        with self.narrate("Both of them look irrational."):
            self.play(FadeIn(claim[0], shift=RIGHT * 0.3), run_time=0.6)
        with self.narrate("Both of them are, in fact, behaving correctly."):
            self.play(FadeIn(claim[1], shift=RIGHT * 0.3), run_time=0.6)
        self.beat()
        with self.narrate("And by the end of this film, you will be able to say "
                          "exactly why — in your own words."):
            self.play(FadeIn(claim[2], shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.6)
        self.play(FadeOut(claim), run_time=0.6)

        # ---------------------------------------------------- the cast
        self.line("This is going to take a while, so let me introduce the people "
                  "it happens to.")

        n = stick.nell(scale=1.05)
        m = stick.marshall(scale=1.05)
        a = stick.ava(scale=1.05)
        row = VGroup(n, m, a).arrange(RIGHT, buff=2.3).shift(DOWN * 0.3)
        ln, lm, la = n.label(), m.label(), a.label()

        with self.narrate("Nell makes the decisions. She owns the factory. Every "
                          "choice in this film is hers, and she is sensible — not timid."):
            self.play(FadeIn(n), FadeIn(ln), run_time=0.8)
            self.play(n.nod(), run_time=0.8)

        with self.narrate("Marshall carries the textbook. He always gives the "
                          "standard answer. He is right when the world is calm, and "
                          "badly wrong when it is not."):
            self.play(FadeIn(m), FadeIn(lm), run_time=0.8)
            b = m.say("The rule is simple.", direction=UP, width=3.0)
            self.play(FadeIn(b), run_time=0.5)
            self.wait(0.8)
            self.play(FadeOut(b), run_time=0.3)

        with self.narrate("And Ava asks the questions you would ask. She never lets "
                          "Marshall get away with anything."):
            self.play(FadeIn(a), FadeIn(la), run_time=0.8)
            q = a.say("Hang on. Why?", direction=UP, width=2.8)
            self.play(FadeIn(q), a.mood("thinking"), run_time=0.5)
            self.wait(0.8)
            self.play(FadeOut(q), run_time=0.3)

        with self.narrate("We start from nothing at all. No economics is assumed. "
                          "Not one word of it."):
            self.play(*[f.nod() for f in (n, m, a)], run_time=0.9)

        self.close_chapter([
            "A farmer absorbs losses, and will not shut.",
            "An owner refuses a project the sums approve.",
            "Both are correct. That is the film.",
        ])
