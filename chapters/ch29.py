import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.theme import *


class Chapter29(Chapter):
    CH = 29
    TITLE = "Money, and what banks can’t do with reserves"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["money", "bank", "flow", "people"]

    def body(self):
        with self.narrate("There is a second way of telling the same story, and it "
                          "clears up the thing almost everybody gets wrong about this "
                          "policy. So it is worth four minutes."):
            pass

        # ---------------------------------------------------- two kinds of money
        head = cards.section_title("Two kinds of money, and they are not the same", color=CHALK, size=T_SUB)
        self.play(FadeIn(head), run_time=0.5)

        narrow = VGroup(
            RoundedRectangle(width=3.6, height=2.0, corner_radius=0.14, color=SRC_BR,
                             stroke_width=3),
            cards.body("NARROW MONEY\nreserves banks hold at the central bank",
                       size=T_SMALL, color=SRC_BR, width=20))
        narrow[1].move_to(narrow[0].get_center())
        broad = VGroup(
            RoundedRectangle(width=3.6, height=2.0, corner_radius=0.14, color=MONEY,
                             stroke_width=3),
            cards.body("BROAD MONEY\ndeposits held by everybody else",
                       size=T_SMALL, color=MONEY, width=20))
        broad[1].move_to(broad[0].get_center())
        pair = VGroup(narrow, broad).arrange(RIGHT, buff=1.6).move_to(UP * 0.8)
        with self.narrate("Narrow money is reserves — the money banks hold at the "
                          "central bank. Nobody else can touch it."):
            self.play(FadeIn(narrow), run_time=0.9)
        with self.narrate("Broad money is deposits — the money in everybody else's bank "
                          "account. That is the one that gets spent."):
            self.play(FadeIn(broad), run_time=0.9)
        self.beat()

        which = cards.body("broad money, not narrow",
                           size=T_SUB, color=MONEY, width=40)
        which.move_to(DOWN * 1.5)
        with self.narrate("And the transmission of this policy runs through broad "
                          "money. Not narrow money. The Bank of England has said so "
                          "explicitly."):
            self.play(FadeIn(which), run_time=1.0)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- the money multiplier
        head2 = cards.section_title("The textbook picture, and why it does not apply", color=COST, size=T_SUB)
        self.play(FadeIn(head2), run_time=0.5)

        small = Rectangle(width=1.0, height=0.7, color=SRC_BR, stroke_width=3,
                          fill_color=SRC_BR, fill_opacity=0.25).move_to(LEFT * 4.0)
        sl = Text("reserves", font=FONT, font_size=T_SMALL, color=SRC_BR)
        sl.next_to(small, DOWN, buff=0.2)
        big = Rectangle(width=1.0, height=5.0, color=MONEY, stroke_width=3,
                        fill_color=MONEY, fill_opacity=0.25)
        big.move_to(LEFT * 1.2).align_to(small, DOWN)
        bl = Text("broad money", font=FONT, font_size=T_SMALL, color=MONEY)
        bl.next_to(big, DOWN, buff=0.2)
        mult = Text("× 10 to 15", font=FONT, font_size=T_SUB, color=COST)
        mult.next_to(big, RIGHT, buff=0.5)
        with self.narrate("The textbook says that reserves multiply. Put a pound of "
                          "reserves into the system and broad money rises by ten or "
                          "fifteen times as much."):
            self.play(FadeIn(small), FadeIn(sl), run_time=0.7)
            self.play(GrowFromEdge(big, DOWN), FadeIn(bl), FadeIn(mult), run_time=1.6)
        self.beat()

        real = Rectangle(width=1.0, height=0.6, color=MONEY, stroke_width=3,
                         fill_color=MONEY, fill_opacity=0.25)
        real.move_to(RIGHT * 3.0).align_to(small, DOWN)
        rl = cards.body("actually: less than one",
                        size=T_SMALL, color=MONEY, width=16)
        rl.next_to(real, DOWN, buff=0.2)
        with self.narrate("In Britain, it was less than one."):
            self.play(FadeIn(real), FadeIn(rl), run_time=1.0)
        self.beat()
        notfail = cards.body("under one is what the theory predicts",
                             size=T_BODY, color=SRC_BR, width=44)
        notfail.to_edge(DOWN, buff=0.62)
        with self.narrate("And the authors say plainly that this is not evidence the "
                          "policy failed. On their own account, the right thing to "
                          "expect was about one, not fifteen. The failure of broad "
                          "money to explode is exactly what their theory predicts."):
            self.play(FadeIn(notfail), run_time=1.2)
        self.beat()
        leak = cards.body("broad money grew < £200bn — the leaks",
                          size=T_BODY, color=CHALK, width=46)
        leak.to_edge(DOWN, buff=0.62)
        with self.narrate("They also explain where it leaked away. Broad money grew by "
                          "less than two hundred billion pounds during the first round. "
                          "Banks swapped short-term deposits for long-term debt. And "
                          "large companies raised money by issuing bonds instead of "
                          "borrowing from banks. Both of those reduce broad money."):
            self.play(FadeOut(notfail), FadeIn(leak), run_time=1.4)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- reserves cannot be lent out
        head3 = cards.section_title("And the thing everybody says, which is simply wrong", color=COST, size=T_SUB)
        self.play(FadeIn(head3), run_time=0.5)

        claim = cards.body("“The banks are sitting on all that money instead of lending "
                           "it out.”", size=T_SUB, color=COST, width=34)
        claim.move_to(UP * 1.5)
        with self.narrate("You will hear it said that the banks are sitting on all that "
                          "money instead of lending it out."):
            self.play(FadeIn(claim), run_time=0.9)
        self.beat()

        pot = VGroup(
            Circle(radius=1.3, color=SRC_BR, stroke_width=4, fill_color=SRC_BR,
                   fill_opacity=0.18),
            Text("reserves", font=FONT, font_size=T_SMALL, color=SRC_BR))
        pot[1].move_to(pot[0].get_center())
        pot.move_to(LEFT * 3.0 + DOWN * 0.5)
        out = Arrow(pot.get_right() + RIGHT * 0.2, RIGHT * 1.4 + DOWN * 0.5,
                    color=COST, buff=0, stroke_width=6)
        cross = VGroup(
            Line(LEFT * 0.4 + UP * 0.4, RIGHT * 0.4 + DOWN * 0.4, color=COST, stroke_width=7),
            Line(LEFT * 0.4 + DOWN * 0.4, RIGHT * 0.4 + UP * 0.4, color=COST, stroke_width=7),
        ).move_to(RIGHT * 0.2 + DOWN * 0.5)
        with self.narrate("The banking system cannot do that. The amount of reserves in "
                          "the system is decided by how the central bank chose to fund "
                          "its purchases — not by any bank's own decision."):
            self.play(FadeIn(pot), run_time=0.8)
            self.play(Create(out), run_time=0.8)
            self.play(FadeIn(cross), run_time=0.6)
        self.beat()
        arith = cards.body("arithmetic, not a choice",
                           size=T_SUB, color=CHALK, width=30)
        arith.move_to(RIGHT * 3.4 + UP * 0.4)
        with self.narrate("Reserves went up a lot because of how the purchases were "
                          "paid for. That is arithmetic, not a choice."):
            self.play(FadeIn(arith), run_time=1.0)
        self.beat()
        only = cards.body("only via the incentive to lend",
                          size=T_BODY, color=MONEY, width=46)
        only.to_edge(DOWN, buff=0.62)
        with self.narrate("The only way more reserves can lead to more lending is if "
                          "they change a bank's incentive to lend — for instance by "
                          "making the bank's own funding cheaper. Which is a completely "
                          "different mechanism."):
            self.play(FadeIn(only), run_time=1.2)
        self.beat()

        self.close_chapter([
            "narrow = reserves · broad = deposits",
            "multiplier: under one",
            "predicted — not a failure",
            "reserves cannot be lent out",
        ])
