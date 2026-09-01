import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.theme import *


class Chapter09(Chapter):
    CH = 9
    TITLE = "Money later is worth less than money now"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["clock", "money", "scale", "flow"]

    def body(self):
        ava = stick.ava(scale=0.8).to_corner(DOWN + LEFT, buff=0.5)
        self.play(FadeIn(ava), run_time=0.5)
        with self.narrate("The next five chapters do the mathematics. Properly, and "
                          "from the beginning. Nothing beyond square roots, fractions "
                          "and percentages is used, and everything is built in front "
                          "of you.", v="c"):
            pass

        # ------------------------------------------------ £100 now vs later
        now = VGroup(W.money_bag(MONEY, 1.1), Text("£100 today", font=FONT,
                                                   font_size=T_BODY, color=MONEY))
        now[1].next_to(now[0], DOWN, buff=0.3)
        later = VGroup(W.money_bag(MUTED, 1.1), Text("£100 in a year", font=FONT,
                                                     font_size=T_BODY, color=MUTED))
        later[1].next_to(later[0], DOWN, buff=0.3)
        pair = VGroup(now, later).arrange(RIGHT, buff=4.0).move_to(UP * 0.6)
        with self.narrate("A hundred pounds today, and a hundred pounds in a year. "
                          "Which would you rather have?"):
            self.play(FadeIn(now), FadeIn(later), run_time=1.0)
        gt = Text(">", font=FONT, font_size=64, color=CHALK).move_to(pair.get_center())
        with self.narrate("Today, obviously. Because you could put today's hundred to "
                          "work, and have more than a hundred by next year."):
            self.play(Write(gt), run_time=0.8)
        self.beat()

        # ------------------------------------------------ the sum, forwards
        sums = VGroup(
            Text("£100  ×  1.05  =  £105", font=FONT, font_size=T_SUB, color=MONEY),
            Text("so £105 in a year  =  £100 today", font=FONT, font_size=T_SUB,
                 color=CHALK),
            Text("£105  ÷  1.05  =  £100", font=FONT, font_size=T_SUB, color=WAIT),
        ).arrange(DOWN, buff=0.6).move_to(DOWN * 1.2)
        with self.narrate("Put a hundred pounds somewhere paying five per cent, and in "
                          "a year you have a hundred and five."):
            self.play(FadeIn(sums[0]), run_time=0.8)
        with self.narrate("Run that backwards. A hundred and five pounds a year from "
                          "now is worth exactly a hundred pounds today."):
            self.play(FadeIn(sums[1]), run_time=0.8)
        with self.narrate("And that is a division. Divide by one point nought five, "
                          "and you have turned money later into money now."):
            self.play(FadeIn(sums[2]), run_time=0.8)
        self.beat()
        self.define("discounting", "Turning money you get later into what it is worth "
                    "today.", "clock", WAIT, at=UP * 2.2, hold=4.2)
        self.clear_stage(keep=[ava])

        # ------------------------------------------------ a stream for ever
        head = Text("Now do it for a stream that never stops",
                    font=FONT, font_size=T_SUB, color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)

        ax = Axes(x_range=[0, 26, 1], y_range=[0, 6, 1], x_length=10.4, y_length=3.2,
                  axis_config={"color": MUTED, "stroke_width": 2,
                               "include_ticks": False, "include_tip": False})
        ax.shift(DOWN * 0.4)
        xl = Text("year 1                    5                   10                  15                  20                 25 …",
                  font=FONT, font_size=T_TINY, color=MUTED)
        xl.next_to(ax, DOWN, buff=0.2)
        self.play(Create(ax), FadeIn(xl), run_time=0.9)

        bars, faded = VGroup(), VGroup()
        for i in range(1, 25):
            h = 5.0
            b = Rectangle(width=0.30, height=h * 0.5, color=MONEY, stroke_width=2,
                          fill_color=MONEY, fill_opacity=0.35)
            b.move_to(ax.c2p(i, 0) + UP * b.height / 2)
            bars.add(b)
        with self.narrate("A factory that earns five pounds a year, for ever. Here is "
                          "the five pounds, arriving year after year."):
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars],
                                  lag_ratio=0.15), run_time=2.4)

        with self.narrate("But each one has to be discounted back. The five pounds in "
                          "year one is divided once. Year two, twice. Year twenty, "
                          "twenty times. So the far-off ones shrink away almost to "
                          "nothing — and that is why the total does not run off to infinity."):
            targets = []
            for i, b in enumerate(bars):
                h = 5.0 * 0.5 / (1.05 ** (i + 1))
                nb = Rectangle(width=0.30, height=h, color=MONEY, stroke_width=2,
                               fill_color=MONEY, fill_opacity=0.35)
                nb.move_to(ax.c2p(i + 1, 0) + UP * h / 2)
                targets.append(nb)
            self.play(*[Transform(b, t) for b, t in zip(bars, targets)], run_time=2.4)
        self.beat()

        with self.narrate("Add up every one of them, all the way out to for ever, and "
                          "the total is not infinite. It settles on one number."):
            brace = Brace(bars, direction=UP, color=CHALK)
            self.play(FadeIn(brace), run_time=0.8)

        answer = VGroup(
            Text("£5  ÷  0.05  =  £100", font=FONT, font_size=T_HEAD, color=MONEY),
            Text("five pounds a year, for ever, at 5%", font=FONT, font_size=T_SMALL,
                 color=MUTED),
        ).arrange(DOWN, buff=0.35)
        answer.move_to(UP * 2.0)
        with self.narrate("And the sum is astonishingly simple. Five pounds, divided by "
                          "nought point nought five. A hundred pounds."):
            self.play(Write(answer[0]), run_time=1.6)
            self.play(FadeIn(answer[1]), run_time=0.6)
        self.beat()

        rule = Text("value  =  yearly amount  ÷  the rate", font=FONT,
                    font_size=T_SUB, color=CHALK)
        rule.to_edge(DOWN, buff=0.7)
        with self.narrate("That is the only piece of machinery you need. The value of a "
                          "stream that goes on for ever is the yearly amount divided by "
                          "the rate."):
            self.play(Write(rule), run_time=1.8)
        self.beat()
        with self.narrate("And the rate we divide by is the one from chapter two. The "
                          "cost of capital. What the money has to earn to be worth "
                          "using."):
            self.play(Indicate(rule, color=WAIT, scale_factor=1.04), run_time=1.2)
        self.beat()

        # ------------------------------------------------ check it
        self.clear_stage(keep=[ava])
        check = VGroup(
            Text("£5 a year at 5%   →   £5 ÷ 0.05  =  £100", font=FONT,
                 font_size=T_SUB, color=MONEY),
            Text("£5 a year at 2%   →   £5 ÷ 0.02  =  £250", font=FONT,
                 font_size=T_SUB, color=WAIT),
            Text("£5 a year at 10%  →   £5 ÷ 0.10  =  £50", font=FONT,
                 font_size=T_SUB, color=COST),
        ).arrange(DOWN, buff=0.7)
        says = ["Five pounds a year at five per cent is worth a hundred.",
                "The same five pounds, when the rate is only two per cent, is worth two "
                "hundred and fifty. Cheaper money makes future income worth more.",
                "And at ten per cent it is worth only fifty. Expensive money makes "
                "future income worth less."]
        for i in range(3):
            with self.narrate(says[i]):
                self.play(FadeIn(check[i], shift=RIGHT * 0.2), run_time=0.8)
            self.beat(0.5)
        with self.narrate("Hold on to the middle one. It is going to matter enormously "
                          "in chapter thirteen."):
            self.play(S.flash_around(check[1], color=WAIT, buff=0.2, stroke_width=4),
                      run_time=1.4)
        self.beat()

        self.close_chapter([
            "money later is worth less than money now",
            "discounting turns later money into today's money",
            "a stream for ever = yearly amount ÷ the rate",
            "cheaper money makes future income worth MORE",
        ])
