import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.theme import *


class Chapter18(Chapter):
    CH = 18
    TITLE = "Why cutting the rate was not enough"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["bank", "risk", "lever", "clock"]

    def body(self):
        # ---------------------------------------------------- the wedge
        with self.narrate("Before the new policy, you need to see exactly what went "
                          "wrong with the old one. And it is one picture."):
            pass

        gov = stick.governor(scale=0.75).move_to(LEFT * 5.4 + DOWN * 0.2)
        bank = VGroup(cards.icon("bank", CHALK, 2.4),
                      Text("a bank", font=FONT, font_size=T_SMALL, color=MUTED))
        bank[1].next_to(bank[0], DOWN, buff=0.25)
        bank.move_to(LEFT * 1.4 + DOWN * 0.2)
        firm = W.factory(CHALK, 0.55, "a firm").move_to(RIGHT * 4.4 + DOWN * 0.2)
        self.play(FadeIn(gov), FadeIn(bank), FadeIn(firm), run_time=1.0)

        a1 = W.flow_arrow(gov.get_right() + RIGHT * 0.3, bank.get_left() + LEFT * 0.3, MONEY)
        t1 = Text("the Bank's rate", font=FONT, font_size=T_SMALL, color=MONEY)
        t1.next_to(a1, UP, buff=0.16)
        a2 = W.flow_arrow(bank.get_right() + RIGHT * 0.3, firm.get_left() + LEFT * 0.3, MONEY)
        t2 = Text("the rate a firm pays", font=FONT, font_size=T_SMALL, color=MONEY)
        t2.next_to(a2, UP, buff=0.16)
        with self.narrate("In normal times the Bank's rate travels down this line, "
                          "through a bank, and comes out as the rate an ordinary firm "
                          "pays."):
            self.play(Create(a1), FadeIn(t1), run_time=0.8)
            self.play(Create(a2), FadeIn(t2), run_time=0.8)

        with self.narrate("Then, in two thousand and seven and eight, banks stopped "
                          "trusting each other. Lenders would provide funds to a bank "
                          "only at a much higher price — if at all."):
            self.play(a2.animate.set_color(COST), t2.animate.set_color(COST), run_time=1.0)

        gapline = DoubleArrow(bank.get_right() + RIGHT * 0.4 + DOWN * 1.3,
                              firm.get_left() + LEFT * 0.4 + DOWN * 1.3,
                              color=COST, buff=0, stroke_width=5)
        self.play(Create(gapline), run_time=0.8)
        self.define("credit spread", "The wedge between the central bank's rate and the "
                    "rate a household or a firm actually pays.", "risk", COST,
                    at=UP * 2.1, hold=4.6)

        wedge = cards.body("the wedge opens", size=T_SUB, color=COST, width=30)
        wedge.move_to(UP * 2.0)
        with self.narrate("A wedge opened up. The Bank's rate went down. The rate a "
                          "firm actually paid did not follow it."):
            self.play(FadeIn(wedge), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- the cuts
        head = Text("So they cut, and cut, and cut", font=FONT, font_size=T_SUB,
                    color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)

        ax = Axes(x_range=[0, 6, 1], y_range=[0, 6, 1], x_length=8.0, y_length=3.6,
                  axis_config={"color": MUTED, "stroke_width": 2,
                               "include_ticks": False, "include_tip": False})
        ax.shift(DOWN * 0.6)
        yl = Text("the Bank's rate", font=FONT, font_size=T_SMALL, color=MONEY)
        yl.next_to(ax, LEFT, buff=0.2).rotate(PI / 2)
        xl = Text("2008                                     2009", font=FONT,
                  font_size=T_SMALL, color=MUTED)
        xl.next_to(ax, DOWN, buff=0.2)
        self.play(Create(ax), FadeIn(yl), FadeIn(xl), run_time=1.0)

        path1 = ax.plot_line_graph(x_values=[0, 2.4], y_values=[5, 5],
                                   line_color=MONEY, add_vertex_dots=False, stroke_width=5)
        path2 = ax.plot_line_graph(x_values=[2.4, 3.8], y_values=[5, 2],
                                   line_color=MONEY, add_vertex_dots=False, stroke_width=5)
        path3 = ax.plot_line_graph(x_values=[3.8, 4.8], y_values=[2, 0.5],
                                   line_color=MONEY, add_vertex_dots=False, stroke_width=5)
        path4 = ax.plot_line_graph(x_values=[4.8, 6], y_values=[0.5, 0.5],
                                   line_color=MONEY, add_vertex_dots=False, stroke_width=5)

        with self.narrate("On the eighth of October two thousand and eight, central "
                          "banks in Canada, China, the euro area, Sweden, Switzerland, "
                          "the United Kingdom and the United States all cut their rates "
                          "on the same day."):
            self.play(Create(path1), run_time=1.0)
        with self.narrate("In Britain, the Bank cut its rate by three percentage points "
                          "in the last three months of two thousand and eight."):
            self.play(Create(path2), run_time=1.6)
        with self.narrate("And by a further one and a half percentage points in the "
                          "first three months of two thousand and nine."):
            self.play(Create(path3), run_time=1.4)
        with self.narrate("And there it stopped, at nought point five per cent."):
            self.play(Create(path4), run_time=1.0)
        self.beat()

        floor = DashedLine(ax.c2p(0, 0), ax.c2p(6, 0), color=COST, stroke_width=4)
        fl = Text("zero", font=FONT, font_size=T_SMALL, color=COST)
        fl.next_to(floor, RIGHT, buff=0.2)
        self.play(Create(floor), FadeIn(fl), run_time=0.8)

        note = cards.body("0.5%, not zero",
                          size=T_BODY, color=MUTED, width=44)
        note.to_edge(DOWN, buff=0.4)
        with self.narrate("And note that they stopped just above zero, not at it. "
                          "Because of worries about what extremely low rates would do "
                          "to banks' own profits, and to the working of the money "
                          "markets themselves."):
            self.play(FadeIn(note), run_time=1.0)
        self.beat()
        self.define("the zero lower bound", "The point where a central bank cannot cut "
                    "its rate any further.", "lever", COST, at=UP * 1.6, hold=4.0)

        # ---------------------------------------------------- what was left
        self.clear_stage()
        head2 = Text("So what is left when the lever is on the floor?",
                     font=FONT, font_size=T_SUB, color=CHALK).to_edge(UP, buff=0.8)
        self.play(FadeIn(head2), run_time=0.5)

        boxes = VGroup(
            VGroup(cards.icon("bank", MONEY, 2.0),
                   cards.body("lend to banks that are short of cash", size=T_SMALL,
                              color=MONEY, width=16)),
            VGroup(cards.icon("ticket", TRIGGER, 2.0),
                   cards.body("buy assets with newly created money", size=T_SMALL,
                              color=TRIGGER, width=16)),
            VGroup(cards.icon("signal", WAIT, 2.0),
                   cards.body("say something about the future", size=T_SMALL,
                              color=WAIT, width=16)),
        )
        for g in boxes:
            g.arrange(DOWN, buff=0.4)
        boxes.arrange(RIGHT, buff=1.6).shift(DOWN * 0.2)
        says = ["lend to banks short of cash",
                "buy assets with new money",
                "say what you intend to do"]
        for i in range(3):
            with self.narrate(says[i]):
                self.play(FadeIn(boxes[i]), run_time=0.9)
        self.beat()
        name = cards.body("unconventional monetary policy",
                          size=T_SUB, color=CHALK, width=44)
        name.to_edge(DOWN, buff=0.6)
        with self.narrate("All of that together goes by one name. Unconventional "
                          "monetary policy."):
            self.play(FadeIn(name), run_time=0.9)
        self.beat()

        self.close_chapter([
            "lenders would fund banks only dearly",
            "a credit spread opened up",
            "cut 3 points, then 1.5 — stop at 0.5",
            "what is left: unconventional policy",
        ])
