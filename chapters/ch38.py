import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter38(Chapter):
    CH = 38
    TITLE = "The concession that hurts most"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["shield", "risk", "people", "scale"]

    def body(self):
        kit = stick.kit(scale=0.85)
        St.place(kit, St.STAGE, ax=-0.7, ay=-0.4)
        with self.narrate("This chapter exists because Kit's own source damages him, "
                          "and that is what intellectual honesty looks like.", v="c"):
            self.heading("A concession that costs him")
            self.play(FadeIn(kit), run_time=0.7)
            self.play(kit.mood("worried"), run_time=0.4)
        self.play(FadeOut(kit), run_time=0.4)

        # ------------------------------------------------ the Japan replay
        self.heading("The cushioned downside, again")
        kenji = stick.kenji(scale=0.85)
        St.place(kenji, St.STAGE, ax=-0.75, ay=-0.35)
        cush = W.shield(SUNK, "the downside cushioned", scale=1.0)
        St.place(cush, St.STAGE, ax=0.5, ay=0.1)
        with self.narrate("Replay the two countries. Japanese firms invested boldly and "
                          "hung on through losses, because their downside was "
                          "cushioned."):
            self.play(FadeIn(kenji), FadeIn(kenji.label()), run_time=0.8)
            self.play(FadeIn(cush), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ which half?
        self.heading("So which half does the policy work on?")
        curve = VMobject(color=WAIT, stroke_width=4)
        pts = [np.array([x, 1.7 * np.exp(-x * x / 1.8) - 1.4, 0])
               for x in np.linspace(-3.2, 3.2, 44)]
        curve.set_points_smoothly(pts)
        St.place(curve, St.FULL, ay=0.35)
        floor = Line(curve.get_left(), curve.get_right(), color=MUTED, stroke_width=2)
        floor.move_to(curve.get_bottom())
        mid = DashedLine(curve.get_top() + UP * 0.15, floor.get_center(),
                         color=MUTED, stroke_width=2)
        mid.move_to([curve.get_center()[0], mid.get_center()[1], 0])
        self.play(Create(curve), Create(floor), run_time=1.4)
        self.play(Create(mid), run_time=0.6)
        lo = Text("bad half", font=FONT, font_size=T_SMALL, color=COST)
        lo.next_to(floor.get_left(), UP, buff=0.25).shift(RIGHT * 1.1)
        hi = Text("good half", font=FONT, font_size=T_SMALL, color=MONEY)
        hi.next_to(floor.get_right(), UP, buff=0.25).shift(LEFT * 1.1)
        self.play(FadeIn(lo), FadeIn(hi), run_time=0.7)

        with self.narrate("Which half of that spread does a policy that props up prices "
                          "and signals that the authorities will act actually work on?"):
            self.play(S.pulse(curve, TRIGGER))

        good = Rectangle(width=curve.width / 2, height=curve.height + 0.2,
                         color=MONEY, stroke_width=4, fill_color=MONEY,
                         fill_opacity=0.16)
        good.align_to(mid, LEFT).align_to(floor, DOWN)
        with self.narrate("This half. Which is exactly the right half for keeping a "
                          "struggling firm from closing."):
            self.play(FadeIn(good), run_time=1.0)
            self.play(S.flash_around(good, MONEY, run_time=2.0))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the cost to him
        self.heading("And that hands the policy a mechanism")
        cost = St.caption("a mechanism for the thing he meant\nto explain another way",
                          COST, T_SUB, width=36)
        St.place(cost, St.FULL, ay=0.4)
        with self.narrate("A policy that props up the upside is aimed at exactly the "
                          "right half of the distribution for keeping firms alive. "
                          "Which hands the policy a mechanism for the very thing he was "
                          "going to explain another way."):
            self.play(FadeIn(cost), run_time=1.2)
            self.play(S.flash_around(cost, COST, run_time=2.0))
        self.beat()

        why = St.caption("because it is what his own source says", SRC_KIT,
                         T_SUB, width=40)
        St.place(why, St.FULL, ay=-0.5)
        with self.narrate("Why include something that damages you? Because it is what "
                          "his own source says. The discomfort is the point.", v="c"):
            self.play(FadeIn(why), run_time=1.0)
        self.beat()

        self.close_chapter([
            "a cushioned downside keeps firms invested",
            "the policy props up the good half",
            "which is the right half for keeping firms alive",
            "so his own source hands the policy a mechanism",
        ])
