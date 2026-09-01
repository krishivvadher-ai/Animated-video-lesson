import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter29(Chapter):
    CH = 29
    TITLE = "What banks cannot do with reserves"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["bank", "money", "slab", "risk"]

    def body(self):
        kit = stick.kit(scale=0.85)
        St.place(kit, St.STAGE, ax=-0.75, ay=-0.45)
        with self.narrate("There is a second way of telling the same story, and it "
                          "clears up the thing almost everybody gets wrong about this "
                          "policy. So it is worth four minutes.", v="c"):
            self.heading("The same story, told in money")
            self.play(FadeIn(kit), run_time=0.7)
        self.play(FadeOut(kit), run_time=0.4)

        # ------------------------------------------------ two kinds of money
        self.heading("Two different things both called money")
        narrow = VGroup(cards.icon("bank", SRC_BR, 1.7),
                        Text("narrow money", font=FONT, font_size=T_BODY, color=SRC_BR),
                        St.caption("reserves — banks only", MUTED, T_SMALL, width=20)
                        ).arrange(DOWN, buff=0.24)
        broad = VGroup(cards.icon("people", MONEY, 1.7),
                       Text("broad money", font=FONT, font_size=T_BODY, color=MONEY),
                       St.caption("deposits — everybody", MUTED, T_SMALL, width=20)
                       ).arrange(DOWN, buff=0.24)
        two = VGroup(narrow, broad).arrange(RIGHT, buff=2.4)
        St.place(two, St.FULL, ay=0.25)
        with self.narrate("Narrow money is reserves — the money banks hold at the "
                          "central bank. Nobody else can touch it."):
            self.play(FadeIn(narrow), run_time=1.0)
        with self.narrate("Broad money is deposits — the money in everybody else's bank "
                          "account. That is the one that gets spent."):
            self.play(FadeIn(broad), run_time=1.0)
        self.beat()

        which = St.caption("the policy runs through broad money", TRIGGER,
                           T_SUB, width=38)
        St.place(which, St.FOOT, pad=0.06)
        with self.narrate("And the transmission of this policy runs through broad "
                          "money. Not narrow money. The Bank of England has said so "
                          "explicitly."):
            self.play(FadeIn(which), run_time=0.8)
            self.play(S.flash_around(broad, MONEY))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the multiplier
        self.heading("The textbook says reserves multiply")
        one = W.Bar(0.55, color=SRC_BR, width=0.9)
        many = W.Bar(3.6, color=MUTED, width=0.9)
        got = W.Bar(0.52, color=MONEY, width=0.9)
        row = VGroup(one, many, got).arrange(RIGHT, buff=1.5, aligned_edge=DOWN)
        St.place(row, St.FULL, ay=0.25)
        labs = VGroup(
            Text("£1 of reserves", font=FONT, font_size=T_TINY, color=SRC_BR),
            Text("textbook: ×10 – 15", font=FONT, font_size=T_TINY, color=MUTED),
            Text("Britain: under ×1", font=FONT, font_size=T_TINY, color=MONEY))
        for i, l in enumerate(labs):
            l.next_to(row[i], DOWN, buff=0.24)
        base = Line(row.get_left() + LEFT * 0.4, row.get_right() + RIGHT * 0.4,
                    color=MUTED, stroke_width=2).move_to(row.get_bottom())
        St.collapse_bars(row)
        self.play(Create(base), run_time=0.5)
        with self.narrate("Put a pound of reserves into the system, says the textbook, "
                          "and broad money rises by ten or fifteen times as much."):
            self.play(Restore(one), FadeIn(labs[0]), run_time=0.8)
            self.play(Restore(many), FadeIn(labs[1]), run_time=1.3)
        with self.narrate("In Britain, it was less than one."):
            self.play(Restore(got), FadeIn(labs[2]), run_time=1.0)
            self.play(S.flash_around(got, MONEY))
        self.beat()

        # ------------------------------------------------ not a failure
        self.heading("And that is not the failure it looks like")
        fair = St.caption("their own theory predicts about one", TRIGGER,
                          T_SUB, width=36)
        St.place(fair, St.FOOT, pad=0.06)
        with self.narrate("And the authors say plainly that this is not evidence the "
                          "policy failed. On their own account, the right thing to "
                          "expect was about one, not fifteen. The failure of broad "
                          "money to explode is exactly what their theory predicts."):
            self.play(FadeIn(fair), run_time=0.9)
            self.play(FadeOut(labs[1]), FadeOut(many), run_time=0.7)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ where it leaked
        self.heading("And they say where it leaked away")
        pipe = Line(LEFT * 4.4, RIGHT * 3.6, color=MONEY, stroke_width=10)
        St.place(pipe, St.FULL, ay=0.72, fill=False)
        pl = Text("broad money: under +£200bn in the first round",
                  font=FONT, font_size=T_SMALL, color=MONEY)
        pl.next_to(pipe, UP, buff=0.45)
        with self.narrate("Broad money grew by less than two hundred billion pounds "
                          "during the first round."):
            self.play(Create(pipe), FadeIn(pl), run_time=1.1)

        leaks = [("banks swapped short deposits\nfor long-term debt", -2.2),
                 ("big firms issued bonds\ninstead of borrowing", 1.4)]
        for text, x in leaks:
            arrow = Arrow(pipe.get_center() + RIGHT * x,
                          pipe.get_center() + RIGHT * x + DOWN * 1.3,
                          color=COST, stroke_width=6, buff=0.05)
            cap = St.caption(text, COST, T_SMALL, width=22)
            cap.next_to(arrow, DOWN, buff=0.22)
            with self.narrate("Banks swapped short-term deposits for long-term debt."
                              if x < 0 else
                              "And large companies raised money by issuing bonds "
                              "instead of borrowing from banks. Both of those reduce "
                              "broad money."):
                self.play(GrowArrow(arrow), run_time=0.7)
                self.play(FadeIn(cap), run_time=0.7)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the myth
        self.heading("So: are the banks sitting on it?")
        banker = stick.StickFigure("a bank", WAIT, scale=0.9)
        St.place(banker, St.STAGE, ax=-0.7, ay=-0.3)
        pile = VGroup(*[W.coin(MONEY, 0.17) for _ in range(6)])
        pile.arrange_in_grid(2, 3, buff=0.14).next_to(banker, UP, buff=0.5)
        with self.narrate("You will hear it said that the banks are sitting on all that "
                          "money instead of lending it out."):
            self.play(FadeIn(banker), FadeIn(banker.label()), run_time=0.8)
            self.play(S.lag_map(GrowFromCenter, pile, lag=0.08), run_time=1.1)

        cant = St.caption("the banking system cannot do that", COST, T_SUB, width=30)
        St.place(cant, St.SIDE, ay=0.6)
        with self.narrate("The banking system cannot do that. The amount of reserves in "
                          "the system is decided by how the central bank chose to fund "
                          "its purchases — not by any bank's own decision."):
            self.play(FadeIn(cant), run_time=0.8)
            x = Cross(pile, stroke_color=COST, stroke_width=6)
            self.play(Create(x), run_time=0.8)

        arith = St.caption("arithmetic, not a choice", TRIGGER, T_BODY, width=22)
        St.place(arith, St.SIDE, ay=-0.2)
        with self.narrate("Reserves went up a lot because of how the purchases were "
                          "paid for. That is arithmetic, not a choice."):
            self.play(FadeIn(arith), run_time=0.8)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the one real route
        self.heading("There is one real route, and it is different")
        d = W.door(MONEY, w=1.2, h=2.2, label="cheaper funding\nfor the bank")
        St.place(d, St.STAGE, ax=-0.35, ay=-0.1)
        route = St.caption("changes the bank's own\nincentive to lend", MONEY,
                           T_BODY, width=22)
        St.place(route, St.SIDE, ay=0.3)
        with self.narrate("The only way more reserves can lead to more lending is if "
                          "they change a bank's incentive to lend — for instance by "
                          "making the bank's own funding cheaper."):
            self.play(Create(d), run_time=1.0)
            self.play(FadeIn(route), run_time=0.8)
        diff = St.caption("which is a different mechanism", MUTED, T_SUB, width=30)
        St.place(diff, St.FOOT, pad=0.06)
        with self.narrate("Which is a completely different mechanism."):
            self.play(FadeIn(diff), run_time=0.8)
        self.beat()

        self.close_chapter([
            "narrow money is reserves; broad money is deposits",
            "the policy runs through broad money",
            "the multiplier was under one — as predicted",
            "banks cannot choose the quantity of reserves",
        ])
