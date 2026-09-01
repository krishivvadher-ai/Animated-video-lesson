import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.scale import MasterScale
from lib.theme import *


class Chapter10(Chapter):
    CH = 10
    TITLE = "The textbook’s line, as a sum"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["scale", "money", "slab", "flow"]

    def body(self):
        nell = stick.nell(scale=0.8).to_corner(DOWN + LEFT, buff=0.5)
        self.play(FadeIn(nell), run_time=0.5)

        # ------------------------------------------------ the two sides
        head = Text("Two amounts, side by side", font=FONT, font_size=T_SUB,
                    color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)

        left = VGroup(
            Rectangle(width=2.6, height=2.8, color=MONEY, stroke_width=3,
                      fill_color=MONEY, fill_opacity=0.16),
            cards.body("what she GETS", size=T_BODY, color=MONEY, width=14))
        left[1].next_to(left[0], UP, buff=0.25)
        left.move_to(LEFT * 3.2 + DOWN * 0.2)
        lsum = Text("R  ÷  ρ", font=FONT, font_size=T_SUB, color=MONEY)
        lsum.move_to(left[0].get_center())

        right = VGroup(
            Rectangle(width=2.6, height=1.4, color=SUNK, stroke_width=3,
                      fill_color=SUNK, fill_opacity=0.16),
            cards.body("what she PAYS", size=T_BODY, color=SUNK, width=14))
        right[1].next_to(right[0], UP, buff=0.25)
        right.move_to(RIGHT * 3.2 + DOWN * 0.9)
        rsum = Text("K", font=FONT, font_size=T_SUB, color=SUNK)
        rsum.move_to(right[0].get_center())

        with self.narrate("Nell is deciding whether to build. There are exactly two "
                          "amounts, and we can write both of them down."):
            self.play(FadeIn(left), FadeIn(right), run_time=1.0)
        with self.narrate("What she gets: the money coming in each month, for ever, "
                          "discounted back. From the last chapter, that is the yearly "
                          "amount divided by the rate. Call the yearly amount R, and "
                          "the rate the Greek letter that we will only ever call the "
                          "cost of capital."):
            self.play(Write(lsum), run_time=1.4)
        self.beat()
        with self.narrate("What she pays: the sunk cost of building it. Call that K."):
            self.play(Write(rsum), run_time=0.9)
        self.beat()

        note = cards.note("R = revenue a year   ·   K = the sunk cost   ·   "
                          "ρ = the cost of capital", width=62)
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.7)
        self.wait(1.2)

        # ------------------------------------------------ net worth
        self.play(FadeOut(note), run_time=0.4)
        nw = Text("R ÷ ρ  −  K", font=FONT, font_size=T_HEAD, color=CHALK)
        nw.move_to(DOWN * 2.4)
        with self.narrate("Subtract one from the other and you have what the project is "
                          "worth. Economists call it net worth."):
            self.play(Write(nw), run_time=1.4)
        self.define("net worth", "What you get, minus what you pay.", "scale", CHALK,
                    at=UP * 1.4, hold=3.6)

        # ------------------------------------------------ the borderline
        self.clear_stage(keep=[nell])
        head2 = Text("So where is the borderline?", font=FONT, font_size=T_SUB,
                     color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head2), run_time=0.5)

        steps = VGroup(
            Text("R ÷ ρ  −  K   =   0", font=FONT, font_size=T_SUB, color=CHALK),
            Text("R ÷ ρ   =   K", font=FONT, font_size=T_SUB, color=CHALK),
            Text("R   =   ρ × K", font=FONT, font_size=T_HEAD, color=COST),
        ).arrange(DOWN, buff=0.8).move_to(UP * 0.4)
        says = ["The borderline is where the two are exactly equal — where net worth "
                "is nothing at all.",
                "Add K to both sides. What she gets equals what she pays.",
                "Multiply both sides by the rate. And there is the textbook's line: the "
                "yearly revenue has to equal the rate times the sunk cost."]
        for i in range(3):
            with self.narrate(says[i]):
                self.play(Write(steps[i]), run_time=1.4)
            self.beat(0.5)

        with self.narrate("That is Marshall's line, and now you know exactly where it "
                          "comes from. It is the interest on the money she sank into "
                          "the building — the normal return on capital, and nothing more."):
            self.play(Circumscribe(steps[2], color=COST, buff=0.2, stroke_width=4),
                      run_time=1.6)
        self.beat()

        # ------------------------------------------------ numbers
        self.clear_stage(keep=[nell])
        head3 = Text("Put Dixit’s own numbers in", font=FONT, font_size=T_SUB,
                     color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head3), run_time=0.5)
        rows = VGroup(
            Text("K = 2        ρ = 0.05", font=FONT, font_size=T_SUB, color=MUTED),
            Text("R  =  0.05 × 2  =  0.1", font=FONT, font_size=T_SUB, color=COST),
            Text("plus a running cost of  C = 1", font=FONT, font_size=T_SUB, color=SUNK),
            Text("M  =  1  +  0.1  =  1.10", font=FONT, font_size=T_HEAD, color=COST),
        ).arrange(DOWN, buff=0.7).move_to(DOWN * 0.2)
        says = ["Dixit's worked example uses a sunk cost of two, and a cost of capital "
                "of five per cent.",
                "So the normal return on that capital is nought point nought five times "
                "two. A tenth.",
                "And the factory also costs one to run each year.",
                "Add them: one, plus a tenth. One point one. That is the eleven-tenths "
                "you have been staring at since chapter two, and you have just worked "
                "it out yourself."]
        for i in range(4):
            with self.narrate(says[i]):
                self.play(Write(rows[i]), run_time=1.2)
            self.beat(0.4)
        self.beat()

        self.close_chapter([
            "what she gets:  R ÷ ρ",
            "what she pays:  K",
            "net worth is the difference; the borderline is where it is zero",
            "so the textbook line is  M = C + ρK  =  1.10",
        ])
