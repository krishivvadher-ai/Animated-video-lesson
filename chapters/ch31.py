import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.balance import TAccount
from lib.theme import *


class Chapter31(Chapter):
    CH = 31
    TITLE = "Three sets of books"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["slab", "bank", "people", "flow"]

    def body(self):
        self.heading("Follow the money through the books")
        kit = stick.kit(scale=0.85)
        St.place(kit, St.STAGE, ax=-0.8, ay=-0.5)
        with self.narrate("The policy is easy to describe and easy to get wrong. So we "
                          "are going to follow the money through three sets of books, "
                          "one at a time.", v="c"):
            self.play(FadeIn(kit), run_time=0.7)

        self.define("a balance sheet", "What somebody owns on one side, what they owe "
                    "on the other.", "slab", CHALK, at=UP * 0.3, hold=4.4)
        self.clear_stage()

        # ------------------------------------------------ who actually sells
        self.heading("Who actually sells the gilts")
        who = VGroup(
            VGroup(cards.icon("people", MONEY, 1.7),
                   Text("pension funds", font=FONT, font_size=T_SMALL, color=MONEY)
                   ).arrange(DOWN, buff=0.22),
            VGroup(cards.icon("shield", MONEY, 1.7),
                   Text("insurers", font=FONT, font_size=T_SMALL, color=MONEY)
                   ).arrange(DOWN, buff=0.22),
        ).arrange(RIGHT, buff=1.6)
        St.place(who, St.STAGE, ay=0.25)
        crossed = VGroup(cards.icon("bank", MUTED, 1.7),
                         Text("not banks", font=FONT, font_size=T_SMALL, color=MUTED)
                         ).arrange(DOWN, buff=0.22)
        St.place(crossed, St.SIDE, ay=0.25)
        with self.narrate("The people who actually sell the gilts are usually not "
                          "banks. They are pension funds and insurance companies — the "
                          "non-bank private sector."):
            self.play(FadeIn(who), run_time=1.0)
            self.play(FadeIn(crossed), run_time=0.6)
            x = Cross(crossed[0], stroke_color=COST, stroke_width=6).scale(0.7)
            self.play(Create(x), run_time=0.6)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the three T-accounts
        self.heading("Three sets of books, one entry at a time")
        seller = TAccount("the seller", width=3.5, height=2.2, colour=MONEY)
        cb = TAccount("the central bank", width=3.5, height=2.2, colour=SRC_BR)
        bank = TAccount("the bank in between", width=3.5, height=2.2, colour=WAIT)
        row = VGroup(seller, cb, bank).arrange(RIGHT, buff=0.55)
        St.place(row, St.FULL, ay=-0.1)
        self.play(S.lag_map(FadeIn, VGroup(seller, cb, bank), lag_ratio=0.18),
                  run_time=1.4)

        e1 = seller.entry("gilts", "L", "−")
        with self.narrate("The seller hands over its gilts. So its holdings of gilts go "
                          "down."):
            self.play(FadeIn(e1, shift=LEFT * 0.3), run_time=0.8)
        e2 = seller.entry("deposits", "L", "+")
        with self.narrate("And it gets money instead — not printed notes, but a number "
                          "credited to its bank account. So its deposits go up."):
            self.play(FadeIn(e2, shift=RIGHT * 0.3), run_time=0.8)
        self.beat()

        e3 = cb.entry("gilts", "L", "+")
        e4 = cb.entry("reserves", "R", "+")
        with self.narrate("The central bank now owns the gilts. And it pays for them by "
                          "creating reserves — money that only banks hold, at the "
                          "central bank."):
            self.play(FadeIn(e3, shift=LEFT * 0.3), run_time=0.7)
            self.play(FadeIn(e4, shift=RIGHT * 0.3), run_time=0.7)
        self.define("reserves", "Money banks hold at the central bank, and nobody "
                    "else can.", "bank", SRC_BR, at=DOWN * 2.55, hold=4.0)

        e5 = bank.entry("reserves", "L", "+")
        e6 = bank.entry("deposits", "R", "+")
        with self.narrate("And the bank in the middle sits between them. It has more "
                          "reserves on one side, and it owes the seller more deposits "
                          "on the other. Both sides of its books grow together."):
            self.play(FadeIn(e5, shift=LEFT * 0.3), run_time=0.7)
            self.play(FadeIn(e6, shift=RIGHT * 0.3), run_time=0.7)
        self.beat()

        matched = St.caption("every entry matched by another", TRIGGER, T_SUB, width=32)
        St.place(matched, St.FOOT, pad=0.06)
        with self.narrate("Look at that and notice what has not happened. Nobody has "
                          "been given anything. Every single one of those entries is "
                          "matched by another one."):
            self.play(FadeIn(matched), run_time=0.8)
            self.play(S.flash_around(matched, TRIGGER, run_time=2.0))
        self.beat()
        self.play(FadeOut(matched), run_time=0.4)
        self.clear_stage()

        # ------------------------------------------------ the disturbance
        self.heading("What the seller is left holding")
        want = W.ticket(SRC_BR, "gilts", scale=0.9)
        got = VGroup(*[W.coin(MONEY, 0.22) for _ in range(3)]).arrange(RIGHT, buff=0.14)
        pairing = VGroup(want, got).arrange(RIGHT, buff=2.0)
        St.place(pairing, St.FULL, ay=0.2)
        wl = Text("what it wanted", font=FONT, font_size=T_SMALL, color=SRC_BR)
        wl.next_to(want, DOWN, buff=0.3)
        gl = Text("what it now has", font=FONT, font_size=T_SMALL, color=MONEY)
        gl.next_to(got, DOWN, buff=0.3)
        self.add(wl, gl)
        with self.narrate("What has happened is that the seller's portfolio has been "
                          "disturbed. It wanted gilts, and now it is holding money. And "
                          "that disturbance is where the whole mechanism starts."):
            self.play(FadeIn(want), FadeIn(wl), run_time=0.8)
            self.play(FadeTransform(want.copy(), got), FadeIn(gl), run_time=1.2)
            self.play(S.pulse(got, MONEY))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ price versus quantity
        self.heading("Price of money, or quantity of it")
        lever = cards.icon("lever", WAIT, 2.4)
        pile = VGroup(*[W.coin(MONEY, 0.16) for _ in range(9)])
        pile.arrange_in_grid(3, 3, buff=0.14)
        cols = VGroup(
            VGroup(lever, St.caption("normal policy sets\nthe price of money",
                                     WAIT, T_SMALL, width=22)
                   ).arrange(DOWN, buff=0.4),
            VGroup(pile, St.caption("QE sets the quantity\ninstead",
                                    MONEY, T_SMALL, width=22)
                   ).arrange(DOWN, buff=0.4),
        ).arrange(RIGHT, buff=2.4)
        St.place(cols, St.FULL, ay=0.1)
        with self.narrate("Ordinary monetary policy sets the price of money. One "
                          "short-term interest rate, and everything else follows from "
                          "what people expect that rate to do."):
            self.play(Create(lever), run_time=0.9)
            self.play(FadeIn(cols[0][1]), run_time=0.6)
        with self.narrate("Quantitative easing sets the quantity instead. And it aims "
                          "directly at longer-term rates, rather than reaching them "
                          "through expectations."):
            self.play(S.lag_map(GrowFromCenter, pile, lag=0.08),
                      run_time=1.2)
            self.play(FadeIn(cols[1][1]), run_time=0.6)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the caveats
        self.heading("Two careful qualifications")
        c1 = St.caption("buying assets is not itself unusual", MUTED, T_SUB, width=32)
        St.place(c1, St.FULL, ay=0.9)
        c2 = St.caption("what is new: the circumstances, and the scale",
                        CHALK, T_SUB, width=40)
        St.place(c2, St.FULL, ay=0.25)
        with self.narrate("And the authors are careful here. There is nothing unusual "
                          "about a central bank buying assets at all. What distinguishes "
                          "these operations is the circumstances they took place in, "
                          "and their scale."):
            self.play(FadeIn(c1), run_time=0.7)
            self.play(FadeIn(c2), run_time=0.7)

        near = VGroup(W.ticket(MUTED, "1-month bill", scale=0.85),
                      Text("≈ money", font=FONT, font_size=T_SMALL, color=MUTED)
                      ).arrange(DOWN, buff=0.2)
        far = VGroup(W.ticket(TRIGGER, "10-year gilt", scale=0.85),
                     Text("not money", font=FONT, font_size=T_SMALL, color=TRIGGER)
                     ).arrange(DOWN, buff=0.2)
        two = VGroup(near, far).arrange(RIGHT, buff=2.6)
        St.place(two, St.FULL, ay=-0.55)
        with self.narrate("And one more difference, which matters enormously in the "
                          "next chapter. What is bought. Short-dated government debt is "
                          "very nearly the same thing as money."):
            self.play(FadeIn(near), run_time=0.8)
        with self.narrate("Long-dated gilts, company debt and mortgage-backed "
                          "securities are not. The effectiveness of the policy may "
                          "depend on what is bought, as well as how much."):
            self.play(FadeIn(far), run_time=0.8)
            self.play(S.flash_around(far, TRIGGER))
        self.beat()

        self.close_chapter([
            "the sellers are pension funds, not banks",
            "three sets of books, every entry matched",
            "QE sets a quantity, not a price",
            "and what is bought matters, not just how much",
        ])
