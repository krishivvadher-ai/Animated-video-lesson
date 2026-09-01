import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.theme import *


class Chapter38(Chapter):
    CH = 38
    TITLE = "The concession that hurts most"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["shield", "people", "money", "door"]

    def body(self):
        kit = stick.kit(scale=0.8).move_to(LEFT * 5.4 + DOWN * 1.8)
        self.play(FadeIn(kit), run_time=0.5)
        with self.narrate("This chapter exists because Kit's own source damages him, "
                          "and that is what intellectual honesty looks like."):
            pass

        kenji = stick.kenji(scale=0.9).move_to(RIGHT * 3.6 + UP * 0.4)
        kl = kenji.label()
        with self.narrate("Replay chapter thirteen. Japanese firms invested boldly and "
                          "hung on through losses, because their downside was cushioned."):
            self.play(FadeIn(kenji), FadeIn(kl), run_time=0.8)

        ax = NumberLine(x_range=[-3, 3, 1], length=6.4, color=MUTED,
                        include_numbers=False, include_ticks=False)
        ax.move_to(LEFT * 1.4 + DOWN * 1.4)
        curve = FunctionGraph(lambda x: 1.1 * np.exp(-x * x / 1.4), x_range=[-3, 3],
                              color=WAIT, stroke_width=4)
        curve.move_to(ax.get_center() + UP * 0.55)
        bad = Text("bad", font=FONT, font_size=T_SMALL, color=COST).next_to(ax, LEFT, buff=0.2)
        good = Text("good", font=FONT, font_size=T_SMALL, color=MONEY).next_to(ax, RIGHT, buff=0.2)
        self.play(Create(ax), Create(curve), FadeIn(bad), FadeIn(good), run_time=1.2)

        self.define("the good news principle", "Staying preserves the good outcomes.",
                    "signal", SRC_DX, at=UP * 2.0, hold=4.6)

        hl = Polygon(*[ax.n2p(x) for x in np.linspace(0, 3, 10)],
                     ax.n2p(3) + UP * 0.02, ax.n2p(0) + UP * 0.02,
                     color=MONEY, stroke_width=0, fill_color=MONEY, fill_opacity=0.0)
        box = Rectangle(width=3.2, height=1.6, color=MONEY, stroke_width=4)
        box.move_to(ax.n2p(1.5) + UP * 0.55)
        with self.narrate("Which half of that spread does a policy that props up prices "
                          "and signals that the authorities will act actually work on?"):
            self.play(Create(box), run_time=1.2)
        self.beat()

        land = cards.body("exactly the right half", size=T_SUB, color=MONEY, width=26)
        land.move_to(RIGHT * 3.6 + DOWN * 1.8)
        with self.narrate("This half. Which is exactly the right half for keeping a "
                          "struggling firm from closing."):
            self.play(FadeIn(land), run_time=0.9)
        self.beat()

        # ------------------------------------------------- Kit writes it against himself
        self.clear_stage()
        head = Text("And Kit writes this into his own argument, against himself",
                    font=FONT, font_size=T_SUB, color=SRC_KIT).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)

        kit2 = stick.kit(scale=1.0).move_to(LEFT * 4.4 + DOWN * 0.8)
        self.play(FadeIn(kit2), kit2.mood("worried"), run_time=0.6)

        page = RoundedRectangle(width=6.6, height=3.6, corner_radius=0.14,
                                color=SRC_KIT, stroke_width=3)
        page.move_to(RIGHT * 1.8 + UP * 0.1)
        written = cards.body("props up the upside\n= keeps firms alive\n= against me",
                             size=T_BODY, color=CHALK, width=32)
        written.move_to(page.get_center())
        with self.narrate("A policy that props up the upside is aimed at exactly the "
                          "right half of the distribution for keeping firms alive. "
                          "Which hands the policy a mechanism for the very thing he was "
                          "going to explain another way."):
            self.play(Create(page), run_time=0.8)
            self.play(FadeIn(written), run_time=1.4)
        self.beat()

        why = cards.body("his own source says it", size=T_SUB, color=SRC_KIT, width=40)
        why.to_edge(DOWN, buff=0.6)
        with self.narrate("Why include something that damages you? Because it is what "
                          "his own source says. The discomfort is the point."):
            self.play(FadeIn(why), run_time=1.0)
        self.beat()

        self.close_chapter([
            "good news principle governs staying",
            "QE works on exactly that half",
            "a real mechanism for keeping firms alive",
            "Kit writes it against himself",
        ])
