"""Re-usable visual devices. Built once, used in many chapters."""
import numpy as np
from manim import (
    VGroup, VMobject, Text, Rectangle, RoundedRectangle, Circle, Line,
    DashedLine, Dot, Polygon, Arrow, Arc, Ellipse, Square, Brace,
    UP, DOWN, LEFT, RIGHT, ORIGIN, PI, TAU, ValueTracker, always_redraw,
    FadeIn, FadeOut, Create, Write, GrowFromEdge, Transform, DEGREES,
)
from lib.theme import (
    BG, CHALK, MUTED, MONEY, COST, SUNK, WAIT, TRIGGER, FONT,
    T_BODY, T_SMALL, T_SUB, T_HEAD, T_TINY,
)
from lib.cards import wrap, body


# ------------------------------------------------------------------ money
def coin(color=MONEY, r=0.17):
    return VGroup(Circle(radius=r, color=color, stroke_width=3),
                  Text("£", font=FONT, font_size=int(r * 110), color=color))


def money_bag(color=MONEY, size=1.0, label=None):
    b = VGroup(
        Polygon(LEFT * 0.34 + DOWN * 0.42, RIGHT * 0.34 + DOWN * 0.42,
                RIGHT * 0.30 + UP * 0.22, LEFT * 0.30 + UP * 0.22,
                color=color, stroke_width=3, fill_color=color, fill_opacity=0.12),
        Line(LEFT * 0.22 + UP * 0.22, RIGHT * 0.22 + UP * 0.22, color=color,
             stroke_width=4),
        Text("£", font=FONT, font_size=26, color=color).shift(DOWN * 0.10),
    )
    b.scale(size)
    if label:
        t = Text(label, font=FONT, font_size=T_SMALL, color=color)
        t.next_to(b, DOWN, buff=0.18)
        b = VGroup(b, t)
    return b


def factory(color=CHALK, size=1.0, label=None):
    base = Rectangle(width=2.0, height=1.05, color=color, stroke_width=3)
    roof = Polygon(LEFT * 1.0 + UP * 0.52, LEFT * 0.35 + UP * 0.95,
                   RIGHT * 0.30 + UP * 0.95, RIGHT * 1.0 + UP * 0.52,
                   color=color, stroke_width=3)
    ch = Rectangle(width=0.24, height=0.66, color=color, stroke_width=3)
    ch.move_to(RIGHT * 0.62 + UP * 1.05)
    door = Rectangle(width=0.34, height=0.48, color=color, stroke_width=3)
    door.move_to(DOWN * 0.28)
    win = VGroup(*[Square(side_length=0.22, color=color, stroke_width=2)
                   .move_to(LEFT * x + UP * 0.08) for x in (0.30, 0.70)])
    g = VGroup(base, roof, ch, door, win).scale(size)
    if label:
        t = Text(label, font=FONT, font_size=T_SMALL, color=MUTED)
        t.next_to(g, DOWN, buff=0.20)
        g = VGroup(g, t)
    return g


def flow_arrow(start, end, color=MONEY, sw=6):
    a = Line(start, end, color=color, stroke_width=sw)
    a.add_tip(tip_length=0.24)
    return a


class Shop(VGroup):
    """Money in on one side, money out on the other -- the film's first picture."""

    def __init__(self, name="Nell's factory", **kw):
        super().__init__(**kw)
        self.building = factory(CHALK, 1.0)
        self.caption = Text(name, font=FONT, font_size=T_SMALL, color=MUTED)
        self.caption.next_to(self.building, DOWN, buff=0.24)
        self.add(self.building, self.caption)

    def inflow(self, label="revenue"):
        a = flow_arrow(self.building.get_left() + LEFT * 2.7,
                       self.building.get_left() + LEFT * 0.25, MONEY)
        t = Text(label, font=FONT, font_size=T_BODY, color=MONEY)
        t.next_to(a, UP, buff=0.18)
        return VGroup(a, t)

    def outflow(self, label="cost"):
        a = flow_arrow(self.building.get_right() + RIGHT * 0.25,
                       self.building.get_right() + RIGHT * 2.7, COST)
        t = Text(label, font=FONT, font_size=T_BODY, color=COST)
        t.next_to(a, UP, buff=0.18)
        return VGroup(a, t)


