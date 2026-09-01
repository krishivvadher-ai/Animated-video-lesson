import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.scale import MasterScale
from lib.theme import *


class Chapter36(Chapter):
    CH = 36
    TITLE = "The instrument that fights itself"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["money", "clock", "scale", "risk"]

    def body(self):
        nell = stick.nell(scale=0.85).move_to(LEFT * 5.2 + DOWN * 1.6)
        self.play(FadeIn(nell), run_time=0.5)

        a = cards.body("Cheap money is meant to make BUILDING attractive.",
                       size=T_SUB, color=MONEY, width=26)
        a.move_to(LEFT * 2.4 + UP * 1.9)
        b = cards.body("But cheap money also makes WAITING cheaper.",
                       size=T_SUB, color=WAIT, width=26)
        b.move_to(RIGHT * 3.0 + UP * 1.9)
        with self.narrate("Cheap money is meant to make building attractive."):
            self.play(FadeIn(a), run_time=0.8)
        with self.narrate("But cheap money also makes waiting cheaper."):
            self.play(FadeIn(b), run_time=0.8)
        self.beat()

        why = cards.body("holding off costs the forgone return",
                         size=T_BODY, color=CHALK, width=44)
        why.move_to(RIGHT * 0.4 + UP * 0.2)
        with self.narrate("Because the cost of holding off for a year is the return the "
                          "money would have earned meanwhile. Make that return small, "
                          "and holding off hurts less."):
            self.play(FadeIn(why), nell.mood("thinking"), run_time=1.1)
        self.beat()
        self.play(FadeOut(why), run_time=0.4)

        # ------------------------------------------------- the two figures again
        sc = MasterScale(x=-1.4, y=-1.0, height=3.4, lo=0.0, hi=3.2)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), run_time=0.7)
        base = sc.add_level("M", 1.0, "break-even", COST, width=2.2)
        h1 = sc.add_level("H1", 1.86, "1.86 × at a 5% cost of capital", TRIGGER,
                          width=2.2, sw=5)
        self.play(Create(base[0]), FadeIn(base[1]), run_time=0.6)
        with self.narrate("Dixit's own figures, on one scale. At a five per cent cost "
                          "of capital, the multiplier is one point eight six."):
            self.play(Create(h1[0]), FadeIn(h1[1]), run_time=0.9)
        h2 = sc.add_level("H2", 2.61, "2.61 × at 2%", TRIGGER, width=2.2, sw=5)
        with self.narrate("At two per cent, it is two point six one."):
            self.play(Create(h2[0]), FadeIn(h2[1]), run_time=0.9)
        self.beat()

        # ------------------------------------------------- two arrows at once
        bar = Rectangle(width=1.0, height=1.6, color=COST, stroke_width=3,
                        fill_color=COST, fill_opacity=0.22)
        bar.move_to(RIGHT * 4.6 + DOWN * 1.0)
        cap = Rectangle(width=1.0, height=1.1, color=TRIGGER, stroke_width=3,
                        fill_color=TRIGGER, fill_opacity=0.22)
        cap.next_to(bar, UP, buff=0)
        bl = Text("break-even", font=FONT, font_size=T_SMALL, color=COST)
        bl.next_to(bar, DOWN, buff=0.2)
        cl = Text("the mark-up\nwaiting adds", font=FONT, font_size=T_SMALL,
                  color=TRIGGER, line_spacing=0.9)
        cl.next_to(cap, RIGHT, buff=0.25)
        with self.narrate("Think of a firm's bar as two pieces. The break-even level, "
                          "and the mark-up that waiting adds on top of it."):
            self.play(FadeIn(bar), FadeIn(bl), run_time=0.7)
            self.play(FadeIn(cap), FadeIn(cl), run_time=0.7)

        down = Arrow(bar.get_left() + LEFT * 1.4 + UP * 0.9,
                     bar.get_left() + LEFT * 0.15, color=MONEY, buff=0, stroke_width=6)
        up = Arrow(cap.get_right() + RIGHT * 1.4 + DOWN * 0.4,
                   cap.get_right() + RIGHT * 0.15, color=TRIGGER, buff=0, stroke_width=6)
        with self.narrate("The policy pushes the bottom piece down."):
            self.play(Create(down), bar.animate.stretch_to_fit_height(1.15).move_to(
                bar.get_center() + DOWN * 0.22), run_time=1.4)
        with self.narrate("And at the same time it fattens the piece on top."):
            self.play(Create(up), cap.animate.stretch_to_fit_height(1.7).next_to(bar, UP, buff=0),
                      run_time=1.4)
        self.beat()

        # ------------------------------------------------- the honest size
        self.clear_stage()
        kit = stick.kit(scale=0.8).move_to(LEFT * 5.4 + DOWN * 1.8)
        self.play(FadeIn(kit), run_time=0.5)
        head = cards.section_title("Now be honest about the size of this", color=SRC_KIT, size=T_SUB)
        self.play(FadeIn(head), run_time=0.5)

        dirn = cards.body("The direction is not in doubt. The bar does come down.",
                          size=T_SUB, color=CHALK, width=40)
        dirn.move_to(UP * 1.7)
        with self.narrate("The direction is not in doubt. The bar does come down. The "
                          "first effect wins."):
            self.play(FadeIn(dirn), run_time=0.9)
        self.beat()

        want = cards.body("“it comes down by LESS than you expect”", size=T_BODY, color=SRC_KIT, width=42)
        want.move_to(UP * 0.4)
        with self.narrate("What Kit originally wanted to say was sharper. That it comes "
                          "down by less than you would expect."):
            self.play(FadeIn(want), kit.mood("pleased"), run_time=0.9)

        col1 = cards.body("percentage points:\nfalls by MORE", size=T_BODY, color=MONEY, width=22)
        col2 = cards.body("As proportions:\nit falls by LESS.",
                          size=T_BODY, color=COST, width=22)
        cols = VGroup(col1, col2).arrange(RIGHT, buff=1.8).move_to(DOWN * 1.2)
        with self.narrate("He has withdrawn it. Because whether that is true depends "
                          "entirely on how you measure it. Compare the two figures as "
                          "percentage points, and the bar falls by more than the cost "
                          "of money does."):
            self.play(FadeIn(col1), run_time=0.9)
        with self.narrate("Compare them as proportions, and it falls by less."):
            self.play(FadeIn(col2), kit.mood("worried"), run_time=0.9)
        both = cards.body("Both sums are correct. Neither is the true one.",
                          size=T_SUB, color=CHALK, width=40)
        both.next_to(cols, DOWN, buff=0.6)
        with self.narrate("Both sums are correct. Neither of them is the true one. So "
                          "he declines to pick."):
            self.play(FadeIn(both), run_time=0.9)
        self.beat()

        cross = Line(want.get_left() + LEFT * 0.2, want.get_right() + RIGHT * 0.2,
                     color=COST, stroke_width=5)
        self.play(Create(cross), run_time=0.9)
        self.beat()

        self.clear_stage()
        claim = cards.body("Part of the policy is spent making patience attractive.",
                           size=T_HEAD, color=CHALK, width=32)
        with self.narrate("The claim he is entitled to is the plain one. Part of the "
                          "policy is spent making patience more attractive."):
            self.play(Write(claim), run_time=2.6)
        self.beat()

        self.close_chapter([
            "cheap money: builds AND waits",
            "1.86 at 5%  ·  2.61 at 2%",
            "withdrawn: “by less than you expect”",
            "surviving claim: patience gets cheaper",
        ])
