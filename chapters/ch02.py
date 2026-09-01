import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.scale import MasterScale
from lib.theme import *


class Chapter02(Chapter):
    CH = 2
    TITLE = "The textbook rule"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ['flow', 'slab', 'scale', 'money']

    def body(self):
        m = stick.marshall(scale=1.15).shift(LEFT * 4.6 + DOWN * 0.4)
        ml = m.label()
        with self.narrate("Marshall has a rule. It is the rule in every textbook, and "
                          "it is worth stating fairly, because for most of the last "
                          "century it was simply what everybody believed."):
            self.play(FadeIn(m), FadeIn(ml), run_time=0.9)
            self.play(m.nod(), run_time=0.8)

        # ---------------------------------------------- average variable cost
        with self.narrate("Before the rule, two more costs. Both are averages — a "
                          "total, shared out over every unit she makes."):
            pass

        bar1 = W.stacked_cost_bar(
            [(1.3, SUNK, "average variable cost\nper chair")], x=0.4, base_y=-2.0)
        with self.narrate("Take everything she spends that moves with output — the "
                          "wood, the power, the wages — and divide it by the number of "
                          "chairs. That is her average variable cost."):
            self.play(GrowFromEdge(bar1[0][0], DOWN), FadeIn(bar1[0][1]), run_time=1.4)
        self.define("average variable cost", "What each extra chair costs her to make.",
                    "flow", SUNK, at=RIGHT * 3.6 + UP * 1.6, hold=3.0)

        bar2 = W.stacked_cost_bar(
            [(1.3, SUNK, ""), (0.9, COST, "share of the building")],
            x=0.4, base_y=-2.0)
        with self.narrate("Now add a share of the cost of the building itself — the "
                          "factory that had to be paid for before a single chair was "
                          "made. Put those together and you have her long-run average "
                          "cost."):
            self.play(GrowFromEdge(bar2[1][0], DOWN), FadeIn(bar2[1][1]), run_time=1.4)
        self.define("long-run average cost", "Everything a chair costs her, including "
                    "a share of the building.", "slab", COST,
                    at=RIGHT * 3.6 + UP * 1.6, hold=3.0)

        with self.narrate("And now Marshall's rule, in two halves."):
            self.play(FadeOut(bar1), FadeOut(bar2), run_time=0.6)

        # ---------------------------------------------- the master scale
        self.play(m.animate.scale(0.78).move_to(LEFT * 5.5 + UP * 1.7), run_time=0.7)
        sc = MasterScale(x=-2.2, y=-0.3, height=4.6)
        with self.narrate("This is the most important picture in the film, so we build "
                          "it slowly. One line, running up the screen. Low down means "
                          "money coming in each month is poor. High up means it is good."):
            self.play(Create(sc.axis), FadeIn(sc.arrow_head), run_time=1.4)
            self.play(FadeIn(sc.title), run_time=0.7)
        self.beat()

        build = sc.add_level("M", 1.10, "BUILD above here", COST, number=None)
        with self.narrate("Marshall's first half. If the money coming in clears the "
                          "long-run average cost — everything, including the building "
                          "— then build. Expand. Enter the trade."):
            self.play(Create(build[0]), FadeIn(build[1]), run_time=1.2)

        quit_ = sc.add_level("C", 1.00, "SHUT DOWN below here", SUNK)
        with self.narrate("Marshall's second half. If the money coming in drops below "
                          "the average variable cost — if a chair no longer covers even "
                          "the wood and the wages — then stop. Shut down, or leave."):
            self.play(Create(quit_[0]), FadeIn(quit_[1]), run_time=1.2)

        band = sc.band(1.00, 1.10, MUTED, 0.30)
        brace = sc.brace_between(1.00, 1.10, "do nothing", MUTED)
        with self.narrate("Notice how close together those two lines are. Between them "
                          "there is a small band where the right thing to do is nothing "
                          "at all. Hold that thought. That band is going to get very "
                          "much wider."):
            self.play(FadeIn(band), run_time=0.8)
            self.play(FadeIn(brace), run_time=0.8)
        self.beat()

        self.play(FadeOut(band), FadeOut(brace), FadeOut(m), FadeOut(ml), run_time=0.6)
        self.play(sc.animate.scale(0.68).to_edge(LEFT, buff=0.7).shift(UP * 0.2),
                  run_time=0.9)

        # ---------------------------------------------- cost of capital
        with self.narrate("One definition left, and it is the single most important "
                          "one in this film. Take your time over it."):
            pass

        nell = stick.nell(scale=0.95).shift(RIGHT * 2.4 + DOWN * 1.4)
        bag = W.money_bag(SUNK, 1.1).shift(RIGHT * 2.4 + UP * 1.7)
        with self.narrate("Nell needs a large sum to build. It comes from one of two "
                          "places, and usually both."):
            self.play(FadeIn(nell), FadeIn(bag), run_time=0.9)

        a = cards.body("borrowed → she must pay extra",
                       size=T_BODY, color=CHALK, width=30)
        b = cards.body("her own → could be elsewhere", size=T_BODY, color=CHALK, width=30)
        col = VGroup(a, b).arrange(DOWN, buff=0.7, aligned_edge=LEFT)
        col.next_to(bag, RIGHT, buff=0.6).shift(DOWN * 0.4)
        if col.width > 6.0:
            col.scale(6.0 / col.width)

        with self.narrate("She borrows it, and then she has to pay extra for the use of it."):
            self.play(FadeIn(a, shift=RIGHT * 0.2), run_time=0.7)
        with self.narrate("Or it is her own money, and by putting it into this factory "
                          "she gives up whatever else she could have done with it."):
            self.play(FadeIn(b, shift=RIGHT * 0.2), run_time=0.7)

        with self.narrate("Either way, the money has a price. Blend the two together "
                          "and you get one number."):
            self.play(FadeOut(col), run_time=0.5)

        self.define("cost of capital", "What the money must earn to be worth using.", "money", WAIT,
                    narration="The cost of capital. The yearly percentage the money "
                              "she uses has to earn, just to be worth using at all.",
                    at=RIGHT * 2.6 + UP * 0.4, hold=5.0)

        with self.narrate("Earn less than that, and she would have done better leaving "
                          "the money where it was. That is the whole idea, and every "
                          "number later in the film is measured against it."):
            self.play(nell.nod(), run_time=0.9)
        self.beat()

        self.close_chapter([
            "AVC: what one more chair costs",
            "LRAC: plus a share of the building",
            "build above LRAC · shut below AVC",
            "cost of capital: what money must earn",
        ])
