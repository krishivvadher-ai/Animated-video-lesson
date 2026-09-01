"""Three balance sheets, drawn as three T-accounts that fill in live.

Bowdler and Radia set the mechanics of QE out as a shock to the balance sheets
of the three parties involved: the non-bank private sector, the central bank,
and the banking sector. The film draws all three, side by side.
"""
from manim import (
    VGroup, Text, Line, Rectangle, RoundedRectangle, UP, DOWN, LEFT, RIGHT, ORIGIN,
)
from lib.theme import BG, CHALK, MUTED, MONEY, COST, SRC_BR, FONT, T_SMALL, T_TINY


class TAccount(VGroup):
    """One party's balance sheet: assets on the left, liabilities on the right."""

    def __init__(self, name, width=3.6, height=2.3, colour=SRC_BR, **kw):
        super().__init__(**kw)
        self.box = Rectangle(width=width, height=height, color=colour,
                             stroke_width=3, fill_color=BG, fill_opacity=1)
        self.mid = Line(self.box.get_top() + DOWN * 0.55,
                        self.box.get_bottom(), color=colour, stroke_width=2)
        self.top = Line(self.box.get_left() + UP * (height / 2 - 0.55),
                        self.box.get_right() + UP * (height / 2 - 0.55),
                        color=colour, stroke_width=2)
        self.a = Text("assets", font=FONT, font_size=T_TINY, color=MUTED)
        self.l = Text("liabilities", font=FONT, font_size=T_TINY, color=MUTED)
        self.a.move_to(self.box.get_top() + DOWN * 0.30 + LEFT * width / 4)
        self.l.move_to(self.box.get_top() + DOWN * 0.30 + RIGHT * width / 4)
        self.title = Text(name, font=FONT, font_size=T_SMALL, color=colour)
        self.title.next_to(self.box, UP, buff=0.22)
        self.entries = VGroup()
        self.add(self.box, self.top, self.mid, self.a, self.l, self.title,
                 self.entries)
        self._n = {"L": 0, "R": 0}
        self._w = width

    def entry(self, text, side="L", sign="+"):
        colour = MONEY if sign == "+" else COST
        t = Text(f"{sign} {text}", font=FONT, font_size=T_SMALL, color=colour)
        if t.width > self._w / 2 - 0.24:
            t.scale((self._w / 2 - 0.24) / t.width)
        x = LEFT * self._w / 4 if side == "L" else RIGHT * self._w / 4
        y = self.box.get_top() + DOWN * (0.95 + 0.45 * self._n[side])
        t.move_to([0, y[1], 0]).shift(x + self.box.get_center() * 0 +
                                      RIGHT * self.box.get_center()[0])
        self._n[side] += 1
        self.entries.add(t)
        return t
