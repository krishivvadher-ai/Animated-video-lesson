import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter26(Chapter):
    CH = 26
    TITLE = "Channel one: the hot potato"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["money", "risk", "flow", "people"]

    def body(self):
        kit = stick.kit(scale=0.85)
        St.place(kit, St.STAGE, ax=-0.75, ay=-0.5)
        with self.narrate("Leg one of the chain has three channels, and this is the big "
                          "one. The one the Bank of England itself puts first."):
            self.heading("The channel the Bank puts first")
            self.play(FadeIn(kit), run_time=0.7)
        self.play(FadeOut(kit), run_time=0.4)

        # ------------------------------------------------ the trap
        self.heading("First, the way it can fail")
        money = VGroup(*[W.coin(MONEY, 0.18) for _ in range(3)]).arrange(RIGHT, buff=0.12)
        bill = W.ticket(MUTED, "1-month bill", scale=0.9)
        pairing = VGroup(money, bill).arrange(RIGHT, buff=2.2)
        St.place(pairing, St.STAGE, ay=0.5)
        z1 = Text("pays 0%", font=FONT, font_size=T_SMALL, color=COST)
        z1.next_to(money, DOWN, buff=0.3)
        z2 = Text("pays 0%", font=FONT, font_size=T_SMALL, color=COST)
        z2.next_to(bill, DOWN, buff=0.3)
        with self.narrate("At the zero lower bound, money pays nothing. And a piece of "
                          "government debt that matures next month, at a rate of "
                          "practically zero, also pays nothing."):
            self.play(FadeIn(money), FadeIn(z1), run_time=0.8)
            self.play(FadeIn(bill), FadeIn(z2), run_time=0.8)
            eq = Text("=", font=FONT, font_size=T_HEAD, color=MUTED)
            eq.move_to(pairing.get_center())
            self.play(FadeIn(eq), run_time=0.5)

        drawer = Rectangle(width=2.4, height=1.1, color=MUTED, stroke_width=3)
        handle = Line(LEFT * 0.3, RIGHT * 0.3, color=MUTED, stroke_width=4)
        handle.move_to(drawer.get_center())
        dr = VGroup(drawer, handle)
        St.place(dr, St.SIDE, ay=-0.3)
        dlab = Text("into a drawer", font=FONT, font_size=T_SMALL, color=MUTED)
        dlab.next_to(dr, DOWN, buff=0.24)
        with self.narrate("If the seller does not care which of those two it holds, the "
                          "story ends right there. It takes the money, puts it in a "
                          "drawer, and nothing else moves."):
            self.play(Create(dr), FadeIn(dlab), run_time=0.9)
            self.play(money.animate.move_to(dr.get_center()), run_time=1.1)
            self.play(FadeOut(money), FadeOut(z1), FadeOut(eq), run_time=0.4)
        self.beat()
        self.clear_stage()
        self.define("a liquidity trap", "When extra money is simply held, and nothing "
                    "moves.", "fog", COST, at=UP * 1.9, hold=4.4)

        jp = St.caption("Japan, 2001 – 2006", MUTED, T_SUB, width=22)
        St.place(jp, St.FULL, ay=0.2)
        with self.narrate("Economists have a name for that. And buying short-dated debt "
                          "with money — what is sometimes called pure quantitative "
                          "easing — can run straight into it. Japan did exactly that "
                          "between two thousand and one and two thousand and six."):
            self.play(FadeIn(jp), run_time=0.8)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the ladder
        self.heading("So line up the things you can hold")
        rungs = [("money", MONEY, 0.0), ("short bills", MUTED, 0.85),
                 ("10-year gilts", SRC_BR, 1.70), ("company bonds", TRIGGER, 2.55),
                 ("shares", COST, 3.40)]
        ladder = VGroup()
        for name, col, y in rungs:
            r = Rectangle(width=3.1, height=0.56, color=col, stroke_width=3,
                          fill_color=col, fill_opacity=0.18)
            t = Text(name, font=FONT, font_size=T_SMALL, color=col)
            t.move_to(r.get_center())
            ladder.add(VGroup(r, t).shift(UP * y))
        ladder.move_to(ORIGIN)
        St.place(ladder, St.STAGE, ax=-0.15, ay=0.0)
        axis = Arrow(ladder.get_bottom() + DOWN * 0.2 + LEFT * 2.1,
                     ladder.get_top() + UP * 0.2 + LEFT * 2.1,
                     color=MUTED, stroke_width=3, buff=0)
        safe = Text("safest", font=FONT, font_size=T_TINY, color=MUTED)
        safe.next_to(axis, DOWN, buff=0.16)
        risky = Text("riskiest", font=FONT, font_size=T_TINY, color=MUTED)
        risky.next_to(axis, UP, buff=0.16)
        with self.narrate("Line up the things somebody can hold, from the safest at the "
                          "bottom to the riskiest at the top."):
            self.play(GrowArrow(axis), FadeIn(safe), FadeIn(risky), run_time=0.8)
            self.play(S.lag_map(FadeIn, ladder, lag=0.14), run_time=1.6)

        drop = St.caption("sell the gilt, hold the money,\nand your return drops",
                          COST, T_BODY, width=24)
        St.place(drop, St.SIDE, ay=0.6)
        with self.narrate("A ten-year gilt pays more than money. Sell it and hold the "
                          "money instead, and the return on your whole portfolio drops."):
            self.play(Indicate(ladder[2], color=SRC_BR, scale_factor=1.08),
                      run_time=0.9)
            self.play(FadeIn(drop), run_time=0.7)
        self.beat()

        # ------------------------------------------------ the hot potato
        self.heading("So the money gets passed along")
        self.play(FadeOut(drop), FadeOut(axis), FadeOut(safe), FadeOut(risky),
                  run_time=0.5)
        self.play(FadeOut(ladder), run_time=0.7)
        holders = VGroup(*[stick.StickFigure("", CHALK, scale=0.55) for _ in range(4)])
        holders.arrange(RIGHT, buff=1.5)
        St.place(holders, St.FULL, ay=-0.75)
        hot = W.coin(MONEY, 0.24)
        hot.next_to(holders[0], UP, buff=0.35)
        with self.narrate("The seller has money it did not want. So it goes looking for "
                          "something else to hold — something a little riskier, which "
                          "is now relatively cheap."):
            self.play(FadeIn(holders), run_time=0.8)
            self.play(GrowFromCenter(hot), run_time=0.5)
        with self.narrate("And whoever sells it that thing now has the money instead. "
                          "So they go looking too."):
            for i in range(1, 4):
                self.play(hot.animate.next_to(holders[i], UP, buff=0.35),
                          run_time=0.55)
                self.play(S.spark(hot, TRIGGER), run_time=0.4)
        pot = St.caption("nobody wants to be left holding it", TRIGGER, T_SUB, width=34)
        St.place(pot, St.FOOT, pad=0.06)
        with self.narrate("The authors call it passing the money around like a hot "
                          "potato. Nobody wants to be left holding it."):
            self.play(FadeIn(pot), run_time=0.8)
            self.play(S.flash_around(pot, TRIGGER, run_time=2.0))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the risk pool
        self.heading("And a second way of seeing it")
        pool = Circle(radius=1.5, color=COST, stroke_width=4,
                      fill_color=COST, fill_opacity=0.18)
        St.place(pool, St.STAGE, ax=-0.2, ay=0.1)
        plab = St.caption("all the interest-rate risk\nin the bond market",
                          COST, T_SMALL, width=24)
        plab.next_to(pool, UP, buff=0.30)
        with self.narrate("Think of all the interest-rate risk in the bond market as "
                          "one pool, which somebody has to carry."):
            self.play(Create(pool), FadeIn(plab), run_time=1.1)

        slice_ = AnnularSector(inner_radius=0.0, outer_radius=1.5,
                               angle=TAU * 0.35, color=SRC_BR,
                               fill_color=SRC_BR, fill_opacity=0.4,
                               stroke_width=3)
        slice_.move_arc_center_to(pool.get_center())
        bank = cards.icon("bank", SRC_BR, 1.6)
        St.place(bank, St.SIDE, ay=0.5)
        with self.narrate("When the central bank buys long-dated bonds, it carries some "
                          "of that risk itself. So there is less left for everybody "
                          "else to carry."):
            self.play(Create(bank), run_time=0.8)
            self.play(FadeIn(slice_), run_time=0.9)
            self.play(slice_.animate.next_to(bank, DOWN, buff=0.35).scale(0.5),
                      run_time=1.4)
            carried = Text("carried by the Bank", font=FONT, font_size=T_SMALL,
                           color=SRC_BR)
            carried.next_to(slice_, DOWN, buff=0.22)
            self.play(FadeIn(carried), run_time=0.6)

        fall = St.caption("so the extra return demanded falls", MONEY, T_SUB, width=32)
        St.place(fall, St.FOOT, pad=0.06)
        with self.narrate("And so the extra return they demand for carrying it falls, "
                          "which pushes longer-term real interest rates down. That is "
                          "the thinking behind the American programme nicknamed "
                          "operation twist."):
            self.play(FadeIn(fall), run_time=0.8)
        self.beat()

        self.close_chapter([
            "if money and bills are the same, nothing moves",
            "buy long, and the seller must go up the ladder",
            "money passed along like a hot potato",
            "and the Bank carries risk everyone else was carrying",
        ])
