import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter14(Chapter):
    CH = 14
    TITLE = "When this is wrong"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["door", "people", "fog", "risk"]

    def body(self):
        with self.narrate("Being honest about the limits is part of the teaching, and "
                          "it also stops you over-applying the idea. The paper sets out "
                          "four qualifications.", hold=True):
            pass

        # ---------------------------------------------------- 1 the race
        self.heading("One — the race")
        nell = stick.nell(scale=0.95)
        St.place(nell, St.STAGE, ax=-0.7, ay=-0.2)
        d = W.door(MONEY, 1.3, 2.6, "one site, one licence")
        St.place(d, St.STAGE, ax=0.35, ay=-0.05)
        with self.narrate("Everything so far assumed the chance was Nell's alone. "
                          "Suppose it is not. Suppose there is one site, or one licence, "
                          "and several firms want it."):
            self.play(FadeIn(nell), Create(d), run_time=1.2)

        rival = stick.StickFigure("a rival", CHALK, scale=0.95)
        rival.move_to(St.SIDE.point(0.7, -0.2))
        with self.narrate("Nell hesitates, sensibly, to see how things develop."):
            self.play(nell.pace(1, run_time=1.8))
            self.play(nell.mood("thinking"), run_time=0.4)
        with self.narrate("And somebody else walks through the door."):
            self.play(FadeIn(rival), run_time=0.5)
            self.play(rival.walk_to(d.get_center() + RIGHT * 0.2, run_time=2.0))
            self.play(FadeOut(rival), nell.mood("surprised"), run_time=0.6)
        with self.narrate("When the chance can be snatched, waiting is not possible. "
                          "And when waiting is not possible, the textbook's trigger is "
                          "valid again. This is a real limit, and Part Three comes back "
                          "to it."):
            self.foot("waiting impossible → the textbook is right", COST)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- 2 first mover
        self.heading("Two — moving first can pay")
        pull = VGroup(
            Arrow(LEFT * 3.4, LEFT * 0.6, color=WAIT, buff=0, stroke_width=6),
            Arrow(RIGHT * 3.4, RIGHT * 0.6, color=MONEY, buff=0, stroke_width=6))
        St.place(pull, St.FULL, ay=0.35)
        l1 = Text("information says: wait", font=FONT, font_size=T_BODY, color=WAIT)
        l1.next_to(pull[0], DOWN, buff=0.4)
        l2 = Text("being first says: go now", font=FONT, font_size=T_BODY, color=MONEY)
        l2.next_to(pull[1], DOWN, buff=0.4)
        with self.narrate("Sometimes moving first has a value of its own — you take the "
                          "best position, and everyone else has to work around you. "
                          "That pulls the other way."):
            self.play(GrowArrow(pull[0]), FadeIn(l1), run_time=0.9)
            self.play(GrowArrow(pull[1]), FadeIn(l2), run_time=0.9)
        with self.narrate("The right answer balances the two against each other."):
            self.foot("the right answer balances the two", CHALK)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- 3 watching
        self.heading("Three — firms watching each other")
        crowd = stick.crowd(6, spacing=1.6, scale=0.55)
        St.place(crowd, St.FULL, ay=-0.2)
        with self.narrate("Six firms, each looking at the same opportunity, each with "
                          "slightly different information about it."):
            self.play(S.lag_map(FadeIn, crowd, lag=0.15), run_time=1.4)
        with self.narrate("Each one looks around, sees that nobody else has moved, and "
                          "concludes the others must have found something discouraging. "
                          "So each revises its own view downwards."):
            self.play(*[f.mood("thinking") for f in crowd], run_time=0.7)
            self.play(*[f.mood("worried") for f in crowd], run_time=0.7)
        with self.narrate("And so everybody waits. Not because the opportunity is bad, "
                          "but because everybody is reading everybody else's silence."):
            self.foot("everybody waits", MUTED)
        self.beat()
        with self.narrate("Then one of them moves."):
            self.play(crowd[2].animate.shift(UP * 1.1), crowd[2].mood("pleased"),
                      run_time=0.9)
        with self.narrate("And now everybody revises upwards — because that firm must "
                          "have seen something good. Investment arrives in a sudden "
                          "bunch. Which is why it comes in waves."):
            self.play(*[f.mood("pleased") for f in crowd], run_time=0.6)
            self.play(LaggedStart(*[f.animate.shift(UP * 1.1)
                                    for i, f in enumerate(crowd) if i != 2],
                                  lag_ratio=0.12), run_time=1.6)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- 4 bad news
        self.heading("Four — the bad news principle")
        q = cards.quote_card(
            "of possible future outcomes, only the unfavorable ones have a bearing on "
            "the current propensity to undertake a given project",
            "Dixit (1992), p. 118, quoting Bernanke (1983)", TRIGGER, width=42)
        St.place(q, St.FULL, ay=0.72, fill=False)
        with self.narrate("This one comes with a quotation, because it is the single "
                          "idea Part Three leans on hardest. Dixit is quoting Bernanke."):
            self.play(FadeIn(q), run_time=1.2)
        self.beat()
        plain = St.caption("when you can wait, the bad futures decide", CHALK, T_SUB,
                           width=44)
        St.place(plain, St.FULL, ay=-0.72)
        with self.narrate("In plain words. When you can wait, it is mainly the bad "
                          "possible futures that decide whether you build now."):
            self.play(FadeIn(plain), run_time=0.9)
        self.beat()
        with self.narrate("Because the good futures will still be there next year. You "
                          "have not missed them. Waiting only ever protects you from "
                          "the bad ones."):
            self.foot("waiting only guards against bad news", MONEY)
        self.beat()

        self.play(FadeOut(q), FadeOut(plain), run_time=0.6)
        qual = St.points(["the total chance still matters",
                          "the shape of the good outcomes does not"],
                         colour=CHALK, dot_colour=TRIGGER, size=T_SUB, width=34)
        St.place(qual, St.FULL, ay=0.25)
        says = ["Carry the qualification the paper adds in the very next sentence, "
                "because dropping it changes the meaning. The total chance of ending up "
                "above the trigger does still matter.",
                "What does not matter is the shape of the good outcomes beyond it. "
                "Those are not the same thing, and Part Three needs the difference."]
        for i, row in enumerate(qual):
            with self.narrate(says[i]):
                self.play(FadeIn(row), run_time=0.9)
        self.beat()

        self.close_chapter([
            "a race → waiting is impossible, textbook right",
            "moving first can pull the other way",
            "inaction reads as bad news → bunching",
            "the bad news principle, with its qualification",
        ])
