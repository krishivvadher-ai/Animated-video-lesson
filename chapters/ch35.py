import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib import surface as SF
from lib.scale import MasterScale
from lib.theme import *


class Chapter35(Chapter):
    CH = 35
    TITLE = "Bringing Part One back"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["scale", "fog", "lever", "chain"]

    def body(self):
        kit = stick.kit(scale=0.8).move_to(LEFT * 5.4 + DOWN * 1.8)
        self.play(FadeIn(kit), run_time=0.5)

        # -------------------------------------------------- two papers, one quantity
        p1 = VGroup(Rectangle(width=1.7, height=2.2, color=SRC_BR, stroke_width=3),
                    cards.body("Bowdler & Radia", size=T_SMALL, color=SRC_BR, width=14))
        p1[1].move_to(p1[0].get_center())
        p2 = VGroup(Rectangle(width=1.7, height=2.2, color=SRC_DX, stroke_width=3),
                    cards.body("Dixit", size=T_SMALL, color=SRC_DX, width=14))
        p2[1].move_to(p2[0].get_center())
        papers = VGroup(p1, p2).arrange(RIGHT, buff=3.4).move_to(UP * 1.4)
        with self.narrate("Kit puts the two articles side by side, and notices they are "
                          "arguing about the same quantity from opposite sides."):
            self.play(FadeIn(papers), run_time=1.0)

        c1 = cards.body("a lower cost of capital raises investment",
                        size=T_SMALL, color=SRC_BR, width=20)
        c1.next_to(p1, DOWN, buff=0.5)
        c2 = cards.body("the number in between is NOT the cost of capital",
                        size=T_SMALL, color=SRC_DX, width=20)
        c2.next_to(p2, DOWN, buff=0.5)
        with self.narrate("One of them asserts that a lower cost of capital raises "
                          "investment."):
            self.play(FadeIn(c1), run_time=0.8)
        with self.narrate("And the other spends a whole article showing that the number "
                          "standing between the cost of capital and the decision is not "
                          "the cost of capital."):
            self.play(FadeIn(c2), run_time=1.0)
        self.beat()
        clash = Line(p1.get_right() + RIGHT * 0.2, p2.get_left() + LEFT * 0.2,
                     color=MUTED, stroke_width=3)
        self.play(Create(clash), run_time=0.8)
        self.beat()
        self.clear_stage(keep=[kit])

        # -------------------------------------------------- the fifteen-second replay
        sc = MasterScale(x=-2.6, y=-0.4, height=4.4, lo=0.0, hi=3.7)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), FadeIn(sc.title), run_time=0.8)
        b = sc.add_level("M", 1.0, "break-even", COST, width=2.6)
        h = sc.add_level("H", 1.86, "the real bar", TRIGGER, width=2.6, sw=5)
        with self.narrate("Fifteen seconds of chapter eight, so it is fresh. The bar a "
                          "project must clear is the textbook bar, multiplied."):
            self.play(Create(b[0]), FadeIn(b[1]), run_time=0.6)
            self.play(Create(h[0]), FadeIn(h[1]), run_time=0.9)
        with self.narrate("And the multiplier grows as the world becomes more uncertain."):
            self.play(h[0].animate.shift(UP * 1.0), h[1].animate.shift(UP * 1.0),
                      run_time=1.4)
        self.beat()
        self.clear_stage(keep=[kit])

        # -------------------------------------------------- the move
        gov = stick.governor(scale=0.95).move_to(LEFT * 3.4 + DOWN * 0.4)
        self.play(FadeIn(gov), run_time=0.6)
        chain_q = cards.bullet_list([
            "When does he reach for this policy?",
            "Only when rates have already been cut to nothing.",
            "And when does that happen? Only in a crisis.",
            "And what is a crisis? Maximum uncertainty.",
        ], color=CHALK, width=32)
        chain_q.move_to(RIGHT * 2.4 + UP * 0.4)
        says = ["Now watch the Governor reach for quantitative easing, and ask when he "
                "does that.",
                "Only when rates have already been cut to nothing.",
                "And when does that happen? Only in a crisis.",
                "And what is a crisis? Maximum uncertainty."]
        for i in range(4):
            with self.narrate(says[i]):
                self.play(FadeIn(chain_q[i], shift=RIGHT * 0.2), run_time=0.6)
                if i == 0:
                    self.play(gov.point_at(chain_q), run_time=0.5)
        self.beat()
        self.clear_stage()

        # -------------------------------------------------- walking the surface
        with self.narrate("Which means we can go back to the sheet from chapter eight, "
                          "and watch what the policy actually does to a firm's bar."):
            pass
        ax = SF.axes()
        self.set_camera_orientation(phi=66 * DEGREES, theta=-58 * DEGREES, zoom=0.95)
        sheet = SF.sheet(ax)
        self.play(Create(ax), run_time=1.0)
        self.play(Create(sheet), run_time=2.4)

        xl = Text("choppier revenue →", font=FONT, font_size=T_SMALL, color=WAIT)
        yl = Text("cheaper money →", font=FONT, font_size=T_SMALL, color=MONEY)
        xl.to_corner(DOWN + LEFT, buff=0.7)
        yl.next_to(xl, UP, buff=0.22).align_to(xl, LEFT)
        self.add_fixed_in_frame_mobjects(xl, yl)
        self.play(FadeIn(xl), FadeIn(yl), run_time=0.5)

        start = SF.point(ax, 0.20, 0.05)
        dot = Dot3D(start, radius=0.11, color=CHALK)
        with self.narrate("Here is a firm in ordinary times. Twenty per cent "
                          "choppiness, money at five per cent. Its bar is one point "
                          "eight six times break-even."):
            self.play(FadeIn(dot), run_time=0.8)
        self.beat()

        mid = SF.point(ax, 0.20, 0.02)
        with self.narrate("The policy makes money cheaper. So the firm slides this way "
                          "— and the sheet under it goes up, not down. Two point six one."):
            self.play(dot.animate.move_to(mid), run_time=2.2)
        self.beat()

        end = SF.point(ax, 0.40, 0.02)
        with self.narrate("But the policy is only ever used in a crisis. So at the very "
                          "same moment, the firm is dragged the other way too — into "
                          "the choppiest part of the sheet."):
            self.play(dot.animate.move_to(end), run_time=2.6)
            self.move_camera(phi=56 * DEGREES, theta=-130 * DEGREES, run_time=2.6)
        self.beat()
        top = cards.body("Both movements push the bar UP.", size=T_SUB, color=TRIGGER,
                         width=24)
        top.to_corner(UP + RIGHT, buff=0.7)
        self.add_fixed_in_frame_mobjects(top)
        self.remove(top)
        with self.narrate("Both movements push the bar up. Not one up and one down. "
                          "Both up."):
            self.play(FadeIn(top), run_time=0.9)
        self.beat()

        self.play(FadeOut(sheet), FadeOut(ax), FadeOut(dot), FadeOut(xl), FadeOut(yl),
                  FadeOut(top), run_time=1.0)
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES, zoom=1.0)

        # -------------------------------------------------- the sentence
        line = cards.body("QE is a rate cut delivered in the one situation that blunts rate cuts.", size=T_HEAD, color=CHALK, width=32)
        with self.narrate("Which gives the sentence this chapter exists for. "
                          "Quantitative easing is not a weaker version of a rate cut. "
                          "It is a rate cut delivered in the one situation that blunts "
                          "rate cuts."):
            self.play(Write(line), run_time=3.0)
        self.beat()
        who = cards.note("the bar: Dixit  ·  the pairing: Kit", width=56)
        who.to_edge(DOWN, buff=0.62)
        with self.narrate("And be clear about whose is whose. The bar, and the fact "
                          "that it rises with uncertainty, is Dixit's. Putting it next "
                          "to this policy is Kit's."):
            self.play(FadeIn(who), run_time=0.9)
        self.beat()

        self.close_chapter([
            "one: cheaper capital raises investment",
            "the other: the number in between is not that",
            "QE ⇒ zero bound ⇒ crisis ⇒ maximum uncertainty",
            "the bar is highest exactly then",
        ])
