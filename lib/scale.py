"""The master revenue scale -- Part One's master diagram.

A single vertical scale of "money coming in each month". Built up live, one
element at a time, and re-used in chapters 2, 6, 10, 11, 12, 13, 14, 16, 22,
23 and 27. Dixit's worked example (running cost 1, sunk cost 2) puts the four
levels at 0.72, 1.00, 1.10 and 1.62, and those are the numbers the scale is
designed around.
"""
import numpy as np
from manim import (
    VGroup, Line, DashedLine, Text, Dot, Arrow, Rectangle, Polygon, Brace,
    UP, DOWN, LEFT, RIGHT, ORIGIN, VMobject, TracedPath, ValueTracker,
    FadeIn, FadeOut, Create, Write, GrowFromEdge, always_redraw,
)
from lib.theme import (
    CHALK, MUTED, MONEY, COST, SUNK, WAIT, TRIGGER, BG, FONT,
    T_BODY, T_SMALL, T_SUB,
)
from lib.cards import wrap

LO, HI = 0.55, 1.85          # bottom and top of the drawn scale
HEIGHT = 5.0                 # manim units from LO to HI


class MasterScale(VGroup):
    def __init__(self, x=-3.4, y=-0.4, height=HEIGHT, lo=LO, hi=HI, **kw):
        super().__init__(**kw)
        self.x0 = x
        self.y0 = y
        self.h = height
        self.lo = lo
        self.hi = hi
        self.axis = Line(RIGHT * x + UP * (y - height / 2),
                         RIGHT * x + UP * (y + height / 2),
                         color=MUTED, stroke_width=3)
        self.arrow_head = Polygon(
            RIGHT * x + UP * (y + height / 2 + 0.22),
            RIGHT * (x - 0.10) + UP * (y + height / 2),
            RIGHT * (x + 0.10) + UP * (y + height / 2),
            color=MUTED, fill_opacity=1, stroke_width=1)
        self.title = Text("Money coming in\neach month", font=FONT,
                          font_size=T_SMALL, color=MUTED, line_spacing=0.9)
        self.title.next_to(self.axis, UP, buff=0.42)
        if self.title.get_left()[0] < -6.9:
            self.title.shift(RIGHT * (-6.9 - self.title.get_left()[0]))
        self.lines = {}
        self.labels = {}
        self.add(self.axis, self.arrow_head)

    # ------------------------------------------------------------ geometry
    def pos(self, value):
        frac = (value - self.lo) / (self.hi - self.lo)
        return RIGHT * self.x0 + UP * (self.y0 - self.h / 2 + frac * self.h)

    def level_line(self, value, color, width=4.6, dashed=False, sw=4):
        p = self.pos(value)
        a = p + LEFT * 0.22
        b = p + RIGHT * width
        cls = DashedLine if dashed else Line
        return cls(a, b, color=color, stroke_width=sw)

    # ------------------------------------------------------------ building
    def add_level(self, key, value, text, color, dashed=False, width=4.6,
                  number=None, sw=4, label_size=T_SMALL):
        ln = self.level_line(value, color, width, dashed, sw)
        lab = Text(text, font=FONT, font_size=label_size, color=color)
        lab.next_to(ln, RIGHT, buff=0.28)
        # never let a label run off the frame
        over = lab.get_right()[0] - 6.85
        if over > 0:
            lab.scale(max(0.55, 1 - over / max(lab.width, 0.01)))
            lab.next_to(ln, RIGHT, buff=0.28)
            if lab.get_right()[0] > 6.85:
                lab.shift(LEFT * (lab.get_right()[0] - 6.85))
        grp = VGroup(ln, lab)
        if number is not None:
            num = Text(number, font=FONT, font_size=T_SMALL, color=color)
            num.next_to(ln, LEFT, buff=0.24)
            grp.add(num)
        self.lines[key] = ln
        self.labels[key] = grp
        self.add(grp)
        return grp

    def band(self, low, high, color, opacity=0.14, width=4.6):
        a = self.pos(low)
        b = self.pos(high)
        r = Rectangle(width=width + 0.22, height=abs(b[1] - a[1]),
                      color=color, fill_color=color, fill_opacity=opacity,
                      stroke_width=0)
        r.move_to((a + b) / 2 + RIGHT * (width / 2 - 0.11 + 0.22))
        return r

    def brace_between(self, low, high, text, color):
        a, b = self.pos(low), self.pos(high)
        seg = Line(a, b).shift(LEFT * 0.55)
        br = Brace(seg, direction=LEFT, color=color)
        t = Text(wrap(text, 14), font=FONT, font_size=T_SMALL, color=color,
                 line_spacing=0.9)
        t.next_to(br, LEFT, buff=0.20)
        return VGroup(br, t)

    def marker(self, value, color=MONEY, r=0.13):
        return Dot(self.pos(value), radius=r, color=color)

    def value_dot(self, tracker, color=MONEY, r=0.13, dx=0.0):
        return always_redraw(
            lambda: Dot(self.pos(tracker.get_value()) + RIGHT * dx,
                        radius=r, color=color))


def path_walk(scale, tracker, values, run_times, scene, dot, trail=None):
    """Move the revenue dot through a list of levels, leaving a trail."""
    for v, rt in zip(values, run_times):
        scene.play(tracker.animate.set_value(v), run_time=rt)