# ------------------------------------------------------------------ bars
class Bar(VGroup):
    """A labelled vertical bar. Numbers get pictures, never bare figures."""

    def __init__(self, height, width=0.9, color=MONEY, label=None,
                 value=None, opacity=0.25, base=ORIGIN, **kw):
        super().__init__(**kw)
        self.h = height
        r = Rectangle(width=width, height=max(height, 0.02), color=color,
                      stroke_width=3, fill_color=color, fill_opacity=opacity)
        r.move_to(np.array(base) + UP * height / 2)
        self.rect = r
        self.add(r)
        if label:
            t = Text(wrap(label, 14), font=FONT, font_size=T_SMALL, color=color,
                     line_spacing=0.9)
            t.next_to(r, DOWN, buff=0.22)
            self.add(t)
        if value:
            v = Text(value, font=FONT, font_size=T_BODY, color=color)
            v.next_to(r, UP, buff=0.16)
            self.add(v)


def stacked_cost_bar(parts, x=0.0, width=1.1, base_y=-2.2):
    """parts: list of (height, colour, label). Built bottom-up."""
    g = VGroup()
    y = base_y
    for h, c, lab in parts:
        r = Rectangle(width=width, height=h, color=c, stroke_width=3,
                      fill_color=c, fill_opacity=0.28)
        r.move_to(RIGHT * x + UP * (y + h / 2))
        t = Text(lab, font=FONT, font_size=T_SMALL, color=c)
        t.next_to(r, RIGHT, buff=0.24)
        g.add(VGroup(r, t))
        y += h
    return g


# ------------------------------------------------------------------ fog
def fog(width=4.0, height=2.4, n=7, color=MUTED, opacity=0.55):
    g = VGroup()
    rng = np.random.default_rng(4)
    for i in range(n):
        e = Ellipse(width=width * rng.uniform(0.45, 0.9),
                    height=height * rng.uniform(0.28, 0.5),
                    color=color, stroke_width=0, fill_color=color,
                    fill_opacity=opacity)
        e.move_to(RIGHT * rng.uniform(-width / 2.4, width / 2.4) +
                  UP * rng.uniform(-height / 2.4, height / 2.4))
        g.add(e)
    return g


# ------------------------------------------------------------------ dials
class Dial(VGroup):
    """A labelled dial with a needle -- the sealed machine of chapter 8."""

    def __init__(self, name, readout, lo_angle=210, hi_angle=-30, frac=0.35,
                 color=WAIT, r=0.85, **kw):
        super().__init__(**kw)
        self.lo, self.hi, self.r, self.color = lo_angle, hi_angle, r, color
        self.face = Circle(radius=r, color=color, stroke_width=3)
        self.ticks = VGroup(*[
            Line(ORIGIN, RIGHT * 0.12, color=MUTED, stroke_width=2)
            .shift(RIGHT * (r - 0.12))
            .rotate(np.deg2rad(lo_angle + (hi_angle - lo_angle) * f), about_point=ORIGIN)
            for f in np.linspace(0, 1, 7)])
        self.needle = Line(ORIGIN, RIGHT * (r - 0.18), color=color, stroke_width=5)
        self.hub = Dot(ORIGIN, radius=0.07, color=color)
        self.name = Text(wrap(name, 16), font=FONT, font_size=T_SMALL,
                         color=color, line_spacing=0.9)
        self.name.next_to(self.face, DOWN, buff=0.28)
        self.readout = Text(readout, font=FONT, font_size=T_BODY, color=CHALK)
        self.readout.next_to(self.name, DOWN, buff=0.18)
        self.add(self.face, self.ticks, self.needle, self.hub, self.name,
                 self.readout)
        self.set_frac(frac)

    def set_frac(self, f):
        ang = np.deg2rad(self.lo + (self.hi - self.lo) * f)
        c = self.face.get_center()
        self.needle.become(Line(c, c + np.array([np.cos(ang), np.sin(ang), 0]) *
                                (self.r - 0.18), color=self.color, stroke_width=5))
        return self

    def turn_to(self, f, readout=None):
        tgt = self.copy().set_frac(f)
        if readout:
            new = Text(readout, font=FONT, font_size=T_BODY, color=CHALK)
            new.move_to(self.readout)
            tgt.readout.become(new)
        return Transform(self, tgt)


