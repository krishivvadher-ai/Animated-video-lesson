import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter11(Chapter):
    CH = 11
    TITLE = "How the future is modelled"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["fog", "flow", "scale", "clock"]

    def body(self):
        # ------------------------------------------------ one step
        self.heading("One step at a time")
        start = Dot(St.STAGE.point(-0.75, -0.1), radius=0.14, color=MONEY)
        sl = Text("this year", font=FONT, font_size=T_SMALL, color=MONEY)
        sl.next_to(start, DOWN, buff=0.3)
        up = Arrow(start.get_center(), start.get_center() + RIGHT * 2.4 + UP * 1.4,
                   color=MONEY, buff=0.16, stroke_width=5)
        dn = Arrow(start.get_center(), start.get_center() + RIGHT * 2.4 + DOWN * 1.4,
                   color=COST, buff=0.16, stroke_width=5)
        ul = Text("+20%", font=FONT, font_size=T_BODY, color=MONEY)
        ul.next_to(up.get_end(), RIGHT, buff=0.22)
        dl = Text("−20%", font=FONT, font_size=T_BODY, color=COST)
        dl.next_to(dn.get_end(), RIGHT, buff=0.22)
        with self.narrate("Every number in the next two chapters rests on one "
                          "assumption about how revenue moves. Each year, revenue does "
                          "one of two things. It goes up by a fixed percentage, or down "
                          "by one."):
            self.play(FadeIn(start), FadeIn(sl), run_time=0.6)
            self.play(GrowArrow(up), FadeIn(ul), run_time=0.8)
            self.play(GrowArrow(dn), FadeIn(dl), run_time=0.8)
        self.beat()
        pct = St.caption("percentages, not pounds", CHALK, T_SUB, width=18)
        St.place(pct, St.SIDE, ay=0.35)
        with self.narrate("Percentages rather than pounds, because a big firm swings by "
                          "big amounts and a small one by small amounts. That is the "
                          "only realistic way to do it."):
            self.play(FadeIn(pct), run_time=0.8)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the lattice
        self.heading("Now let it run")
        levels, dx, dy = 6, 1.55, 0.48
        nodes = {}
        for t in range(levels + 1):
            for k in range(t + 1):
                nodes[(t, k)] = np.array([-5.0 + t * dx, (t - 2 * k) * dy + 0.25, 0.0])
        edges = VGroup(*[Line(nodes[(t, k)], nodes[(t + 1, kk)], color=MUTED,
                              stroke_width=2)
                         for t in range(levels) for k in range(t + 1)
                         for kk in (k, k + 1)])
        pts = VGroup(*[Dot(p, radius=0.055, color=MUTED) for p in nodes.values()])
        with self.narrate("Do that again the next year, and the next. Every point "
                          "splits in two, and the possibilities fan out."):
            self.play(Create(edges), run_time=2.6)
            self.play(FadeIn(pts), run_time=0.7)
        self.beat()

        def walk(seed, colour, width):
            rng = np.random.default_rng(seed)
            k, seq = 0, [nodes[(0, 0)]]
            for t in range(levels):
                k += int(rng.random() < 0.5)
                seq.append(nodes[(t + 1, k)])
            m = VMobject(color=colour, stroke_width=width)
            m.set_points_as_corners(seq)
            return m

        one = walk(7, MONEY, 5)
        with self.narrate("Watch one possible path through it. That is one future — one "
                          "thing that might happen."):
            self.play(Create(one), run_time=2.0)
        more = VGroup(*[walk(s + 20, WAIT, 2.5) for s in range(12)])
        with self.narrate("And here are a dozen more. Nobody knows which one happens. "
                          "All anybody knows is the shape of the fan."):
            self.play(LaggedStartMap(Create, more, lag_ratio=0.12), run_time=3.0)
        self.beat()
        self.define("a random walk", "Each step is up or down, and you cannot tell "
                    "which.", "fog", WAIT, at=DOWN * 2.4, hold=4.0)
        self.clear_stage()

        # ------------------------------------------------ the spread
        self.heading("One number describes the whole fan")
        ax = Axes(x_range=[-3, 3, 1], y_range=[0, 1.3, 1], x_length=8.0, y_length=2.6,
                  axis_config=AXIS)
        St.place(ax, St.STAGE, ay=-0.1)
        narrow = ax.plot(lambda x: np.exp(-x * x / (2 * 0.35 ** 2)), color=MONEY,
                         stroke_width=5)
        wide = ax.plot(lambda x: np.exp(-x * x / (2 * 1.0 ** 2)), color=COST,
                       stroke_width=5)
        self.play(Create(ax), run_time=0.9)
        nl = St.caption("a calm trade — 10% a year", MONEY, T_BODY, width=20)
        St.place(nl, St.SIDE, ay=0.55)
        wl = St.caption("a rough trade — 40% a year", COST, T_BODY, width=20)
        St.place(wl, St.SIDE, ay=0.05)
        with self.narrate("Take a typical year and ask how far revenue moved. In a calm "
                          "trade, not far. The outcomes bunch up."):
            self.play(Create(narrow), FadeIn(nl), run_time=1.4)
        with self.narrate("In a rough trade — oil, metals — they spread right out."):
            self.play(Create(wide), FadeIn(wl), run_time=1.4)
        self.beat()

        br = BraceBetweenPoints(ax.c2p(-1, 0.62), ax.c2p(1, 0.62), direction=UP,
                                color=CHALK)
        bt = Text("the choppiness", font=FONT, font_size=T_SMALL, color=CHALK)
        bt.next_to(br, UP, buff=0.15)
        with self.narrate("The width of that spread is the number the paper calls the "
                          "choppiness. It is the size of a typical yearly swing, as a "
                          "percentage. Ten per cent with exchange rates. Twenty-five to "
                          "forty for an oil well. And the base case at twenty."):
            self.play(GrowFromCenter(br), FadeIn(bt), run_time=1.2)
        self.beat()
        with self.narrate("The paper writes it as a Greek letter. This film never will. "
                          "It is the choppiness, and it is a percentage."):
            self.foot("the choppiness — never a Greek letter", MUTED)
        self.beat()

        self.close_chapter([
            "each year: up or down by a fixed percentage",
            "run it forward and the futures fan out",
            "nobody knows the path, only the fan",
            "the width of the fan is the choppiness",
        ])
