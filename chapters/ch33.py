import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter33(Chapter):
    CH = 33
    TITLE = "One sentence, two different kinds of claim"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["shield", "scale", "door", "people"]

    def body(self):
        # ------------------------------------------------ the sentence
        self.heading("The sentence Part Two turns on")
        half1 = Text("this fall in the cost of capital", font=FONT,
                     font_size=T_BODY, color=WAIT)
        half2 = Text("should boost consumption\nand investment", font=FONT,
                     font_size=T_BODY, color=TRIGGER, line_spacing=0.95)
        sentence = VGroup(half1, half2).arrange(DOWN, buff=0.3)
        St.place(sentence, St.FULL, ay=0.9)
        src = cards.source_tag("Bowdler & Radia, p. 612", SRC_BR)
        src.next_to(sentence, DOWN, buff=0.45)
        with self.narrate("Here is the sentence the whole of Part Two turns on. It is "
                          "on page six hundred and twelve, and these are the authors' "
                          "exact words."):
            self.play(Write(half1), run_time=1.5)
            self.play(Write(half2), run_time=1.8)
            self.play(FadeIn(src), run_time=0.5)
        self.wait(1.4)

        with self.narrate("It contains two completely different kinds of claim, "
                          "stitched together. Split it in half."):
            self.play(half1.animate.shift(LEFT * 3.2 + UP * 0.2),
                      half2.animate.shift(RIGHT * 3.2 + DOWN * 0.2),
                      FadeOut(src), run_time=1.4)
        divider = DashedLine(UP * 2.0, DOWN * 2.6, color=MUTED, stroke_width=3)
        self.play(Create(divider), run_time=0.7)

        q1 = St.caption("does cheaper money arrive?", WAIT, T_BODY, width=20)
        q1.next_to(half1, DOWN, buff=0.5)
        with self.narrate("The first half is a question about prices. Does the cheaper "
                          "money actually arrive at a firm? You can go and check that."):
            self.play(FadeIn(q1), run_time=0.8)
        q2 = St.caption("what does a firm then do?", TRIGGER, T_BODY, width=20)
        q2.next_to(half2, DOWN, buff=0.5)
        with self.narrate("The second half is a question about behaviour. What does a "
                          "firm do once the money has arrived? That is a different sort "
                          "of question entirely."):
            self.play(FadeIn(q2), run_time=0.8)
        self.beat()

        # ------------------------------------------------ the shields
        shields = VGroup()
        for t in ("banks impaired", "no market access", "may not benefit"):
            sh = W.shield(SUNK, None, scale=0.55)
            lab = Text(t, font=FONT, font_size=T_SMALL, color=SUNK)
            lab.next_to(sh, RIGHT, buff=0.24)
            shields.add(VGroup(sh, lab))
        shields.arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        shields.next_to(q1, DOWN, buff=0.4)
        says = ["The first half gets hedged. Banks were impaired.",
                "Households and smaller companies have no access to capital markets.",
                "So they may not directly benefit."]
        for i, sh in enumerate(shields):
            with self.narrate(says[i]):
                self.play(FadeIn(sh, shift=UP * 0.2), run_time=0.7)

        with self.narrate("And be fair to them. These are honest, careful "
                          "qualifications. They also name several other routes by which "
                          "small firms might still benefit — through supply chains, "
                          "through a cheaper currency helping exporters, and through "
                          "banks passing on lower rates. All of that is in the article."):
            self.play(S.flash_around(shields, SUNK, run_time=2.4))

        kit = stick.kit(scale=0.55)
        kit.next_to(q2, DOWN, buff=0.9)
        with self.narrate("Now Kit waits for the same thing to happen to the other "
                          "half.", v="c"):
            self.play(FadeIn(kit), run_time=0.6)
            self.play(kit.mood("thinking"), run_time=0.4)
        # the film's scripted silence
        self.wait(3.4)

        count = St.caption("three hedges  ·  none", CHALK, T_SUB, width=26)
        St.place(count, St.FOOT, pad=0.06)
        with self.narrate("One half of that sentence is hedged three times. The other "
                          "half is not hedged once."):
            self.play(FadeIn(count), run_time=0.9)
            self.play(S.flash_around(count, SRC_KIT, run_time=2.0))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ what Kit actually says
        self.heading("And notice what he is not saying")
        not_this = St.caption("not: the sentence is wrong", MUTED, T_SUB, width=26)
        St.place(not_this, St.FULL, ay=0.85)
        but_this = St.caption("but: two halves, one level of trust",
                              SRC_KIT, T_SUB, width=34)
        St.place(but_this, St.FULL, ay=0.25)
        with self.narrate("His first reaction is not disagreement, and that matters for "
                          "everything that follows.", v="c"):
            self.play(FadeIn(not_this), run_time=0.8)
        with self.narrate("His first reaction is that two halves of one sentence are "
                          "not the same kind of statement, and are being given the same "
                          "amount of trust.", v="c"):
            self.play(FadeIn(but_this), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the machine
        self.heading("Why the second half goes unexamined")
        market = VGroup(cards.icon("flow", SRC_BR, 1.7),
                        St.caption("markets: modelled in\nenormous detail",
                                   SRC_BR, T_SMALL, width=20)
                        ).arrange(DOWN, buff=0.3)
        machine = VGroup(
            Rectangle(width=2.0, height=1.5, color=MUTED, stroke_width=3),
            Text("the firm", font=FONT, font_size=T_SMALL, color=MUTED))
        machine[1].move_to(machine[0].get_center())
        box = VGroup(machine, St.caption("a machine: numbers in,\ndecision out",
                                         MUTED, T_SMALL, width=20)
                     ).arrange(DOWN, buff=0.3)
        two = VGroup(market, box).arrange(RIGHT, buff=2.4)
        St.place(two, St.FULL, ay=0.2)
        with self.narrate("This is not carelessness. It is what a certain kind of "
                          "economics does by construction. It models markets in "
                          "enormous detail, and it treats a firm as a machine. Numbers "
                          "in. Decision out."):
            self.play(FadeIn(market), run_time=0.9)
            self.play(FadeIn(box), run_time=0.9)
            arr_in = Arrow(machine[0].get_left() + LEFT * 1.0,
                           machine[0].get_left(), color=WAIT, buff=0.05,
                           stroke_width=5)
            arr_out = Arrow(machine[0].get_right(),
                            machine[0].get_right() + RIGHT * 1.0, color=MONEY,
                            buff=0.05, stroke_width=5)
            self.play(GrowArrow(arr_in), GrowArrow(arr_out), run_time=0.8)

        fair = St.caption("and simplifications are how anyone thinks",
                          MUTED, T_SUB, width=40)
        St.place(fair, St.FOOT, pad=0.06)
        with self.narrate("There is nothing dishonest in that. It is a simplification, "
                          "and simplifications are how anyone thinks about anything "
                          "complicated."):
            self.play(FadeIn(fair), run_time=0.9)
        self.beat()

        last = St.caption("but the last link is the one nobody examines",
                          SRC_KIT, T_SUB, width=42)
        St.place(last, St.FULL, ay=-0.85)
        with self.narrate("But it does mean that the last link in the chain is the only "
                          "one nobody examines."):
            self.play(FadeIn(last), run_time=0.9)
            self.play(S.flash_around(last, SRC_KIT, run_time=2.0))
        self.beat()

        self.close_chapter([
            "one sentence, two different kinds of claim",
            "the price half is hedged three times",
            "the behaviour half is not hedged once",
            "because a firm is modelled as a machine",
        ])
