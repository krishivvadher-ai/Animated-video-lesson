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
    """An iron bar with a wire wound round it.

    The coil is drawn as a real helix -- each turn passing in front of the bar
    and back behind it -- rather than as a row of overlapping rings, which read
    as a smear rather than as a wire."""
    bar = Rectangle(width=3.4, height=0.62, color=color, stroke_width=4,
                    fill_color=color, fill_opacity=0.10)
    turns = 7
    front, back = VGroup(), VGroup()
    for i, x in enumerate(np.linspace(-1.30, 1.30, turns)):
        f = Arc(radius=0.46, start_angle=-PI / 2 + 0.28, angle=PI - 0.56,
                color=SUNK, stroke_width=5)
        f.rotate(PI).move_to(RIGHT * x)
        b = Arc(radius=0.46, start_angle=PI / 2 + 0.28, angle=PI - 0.56,
                color=SUNK, stroke_width=3, stroke_opacity=0.45)
        b.rotate(PI).move_to(RIGHT * (x + 0.20))
        back.add(b)
        front.add(f)
    lead_l = Line(back[0].get_start() + LEFT * 0.5, back[0].get_start(),
                  color=SUNK, stroke_width=4)
    lead_r = Line(front[-1].get_end(), front[-1].get_end() + RIGHT * 0.5,
                  color=SUNK, stroke_width=4)
    return VGroup(bar, back, front, lead_l, lead_r)


def ticket(color=CHALK, label="£100 in 2030", scale=1.0):
    """A bond drawn as a physical ticket: a stub, a perforation, and the terms."""
    t = Text(wrap(label, 15), font=FONT, font_size=T_SMALL, color=color,
             line_spacing=0.92)
    body_w = max(t.width + 0.5, 1.9)
    stub_w = 0.62
    r = Rectangle(width=body_w + stub_w, height=max(t.height + 0.55, 1.0),
                  color=color, stroke_width=3, fill_color=BG, fill_opacity=1)
    perf = DashedLine(r.get_top() + RIGHT * (r.width / 2 - stub_w),
                      r.get_bottom() + RIGHT * (r.width / 2 - stub_w),
                      color=color, stroke_width=2, dash_length=0.07)
    marks = VGroup(*[Line(LEFT * 0.16, RIGHT * 0.16, color=color, stroke_width=2)
                     .move_to(r.get_center() + RIGHT * (r.width / 2 - stub_w / 2)
                              + UP * y) for y in (0.16, 0.0, -0.16)])
    t.move_to(r.get_center() + LEFT * stub_w / 2)
    return VGroup(r, perf, marks, t).scale(scale)


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


# ------------------------------------------------------------------ buildings
def building(color=CHALK, size=1.0, kind="office", label=None):
    """A simple, readable building. kind: office | government | bank | house."""
    g = VGroup()
    if kind == "government":
        base = Rectangle(width=3.2, height=1.5, color=color, stroke_width=3)
        steps = VGroup(*[Line(LEFT * (1.7 + 0.12 * i), RIGHT * (1.7 + 0.12 * i),
                              color=color, stroke_width=3)
                         .shift(DOWN * (0.75 + 0.16 * i)) for i in range(3)])
        cols = VGroup(*[Line(DOWN * 0.72, UP * 0.62, color=color, stroke_width=3)
                        .shift(RIGHT * x) for x in (-1.15, -0.58, 0.0, 0.58, 1.15)])
        arch = Line(LEFT * 1.5 + UP * 0.62, RIGHT * 1.5 + UP * 0.62,
                    color=color, stroke_width=4)
        pediment = Polygon(LEFT * 1.7 + UP * 0.62, ORIGIN + UP * 1.5,
                           RIGHT * 1.7 + UP * 0.62, color=color, stroke_width=3)
        flag = VGroup(Line(UP * 1.5, UP * 2.15, color=color, stroke_width=3),
                      Polygon(UP * 2.15, UP * 2.15 + RIGHT * 0.5,
                              UP * 1.85 + RIGHT * 0.5, UP * 1.85,
                              color=color, stroke_width=2, fill_opacity=0.25,
                              fill_color=color))
        g.add(base, cols, arch, pediment, steps, flag)
        g.remove(base)
    elif kind == "bank":
        body = Rectangle(width=2.6, height=1.7, color=color, stroke_width=3)
        pediment = Polygon(LEFT * 1.5 + UP * 0.85, ORIGIN + UP * 1.6,
                           RIGHT * 1.5 + UP * 0.85, color=color, stroke_width=3)
        cols = VGroup(*[Line(DOWN * 0.85, UP * 0.85, color=color, stroke_width=3)
                        .shift(RIGHT * x) for x in (-0.9, -0.3, 0.3, 0.9)])
        step = Line(LEFT * 1.5 + DOWN * 0.9, RIGHT * 1.5 + DOWN * 0.9,
                    color=color, stroke_width=4)
        g.add(pediment, cols, step)
        g.remove(body)
    elif kind == "house":
        body = Rectangle(width=1.5, height=1.1, color=color, stroke_width=3)
        roof = Polygon(LEFT * 0.85 + UP * 0.55, ORIGIN + UP * 1.15,
                       RIGHT * 0.85 + UP * 0.55, color=color, stroke_width=3)
        door = Rectangle(width=0.3, height=0.45, color=color, stroke_width=2)
        door.move_to(DOWN * 0.32)
        win = Square(side_length=0.26, color=color, stroke_width=2).move_to(
            LEFT * 0.42 + UP * 0.1)
        g.add(body, roof, door, win)
    else:  # office
        body = Rectangle(width=2.0, height=2.6, color=color, stroke_width=3)
        wins = VGroup(*[Square(side_length=0.26, color=color, stroke_width=2)
                        .move_to(RIGHT * x + UP * y)
                        for x in (-0.55, 0.0, 0.55) for y in (-0.75, -0.1, 0.55, 1.0)])
        door = Rectangle(width=0.42, height=0.5, color=color, stroke_width=3)
        door.move_to(DOWN * 1.05)
        g.add(body, wins, door)
    g.scale(size)
    if label:
        t = Text(label, font=FONT, font_size=T_SMALL, color=MUTED)
        t.next_to(g, DOWN, buff=0.3)
        g = VGroup(g, t)
    return g


def coupon_stream(bond, n=4, color=MONEY):
    """Little coins falling out of a bond, one per year."""
    coins = VGroup()
    for i in range(n):
        c = coin(color, 0.13)
        c.move_to(bond.get_bottom() + DOWN * 0.5 + RIGHT * (i - (n - 1) / 2) * 0.75)
        coins.add(c)
    return coins
