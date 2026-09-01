import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter22(Chapter):
    CH = 22
    TITLE = "Money, and who is in charge of it"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["bank", "money", "lever", "clock"]

    def body(self):
        self.heading("Part Two starts from nothing again")
        kit = stick.kit(scale=1.0)
        St.place(kit, St.STAGE, ax=-0.6, ay=-0.2)
        with self.narrate("Nothing here assumes you know what a central bank is, or an "
                          "interest rate, or a bond. We build all of them from scratch, "
                          "exactly as we built cost and revenue."):
            self.play(FadeIn(kit), FadeIn(kit.label()), run_time=0.9)
        with self.narrate("And there is one new person. This is Kit. He is a student, "
                          "and the argument in Part Three is his. He notices things, "
                          "gets excited, and then talks himself down when the evidence "
                          "will not carry him. That last part is the whole point."):
            self.play(kit.mood("thinking"), run_time=0.4)
            self.play(kit.nod(), run_time=0.9)
        self.clear_stage()

        self.define("central bank", "The public body that looks after a country's "
                    "money.", "bank", SRC_BR, hold=4.0)
        self.define("interest", "The extra a borrower pays for the use of money.",
                    "money", MONEY, hold=3.6)

        # ------------------------------------------------ a worked rate
        self.heading("An interest rate, with numbers")
        lender = stick.StickFigure("a lender", CHALK, scale=0.8)
        St.place(lender, St.STAGE, ax=-0.7, ay=0.1)
        borrower = stick.StickFigure("a borrower", CHALK, scale=0.8)
        St.place(borrower, St.STAGE, ax=0.7, ay=0.1)
        self.play(FadeIn(lender), FadeIn(borrower), run_time=0.8)
        a1 = W.flow_arrow(lender.get_right() + RIGHT * 0.3,
                          borrower.get_left() + LEFT * 0.3, MONEY)
        t1 = Text("£100 now", font=FONT, font_size=T_BODY, color=MONEY)
        t1.next_to(a1, UP, buff=0.18)
        a2 = W.flow_arrow(borrower.get_left() + LEFT * 0.3 + DOWN * 1.5,
                          lender.get_right() + RIGHT * 0.3 + DOWN * 1.5, MONEY)
        t2 = Text("£105 in a year", font=FONT, font_size=T_BODY, color=MONEY)
        t2.next_to(a2, DOWN, buff=0.18)
        with self.narrate("Borrow a hundred pounds at five per cent, and you pay back a "
                          "hundred and five after a year."):
            self.play(Create(a1), FadeIn(t1), run_time=0.9)
            self.play(S.flow_along(a1, MONEY))
            self.play(Create(a2), FadeIn(t2), run_time=0.9)
        self.beat()
        self.define("interest rate", "How much extra, as a percentage per year.",
                    "money", MONEY, at=UP * 1.9, hold=3.4)
        self.clear_stage()
        self.define("monetary policy", "What a central bank does to make borrowing "
                    "easier or harder.", "lever", SRC_BR, hold=4.2)

        # ------------------------------------------------ 2008
        self.heading("2008, in ninety seconds")
        gov = stick.governor(scale=1.05)
        St.place(gov, St.STAGE, ax=-0.65, ay=-0.15)
        with self.narrate("Meet the Governor. He runs the central bank. He is "
                          "well-meaning, he holds the levers, and he is genuinely "
                          "trying to help. He is not the villain of this film. There "
                          "isn't one."):
            self.play(FadeIn(gov), FadeIn(gov.label()), run_time=1.0)

        track = Line(UP * 2.0, DOWN * 2.0, color=MUTED, stroke_width=4)
        St.place(track, St.STAGE, ax=0.45)
        floor = Line(LEFT * 0.7, RIGHT * 0.7, color=COST, stroke_width=6)
        floor.move_to(track.get_bottom())
        fl = Text("zero", font=FONT, font_size=T_SMALL, color=COST)
        fl.next_to(floor, RIGHT, buff=0.25)
        handle = ValueTracker(1.7)
        knob = always_redraw(lambda: Line(
            track.get_center() + LEFT * 0.5 + UP * handle.get_value(),
            track.get_center() + RIGHT * 0.5 + UP * handle.get_value(),
            color=SRC_BR, stroke_width=8))
        rate = St.caption("the interest rate", SRC_BR, T_BODY, width=16)
        St.place(rate, St.SIDE, ay=0.55)
        self.play(Create(track), Create(floor), FadeIn(fl), FadeIn(knob),
                  FadeIn(rate), run_time=1.1)

        with self.narrate("After the crash of two thousand and eight, the Bank wanted "
                          "people and businesses to spend and build. So it did the "
                          "usual thing. It cut the rate."):
            self.play(handle.animate.set_value(0.6), run_time=1.6)
            self.play(gov.point_at(track), run_time=0.6)
        with self.narrate("And it cut it again. And again."):
            self.play(handle.animate.set_value(-1.1), run_time=1.3)
            self.play(handle.animate.set_value(-1.85), run_time=1.1)
        with self.narrate("And by two thousand and nine the rate was almost at zero. "
                          "The lever had hit the floor. You cannot cut much below "
                          "nothing."):
            self.play(handle.animate.set_value(-1.97), run_time=1.0)
            self.play(gov.mood("worried"), run_time=0.5)
        self.beat()
        with self.narrate("So they needed something else. That something else is the "
                          "subject of the next two chapters."):
            self.foot("so they needed something else", CHALK)
        self.beat()

        self.close_chapter([
            "central bank: looks after the money",
            "interest, and the rate, per year",
            "monetary policy: the lever",
            "by 2009 the lever hit the floor",
        ])
