import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.balance import TAccount
from lib.theme import *


class Chapter25(Chapter):
    CH = 25
    TITLE = "Three balance sheets"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["people", "bank", "money", "ticket"]

    def body(self):
        with self.narrate("The policy is easy to describe and easy to get wrong. So we "
                          "are going to follow the money through three sets of books, "
                          "one at a time."):
            pass

        self.define("balance sheet", "What you own, and what you owe.", "scale", CHALK, hold=4.2)
        self.define("portfolio", "Everything somebody holds.", "queue", CHALK, hold=3.4)

        # ---------------------------------------------------- who sells
        seller = VGroup(
            stick.StickFigure("", CHALK, hat="specs", scale=0.7),
            stick.StickFigure("", CHALK, scale=0.7)).arrange(RIGHT, buff=0.5)
        slab = cards.body("pension funds and insurance companies", size=T_SMALL,
                          color=MUTED, width=20)
        slab.next_to(seller, DOWN, buff=0.25)
        grp = VGroup(seller, slab).move_to(LEFT * 4.0 + UP * 1.2)
        with self.narrate("The people who actually sell the gilts are usually not "
                          "banks. They are pension funds and insurance companies — the "
                          "non-bank private sector."):
            self.play(FadeIn(grp), run_time=1.0)
        self.define("the non-bank private sector", "Pension funds, insurers — not banks.",
                    "people", CHALK, at=RIGHT * 2.0 + UP * 0.6, hold=4.4)

        # ---------------------------------------------------- three T accounts
        self.clear_stage()
        t1 = TAccount("the seller", 3.7, 2.2, CHALK).move_to(LEFT * 4.3 + UP * 0.4)
        t2 = TAccount("the central bank", 3.7, 2.2, SRC_BR).move_to(UP * 0.4)
        t3 = TAccount("a private bank", 3.7, 2.2, MONEY).move_to(RIGHT * 4.3 + UP * 0.4)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), run_time=0.7)
        self.play(FadeIn(t3), run_time=0.7)

        e1 = t1.entry("gilts", "L", "−")
        with self.narrate("The seller hands over its gilts. So its holdings of gilts "
                          "go down."):
            self.play(FadeIn(e1), run_time=0.8)
        e2 = t1.entry("deposits", "L", "+")
        with self.narrate("And it gets money instead — not printed notes, but a number "
                          "credited to its bank account. So its deposits go up."):
            self.play(FadeIn(e2), run_time=0.8)
        self.beat()

        e3 = t2.entry("gilts", "L", "+")
        e4 = t2.entry("reserves", "R", "+")
        with self.narrate("The central bank now owns the gilts. And it pays for them by "
                          "creating reserves — money that only banks hold, at the "
                          "central bank."):
            self.play(FadeIn(e3), run_time=0.7)
            self.play(FadeIn(e4), run_time=0.7)
        self.beat()

        e5 = t3.entry("reserves", "L", "+")
        e6 = t3.entry("deposits", "R", "+")
        with self.narrate("And the bank in the middle sits between them. It has more "
                          "reserves on one side, and it owes the seller more deposits "
                          "on the other. Both sides of its books grow together."):
            self.play(FadeIn(e5), run_time=0.7)
            self.play(FadeIn(e6), run_time=0.7)
        self.beat()

        key = cards.body("every entry is matched", size=T_SUB, color=CHALK, width=44)
        key.to_edge(DOWN, buff=0.8)
        with self.narrate("Look at that and notice what has not happened. Nobody has "
                          "been given anything. Every single one of those entries is "
                          "matched by another one."):
            self.play(FadeIn(key), run_time=1.0)
        self.beat()

        start = cards.body("the seller's portfolio is disturbed",
                           size=T_SUB, color=TRIGGER, width=44)
        start.to_edge(DOWN, buff=0.8)
        with self.narrate("What has happened is that the seller's portfolio has been "
                          "disturbed. It wanted gilts, and now it is holding money. And "
                          "that disturbance is where the whole mechanism starts."):
            self.play(FadeOut(key), FadeIn(start), run_time=1.0)
            self.play(S.flash_around(t1.box, color=TRIGGER, buff=0.15, stroke_width=4),
                      run_time=1.4)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- how it differs
        head = Text("So how is this different from ordinary monetary policy?",
                    font=FONT, font_size=T_SUB, color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)

        left = VGroup(
            cards.body("ORDINARY", size=T_SUB, color=MONEY, width=18),
            cards.body("the PRICE of money",
                       size=T_BODY, color=CHALK, width=22),
        ).arrange(DOWN, buff=0.5)
        right = VGroup(
            cards.body("QUANTITATIVE EASING", size=T_SUB, color=TRIGGER, width=18),
            cards.body("the QUANTITY of money", size=T_BODY, color=CHALK, width=22),
        ).arrange(DOWN, buff=0.5)
        cols = VGroup(left, right).arrange(RIGHT, buff=2.0).move_to(UP * 0.6)
        with self.narrate("Ordinary monetary policy sets the price of money. One "
                          "short-term interest rate, and everything else follows from "
                          "what people expect that rate to do."):
            self.play(FadeIn(left), run_time=1.0)
        with self.narrate("Quantitative easing sets the quantity instead. And it aims "
                          "directly at longer-term rates, rather than reaching them "
                          "through expectations."):
            self.play(FadeIn(right), run_time=1.0)
        self.beat()

        fair = cards.body("what is unusual is the scale, not the act", size=T_BODY, color=SRC_BR, width=48)
        fair.to_edge(DOWN, buff=0.7)
        with self.narrate("And the authors are careful here. There is nothing unusual "
                          "about a central bank buying assets at all. What distinguishes "
                          "these operations is the circumstances they took place in, "
                          "and their scale."):
            self.play(FadeIn(fair), run_time=1.2)
        self.beat()
        self.play(FadeOut(fair), run_time=0.4)

        what = cards.body("short debt ≈ money   ·   long gilts ≠ money",
                          size=T_BODY, color=CHALK, width=48)
        what.to_edge(DOWN, buff=0.62)
        with self.narrate("And one more difference, which matters enormously in the "
                          "next chapter. What is bought. Short-dated government debt is "
                          "very nearly the same thing as money. Long-dated gilts, "
                          "company debt and mortgage-backed securities are not. The "
                          "effectiveness of the policy may depend on what is bought, "
                          "as well as how much."):
            self.play(FadeIn(what), run_time=1.4)
        self.beat()

        self.close_chapter([
            "sellers: pension funds and insurers",
            "gilts ⇄ deposits ⇄ reserves",
            "every entry is matched",
            "the seller holds money it did not want",
        ])
