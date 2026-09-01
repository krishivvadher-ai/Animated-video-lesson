import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.scale import MasterScale
from lib.theme import *


class Chapter22(Chapter):
    CH = 22
    TITLE = "The zone of inaction"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["scale", "fog", "slab", "people"]

    def body(self):
        # ------------------------------------------------ narrow, then wide
        self.heading("A narrow band, and a wide one")
        sc = MasterScale(x=-3.2, y=-0.45, height=4.8)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), FadeIn(sc.title), run_time=1.0)
        c = sc.add_level("C", 1.00, "1.00", SUNK, width=2.6, sw=3)
        m = sc.add_level("M", 1.10, "1.10", COST, width=2.6, sw=3)
        with self.narrate("Take away the uncertainty for a moment, and leave only the "
                          "sunk cost. The textbook still has a small band where doing "
                          "nothing is right — from one, to one point one."):
            self.play(Create(c[0]), FadeIn(c[1]), Create(m[0]), FadeIn(m[1]),
                      run_time=1.3)
        narrow = sc.band(1.00, 1.10, MUTED, 0.5, width=2.6)
        nb = sc.brace_between(1.00, 1.10, "0.10 wide", MUTED)
        with self.narrate("That is the whole of it. A band nought point one wide."):
            self.play(FadeIn(narrow), FadeIn(nb), run_time=1.0)
        self.beat()

        l = sc.add_level("L", 0.72, "0.72", TRIGGER, width=2.6, sw=5)
        h = sc.add_level("H", 1.62, "1.62", TRIGGER, width=2.6, sw=5)
        with self.narrate("Now put the uncertainty back in."):
            self.play(Create(l[0]), FadeIn(l[1]), Create(h[0]), FadeIn(h[1]),
                      run_time=1.5)
        wide = sc.band(0.72, 1.62, TRIGGER, 0.16, width=2.6)
        wb = sc.brace_between(0.72, 1.62, "0.90 wide", TRIGGER)
        with self.narrate("Nought point seven two, to one point six two. Nought point "
                          "nine wide."):
            self.play(FadeOut(nb), FadeIn(wide), FadeIn(wb), run_time=1.2)
        self.beat()

        nine = St.caption("about nine times wider", TRIGGER, T_SUB, width=18)
        St.place(nine, St.SIDE, ay=0.6)
        deriv = St.caption("0.90 ÷ 0.10 — ours, not the paper's", MUTED, T_SMALL,
                           width=22)
        St.place(deriv, St.SIDE, ay=0.1)
        with self.narrate("About nine times wider. That comparison is ours, not the "
                          "paper's — the paper prints the four levels and calls the "
                          "difference quite a dramatic difference. We did the division."):
            self.play(FadeIn(nine), run_time=0.8)
            self.play(FadeIn(deriv), run_time=0.7)
        self.beat()
        name = St.caption("where doing nothing is right", CHALK, T_BODY, width=20)
        St.place(name, St.SIDE, ay=-0.45)
        with self.narrate("This band has a name. The zone of inaction. The stretch "
                          "where the right thing to do is nothing at all."):
            self.play(FadeIn(name), run_time=0.8)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ consequences
        self.heading("Two consequences the paper draws")
        one = St.caption("small frictions → large rigidities", CHALK, T_SUB, width=34)
        St.place(one, St.FULL, ay=0.6)
        with self.narrate("First. Small frictions can produce much larger rigidities "
                          "than models which ignore gradually-arriving information "
                          "would ever suggest. A little stickiness goes a very long way."):
            self.play(FadeIn(one), run_time=1.0)
        self.beat()
        self.play(FadeOut(one), run_time=0.4)

        boss = stick.StickFigure("an employer", CHALK, hat="specs", scale=0.85)
        St.place(boss, St.STAGE, ax=-0.75, ay=-0.15)
        workers = stick.crowd(4, spacing=1.5, scale=0.5)
        St.place(workers, St.STAGE, ax=0.35, ay=-0.15)
        with self.narrate("Second, and this one reaches outside the firm altogether. "
                          "Hiring and firing cost money. So exactly the same logic "
                          "applies to jobs."):
            self.play(FadeIn(boss), S.lag_map(FadeIn, workers, lag=0.2),
                      run_time=1.4)
        self.side(["employers hoard labour in downturns",
                   "and are slow to hire in upturns",
                   "so a worker can sit above the wage — or below it"],
                  colour=CHALK, dot_colour=WAIT, width=20,
                  spoken=["Employers hoard labour in downturns.",
                          "And they are slow to hire in upturns.",
                          "So what a worker adds to the business can sit well above "
                          "the wage without anybody being hired — and well below it "
                          "without anybody being let go."])
        self.play(*[w.mood("worried") for w in workers], run_time=0.5)
        self.beat()
        with self.narrate("And the paper draws a conclusion from that which is worth "
                          "hearing. The popular worry about loss of jobs — the one "
                          "economists usually wave away — may have more justification "
                          "than the textbook allows."):
            self.foot("“loss of jobs” may be better founded than we allow", CHALK)
        self.beat()

        self.close_chapter([
            "sunk costs alone: 1.00 – 1.10",
            "with uncertainty: 0.72 – 1.62",
            "small frictions → large rigidities",
            "and the same logic applies to jobs",
        ])
