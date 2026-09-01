"""3Blue1Brown's animation vocabulary, as helpers this film can use everywhere.

Idioms taken from his published video source (github.com/3b1b/videos): the
staggered reveal, the copy that flies out and becomes the next thing, the
cross-fade morph, the box that flashes round a phrase, and colouring the words
that name things on screen.
"""
import numpy as np
from manim import (
    Indicate, Circle, Succession, Uncreate, ApplyWave, AnimationGroup,
    VGroup, VMobject, Text, Mobject, Line, DashedLine, Arrow, DoubleArrow,
    Circle, Rectangle, RoundedRectangle, Polygon, Dot, SurroundingRectangle,
    Underline, ValueTracker, always_redraw,
    FadeIn, FadeOut, Write, Create, Transform, ReplacementTransform,
    TransformFromCopy, FadeTransform, LaggedStart, LaggedStartMap,
    GrowFromCenter, GrowArrow, DrawBorderThenFill, Circumscribe, Flash,
    Indicate, ShowPassingFlash, AnimationGroup, Succession,
    UP, DOWN, LEFT, RIGHT, ORIGIN, PI, smooth, there_and_back,
)
from lib.theme import (
    CHALK, MUTED, MONEY, COST, SUNK, WAIT, TRIGGER, BG, FONT, LAG,
    T_BODY, T_SMALL, YELLOW_D, BLUE_C, GREEN_C, RED_C, GOLD_C,
)

# ---------------------------------------------------------------- word colour
# 3b1b colours the symbols that name the things on screen. This is the film's
# vocabulary, and it is applied automatically wherever text is built.
T2C = {
    # money and outcomes
    "revenue": MONEY, "Revenue": MONEY, "profit": MONEY, "profits": MONEY,
    "gains": MONEY, "upside": MONEY, "good news": MONEY, "cheaper": MONEY,
    # costs and bad outcomes
    "cost": COST, "Cost": COST, "costs": COST, "loss": COST, "losses": COST,
    "downside": COST, "bad news": COST,
    # irreversibility
    "sunk": SUNK, "Sunk": SUNK, "irreversible": SUNK,
    # waiting and uncertainty
    "waiting": WAIT, "Waiting": WAIT, "uncertainty": WAIT, "uncertain": WAIT,
    "choppiness": WAIT, "choppier": WAIT, "option": WAIT, "patience": WAIT,
    # the thing the whole film is about
    "trigger": TRIGGER, "Trigger": TRIGGER, "hurdle": TRIGGER,
    "multiplier": TRIGGER, "hysteresis": TRIGGER, "Hysteresis": TRIGGER,
    "the bar": TRIGGER,
}


def t2c_for(text, extra=None):
    """Colour ranges for one string.

    Longest match first, and never overlapping, so "cost" inside "costs" can
    never fight with it. Returned as explicit index ranges, which is the form
    Manim colours exactly.
    """
    table = dict(T2C)
    if extra:
        table.update(extra)
    words = sorted(table, key=len, reverse=True)
    taken = [False] * len(text)
    out = {}
    for w in words:
        start = 0
        while True:
            i = text.find(w, start)
            if i < 0:
                break
            j = i + len(w)
            # whole words only, and not already coloured
            before_ok = i == 0 or not (text[i - 1].isalpha())
            after_ok = j >= len(text) or not (text[j].isalpha())
            if before_ok and after_ok and not any(taken[i:j]):
                out[f"[{i}:{j}]"] = table[w]
                for k in range(i, j):
                    taken[k] = True
            start = j
    return out





# ---------------------------------------------------------------- reveals
def lag_map(anim_class, group, lag=LAG, run_time=None, lag_ratio=None, **kw):
    """What LaggedStartMap should do.

    Manim's own LaggedStartMap passes each submobject to the animation as
    ``*args``, which silently unpacks a group into its children -- so a group
    of two-part coins becomes ``GrowFromCenter(circle, text)``. This builds the
    animations one at a time instead."""
    anims = [anim_class(m, **kw) for m in group]
    extra = {"run_time": run_time} if run_time else {}
    return LaggedStart(*anims, lag_ratio=lag if lag_ratio is None else lag_ratio,
                       **extra)


def reveal(mob, direction=UP, lag=LAG, run_time=None):
    """His commonest move: a staggered fade in, drifting a little."""
    if isinstance(mob, VGroup) and len(mob) > 1:
        return LaggedStartMap(FadeIn, mob, shift=direction * 0.25,
                              lag_ratio=lag, run_time=run_time or 1.4)
    return FadeIn(mob, shift=direction * 0.25, run_time=run_time or 1.0)


def dismiss(mob, direction=DOWN, run_time=0.7):
    return FadeOut(mob, shift=direction * 0.15, run_time=run_time)


def draw(mob, run_time=1.4):
    return Create(mob, run_time=run_time)


