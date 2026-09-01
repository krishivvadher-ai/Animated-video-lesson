import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.scale import MasterScale
from lib.theme import *


class Chapter05(Chapter):
    CH = 5
    TITLE = "Why waiting is worth money"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["scale", "fog", "money", "people"]

    def body(self):
        # ------------------------------------------------ on the line
        self.heading("Stand her exactly on the line")
        sc = MasterScale(x=-5.6, y=-0.3, height=4.2)
        line = sc.add_level("M", 1.10, "", COST, width=7.4)
        mtxt = Text("Marshall's line", font=FONT, font_size=T_SMALL, color=COST)
        mtxt.next_to(line[0], UP, buff=0.18).align_to(line[0], RIGHT).shift(LEFT * 0.2)
        line[1].become(mtxt)
        with self.narrate("Put Nell exactly on Marshall's line. Exactly on it. The "
                          "money coming in is precisely enough to cover everything, "
                          "including the cost of her money."):
            self.play(Create(sc.axis), FadeIn(sc.arrow_head), run_time=0.9)
            self.play(Create(line[0]), FadeIn(line[1]), run_time=1.1)

        marshall = stick.marshall(scale=0.75)
        marshall.move_to(St.STAGE.point(-0.55, -0.75))
        with self.narrate("Marshall says she should be indifferent. Build, or do not "
                          "build. It makes no difference either way."):
            self.play(FadeIn(marshall), run_time=0.6)
            b = marshall.say("Indifferent.", direction=UP, width=2.6)
            self.play(FadeIn(b), run_time=0.5)
            self.play(FadeOut(b), run_time=0.4)

        ava = stick.ava(scale=0.75)
        ava.move_to(St.STAGE.point(0.25, -0.75))
        with self.narrate("Hang on. There is a third thing she could do, and neither of "
                          "those is it.", v="c"):
            self.play(FadeIn(ava), run_time=0.5)
            q = ava.say("She could wait.", direction=UP, width=2.6)
            self.play(FadeIn(q), run_time=0.5)
            self.play(FadeOut(q), FadeOut(marshall), FadeOut(ava), run_time=0.5)

        # ------------------------------------------------ the plan
        self.heading("One very simple plan")
        plan = St.points(["wait a fixed stretch of time",
                          "then look at the money coming in",
                          "above the line → build. Else, never."],
                         colour=WAIT, dot_colour=WAIT, size=T_BODY, width=22)
        St.place(plan, St.SIDE)
        says = ["Give her one very simple plan. Wait a fixed stretch of time.",
                "Then look at the money coming in.",
                "If it is above the line, build. If it is not, never build. It is not "
                "even the best plan — it is just a plan, and it is enough to make the "
                "point."]
        for i, row in enumerate(plan):
            with self.narrate(says[i]):
                self.play(FadeIn(row), run_time=0.7)
        self.beat()
        self.play(FadeOut(plan), run_time=0.5)

        # ------------------------------------------------ five futures
        self.heading("Five futures, from one point")
        start = sc.pos(1.10)
        seed = Dot(start, radius=0.13, color=CHALK)
        self.play(FadeIn(seed), run_time=0.5)

        ends = [1.62, 1.36, 1.10, 0.90, 0.70]
        colours = [MONEY, MONEY, MUTED, COST, COST]
        paths, dots = VGroup(), VGroup()
        for e, c in zip(ends, colours):
            p = VMobject(color=c, stroke_width=4)
            pts = [start]
            for i in range(1, 9):
                a = i / 8
                v = 1.10 + (e - 1.10) * a + 0.05 * np.sin(i * 2.1) * (1 - a)
                pts.append(sc.pos(v) + RIGHT * (6.2 * a))
            p.set_points_smoothly(pts)
            paths.add(p)
            dots.add(Dot(p.get_end(), radius=0.10, color=c))

        with self.narrate("Now watch what the future might do, starting from that "
                          "point. Here are five futures. Nobody knows which one "
                          "happens. Some end high. Some end low."):
            self.play(S.lag_map(Create, paths, lag=0.12), run_time=2.8)
            self.play(FadeIn(dots), run_time=0.5)

        gains = VGroup(*[Text("builds — gains", font=FONT, font_size=T_SMALL,
                              color=MONEY).next_to(dots[i], RIGHT, buff=0.22)
                         for i in (0, 1)])
        with self.narrate("In the two futures that end high, she looks, she sees the "
                          "money is well above the line, and she builds. She gains."):
            self.play(FadeIn(gains), run_time=0.9)

        zeros = VGroup(*[Text("does not build", font=FONT, font_size=T_SMALL,
                              color=MUTED).next_to(dots[i], RIGHT, buff=0.22)
                         for i in (3, 4)])
        with self.narrate("In the two that end low, she looks, and she does not build. "
                          "She gains nothing."):
            self.play(FadeIn(zeros), run_time=0.9)

        key = St.caption("gains nothing — but loses nothing", CHALK, T_SUB, width=34)
        St.place(key, St.FOOT, pad=0.06)
        with self.narrate("But look at that again, because everything turns on it. She "
                          "gains nothing — and she loses nothing."):
            self.play(FadeIn(key), run_time=0.8)
            self.play(S.flash_around(key, WAIT, run_time=2.0))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the arithmetic
        self.heading("So do the sum")
        pos_bars = VGroup(*[Rectangle(width=0.8, height=h, color=MONEY, stroke_width=3,
                                      fill_color=MONEY, fill_opacity=0.32)
                            for h in (1.6, 1.0)])
        zero_bars = VGroup(*[Rectangle(width=0.8, height=0.04, color=MUTED,
                                       stroke_width=3, fill_color=MUTED,
                                       fill_opacity=0.32) for _ in range(3)])
        row = VGroup(*pos_bars, *zero_bars).arrange(RIGHT, buff=0.45, aligned_edge=DOWN)
        St.place(row, St.STAGE, ay=-0.1)
        base = Line(row.get_left() + LEFT * 0.3, row.get_right() + RIGHT * 0.3,
                    color=MUTED, stroke_width=2)
        base.move_to(row.get_bottom())
        with self.narrate("Two outcomes that pay something. Three that pay nothing at "
                          "all — but cost nothing either."):
            self.play(Create(base), run_time=0.5)
            self.play(S.lag_map(FadeIn, row, lag=0.15), run_time=1.6)

        avg = Line(row.get_left() + LEFT * 0.3, row.get_right() + RIGHT * 0.3,
                   color=TRIGGER, stroke_width=5)
        avg.move_to(row.get_bottom() + UP * 0.52)
        al = St.caption("the average is above zero", TRIGGER, T_BODY, width=20)
        St.place(al, St.SIDE, ay=0.2)
        with self.narrate("Weigh each by how likely it is, and add them up. The answer "
                          "is bigger than nothing. It cannot be anything else."):
            self.play(Create(avg), run_time=1.0)
            self.play(FadeIn(al), run_time=0.7)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the sentence
        self.drop_heading()
        sentence = St.caption("waiting cuts off the bad half\nand keeps the good half",
                              CHALK, T_HEAD, width=32)
        St.place(sentence, St.WIDE, ay=0.25)
        with self.narrate("Here is the sentence this chapter exists for. Waiting cuts "
                          "off the bad half, and keeps the good half."):
            self.play(Write(sentence), run_time=2.4)
        # the first of the film's three scripted silences
        self.wait(3.2)
        under = St.caption("that is what waiting is worth", WAIT, T_SUB, width=30)
        St.place(under, St.FOOT, pad=0.06)
        with self.narrate("That selective removal of risk is what waiting is worth."):
            self.play(FadeIn(under), run_time=0.9)
        self.wait(1.0)
        self.clear_stage()

        # ------------------------------------------------ not about nerves
        self.heading("And it is not about nerves")
        n2 = stick.nell(scale=1.0)
        St.place(n2, St.STAGE, ax=-0.55, ay=-0.2)
        self.play(FadeIn(n2), run_time=0.6)
        t1 = St.caption("nothing to do with disliking risk", TRIGGER, T_SUB, width=22)
        St.place(t1, St.SIDE, ay=0.5)
        with self.narrate("This is the most counter-intuitive part of the chapter, so I "
                          "am going to say it twice. It has nothing whatsoever to do "
                          "with disliking risk."):
            self.play(FadeIn(t1), run_time=0.9)
        self.beat()
        t2 = St.caption("she would take a fair gamble\nand she still waits",
                        CHALK, T_BODY, width=22)
        St.place(t2, St.SIDE, ay=-0.1)
        with self.narrate("Nell is assumed not to mind risk at all. She would take a "
                          "fair gamble without blinking. And she still waits."):
            self.play(FadeIn(t2), n2.mood("neutral"), run_time=0.9)
        self.beat()
        t3 = St.caption("risk now versus risk later", WAIT, T_SUB, width=22)
        St.place(t3, St.SIDE, ay=-0.7)
        with self.narrate("The trade she is making is between risk now and risk later. "
                          "It is about timing, not nerves."):
            self.play(FadeIn(t3), run_time=0.9)
            self.play(S.flash_around(t3, WAIT))
        self.beat()

        self.close_chapter([
            "start exactly on the textbook's line",
            "good futures pay · bad ones cost nothing",
            "gains + zeros > nothing, so waiting wins",
            "and none of it is about disliking risk",
        ])
