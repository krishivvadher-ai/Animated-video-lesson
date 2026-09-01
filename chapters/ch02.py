import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.scale import MasterScale
from lib.theme import *


class Chapter02(Chapter):
    CH = 2
    TITLE = "The textbook rule"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["flow", "slab", "scale", "money"]

    def body(self):
        # ------------------------------------------------ two averages
        self.heading("What a chair costs her")
        marshall = stick.marshall(scale=0.95)
        St.place(marshall, St.STAGE, ax=-0.78, ay=-0.15)
        with self.narrate("Marshall has a rule. It is the rule in every textbook, and "
                          "it is worth stating fairly, because for most of the last "
                          "century it was simply what everybody believed."):
            self.play(FadeIn(marshall), FadeIn(marshall.label()), run_time=0.9)
            self.play(marshall.nod(), run_time=0.8)

        bar_v = Rectangle(width=1.5, height=1.7, color=SUNK, stroke_width=3,
                          fill_color=SUNK, fill_opacity=0.28)
        bar_f = Rectangle(width=1.5, height=1.1, color=COST, stroke_width=3,
                          fill_color=COST, fill_opacity=0.28)
        stack = VGroup(bar_f, bar_v).arrange(UP, buff=0)
        St.place(stack, St.STAGE, ax=0.25, ay=-0.05)
        lab_v = Text("wood, power, wages", font=FONT, font_size=T_SMALL, color=SUNK)
        lab_v.next_to(bar_v, RIGHT, buff=0.3)
        lab_f = Text("a share of the building", font=FONT, font_size=T_SMALL, color=COST)
        lab_f.next_to(bar_f, RIGHT, buff=0.3)

        bar_v.save_state(); bar_v.stretch(0.0001, 1, about_edge=DOWN)
        bar_f.save_state(); bar_f.stretch(0.0001, 1, about_edge=DOWN)

        with self.narrate("Take everything she spends that moves with output — the "
                          "wood, the power, the wages — and divide it by the number of "
                          "chairs she makes."):
            self.play(Restore(bar_v), run_time=1.2)
            self.play(FadeIn(lab_v), run_time=0.5)
        self.define("average variable cost", "What each extra chair costs her to make.",
                    "flow", SUNK, at=DOWN * 2.3, hold=3.4)

        with self.narrate("Now add a share of the cost of the building itself — the "
                          "factory that had to be paid for before a single chair was "
                          "made."):
            self.play(Restore(bar_f), run_time=1.2)
            self.play(FadeIn(lab_f), run_time=0.5)
        self.define("long-run average cost", "Everything a chair costs, the building "
                    "included.", "slab", COST, at=DOWN * 2.3, hold=3.4)
        self.clear_stage()

        # ------------------------------------------------ the master scale
        self.heading("The master scale")
        sc = MasterScale(x=-1.6, y=-0.55, height=4.3)
        with self.narrate("This is the most important picture in the film, so we build "
                          "it slowly. One line, running up the screen. Low down, the "
                          "money coming in each month is poor. High up, it is good."):
            self.play(Create(sc.axis), FadeIn(sc.arrow_head), run_time=1.2)
            self.play(FadeIn(sc.title), run_time=0.6)
        self.beat()

        build = sc.add_level("M", 1.10, "BUILD above", COST, width=3.0)

        with self.narrate("Marshall's first half. If the money coming in clears the "
                          "long-run average cost, then build. Expand. Enter the trade."):
            self.play(Create(build[0]), FadeIn(build[1]), run_time=1.1)

        quit_ = sc.add_level("C", 1.00, "SHUT DOWN below", SUNK, width=3.0)

        with self.narrate("Marshall's second half. If the money coming in drops below "
                          "the average variable cost — if a chair no longer covers even "
                          "the wood and the wages — then stop."):
            self.play(Create(quit_[0]), FadeIn(quit_[1]), run_time=1.1)

        band = sc.band(1.00, 1.10, MUTED, 0.35, width=3.0)
        brace = sc.brace_between(1.00, 1.10, "do nothing", MUTED)
        with self.narrate("Notice how close together those two lines are. Between them "
                          "is a narrow band where the right thing to do is nothing at "
                          "all. Hold that thought. It is going to get very much wider."):
            self.play(FadeIn(band), run_time=0.7)
            self.play(FadeIn(brace), run_time=0.8)
        self.beat()
        self.play(FadeOut(band), FadeOut(brace), run_time=0.5)
        self.play(FadeOut(sc), run_time=0.6)

        # ------------------------------------------------ cost of capital
        self.heading("What her money costs her")
        nell = stick.nell(scale=0.95)
        St.place(nell, St.STAGE, ax=-0.2, ay=-0.4)
        bag = W.money_bag(SUNK, 1.1)
        St.place(bag, St.STAGE, ax=0.55, ay=0.35)
        with self.narrate("One definition left, and it is the single most important one "
                          "in this film. Nell needs a large sum to build. It comes from "
                          "one of two places, and usually both."):
            self.play(FadeIn(nell), FadeIn(bag), run_time=1.0)

        self.side(["borrowed → she pays extra", "her own → could be elsewhere"],
                  colour=CHALK, dot_colour=WAIT,
                  spoken=["She borrows it, and then she has to pay extra for the use "
                          "of it.",
                          "Or it is her own money, and by putting it into this factory "
                          "she gives up whatever else she could have done with it."])
        with self.narrate("Either way, the money has a price. Blend the two together "
                          "and you get one number."):
            self.play(S.pulse(bag, SUNK), run_time=1.2)

        self.define("cost of capital", "The yearly percentage her money must earn to be "
                    "worth using.", "money", WAIT, at=DOWN * 2.2, hold=5.0)
        with self.narrate("Earn less than that, and she would have done better leaving "
                          "the money where it was. Every number later in this film is "
                          "measured against it."):
            self.play(nell.nod(), run_time=0.9)
        self.beat()

        self.close_chapter([
            "AVC: what one more chair costs",
            "LRAC: plus a share of the building",
            "build above LRAC · shut below AVC",
            "cost of capital: what money must earn",
        ])
