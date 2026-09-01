import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter01(Chapter):
    CH = 1
    TITLE = "What “investment” actually means"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["money", "flow", "slab"]

    def body(self):
        # ------------------------------------------------ the shop
        self.heading("Money in, money out")
        fac = W.factory(CHALK, 1.0)
        St.place(fac, St.FULL, ay=0.15)
        cap = Text("Nell's factory", font=FONT, font_size=T_SMALL, color=MUTED)
        cap.next_to(fac, DOWN, buff=0.3)
        with self.narrate("Start with the simplest picture there is. A factory. "
                          "Nell's factory."):
            self.play(Create(fac), run_time=1.4)
            self.play(FadeIn(cap), run_time=0.5)

        a_in = W.flow_arrow(fac.get_left() + LEFT * 3.2, fac.get_left() + LEFT * 0.3, MONEY)
        t_in = Text("money coming in", font=FONT, font_size=T_BODY, color=MONEY)
        t_in.next_to(a_in, UP, buff=0.2)
        with self.narrate("Every month, money comes in. Customers buy what she makes, "
                          "and they pay her."):
            self.play(Create(a_in), FadeIn(t_in), run_time=1.1)
            self.play(S.flow_along(a_in, MONEY))
        self.define("revenue", "All the money coming in, before anything is taken out.",
                    "money", MONEY, at=DOWN * 2.2, hold=3.6,
                    narration="Economists call that revenue. All the money coming in, "
                              "before anything is taken out of it.")

        a_out = W.flow_arrow(fac.get_right() + RIGHT * 0.3, fac.get_right() + RIGHT * 3.2, COST)
        t_out = Text("money going out", font=FONT, font_size=T_BODY, color=COST)
        t_out.next_to(a_out, UP, buff=0.2)
        with self.narrate("Every month, money also goes out. She pays for materials, "
                          "for electricity, for wages, for the rent."):
            self.play(Create(a_out), FadeIn(t_out), run_time=1.1)
            self.play(S.flow_along(a_out, COST))
        self.define("cost", "All the money going out to keep the place running.",
                    "flow", COST, at=DOWN * 2.2, hold=3.4)

        keep = St.caption("what is left over", MONEY, T_SUB, width=20)
        St.place(keep, St.FOOT, pad=0.06)
        with self.narrate("The difference between the two is what she actually keeps."):
            self.play(FadeIn(keep), run_time=0.8)
            self.play(S.flash_around(keep, MONEY))
        self.define("profit", "Revenue minus cost. What is left over.", "money", MONEY,
                    at=DOWN * 2.2, hold=3.4)
        self.clear_stage()

        # ------------------------------------------------ two kinds of cost
        self.heading("Two kinds of cost")
        rent = VGroup(Rectangle(width=2.4, height=1.4, color=COST, stroke_width=3,
                                fill_color=COST, fill_opacity=0.20),
                      Text("the rent", font=FONT, font_size=T_BODY, color=COST))
        rent[1].move_to(rent[0])
        wood = VGroup(Rectangle(width=2.4, height=1.4, color=SUNK, stroke_width=3,
                                fill_color=SUNK, fill_opacity=0.20),
                      Text("the wood", font=FONT, font_size=T_BODY, color=SUNK))
        wood[1].move_to(wood[0])
        pair = VGroup(rent, wood).arrange(RIGHT, buff=2.2)
        St.place(pair, St.FULL, ay=0.35)

        with self.narrate("Not all costs behave the same way. The rent is the same "
                          "whether she makes one chair or a thousand."):
            self.play(FadeIn(rent), run_time=0.9)
            self.play(rent[0].animate.set_stroke(width=6), run_time=0.4)
            self.play(rent[0].animate.set_stroke(width=3), run_time=0.4)
        self.define("fixed cost", "A cost that does not change with how much you make.",
                    "slab", COST, at=DOWN * 2.3, hold=3.2)

        with self.narrate("The wood is different. Make twice as many chairs and she "
                          "buys twice as much wood."):
            self.play(FadeIn(wood), run_time=0.9)
            self.play(wood[0].animate.stretch(2.0, 0), run_time=1.0)
            self.play(wood[0].animate.stretch(0.5, 0), run_time=0.7)
        self.define("variable cost", "A cost that rises and falls with how much you "
                    "make.", "flow", SUNK, at=DOWN * 2.3, hold=3.2)
        self.clear_stage()

        # ------------------------------------------------ investment
        self.heading("The word this film turns on")
        ava = stick.ava(scale=0.95)
        St.place(ava, St.STAGE, ax=-0.78, ay=-0.2)
        self.play(FadeIn(ava), run_time=0.6)
        q = ava.say("Isn't that buying shares?", direction=UP, width=3.4)
        with self.narrate("You may think investment means buying shares in a company. "
                          "That is not what an economist means by it.", v="c"):
            self.play(FadeIn(q), ava.mood("thinking"), run_time=0.7)
            self.play(FadeOut(q), run_time=0.4)

        bag = W.money_bag(SUNK, 1.15)
        fac2 = W.factory(CHALK, 0.72)
        later = VGroup(*[W.coin(MONEY, 0.16) for _ in range(4)]).arrange(RIGHT, buff=0.32)
        row = VGroup(bag, fac2, later).arrange(RIGHT, buff=1.5)
        St.place(row, St.STAGE, ax=0.12, ay=0.1)
        a1 = W.flow_arrow(bag.get_right() + RIGHT * 0.2, fac2.get_left() + LEFT * 0.2, SUNK)
        a2 = W.flow_arrow(fac2.get_right() + RIGHT * 0.2, later.get_left() + LEFT * 0.2, MONEY)
        now = Text("now", font=FONT, font_size=T_SMALL, color=SUNK)
        now.next_to(bag, DOWN, buff=0.28)
        lat = Text("later", font=FONT, font_size=T_SMALL, color=MONEY)
        lat.next_to(later, DOWN, buff=0.28)

        with self.narrate("It means this. You spend a large sum of money now, to build "
                          "something that will produce revenue later."):
            self.play(FadeIn(bag), FadeIn(now), run_time=0.7)
            self.play(Create(a1), run_time=0.7)
            self.play(Create(fac2), run_time=0.9)
            self.play(Create(a2), run_time=0.7)
            self.play(FadeIn(later), FadeIn(lat), run_time=0.7)
        self.define("investment", "Spending a large sum now to build something that "
                    "earns later.", "slab", SUNK, at=DOWN * 2.4, hold=4.0)

        with self.narrate("A factory. A shop fitted out. A well drilled. A machine "
                          "bought. That is investment, and that is the decision this "
                          "whole film is about."):
            self.play(ava.point_at(fac2), ava.mood("pleased"), run_time=0.9)
            self.play(S.flash_around(VGroup(bag, fac2, later), SUNK, run_time=2.0))
        self.beat()

        self.close_chapter([
            "revenue − cost = profit",
            "fixed stays put · variable moves",
            "investment = spend now, earn later",
        ])
