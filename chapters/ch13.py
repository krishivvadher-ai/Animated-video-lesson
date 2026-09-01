import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter13(Chapter):
    CH = 13
    TITLE = "The one formula in the film"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["scale", "money", "fog", "clock"]

    def body(self):
        # ------------------------------------------------ build the formula
        self.heading("It is a square root and a division")
        inner = VGroup(
            Text("8", font=FONT, font_size=T_HEAD, color=CHALK),
            Text("×", font=FONT, font_size=T_HEAD, color=MUTED),
            Text("the cost of capital", font=FONT, font_size=T_BODY, color=MONEY),
            Text("÷", font=FONT, font_size=T_HEAD, color=MUTED),
            Text("choppiness²", font=FONT, font_size=T_BODY, color=WAIT),
        ).arrange(RIGHT, buff=0.3)
        St.place(inner, St.FULL, ay=0.72)
        with self.narrate("Start inside. Eight, times the cost of capital, divided by "
                          "the choppiness multiplied by itself."):
            self.play(LaggedStartMap(FadeIn, inner, shift=UP * 0.25, lag_ratio=0.18),
                      run_time=1.6)
        self.beat()

        whole = Text("½ × ( 1 + √( 1 + that ) )", font=FONT, font_size=T_HEAD,
                     color=TRIGGER)
        St.place(whole, St.FULL, ay=-0.35)
        with self.narrate("Add one to it. Take the square root. Add one again, and "
                          "halve it. That is the whole formula."):
            self.play(TransformFromCopy(inner, whole, path_arc=PI / 5), run_time=2.0)
        self.beat()
        with self.narrate("The paper calls the answer beta. This film calls it the "
                          "steepness, because that is what it measures — how steeply "
                          "the value of waiting curves upward."):
            self.foot("call it the steepness", TRIGGER)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ work it out
        self.heading("Base case: cost of capital 5%, choppiness 20%")
        work = VGroup(
            Text("0.2 × 0.2  =  0.04", font=FONT, font_size=T_SUB, color=WAIT),
            Text("8 × 0.05  =  0.4        0.4 ÷ 0.04  =  10", font=FONT,
                 font_size=T_SUB, color=MONEY),
            Text("1 + 10  =  11        √11  =  3.317", font=FONT, font_size=T_SUB,
                 color=CHALK),
            Text("1 + 3.317  =  4.317        ÷ 2  =  2.158", font=FONT,
                 font_size=T_SUB, color=TRIGGER),
        ).arrange(DOWN, buff=0.62)
        St.place(work, St.FULL, ay=0.05)
        says = ["The choppiness is nought point two. Times itself, nought point nought "
                "four.",
                "Eight times nought point nought five is nought point four. Divided by "
                "nought point nought four, that is ten.",
                "One plus ten is eleven. The square root of eleven is three point three "
                "one seven.",
                "One plus that is four point three one seven. Halve it. Two point one "
                "five eight."]
        for i, row in enumerate(work):
            with self.narrate(says[i]):
                self.play(Write(row), run_time=1.1)
            self.beat(0.35)
        with self.narrate("The paper prints two point one five. That is your answer, "
                          "with the paper's own rounding."):
            self.play(S.spark(work[3], TRIGGER))
            self.foot("the paper prints 2.15", MUTED)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the multiplier
        self.heading("Turn the steepness into the multiplier")
        f1 = Text("steepness ÷ (steepness − 1)", font=FONT, font_size=T_SUB, color=CHALK)
        f2 = Text("2.158  ÷  1.158  =  1.86", font=FONT, font_size=T_HEAD, color=TRIGGER)
        col = VGroup(f1, f2).arrange(DOWN, buff=0.8)
        St.place(col, St.FULL, ay=0.55)
        with self.narrate("Divide the steepness by itself-minus-one."):
            self.play(FadeIn(f1), run_time=0.8)
        with self.narrate("Two point one five eight, divided by one point one five "
                          "eight. One point eight six. There is the multiplier from "
                          "chapter eight — and you have just derived it."):
            self.play(TransformFromCopy(f1, f2, path_arc=PI / 4), run_time=1.8)
            self.play(S.flash_around(f2, TRIGGER))
        self.beat()

        two = VGroup(
            Text("H  =  1.86  ×  M", font=FONT, font_size=T_SUB, color=TRIGGER),
            Text("or a hurdle rate of  1.86 × 5%  =  9.3%", font=FONT,
                 font_size=T_SUB, color=TRIGGER),
        ).arrange(DOWN, buff=0.55)
        St.place(two, St.FULL, ay=-0.62)
        with self.narrate("Multiply the textbook's line by it, and you have the real "
                          "trigger."):
            self.play(FadeIn(two[0]), run_time=0.8)
        with self.narrate("Or multiply the cost of capital by it, and you have the "
                          "corrected hurdle rate. Nine point three per cent."):
            self.play(FadeIn(two[1]), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ do the other two
        self.heading("Now do the other two yourself")
        rows = VGroup(
            Text("choppiness 40%:   0.4 ÷ 0.16 = 2.5   √3.5 = 1.87   →  1.435",
                 font=FONT, font_size=T_BODY, color=WAIT),
            Text("1.435 ÷ 0.435  =  3.30           the paper prints 3.32",
                 font=FONT, font_size=T_BODY, color=TRIGGER),
            Text("cost of capital 2%:   0.16 ÷ 0.04 = 4   √5 = 2.236   →  1.618",
                 font=FONT, font_size=T_BODY, color=MONEY),
            Text("1.618 ÷ 0.618  =  2.62           the paper prints 2.61",
                 font=FONT, font_size=T_BODY, color=TRIGGER),
        ).arrange(DOWN, buff=0.6)
        St.place(rows, St.FULL, ay=0.15)
        says = ["Turn the choppiness up to forty per cent. Nought point four times "
                "itself is nought point one six. Eight times nought point nought five "
                "over that is two and a half. One plus that is three and a half; its "
                "square root is one point eight seven. Halve one plus that: one point "
                "four three five.",
                "Divide by itself-minus-one: three point three. The paper prints three "
                "point three two, because it rounds the steepness first.",
                "Now put the choppiness back to twenty and drop the cost of capital to "
                "two per cent. That gives four inside; one plus four is five; the "
                "square root of five is two point two three six. Halve one plus that: "
                "one point six one eight.",
                "And divide: two point six two. The paper prints two point six one."]
        for i, row in enumerate(rows):
            with self.narrate(says[i]):
                self.play(Write(row), run_time=1.2)
            self.beat(0.3)
        with self.narrate("And now you can see why both dials push the same way. More "
                          "choppiness, or cheaper money, both make the number inside "
                          "the square root smaller. That makes the steepness smaller. "
                          "And a smaller steepness gives a bigger multiplier."):
            self.foot("smaller steepness → bigger multiplier", TRIGGER)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the limits
        self.heading("Two things the formula gives you free")
        lim = VGroup(
            Text("choppiness → 0   ⇒   multiplier → 1", font=FONT, font_size=T_SUB,
                 color=MONEY),
            Text("cost of capital → 0   ⇒   multiplier → ∞", font=FONT,
                 font_size=T_SUB, color=COST),
        ).arrange(DOWN, buff=0.9)
        St.place(lim, St.FULL, ay=0.35)
        says = ["Let the choppiness shrink to nothing. The number inside the square "
                "root grows without limit, the steepness grows with it, and the "
                "multiplier settles on one. The textbook is exactly right in a certain "
                "world.",
                "Let the cost of capital fall to nothing instead. The steepness goes to "
                "one, and the multiplier goes off to infinity. Which is the paper's own "
                "line: the textbook analysis becomes totally misleading."]
        for i, row in enumerate(lim):
            with self.narrate(says[i]):
                self.play(FadeIn(row), run_time=0.9)
            self.beat(0.4)
        with self.narrate("One honest note to finish on. All of that works because the "
                          "project, once built, always makes money. Once you let it "
                          "make losses and allow her to give up, the two lines have to "
                          "be found together, and there is no formula — it needs four "
                          "equations and a computer. The paper does that, and prints "
                          "the answers: nought point seven two, and one point six two."):
            self.foot("L and H need a computer: 0.72 and 1.62", MUTED)
        self.beat()

        self.close_chapter([
            "one square root gives the steepness: 2.158",
            "steepness ÷ (steepness − 1) = 1.86",
            "40% choppiness → 3.30 · 2% money → 2.62",
            "both dials shrink it, so both raise the bar",
        ])
