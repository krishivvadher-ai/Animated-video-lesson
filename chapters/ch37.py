import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter37(Chapter):
    CH = 37
    TITLE = "The other tools in the drawer"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["signal", "bank", "door", "money"]

    def body(self):
        self.heading("Three more things they did")
        tools = VGroup()
        for kind, name, col in (("signal", "saying what\ncomes next", SRC_BR),
                                ("bank", "lending to\nbanks in a panic", WAIT),
                                ("door", "cheap funding,\nif you lend it on", MONEY)):
            tools.add(VGroup(cards.icon(kind, col, 1.6),
                             St.caption(name, col, T_SMALL, width=18)
                             ).arrange(DOWN, buff=0.3))
        tools.arrange(RIGHT, buff=1.2)
        St.place(tools, St.FULL, ay=0.15)
        with self.narrate("Buying assets was not the only thing central banks did. The "
                          "authors group the rest into three, and each one is worth "
                          "knowing, because Part Three has to be fair about what else "
                          "was going on."):
            self.play(S.lag_map(FadeIn, tools, shift=UP * 0.25, lag=0.2), run_time=1.8)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ 1: guidance
        self.heading("One — saying what comes next")
        ax = Axes(x_range=[0, 6, 1], y_range=[0, 3, 1], x_length=6.4, y_length=2.8,
                  axis_config=AXIS)
        St.place(ax, St.STAGE, ay=0.15)
        xl = Text("time →", font=FONT, font_size=T_TINY, color=MUTED)
        xl.next_to(ax, DOWN, buff=0.2).align_to(ax, RIGHT)
        yl = Text("the rate", font=FONT, font_size=T_TINY, color=MUTED)
        yl.next_to(ax, UP, buff=0.16).align_to(ax, LEFT)
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), run_time=1.0)

        expect = ax.plot(lambda x: 0.35 + 0.42 * max(x - 1.2, 0), x_range=[0, 6],
                         color=COST, stroke_width=5)
        el = Text("what people expect", font=FONT, font_size=T_TINY, color=COST)
        el.next_to(expect.get_end(), UP, buff=0.18).shift(LEFT * 1.0)
        with self.narrate("Left to themselves, people expect a rate that has been cut "
                          "to nothing to start rising again fairly soon."):
            self.play(Create(expect), FadeIn(el), run_time=1.5)

        gov = stick.governor(scale=0.6)
        St.place(gov, St.SIDE, ay=0.85, fill=False)
        flat = ax.plot(lambda x: 0.35, x_range=[0, 6], color=SRC_BR, stroke_width=6)
        fl = Text("held flat, by announcement", font=FONT, font_size=T_SMALL,
                  color=SRC_BR)
        fl.next_to(flat, DOWN, buff=0.42)
        with self.narrate("So the central bank simply tells them otherwise. It says the "
                          "rate will stay where it is for a long time yet."):
            self.play(FadeIn(gov), run_time=0.6)
            self.play(Transform(expect, flat), FadeOut(el), FadeIn(fl), run_time=1.8)
        self.beat()

        hedge = St.points(["it did move expectations",
                           "but markets never fully priced it in",
                           "and it was not the promise the theory wants"],
                          colour=MUTED, dot_colour=SUNK, size=T_SMALL, width=22)
        St.place(hedge, St.SIDE, ay=-0.25)
        says = ["And the authors are careful about how well it worked. It did move "
                "expectations.",
                "But markets never fully priced in the cuts the announcements implied.",
                "And none of it was quite the promise to be irresponsible later that "
                "the theory in the last chapter actually calls for."]
        for i, row in enumerate(hedge):
            with self.narrate(says[i]):
                self.play(FadeIn(row), run_time=0.7)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ 2: lender of last resort
        self.heading("Two — the oldest job there is")
        bank = W.building(WAIT, size=0.7, kind="bank")
        St.place(bank, St.STAGE, ax=-0.6, ay=0.2)
        cb = cards.icon("bank", SRC_BR, 1.8)
        St.place(cb, St.SIDE, ay=0.5)
        arrow = W.flow_arrow(cb.get_left() + LEFT * 0.2, bank.get_right() + RIGHT * 0.3,
                             MONEY)
        terms = St.points(["at a penal rate", "against good collateral"],
                          colour=CHALK, dot_colour=MONEY, size=T_SMALL, width=20)
        St.place(terms, St.SIDE, ay=-0.55)
        with self.narrate("This one is the oldest job a central bank has, and it is not "
                          "really monetary policy at all. When a sound bank cannot "
                          "borrow simply because everyone has panicked, the central "
                          "bank lends to it — at a penal rate, and against good "
                          "collateral."):
            self.play(Create(bank), run_time=0.9)
            self.play(Create(cb), run_time=0.7)
            self.play(Create(arrow), run_time=0.6)
            self.play(S.flow_along(arrow, MONEY))
            self.play(FadeIn(terms), run_time=0.8)

        euro = VGroup(
            Text("over €1 trillion", font=FONT, font_size=T_SUB, color=TRIGGER),
            Text("two operations, late 2011 and early 2012", font=FONT,
                 font_size=T_TINY, color=MUTED),
            Text("three-year money", font=FONT, font_size=T_TINY, color=MUTED),
        ).arrange(DOWN, buff=0.18)
        St.place(euro, St.STAGE, ax=-0.1, ay=-0.72)
        with self.narrate("And in the euro area, two operations in late twenty-eleven "
                          "and early twenty-twelve lent over a trillion euros for three "
                          "years — aimed, their central bank argued, at repairing the "
                          "transmission mechanism itself."):
            self.play(FadeIn(euro), run_time=1.1)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ 3: the wedge again
        self.heading("Three — going straight at the wedge")
        wedge = DoubleArrow(LEFT * 1.6, RIGHT * 1.6, color=COST, stroke_width=6,
                            buff=0)
        St.place(wedge, St.STAGE, ay=0.85)
        wl = St.caption("banks looked risky, so what they charged stayed high",
                        COST, T_SMALL, width=30)
        wl.next_to(wedge, DOWN, buff=0.3)
        with self.narrate("The third group exists because of the wedge from an earlier "
                          "chapter. Banks looked risky, so their own funding was dear, "
                          "so what they charged households and firms stayed high."):
            self.play(GrowFromCenter(wedge), run_time=0.9)
            self.play(FadeIn(wl), run_time=0.7)

        g1 = VGroup(
            Text("£20bn", font=FONT, font_size=T_SUB, color=MONEY),
            St.caption("of bank debt guaranteed", MUTED, T_SMALL, width=20),
        ).arrange(DOWN, buff=0.2)
        St.place(g1, St.STAGE, ax=-0.55, ay=-0.6)
        with self.narrate("The first was a guarantee. The government stands behind up "
                          "to twenty billion pounds of bank debt, so an investor buying "
                          "it faces the same risk as buying a gilt. And the bank gets "
                          "that funding at a discount if it agrees to cut what it "
                          "charges smaller companies."):
            self.play(FadeIn(g1), run_time=1.0)

        small = St.caption("about 8% of a year's lending to small firms", SUNK,
                           T_SMALL, width=26)
        St.place(small, St.SIDE, ay=0.1)
        with self.narrate("Though twenty billion is only about eight per cent of a "
                          "year's lending to small firms by the largest banks. Limited "
                          "in scale, as the authors put it."):
            self.play(FadeIn(small), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the funding scheme
        self.heading("And one that pays you to lend")
        g2 = VGroup(
            Text("≈ £80bn", font=FONT, font_size=T_SUB, color=MONEY),
            St.caption("four-year funding, 5% of the loan book", MUTED,
                       T_SMALL, width=26),
        ).arrange(DOWN, buff=0.2)
        St.place(g2, St.SIDE, ay=0.7)
        with self.narrate("The second was bigger, and cleverer. Four-year funding, of "
                          "at least five per cent of a bank's existing loan book — "
                          "around eighty billion pounds across the eligible banks."):
            self.play(FadeIn(g2), run_time=1.0)

        b1 = W.Bar(0.35, color=MONEY, width=1.1)
        b2 = W.Bar(2.1, color=COST, width=1.1)
        pair = VGroup(b1, b2).arrange(RIGHT, buff=2.2, aligned_edge=DOWN)
        St.place(pair, St.FULL, ay=-0.05, fill=False)
        l1 = VGroup(Text("0.25%", font=FONT, font_size=T_BODY, color=MONEY),
                    St.caption("lending steady or growing", MUTED, T_SMALL, width=18)
                    ).arrange(DOWN, buff=0.16)
        l1.next_to(b1, DOWN, buff=0.24)
        l2 = VGroup(Text("1.5%", font=FONT, font_size=T_BODY, color=COST),
                    St.caption("lending shrinking by 5%", MUTED, T_SMALL, width=18)
                    ).arrange(DOWN, buff=0.16)
        l2.next_to(b2, DOWN, buff=0.24)
        base = Line(pair.get_left() + LEFT * 0.5, pair.get_right() + RIGHT * 0.5,
                    color=MUTED, stroke_width=2).move_to(pair.get_bottom())
        St.collapse_bars(pair)
        with self.narrate("And every extra pound a bank lent raised the amount it could "
                          "borrow under the scheme."):
            self.play(Create(base), run_time=0.5)
        with self.narrate("A bank holding its lending steady or growing it paid a "
                          "quarter of one per cent."):
            self.play(Restore(b1), FadeIn(l1), run_time=1.0)
        with self.narrate("A bank shrinking its lending by five per cent paid one and a "
                          "half — six times as much, on the whole amount."):
            self.play(Restore(b2), FadeIn(l2), run_time=1.3)
            self.play(S.flash_around(b2, COST))
        self.beat()

        self.close_chapter([
            "guidance: the rate path, held flat by announcement",
            "lending in a panic: penal rate, good collateral",
            "and schemes aimed straight at the wedge",
            "one of which charged 6× more for shrinking lending",
        ])
