import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.scale import MasterScale
from lib.theme import *


class Chapter40(Chapter):
    CH = 40
    TITLE = "And the ones that did not come back"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["magnet", "door", "slab", "fog"]

    def body(self):
        with self.narrate("You will recognise this picture instantly, because it is "
                          "the one from chapter twelve. Same scale, same lines. Only "
                          "the direction is different."):
            pass

        sc = MasterScale(x=-5.6, y=-0.3, height=4.8)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), FadeIn(sc.title), run_time=0.8)
        for k, v, t, c, sw in [("L", 0.72, "0.72", TRIGGER, 5),
                               ("M", 1.10, "1.10", COST, 3),
                               ("H", 1.62, "1.62", TRIGGER, 5)]:
            g = sc.add_level(k, v, t, c, width=11.0, sw=sw)
            g[1].next_to(g[0], LEFT, buff=0.18)
            self.play(Create(g[0]), FadeIn(g[1]), run_time=0.4)

        t = ValueTracker(1.05)
        xt = ValueTracker(0.0)
        dot = always_redraw(lambda: Dot(sc.pos(t.get_value()) + RIGHT * xt.get_value(),
                                        radius=0.14, color=MONEY))
        trail = TracedPath(dot.get_center, stroke_color=MONEY, stroke_width=4)
        self.add(trail, dot)
        fac = W.factory(MONEY, 0.42).move_to(sc.pos(1.05) + UP * 0.9)
        self.play(FadeIn(fac), run_time=0.5)

        with self.narrate("A firm that is already running. The crisis arrives, and its "
                          "takings fall."):
            self.play(t.animate.set_value(0.92), xt.animate.set_value(2.4),
                      run_time=2.0, rate_func=linear)
        with self.narrate("Down past the level where the textbook would have closed it. "
                          "And still it holds on, because holding on keeps the chance "
                          "of recovery alive."):
            self.play(t.animate.set_value(0.80), xt.animate.set_value(4.4),
                      run_time=2.0, rate_func=linear)
        with self.narrate("And then through the quit line. It closes."):
            self.play(t.animate.set_value(0.66), xt.animate.set_value(6.2),
                      run_time=2.0, rate_func=linear)
            cross = VGroup(
                Line(LEFT * 0.34 + UP * 0.34, RIGHT * 0.34 + DOWN * 0.34, color=COST,
                     stroke_width=6),
                Line(LEFT * 0.34 + DOWN * 0.34, RIGHT * 0.34 + UP * 0.34, color=COST,
                     stroke_width=6)).move_to(fac)
            self.play(FadeIn(cross), fac.animate.set_color(MUTED), run_time=0.8)
        self.beat()

        gov = stick.governor(scale=0.7).move_to(RIGHT * 5.2 + DOWN * 2.2)
        self.play(FadeIn(gov), run_time=0.5)
        with self.narrate("Now the policy works. Conditions come back up to normal. All "
                          "the way back to where they started."):
            self.play(t.animate.set_value(1.05), xt.animate.set_value(9.6),
                      run_time=3.0, rate_func=linear)
        self.beat()

        gone = cards.body("The firm does not come back.", size=T_HEAD, color=CHALK,
                          width=22)
        gone.move_to(RIGHT * 3.0 + DOWN * 2.2)
        with self.narrate("The firm does not come back. Because coming back means "
                          "paying the whole set-up cost over again."):
            self.play(FadeIn(gone), run_time=1.0)
        self.beat()

        # -------------------------------------------------- the plain statement
        self.clear_stage()
        plain = cards.body("What it prevented needs no explaining.\nWhat never came back does.",
                           size=T_SUB, color=CHALK, width=42)
        with self.narrate("State it plainly. What the policy stops from happening does "
                          "not need explaining. What needs explaining is why, for the "
                          "firms it did not reach in time, nothing came back."):
            self.play(FadeIn(plain), run_time=1.4)
        self.beat()

        # -------------------------------------------------- the caveats
        self.clear_stage()
        kit = stick.kit(scale=0.8).move_to(LEFT * 5.4 + DOWN * 1.8)
        self.play(FadeIn(kit), kit.mood("thinking"), run_time=0.5)
        head = cards.section_title("And carry both caveats", color=SRC_KIT, size=T_SUB)
        self.play(FadeIn(head), run_time=0.5)
        cav = cards.bullet_list([
            "rests on “ruined instantly” — a flagged simplification",
            "and the policy kept some of them alive",
        ], color=CHALK, width=42, dotc=SRC_KIT)
        cav.move_to(RIGHT * 0.8 + UP * 0.2)
        says = ["This limb rests on Dixit's assumption that a stopped business is "
                "ruined instantly, which he flags himself as a simplification. Where a "
                "firm really can mothball a factory and restart it cheaply, this "
                "argument gets weaker.",
                "And chapter twenty-five's concession means the policy plausibly held "
                "some firms above the quit line who would otherwise have crossed it. So "
                "the group this applies to is smaller than Kit first supposed."]
        for i in range(2):
            with self.narrate(says[i]):
                self.play(FadeIn(cav[i], shift=RIGHT * 0.2), run_time=0.8)
        self.beat()

        self.close_chapter([
            "through the quit line ⇒ closed for good",
            "restored — and it does not return",
            "explain what never returned",
            "two caveats carried",
        ])
