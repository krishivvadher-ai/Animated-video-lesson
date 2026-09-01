import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter42(Chapter):
    CH = 42
    TITLE = "The instrument that fights itself"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["scale", "clock", "money", "risk"]

    def body(self):
        # ------------------------------------------------ two arrows, one bar
        self.heading("Cheap money pulls two ways")
        build = VGroup(cards.icon("slab", MONEY, 1.6),
                       St.caption("building looks\nmore attractive", MONEY,
                                  T_SMALL, width=18)).arrange(DOWN, buff=0.28)
        wait_ = VGroup(cards.icon("clock", WAIT, 1.6),
                       St.caption("waiting also gets\ncheaper", WAIT,
                                  T_SMALL, width=18)).arrange(DOWN, buff=0.28)
        two = VGroup(build, wait_).arrange(RIGHT, buff=2.8)
        St.place(two, St.FULL, ay=0.4)
        with self.narrate("Cheap money is meant to make building attractive."):
            self.play(FadeIn(build), run_time=0.9)
        with self.narrate("But cheap money also makes waiting cheaper."):
            self.play(FadeIn(wait_), run_time=0.9)

        why = St.caption("holding off costs the return\nthe money would have earned",
                         MUTED, T_BODY, width=32)
        St.place(why, St.FULL, ay=-0.75)
        with self.narrate("Because the cost of holding off for a year is the return the "
                          "money would have earned meanwhile. Make that return small, "
                          "and holding off hurts less."):
            self.play(FadeIn(why), run_time=1.0)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ Dixit's own figures
        self.heading("Dixit's own figures, on one scale")
        b1 = W.Bar(1.86, color=TRIGGER, width=1.1)
        b2 = W.Bar(2.61, color=COST, width=1.1)
        pair = VGroup(b1, b2).arrange(RIGHT, buff=2.4, aligned_edge=DOWN)
        St.place(pair, St.STAGE, ay=-0.25)
        base = Line(pair.get_left() + LEFT * 0.5, pair.get_right() + RIGHT * 0.5,
                    color=MUTED, stroke_width=2).move_to(pair.get_bottom())
        l1 = VGroup(Text("1.86", font=FONT, font_size=T_BODY, color=TRIGGER),
                    St.caption("money at 5%", MUTED, T_SMALL, width=14)
                    ).arrange(DOWN, buff=0.14)
        l1.next_to(b1, DOWN, buff=0.22)
        l2 = VGroup(Text("2.61", font=FONT, font_size=T_BODY, color=COST),
                    St.caption("money at 2%", MUTED, T_SMALL, width=14)
                    ).arrange(DOWN, buff=0.14)
        l2.next_to(b2, DOWN, buff=0.22)
        St.collapse_bars(pair)
        self.play(Create(base), run_time=0.5)
        with self.narrate("At a five per cent cost of capital, the multiplier is one "
                          "point eight six."):
            self.play(Restore(b1), FadeIn(l1), run_time=1.1)
        with self.narrate("At two per cent, it is two point six one."):
            self.play(Restore(b2), FadeIn(l2), run_time=1.3)
            self.play(S.flash_around(b2, COST))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the bar in two pieces
        self.heading("So split the bar into two pieces")
        parts = W.stacked_cost_bar([(1.2, WAIT, "break-even"),
                                    (1.3, TRIGGER, "what waiting adds")],
                                   x=-1.6, width=1.3, base_y=-1.6)
        St.place(parts, St.STAGE, ay=-0.1)
        with self.narrate("Think of a firm's bar as two pieces. The break-even level, "
                          "and the mark-up that waiting adds on top of it."):
            self.play(FadeIn(parts), run_time=1.2)

        down = Arrow(UP * 0.5, DOWN * 0.5, color=MONEY, buff=0, stroke_width=7,
                     max_tip_length_to_length_ratio=0.4)
        down.next_to(parts[0], LEFT, buff=0.5)
        with self.narrate("The policy pushes the bottom piece down."):
            self.play(GrowArrow(down), run_time=0.7)
            self.play(parts[0][0].animate.stretch_to_fit_height(0.8).align_to(
                parts[0][0], DOWN), run_time=1.1)

        up = Arrow(DOWN * 0.5, UP * 0.5, color=COST, buff=0, stroke_width=7,
                   max_tip_length_to_length_ratio=0.4)
        up.next_to(parts[1], RIGHT, buff=1.6)
        with self.narrate("And at the same time it fattens the piece on top."):
            self.play(GrowArrow(up), run_time=0.7)
            self.play(parts[1][0].animate.stretch_to_fit_height(1.9).align_to(
                parts[1][0], DOWN), run_time=1.1)
        self.beat()

        honest = St.caption("the bar does come down — the first effect wins",
                            MONEY, T_SUB, width=44)
        St.place(honest, St.FOOT, pad=0.06)
        with self.narrate("The direction is not in doubt. The bar does come down. The "
                          "first effect wins."):
            self.play(FadeIn(honest), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the withdrawn claim
        self.heading("And a claim Kit has withdrawn")
        kit = stick.kit(scale=0.85)
        St.place(kit, St.STAGE, ax=-0.75, ay=-0.4)
        sharper = St.caption("it comes down by less\nthan you would expect",
                             SRC_KIT, T_SUB, width=22)
        St.place(sharper, St.SIDE, ay=0.6)
        with self.narrate("What Kit originally wanted to say was sharper. That it comes "
                          "down by less than you would expect.", v="c"):
            self.play(FadeIn(kit), run_time=0.6)
            self.play(FadeIn(sharper), run_time=0.8)
        with self.narrate("He has withdrawn it. Because whether that is true depends "
                          "entirely on how you measure it.", v="c"):
            strike = Line(sharper.get_left(), sharper.get_right(), color=COST,
                          stroke_width=5)
            self.play(Create(strike), run_time=0.9)
            self.play(kit.mood("worried"), run_time=0.4)

        m1 = VGroup(Text("in points", font=FONT, font_size=T_SMALL,
                         color=MONEY),
                    Text("falls by more", font=FONT, font_size=T_BODY, color=MONEY)
                    ).arrange(DOWN, buff=0.16)
        m2 = VGroup(Text("as proportions", font=FONT, font_size=T_SMALL,
                         color=COST),
                    Text("falls by less", font=FONT, font_size=T_BODY, color=COST)
                    ).arrange(DOWN, buff=0.16)
        both = VGroup(m1, m2).arrange(DOWN, buff=0.45)
        St.place(both, St.SIDE, ay=-0.45)
        with self.narrate("Compare the two figures as percentage points, and the bar "
                          "falls by more than the cost of money does."):
            self.play(FadeIn(m1), run_time=0.8)
        with self.narrate("Compare them as proportions, and it falls by less."):
            self.play(FadeIn(m2), run_time=0.8)
        with self.narrate("Both sums are correct. Neither of them is the true one. So "
                          "he declines to pick.", v="c"):
            self.play(kit.shrug(), run_time=1.0)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ what survives
        self.drop_heading()
        claim = St.caption("part of the policy is spent\nmaking patience more attractive",
                           CHALK, T_HEAD, width=34)
        St.place(claim, St.WIDE, ay=0.2)
        with self.narrate("The claim he is entitled to is the plain one. Part of the "
                          "policy is spent making patience more attractive."):
            self.play(Write(claim), run_time=2.8)
        self.wait(1.8)
        self.beat()

        self.close_chapter([
            "cheap money makes building and waiting both cheaper",
            "1.86 at 5% · 2.61 at 2% — Dixit's own figures",
            "the bar does fall: the first effect wins",
            "but part of the policy is spent on patience",
        ])
