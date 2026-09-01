import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.chain import Chain
from lib.theme import *


class Chapter43(Chapter):
    CH = 43
    TITLE = "What is actually being claimed"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["chain", "scale", "people", "door"]

    def body(self):
        # ------------------------------------------------ what it is not
        self.heading("First, what it is not")
        nots = VGroup(
            St.caption("not: the policy does not work", MUTED, T_SUB, width=32),
            St.caption("not: the theory is false", MUTED, T_SUB, width=32),
        ).arrange(DOWN, buff=0.6)
        St.place(nots, St.FULL, ay=0.7)
        with self.narrate("This is not a claim that quantitative easing does not work."):
            self.play(FadeIn(nots[0]), run_time=0.9)
        with self.narrate("Kit has not disputed that it moved prices in financial "
                          "markets, which is the best-established finding in the whole "
                          "body of research."):
            self.play(S.flash_around(nots[0], MUTED))
        with self.narrate("It is not a claim that the theory is false."):
            self.play(FadeIn(nots[1]), run_time=0.9)

        is_ = St.caption("but: incomplete, in one place", SRC_KIT, T_HEAD, width=32)
        St.place(is_, St.FULL, ay=-0.55)
        with self.narrate("It is a claim that the theory is incomplete, in one specific "
                          "place."):
            self.play(Write(is_), run_time=2.2)
        self.wait(1.2)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the chain, one last time
        self.heading("The chain, one last time")
        chain = Chain(y=0.0, width=13.0)
        St.place(chain, St.FULL, ay=0.6)
        with self.narrate("So rebuild the chain one final time."):
            self.play(S.lag_map(FadeIn, chain.boxes, shift=UP * 0.2, lag=0.12),
                      run_time=2.0)
            self.play(S.lag_map(Create, chain.arrows, lag=0.08), run_time=1.0)

        care = St.caption("careful reasoning at every stage", SRC_BR, T_SUB, width=34)
        St.place(care, St.FULL, ay=-0.55)
        with self.narrate("Careful reasoning about what can go wrong at every stage."):
            self.play(FadeIn(care), run_time=0.8)
            self.play(*[chain.boxes[i][0].animate.set_stroke(SRC_BR, width=5)
                        for i in (0, 1, 2, 3, 5)], run_time=1.0)

        with self.narrate("Except one. The stage where a quantity finally has to "
                          "change, because somebody in a room has to say yes."):
            self.play(*[chain.boxes[i][0].animate.set_stroke(MUTED, width=2)
                        for i in (0, 1, 2, 3, 5)],
                      chain.highlight(4, SRC_KIT), run_time=1.2)
            self.play(chain.link(4).animate.scale(1.2), run_time=0.8)
            self.play(S.flash_around(chain.link(4), SRC_KIT, run_time=2.0))
        self.beat()
        self.play(FadeOut(care), run_time=0.4)
        self.play(St.park(chain, UP, height=1.1), run_time=1.0)
        self.play(FadeOut(chain), run_time=0.5)
        self.clear_stage()

        # ------------------------------------------------ two claims
        self.heading("So: two claims, held differently")
        one = VGroup(
            cards.source_tag("mostly Dixit's, and he reports it", SRC_DX),
            St.points(["the bar is higher than the textbook says",
                       "and it rises as the world frightens",
                       "so the policy fights the largest bar"],
                      colour=CHALK, dot_colour=SRC_DX, size=T_SMALL, width=32,
                      buff=0.34),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        St.place(one, St.FULL, ay=0.55)
        with self.narrate("The first is Dixit's, and Kit is mostly reporting it. When "
                          "spending cannot be undone and the future is unknown, the bar "
                          "is higher than the textbook says. And it rises as the world "
                          "becomes more frightening."):
            self.play(FadeIn(one), run_time=1.4)
        with self.narrate("So a policy used in frightening times is working against the "
                          "largest version of that bar. That is well-established "
                          "economics, published in a general economics journal, and "
                          "simply absent from the article he began with."):
            self.play(S.flash_around(one, SRC_DX, run_time=2.2))

        two = VGroup(
            cards.source_tag("Kit's own, and held loosely", SRC_KIT),
            St.points(["a decision is a queue, not a calculation"],
                      colour=CHALK, dot_colour=SRC_KIT, size=T_SMALL, width=32),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        St.place(two, St.FULL, ay=-0.75)
        with self.narrate("The second is Kit's. And he holds it loosely, for all the "
                          "reasons the four open doors gave."):
            self.play(FadeIn(two), run_time=1.2)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the boundary
        self.drop_heading()
        a = St.caption("the gap is not a mistake", MUTED, T_SUB, width=30)
        St.place(a, St.WIDE, ay=0.85)
        with self.narrate("The gap is not a mistake in anybody's reasoning."):
            self.play(FadeIn(a), run_time=0.9)
        b = St.caption("it is a boundary", CHALK, T_HEAD, width=24)
        St.place(b, St.WIDE, ay=0.25)
        with self.narrate("It is a boundary."):
            self.play(Write(b), run_time=1.6)
        # the film's last scripted silence
        self.wait(3.0)

        edge = DashedLine(UP * 1.2, DOWN * 1.6, color=SUNK, stroke_width=4)
        edge.move_to(St.WIDE.point(0.0, -0.55))
        left = St.caption("a model of the whole economy", SRC_BR, T_SMALL, width=22)
        left.next_to(edge, LEFT, buff=0.6)
        right = St.caption("how the decision gets made", SRC_KIT, T_SMALL, width=22)
        right.next_to(edge, RIGHT, buff=0.6)
        with self.narrate("A model of the whole economy hands off to a decision it does "
                          "not model. And the study of how that decision actually gets "
                          "made sits in a different journal, on a different reading "
                          "list, and in the other half of the same degree."):
            self.play(Create(edge), run_time=0.9)
            self.play(FadeIn(left), run_time=0.7)
            self.play(FadeIn(right), run_time=0.7)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the last shot
        chain2 = Chain(y=0.0, width=12.4)
        St.place(chain2, St.FULL, ay=0.9)
        self.play(FadeIn(chain2), run_time=1.2)
        self.play(chain2.highlight(4, SRC_KIT), run_time=0.6)
        cast = VGroup(stick.nell(scale=0.5), stick.marshall(scale=0.5),
                      stick.ava(scale=0.5), stick.kenji(scale=0.5),
                      stick.kit(scale=0.5), stick.governor(scale=0.5))
        cast.arrange(RIGHT, buff=1.15)
        St.place(cast, St.FULL, ay=-0.85)
        with self.narrate("And the last shot is all of them, standing either side of "
                          "the chain, at the link nobody examined."):
            self.play(S.lag_map(FadeIn, cast, lag=0.12), run_time=2.0)
            self.play(S.flash_around(chain2.link(4), SRC_KIT, run_time=2.4))
        self.wait(2.0)

        self.close_chapter([
            "not that the policy fails, or the theory is false",
            "that the theory is incomplete in one place",
            "the bar rises exactly when the policy is used",
            "and the last link is a boundary, not a mistake",
        ])
