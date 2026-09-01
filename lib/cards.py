"""Title cards, definition cards, recap ladders, quotation cards, progress dot."""
import numpy as np
from manim import (
    VGroup, Text, RoundedRectangle, Rectangle, Line, Dot, Circle, Square,
    Triangle, Polygon, Arc, UP, DOWN, LEFT, RIGHT, ORIGIN, PI, FadeIn, FadeOut,
    Write, Create, GrowFromCenter, DEGREES,
)
from lib.theme import (
    BG, CHALK, MUTED, MONEY, COST, SUNK, WAIT, TRIGGER, FONT, GREY_A,
    T_HEAD, T_SUB, T_BODY, T_SMALL, T_TINY, SAFE_W, TOTAL_CHAPTERS,
)


def wrap(text, width=52):
    """Hard-wrap a string to a given column so Text never runs off screen."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return "\n".join(lines)


def body(text, size=T_BODY, color=CHALK, width=52, weight=None, t2c=None,
         plain=False, **kw):
    """Body text. The words that name things on screen are coloured, the way
    3Blue1Brown colours the symbols in an expression."""
    wrapped = wrap(text, width)
    colours = {}
    if not plain:
        from lib.style import t2c_for
        colours = t2c_for(wrapped, t2c)
    return Text(wrapped, font=FONT, font_size=size, color=color,
                line_spacing=0.95, t2c=colours, **kw)


def title_card(number, title, part=None):
    g = VGroup()
    num = Text(f"CHAPTER {number}", font=FONT, font_size=T_SMALL, color=MUTED)
    ttl = Text(wrap(title, 34), font=FONT, font_size=T_HEAD, color=CHALK,
               line_spacing=0.9)
    rule = Line(LEFT * 2.2, RIGHT * 2.2, color=MUTED, stroke_width=2)
    g.add(num, rule, ttl)
    g.arrange(DOWN, buff=0.34)
    if part:
        p = Text(part, font=FONT, font_size=T_SMALL, color=MUTED)
        p.next_to(g, DOWN, buff=0.55)
        g.add(p)
    return g


ICONS = {
    "money": lambda c: VGroup(
        Circle(radius=0.22, color=c, stroke_width=3),
        Text("£", font=FONT, font_size=24, color=c)),
    "flow": lambda c: VGroup(
        Line(LEFT * 0.28, RIGHT * 0.20, color=c, stroke_width=4),
        Polygon(RIGHT * 0.30, RIGHT * 0.14 + UP * 0.11, RIGHT * 0.14 + DOWN * 0.11,
                color=c, fill_opacity=1, stroke_width=1)),
    "slab": lambda c: VGroup(
        Rectangle(width=0.56, height=0.20, color=c, stroke_width=3,
                  fill_opacity=0.30, fill_color=c)),
    "fog": lambda c: VGroup(*[Line(LEFT * 0.28, RIGHT * 0.28, color=c,
                                   stroke_width=3).shift(UP * y)
                              for y in (0.12, 0.0, -0.12)]),
    "door": lambda c: VGroup(
        Rectangle(width=0.34, height=0.52, color=c, stroke_width=3),
        Dot(RIGHT * 0.10, radius=0.035, color=c)),
    "clock": lambda c: VGroup(
        Circle(radius=0.24, color=c, stroke_width=3),
        Line(ORIGIN, UP * 0.15, color=c, stroke_width=3),
        Line(ORIGIN, RIGHT * 0.11, color=c, stroke_width=3)),
    "scale": lambda c: VGroup(
        Line(DOWN * 0.28, UP * 0.28, color=c, stroke_width=3),
        Line(LEFT * 0.12, RIGHT * 0.12, color=c, stroke_width=3).shift(UP * 0.13),
        Line(LEFT * 0.12, RIGHT * 0.12, color=c, stroke_width=3).shift(DOWN * 0.13)),
    "voucher": lambda c: VGroup(
        Rectangle(width=0.58, height=0.32, color=c, stroke_width=3),
        Line(LEFT * 0.10 + DOWN * 0.16, LEFT * 0.10 + UP * 0.16, color=c,
             stroke_width=2)),
    "ticket": lambda c: VGroup(
        Rectangle(width=0.62, height=0.34, color=c, stroke_width=3),
        Line(LEFT * 0.20 + DOWN * 0.17, LEFT * 0.20 + UP * 0.17, color=c, stroke_width=2),
        Line(LEFT * 0.05, RIGHT * 0.22, color=c, stroke_width=2).shift(UP * 0.07),
        Line(LEFT * 0.05, RIGHT * 0.22, color=c, stroke_width=2).shift(DOWN * 0.05)),
    "bank": lambda c: VGroup(
        Polygon(LEFT * 0.34 + UP * 0.06, ORIGIN + UP * 0.30, RIGHT * 0.34 + UP * 0.06,
                color=c, stroke_width=3),
        *[Line(DOWN * 0.24, UP * 0.06, color=c, stroke_width=3).shift(RIGHT * x)
          for x in (-0.22, 0.0, 0.22)],
        Line(LEFT * 0.36 + DOWN * 0.26, RIGHT * 0.36 + DOWN * 0.26, color=c,
             stroke_width=3)),
    "lever": lambda c: VGroup(
        Line(LEFT * 0.30, RIGHT * 0.30, color=c, stroke_width=3).shift(DOWN * 0.24),
        Line(DOWN * 0.24, UP * 0.26 + RIGHT * 0.14, color=c, stroke_width=4),
        Dot(UP * 0.26 + RIGHT * 0.14, radius=0.06, color=c)),
    "chain": lambda c: VGroup(*[
        Circle(radius=0.13, color=c, stroke_width=3).shift(RIGHT * x)
        for x in (-0.20, 0.0, 0.20)]),
    "shield": lambda c: VGroup(
        Polygon(UP * 0.30, RIGHT * 0.24 + UP * 0.14, RIGHT * 0.20 + DOWN * 0.24,
                DOWN * 0.32, LEFT * 0.20 + DOWN * 0.24, LEFT * 0.24 + UP * 0.14,
                color=c, stroke_width=3, fill_opacity=0.18, fill_color=c)),
    "queue": lambda c: VGroup(*[
        Rectangle(width=0.16, height=0.26, color=c, stroke_width=3).shift(RIGHT * x)
        for x in (-0.26, 0.0, 0.26)]),
    "risk": lambda c: VGroup(*[
        Arc(radius=0.10, start_angle=0, angle=PI, color=c,
            stroke_width=3).shift(RIGHT * x + UP * 0.0)
        for x in (-0.20, 0.0, 0.20)]),
    "people": lambda c: VGroup(*[
        VGroup(Circle(radius=0.07, color=c, stroke_width=3).shift(UP * 0.16),
               Line(UP * 0.09, DOWN * 0.14, color=c, stroke_width=3)).shift(RIGHT * x)
        for x in (-0.20, 0.0, 0.20)]),
    "signal": lambda c: VGroup(
        Dot(ORIGIN, radius=0.05, color=c),
        *[Arc(radius=r, start_angle=-PI / 3, angle=2 * PI / 3, color=c, stroke_width=3)
          for r in (0.16, 0.28)]),
    "magnet": lambda c: VGroup(
        Arc(radius=0.26, start_angle=0, angle=PI, color=c, stroke_width=5),
        Line(LEFT * 0.26, LEFT * 0.26 + DOWN * 0.18, color=c, stroke_width=5),
        Line(RIGHT * 0.26, RIGHT * 0.26 + DOWN * 0.18, color=c, stroke_width=5)),
    "border": lambda c: VGroup(
        *[Line(DOWN * 0.28, UP * 0.28, color=c, stroke_width=3).shift(RIGHT * 0.0)],
        Rectangle(width=0.22, height=0.18, color=c, stroke_width=3).shift(LEFT * 0.30),
        Polygon(RIGHT * 0.22, RIGHT * 0.42 + UP * 0.10, RIGHT * 0.42 + DOWN * 0.10,
                color=c, stroke_width=2, fill_opacity=1)),
}


def icon(kind, color=CHALK, size=1.0):
    maker = ICONS.get(kind)
    g = maker(color) if maker else Square(side_length=0.4, color=color, stroke_width=3)
    g.scale(size)
    return g


def definition_card(term, definition, icon_kind=None, color=CHALK, width=40):
    """The word, a one-line plain definition, and its recurring icon."""
    head = Text(term, font=FONT, font_size=T_SUB, color=color)
    head_rule = Line(LEFT * head.width / 2, RIGHT * head.width / 2,
                     color=color, stroke_width=2)
    dfn = Text(wrap(definition, width), font=FONT, font_size=T_BODY, color=CHALK,
               line_spacing=0.95)
    head_rule.next_to(head, DOWN, buff=0.10).align_to(head, LEFT)
    headg = VGroup(head, head_rule)
    inner = VGroup(headg, dfn).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
    if icon_kind:
        ic = icon(icon_kind, color, 1.5)
        row = VGroup(ic, inner).arrange(RIGHT, buff=0.55)
    else:
        row = inner
    box = RoundedRectangle(width=row.width + 1.0, height=row.height + 0.9,
                           corner_radius=0.14, color=color, stroke_width=3,
                           fill_color=BG, fill_opacity=1.0)
    row.move_to(box.get_center())
    tag = Text("DEFINITION", font=FONT, font_size=T_TINY, color=MUTED)
    tag.next_to(box.get_top(), DOWN, buff=0.02).align_to(box, LEFT).shift(RIGHT * 0.35)
    return VGroup(box, row)


def quote_card(quote, attribution, color=CHALK, width=46):
    q = Text("“" + wrap(quote, width) + "”", font=FONT,
             font_size=T_SUB, color=color, line_spacing=1.0, slant="ITALIC")
    a = Text(attribution, font=FONT, font_size=T_SMALL, color=MUTED)
    g = VGroup(q, a).arrange(DOWN, buff=0.40)
    bar = Line(g.get_top(), g.get_bottom(), color=color, stroke_width=6)
    bar.next_to(g, LEFT, buff=0.45)
    return VGroup(bar, g)


def bullet_list(items, color=CHALK, size=T_BODY, width=46, buff=0.36, dotc=None,
                icons=None, icon_colors=None, icon_size=1.15):
    """A list. If icon names are given, each row is led by its picture."""
    rows = VGroup()
    for i, it in enumerate(items):
        if icons and i < len(icons) and icons[i]:
            ic = (icon_colors[i % len(icon_colors)] if icon_colors else (dotc or color))
            d = icon(icons[i], ic, icon_size)
        else:
            d = Dot(radius=0.06, color=dotc or color)
        t = body(it, size=size, color=color, width=width)
        r = VGroup(d, t).arrange(RIGHT, buff=0.36, aligned_edge=UP)
        d.align_to(t, UP).shift(DOWN * (0.02 if icons else 0.16))
        rows.add(r)
    rows.arrange(DOWN, buff=buff, aligned_edge=LEFT)
    return rows


def recap_panel(items, heading="So far", icons=None):
    h = Text(heading, font=FONT, font_size=T_SUB, color=MUTED)
    rule = Line(LEFT * 2.0, RIGHT * 2.0, color=MUTED, stroke_width=2)
    lst = bullet_list(items, width=40, buff=0.60, icons=icons,
                      icon_colors=[SUNK, WAIT, MONEY, TRIGGER], icon_size=1.7)
    g = VGroup(h, lst).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
    return g


def progress(chapter):
    """A small persistent indicator: where we are in the thirty-one chapters."""
    w = 2.6
    track = Line(LEFT * w / 2, RIGHT * w / 2, color=MUTED, stroke_width=1.5)
    track.set_opacity(0.45)
    frac = chapter / (TOTAL_CHAPTERS - 1)
    fill = Line(LEFT * w / 2, LEFT * w / 2 + RIGHT * w * frac,
                color=GREY_A, stroke_width=3)
    lab = Text(f"{chapter}/43", font=FONT, font_size=T_TINY, color=MUTED)
    lab.set_opacity(0.7)
    lab.next_to(track, LEFT, buff=0.24)
    g = VGroup(track, fill, lab)
    g.to_corner(DOWN + RIGHT, buff=0.34)
    return g


def source_tag(text, color):
    """A small coloured tag saying whose claim is on screen (Part Two)."""
    t = Text(text, font=FONT, font_size=T_TINY, color=color)
    u = Line(t.get_corner(DOWN + LEFT), t.get_corner(DOWN + RIGHT),
             color=color, stroke_width=3).shift(DOWN * 0.10)
    return VGroup(t, u)


def note(text, color=MUTED, size=T_SMALL, width=70):
    return Text(wrap(text, width), font=FONT, font_size=size, color=color,
                line_spacing=0.95)
