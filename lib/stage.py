"""The staging system.

A scene is built out of **regions**, and no two regions overlap. Placing a
thing into a region fits it to that region, so two things on screen cannot
collide. Three rules are enforced by raising an error rather than by silently
coping, because every one of them was broken by hand in the first attempt:

1. A caption is at most `MAX_CAPTION` characters. Anything longer belongs in
   the narration, which is spoken, not printed.
2. Text is never scaled below `MIN_LINE`. If it does not fit at a readable
   size there is too much of it.
3. Every narrated beat has something moving. A beat that plays no animation
   raises, unless it is declared a deliberate hold.

The motion vocabulary underneath is 3Blue1Brown's, read out of his own video
source: bars that grow by being restored from a collapsed state, finished
diagrams that shrink into a corner instead of vanishing, charts that morph
into their successors, and labels that cross-fade one after another.
"""
import numpy as np
from manim import (
    VGroup, VMobject, Text, Line, Rectangle, RoundedRectangle, Dot,
    FadeIn, FadeOut, Write, Create, Transform, ReplacementTransform,
    TransformFromCopy, FadeTransform, LaggedStart, LaggedStartMap, Restore,
    GrowFromCenter, GrowArrow, Underline, SurroundingRectangle,
    UP, DOWN, LEFT, RIGHT, UL, UR, DL, DR, ORIGIN, PI,
)
from lib.theme import (
    CHALK, MUTED, MONEY, COST, SUNK, WAIT, TRIGGER, BG, FONT, LAG,
    T_HEAD, T_SUB, T_BODY, T_SMALL, T_TINY, BUFF_TITLE,
)
from lib import style as S
from lib.cards import wrap

MAX_CAPTION = 60      # characters; longer is narration, not a caption
MAX_DEFINITION = 84   # a definition card is allowed one full line
MIN_FONT = 22         # the readable minimum, in Manim font-size units


class Region:
    """A rectangle on the frame. Regions never overlap."""

    def __init__(self, name, x0, x1, y0, y1):
        self.name, self.x0, self.x1, self.y0, self.y1 = name, x0, x1, y0, y1

    @property
    def width(self):
        return self.x1 - self.x0

    @property
    def height(self):
        return self.y1 - self.y0

    @property
    def centre(self):
        return np.array([(self.x0 + self.x1) / 2, (self.y0 + self.y1) / 2, 0.0])

    def point(self, ax=0.0, ay=0.0):
        """A point inside the region; ax, ay in -1..1 from the centre."""
        return np.array([
            (self.x0 + self.x1) / 2 + ax * self.width / 2,
            (self.y0 + self.y1) / 2 + ay * self.height / 2, 0.0])

    def box(self, colour=MUTED):
        r = Rectangle(width=self.width, height=self.height, color=colour,
                      stroke_width=1)
        r.move_to(self.centre)
        return r


# The frame is 14.222 by 8.0. These divide it up and do not overlap.
TITLE = Region("title", -6.9, 6.9, 2.88, 3.86)
STAGE = Region("stage", -6.9, 1.9, -3.00, 2.62)     # with a side column
SIDE = Region("side", 2.25, 6.9, -3.00, 2.62)
FULL = Region("full", -6.9, 6.9, -3.00, 2.62)       # no side column
WIDE = Region("wide", -6.9, 6.9, -3.00, 3.80)       # no title either
FOOT = Region("foot", -6.9, 4.30, -3.90, -3.10)     # one short line

REGIONS = {r.name: r for r in (TITLE, STAGE, SIDE, FULL, WIDE, FOOT)}


class CaptionTooLong(ValueError):
    pass


class TextTooSmall(ValueError):
    pass


class NothingHappened(ValueError):
    pass


def check_caption(text, limit=MAX_CAPTION):
    flat = " ".join(str(text).split())
    if len(flat) > limit:
        raise CaptionTooLong(
            f"{len(flat)} characters on screen; the limit is {limit}. "
            f"Put it in the narration instead: {flat[:90]!r}")
    return flat


def effective_font_size(mob):
    """The size a caption is actually rendered at, after any scaling.

    Measured from the font size rather than the bounding box, because a word
    with no ascenders -- "now" -- has a box barely half the height of one with
    them, and the box would flag it wrongly.

    A one- or two-character glyph is decoration, not a caption.
    """
    txt = getattr(mob, "text", None)
    if not isinstance(txt, str) or len(txt.strip()) < 3:
        return None
    fs = getattr(mob, "font_size", None)
    if fs is None:
        return None
    return fs * getattr(mob, "_stage_scale", 1.0)


