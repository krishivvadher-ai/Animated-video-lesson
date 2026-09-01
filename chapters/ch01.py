import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.theme import *


class Chapter01(Chapter):
    CH = 1
    TITLE = "What “investment” actually means"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ['money', 'flow', 'slab']

    def body(self):
        shop = W.Shop("Nell's factory")
        shop.scale(1.0).shift(UP * 0.4)
        nell = stick.nell(scale=0.85).next_to(shop, DOWN, buff=0.1).shift(LEFT * 2.6)

        with self.narrate("Start with the simplest picture there is. A factory. "
                          "Nell's factory."):
            self.play(FadeIn(shop.building), FadeIn(shop.caption), run_time=1.0)
            self.play(FadeIn(nell), run_time=0.6)

        inflow = shop.inflow("money coming in")
        with self.narrate("Every month, money comes in. Customers buy what she makes, "
                          "and they pay her."):
            self.play(Create(inflow[0]), FadeIn(inflow[1]), run_time=1.2)
        self.define("revenue", "All the money coming in, before anything is taken out.",
                    "money", MONEY,
                    narration="Economists call that money coming in her revenue. "
                              "Revenue is all the money coming in, before anything "
                              "is taken out of it.")

        outflow = shop.outflow("money going out")
        with self.narrate("Every month, money also goes out. She pays for materials, "
                          "for electricity, for wages, for the rent."):
            self.play(Create(outflow[0]), FadeIn(outflow[1]), run_time=1.2)
        self.define("cost", "All the money going out to keep the place running.",
                    "flow", COST,
                    narration="That is her cost. All the money going out to keep the "
                              "place running.")

        with self.narrate("The difference between the two is what she actually keeps."):
            g = VGroup(inflow, outflow, shop)
            self.play(g.animate.scale(0.8).shift(UP * 0.9), FadeOut(nell), run_time=1.0)
        self.define("profit", "Revenue minus cost. What is left over.", "money", MONEY,
                    narration="Her profit. Revenue minus cost. What is left over.",
                    at=DOWN * 1.9)

        self.clear_stage()

        # ------------------------------------------------ fixed vs variable
        head = Text("Two kinds of cost", font=FONT, font_size=T_HEAD, color=CHALK)
        head.to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.6)

        left = VGroup(
            Rectangle(width=2.6, height=1.5, color=COST, stroke_width=3),
            Text("the rent", font=FONT, font_size=T_BODY, color=COST))
        left[1].move_to(left[0])
        left.shift(LEFT * 3.4 + UP * 0.4)
        right = VGroup(
            Rectangle(width=2.6, height=1.5, color=SUNK, stroke_width=3),
            Text("the materials", font=FONT, font_size=T_BODY, color=SUNK))
        right[1].move_to(right[0])
        right.shift(RIGHT * 3.4 + UP * 0.4)

        with self.narrate("Not all costs behave the same way. The rent is the same "
                          "whether she makes one chair or a thousand."):
            self.play(FadeIn(left), run_time=0.8)
        self.define("fixed cost", "A cost that does not change with how much you make.",
                    "slab", COST, at=DOWN * 2.1, hold=3.2)

        with self.narrate("The wood is different. Make twice as many chairs and she "
                          "buys twice as much wood."):
            self.play(FadeIn(right), run_time=0.8)
        self.define("variable cost", "A cost that rises and falls with how much you make.",
                    "flow", SUNK, at=DOWN * 2.1, hold=3.2)

        self.clear_stage()

        # ------------------------------------------------ investment
        ava = stick.ava(scale=1.0).shift(LEFT * 4.4 + DOWN * 0.4)
        with self.narrate("Now the word this whole film turns on.", ):
            self.play(FadeIn(ava), run_time=0.6)
        q = ava.say("Investment? Isn't that\nbuying shares?", direction=UP, width=3.6)
        with self.narrate("You may think investment means buying shares in a company. "
                          "That is not what an economist means by it.", v="c"):
            self.play(FadeIn(q), ava.mood("thinking"), run_time=0.6)
        self.play(FadeOut(q), run_time=0.4)

        bag = W.money_bag(SUNK, 1.3).shift(RIGHT * 0.2 + UP * 0.9)
        fac = W.factory(CHALK, 0.85).shift(RIGHT * 4.2 + UP * 0.7)
        arr = W.flow_arrow(bag.get_right() + RIGHT * 0.2, fac.get_left() + LEFT * 0.3,
                           SUNK)
        later = VGroup(*[W.coin(MONEY, 0.15) for _ in range(4)]).arrange(RIGHT, buff=0.3)
        later.next_to(fac, DOWN, buff=0.7)
        lt = Text("revenue, later", font=FONT, font_size=T_SMALL, color=MONEY)
        lt.next_to(later, DOWN, buff=0.18)

        with self.narrate("It means this. You spend a large sum of money now, to build "
                          "something that will produce revenue later."):
            self.play(FadeIn(bag), run_time=0.7)
            self.play(Create(arr), run_time=0.8)
            self.play(FadeIn(fac), run_time=0.8)
            self.play(FadeIn(later), FadeIn(lt), run_time=0.8)

        self.define("investment", "Spending now to earn later.", "slab", SUNK,
                    narration="Investment. Spending a large sum now, to build "
                              "something that produces revenue later.",
                    at=DOWN * 2.2)

        with self.narrate("A factory. A shop fitted out. A well drilled. A machine "
                          "bought. That is investment, and that is the decision this "
                          "whole film is about."):
            self.play(ava.point_at(fac), ava.mood("pleased"), run_time=0.9)
            self.wait(1.0)

        self.close_chapter([
            "revenue − cost = profit",
            "fixed stays put · variable moves",
            "investment = spend now, earn later",
        ])