# ------------------------------------------------------------------ misc
def door(color=CHALK, w=1.0, h=2.0, label=None):
    fr = Rectangle(width=w, height=h, color=color, stroke_width=4)
    kn = Dot(RIGHT * (w / 2 - 0.18), radius=0.055, color=color)
    g = VGroup(fr, kn)
    if label:
        t = Text(wrap(label, 16), font=FONT, font_size=T_SMALL, color=color,
                 line_spacing=0.9)
        t.next_to(fr, DOWN, buff=0.22)
        g.add(t)
    return g


def iron_bar(color=CHALK):
    bar = Rectangle(width=3.0, height=0.5, color=color, stroke_width=4,
                    fill_color=color, fill_opacity=0.10)
    coils = VGroup(*[Arc(radius=0.42, start_angle=-PI / 2.2, angle=PI * 1.4,
                         color=SUNK, stroke_width=4).move_to(RIGHT * x)
                     for x in np.linspace(-1.0, 1.0, 6)])
    return VGroup(bar, coils)


def ticket(color=CHALK, label="£100 in 2030", scale=1.0):
    r = Rectangle(width=2.6, height=1.4, color=color, stroke_width=3,
                  fill_color=BG, fill_opacity=1)
    perf = DashedLine(r.get_top() + LEFT * 0.72, r.get_bottom() + LEFT * 0.72,
                      color=color, stroke_width=2, dash_length=0.08)
    t = Text(wrap(label, 16), font=FONT, font_size=T_SMALL, color=color,
             line_spacing=0.9)
    t.move_to(r.get_center() + RIGHT * 0.34)
    return VGroup(r, perf, t).scale(scale)


def shield(color=SUNK, label=None, scale=1.0):
    s = Polygon(UP * 0.62, RIGHT * 0.50 + UP * 0.28, RIGHT * 0.42 + DOWN * 0.48,
                DOWN * 0.68, LEFT * 0.42 + DOWN * 0.48, LEFT * 0.50 + UP * 0.28,
                color=color, stroke_width=3, fill_color=color, fill_opacity=0.16)
    g = VGroup(s)
    if label:
        t = Text(wrap(label, 20), font=FONT, font_size=T_SMALL, color=color,
                 line_spacing=0.9)
        t.next_to(s, DOWN, buff=0.20)
        g.add(t)
    return g.scale(scale)


def spring(color=COST, turns=7, width=2.4, height=0.9, compressed=0.0):
    w = width * (1 - 0.55 * compressed)
    pts = []
    for i in range(turns * 12 + 1):
        a = i / (turns * 12)
        pts.append(np.array([-w / 2 + w * a,
                             height / 2 * np.sin(a * turns * TAU), 0]))
    m = VMobject(color=color, stroke_width=4)
    m.set_points_smoothly(pts)
    return m


def arrow_pair(center, up_color=MONEY, down_color=COST, span=1.1):
    a = Arrow(center + DOWN * span, center, color=up_color, buff=0,
              stroke_width=6, max_tip_length_to_length_ratio=0.22)
    b = Arrow(center + UP * span, center, color=down_color, buff=0,
              stroke_width=6, max_tip_length_to_length_ratio=0.22)
    return VGroup(a, b)


def table_two_row(head, rows, colors, width=5.4, font_size=T_SMALL):
    """A two-column, two-row table built live (chapter 26)."""
    g = VGroup()
    cells = []
    for r, (a, b) in enumerate(rows):
        ta = body(a, size=font_size, color=colors[r], width=26)
        tb = body(b, size=font_size, color=CHALK, width=34)
        cells.append((ta, tb))
    ca = VGroup(*[c[0] for c in cells]).arrange(DOWN, buff=1.0, aligned_edge=LEFT)
    cb = VGroup(*[c[1] for c in cells]).arrange(DOWN, buff=1.0, aligned_edge=LEFT)
    row = VGroup(ca, cb).arrange(RIGHT, buff=0.9, aligned_edge=UP)
    g.add(row)
    return g, cells
