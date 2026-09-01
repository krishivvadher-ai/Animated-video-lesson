import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter24(Chapter):
    CH = 24
    TITLE = "What quantitative easing actually is"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["bank", "ticket", "money", "flow"]

    def body(self):
        # ------------------------------------------------ the government borrows
        self.heading("Why a government borrows at all")
        gov = W.building(SRC_BR, size=0.85, kind="government")
        St.place(gov, St.STAGE, ax=-0.55, ay=0.15)
        glab = Text("the government", font=FONT, font_size=T_SMALL, color=SRC_BR)
        glab.next_to(gov, DOWN, buff=0.28)
        with self.narrate("This is the chapter where it would be easiest to lose you, "
                          "so we go slowly, and we do the key sum three times."):
            self.play(Create(gov), FadeIn(glab), run_time=1.4)

        tax = W.Bar(0.9, color=MONEY, width=0.9)
        spend = W.Bar(1.7, color=COST, width=0.9)
        bars = VGroup(tax, spend).arrange(RIGHT, buff=0.8, aligned_edge=DOWN)
        St.place(bars, St.SIDE, ay=-0.1)
        tl = Text("tax in", font=FONT, font_size=T_TINY, color=MONEY)
        tl.next_to(tax, DOWN, buff=0.2)
        sl = Text("spending", font=FONT, font_size=T_TINY, color=COST)
        sl.next_to(spend, DOWN, buff=0.2)
        St.collapse_bars(VGroup(tax, spend))
        with self.narrate("A government wants to spend more this year than it collects "
                          "in tax. So it needs to borrow."):
            self.play(St.grow_bars(VGroup(tax, spend)), FadeIn(tl), FadeIn(sl))
            self.play(S.flash_around(spend, COST))
        self.beat()

        saver = stick.StickFigure("a pension fund", MONEY, scale=0.8)
        St.place(saver, St.STAGE, ax=0.85, ay=-0.45)
        with self.narrate("And here is somebody with money they would like to put "
                          "somewhere safe — a pension fund, an insurer, a saver."):
            self.play(FadeIn(saver), FadeIn(saver.label()), run_time=0.8)

        # ------------------------------------------------ the swap
        cash = VGroup(*[W.coin(MONEY, 0.15) for _ in range(4)]).arrange(RIGHT, buff=0.1)
        cash.move_to(saver.get_top() + UP * 0.7)
        arrow = W.flow_arrow(saver.get_left() + LEFT * 0.2,
                             gov.get_right() + RIGHT * 0.2, MONEY)
        amt = Text("£100", font=FONT, font_size=T_BODY, color=MONEY)
        amt.next_to(arrow, UP, buff=0.16)
        with self.narrate("The saver hands over a hundred pounds."):
            self.play(FadeIn(cash), run_time=0.5)
            self.play(FadeOut(cash), Create(arrow), FadeIn(amt), run_time=0.9)
            self.play(S.flow_along(arrow, MONEY))
        self.clear_stage(keep=[gov, glab, saver])

        self.define("a gilt", "A piece of British government debt, bought and sold.",
                    "ticket", SRC_BR, at=UP * 1.8, hold=4.2)

        gilt = W.ticket(SRC_BR, "£5 a year · £100 in 2030", scale=1.0)
        St.place(gilt, St.STAGE, ax=0.15, ay=0.35)
        back = W.flow_arrow(gov.get_right() + RIGHT * 0.2 + DOWN * 1.2,
                            saver.get_left() + LEFT * 0.2 + DOWN * 0.6, SRC_BR)
        with self.narrate("And gets back a piece of paper. A promise. Five pounds every "
                          "year, and then the hundred pounds back on a fixed date."):
            self.play(Create(back), run_time=0.7)
            self.play(FadeIn(gilt, shift=RIGHT * 0.4), run_time=1.0)
        self.play(FadeOut(back), FadeOut(gov), FadeOut(glab), FadeOut(saver),
                  run_time=0.6)

        # ------------------------------------------------ the coupons
        self.heading("The payments never change")
        self.play(gilt.animate.move_to(St.STAGE.point(-0.3, 0.5)), run_time=0.8)
        years = ["2026", "2027", "2028", "2029"]
        coins = W.coupon_stream(gilt, 4, MONEY)
        labs = VGroup(*[Text(y, font=FONT, font_size=T_TINY, color=MUTED)
                        .next_to(coins[i], DOWN, buff=0.16)
                        for i, y in enumerate(years)])
        five = VGroup(*[Text("£5", font=FONT, font_size=T_SMALL, color=MONEY)
                        .next_to(coins[i], UP, buff=0.12) for i in range(4)])
        with self.narrate("Year after year, the five pounds arrives. It never changes. "
                          "That is the whole point of it."):
            for i in range(4):
                self.play(FadeIn(coins[i], shift=DOWN * 0.3), FadeIn(five[i]),
                          FadeIn(labs[i]), run_time=0.42)

        final = Text("£100 back", font=FONT, font_size=T_BODY, color=SRC_BR)
        final.next_to(labs, RIGHT, buff=0.7)
        fy = Text("2030", font=FONT, font_size=T_TINY, color=MUTED)
        fy.next_to(final, DOWN, buff=0.16)
        with self.narrate("And on the date printed on it, the hundred pounds comes "
                          "back."):
            self.play(FadeIn(final, shift=UP * 0.3), FadeIn(fy), run_time=0.9)
        self.beat()
        self.clear_stage(keep=[gilt])

        # ------------------------------------------------ the market
        self.heading("But it can be sold on")
        a = stick.StickFigure("holder", CHALK, scale=0.7)
        b = stick.StickFigure("buyer", CHALK, scale=0.7)
        pair = VGroup(a, b).arrange(RIGHT, buff=4.2)
        St.place(pair, St.STAGE, ay=-0.5)
        self.play(gilt.animate.move_to(St.STAGE.point(0.0, 0.9)),
                  run_time=0.7)
        with self.narrate("The saver does not have to keep it until then. There is a "
                          "market, and the gilt can be sold on to somebody else, at "
                          "whatever price the two of them agree."):
            self.play(FadeIn(a), FadeIn(b), FadeIn(a.label()), FadeIn(b.label()),
                      run_time=0.8)
            mv = W.flow_arrow(a.get_top() + UP * 0.3, b.get_top() + UP * 0.3, SRC_BR)
            self.play(Create(mv), run_time=0.8)
            self.play(S.flow_along(mv, SRC_BR))
        fixed = St.caption("£5 a year — whatever it sells for", TRIGGER, T_SUB, width=34)
        St.place(fixed, St.FOOT, pad=0.06)
        with self.narrate("But whatever price it changes hands at, the five pounds a "
                          "year printed on it never changes. That one fact is the whole "
                          "of the next section."):
            self.play(FadeIn(fixed), run_time=0.8)
            self.play(S.flash_around(fixed, TRIGGER))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the sum, three times
        self.heading("The one sum, done three times")
        self.define("yield", "What the fixed payments are worth, as a percentage of "
                    "today's price.", "flow", TRIGGER, hold=4.4)

        pay = Text("£5", font=FONT, font_size=T_HEAD, color=MONEY)
        bar_ = Line(LEFT * 1.1, RIGHT * 1.1, color=CHALK, stroke_width=4)
        price = Text("£100", font=FONT, font_size=T_HEAD, color=SRC_BR)
        frac = VGroup(pay, bar_, price).arrange(DOWN, buff=0.24)
        eq = Text("=  5%", font=FONT, font_size=T_HEAD, color=TRIGGER)
        eq.next_to(frac, RIGHT, buff=0.55)
        sum1 = VGroup(frac, eq)
        St.place(sum1, St.STAGE, ay=0.2)
        cap = St.caption("payments printed on the ticket\nnever change",
                         TRIGGER, T_BODY, width=22)
        St.place(cap, St.SIDE, ay=0.75)
        with self.narrate("The payments printed on the ticket never change. Whatever "
                          "happens, it pays five pounds a year. Hold on to that."):
            self.play(FadeIn(frac), run_time=0.9)
            self.play(FadeIn(eq), FadeIn(cap), run_time=0.8)

        rows = [("£100", "5%", SRC_BR, TRIGGER),
                ("£125", "4%", SRC_BR, WAIT),
                ("£200", "2.5%", SRC_BR, MONEY)]
        says = ["Pay a hundred for it, and five pounds a year is five per cent.",
                "Pay a hundred and twenty-five for exactly the same ticket, and the "
                "same five pounds is only four per cent.",
                "Pay two hundred, and it is two and a half. Same ticket. Same five "
                "pounds."]
        p2 = Text("£125", font=FONT, font_size=T_HEAD, color=SRC_BR)
        e2 = Text("=  4%", font=FONT, font_size=T_HEAD, color=WAIT)
        with self.narrate(says[1]):
            self.play(Transform(price, p2.move_to(price)),
                      Transform(eq, e2.move_to(eq, aligned_edge=LEFT)), run_time=1.2)
        p3 = Text("£200", font=FONT, font_size=T_HEAD, color=SRC_BR)
        e3 = Text("=  2.5%", font=FONT, font_size=T_HEAD, color=MONEY)
        with self.narrate(says[2]):
            self.play(Transform(price, p3.move_to(price)),
                      Transform(eq, e3.move_to(eq, aligned_edge=LEFT)), run_time=1.2)
        self.beat()

        law = St.caption("price up  →  yield down", CHALK, T_HEAD, width=26)
        St.place(law, St.FOOT, pad=0.06)
        up = Arrow(DOWN * 0.4, UP * 0.4, color=MONEY, buff=0,
                   stroke_width=6, max_tip_length_to_length_ratio=0.4)
        dn = Arrow(UP * 0.4, DOWN * 0.4, color=COST, buff=0,
                   stroke_width=6, max_tip_length_to_length_ratio=0.4)
        arrows = VGroup(up, dn).arrange(RIGHT, buff=1.6)
        St.place(arrows, St.SIDE, ay=-0.55)
        with self.narrate("Price up, return down. Always. There is no way round it, "
                          "because the payments on the ticket are fixed."):
            self.play(GrowArrow(up), GrowArrow(dn), run_time=0.9)
            self.play(FadeIn(law), run_time=0.7)
            self.play(S.flash_around(law, TRIGGER, run_time=2.0))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the Bank buys
        self.heading("So the Bank steps into that market")
        bank = W.building(SRC_BR, size=0.85, kind="bank")
        St.place(bank, St.STAGE, ax=-0.75, ay=0.35)
        bl = Text("the central bank", font=FONT, font_size=T_SMALL, color=SRC_BR)
        bl.next_to(bank, DOWN, buff=0.28)
        self.play(Create(bank), FadeIn(bl), run_time=1.2)

        new = VGroup(*[W.coin(MONEY, 0.16) for _ in range(6)])
        new.arrange_in_grid(2, 3, buff=0.16).next_to(bank, UP, buff=0.4)
        with self.narrate("The central bank creates new money."):
            self.play(S.lag_map(GrowFromCenter, new, lag=0.12),
                      run_time=1.2)

        tix = VGroup(*[W.ticket(SRC_BR, "£5 a year", scale=0.85) for _ in range(3)])
        tix.arrange(RIGHT, buff=0.22)
        St.place(tix, St.STAGE, ax=0.55, ay=-0.7, fill=False)
        buy = W.flow_arrow(bank.get_bottom() + DOWN * 0.15 + RIGHT * 0.2,
                           tix.get_top() + UP * 0.2 + LEFT * 0.2, MONEY)
        with self.narrate("And uses it to buy these tickets. In enormous quantities."):
            self.play(FadeIn(tix), run_time=0.8)
            self.play(Create(buy), run_time=0.6)
            self.play(S.flow_along(buy, MONEY), FadeOut(new), run_time=1.4)

        pu = Text("price ↑", font=FONT, font_size=T_SUB, color=MONEY)
        yd = Text("yield ↓", font=FONT, font_size=T_SUB, color=COST)
        res = VGroup(pu, yd).arrange(DOWN, buff=0.45)
        St.place(res, St.SIDE, ay=0.25)
        with self.narrate("So many buyers appear that the price of gilts rises. And "
                          "therefore, by the sum we just did three times, the yield "
                          "falls."):
            self.play(FadeIn(pu, shift=UP * 0.4), run_time=0.7)
            self.play(FadeIn(yd, shift=DOWN * 0.4), run_time=0.7)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ not printing money
        self.heading("Nothing is printed, nothing is given away")
        left = VGroup(cards.icon("bank", SRC_BR, 2.0),
                      Text("the Bank", font=FONT, font_size=T_SMALL, color=SRC_BR)
                      ).arrange(DOWN, buff=0.25)
        right = VGroup(cards.icon("people", MONEY, 2.0),
                       Text("the seller", font=FONT, font_size=T_SMALL, color=MONEY)
                       ).arrange(DOWN, buff=0.25)
        row = VGroup(left, right).arrange(RIGHT, buff=4.6)
        St.place(row, St.FULL, ay=0.45)
        self.play(FadeIn(left), FadeIn(right), run_time=0.8)
        a1 = W.flow_arrow(left.get_right() + RIGHT * 0.25 + UP * 0.35,
                          right.get_left() + LEFT * 0.25 + UP * 0.35, MONEY)
        t1 = Text("money", font=FONT, font_size=T_SMALL, color=MONEY)
        t1.next_to(a1, UP, buff=0.14)
        a2 = W.flow_arrow(right.get_left() + LEFT * 0.25 + DOWN * 0.35,
                          left.get_right() + RIGHT * 0.25 + DOWN * 0.35, SRC_BR)
        t2 = Text("the bond", font=FONT, font_size=T_SMALL, color=SRC_BR)
        t2.next_to(a2, DOWN, buff=0.14)
        with self.narrate("One careful sentence about creating money, because it is the "
                          "thing everyone misunderstands. The Bank credits the seller's "
                          "account with money that did not exist before, and takes the "
                          "bond in exchange."):
            self.play(Create(a1), FadeIn(t1), run_time=0.8)
            self.play(S.flow_along(a1, MONEY))
            self.play(Create(a2), FadeIn(t2), run_time=0.8)
            self.play(S.flow_along(a2, SRC_BR))
        swap = St.caption("an asset swapped for money", TRIGGER, T_SUB, width=30)
        St.place(swap, St.FOOT, pad=0.06)
        with self.narrate("Nothing is printed, and nothing is given away. An asset is "
                          "swapped for money."):
            self.play(FadeIn(swap), run_time=0.8)
            self.play(S.flash_around(swap, TRIGGER, run_time=2.0))
        self.beat()

        self.close_chapter([
            "a gilt: fixed payments, on a fixed date",
            "price up → yield down, always",
            "the Bank creates money and buys gilts",
            "an asset swap — not a gift, not printing",
        ])
