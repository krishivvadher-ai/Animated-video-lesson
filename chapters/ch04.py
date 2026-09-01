import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter04(Chapter):
    CH = 4
    TITLE = "The three ingredients"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["slab", "fog", "door", "clock"]

    def body(self):
        nell = stick.nell(scale=1.0)
        St.place(nell, St.STAGE, ax=-0.82, ay=-0.25)
        with self.narrate("Everything that follows rests on three things being true at "
                          "once. Each one gets a picture, and each one gets an icon you "
                          "will see again whenever it is in play."):
            self.play(FadeIn(nell), FadeIn(nell.label()), run_time=0.8)

        # ---------------------------------------------------- 1 sunk cost
        self.heading("One — money that cannot come back")
        slab = Rectangle(width=3.0, height=0.5, color=SUNK, stroke_width=4,
                         fill_color=SUNK, fill_opacity=0.22)
        St.place(slab, St.STAGE, ax=0.25, ay=-0.5)
        slabel = Text("concrete foundation", font=FONT, font_size=T_SMALL, color=SUNK)
        slabel.next_to(slab, DOWN, buff=0.22)
        bag = W.money_bag(SUNK, 1.0)
        St.place(bag, St.STAGE, ax=0.25, ay=0.55)

        with self.narrate("Nell pays for the concrete foundation of her new factory. "
                          "The money leaves her hands, and the slab appears."):
            self.play(FadeIn(bag), run_time=0.7)
            self.play(bag.animate.move_to(slab.get_center()).scale(0.35).set_opacity(0),
                      GrowFromEdge(slab, DOWN), FadeIn(slabel), run_time=1.5)
            self.remove(bag)

        back = W.flow_arrow(slab.get_center() + UP * 0.45,
                            slab.get_center() + UP * 1.7, MUTED, sw=4)
        cross = VGroup(
            Line(LEFT * 0.4 + UP * 0.4, RIGHT * 0.4 + DOWN * 0.4, color=COST, stroke_width=7),
            Line(LEFT * 0.4 + DOWN * 0.4, RIGHT * 0.4 + UP * 0.4, color=COST, stroke_width=7),
        ).move_to(slab.get_center() + UP * 1.7)
        with self.narrate("Now she changes her mind, and tries to sell the foundation "
                          "back. Nobody wants a hole in a field with concrete in it."):
            self.play(nell.mood("worried"), run_time=0.4)
            self.play(Create(back), run_time=0.7)
            self.play(Create(cross), run_time=0.6)
            self.play(FadeOut(back), run_time=0.4)

        self.define("sunk cost", "Money that cannot be got back if you change your "
                    "mind.", "slab", SUNK, at=UP * 1.2, hold=4.2)
        note = St.caption("sunk ≠ expensive", SUNK, T_SUB, width=18)
        St.place(note, St.SIDE, ay=0.4)
        with self.narrate("And be careful. Sunk is not the same as expensive. A lorry "
                          "is expensive and you can sell it again. A hole in the ground "
                          "is cheap, and you cannot."):
            self.play(FadeIn(note), run_time=0.8)
            self.play(S.flash_around(note, SUNK))
        self.beat()
        self.clear_stage(keep=[nell])

        # ---------------------------------------------------- 2 uncertainty
        self.heading("Two — a future you learn slowly")
        future = Text("next year's\ncustomers", font=FONT, font_size=T_SUB,
                      color=CHALK, line_spacing=0.9)
        St.place(future, St.STAGE, ax=0.3, ay=0.0)
        cloud = W.fog(width=5.4, height=2.8, n=9)
        cloud.move_to(future)
        with self.narrate("Second ingredient. Nell does not know what next year holds. "
                          "Will there be customers? How many? At what price?"):
            self.play(FadeIn(future), run_time=0.6)
            self.play(FadeIn(cloud), nell.mood("thinking"), run_time=1.0)

        months = St.points(["one month on", "two months on", "three months on"],
                           colour=WAIT, dot_colour=WAIT, size=T_BODY, width=16)
        St.place(months, St.SIDE)
        with self.narrate("But the fog thins. Every month that passes tells her a "
                          "little more than she knew the month before."):
            for i, row in enumerate(months):
                self.play(FadeIn(row),
                          cloud.animate.set_opacity(0.55 - 0.17 * (i + 1)),
                          run_time=0.9)

        self.define("ongoing uncertainty", "You do not know what is coming, and you "
                    "learn a little at a time.", "fog", WAIT, at=DOWN * 2.2, hold=4.2)
        self.clear_stage(keep=[nell])

        # ---------------------------------------------------- 3 the door
        self.heading("Three — a chance that keeps")
        d = W.door(MONEY, 1.4, 2.7, "the chance to build")
        St.place(d, St.STAGE, ax=0.35, ay=-0.05)
        with self.narrate("Third. If she does not build this year, the chance is "
                          "generally still there next year. The door stays open."):
            self.play(Create(d), nell.mood("neutral"), run_time=1.2)

        years = St.points(["this year", "next year", "the year after"],
                          colour=MONEY, dot_colour=MONEY, size=T_BODY, width=16)
        St.place(years, St.SIDE)
        with self.narrate("This year. Next year. The year after that. Still open."):
            for row in years:
                self.play(FadeIn(row), run_time=0.5)
        self.play(FadeOut(d[2]), run_time=0.3)
        self.define("the chance keeps", "The opportunity does not vanish if you do not "
                    "take it today.", "door", MONEY, at=DOWN * 1.9, hold=3.6)
        self.clear_stage()

        # ---------------------------------------------------- the payoff
        self.heading("Put the three together")
        icons = VGroup(
            VGroup(cards.icon("slab", SUNK, 2.0),
                   St.caption("cannot get it back", SUNK, T_SMALL, width=14)),
            VGroup(cards.icon("fog", WAIT, 2.0),
                   St.caption("you learn slowly", WAIT, T_SMALL, width=14)),
            VGroup(cards.icon("door", MONEY, 2.0),
                   St.caption("the chance keeps", MONEY, T_SMALL, width=14)),
        )
        for g in icons:
            g.arrange(DOWN, buff=0.42)
        icons.arrange(RIGHT, buff=1.7)
        St.place(icons, St.FULL, ay=0.35)
        with self.narrate("Money you cannot get back. A future you learn about slowly. "
                          "And a chance that keeps."):
            self.play(S.lag_map(FadeIn, icons, shift=UP * 0.3, lag=0.25),
                      run_time=1.8)

        payoff = St.caption("waiting is worth money", TRIGGER, T_HEAD, width=26)
        St.place(payoff, St.FOOT, pad=0.06)
        with self.narrate("When all three are true, waiting is worth money."):
            self.play(FadeIn(payoff), run_time=0.9)
            self.play(S.flash_around(payoff, TRIGGER))
        self.beat()
        with self.narrate("And when any one of them is missing, it is not. Remember "
                          "that — in chapter twenty we take the third one away, and "
                          "the whole conclusion flips over."):
            self.play(S.pulse(icons[2], COST, run_time=1.6))
        self.beat()

        self.close_chapter([
            "sunk cost: money you cannot get back",
            "a future you learn a bit at a time",
            "a chance that keeps",
            "all three → waiting pays",
        ])
