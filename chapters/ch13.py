import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.theme import *


class Chapter13(Chapter):
    CH = 13
    TITLE = "The one formula in the film"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["scale", "money", "fog", "clock"]

    def body(self):
        ava = stick.ava(scale=0.7).to_corner(DOWN + LEFT, buff=0.62)
        self.play(FadeIn(ava), run_time=0.5)
        with self.narrate("Here is the formula that finds the touching point. It looks "
                          "worse than it is. There is a square root, a division, and "
                          "nothing else — and we are going to work it out together."):
            pass

        # ------------------------------------------------ build the formula
        parts = VGroup(
            Text("8", font=FONT, font_size=T_HEAD, color=CHALK),
            Text("×", font=FONT, font_size=T_HEAD, color=MUTED),
            Text("the cost of capital", font=FONT, font_size=T_BODY, color=MONEY),
            Text("÷", font=FONT, font_size=T_HEAD, color=MUTED),
            Text("the choppiness²", font=FONT, font_size=T_BODY, color=WAIT),
        ).arrange(RIGHT, buff=0.32).move_to(UP * 1.6)
        with self.narrate("Start inside. Eight, times the cost of capital, divided by "
                          "the choppiness multiplied by itself."):
            for p in parts:
                self.play(FadeIn(p, shift=UP * 0.15), run_time=0.35)
        self.beat()

        step2 = Text("1  +  (that)", font=FONT, font_size=T_HEAD, color=CHALK)
        step2.move_to(UP * 0.2)
        with self.narrate("Add one to it."):
            self.play(FadeIn(step2), run_time=0.7)
        step3 = Text("√( 1 + that )", font=FONT, font_size=T_HEAD, color=CHALK)
        step3.move_to(DOWN * 1.0)
        with self.narrate("Take the square root."):
            self.play(FadeIn(step3), run_time=0.7)
        step4 = Text("½ × ( 1 + √( 1 + that ) )", font=FONT, font_size=T_HEAD,
                     color=TRIGGER)
        step4.move_to(DOWN * 2.3)
        with self.narrate("Add one again, and halve it. That is the whole formula. The "
                          "paper calls the answer beta; this film will call it the "
                          "steepness, because that is what it measures — how steeply "
                          "the value of waiting curves upward."):
            self.play(FadeIn(step4), run_time=0.9)
        self.beat()
        self.play(FadeOut(VGroup(parts, step2, step3)), run_time=0.6)
        self.play(step4.animate.move_to(UP * 2.5).scale(0.8), run_time=0.9)

        # ------------------------------------------------ work it out
        head = Text("Base case:  cost of capital 5%,  choppiness 20%",
                    font=FONT, font_size=T_SUB, color=MUTED)
        head.next_to(step4, DOWN, buff=0.7)
        self.play(FadeIn(head), run_time=0.6)

        work = VGroup(
            Text("0.2 × 0.2  =  0.04", font=FONT, font_size=T_SUB, color=WAIT),
            Text("8 × 0.05  =  0.4        0.4 ÷ 0.04  =  10", font=FONT,
                 font_size=T_SUB, color=MONEY),
            Text("1 + 10  =  11        √11  =  3.317", font=FONT, font_size=T_SUB,
                 color=CHALK),
            Text("1 + 3.317  =  4.317        ÷ 2  =  2.158", font=FONT,
                 font_size=T_SUB, color=TRIGGER),
        ).arrange(DOWN, buff=0.55).next_to(head, DOWN, buff=0.6)
        says = ["The choppiness is nought point two. Times itself, that is nought point "
                "nought four.",
                "Eight times nought point nought five is nought point four. And nought "
                "point four divided by nought point nought four is ten.",
                "One plus ten is eleven. The square root of eleven is three point three "
                "one seven.",
                "One plus that is four point three one seven. Halve it. Two point one "
                "five eight."]
        for i in range(4):
            with self.narrate(says[i]):
                self.play(FadeIn(work[i], shift=RIGHT * 0.2), run_time=0.7)
            self.beat(0.4)
        match = cards.body("the paper prints 2.15", size=T_BODY, color=MUTED, width=22)
        match.next_to(work, DOWN, buff=0.45)
        with self.narrate("The paper prints two point one five. That is your answer, "
                          "with the paper's own rounding."):
            self.play(FadeIn(match), run_time=0.8)
            self.play(Flash(work[3], color=TRIGGER, line_length=0.3), run_time=0.9)
        self.beat()
        self.clear_stage(keep=[ava])

        # ------------------------------------------------ steepness -> multiplier
        head2 = cards.section_title("And now turn the steepness into the multiplier", color=CHALK, size=T_SUB)
        self.play(FadeIn(head2), run_time=0.5)

        f = VGroup(
            Text("steepness ÷ (steepness − 1)", font=FONT, font_size=T_SUB, color=CHALK),
            Text("2.158  ÷  1.158  =  1.86", font=FONT, font_size=T_HEAD, color=TRIGGER),
        ).arrange(DOWN, buff=0.7).move_to(UP * 1.2)
        with self.narrate("Divide the steepness by itself-minus-one."):
            self.play(FadeIn(f[0]), run_time=0.8)
        with self.narrate("Two point one five eight, divided by one point one five "
                          "eight. One point eight six. There is the multiplier you met "
                          "in chapter eight — and you have just derived it."):
            self.play(Write(f[1]), run_time=1.6)
        self.beat()

        two = VGroup(
            Text("H  =  1.86  ×  M", font=FONT, font_size=T_SUB, color=TRIGGER),
            Text("ρ′  =  1.86  ×  5%   =   9.3%", font=FONT, font_size=T_SUB,
                 color=TRIGGER),
        ).arrange(DOWN, buff=0.6).move_to(DOWN * 1.4)
        with self.narrate("Multiply the textbook's line by it, and you have the real "
                          "trigger."):
            self.play(FadeIn(two[0]), run_time=0.8)
        with self.narrate("Or multiply the cost of capital by it, and you have the "
                          "corrected hurdle rate. One point eight six times five per "
                          "cent is nine point three."):
            self.play(FadeIn(two[1]), run_time=0.9)
        self.beat()
        self.clear_stage(keep=[ava])

        # ------------------------------------------------ turn the dials, by hand
        head3 = cards.section_title("Now do the other two, yourself", color=CHALK, size=T_SUB)
        self.play(FadeIn(head3), run_time=0.5)

        rows = VGroup(
            Text("choppiness 40%:   8×0.05 ÷ 0.16 = 2.5    √3.5 = 1.87    → 1.435",
                 font=FONT, font_size=T_BODY, color=WAIT),
            Text("1.435 ÷ 0.435  =  3.30      the paper prints 3.32",
                 font=FONT, font_size=T_BODY, color=TRIGGER),
            Text("cost of capital 2%:   8×0.02 ÷ 0.04 = 4    √5 = 2.236    → 1.618",
                 font=FONT, font_size=T_BODY, color=MONEY),
            Text("1.618 ÷ 0.618  =  2.62      the paper prints 2.61",
                 font=FONT, font_size=T_BODY, color=TRIGGER),
        ).arrange(DOWN, buff=0.55).move_to(DOWN * 0.1)
        says2 = ["Turn the choppiness up to forty per cent. Nought point four times "
                 "itself is nought point one six. Eight times nought point nought five, "
                 "over that, is two and a half. One plus that is three and a half, and "
                 "its square root is one point eight seven. Halve one plus that: one "
                 "point four three five.",
                 "Divide by itself-minus-one: three point three. The paper prints three "
                 "point three two, because it rounds the steepness first.",
                 "Now put the choppiness back to twenty and drop the cost of capital to "
                 "two per cent. Eight times nought point nought two, over nought point "
                 "nought four, is four. One plus four is five. The square root of five "
                 "is two point two three six. Halve one plus that: one point six one "
                 "eight.",
                 "And divide: two point six two. The paper prints two point six one."]
        for i in range(4):
            with self.narrate(says2[i]):
                self.play(FadeIn(rows[i], shift=RIGHT * 0.2), run_time=0.8)
            self.beat(0.4)

        why = cards.body("smaller steepness ⇒ bigger multiplier", size=T_SUB,
                         color=TRIGGER, width=30)
        why.to_edge(DOWN, buff=0.62)
        with self.narrate("And now you can see why both dials push the same way. More "
                          "choppiness, or cheaper money, both make the number inside "
                          "the square root smaller. That makes the steepness smaller. "
                          "And a smaller steepness, divided by itself-minus-one, gives "
                          "a bigger multiplier."):
            self.play(FadeIn(why), run_time=1.2)
        self.beat()

        # ------------------------------------------------ the limits, and L
        self.clear_stage(keep=[ava])
        head4 = cards.section_title("Two things the formula tells you for free", color=CHALK, size=T_SUB)
        self.play(FadeIn(head4), run_time=0.5)
        lim = VGroup(
            Text("choppiness → 0   ⇒   steepness → huge   ⇒   multiplier → 1",
                 font=FONT, font_size=T_BODY, color=MONEY),
            Text("cost of capital → 0   ⇒   steepness → 1   ⇒   multiplier → ∞",
                 font=FONT, font_size=T_BODY, color=COST),
        ).arrange(DOWN, buff=0.8).move_to(UP * 0.6)
        says3 = ["Let the choppiness shrink to nothing. The number inside the square "
                 "root grows without limit, the steepness grows with it, and the "
                 "multiplier settles on one. The textbook is exactly right in a certain "
                 "world.",
                 "Let the cost of capital fall to nothing instead. The number inside "
                 "goes to one, the steepness goes to one, and the multiplier goes off "
                 "to infinity. Which is the paper's own line: the textbook analysis "
                 "becomes totally misleading."]
        for i in range(2):
            with self.narrate(says3[i]):
                self.play(FadeIn(lim[i], shift=RIGHT * 0.2), run_time=0.8)
            self.beat(0.5)

        hard = cards.body("The quit-line L needs four equations solved together, and a "
                          "computer. The paper gives the answers: 0.72 and 1.62.",
                          size=T_BODY, color=MUTED, width=44)
        hard.to_edge(DOWN, buff=0.7)
        with self.narrate("One honest note to finish on. Everything you have just done "
                          "works because the project, once built, always makes money. "
                          "Once you let it make losses and allow her to give up, the "
                          "two lines have to be found together, and there is no formula "
                          "— it needs four equations and a computer. The paper does "
                          "that, and prints the answers. Nought point seven two, and "
                          "one point six two."):
            self.play(FadeIn(hard), run_time=1.4)
        self.beat()

        self.close_chapter([
            "one square root gives the steepness: 2.158",
            "steepness ÷ (steepness − 1) is the multiplier: 1.86",
            "40% choppiness → 3.30;  2% cost of capital → 2.62",
            "both dials shrink the steepness, so both raise the bar",
        ])
