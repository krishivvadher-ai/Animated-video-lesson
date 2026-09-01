import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.theme import *


class Chapter07(Chapter):
    CH = 7
    TITLE = "A right, but not an obligation"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ['voucher', 'door', 'money', 'clock']

    def body(self):
        nell = stick.nell(scale=0.95).shift(LEFT * 4.9 + DOWN * 1.0)
        with self.narrate("Here is a way of holding the idea that makes it easy to "
                          "carry around. Forget factories for two minutes."):
            self.play(FadeIn(nell), run_time=0.6)

        v = W.ticket(SUNK, "£40 for this bicycle,\nany day you like", 1.0)
        v.move_to(RIGHT * 1.6 + UP * 1.5)
        with self.narrate("Somebody gives Nell a voucher. It says: you may buy this "
                          "bicycle for forty pounds, on any day you like. It never "
                          "expires. And it never forces you to buy anything."):
            self.play(FadeIn(v), run_time=1.0)
        self.beat()

        q = cards.body("Is the voucher worth anything before she uses it?",
                       size=T_SUB, color=CHALK, width=28)
        q.next_to(v, DOWN, buff=0.9)
        with self.narrate("Question. Is the voucher worth anything before she uses it?",
                          v="c"):
            self.play(FadeIn(q), nell.mood("thinking"), run_time=0.8)
        self.beat()
        with self.narrate("Of course it is. Somebody would buy it off her. It gives "
                          "her a right she would not otherwise have, and it never "
                          "obliges her to do anything at all."):
            self.play(nell.mood("pleased"), run_time=0.5)
        self.play(FadeOut(q), run_time=0.4)

        # ------------------------------------------------------ using it
        used = cards.body("The moment she uses it, the voucher is gone.",
                          size=T_SUB, color=COST, width=28)
        used.next_to(v, DOWN, buff=0.9)
        with self.narrate("And here is the point. The moment she uses it, the voucher "
                          "is gone. She has a bicycle instead. She cannot use it again, "
                          "and she cannot sell it on."):
            self.play(FadeIn(used), run_time=0.8)
            self.play(v.animate.set_opacity(0.25), run_time=0.8)
        self.beat()
        self.play(FadeOut(used), FadeOut(v), run_time=0.5)

        # ------------------------------------------------------ the mapping
        rows = [
            ("the voucher", "the chance to build", MONEY),
            ("the £40 price", "the sunk cost", SUNK),
            ("the bicycle", "all the revenue the factory will earn", CHALK),
        ]
        left = VGroup(*[Text(a, font=FONT, font_size=T_BODY, color=c) for a, b, c in rows])
        right = VGroup(*[cards.body(b, size=T_BODY, color=c, width=24) for a, b, c in rows])
        left.arrange(DOWN, buff=0.95, aligned_edge=RIGHT)
        right.arrange(DOWN, buff=0.95, aligned_edge=LEFT)
        pair = VGroup(left, right).arrange(RIGHT, buff=2.0).shift(RIGHT * 0.8 + UP * 0.2)
        arrows = VGroup(*[Line(l.get_right() + RIGHT * 0.2, r.get_left() + LEFT * 0.2,
                               color=MUTED, stroke_width=3).add_tip(tip_length=0.14)
                          for l, r in zip(left, right)])

        with self.narrate("Now map it across, one line at a time."):
            self.play(FadeOut(nell), run_time=0.4)
        for i in range(3):
            texts = ["The voucher is the chance to build.",
                     "the sunk cost",
                     "all the revenue, later"]
            with self.narrate(texts[i]):
                self.play(FadeIn(left[i]), run_time=0.5)
                self.play(Create(arrows[i]), FadeIn(right[i]), run_time=0.8)
        self.beat()
        self.play(FadeOut(pair), FadeOut(arrows), run_time=0.6)

        # ------------------------------------------------------ two values
        self.define("intrinsic value", "What using it now would give you.", "money", MONEY,
                    narration="Two words for two different values. Intrinsic value is "
                              "what she would get by using the chance right now.",
                    at=UP * 1.5, hold=4.0)
        self.define("holding premium", "What the waiting itself is worth.", "clock", WAIT,
                    narration="And the holding premium — some people call it time value "
                              "— is what the waiting itself is worth.",
                    at=DOWN * 1.4, hold=4.4)

        self.clear_stage()
        rule = cards.body("Use it when the holding premium hits zero.",
                          size=T_HEAD, color=CHALK, width=30)
        rule.move_to(UP * 0.5)
        with self.narrate("And that gives the rule, in one line. Use the chance when "
                          "the holding premium has fallen to zero. Not before."):
            self.play(Write(rule), run_time=2.0)
        self.beat()
        why = cards.body("waiting still pays · building throws it away", size=T_BODY, color=WAIT, width=40)
        why.next_to(rule, DOWN, buff=0.8)
        with self.narrate("Before that point, waiting is still worth something, and "
                          "building throws it away for nothing."):
            self.play(FadeIn(why), run_time=0.8)
        self.beat()

        foot = cards.note("the mathematics is in the paper's appendix",
                          width=60)
        foot.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(foot), run_time=0.5)
        self.wait(1.6)

        self.close_chapter([
            "a right, not an obligation",
            "worth something before it is used",
            "intrinsic value: using it now",
            "holding premium → zero, then build",
        ])
