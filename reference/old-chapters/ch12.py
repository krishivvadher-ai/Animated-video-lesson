import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.theme import *

RHO, K = 0.05, 2.0
BETA = 2.158
B = (1 / RHO) / (BETA * (BETA / (BETA - 1) * RHO * K) ** (BETA - 1))
H = BETA / (BETA - 1) * RHO * K          # 0.1863…  (per unit time)


class Chapter12(Chapter):
    CH = 12
    TITLE = "The picture the paper draws"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["scale", "voucher", "clock", "fog"]

    def body(self):
        with self.narrate("The paper has two diagrams, and they are the heart of it. We "
                          "are going to draw both, one line at a time."):
            pass

        ax = Axes(x_range=[0, 0.34, 0.05], y_range=[-2.6, 3.2, 1],
                  x_length=9.2, y_length=5.0,
                  axis_config=AXIS)
        ax.shift(RIGHT * 1.6 + DOWN * 0.3).scale(0.86)
        xl = Text("revenue a year →", font=FONT, font_size=T_SMALL, color=MUTED)
        xl.next_to(ax.x_axis, DOWN, buff=0.18).align_to(ax.x_axis, RIGHT)
        yl = Text("value →", font=FONT, font_size=T_SMALL, color=MUTED).rotate(PI / 2)
        yl.next_to(ax.y_axis, LEFT, buff=0.18).shift(UP * 1.2)
        with self.narrate("Across the bottom, the revenue coming in each year. Up the "
                          "side, what the whole opportunity is worth to Nell."):
            self.play(Create(ax), FadeIn(xl), FadeIn(yl), run_time=1.6)

        # ---- the straight line: build now
        line = ax.plot(lambda r: r / RHO - K, x_range=[0, 0.33], color=MONEY,
                       stroke_width=5)
        ll = Text("build now", font=FONT, font_size=T_BODY, color=MONEY)
        ll.next_to(line.get_end(), UP, buff=0.2).shift(LEFT * 0.6)
        with self.narrate("First, the straight line. If she builds today, she gets the "
                          "revenue for ever, divided by the rate, minus the sunk cost. "
                          "That is the sum from two chapters ago, and drawn against "
                          "revenue it is a straight line."):
            self.play(Create(line), FadeIn(ll), run_time=2.2)
        self.beat()

        below = Text("below zero — she would lose money", font=FONT, font_size=T_SMALL,
                     color=COST)
        below.move_to(LEFT * 4.6 + DOWN * 2.4)
        with self.narrate("Notice where it starts. At zero revenue she would simply "
                          "lose the sunk cost, so the line begins below the axis."):
            self.play(FadeIn(below), run_time=0.9)
        m_dot = Dot(ax.c2p(RHO * K, 0), radius=0.10, color=COST)
        m_lab = Text("M — the textbook line", font=FONT, font_size=T_SMALL, color=COST)
        m_lab.next_to(m_dot, DOWN, buff=0.25).shift(RIGHT * 0.2)
        with self.narrate("And it crosses zero exactly at Marshall's line. Everything "
                          "to the right of that point looks, to the textbook, like a "
                          "project worth doing."):
            self.play(FadeIn(m_dot), FadeIn(m_lab), run_time=1.0)
            self.play(Flash(m_dot, color=COST, line_length=0.25), run_time=0.8)
        self.beat()
        self.play(FadeOut(below), run_time=0.4)

        # ---- the curve: the value of waiting
        curve = ax.plot(lambda r: B * r ** BETA, x_range=[0, H], color=WAIT,
                        stroke_width=5)
        cl = Text("wait", font=FONT, font_size=T_BODY, color=WAIT)
        cl.next_to(curve.point_from_proportion(0.75), UP + LEFT, buff=0.18)
        with self.narrate("Now the second line, and this one is a curve. It is what the "
                          "chance to build is worth if she does not use it yet."):
            self.play(Create(curve), FadeIn(cl), run_time=2.4)
        self.beat()

        shape = cards.bullet_list([
            "very low → worthless",
            "rising → worth more, faster",
            "near the trigger → worth building",
        ], color=WAIT, width=20, dotc=WAIT, size=T_SMALL)
        cards.fit(shape, 5.0, 3.2)
        shape.move_to(LEFT * 4.4 + DOWN * 1.7)
        says = ["When revenue is very low, the chance is nearly worthless — things would "
                "have to improve enormously, and that is a long way off.",
                "As revenue rises the chance is worth more, and worth more faster. That "
                "is why it bends upwards.",
                "And close to the point where she would build, it is worth just about "
                "what building is worth. The two have to meet."]
        for i in range(3):
            with self.narrate(says[i]):
                self.play(FadeIn(shape[i], shift=RIGHT * 0.2), run_time=0.7)
        self.beat()
        self.play(FadeOut(shape), run_time=0.5)

        # ---- tangency
        h_dot = Dot(ax.c2p(H, B * H ** BETA), radius=0.11, color=TRIGGER)
        h_lab = Text("H — where she actually builds", font=FONT, font_size=T_SMALL,
                     color=TRIGGER)
        h_lab.next_to(h_dot, UP, buff=0.25).shift(LEFT * 0.4)
        with self.narrate("They meet here. And they do not cross — they touch, and run "
                          "off in the same direction."):
            self.play(FadeIn(h_dot), FadeIn(h_lab), run_time=1.0)
            self.play(S.flash_around(h_dot, color=TRIGGER, buff=0.12, stroke_width=4),
                      run_time=1.4)
        self.beat()

        why = cards.bullet_list([
            "crossing → she would not build there",
            "curve below → she would build sooner",
            "touching → exactly right",
        ], color=CHALK, width=20, dotc=TRIGGER, size=T_SMALL)
        cards.fit(why, 5.0, 3.2)
        why.move_to(LEFT * 4.4 + DOWN * 1.7)
        says2 = ["And that touching is doing real work. If the two lines crossed, "
                 "waiting would still be worth more just past the meeting point — so "
                 "she would not build there after all.",
                 "And if the curve stayed below the line, she would have been better "
                 "off building sooner.",
                 "Touching, and only touching, is the right place. That single "
                 "condition is what picks out the trigger."]
        for i in range(3):
            with self.narrate(says2[i]):
                self.play(FadeIn(why[i], shift=RIGHT * 0.2), run_time=0.7)
        self.beat()

        # ---- the gap
        self.play(FadeOut(why), run_time=0.4)
        gap = DoubleArrow(ax.c2p(RHO * K, -0.55), ax.c2p(H, -0.55), color=TRIGGER,
                          buff=0, stroke_width=5)
        gl = Text("the gap the whole film is about", font=FONT, font_size=T_SMALL,
                  color=TRIGGER)
        gl.next_to(gap, DOWN, buff=0.2)
        with self.narrate("And there, between where the textbook says build and where "
                          "she actually should, is the gap this whole film is about. "
                          "You have now seen exactly where it comes from."):
            self.play(Create(gap), FadeIn(gl), run_time=1.4)
        self.beat()

        note = cards.note("The paper works the touching point out with calculus. We are "
                          "about to get the same answer with a square root.", width=60)
        note.to_edge(DOWN, buff=0.62)
        with self.narrate("The paper finds that touching point with calculus. We are "
                          "about to get exactly the same answer with a square root."):
            self.play(FadeIn(note), run_time=1.0)
        self.beat()

        self.close_chapter([
            "the straight line: what building now is worth",
            "the curve: what the chance is worth if she waits",
            "they touch — they do not cross",
            "and where they touch is the trigger, H",
        ])
