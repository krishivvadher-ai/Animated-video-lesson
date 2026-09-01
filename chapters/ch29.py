import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter29(Chapter):
    CH = 29
    TITLE = "Why cutting the rate was not enough"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["bank", "risk", "lever", "clock"]

    def body(self):
        # ------------------------------------------------ the wedge
        self.heading("Where the rate is supposed to travel")
        gov = stick.governor(scale=0.75)
        St.place(gov, St.STAGE, ax=-0.85, ay=0.05)
        bank = VGroup(cards.icon("bank", CHALK, 2.4),
                      Text("a bank", font=FONT, font_size=T_SMALL, color=MUTED))
        bank[1].next_to(bank[0], DOWN, buff=0.25)
        St.place(bank, St.STAGE, ax=0.0, ay=0.05)
        firm = W.factory(CHALK, 0.5, "a firm")
        St.place(firm, St.STAGE, ax=0.85, ay=0.05)
        self.play(FadeIn(gov), FadeIn(bank), FadeIn(firm), run_time=1.0)

        a1 = W.flow_arrow(gov.get_right() + RIGHT * 0.25, bank.get_left() + LEFT * 0.25,
                          MONEY)
        a2 = W.flow_arrow(bank.get_right() + RIGHT * 0.25, firm.get_left() + LEFT * 0.25,
                          MONEY)
        with self.narrate("In normal times the Bank's rate travels down this line, "
                          "through a bank, and comes out as the rate an ordinary firm "
                          "pays."):
            self.play(Create(a1), run_time=0.8)
            self.play(S.flow_along(a1, MONEY))
            self.play(Create(a2), run_time=0.8)
            self.play(S.flow_along(a2, MONEY))
        with self.narrate("Then, in two thousand and seven and eight, banks stopped "
                          "trusting each other. Lenders would provide funds to a bank "
                          "only at a much higher price — if at all."):
            self.play(a2.animate.set_color(COST), run_time=1.0)
        gapline = DoubleArrow(bank.get_right() + RIGHT * 0.3 + DOWN * 1.5,
                              firm.get_left() + LEFT * 0.3 + DOWN * 1.5,
                              color=COST, buff=0, stroke_width=5)
        with self.narrate("A wedge opened up. The Bank's rate went down. The rate a "
                          "firm actually paid did not follow it."):
            self.play(GrowFromCenter(gapline), run_time=0.9)
        self.define("credit spread", "The wedge between the Bank's rate and the rate a "
                    "firm pays.", "risk", COST, at=UP * 1.7, hold=4.4)
        self.clear_stage()

        # ------------------------------------------------ the cuts
        self.heading("So they cut, and cut, and cut")
        ax = Axes(x_range=[0, 6, 1], y_range=[0, 6, 1], x_length=8.0, y_length=3.4,
                  axis_config=AXIS)
        St.place(ax, St.STAGE, ay=-0.05, fill=False)
        yl = Text("the Bank's rate", font=FONT, font_size=T_SMALL, color=MONEY)
        yl.rotate(PI / 2).next_to(ax, LEFT, buff=0.18)
        xl = Text("2008                    2009", font=FONT, font_size=T_TINY,
                  color=MUTED)
        xl.next_to(ax, DOWN, buff=0.2)
        self.play(Create(ax), FadeIn(yl), FadeIn(xl), run_time=1.0)

        segs = [([0, 2.4], [5, 5], "On the eighth of October two thousand and eight, "
                 "central banks in Canada, China, the euro area, Sweden, Switzerland, "
                 "the United Kingdom and the United States all cut on the same day."),
                ([2.4, 3.8], [5, 2], "In Britain, the Bank cut its rate by three "
                 "percentage points in the last three months of that year."),
                ([3.8, 4.8], [2, 0.5], "And by a further one and a half percentage "
                 "points in the first three months of two thousand and nine."),
                ([4.8, 6], [0.5, 0.5], "And there it stopped, at nought point five per "
                 "cent.")]
        for xs, ys, say in segs:
            g = ax.plot_line_graph(x_values=xs, y_values=ys, line_color=MONEY,
                                   add_vertex_dots=False, stroke_width=5)
            with self.narrate(say):
                self.play(Create(g), run_time=1.4)
        self.beat()

        floor = DashedLine(ax.c2p(0, 0), ax.c2p(6, 0), color=COST, stroke_width=4)
        fl = Text("zero", font=FONT, font_size=T_SMALL, color=COST)
        fl.next_to(floor, RIGHT, buff=0.2)
        note = St.caption("0.5%, not zero", COST, T_SUB, width=16)
        St.place(note, St.SIDE, ay=0.5)
        with self.narrate("And note that they stopped just above zero, not at it — "
                          "because of worries about what extremely low rates would do "
                          "to banks' own profits, and to the working of the money "
                          "markets themselves."):
            self.play(Create(floor), FadeIn(fl), run_time=0.8)
            self.play(FadeIn(note), run_time=0.7)
        self.beat()
        self.play(FadeOut(note), run_time=0.4)
        self.define("the zero lower bound", "The point where a central bank cannot cut "
                    "any further.", "lever", COST, at=UP * 1.7, hold=4.0)
        self.clear_stage()

        # ------------------------------------------------ what is left
        self.heading("What is left when the lever is down")
        boxes = VGroup(
            VGroup(cards.icon("bank", MONEY, 2.0),
                   St.caption("lend to banks short of cash", MONEY, T_SMALL, width=14)),
            VGroup(cards.icon("ticket", TRIGGER, 2.0),
                   St.caption("buy assets with new money", TRIGGER, T_SMALL, width=14)),
            VGroup(cards.icon("signal", WAIT, 2.0),
                   St.caption("say what you intend to do", WAIT, T_SMALL, width=14)),
        )
        for g in boxes:
            g.arrange(DOWN, buff=0.4)
        boxes.arrange(RIGHT, buff=1.6)
        St.place(boxes, St.FULL, ay=0.25)
        says = ["They could lend to banks that were short of cash — the oldest job a "
                "central bank has.",
                "They could buy assets with money they created. That is the one this "
                "film is about, and the next chapter builds it.",
                "Or they could simply say something about what they intended to do in "
                "future — which turns out to matter more than you would think."]
        for i, g in enumerate(boxes):
            with self.narrate(says[i]):
                self.play(FadeIn(g), run_time=0.9)
        with self.narrate("All of that together goes by one name. Unconventional "
                          "monetary policy."):
            self.foot("unconventional monetary policy", CHALK)
        self.beat()

        self.close_chapter([
            "lenders would fund banks only dearly",
            "a credit spread opened up",
            "cut 3 points, then 1.5 — stop at 0.5",
            "what is left: unconventional policy",
        ])
