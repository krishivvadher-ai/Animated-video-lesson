import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.theme import *


class Chapter24(Chapter):
    CH = 24
    TITLE = "What quantitative easing actually is"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ['ticket', 'money', 'scale', 'bank']

    def body(self):
        with self.narrate("This is the chapter where it would be easiest to lose you, "
                          "so we go slowly, and we do the key sum three times."):
            pass

        # -------------------------------------------------- a bond, from the start
        head0 = cards.section_title("Where a gilt comes from", color=CHALK, size=T_SUB)
        self.play(FadeIn(head0), run_time=0.5)

        gov = W.building(SRC_BR, 0.8, "government", "the government").move_to(
            LEFT * 4.4 + UP * 0.4)
        with self.narrate("A government wants to spend more this year than it collects "
                          "in tax. So it needs to borrow."):
            self.play(Create(gov[0]), FadeIn(gov[1]), run_time=1.4)

        saver = stick.StickFigure("a saver", CHALK, scale=0.8).move_to(
            RIGHT * 4.2 + DOWN * 0.4)
        sl = saver.label()
        with self.narrate("And here is somebody with money they would like to put "
                          "somewhere safe — a pension fund, an insurer, a saver."):
            self.play(FadeIn(saver), FadeIn(sl), run_time=0.8)

        bag = W.money_bag(MONEY, 0.9).move_to(RIGHT * 1.2 + UP * 1.2)
        with self.narrate("The saver hands over a hundred pounds."):
            self.play(FadeIn(bag), run_time=0.6)
            self.play(bag.animate.move_to(LEFT * 2.2 + UP * 0.9), run_time=1.4)

        tk = W.ticket(SRC_BR, "£5 a year\nthen £100 in 2030", 0.9)
        tk.move_to(RIGHT * 0.9 + DOWN * 0.9)
        with self.narrate("And gets back a piece of paper. A promise. Five pounds every "
                          "year, and then the hundred pounds back on a fixed date."):
            self.play(FadeOut(bag), run_time=0.3)
            self.play(FadeIn(tk, scale=0.8), run_time=0.9)
            self.play(tk.animate.next_to(saver, LEFT, buff=0.5), run_time=1.0)

        coins = W.coupon_stream(tk, 4, MONEY)
        yrs = VGroup(*[Text(y, font=FONT, font_size=T_TINY, color=MUTED)
                       for y in ("2026", "2027", "2028", "2029")])
        for c, y in zip(coins, yrs):
            y.next_to(c, DOWN, buff=0.15)
        with self.narrate("Year after year, the five pounds arrives. It never changes. "
                          "That is the whole point of it."):
            for c, y in zip(coins, yrs):
                self.play(FadeIn(c, shift=DOWN * 0.2), FadeIn(y), run_time=0.45)
        self.beat()

        back = W.money_bag(MONEY, 0.7).move_to(coins.get_right() + RIGHT * 1.2)
        bl = Text("2030", font=FONT, font_size=T_TINY, color=MUTED)
        bl.next_to(back, DOWN, buff=0.2)
        with self.narrate("And on the date printed on it, the hundred pounds comes back."):
            self.play(FadeIn(back), FadeIn(bl), run_time=0.8)
        self.beat()

        self.define("government bond, or gilt", "A promise the government has already "
                    "sold, to pay fixed amounts on fixed dates.", "ticket", SRC_BR,
                    at=UP * 2.0, hold=4.6)

        # -------------------------------------------------- it can change hands
        self.clear_stage()
        head1 = cards.section_title("And it can be sold on", color=CHALK, size=T_SUB)
        self.play(FadeIn(head1), run_time=0.5)
        a = stick.StickFigure("", CHALK, scale=0.75).move_to(LEFT * 4.2 + DOWN * 0.3)
        b = stick.StickFigure("", CHALK, scale=0.75).move_to(RIGHT * 4.2 + DOWN * 0.3)
        tk2 = W.ticket(SRC_BR, "£5 a year", 0.8).next_to(a, UP, buff=0.6)
        self.play(FadeIn(a), FadeIn(b), FadeIn(tk2), run_time=0.9)
        price = Text("£100", font=FONT, font_size=T_SUB, color=MONEY)
        price.move_to(UP * 0.3)
        with self.narrate("The saver does not have to keep it until then. There is a "
                          "market, and the gilt can be sold on to somebody else, at "
                          "whatever price the two of them agree."):
            self.play(tk2.animate.next_to(b, UP, buff=0.6), run_time=1.6)
            self.play(FadeIn(price), run_time=0.6)
        fix = Text("but the £5 a year never changes", font=FONT, font_size=T_BODY,
                   color=SRC_BR)
        fix.to_edge(DOWN, buff=0.9)
        with self.narrate("But whatever price it changes hands at, the five pounds a "
                          "year printed on it never changes. That one fact is the whole "
                          "of the next section."):
            self.play(FadeIn(fix), run_time=0.9)
            self.play(S.flash_around(fix, color=SRC_BR, buff=0.2, stroke_width=4),
                      run_time=1.4)
        self.beat()
        self.clear_stage()

        # -------------------------------------------------- price up, yield down
        self.clear_stage()
        head = cards.section_title("One idea. Everything downstream depends on it.", color=CHALK, size=T_SUB)
        self.play(FadeIn(head), run_time=0.5)

        tk2 = W.ticket(SRC_BR, "pays £5 a year", 0.95).move_to(LEFT * 4.2 + UP * 0.6)
        fixed = Text("this never changes", font=FONT, font_size=T_SMALL, color=SRC_BR)
        fixed.next_to(tk2, DOWN, buff=0.25)
        self.play(FadeIn(tk2), FadeIn(fixed), run_time=0.8)
        with self.narrate("The payments printed on the ticket never change. Whatever "
                          "happens, it pays five pounds a year. Hold on to that."):
            self.play(Indicate(fixed, color=SRC_BR), run_time=1.0)

        rows = [("£100", "£5 ÷ £100  =  5%", 0.0),
                ("£125", "£5 ÷ £125  =  4%", -1.2),
                ("£200", "£5 ÷ £200  =  2.5%", -2.4)]
        says = ["Pay a hundred pounds for it, and you get five pounds a year. That is "
                "five per cent.",
                "Now suppose lots of buyers appear and the price goes up to a hundred "
                "and twenty-five. You are paying more for exactly the same five pounds. "
                "Four per cent.",
                "Push the price to two hundred, and it is two and a half per cent. Same "
                "ticket. Same five pounds. Half the return."]
        grp = VGroup()
        for i, (price, sums, y) in enumerate(rows):
            p = Text("you pay " + price, font=FONT, font_size=T_BODY, color=CHALK)
            s = Text(sums, font=FONT, font_size=T_BODY, color=MONEY)
            r = VGroup(p, s).arrange(RIGHT, buff=0.9)
            r.move_to(RIGHT * 1.6 + UP * (1.4 + y))
            grp.add(r)
            with self.narrate(says[i]):
                self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.8)
            self.beat(0.5)

        law = cards.body("Price up, return down. Always.", size=T_HEAD, color=SRC_BR,
                         width=26)
        law.to_edge(DOWN, buff=0.7)
        with self.narrate("Price up, return down. Always. There is no way round it, "
                          "because the payments on the ticket are fixed."):
            self.play(FadeIn(law), run_time=0.9)
        self.beat()

        self.define("yield", "The return, as a share of what you paid.", "ticket", SRC_BR,
                    narration="That return has a name. The yield. The return on a bond, "
                              "as a percentage of what you paid for it.",
                    at=UP * 0.2, hold=4.2)

        # -------------------------------------------------- QE itself
        self.clear_stage()
        gov = stick.governor(scale=1.0).shift(LEFT * 4.6 + DOWN * 0.6)
        self.play(FadeIn(gov), run_time=0.5)
        head2 = cards.section_title("So here is the policy", color=CHALK, size=T_SUB)
        self.play(FadeIn(head2), run_time=0.5)

        newmoney = W.money_bag(MONEY, 1.0).move_to(LEFT * 1.4 + UP * 1.4)
        tickets = VGroup(*[W.ticket(SRC_BR, "gilt", 0.42) for _ in range(6)])
        tickets.arrange_in_grid(2, 3, buff=0.35).move_to(RIGHT * 3.4 + UP * 1.2)
        with self.narrate("The central bank creates new money."):
            self.play(FadeIn(newmoney), run_time=0.7)
        with self.narrate("And uses it to buy these tickets. In enormous quantities."):
            self.play(FadeIn(tickets), run_time=0.8)
            arr = W.flow_arrow(newmoney.get_right() + RIGHT * 0.2,
                               tickets.get_left() + LEFT * 0.2, MONEY)
            self.play(Create(arr), run_time=0.9)

        res = cards.body("price up ⇒ yield down", size=T_SUB, color=SRC_BR, width=40)
        res.move_to(DOWN * 1.6)
        with self.narrate("So many buyers appear that the price of gilts rises. And "
                          "therefore, by the sum we just did three times, the yield "
                          "falls."):
            self.play(FadeIn(res), run_time=1.0)
        self.beat()

        self.define("quantitative easing", "New money, buying government bonds in bulk.",
                    "bank", SRC_BR,
                    at=UP * 0.2, hold=4.6)

        # -------------------------------------------------- creating money
        self.clear_stage()
        careful = cards.body("an asset is swapped for money — nothing is printed, nothing given away",
                             size=T_BODY, color=CHALK, width=44)
        careful.move_to(UP * 0.4)
        with self.narrate("One careful sentence about creating money, because it is the "
                          "thing everyone misunderstands. The Bank credits the seller's "
                          "account with money that did not exist before, and takes the "
                          "bond in exchange. Nothing is printed, and nothing is given "
                          "away. An asset is swapped for money."):
            self.play(FadeIn(careful), run_time=1.4)
        self.beat()

        self.close_chapter([
            "a gilt: fixed payments, fixed dates",
            "payments fixed ⇒ price up, return down",
            "That return is the yield.",
            "QE: new money buys gilts",
        ])
