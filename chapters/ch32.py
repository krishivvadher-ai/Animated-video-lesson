import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.chain import Chain
from lib.theme import *


class Chapter32(Chapter):
    CH = 32
    TITLE = "The chain"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["chain", "people", "door", "signal"]

    def body(self):
        with self.narrate("Two economists, writing in twenty-twelve, set out how the "
                          "policy is supposed to work. They set it out as a chain. And "
                          "the chain is the picture Part Two is built on, exactly as "
                          "the vertical scale was Part One's."):
            pass

        pair = VGroup(
            stick.StickFigure("", CHALK, prop="printout", scale=0.75),
            stick.StickFigure("", CHALK, hat="specs", prop="book", scale=0.75),
        ).arrange(RIGHT, buff=0.6)
        plabel = Text("Bowdler & Radia (2012)", font=FONT, font_size=T_SMALL, color=SRC_BR)
        plabel.next_to(pair, DOWN, buff=0.25)
        grp = VGroup(pair, plabel).move_to(LEFT * 4.4 + UP * 1.6)
        with self.narrate("Christopher Bowdler and Amar Radia. They are careful, "
                          "serious people, and nothing in this film is an attack on "
                          "them. Their colour, from here on, is red."):
            self.play(FadeIn(grp), run_time=1.0)
        self.beat()
        self.play(grp.animate.scale(0.7).to_corner(UP + LEFT, buff=0.5), run_time=0.8)

        ch = Chain(y=0.6, width=12.4)
        says = [
            "One. The Bank creates money and buys gilts.",
            "Two. Gilt prices rise, and yields fall.",
            "Three. Other borrowing rates follow them down.",
            "Four. The cheaper price reaches an ordinary firm.",
            "Five. The firm decides to build.",
            "Six. Investment and output rise.",
        ]
        for i in range(6):
            with self.narrate(says[i]):
                self.play(FadeIn(ch.boxes[i], scale=0.9), run_time=0.5)
                if i > 0:
                    self.play(Create(ch.arrows[i - 1]), run_time=0.4)
        self.beat()

        why = cards.body("examine each link on its own", size=T_BODY, color=CHALK, width=54)
        why.to_edge(DOWN, buff=1.2)
        with self.narrate("Why a chain? Because it is honest. Each link can be examined "
                          "on its own. And if any single link fails, the whole thing "
                          "stops there."):
            self.play(FadeIn(why), run_time=1.0)
        self.beat()
        self.play(FadeOut(why), run_time=0.4)

        # -------------------------------------------------- two legs
        leg1 = SurroundingRectangle(VGroup(*ch.boxes[0:3]), color=MUTED, buff=0.22,
                                    stroke_width=3, corner_radius=0.12)
        l1 = Text("leg one: purchases → asset prices", font=FONT, font_size=T_SMALL,
                  color=MUTED)
        l1.next_to(leg1, DOWN, buff=0.25)
        leg2 = SurroundingRectangle(VGroup(*ch.boxes[3:6]), color=MUTED, buff=0.22,
                                    stroke_width=3, corner_radius=0.12)
        l2 = Text("leg two: asset prices → spending", font=FONT, font_size=T_SMALL,
                  color=MUTED)
        l2.next_to(leg2, DOWN, buff=0.25)
        with self.narrate("The authors themselves split the chain into two legs. From "
                          "the purchases to the price of assets."):
            self.play(Create(leg1), FadeIn(l1), run_time=0.9)
        with self.narrate("And from the price of assets to what anybody actually spends."):
            self.play(Create(leg2), FadeIn(l2), run_time=0.9)
        self.beat()

        kit = stick.kit(scale=0.75).move_to(LEFT * 4.6 + DOWN * 2.2)
        b = kit.say("I'm only ever disputing\nthe second leg.", direction=UP, width=3.8,
                    color=SRC_KIT)
        with self.narrate("And Kit wants to say this out loud, now, before anything "
                          "else. He is only ever disputing the second leg. Not the "
                          "first. The first leg is the part everybody argues about, and "
                          "he is not arguing about it.", v="c"):
            self.play(FadeIn(kit), run_time=0.5)
            self.play(FadeIn(b), run_time=0.7)
        self.beat()
        self.play(FadeOut(leg1), FadeOut(l1), FadeOut(b), run_time=0.5)

        # -------------------------------------------------- link five
        with self.narrate("And within that second leg, one link is going to matter more "
                          "than all the others."):
            self.play(*ch.dim_all(), run_time=0.8)
            self.play(ch.highlight(4, SRC_KIT), run_time=0.9)
        five = cards.body("Link five. The firm decides to build.", size=T_SUB,
                          color=SRC_KIT, width=30)
        five.to_edge(DOWN, buff=1.0)
        with self.narrate("Link five. The firm decides to build. Keep your eye on it "
                          "for the rest of the film."):
            self.play(FadeIn(five), run_time=0.9)
        self.beat()

        self.close_chapter([
            "a chain of six links",
            "one link fails ⇒ everything stops",
            "two legs: to prices, then to spending",
            "Kit disputes the second leg only",
        ])