def fit(mob, region, pad=0.25, strict=True):
    """Shrink a thing until it sits inside a region. Text that would end up
    too small to read raises instead of shrinking."""
    max_w = region.width - 2 * pad
    max_h = region.height - 2 * pad
    k = 1.0
    if mob.width > max_w:
        k *= max_w / mob.width
        mob.scale(max_w / mob.width)
    if mob.height > max_h:
        k *= max_h / mob.height
        mob.scale(max_h / mob.height)
    if k < 1.0:
        for sub in mob.get_family():
            sub._stage_scale = getattr(sub, "_stage_scale", 1.0) * k
    if strict:
        for sub in mob.get_family():
            fs = effective_font_size(sub)
            if fs is not None and fs < MIN_FONT:
                raise TextTooSmall(
                    f"{fs:.0f} in {region.name!r}; the readable minimum is "
                    f"{MIN_FONT}. There is too much text: "
                    f"{str(getattr(sub, 'text', ''))[:60]!r}")
    return mob


def place(mob, region, ax=0.0, ay=0.0, pad=0.25, strict=True):
    """Fit a thing to a region and put it there."""
    fit(mob, region, pad, strict)
    mob.move_to(region.point(ax, ay))
    # keep it inside even after the offset
    if mob.get_left()[0] < region.x0 + 0.05:
        mob.shift(RIGHT * (region.x0 + 0.05 - mob.get_left()[0]))
    if mob.get_right()[0] > region.x1 - 0.05:
        mob.shift(LEFT * (mob.get_right()[0] - (region.x1 - 0.05)))
    if mob.get_bottom()[1] < region.y0 + 0.05:
        mob.shift(UP * (region.y0 + 0.05 - mob.get_bottom()[1]))
    if mob.get_top()[1] > region.y1 - 0.05:
        mob.shift(DOWN * (mob.get_top()[1] - (region.y1 - 0.05)))
    return mob


# ---------------------------------------------------------------- text pieces
def caption(text, colour=CHALK, size=T_BODY, width=26):
    """One short label. Anything long enough to be a paragraph raises."""
    flat = check_caption(text)
    wrapped = wrap(flat, width)
    return Text(wrapped, font=FONT, font_size=size, color=colour,
                line_spacing=0.95, t2c=S.t2c_for(wrapped))


def heading(text, colour=CHALK, size=T_SUB):
    """His section heading: large, at the top, with an underline beneath."""
    flat = check_caption(text)
    t = Text(flat, font=FONT, font_size=size, color=colour, t2c=S.t2c_for(flat))
    if t.width > TITLE.width - 0.4:
        t.scale((TITLE.width - 0.4) / t.width)
    u = Line(t.get_corner(DL), t.get_corner(DR), color=colour, stroke_width=3)
    u.shift(DOWN * 0.16).set_opacity(0.7)
    g = VGroup(t, u)
    g.move_to(TITLE.centre)
    return g


def points(items, colour=CHALK, size=T_BODY, width=22, dot_colour=None,
           icons=None, buff=0.55):
    """A column of short labels, each with a mark. Not a paragraph: every item
    is checked against the caption limit."""
    from lib.cards import icon as make_icon
    rows = VGroup()
    for i, it in enumerate(items):
        flat = check_caption(it)
        if icons and i < len(icons) and icons[i]:
            mark = make_icon(icons[i], dot_colour or colour, 1.2)
        else:
            mark = Dot(radius=0.065, color=dot_colour or colour)
        t = Text(wrap(flat, width), font=FONT, font_size=size, color=colour,
                 line_spacing=0.95, t2c=S.t2c_for(wrap(flat, width)))
        row = VGroup(mark, t).arrange(RIGHT, buff=0.32, aligned_edge=UP)
        mark.align_to(t, UP).shift(DOWN * 0.09)
        rows.add(row)
    rows.arrange(DOWN, buff=buff, aligned_edge=LEFT)
    return rows


def number(value, colour=TRIGGER, size=T_HEAD, places=2, prefix="", suffix=""):
    return S.counter(value, colour, size, places, prefix, suffix)


# ---------------------------------------------------------------- his moves
def collapse_bars(bars):
    """Save each bar and flatten it to the axis, ready to be grown."""
    for b in bars:
        b.save_state()
        b.stretch(0.0001, 1, about_edge=DOWN)
    return bars


def grow_bars(bars, lag=0.12, run_time=1.8):
    """His bar growth: restore from the collapsed state, staggered."""
    return LaggedStartMap(Restore, bars, lag_ratio=lag, run_time=run_time)


def park(mob, corner=UL, height=1.9, run_time=1.2):
    """Shrink a finished diagram into a corner instead of throwing it away."""
    return mob.animate(run_time=run_time).set(height=height).to_corner(
        corner, buff=0.45)


def morph_labels(pairs, lag=0.05, run_time=1.6):
    """Labels cross-fading one after another into their successors."""
    return LaggedStart(*(FadeTransform(a, b) for a, b in pairs),
                       lag_ratio=lag, run_time=run_time)
