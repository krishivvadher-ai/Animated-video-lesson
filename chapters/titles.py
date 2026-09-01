import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.theme import *


class _Card(Chapter):
    HEAD = ""
    SUB = ""
    NOTE = ""

    def construct(self):
        head = Text(self.HEAD, font=FONT, font_size=T_HEAD + 10, color=CHALK)
        rule = Line(LEFT * 3.0, RIGHT * 3.0, color=MUTED, stroke_width=2)
        sub = cards.body(self.SUB, size=T_SUB, color=MUTED, width=44)
        g = VGroup(head, rule, sub).arrange(DOWN, buff=0.5)
        if self.NOTE:
            n = cards.note(self.NOTE, width=60)
            n.next_to(g, DOWN, buff=0.8)
            g.add(n)
        g.move_to(ORIGIN)
        self.play(Write(head), run_time=1.6)
        self.play(Create(rule), run_time=0.7)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=1.0)
        if self.NOTE:
            self.play(FadeIn(g[-1]), run_time=0.8)
        self.wait(2.4)
        self.play(FadeOut(g), run_time=1.0)


class TitleFilm(_Card):
    HEAD = "Investment, Hysteresis\nand Quantitative Easing"
    SUB = "a film in three parts"
    NOTE = "Dixit (1992) · Bowdler & Radia (2012) · Martin & Milas (2012)"


class TitleOne(_Card):
    HEAD = "PART ONE"
    SUB = "The Paper"
    NOTE = "Avinash Dixit, ‘Investment and Hysteresis’,\nJournal of Economic Perspectives 6(1), 1992"


class TitleTwo(_Card):
    HEAD = "PART TWO"
    SUB = "The Policy"
    NOTE = "Christopher Bowdler and Amar Radia,\n‘Unconventional monetary policy: the assessment’,\nOxford Review of Economic Policy 28(4), 2012"


class TitleThree(_Card):
    HEAD = "PART THREE"
    SUB = "The Argument"
    NOTE = "with Christopher Martin and Costas Milas,\n‘Quantitative easing: a sceptical survey’,\nOxford Review of Economic Policy 28(4), 2012"


class Interval(_Card):
    HEAD = "Interval"
    SUB = "take a break — the next part starts from nothing again"
    NOTE = ""


class EndCard(Chapter):
    def construct(self):
        cast = VGroup(stick.nell(scale=0.55), stick.marshall(scale=0.55),
                      stick.ava(scale=0.55), stick.kenji(scale=0.55),
                      stick.kit(scale=0.55), stick.governor(scale=0.55))
        cast.arrange(RIGHT, buff=0.9).shift(UP * 0.6)
        names = Text("Nell · Marshall · Ava · Kenji · Kit · the Governor",
                     font=FONT, font_size=T_SMALL, color=MUTED)
        names.next_to(cast, DOWN, buff=0.5)
        end = Text("End", font=FONT, font_size=T_HEAD, color=CHALK)
        end.next_to(names, DOWN, buff=0.9)
        made = cards.note("Animated with Manim. Narration and score generated for this "
                          "film. Every claim is sourced in docs/content-ledger.md.",
                          width=66)
        made.next_to(end, DOWN, buff=0.7)
        self.play(LaggedStart(*[FadeIn(f) for f in cast], lag_ratio=0.18), run_time=2.0)
        self.play(FadeIn(names), run_time=0.8)
        self.play(Write(end), run_time=1.2)
        self.play(FadeIn(made), run_time=0.9)
        self.wait(2.6)
        self.play(FadeOut(VGroup(cast, names, end, made)), run_time=1.2)
