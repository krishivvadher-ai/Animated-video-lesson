import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.theme import *


class Chapter32(Chapter):
    CH = 32
    TITLE = "Two different kinds of fear"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["risk", "fog", "shield", "signal"]

    def body(self):
        q = cards.quote_card(
            "of possible future outcomes, only the unfavorable ones have a bearing on "
            "the current propensity to undertake a given project",
            "Dixit (1992), p. 118, quoting Bernanke (1983)", SRC_DX, width=42)
        q.move_to(UP * 1.6)
        if q.width > 11.4:
            q.scale(11.4 / q.width)
        with self.narrate("Replay the bad news principle from chapter nine. When you "
                          "can wait, it is mainly the bad possible outcomes that decide "
                          "whether you build now."):
            self.play(FadeIn(q), run_time=1.2)
        self.beat()
        ask = cards.body("So ask what this policy actually compresses.",
                         size=T_SUB, color=SRC_KIT, width=36)
        ask.move_to(DOWN * 1.2)
        with self.narrate("So the question to ask is: what does this policy actually "
                          "compress?"):
            self.play(FadeIn(ask), run_time=0.9)
        self.beat()
        self.clear_stage()

        self.define("the price of risk", "Extra return, for the worry.", "risk", SRC_BR,
                    at=UP * 0.4, hold=5.0)

        # ------------------------------------------------- the spring
        head = Text("What QE pushes down", font=FONT, font_size=T_SUB,
                    color=SRC_BR).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)
        sp = W.spring(SRC_BR, turns=7, width=5.0, height=1.0).move_to(UP * 0.6)
        wall = Line(LEFT * 3.0 + UP * 1.6, LEFT * 3.0 + DOWN * 0.4, color=MUTED,
                    stroke_width=5)
        lab = Text("the price of risk in financial markets", font=FONT,
                   font_size=T_SMALL, color=SRC_BR)
        lab.next_to(sp, DOWN, buff=0.6)
        with self.narrate("In financial markets, quantitative easing pushes that price "
                          "down. Squeeze the spring."):
            self.play(Create(wall), Create(sp), FadeIn(lab), run_time=1.2)
            sp2 = W.spring(SRC_BR, turns=7, width=5.0, height=1.0, compressed=0.85)
            sp2.move_to(sp.get_center() + LEFT * 0.6)
            self.play(Transform(sp, sp2), run_time=1.8)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------- the other fear
        nell = stick.nell(scale=1.0).move_to(LEFT * 4.0 + DOWN * 0.8)
        self.play(FadeIn(nell), nell.mood("worried"), run_time=0.6)
        head2 = Text("And now the other fear, inside Nell's head",
                     font=FONT, font_size=T_SUB, color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head2), run_time=0.5)

        fears = ["Will there still be customers in three years?",
                 "Will the euro survive, or will countries start leaving it?",
                 "Will this whole industry still exist?"]
        bubbles = VGroup()
        for i, f in enumerate(fears):
            th = nell.think(f, direction=UP, width=3.4, color=WAIT)
            th.move_to(RIGHT * 1.4 + UP * (1.7 - i * 1.6))
            bubbles.add(th)
            with self.narrate(f, v="c"):
                self.play(FadeIn(th), run_time=0.8)
        self.beat()
        diff = cards.body("Different worries entirely.", size=T_SUB, color=WAIT, width=24)
        diff.move_to(LEFT * 4.0 + DOWN * 2.6)
        with self.narrate("Those are different worries entirely. A central bank buying "
                          "government bonds reaches them only indirectly, if at all."):
            self.play(FadeIn(diff), run_time=0.9)
        self.beat()

        # ------------------------------------------------- the concession
        self.clear_stage()
        kit = stick.kit(scale=0.8).move_to(LEFT * 5.4 + DOWN * 1.8)
        self.play(FadeIn(kit), run_time=0.5)
        head3 = Text("And here Kit narrows his own claim, in writing",
                     font=FONT, font_size=T_SUB, color=SRC_KIT).to_edge(UP, buff=0.7)
        self.play(FadeIn(head3), run_time=0.5)

        conc = cards.bullet_list([
            "it does touch that fear",
            "richer owners spend more",
            "one firm's customers are others' spending",
            "and gilts aim at doubts about governments",
        ], color=CHALK, width=42, dotc=SRC_KIT)
        conc.move_to(RIGHT * 0.8 + UP * 0.5)
        says = ["He cannot say the policy fails to touch that fear.",
                "Higher share and property prices do make some owners spend more.",
                "And one company's customers are other people's spending. So the fear "
                "is thinned a little.",
                "And buying government bonds is obviously aimed at doubts about "
                "governments in the first place."]
        for i in range(4):
            with self.narrate(says[i]):
                self.play(FadeIn(conc[i], shift=RIGHT * 0.2), run_time=0.6)
        self.beat()

        self.play(FadeOut(conc), run_time=0.5)
        honest = cards.body("So the honest version is about how DIRECTLY, not about "
                            "whether.", size=T_HEAD, color=SRC_KIT, width=30)
        honest.move_to(UP * 0.8)
        with self.narrate("So the honest version of his claim is about how directly, "
                          "not about whether."):
            self.play(Write(honest), run_time=2.2)
        self.beat()
        split = VGroup(
            cards.body("DIRECTLY:\nthe price of risk", size=T_BODY, color=SRC_BR, width=24),
            cards.body("AT ONE REMOVE:\nthe doubt itself",
                       size=T_BODY, color=WAIT, width=24),
        ).arrange(RIGHT, buff=1.6).move_to(DOWN * 1.5)
        with self.narrate("What a central bank reaches directly is the price at which "
                          "risk trades. What it reaches at one or two removes is the "
                          "doubt itself."):
            self.play(FadeIn(split[0]), run_time=0.8)
            self.play(FadeIn(split[1]), run_time=0.8)
        self.beat()

        self.close_chapter([
            "bad news principle",
            "QE squeezes the price of risk",
            "a different fear: will there be customers?",
            "how DIRECTLY — not whether",
        ])
