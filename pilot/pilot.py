"""The pilot. Every primitive the film uses, on one reel, so the visual system
can be looked at and locked before a single chapter is written."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib import surface as SF
from lib.scale import MasterScale
from lib.theme import *


class Pilot(Chapter):
    CH = 0
    TITLE = "Pilot — every primitive"
    PART = "SYSTEM CHECK"
    RECAP_ICONS = ["scale", "fog", "money"]

    def body(self):
        # ---------------------------------------------------- 1. the cast
        self.heading("The cast, and how they move")
        nell = stick.nell(scale=1.05)
        St.place(nell, St.STAGE, ax=-0.7, ay=-0.2)
        lab = nell.label()
        self.play(FadeIn(nell), FadeIn(lab), run_time=0.8)
        self.play(nell.walk_to(St.STAGE.point(0.1, -0.2), run_time=2.0))
        for mood in ("thinking", "worried", "pleased", "surprised", "neutral"):
            self.play(nell.mood(mood), run_time=0.35)
        self.play(nell.pace(2, run_time=1.8))
        b = nell.say("I could build it now.", direction=UP, width=3.4)
        self.play(FadeIn(b), run_time=0.6)
        self.play(FadeOut(b), run_time=0.4)
        th = nell.think("Or I could wait.", direction=UP, width=3.0)
        self.play(FadeIn(th), run_time=0.6)
        self.play(FadeOut(th), run_time=0.4)

        self.side(["walks, with legs", "five moods", "speaks and thinks"],
                  colour=CHALK, dot_colour=WAIT)
        self.clear_stage()

        # ---------------------------------------------------- 2. a definition
        self.heading("A definition card")
        self.define("sunk cost", "Money you cannot get back.", "slab", SUNK,
                    hold=3.4)

        # ---------------------------------------------------- 3. bars growing
        self.heading("Bars, grown the way he grows them")
        ax = Axes(x_range=[0, 7, 1], y_range=[0, 5, 1], x_length=7.0,
                  y_length=3.4, axis_config=AXIS)
        St.place(ax, St.STAGE)
        self.play(Create(ax), run_time=1.2)
        bars = VGroup(*[
            Rectangle(width=0.62, height=h, color=MONEY, stroke_width=2,
                      fill_color=MONEY, fill_opacity=0.35)
            .move_to(ax.c2p(i + 1, 0) + UP * h / 2)
            for i, h in enumerate([0.9, 1.5, 2.1, 2.6, 2.9, 3.0])])
        St.collapse_bars(bars)
        self.add(bars)
        self.play(St.grow_bars(bars))
        self.play(S.pulse(bars[4]))
        self.park(VGroup(ax, bars), corner=UL, height=1.7)

        # ---------------------------------------------------- 4. the scale
        self.heading("The master scale")
        sc = MasterScale(x=-1.2, y=-0.3, height=4.2)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), FadeIn(sc.title),
                  run_time=1.0)
        for k, v, t, c, sw in [("L", 0.72, "0.72", TRIGGER, 5),
                               ("M", 1.10, "1.10", COST, 3),
                               ("H", 1.62, "1.62", TRIGGER, 5)]:
            g = sc.add_level(k, v, t, c, width=3.0, sw=sw)
            self.play(Create(g[0]), FadeIn(g[1]), run_time=0.5)
        band = sc.band(0.72, 1.62, TRIGGER, 0.14, width=3.0)
        self.play(FadeIn(band), run_time=0.8)

        # ---------------------------------------------------- 5. a counter
        n = St.number(1.00, TRIGGER, T_HEAD)
        St.place(n, St.SIDE, ay=0.5)
        self.play(FadeIn(n), run_time=0.6)
        self.play(S.count_to(n, 1.86, run_time=1.6))
        self.play(S.spark(n))
        self.foot("the trigger sits above the textbook line")
        self.clear_stage()

        # ---------------------------------------------------- 6. flow + flash
        self.heading("Flow, and the flash that races round a phrase")
        a = W.building(SRC_BR, 0.6, "government", "the government")
        St.place(a, St.STAGE, ax=-0.75)
        b2 = stick.StickFigure("a saver", CHALK, scale=0.8)
        St.place(b2, St.STAGE, ax=0.7)
        self.play(FadeIn(a), FadeIn(b2), run_time=0.9)
        arrow = W.flow_arrow(a.get_right() + RIGHT * 0.3,
                             b2.get_left() + LEFT * 0.3, MONEY)
        self.play(Create(arrow), run_time=0.8)
        self.play(S.flow_along(arrow, MONEY))
        c = St.caption("price up, yield down", SRC_BR, T_SUB, width=22)
        St.place(c, St.SIDE, ay=0.4)
        self.play(FadeIn(c), run_time=0.7)
        self.play(S.flash_around(c))
        self.clear_stage()

        # ---------------------------------------------------- 7. three dimensions
        self.drop_heading()
        axes3 = SF.axes()
        self.set_camera_orientation(phi=66 * DEGREES, theta=-56 * DEGREES, zoom=0.95)
        self.play(Create(axes3), run_time=1.0)
        sheet = SF.sheet(axes3)
        self.play(Create(sheet), run_time=2.2)
        dot = Dot3D(SF.point(axes3, 0.20, 0.05), radius=0.11, color=CHALK)
        self.play(FadeIn(dot), run_time=0.6)
        self.play(dot.animate.move_to(SF.point(axes3, 0.40, 0.02)), run_time=1.8)
        self.move_camera(phi=58 * DEGREES, theta=-120 * DEGREES, run_time=2.4)
        self.play(FadeOut(sheet), FadeOut(axes3), FadeOut(dot), run_time=0.8)
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES, zoom=1.0)

        self.close_chapter(["every primitive works",
                            "nothing overlaps",
                            "nothing is too small to read"])
