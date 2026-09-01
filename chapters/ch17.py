import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.theme import *

class Chapter17(Chapter):
    CH = 17
    TITLE = "Money, and who is in charge of it"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ['bank', 'money', 'lever', 'clock']

    def body(self):
        kit = stick.kit(scale=1.0).shift(LEFT * 4.8 + DOWN * 0.7)
        kl = kit.label()
        with self.narrate("Part Two starts from nothing again. Nothing here assumes you "
                          "know what a central bank is, or an interest rate, or a bond. "
                          "We build all of them from scratch, exactly as we built cost "
                          "and revenue."):
            self.play(FadeIn(kit), FadeIn(kl), run_time=0.8)

        with self.narrate("And there is one new person. This is Kit. He is a student, "
                          "and the argument in this half of the film is his. He notices "
                          "things, gets excited about them, and then talks himself down "
                          "when the evidence will not carry him. That last part is the "
                          "whole point of Part Two."):
            self.play(kit.mood("thinking"), run_time=0.5)
            self.play(kit.nod(), run_time=0.8)

        self.define("central bank", "The public body that looks after a country's "
                    "money. The Bank of England is ours.", "bank", SRC_BR,
                    at=RIGHT * 1.6, hold=4.4)
        self.define("interest", "The extra a borrower pays a lender for the use of the "
                    "money.", "money", MONEY, at=RIGHT * 1.6, hold=4.0)

        # ------------------------------------------------- interest rate, worked
        lender = stick.StickFigure("a lender", CHALK, scale=0.8).shift(RIGHT * 0.6 + UP * 0.9)
        borrower = stick.StickFigure("a borrower", CHALK, scale=0.8).shift(RIGHT * 5.2 + UP * 0.9)
        a1 = W.flow_arrow(lender.get_right() + RIGHT * 0.3, borrower.get_left() + LEFT * 0.3, MONEY)
        t1 = Text("£100 now", font=FONT, font_size=T_SMALL, color=MONEY).next_to(a1, UP, buff=0.14)
        a2 = W.flow_arrow(borrower.get_left() + LEFT * 0.3 + DOWN * 1.2,
                          lender.get_right() + RIGHT * 0.3 + DOWN * 1.2, MONEY)
        t2 = Text("£105 in a year", font=FONT, font_size=T_SMALL, color=MONEY).next_to(a2, DOWN, buff=0.14)
        with self.narrate("Here is what an interest rate means, with numbers. Borrow a "
                          "hundred pounds at five per cent, and you pay back a hundred "
                          "and five after a year."):
            self.play(FadeIn(lender), FadeIn(borrower), run_time=0.7)
            self.play(Create(a1), FadeIn(t1), run_time=0.9)
            self.play(Create(a2), FadeIn(t2), run_time=0.9)
        self.beat()
        self.define("interest rate", "How much extra, as a percentage per year.",
                    "money", MONEY, at=DOWN * 2.0, hold=3.6)
        self.play(FadeOut(VGroup(lender, borrower, a1, a2, t1, t2)), run_time=0.5)

        self.define("monetary policy", "The things a central bank does to make "
                    "borrowing easier or harder across the whole country.",
                    "lever", SRC_BR, at=RIGHT * 1.6, hold=4.6)

        # ------------------------------------------------- 2008
        self.clear_stage()
        head = Text("2008, in ninety seconds", font=FONT, font_size=T_SUB,
                    color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)

        gov = stick.governor(scale=1.1).shift(LEFT * 4.0 + DOWN * 0.3)
        gl = gov.label()
        with self.narrate("Meet the Governor. He runs the central bank. He is "
                          "well-meaning, he holds the levers, and he is genuinely "
                          "trying to help. He is not the villain of this film. There "
                          "isn't one."):
            self.play(FadeIn(gov), FadeIn(gl), run_time=0.9)

        track = Line(RIGHT * 1.4 + UP * 2.0, RIGHT * 1.4 + DOWN * 2.0,
                     color=MUTED, stroke_width=4)
        floor = Line(RIGHT * 0.7 + DOWN * 2.0, RIGHT * 2.1 + DOWN * 2.0,
                     color=COST, stroke_width=6)
        fl = Text("zero", font=FONT, font_size=T_SMALL, color=COST).next_to(floor, RIGHT, buff=0.25)
        handle = ValueTracker(1.7)
        knob = always_redraw(lambda: VGroup(
            Line(RIGHT * 0.9 + UP * handle.get_value(), RIGHT * 1.9 + UP * handle.get_value(),
                 color=SRC_BR, stroke_width=8),
            Text("the interest rate", font=FONT, font_size=T_SMALL, color=SRC_BR)
            .move_to(RIGHT * 3.6 + UP * handle.get_value())))
        self.play(Create(track), Create(floor), FadeIn(fl), FadeIn(knob), run_time=1.0)

        with self.narrate("After the crash of two thousand and eight, the Bank wanted "
                          "people and businesses to spend and build. So it did the "
                          "usual thing. It cut the rate."):
            self.play(handle.animate.set_value(0.6), run_time=1.6)
            self.play(gov.point_at(track), run_time=0.6)
        with self.narrate("And it cut it again. And again."):
            self.play(handle.animate.set_value(-1.1), run_time=1.4)
            self.play(handle.animate.set_value(-1.85), run_time=1.2)
        with self.narrate("And by two thousand and nine the rate was almost at zero. "
                          "The lever had hit the floor. You cannot cut much below "
                          "nothing."):
            self.play(handle.animate.set_value(-1.96), run_time=1.0)
            self.play(gov.mood("worried"), run_time=0.5)
        self.beat()
        need = cards.body("So they needed something else.", size=T_SUB, color=CHALK,
                          width=22)
        need.move_to(RIGHT * 4.6 + UP * 1.4)
        with self.narrate("So they needed something else. That something else is the "
                          "subject of the next chapter."):
            self.play(FadeIn(need), run_time=0.8)
        self.beat()

        self.close_chapter([
            "central bank: looks after the money",
            "interest · and the rate, per year",
            "monetary policy: the lever",
            "by 2009: the lever hit the floor",
        ])
