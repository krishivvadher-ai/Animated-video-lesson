import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.scale import MasterScale
from lib.theme import *


class Chapter05(Chapter):
    CH = 5
    TITLE = "Why waiting is worth money"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ['scale', 'fog', 'money', 'people']

    def body(self):
        # -------------------------------------------------- set her on the line
        sc = MasterScale(x=-4.6, y=-0.2, height=4.4)
        line = sc.add_level("M", 1.10, "", COST, width=9.6)
        mtxt = Text("Marshall's build-line", font=FONT, font_size=T_SMALL, color=COST)
        mtxt.next_to(line[0], UP, buff=0.16).align_to(line[0], RIGHT).shift(LEFT * 0.2)
        line[1].become(mtxt)
        with self.narrate("Put Nell exactly on Marshall's line. Exactly on it. The "
                          "money coming in is precisely enough to cover everything, "
                          "including the cost of her money."):
            self.play(Create(sc.axis), FadeIn(sc.arrow_head), FadeIn(sc.title), run_time=1.2)
            self.play(Create(line[0]), FadeIn(line[1]), run_time=1.0)

        nell = stick.nell(scale=0.9)
        nell.move_to(sc.pos(1.10) + RIGHT * 3.2 + UP * 1.3)
        self.play(FadeIn(nell), run_time=0.6)

        m = stick.marshall(scale=0.8).move_to(RIGHT * 4.9 + DOWN * 1.9)
        with self.narrate("Marshall says she should be indifferent. Build, or do not "
                          "build. It makes no difference either way."):
            self.play(FadeIn(m), run_time=0.6)
            b = m.say("Indifferent.", direction=UP, width=2.6)
            self.play(FadeIn(b), run_time=0.5)
            self.wait(0.6)
            self.play(FadeOut(b), run_time=0.4)

        ava = stick.ava(scale=0.8).move_to(RIGHT * 1.3 + DOWN * 2.0)
        with self.narrate("Hang on. There is a third thing she could do, and neither of "
                          "those is it.", v="c"):
            self.play(FadeIn(ava), run_time=0.5)
            q = ava.say("She could wait.", direction=UP, width=2.6)
            self.play(FadeIn(q), run_time=0.5)
            self.wait(0.5)
            self.play(FadeOut(q), FadeOut(m), run_time=0.4)

        # -------------------------------------------------- the strategy
        strat = cards.bullet_list([
            "Wait a fixed stretch of time.",
            "Then look at the money coming in.",
            "above the line → build. Else, never.",
        ], color=WAIT, width=32, size=T_BODY)
        strat.move_to(RIGHT * 2.6 + UP * 1.2)
        with self.narrate("Give her one very simple plan. It is not even the best plan "
                          "— it is just a plan, and it is enough to make the point."):
            self.play(FadeIn(strat[0], shift=RIGHT * 0.2), run_time=0.6)
        with self.narrate("Wait a fixed stretch of time. Then look at the money coming "
                          "in. If it is above the line, build. If it is not, never build."):
            self.play(FadeIn(strat[1], shift=RIGHT * 0.2), run_time=0.6)
            self.play(FadeIn(strat[2], shift=RIGHT * 0.2), run_time=0.6)
        self.beat()
        self.play(FadeOut(strat), FadeOut(nell), FadeOut(ava), run_time=0.6)

        # -------------------------------------------------- the branching futures
        start = sc.pos(1.10)
        seed = Dot(start, radius=0.12, color=CHALK)
        with self.narrate("Now watch what the future might do, starting from that "
                          "point. Here are five futures. Nobody knows which one happens."):
            self.play(FadeIn(seed), run_time=0.5)

        ends = [1.62, 1.36, 1.10, 0.90, 0.70]
        colors = [MONEY, MONEY, MUTED, COST, COST]
        paths, dots = VGroup(), VGroup()
        for e, c in zip(ends, colors):
            p = VMobject(color=c, stroke_width=4)
            pts = [start]
            n = 8
            for i in range(1, n + 1):
                a = i / n
                v = 1.10 + (e - 1.10) * a + 0.055 * np.sin(i * 2.1) * (1 - a)
                pts.append(sc.pos(v) + RIGHT * (5.2 * a))
            p.set_points_smoothly(pts)
            paths.add(p)
            dots.add(Dot(p.get_end(), radius=0.09, color=c))

        with self.narrate("Some of them end up high. Some end up low. That is what "
                          "uncertainty looks like."):
            self.play(*[Create(p) for p in paths], run_time=2.6)
            self.play(FadeIn(dots), run_time=0.5)

        # -------------------------------------------------- the good ones
        gains = VGroup()
        for i in (0, 1):
            t = Text("builds — gains", font=FONT, font_size=T_SMALL, color=MONEY)
            t.next_to(dots[i], RIGHT, buff=0.24)
            gains.add(t)
        with self.narrate("In the two futures that end up high, she looks, she sees "
                          "the money is well above the line, and she builds. She gains."):
            self.play(FadeIn(gains), run_time=0.8)

        zeros = VGroup()
        for i in (3, 4):
            t = Text("does not build — nothing", font=FONT, font_size=T_SMALL, color=MUTED)
            t.next_to(dots[i], RIGHT, buff=0.24)
            zeros.add(t)
        with self.narrate("In the two futures that end up low, she looks, and she does "
                          "not build. She gains nothing."):
            self.play(FadeIn(zeros), run_time=0.8)

        key = cards.body("She gains nothing — but she loses nothing.",
                         size=T_SUB, color=CHALK, width=30)
        key.to_edge(DOWN, buff=0.55)
        with self.narrate("But look at that again, because everything turns on it. She "
                          "gains nothing — and she loses nothing."):
            self.play(FadeIn(key), run_time=0.8)
            self.play(Circumscribe(key, color=WAIT, buff=0.2), run_time=1.4)
        self.beat()

        # -------------------------------------------------- the arithmetic
        self.clear_stage()
        sums = VGroup(
            Text("some outcomes", font=FONT, font_size=T_BODY, color=MONEY),
            Text("+", font=FONT, font_size=T_BODY, color=MUTED),
            Text("some zeros", font=FONT, font_size=T_BODY, color=MUTED),
        ).arrange(RIGHT, buff=0.5).shift(UP * 1.3)
        pos = Text("bigger than nothing", font=FONT, font_size=T_SUB, color=MONEY)
        pos.next_to(sums, DOWN, buff=0.9)
        arrow = Line(sums.get_bottom() + DOWN * 0.15, pos.get_top() + UP * 0.15,
                     color=MUTED, stroke_width=3).add_tip(tip_length=0.16)

        with self.narrate("So do the sum. Mix together some positive outcomes and some "
                          "zeros, and weigh each by how likely it is."):
            self.play(FadeIn(sums), run_time=0.9)
        with self.narrate("The answer is bigger than nothing. It cannot be anything "
                          "else."):
            self.play(Create(arrow), FadeIn(pos), run_time=1.0)
        self.beat()

        concl = cards.body("So waiting beats acting — here.",
                           size=T_SUB, color=CHALK, width=34)
        concl.next_to(pos, DOWN, buff=0.8)
        with self.narrate("Which means waiting beats acting, at the very point where "
                          "the textbook says she should not care either way. So the "
                          "textbook's line is in the wrong place."):
            self.play(FadeIn(concl), run_time=1.0)
        self.beat()

        # -------------------------------------------------- the sentence  (SILENCE)
        self.clear_stage()
        sentence = cards.body("Waiting lets her avoid the downside over that stretch "
                              "of time, while keeping the upside.",
                              size=T_HEAD, color=CHALK, width=30)
        sentence.move_to(UP * 0.3)
        with self.narrate("Here is the sentence. Waiting lets her avoid the downside "
                          "over that stretch of time, while keeping the upside."):
            self.play(Write(sentence), run_time=2.4)
        # --- scripted silence #1: the moment the value of waiting lands
        self.wait(3.2)
        under = cards.body("That is what waiting is worth.", size=T_SUB,
                           color=WAIT, width=30)
        under.next_to(sentence, DOWN, buff=0.8)
        with self.narrate("That selective removal of risk — cutting off the bad half "
                          "and keeping the good half — is what waiting is worth."):
            self.play(FadeIn(under), run_time=0.9)
        self.wait(1.0)

        # -------------------------------------------------- not about nerves
        self.clear_stage()
        n2 = stick.nell(scale=1.0).shift(LEFT * 4.4 + DOWN * 0.4)
        warn = Text("Say this one twice", font=FONT, font_size=T_SMALL, color=MUTED)
        warn.to_edge(UP, buff=0.7)
        t1 = cards.body("This has nothing to do with disliking risk.",
                        size=T_SUB, color=TRIGGER, width=26)
        t1.move_to(RIGHT * 1.6 + UP * 1.1)
        with self.narrate("One more thing, and it is the most counter-intuitive part "
                          "of the chapter, so I am going to say it twice."):
            self.play(FadeIn(n2), FadeIn(warn), run_time=0.7)
        with self.narrate("This has nothing whatsoever to do with disliking risk."):
            self.play(FadeIn(t1), run_time=0.8)
        self.beat()
        t2 = cards.body("She would take a fair gamble. She still waits.",
                        size=T_BODY, color=CHALK, width=32)
        t2.next_to(t1, DOWN, buff=0.8)
        with self.narrate("Nell is assumed not to mind risk at all. She would take a "
                          "fair gamble without blinking. And she still waits."):
            self.play(FadeIn(t2), n2.mood("neutral"), run_time=0.9)
        self.beat()
        t3 = cards.note("risk now vs risk later",
                        color=WAIT, size=T_BODY, width=44)
        t3.next_to(t2, DOWN, buff=0.7)
        with self.narrate("The trade she is making is between risk now and risk later. "
                          "It is not about nerves. It is about timing."):
            self.play(FadeIn(t3), run_time=0.9)
        self.beat()

        self.close_chapter([
            "start exactly on the textbook's line",
            "good futures pay · bad ones cost nothing",
            "gains + zeros > nothing",
            "None of this is about disliking risk.",
        ])
