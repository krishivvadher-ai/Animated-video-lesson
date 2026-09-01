import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.chain import Chain
from lib.theme import *


class Chapter43(Chapter):
    CH = 43
    TITLE = "What is actually being claimed"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["chain", "scale", "queue", "people"]

    def body(self):
        head = Text("Narrow it down, one line at a time", font=FONT, font_size=T_SUB,
                    color=CHALK).to_edge(UP, buff=0.8)
        self.play(FadeIn(head), run_time=0.5)

        n1 = cards.body("This is NOT a claim that quantitative easing does not work.",
                        size=T_SUB, color=COST, width=40)
        n1.move_to(UP * 1.4)
        with self.narrate("This is not a claim that quantitative easing does not work."):
            self.play(FadeIn(n1), run_time=0.9)
        self.beat()
        n1b = cards.body("prices in financial markets DID move", size=T_BODY, color=CHALK, width=44)
        n1b.next_to(n1, DOWN, buff=0.5)
        with self.narrate("Kit has not disputed that it moved prices in financial "
                          "markets, which is the best-established finding in the whole "
                          "body of research."):
            self.play(FadeIn(n1b), run_time=1.0)
        self.beat()
        n2 = cards.body("It is NOT a claim that the theory is false.",
                        size=T_SUB, color=COST, width=40)
        n2.next_to(n1b, DOWN, buff=0.7)
        with self.narrate("It is not a claim that the theory is false."):
            self.play(FadeIn(n2), run_time=0.9)
        self.beat()
        n3 = cards.body("INCOMPLETE — in one place", size=T_SUB, color=SRC_KIT, width=40)
        n3.next_to(n2, DOWN, buff=0.5)
        with self.narrate("It is a claim that the theory is incomplete, in one specific "
                          "place."):
            self.play(FadeIn(n3), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- the chain, marked up
        ch = Chain(y=1.0, width=12.4)
        with self.narrate("So rebuild the chain one final time."):
            self.play(FadeIn(ch), run_time=1.4)
        marks = VGroup()
        for i in range(4):
            t = Text("✓", font=FONT, font_size=28, color=MONEY)
            t.next_to(ch.boxes[i], DOWN, buff=0.22)
            marks.add(t)
        t5 = Text("?", font=FONT, font_size=34, color=SRC_KIT)
        t5.next_to(ch.boxes[4], DOWN, buff=0.22)
        t6 = Text("✓", font=FONT, font_size=28, color=MONEY)
        t6.next_to(ch.boxes[5], DOWN, buff=0.22)
        with self.narrate("Careful reasoning about what can go wrong at every stage."):
            self.play(LaggedStart(*[FadeIn(m) for m in marks], lag_ratio=0.3),
                      FadeIn(t6), run_time=1.8)
        with self.narrate("Except one. The stage where a quantity finally has to "
                          "change, because somebody in a room has to say yes."):
            self.play(ch.highlight(4, SRC_KIT), FadeIn(t5), run_time=1.2)
            self.play(Circumscribe(ch.boxes[4], color=SRC_KIT, buff=0.15,
                                   stroke_width=5), run_time=1.6)
        self.beat()

        # ---------------------------------------------------- two things belong there
        two = Text("Two things belong there", font=FONT, font_size=T_SUB, color=CHALK)
        two.move_to(DOWN * 0.6)
        self.play(FadeIn(two), run_time=0.6)

        a = cards.body("DIXIT'S:\nthe bar is higher\nand rises with fear",
                       size=T_BODY, color=SRC_DX, width=40)
        a.move_to(DOWN * 0.3)
        self.play(FadeOut(two), run_time=0.3)
        with self.narrate("The first is Dixit's, and Kit is mostly reporting it. When "
                          "spending cannot be undone and the future is unknown, the bar "
                          "is higher than the textbook says. And it rises as the world "
                          "becomes more frightening. So a policy used in frightening "
                          "times is working against the largest version of that bar. "
                          "That is well-established economics, published in a general "
                          "economics journal, and simply absent from the article he "
                          "began with."):
            self.play(FadeIn(a), run_time=1.6)
        self.beat()
        self.play(FadeOut(a), run_time=0.5)

        b = cards.body("KIT'S:\nheld loosely",
                       size=T_SUB, color=SRC_KIT, width=40)
        b.move_to(DOWN * 0.3)
        with self.narrate("The second is Kit's. And he holds it loosely, for all the "
                          "reasons chapter twenty-nine gave."):
            self.play(FadeIn(b), run_time=1.0)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- the closing thought
        head3 = Text("And the closing thought — what the whole film has been for",
                     font=FONT, font_size=T_SUB, color=CHALK).to_edge(UP, buff=0.8)
        self.play(FadeIn(head3), run_time=0.5)

        c1 = cards.body("Not a mistake in anybody's reasoning.",
                        size=T_SUB, color=CHALK, width=38)
        c1.move_to(UP * 1.2)
        with self.narrate("The gap is not a mistake in anybody's reasoning."):
            self.play(FadeIn(c1), run_time=0.9)
        self.beat()
        c2 = cards.body("It is a BOUNDARY.", size=T_HEAD, color=SRC_KIT, width=26)
        c2.move_to(UP * 0.1)
        with self.narrate("It is a boundary."):
            self.play(Write(c2), run_time=1.6)
        self.beat()
        c3 = cards.body("one model hands off\nto a decision it does not model",
                        size=T_BODY, color=CHALK, width=46)
        c3.move_to(DOWN * 1.6)
        with self.narrate("A model of the whole economy hands off to a decision it does "
                          "not model. And the study of how that decision actually gets "
                          "made sits in a different journal, on a different reading "
                          "list, and in the other half of the same degree."):
            self.play(FadeIn(c3), run_time=1.6)
        self.beat()

        # ---------------------------------------------------- the final shot
        self.clear_stage()
        chn = Chain(y=0.0, width=11.0).scale(0.9)
        self.play(FadeIn(chn), run_time=1.2)
        self.play(chn.highlight(4, SRC_KIT), run_time=0.8)

        cast_left = VGroup(stick.nell(scale=0.6), stick.marshall(scale=0.6),
                           stick.ava(scale=0.6)).arrange(RIGHT, buff=1.0)
        cast_left.next_to(chn, UP, buff=0.7)
        cast_right = VGroup(stick.kit(scale=0.6), stick.governor(scale=0.6),
                            stick.StickFigure("", CHALK, prop="printout", scale=0.6),
                            stick.StickFigure("", CHALK, hat="specs", prop="book", scale=0.6)
                            ).arrange(RIGHT, buff=0.9)
        cast_right.next_to(chn, DOWN, buff=0.7)
        names = Text("Nell · Marshall · Ava · Kit · the Governor · the Authors",
                     font=FONT, font_size=T_SMALL, color=MUTED)
        names.next_to(cast_right, DOWN, buff=0.45)

        with self.narrate("And the last shot is all of them, standing either side of "
                          "the chain, at the link nobody examined."):
            self.play(FadeIn(cast_left), run_time=1.0)
            self.play(FadeIn(cast_right), run_time=1.0)
            self.play(FadeIn(names), run_time=0.8)
        self.wait(2.0)

        self.close_chapter([
            "not “it fails” · not “the theory is false”",
            "incomplete at the link where somebody says yes",
            "Dixit's half: established, and absent",
            "Kit's half: his own, held loosely",
        ])
