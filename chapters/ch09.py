import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter09(Chapter):
    CH = 9
    TITLE = "Money later is worth less than money now"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["clock", "money", "scale", "flow"]

    def body(self):
        ava = stick.ava(scale=0.8)
        St.place(ava, St.STAGE, ax=-0.9, ay=-0.7)
        with self.narrate("The next five chapters do the mathematics. Properly, and "
                          "from the beginning. Nothing beyond square roots, fractions "
                          "and percentages is used, and everything is built in front "
                          "of you.", v="c"):
            self.play(FadeIn(ava), run_time=0.6)

        # ------------------------------------------------ now versus later
        self.heading("A hundred now, or a hundred later")
        now = VGroup(W.money_bag(MONEY, 1.05),
                     Text("£100 today", font=FONT, font_size=T_BODY, color=MONEY))
        now[1].next_to(now[0], DOWN, buff=0.28)
        later = VGroup(W.money_bag(MUTED, 1.05),
                       Text("£100 in a year", font=FONT, font_size=T_BODY, color=MUTED))
        later[1].next_to(later[0], DOWN, buff=0.28)
        pair = VGroup(now, later).arrange(RIGHT, buff=3.4)
        St.place(pair, St.STAGE, ay=0.35)
        with self.narrate("A hundred pounds today, and a hundred pounds in a year. "
                          "Which would you rather have?"):
            self.play(FadeIn(now), FadeIn(later), run_time=1.0)
        gt = Text(">", font=FONT, font_size=64, color=CHALK).move_to(pair.get_center())
        with self.narrate("Today, obviously. Because you could put today's hundred to "
                          "work, and have more than a hundred by next year."):
            self.play(Write(gt), run_time=0.8)
        self.beat()

        sums = VGroup(
            Text("£100  ×  1.05  =  £105", font=FONT, font_size=T_SUB, color=MONEY),
            Text("£105  ÷  1.05  =  £100", font=FONT, font_size=T_SUB, color=WAIT),
        ).arrange(DOWN, buff=0.6)
        St.place(sums, St.STAGE, ay=-0.62)
        with self.narrate("Put a hundred pounds somewhere paying five per cent, and in "
                          "a year you have a hundred and five."):
            self.play(Write(sums[0]), run_time=1.2)
        with self.narrate("Run that backwards, and it is a division. Divide by one "
                          "point nought five, and you have turned money later into "
                          "money now."):
            self.play(TransformFromCopy(sums[0], sums[1], path_arc=PI / 3),
                      run_time=1.6)
        self.beat()
        self.define("interest", "The extra a borrower pays for the use of money.",
                    "money", MONEY, hold=3.4)
        self.define("discounting", "Turning money you get later into what it is worth "
                    "today.", "clock", WAIT, at=UP * 1.4, hold=4.0)
        self.clear_stage(keep=[ava])

        # ------------------------------------------------ a stream for ever
        self.heading("A stream that never stops")
        ax = Axes(x_range=[0, 26, 5], y_range=[0, 6, 2], x_length=9.4, y_length=2.9,
                  axis_config=AXIS)
        St.place(ax, St.FULL, ay=0.05)
        xl = Text("year 1                        10                        20 …",
                  font=FONT, font_size=T_TINY, color=MUTED)
        xl.next_to(ax, DOWN, buff=0.22)
        self.play(Create(ax), FadeIn(xl), run_time=1.1)

        bars = VGroup(*[
            Rectangle(width=0.28, height=2.5, color=MONEY, stroke_width=2,
                      fill_color=MONEY, fill_opacity=0.35)
            .move_to(ax.c2p(i, 0) + UP * 1.25) for i in range(1, 25)])
        St.collapse_bars(bars)
        self.add(bars)
        with self.narrate("A factory that earns five pounds a year, for ever. Here is "
                          "the five pounds, arriving year after year."):
            self.play(St.grow_bars(bars, lag=0.06, run_time=2.4))

        targets = VGroup(*[
            Rectangle(width=0.28, height=2.5 / (1.05 ** i), color=MONEY,
                      stroke_width=2, fill_color=MONEY, fill_opacity=0.35)
            .move_to(ax.c2p(i, 0) + UP * (2.5 / (1.05 ** i)) / 2)
            for i in range(1, 25)])
        with self.narrate("But each one has to be discounted back. Year one is divided "
                          "once. Year two, twice. Year twenty, twenty times. So the "
                          "far-off ones shrink away almost to nothing — and that is why "
                          "the total does not run off to infinity."):
            self.play(*[Transform(b, t) for b, t in zip(bars, targets)], run_time=2.6)
        self.beat()

        answer = St.caption("£5  ÷  0.05  =  £100", MONEY, T_HEAD, width=22)
        St.place(answer, St.STAGE, ay=0.8)
        with self.narrate("Add up every one of them, all the way out to for ever, and "
                          "the sum is astonishingly simple. Five pounds, divided by "
                          "nought point nought five. A hundred pounds."):
            self.play(FadeIn(answer), run_time=1.0)
            self.play(S.flash_around(answer, MONEY))
        self.beat()
        with self.narrate("That is the only piece of machinery you need. The value of a "
                          "stream that goes on for ever is the yearly amount divided by "
                          "the rate. And the rate we divide by is the cost of capital."):
            self.foot("value  =  yearly amount  ÷  the rate", CHALK)
        self.beat()
        self.clear_stage(keep=[ava])

        # ------------------------------------------------ check it
        self.heading("Check it three times")
        rows = VGroup(
            Text("£5 a year at 5%   →   £100", font=FONT, font_size=T_SUB, color=MONEY),
            Text("£5 a year at 2%   →   £250", font=FONT, font_size=T_SUB, color=WAIT),
            Text("£5 a year at 10%  →   £50", font=FONT, font_size=T_SUB, color=COST),
        ).arrange(DOWN, buff=0.75, aligned_edge=LEFT)
        St.place(rows, St.FULL, ay=0.05)
        says = ["Five pounds a year at five per cent is worth a hundred.",
                "The same five pounds, when the rate is only two per cent, is worth two "
                "hundred and fifty. Cheaper money makes future income worth more.",
                "And at ten per cent it is worth only fifty. Expensive money makes "
                "future income worth less."]
        for i, row in enumerate(rows):
            with self.narrate(says[i]):
                self.play(FadeIn(row), run_time=0.8)
            self.beat(0.4)
        with self.narrate("Hold on to the middle one. It is going to matter enormously "
                          "in chapter thirteen."):
            self.play(S.flash_around(rows[1], WAIT, run_time=2.0))
        self.beat()

        self.close_chapter([
            "money later is worth less than money now",
            "discounting turns later money into today's",
            "a stream for ever = amount ÷ the rate",
            "cheaper money makes future income worth MORE",
        ])
