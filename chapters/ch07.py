import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter07(Chapter):
    CH = 7
    TITLE = "A right, but not an obligation"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["voucher", "door", "money", "clock"]

    def body(self):
        # ------------------------------------------------ the voucher
        self.heading("A voucher, and what it is worth")
        nell = stick.nell(scale=0.95)
        St.place(nell, St.STAGE, ax=-0.8, ay=-0.35)
        self.play(FadeIn(nell), run_time=0.6)

        v = W.ticket(SUNK, "£40 for this bicycle,\nany day you like", 1.0)
        St.place(v, St.STAGE, ax=0.2, ay=0.35)
        with self.narrate("Forget factories for two minutes. Somebody gives Nell a "
                          "voucher. It says: you may buy this bicycle for forty pounds, "
                          "on any day you like. It never expires. And it never forces "
                          "you to buy anything."):
            self.play(Create(v), run_time=1.4)
        self.beat()

        q = St.caption("is it worth anything\nbefore she uses it?", CHALK, T_SUB, width=20)
        St.place(q, St.SIDE, ay=0.4)
        with self.narrate("Question. Is the voucher worth anything before she uses it?",
                          v="c"):
            self.play(FadeIn(q), nell.mood("thinking"), run_time=0.8)
        self.beat()
        yes = St.caption("of course — somebody would buy it", MONEY, T_BODY, width=22)
        St.place(yes, St.SIDE, ay=-0.15)
        with self.narrate("Of course it is. Somebody would buy it off her. It gives her "
                          "a right she would not otherwise have, and it never obliges "
                          "her to do anything at all."):
            self.play(FadeIn(yes), nell.mood("pleased"), run_time=0.8)
        self.beat()

        gone = St.caption("use it, and it is gone", COST, T_SUB, width=20)
        St.place(gone, St.SIDE, ay=-0.65)
        with self.narrate("And here is the point. The moment she uses it, the voucher "
                          "is gone. She has a bicycle instead. She cannot use it again, "
                          "and she cannot sell it on."):
            self.play(FadeIn(gone), run_time=0.8)
            self.play(v.animate.set_opacity(0.25), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the mapping
        self.heading("Now map it across")
        rows = [("the voucher", "the chance to build", MONEY),
                ("the £40 price", "the sunk cost", SUNK),
                ("the bicycle", "the revenue, later", CHALK)]
        left = VGroup(*[Text(a, font=FONT, font_size=T_BODY, color=c)
                        for a, b, c in rows])
        right = VGroup(*[Text(b, font=FONT, font_size=T_BODY, color=c)
                         for a, b, c in rows])
        left.arrange(DOWN, buff=0.95, aligned_edge=RIGHT)
        right.arrange(DOWN, buff=0.95, aligned_edge=LEFT)
        pair = VGroup(left, right).arrange(RIGHT, buff=2.4)
        St.place(pair, St.FULL, ay=0.0)
        arrows = VGroup(*[Line(l.get_right() + RIGHT * 0.25, r.get_left() + LEFT * 0.25,
                              color=MUTED, stroke_width=3).add_tip(tip_length=0.16)
                          for l, r in zip(left, right)])
        says = ["The voucher is the chance to build.",
                "The forty pounds is the sunk cost — the money she cannot get back.",
                "And the bicycle is all the revenue the factory will ever earn."]
        for i in range(3):
            with self.narrate(says[i]):
                self.play(FadeIn(left[i]), run_time=0.5)
                self.play(Create(arrows[i]), run_time=0.5)
                self.play(FadeIn(right[i]), run_time=0.5)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ two values
        self.heading("Two values, not one")
        self.define("intrinsic value", "What using the chance right now would give you.",
                    "money", MONEY, at=UP * 1.3, hold=4.0)
        self.define("holding premium", "What the waiting itself is worth.", "clock",
                    WAIT, at=DOWN * 1.3, hold=4.2)

        self.clear_stage()
        self.drop_heading()
        rule = St.caption("use it when the holding premium\nhas fallen to zero",
                          CHALK, T_HEAD, width=32)
        St.place(rule, St.WIDE, ay=0.2)
        with self.narrate("Which gives the rule, in one line. Use the chance when the "
                          "holding premium has fallen to zero. Not before."):
            self.play(Write(rule), run_time=2.2)
        self.beat()
        with self.narrate("Before that point, waiting is still worth something, and "
                          "building throws it away for nothing."):
            self.foot("before that, building throws it away", WAIT)
            self.play(S.flash_around(rule, TRIGGER, run_time=2.0))
        self.beat()

        self.close_chapter([
            "a right, not an obligation",
            "worth something before it is used",
            "intrinsic value: using it now",
            "holding premium → zero, then build",
        ])
