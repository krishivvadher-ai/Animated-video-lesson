"""The six-link transmission chain -- Part Two's master diagram.

Bowdler and Radia set the mechanism out as a chain, and the film keeps it as
one: each link can be examined separately, and if a link fails the whole thing
stops there.
"""
from manim import (
    VGroup, Text, RoundedRectangle, Line, Polygon, Arrow, Circle, Cross,
    UP, DOWN, LEFT, RIGHT, ORIGIN, FadeIn, FadeOut, Create,
)
from lib.theme import (
    CHALK, MUTED, MONEY, COST, SUNK, WAIT, TRIGGER, BG, FONT,
    T_SMALL, T_BODY, SRC_BR, SRC_DX, SRC_KIT,
)
from lib.cards import wrap

LINKS = [
    "The Bank creates\nmoney and buys gilts",
    "Gilt prices rise,\nyields fall",
    "Other borrowing\nrates follow down",
    "The cheaper price\nreaches a firm",
    "The firm decides\nto build",
    "Investment and\noutput rise",
]


class Chain(VGroup):
    """Six labelled links running across the screen, with arrows between."""

    def __init__(self, y=0.0, width=12.6, color=SRC_BR, **kw):
        super().__init__(**kw)
        self.boxes = VGroup()
        self.arrows = VGroup()
        self.color = color
        bw = (width - 5 * 0.42) / 6
        for i, text in enumerate(LINKS):
            t = Text(text, font=FONT, font_size=20, color=CHALK,
                     line_spacing=0.92)
            if t.width > bw - 0.24:
                t.scale((bw - 0.24) / t.width)
            box = RoundedRectangle(width=bw, height=1.34, corner_radius=0.14,
                                   color=color, stroke_width=3,
                                   fill_color=BG, fill_opacity=1)
            num = Text(str(i + 1), font=FONT, font_size=18, color=MUTED)
            g = VGroup(box, t, num)
            t.move_to(box.get_center() + DOWN * 0.06)
            num.move_to(box.get_top() + DOWN * 0.20)
            self.boxes.add(g)
        self.boxes.arrange(RIGHT, buff=0.42)
        self.boxes.move_to(UP * y)
        for a, b in zip(self.boxes[:-1], self.boxes[1:]):
            self.arrows.add(Line(a.get_right() + RIGHT * 0.06,
                                 b.get_left() + LEFT * 0.06,
                                 color=MUTED, stroke_width=3)
                            .add_tip(tip_length=0.16))
        self.add(self.boxes, self.arrows)

    def link(self, i):
        return self.boxes[i]

    def highlight(self, i, color):
        box = self.boxes[i][0]
        return box.animate.set_stroke(color, width=7)

    def dim_all(self):
        return [b[0].animate.set_stroke(MUTED, width=2) for b in self.boxes]