def from_copy(source, target, arc=PI / 2, run_time=1.4):
    """A copy of something already on screen becomes the new thing."""
    return TransformFromCopy(source, target, path_arc=arc, run_time=run_time)


def morph(a, b, run_time=1.4):
    """Cross-fade one thing into another."""
    return FadeTransform(a, b, run_time=run_time)


# ---------------------------------------------------------------- emphasis
def box(mob, colour=YELLOW_D, buff=0.14):
    return SurroundingRectangle(mob, color=colour, buff=buff, stroke_width=3,
                                corner_radius=0.06)


def flash_around(mob, colour=None, run_time=1.6, buff=0.14, color=None,
                 stroke_width=4, **kw):
    """The outline that races round a phrase and vanishes -- his FlashAround."""
    c = colour or color or YELLOW_D
    r = SurroundingRectangle(mob, color=c, buff=buff, stroke_width=stroke_width,
                             corner_radius=0.06)
    return ShowPassingFlash(r, time_width=0.6, run_time=run_time)


def indicate(mob, colour=YELLOW_D, run_time=1.0, scale=1.14):
    """His Indicate: a quick swell and colour flash, then back."""
    return Indicate(mob, color=colour, scale_factor=scale, run_time=run_time)


def circle_around(mob, colour=YELLOW_D, run_time=1.2, buff=0.16):
    """His CircleIndicate: a ring drawn round a thing, then taken away."""
    ring = Circle(color=colour, stroke_width=4)
    ring.surround(mob, buffer_factor=1.0).scale(1 + buff)
    return Succession(Create(ring, run_time=run_time * 0.55),
                      Uncreate(ring, run_time=run_time * 0.45))


def wave(mob, run_time=1.2, amplitude=0.18):
    """His ApplyWave, for a thing that should look alive rather than static."""
    return ApplyWave(mob, amplitude=amplitude, run_time=run_time)


def dim(mobs, opacity=0.28, run_time=0.6):
    """Push everything else back so the eye goes where it is wanted."""
    return AnimationGroup(*[m.animate.set_opacity(opacity) for m in mobs],
                          run_time=run_time)


def undim(mobs, run_time=0.6):
    return AnimationGroup(*[m.animate.set_opacity(1.0) for m in mobs],
                          run_time=run_time)


def underline(mob, colour=YELLOW_D, run_time=0.8):
    u = Underline(mob, color=colour, stroke_width=4, buff=0.12)
    return Create(u, run_time=run_time)


def pulse(mob, colour=YELLOW_D, run_time=1.2, scale=1.06):
    return Indicate(mob, color=colour, scale_factor=scale, run_time=run_time)


def spark(mob, colour=YELLOW_D, run_time=0.9):
    return Flash(mob, color=colour, line_length=0.26, num_lines=14,
                 flash_radius=0.42, run_time=run_time)


def flow_along(path, colour=MONEY, run_time=1.6, width=0.5):
    """A pulse of light running along a line -- his way of showing flow."""
    p = path.copy().set_stroke(colour, width=7)
    return ShowPassingFlash(p, time_width=width, run_time=run_time)


# ---------------------------------------------------------------- numbers
class Counter(VGroup):
    """A number that counts up on screen. Built from Text, so no LaTeX is
    needed anywhere in this film."""

    def __init__(self, value=0.0, colour=CHALK, size=T_BODY, places=2,
                 prefix="", suffix="", **kw):
        super().__init__(**kw)
        self.value = float(value)
        self.colour, self.size, self.places = colour, size, places
        self.prefix, self.suffix = prefix, suffix
        self.label = self._make(self.value)
        self.add(self.label)

    def _make(self, v):
        return Text(f"{self.prefix}{v:.{self.places}f}{self.suffix}",
                    font=FONT, font_size=self.size, color=self.colour)

    def set_value(self, v):
        c = self.get_center()
        self.label.become(self._make(float(v)).move_to(c))
        self.value = float(v)
        return self


def counter(value=0.0, colour=CHALK, size=T_BODY, places=2, prefix="", suffix=""):
    return Counter(value, colour, size, places, prefix, suffix)


def count_to(ctr, value, run_time=1.6):
    """Run a Counter up (or down) to a new value."""
    from manim import UpdateFromAlphaFunc
    start = ctr.value

    def uf(m, alpha):
        m.set_value(start + (value - start) * alpha)

    return UpdateFromAlphaFunc(ctr, uf, run_time=run_time)


def tracked_number(tracker, colour=CHALK, size=T_BODY, places=2, at=ORIGIN,
                   prefix="", suffix=""):
    def build():
        return Text(f"{prefix}{tracker.get_value():.{places}f}{suffix}",
                    font=FONT, font_size=size, color=colour).move_to(at)
    return always_redraw(build)
