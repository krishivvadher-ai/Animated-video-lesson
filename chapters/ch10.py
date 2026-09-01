import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter10(Chapter):
    CH = 10
    TITLE = "The textbook’s line, as a sum"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["scale", "money", "slab", "flow"]

    def body(self):
        # ------------------------------------------------ two amounts
        self.heading("Two amounts, side by side")
        gets = VGroup(
            Rectangle(width=2.6, height=2.9, color=MONEY, stroke_width=3,
                      fill_color=MONEY, fill_opacity=0.18),
            Text("R ÷ ρ", font=FONT, font_size=T_HEAD, color=MONEY))
        gets[1].move_to(gets[0])
        pays = VGroup(
            Rectangle(width=2.6, height=1.45, color=SUNK, stroke_width=3,
                      fill_color=SUNK, fill_opacity=0.18),
            Text("K", font=FONT, font_size=T_HEAD, color=SUNK))
        pays[1].move_to(pays[0])
        pair = VGroup(gets, pays).arrange(RIGHT, buff=2.4, aligned_edge=DOWN)
        St.place(pair, St.STAGE, ay=0.1)
        lg = Text("what she gets", font=FONT, font_size=T_SMALL, color=MONEY)
        lg.next_to(gets, UP, buff=0.25)
        lp = Text("what she pays", font=FONT, font_size=T_SMALL, color=SUNK)
        lp.next_to(pays, UP, buff=0.25)

        with self.narrate("Nell is deciding whether to build. There are exactly two "
                          "amounts, and we can write both of them down."):
            self.play(FadeIn(gets[0]), FadeIn(lg), run_time=0.8)
        with self.narrate("What she gets: the money coming in each month, for ever, "
                          "discounted back. From the last chapter, that is the yearly "
                          "amount divided by the rate. Call the yearly amount R, and "
                          "the rate the cost of capital."):
            self.play(Write(gets[1]), run_time=1.4)
        self.beat()
        with self.narrate("What she pays: the sunk cost of building it. Call that K."):
            self.play(FadeIn(pays[0]), FadeIn(lp), run_time=0.7)
            self.play(Write(pays[1]), run_time=0.8)
        self.beat()

        key = St.points(["R — revenue a year", "K — the sunk cost",
                         "ρ — the cost of capital"],
                        colour=CHALK, dot_colour=WAIT, size=T_BODY, width=20)
        St.place(key, St.SIDE, ay=0.2)
        with self.narrate("Three letters, and nothing more. R is the revenue a year. K "
                          "is the sunk cost. And the third one we will only ever call "
                          "the cost of capital."):
            self.play(S.lag_map(FadeIn, key, lag=0.25), run_time=1.5)
        self.beat()
        self.play(FadeOut(key), run_time=0.4)

        nw = Text("R ÷ ρ  −  K", font=FONT, font_size=T_HEAD, color=CHALK)
        St.place(nw, St.FOOT, pad=0.06)
        with self.narrate("Subtract one from the other and you have what the project is "
                          "worth."):
            self.play(TransformFromCopy(VGroup(gets[1], pays[1]), nw, path_arc=PI / 4),
                      run_time=1.6)
        self.play(FadeOut(lg), FadeOut(lp), run_time=0.35)
        self.define("net worth", "What you get, minus what you pay.", "scale", CHALK,
                    at=UP * 1.1, hold=3.4)
        self.clear_stage()

        # ------------------------------------------------ the borderline
        self.heading("So where is the borderline?")
        steps = VGroup(
            Text("R ÷ ρ  −  K   =   0", font=FONT, font_size=T_SUB, color=CHALK),
            Text("R ÷ ρ   =   K", font=FONT, font_size=T_SUB, color=CHALK),
            Text("R   =   ρ × K", font=FONT, font_size=T_HEAD, color=COST),
        ).arrange(DOWN, buff=0.85)
        St.place(steps, St.FULL, ay=0.1)
        says = ["The borderline is where the two are exactly equal — where net worth is "
                "nothing at all.",
                "Add K to both sides. What she gets equals what she pays.",
                "Multiply both sides by the rate. And there is the textbook's line."]
        self.play(Write(steps[0]), run_time=1.3)
        with self.narrate(says[0]):
            self.play(S.pulse(steps[0], CHALK))
        with self.narrate(says[1]):
            self.play(TransformFromCopy(steps[0], steps[1], path_arc=PI / 5),
                      run_time=1.5)
        with self.narrate(says[2]):
            self.play(TransformFromCopy(steps[1], steps[2], path_arc=PI / 5),
                      run_time=1.5)
        self.beat()
        with self.narrate("That is Marshall's line, and now you know exactly where it "
                          "comes from. It is the interest on the money she sank into "
                          "the building — the normal return on capital, and nothing "
                          "more."):
            self.play(S.flash_around(steps[2], COST, run_time=2.0))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the numbers
        self.heading("Put Dixit’s own numbers in")
        rows = VGroup(
            Text("K = 2        ρ = 0.05", font=FONT, font_size=T_SUB, color=MUTED),
            Text("ρ × K  =  0.05 × 2  =  0.1", font=FONT, font_size=T_SUB, color=COST),
            Text("running cost  C = 1", font=FONT, font_size=T_SUB, color=SUNK),
            Text("M  =  1  +  0.1  =  1.10", font=FONT, font_size=T_HEAD, color=COST),
        ).arrange(DOWN, buff=0.7)
        St.place(rows, St.FULL, ay=0.05)
        says = ["Dixit's worked example uses a sunk cost of two, and a cost of capital "
                "of five per cent.",
                "So the normal return on that capital is nought point nought five times "
                "two. A tenth.",
                "And the factory also costs one to run each year.",
                "Add them: one, plus a tenth. One point one. That is the number you "
                "have been staring at since chapter two, and you have just worked it "
                "out yourself."]
        for i, row in enumerate(rows):
            with self.narrate(says[i]):
                self.play(Write(row), run_time=1.1)
            self.beat(0.4)
        self.play(S.spark(rows[3], COST))
        self.beat()

        self.close_chapter([
            "what she gets:  R ÷ ρ",
            "what she pays:  K",
            "the borderline is where net worth is zero",
            "so the textbook line is  M = C + ρK = 1.10",
        ])
