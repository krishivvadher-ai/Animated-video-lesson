import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.chain import Chain
from lib.theme import *


class Chapter38(Chapter):
    CH = 38
    TITLE = "The chain"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["chain", "flow", "door", "people"]

    def body(self):
        # ------------------------------------------------ the authors
        self.heading("The two people who wrote it down")
        pair = VGroup(stick.StickFigure("Bowdler", SRC_BR, scale=0.8),
                      stick.StickFigure("Radia", SRC_BR, scale=0.8)
                      ).arrange(RIGHT, buff=2.2)
        St.place(pair, St.STAGE, ay=-0.3)
        with self.narrate("Two economists, writing in twenty-twelve, set out how the "
                          "policy is supposed to work. Christopher Bowdler and Amar "
                          "Radia."):
            self.play(FadeIn(pair[0]), FadeIn(pair[0].label()), run_time=0.7)
            self.play(FadeIn(pair[1]), FadeIn(pair[1].label()), run_time=0.7)

        tag = cards.source_tag("their colour, from here on", SRC_BR)
        St.place(tag, St.SIDE, ay=0.3)
        with self.narrate("They are careful, serious people, and nothing in this film "
                          "is an attack on them. Their colour, from here on, is red."):
            self.play(FadeIn(tag), run_time=0.8)
            self.play(S.flash_around(tag, SRC_BR))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the chain
        self.heading("They set it out as a chain")
        chain = Chain(y=0.0, width=13.0)
        St.place(chain, St.FULL, ay=0.25)
        with self.narrate("And the chain is the picture Part Two is built on, exactly "
                          "as the vertical scale was Part One's."):
            self.play(S.lag_map(FadeIn, chain.boxes, shift=UP * 0.2, lag=0.14),
                      run_time=2.2)
            self.play(S.lag_map(Create, chain.arrows, lag=0.1), run_time=1.2)

        why = St.caption("each link can be examined on its own", CHALK, T_SUB, width=38)
        St.place(why, St.FOOT, pad=0.06)
        with self.narrate("Why a chain? Because it is honest. Each link can be examined "
                          "on its own."):
            self.play(FadeIn(why), run_time=0.8)

        with self.narrate("And if any single link fails, the whole thing stops there."):
            self.play(chain.highlight(3, COST), run_time=0.6)
            brk = Cross(chain.link(3)[0], stroke_color=COST, stroke_width=6).scale(0.5)
            self.play(Create(brk), run_time=0.6)
            self.play(*[chain.boxes[i][0].animate.set_stroke(MUTED, width=2)
                        for i in (4, 5)], run_time=0.9)
        self.beat()
        self.play(FadeOut(brk), chain.highlight(3, SRC_BR), run_time=0.6)
        self.play(*[chain.boxes[i][0].animate.set_stroke(SRC_BR, width=3)
                    for i in (4, 5)], FadeOut(why), run_time=0.6)

        # ------------------------------------------------ two legs
        self.heading("The authors split it into two legs")
        b1 = Brace(VGroup(*chain.boxes[0:3]), DOWN, color=WAIT)
        t1 = Text("leg one", font=FONT, font_size=T_BODY, color=WAIT)
        t1.next_to(b1, DOWN, buff=0.16)
        with self.narrate("The authors themselves split the chain into two legs. From "
                          "the purchases to the price of assets."):
            self.play(GrowFromCenter(b1), FadeIn(t1), run_time=1.0)
        b2 = Brace(VGroup(*chain.boxes[3:6]), DOWN, color=TRIGGER)
        t2 = Text("leg two", font=FONT, font_size=T_BODY, color=TRIGGER)
        t2.next_to(b2, DOWN, buff=0.16)
        with self.narrate("And from the price of assets to what anybody actually "
                          "spends."):
            self.play(GrowFromCenter(b2), FadeIn(t2), run_time=1.0)
        self.beat()

        # ------------------------------------------------ Kit's disclaimer
        kit = stick.kit(scale=0.7)
        St.place(kit, St.FOOT, ax=-0.85, ay=0.0, pad=0.02, strict=False)
        with self.narrate("And Kit wants to say this out loud, now, before anything "
                          "else. He is only ever disputing the second leg. Not the "
                          "first.", v="c"):
            self.play(FadeIn(kit), run_time=0.6)
            self.play(*[chain.boxes[i][0].animate.set_stroke(MUTED, width=2)
                        for i in range(3)], run_time=0.9)
        with self.narrate("The first leg is the part everybody argues about, and he is "
                          "not arguing about it.", v="c"):
            self.play(S.flash_around(VGroup(*chain.boxes[3:6]), TRIGGER,
                                     run_time=2.0))
        self.beat()
        self.play(FadeOut(b1), FadeOut(t1), FadeOut(b2), FadeOut(t2), FadeOut(kit),
                  run_time=0.6)

        # ------------------------------------------------ link five
        self.heading("And one link inside it")
        with self.narrate("And within that second leg, one link is going to matter more "
                          "than all the others."):
            self.play(*[chain.boxes[i][0].animate.set_stroke(MUTED, width=2)
                        for i in (3, 5)], run_time=0.8)
        with self.narrate("Link five. The firm decides to build. Keep your eye on it "
                          "for the rest of the film."):
            self.play(chain.highlight(4, SRC_KIT), run_time=0.7)
            self.play(chain.link(4).animate.scale(1.22), run_time=0.9)
            self.play(S.flash_around(chain.link(4), SRC_KIT, run_time=2.0))
        self.beat()

        self.close_chapter([
            "Bowdler and Radia set the policy out as a chain",
            "leg one: purchases → the price of assets",
            "leg two: prices → what anybody spends",
            "and link five is where a firm decides",
        ])
