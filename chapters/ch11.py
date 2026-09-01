import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.theme import *


class Chapter11(Chapter):
    CH = 11
    TITLE = "How the future is modelled"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["fog", "flow", "scale", "clock"]

    def body(self):
        with self.narrate("Every number in the next two chapters rests on one "
                          "assumption about how revenue moves. So we build that first, "
                          "and we build it with coins."):
            pass

        # ------------------------------------------------ one step
        head = Text("One step at a time", font=FONT, font_size=T_SUB,
                    color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)

        start = Dot(LEFT * 5.0, radius=0.14, color=MONEY)
        sl = Text("this year’s revenue", font=FONT, font_size=T_SMALL, color=MONEY)
        sl.next_to(start, DOWN, buff=0.3)
        up = Arrow(start.get_center(), start.get_center() + RIGHT * 2.2 + UP * 1.3,
                   color=MONEY, buff=0.14, stroke_width=5)
        dn = Arrow(start.get_center(), start.get_center() + RIGHT * 2.2 + DOWN * 1.3,
                   color=COST, buff=0.14, stroke_width=5)
        ul = Text("+20%", font=FONT, font_size=T_BODY, color=MONEY).next_to(up.get_end(), RIGHT, buff=0.2)
        dl = Text("−20%", font=FONT, font_size=T_BODY, color=COST).next_to(dn.get_end(), RIGHT, buff=0.2)
        with self.narrate("Each year, revenue does one of two things. It goes up by a "
                          "fixed percentage, or down by one."):
            self.play(FadeIn(start), FadeIn(sl), run_time=0.6)
            self.play(Create(up), FadeIn(ul), run_time=0.8)
            self.play(Create(dn), FadeIn(dl), run_time=0.8)
        self.beat()
        pct = cards.body("Percentages, not pounds — because a big firm swings by big "
                         "amounts and a small one by small ones.",
                         size=T_BODY, color=CHALK, width=30)
        pct.move_to(RIGHT * 3.0 + DOWN * 0.4)
        if pct.width > 5.4:
            pct.scale(5.4 / pct.width)
        with self.narrate("Percentages rather than pounds, because a big firm swings by "
                          "big amounts and a small one by small amounts. That is the "
                          "only realistic way to do it."):
            self.play(FadeIn(pct), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the tree
        head2 = Text("Now let it run", font=FONT, font_size=T_SUB,
                     color=CHALK).to_edge(UP, buff=0.6)
        self.play(FadeIn(head2), run_time=0.5)

        levels = 6
        dx, dy = 1.62, 0.50
        nodes = {}
        pts = VGroup()
        edges = VGroup()
        for t in range(levels + 1):
            for k in range(t + 1):
                x = -5.1 + t * dx
                y = (t - 2 * k) * dy + 0.35
                nodes[(t, k)] = np.array([x, y, 0])
        for t in range(levels):
            for k in range(t + 1):
                for kk in (k, k + 1):
                    edges.add(Line(nodes[(t, k)], nodes[(t + 1, kk)],
                                   color=MUTED, stroke_width=2))
        for key, p in nodes.items():
            pts.add(Dot(p, radius=0.055, color=MUTED))

        with self.narrate("Do that again the next year, and the next. Every point "
                          "splits in two, and the possibilities fan out."):
            self.play(Create(edges), run_time=2.6)
            self.play(FadeIn(pts), run_time=0.8)
        self.beat()

        with self.narrate("Watch one possible path through it. That is one future — "
                          "one thing that might happen."):
            path = VMobject(color=MONEY, stroke_width=5)
            rng = np.random.default_rng(7)
            k = 0
            seq = [nodes[(0, 0)]]
            for t in range(levels):
                k += int(rng.random() < 0.5)
                seq.append(nodes[(t + 1, k)])
            path.set_points_as_corners(seq)
            self.play(Create(path), run_time=2.2)
        self.beat()

        with self.narrate("And here are a dozen more. Nobody knows which one happens. "
                          "All anybody knows is the shape of the fan."):
            more = VGroup()
            for s in range(12):
                rng = np.random.default_rng(s + 20)
                k = 0
                seq = [nodes[(0, 0)]]
                for t in range(levels):
                    k += int(rng.random() < 0.5)
                    seq.append(nodes[(t + 1, k)])
                m = VMobject(color=WAIT, stroke_width=2.5)
                m.set_points_as_corners(seq)
                more.add(m)
            self.play(LaggedStart(*[Create(m) for m in more], lag_ratio=0.12),
                      run_time=3.0)
        self.beat()

        self.define("a random walk", "Each step is up or down by a fixed percentage, "
                    "and you cannot tell which.", "fog", WAIT, at=DOWN * 2.4, hold=4.4)
        self.clear_stage()

        # ------------------------------------------------ sigma
        head3 = Text("And one number describes the whole fan",
                     font=FONT, font_size=T_SUB, color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head3), run_time=0.5)

        axes = Axes(x_range=[-3, 3, 1], y_range=[0, 1.2, 1], x_length=8.4, y_length=2.6,
                    axis_config={"color": MUTED, "stroke_width": 2,
                                 "include_ticks": False, "include_tip": False})
        axes.shift(DOWN * 0.6)
        narrow = axes.plot(lambda x: np.exp(-x * x / (2 * 0.35 ** 2)),
                           color=MONEY, stroke_width=4)
        wide = axes.plot(lambda x: np.exp(-x * x / (2 * 1.0 ** 2)),
                         color=COST, stroke_width=4)
        nl = Text("a calm trade — 10% a year", font=FONT, font_size=T_SMALL, color=MONEY)
        wl = Text("a rough trade — 40% a year", font=FONT, font_size=T_SMALL, color=COST)
        nl.next_to(axes, UP, buff=0.35).shift(LEFT * 3.0)
        wl.next_to(axes, UP, buff=0.35).shift(RIGHT * 3.0)

        self.play(Create(axes), run_time=0.8)
        with self.narrate("Take a typical year and ask: how far did revenue move? In a "
                          "calm trade, not far. The outcomes bunch up."):
            self.play(Create(narrow), FadeIn(nl), run_time=1.4)
        with self.narrate("In a rough trade — oil, metals — they spread right out."):
            self.play(Create(wide), FadeIn(wl), run_time=1.4)
        self.beat()

        with self.narrate("The width of that spread is the number the paper calls the "
                          "choppiness. It is the size of a typical yearly swing, "
                          "written as a percentage. Ten per cent for revenue that moves "
                          "with exchange rates. Twenty-five to forty for an oil well or "
                          "a copper mine. And the paper's base case sits between, at "
                          "twenty."):
            br = BraceBetweenPoints(axes.c2p(-1, 0.62), axes.c2p(1, 0.62),
                                    direction=UP, color=CHALK)
            bt = Text("the choppiness", font=FONT, font_size=T_SMALL, color=CHALK)
            bt.next_to(br, UP, buff=0.15)
            self.play(FadeIn(br), FadeIn(bt), run_time=1.2)
        self.beat()

        note = cards.note("The paper writes it as a Greek letter. This film never does "
                          "— it is just “the choppiness”, and it is a percentage.",
                          width=62)
        note.to_edge(DOWN, buff=0.5)
        with self.narrate("The paper writes it as a Greek letter. This film never will. "
                          "It is the choppiness, and it is a percentage."):
            self.play(FadeIn(note), run_time=0.9)
        self.beat()

        self.close_chapter([
            "each year revenue goes up or down by a fixed percentage",
            "run that forward and the possibilities fan out",
            "nobody knows the path — only the shape of the fan",
            "the width of the fan is the choppiness: 10% calm, 40% rough, 20% base case",
        ])
