import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *

RHO, K = 0.05, 2.0
BETA = 2.158
H = BETA / (BETA - 1) * RHO * K
B = (1 / RHO) / (BETA * H ** (BETA - 1))


class Chapter12(Chapter):
    CH = 12
    TITLE = "The picture the paper draws"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["scale", "voucher", "clock", "fog"]

    def body(self):
        self.heading("Two lines, and where they touch")
        ax = Axes(x_range=[0, 0.33, 0.05], y_range=[-2.6, 3.2, 1],
                  x_length=7.6, y_length=4.6, axis_config=AXIS)
        St.place(ax, St.STAGE, ay=-0.05)
        xl = Text("revenue a year →", font=FONT, font_size=T_SMALL, color=MUTED)
        xl.next_to(ax, DOWN, buff=0.2).align_to(ax, RIGHT)
        yl = Text("value →", font=FONT, font_size=T_SMALL, color=MUTED).rotate(PI / 2)
        yl.next_to(ax.y_axis, LEFT, buff=0.15).align_to(ax.y_axis, UP)
        with self.narrate("The paper has two diagrams, and they are the heart of it. "
                          "Across the bottom, the revenue coming in each year. Up the "
                          "side, what the whole opportunity is worth to Nell."):
            self.play(Create(ax), FadeIn(xl), FadeIn(yl), run_time=1.6)

        line = ax.plot(lambda r: r / RHO - K, x_range=[0, 0.32], color=MONEY,
                       stroke_width=5)
        ll = Text("build now", font=FONT, font_size=T_BODY, color=MONEY)
        ll.next_to(line.get_end(), RIGHT, buff=0.25)
        with self.narrate("First, the straight line. If she builds today she gets the "
                          "revenue for ever, divided by the rate, minus the sunk cost. "
                          "That is the sum from two chapters ago, and drawn against "
                          "revenue it is a straight line."):
            self.play(Create(line), FadeIn(ll), run_time=2.2)
        self.beat()

        m_dot = Dot(ax.c2p(RHO * K, 0), radius=0.11, color=COST)
        m_lab = Text("M", font=FONT, font_size=T_BODY, color=COST)
        m_lab.next_to(m_dot, DOWN, buff=0.22)
        with self.narrate("It starts below the axis, because at zero revenue she would "
                          "simply lose the sunk cost. And it crosses zero exactly at "
                          "Marshall's line."):
            self.play(FadeIn(m_dot), FadeIn(m_lab), run_time=0.8)
            self.play(S.spark(m_dot, COST))
        self.beat()

        curve = ax.plot(lambda r: B * r ** BETA, x_range=[0, H], color=WAIT,
                        stroke_width=5)
        cl = Text("wait", font=FONT, font_size=T_BODY, color=WAIT)
        cl.next_to(curve.point_from_proportion(0.72), UL, buff=0.12)
        with self.narrate("Now the second line, and this one is a curve. It is what the "
                          "chance to build is worth if she does not use it yet."):
            self.play(Create(curve), FadeIn(cl), run_time=2.4)
        self.beat()

        shape = St.points(["very low → worthless",
                           "rising → worth more, faster",
                           "near the trigger → worth building"],
                          colour=WAIT, dot_colour=WAIT, size=T_BODY, width=20)
        St.place(shape, St.SIDE, ay=0.35)
        says = ["When revenue is very low the chance is nearly worthless — things would "
                "have to improve enormously, and that is a long way off.",
                "As revenue rises the chance is worth more, and worth more faster. That "
                "is why it bends upwards.",
                "And close to the point where she would build, it is worth just about "
                "what building is worth. The two have to meet."]
        for i, row in enumerate(shape):
            with self.narrate(says[i]):
                self.play(FadeIn(row), run_time=0.8)
        self.beat()
        self.play(FadeOut(shape), run_time=0.5)

        h_dot = Dot(ax.c2p(H, B * H ** BETA), radius=0.12, color=TRIGGER)
        h_lab = Text("H", font=FONT, font_size=T_BODY, color=TRIGGER)
        h_lab.next_to(h_dot, UP, buff=0.22)
        with self.narrate("They meet here. And they do not cross — they touch, and run "
                          "off in the same direction."):
            self.play(FadeIn(h_dot), FadeIn(h_lab), run_time=0.8)
            self.play(S.flash_around(h_dot, TRIGGER, buff=0.22))
        self.beat()

        why = St.points(["crossing → she would not build there",
                         "curve below → she would build sooner",
                         "touching → exactly right"],
                        colour=CHALK, dot_colour=TRIGGER, size=T_BODY, width=20)
        St.place(why, St.SIDE, ay=0.35)
        says2 = ["If the two lines crossed, waiting would still be worth more just past "
                 "the meeting point — so she would not build there after all.",
                 "And if the curve stayed below the line, she would have been better "
                 "off building sooner.",
                 "Touching, and only touching, is the right place. That single "
                 "condition is what picks out the trigger."]
        for i, row in enumerate(why):
            with self.narrate(says2[i]):
                self.play(FadeIn(row), run_time=0.8)
        self.beat()
        self.play(FadeOut(why), run_time=0.5)

        gap = DoubleArrow(ax.c2p(RHO * K, -0.9), ax.c2p(H, -0.9), color=TRIGGER,
                          buff=0, stroke_width=5)
        gl = Text("the gap", font=FONT, font_size=T_SMALL, color=TRIGGER)
        gl.next_to(gap, DOWN, buff=0.18)
        with self.narrate("And there, between where the textbook says build and where "
                          "she actually should, is the gap this whole film is about. "
                          "You have now seen exactly where it comes from."):
            self.play(GrowFromCenter(gap), FadeIn(gl), run_time=1.4)
        self.beat()
        with self.narrate("The paper finds that touching point with calculus. We are "
                          "about to get exactly the same answer with a square root."):
            self.foot("next: the same answer, with a square root", MUTED)
        self.beat()

        self.close_chapter([
            "the straight line: building now",
            "the curve: what waiting is worth",
            "they touch — they do not cross",
            "and where they touch is the trigger",
        ])
