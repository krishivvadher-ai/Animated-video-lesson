import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.scale import MasterScale
from lib.theme import *


class Chapter46(Chapter):
    CH = 46
    TITLE = "And the ones that did not come back"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["scale", "door", "clock", "people"]

    def body(self):
        self.heading("The same picture, downwards")
        sc = MasterScale(x=-4.6, y=-0.45, height=4.3)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), FadeIn(sc.title),
                  run_time=1.0)
        hline = sc.add_level("H", 1.62, "the build-line", TRIGGER, width=2.8, sw=5)
        mline = sc.add_level("M", 1.10, "Marshall's line", MUTED, width=2.8,
                             dashed=True, sw=2)
        cline = sc.add_level("C", 1.00, "Marshall's quit-line", SUNK, width=2.8,
                             dashed=True, sw=2)
        lline = sc.add_level("L", 0.72, "the real quit-line", COST, width=2.8, sw=5)
        with self.narrate("You will recognise this picture instantly, because it is the "
                          "hysteresis one. Same scale, same lines. Only the direction "
                          "is different."):
            for lv in (hline, mline, cline, lline):
                self.play(Create(lv[0]), FadeIn(lv[1]), run_time=0.5)

        tracker = ValueTracker(1.30)
        dot = always_redraw(lambda: Dot(sc.pos(tracker.get_value()), radius=0.13,
                                        color=MONEY))
        self.add(dot)
        firm = W.building(CHALK, size=0.42, kind="office")
        St.place(firm, St.SIDE, ay=0.5)
        with self.narrate("A firm that is already running."):
            self.play(Create(firm), run_time=0.8)

        with self.narrate("The crisis arrives, and its takings fall."):
            self.play(tracker.animate.set_value(1.02), run_time=1.6)

        holds = St.caption("still open — holding on keeps\nthe chance alive", WAIT,
                           T_BODY, width=22)
        St.place(holds, St.SIDE, ay=-0.25)
        with self.narrate("Down past the level where the textbook would have closed it. "
                          "And still it holds on, because holding on keeps the chance "
                          "of recovery alive."):
            self.play(tracker.animate.set_value(0.86), run_time=1.6)
            self.play(FadeIn(holds), run_time=0.7)

        with self.narrate("And then through the quit line. It closes."):
            self.play(tracker.animate.set_value(0.66), run_time=1.6)
            x = Cross(firm, stroke_color=COST, stroke_width=6).scale(0.8)
            self.play(Create(x), FadeOut(holds), run_time=0.9)
        self.beat()

        with self.narrate("Now the policy works. Conditions come back up to normal. All "
                          "the way back to where they started."):
            self.play(tracker.animate.set_value(1.30), run_time=2.6)
        self.beat()

        gone = St.caption("the firm does not come back", COST, T_SUB, width=26)
        St.place(gone, St.SIDE, ay=-0.25)
        with self.narrate("The firm does not come back. Because coming back means "
                          "paying the whole set-up cost over again."):
            self.play(FadeIn(gone), run_time=0.9)
            self.play(S.flash_around(gone, COST))
        self.beat()
        self.remove(dot)
        self.clear_stage()

        # ------------------------------------------------ the point
        self.drop_heading()
        a = St.caption("what the policy stopped\nneeds no explaining", MUTED,
                       T_SUB, width=30)
        St.place(a, St.WIDE, ay=0.75)
        b = St.caption("why nothing came back\nfor the rest — does", SRC_KIT,
                       T_HEAD, width=30)
        St.place(b, St.WIDE, ay=-0.15)
        with self.narrate("State it plainly. What the policy stops from happening does "
                          "not need explaining."):
            self.play(FadeIn(a), run_time=0.9)
        with self.narrate("What needs explaining is why, for the firms it did not reach "
                          "in time, nothing came back."):
            self.play(Write(b), run_time=2.4)
        self.wait(1.6)
        self.beat()

        self.close_chapter([
            "a firm absorbs losses, then closes",
            "conditions recover all the way",
            "and the firm does not come back",
            "because coming back costs the set-up again",
        ])
