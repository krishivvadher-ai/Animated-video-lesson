import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.scale import MasterScale
from lib.theme import *


class Chapter16(Chapter):
    CH = 16
    TITLE = "The zone of inaction"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ['scale', 'fog', 'slab', 'people']

    def body(self):
        sc = MasterScale(x=-3.4, y=-0.3, height=5.0)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), FadeIn(sc.title), run_time=1.0)

        c = sc.add_level("C", 1.00, "1.00", SUNK, width=3.0, sw=3)
        m = sc.add_level("M", 1.10, "1.10", COST, width=3.0, sw=3)
        with self.narrate("Take away the uncertainty for a moment, and leave only the "
                          "sunk cost. The textbook still has a small band where doing "
                          "nothing is right — from one, to one point one."):
            self.play(Create(c[0]), FadeIn(c[1]), Create(m[0]), FadeIn(m[1]),
                      run_time=1.2)
        narrow = sc.band(1.00, 1.10, MUTED, 0.45, width=3.0)
        nb = sc.brace_between(1.00, 1.10, "0.10 wide", MUTED)
        with self.narrate("That is the whole of it. A band nought point one wide."):
            self.play(FadeIn(narrow), FadeIn(nb), run_time=1.0)
        self.beat()

        l = sc.add_level("L", 0.72, "0.72", TRIGGER, width=3.0, sw=5)
        h = sc.add_level("H", 1.62, "1.62", TRIGGER, width=3.0, sw=5)
        with self.narrate("Now put the uncertainty back in."):
            self.play(Create(l[0]), FadeIn(l[1]), Create(h[0]), FadeIn(h[1]),
                      run_time=1.4)
        wide = sc.band(0.72, 1.62, TRIGGER, 0.16, width=3.0)
        wb = sc.brace_between(0.72, 1.62, "0.90 wide", TRIGGER)
        with self.narrate("Nought point seven two, to one point six two. Nought point "
                          "nine wide."):
            self.play(FadeOut(nb), FadeIn(wide), FadeIn(wb), run_time=1.2)
        self.beat()

        nine = cards.body("About nine times wider.", size=T_SUB, color=TRIGGER, width=20)
        nine.move_to(RIGHT * 3.6 + UP * 1.6)
        deriv = cards.note("derived: 0.90 ÷ 0.10 — ours, not the paper's", width=30)
        deriv.next_to(nine, DOWN, buff=0.4)
        with self.narrate("About nine times wider. That comparison is ours, not the "
                          "paper's — the paper prints the four levels and calls the "
                          "difference quite a dramatic difference. We did the sum."):
            self.play(FadeIn(nine), run_time=0.7)
            self.play(FadeIn(deriv), run_time=0.8)
        self.beat()

        name = cards.body("where doing nothing is right", size=T_BODY, color=CHALK, width=26)
        name.move_to(RIGHT * 3.6 + DOWN * 1.6)
        with self.narrate("This band has a name. The zone of inaction. The stretch "
                          "where the right thing to do is nothing at all."):
            self.play(FadeIn(name), run_time=0.9)
        self.beat()

        self.clear_stage()

        # ------------------------------------------------ two consequences
        head = Text("Two consequences the paper draws", font=FONT,
                    font_size=T_SUB, color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)

        one = cards.body("small frictions → large rigidities",
                         size=T_BODY, color=CHALK, width=44)
        one.move_to(UP * 1.5)
        with self.narrate("First. Small frictions can produce much larger rigidities "
                          "than models which ignore gradually-arriving information "
                          "would ever suggest. A little stickiness goes a very long way."):
            self.play(FadeIn(one), run_time=1.0)
        self.beat()

        # ------------------------------------------------ labour
        self.play(FadeOut(one), run_time=0.4)
        boss = stick.StickFigure("an employer", CHALK, hat="specs", scale=0.85)
        boss.shift(LEFT * 4.4 + DOWN * 0.6)
        workers = stick.crowd(4, spacing=1.4, scale=0.5).shift(RIGHT * 1.6 + DOWN * 0.6)
        with self.narrate("Second, and this one reaches outside the firm altogether. "
                          "Hiring and firing cost money. So exactly the same logic "
                          "applies to jobs."):
            self.play(FadeIn(boss), FadeIn(workers), run_time=1.0)

        pts = cards.bullet_list([
            "Employers hoard labour in downturns.",
            "And are slow to hire in upturns.",
            "above the wage, no hiring · below it, no firing",
        ], color=CHALK, width=34)
        pts.move_to(DOWN * 2.0)
        if pts.height > 2.4:
            pts.scale(2.4 / pts.height)
        pts.to_edge(DOWN, buff=0.62)
        says = ["Employers hoard labour in downturns.",
                "And they are slow to hire in upturns.",
                "above the wage, no hiring · below it, no firing"]
        for i in range(3):
            with self.narrate(says[i]):
                self.play(FadeIn(pts[i], shift=RIGHT * 0.2), run_time=0.6)
                if i == 0:
                    self.play(*[w.mood("worried") for w in workers], run_time=0.4)
        self.beat()

        self.play(FadeOut(pts), FadeOut(boss), FadeOut(workers), run_time=0.5)
        pop = cards.body("“loss of jobs” — better founded than the textbook allows",
                         size=T_BODY, color=CHALK, width=42)
        pop.move_to(UP * 0.2)
        with self.narrate("And the paper draws a conclusion from that which is worth "
                          "hearing. The popular worry about loss of jobs — the one "
                          "economists usually wave away — may have more justification "
                          "than the textbook allows."):
            self.play(FadeIn(pop), run_time=1.1)
        self.beat()

        self.close_chapter([
            "sunk costs alone: 1.00 – 1.10",
            "with uncertainty: 0.72 – 1.62",
            "small frictions → large rigidities",
            "and the same logic applies to jobs",
        ])
