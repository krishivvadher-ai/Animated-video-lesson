import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.theme import *


class Chapter09(Chapter):
    CH = 9
    TITLE = "When this is wrong"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ['door', 'people', 'fog', 'risk']

    def body(self):
        with self.narrate("Being honest about the limits is part of the teaching, and "
                          "it also stops you over-applying the idea. The paper sets out "
                          "four qualifications, and every one of them matters."):
            pass

        # ------------------------------------------------------- 1 the race
        head = Text("One — the race", font=FONT, font_size=T_SUB, color=COST)
        head.to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)

        nell = stick.nell(scale=0.95).shift(LEFT * 3.4 + DOWN * 0.9)
        d = W.door(MONEY, 1.3, 2.6, "one site, one licence").move_to(RIGHT * 1.4 + DOWN * 0.3)
        with self.narrate("Everything so far assumed the chance was Nell's alone. "
                          "Suppose it is not. Suppose there is one site, or one licence, "
                          "and several firms want it."):
            self.play(FadeIn(nell), Create(d), run_time=1.1)

        rival = stick.StickFigure("a rival", CHALK, scale=0.95).shift(RIGHT * 5.6 + DOWN * 0.9)
        with self.narrate("Nell hesitates, sensibly, to see how things develop."):
            self.play(nell.pace(1, run_time=2.0))
            self.play(nell.mood("thinking"), run_time=0.4)
        with self.narrate("And somebody else walks through the door."):
            self.play(FadeIn(rival), run_time=0.5)
            self.play(rival.walk_to(RIGHT * 1.4 + DOWN * 0.9, run_time=2.0))
            self.play(FadeOut(rival), nell.mood("surprised"), run_time=0.6)

        v = cards.body("waiting impossible → textbook valid", size=T_SUB, color=CHALK, width=30)
        v.to_edge(DOWN, buff=0.8)
        with self.narrate("When the chance can be snatched, waiting is no longer "
                          "possible. And when waiting is not possible, the textbook's "
                          "trigger is valid again. This is a real limit, and we will "
                          "come back to it in Part Two."):
            self.play(FadeIn(v), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------------- 2 first mover
        head2 = Text("Two — moving first can be worth something",
                     font=FONT, font_size=T_SUB, color=MONEY).to_edge(UP, buff=0.7)
        self.play(FadeIn(head2), run_time=0.5)
        pull = VGroup(
            Arrow(LEFT * 3.6, LEFT * 0.5, color=WAIT, buff=0, stroke_width=6),
            Arrow(RIGHT * 3.6, RIGHT * 0.5, color=MONEY, buff=0, stroke_width=6))
        l1 = cards.body("information says: wait", size=T_BODY, color=WAIT, width=18)
        l1.next_to(pull[0], DOWN, buff=0.4)
        l2 = cards.body("being first says: go now", size=T_BODY, color=MONEY, width=18)
        l2.next_to(pull[1], DOWN, buff=0.4)
        with self.narrate("Sometimes moving first has a value of its own — you take the "
                          "best position, and everyone else has to work around you. "
                          "That pulls the other way."):
            self.play(Create(pull), FadeIn(l1), FadeIn(l2), run_time=1.3)
        bal = cards.body("The right answer balances the two.", size=T_SUB,
                         color=CHALK, width=30)
        bal.to_edge(DOWN, buff=0.9)
        with self.narrate("The right answer balances the two against each other."):
            self.play(FadeIn(bal), run_time=0.7)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------------- 3 watching
        head3 = Text("Three — firms watching each other",
                     font=FONT, font_size=T_SUB, color=WAIT).to_edge(UP, buff=0.7)
        self.play(FadeIn(head3), run_time=0.5)
        crowd = stick.crowd(6, spacing=1.5, scale=0.55).shift(DOWN * 0.6)
        with self.narrate("Six firms, each looking at the same opportunity, each with "
                          "slightly different information about it."):
            self.play(FadeIn(crowd), run_time=0.9)
        with self.narrate("Each one looks around, sees that nobody else has moved, and "
                          "concludes that the others must have found something "
                          "discouraging. So each one revises its own view downwards."):
            self.play(*[f.mood("thinking") for f in crowd], run_time=0.8)
            self.play(*[f.mood("worried") for f in crowd], run_time=0.8)
        st = Text("everybody waits", font=FONT, font_size=T_SUB, color=MUTED)
        st.next_to(crowd, DOWN, buff=0.8)
        with self.narrate("And so everybody waits. Not because the opportunity is bad, "
                          "but because everybody is reading everybody else's silence."):
            self.play(FadeIn(st), run_time=0.7)
        self.beat()
        with self.narrate("Then one of them moves."):
            self.play(crowd[2].animate.shift(UP * 1.0), crowd[2].mood("pleased"),
                      run_time=0.9)
        with self.narrate("And now everybody revises upwards — because that firm must "
                          "have seen something good. Investment arrives in a sudden bunch."):
            self.play(*[f.mood("pleased") for f in crowd], run_time=0.6)
            self.play(*[f.animate.shift(UP * 1.0) for i, f in enumerate(crowd) if i != 2],
                      run_time=1.1)
        wave = cards.body("Which is why investment comes in waves.", size=T_SUB,
                          color=CHALK, width=30)
        wave.to_edge(DOWN, buff=0.7)
        self.play(FadeOut(st), FadeIn(wave), run_time=0.7)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------------- 4 bad news
        head4 = Text("Four — the bad news principle",
                     font=FONT, font_size=T_SUB, color=TRIGGER).to_edge(UP, buff=0.7)
        self.play(FadeIn(head4), run_time=0.5)
        qc = cards.quote_card(
            "of possible future outcomes, only the unfavorable ones have a bearing on "
            "the current propensity to undertake a given project",
            "Dixit (1992), p. 118, quoting Bernanke (1983)", TRIGGER, width=42)
        qc.move_to(UP * 0.9)
        if qc.width > 11.5:
            qc.scale(11.5 / qc.width)
        with self.narrate("This one comes with a quotation, because it is the single "
                          "idea Part Two leans on hardest. Dixit is quoting Bernanke."):
            self.play(FadeIn(qc), run_time=1.0)
        self.beat()
        plain = cards.body("the bad futures decide",
                           size=T_BODY, color=CHALK, width=44)
        plain.next_to(qc, DOWN, buff=0.9)
        with self.narrate("In plain words. When you can wait, it is mainly the bad "
                          "possible futures that decide whether you build now."):
            self.play(FadeIn(plain), run_time=0.9)
        self.beat()
        why = cards.body("good futures keep · waiting guards the bad ones",
                         size=T_BODY, color=MONEY, width=44)
        why.next_to(plain, DOWN, buff=0.6)
        with self.narrate("Because the good futures will still be there next year. You "
                          "have not missed them. Waiting only ever protects you from "
                          "the bad ones."):
            self.play(FadeIn(why), run_time=0.9)
        self.beat()

        self.play(FadeOut(qc), FadeOut(plain), FadeOut(why), run_time=0.6)
        qual = cards.body("total chance: matters\nshape of the good ones: does not",
                          size=T_BODY, color=CHALK, width=42)
        qual.move_to(UP * 0.4)
        with self.narrate("And carry the qualification the paper adds in the very next "
                          "sentence, because dropping it changes the meaning. The total "
                          "chance of ending up above the trigger does still matter. "
                          "What does not matter is the shape of the good outcomes "
                          "beyond it. Those are not the same thing, and Part Two needs "
                          "the difference."):
            self.play(FadeIn(qual), run_time=1.2)
        self.beat()

        self.close_chapter([
            "a race → the textbook is right",
            "first-mover value pulls the other way",
            "inaction reads as bad news → bunching",
            "bad news principle",
        ])
