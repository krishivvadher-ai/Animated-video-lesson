import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.scale import MasterScale
from lib.theme import *


class Chapter17(Chapter):
    CH = 17
    TITLE = "Hysteresis"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["scale", "door", "magnet", "border"]

    def body(self):
        # ------------------------------------------------ the path
        self.heading("Walk one path, and watch what it leaves")
        sc = MasterScale(x=-5.9, y=-0.35, height=4.6)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), run_time=0.8)
        for k, v, t, c, sw in [("L", 0.72, "0.72", TRIGGER, 5),
                               ("M", 1.10, "1.10", COST, 3),
                               ("H", 1.62, "1.62", TRIGGER, 5)]:
            g = sc.add_level(k, v, t, c, width=11.6, sw=sw)
            g[1].next_to(g[0], LEFT, buff=0.18)
            self.play(Create(g[0]), FadeIn(g[1]), run_time=0.5)

        t = ValueTracker(1.00)
        xt = ValueTracker(0.0)
        dot = always_redraw(lambda: Dot(sc.pos(t.get_value()) + RIGHT * xt.get_value(),
                                        radius=0.14, color=MONEY))
        trail = TracedPath(dot.get_center, stroke_color=MONEY, stroke_width=4)
        self.add(trail, dot)
        nell = stick.nell(scale=0.62)
        nell.move_to(St.STAGE.point(0.95, -0.85))
        self.play(FadeIn(nell), run_time=0.4)

        with self.narrate("She starts at one. Money coming in exactly covers the "
                          "day-to-day costs. Nothing is built."):
            self.play(xt.animate.set_value(1.2), run_time=1.2, rate_func=linear)
        with self.narrate("It rises. It crosses one point one — the textbook's "
                          "build-line — and nothing happens. She does not build."):
            self.play(t.animate.set_value(1.28), xt.animate.set_value(3.0),
                      run_time=2.2, rate_func=linear)
            self.play(nell.mood("thinking"), run_time=0.4)
        with self.narrate("It keeps rising. And at one point six two, she builds."):
            self.play(t.animate.set_value(1.66), xt.animate.set_value(5.4),
                      run_time=2.4, rate_func=linear)
        fac = W.factory(MONEY, 0.42)
        fac.move_to(sc.pos(1.66) + RIGHT * 5.4 + UP * 1.0)
        self.play(Create(fac), nell.mood("pleased"), run_time=0.8)

        with self.narrate("Now the money coming in starts to fall. Back past one point "
                          "six two. Back past one point one."):
            self.play(t.animate.set_value(1.20), xt.animate.set_value(7.6),
                      run_time=2.4, rate_func=linear)
        with self.narrate("All the way back down to one — exactly where it started."):
            self.play(t.animate.set_value(1.00), xt.animate.set_value(9.6),
                      run_time=2.2, rate_func=linear)
        self.beat()

        # the second of the film's three scripted silences
        stays = St.caption("she does not close", CHALK, T_HEAD, width=22)
        St.place(stays, St.FOOT, pad=0.06)
        self.play(FadeIn(stays), run_time=0.9)
        self.wait(3.4)
        with self.narrate("The cause has completely reversed. The effect has not."):
            self.play(S.pulse(fac, MONEY, run_time=1.5))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the physics
        self.heading("Why the paper borrows a word from physics")
        bar = W.iron_bar(CHALK).scale(1.25)
        St.place(bar, St.STAGE, ay=0.35)
        with self.narrate("Take an iron bar, and loop a wire around it."):
            self.play(Create(bar), run_time=1.4)
        cur = St.caption("current on", SUNK, T_SUB, width=16)
        St.place(cur, St.SIDE, ay=0.55)
        mag = cards.icon("magnet", TRIGGER, 2.6)
        mag.next_to(bar, DOWN, buff=0.55)
        with self.narrate("Pass an electric current through the wire, and the iron "
                          "becomes magnetic."):
            self.play(FadeIn(cur), bar[2].animate.set_stroke(TRIGGER, width=7),
                      run_time=1.0)
            self.play(Create(mag), run_time=0.8)
        off = St.caption("current off", MUTED, T_SUB, width=16)
        St.place(off, St.SIDE, ay=0.55)
        with self.narrate("Now switch the current off."):
            self.play(FadeTransform(cur, off), bar[2].animate.set_stroke(SUNK, width=4),
                      run_time=1.1)
        with self.narrate("The magnetism does not go away. Some of it stays. The cause "
                          "was temporary. The effect lasted."):
            self.play(S.pulse(mag, TRIGGER, run_time=1.4))
        self.beat()
        self.define("hysteresis", "When the cause is reversed and the effect stays "
                    "behind.", "magnet", TRIGGER, at=DOWN * 2.1, hold=4.4)
        self.clear_stage()

        # ------------------------------------------------ in reverse
        self.heading("And it works in reverse")
        self.side(["push far enough down → she quits",
                   "let it recover, all the way",
                   "she does not come back"],
                  colour=CHALK, dot_colour=COST, width=22, region=St.FULL,
                  spoken=["Push the money coming in far enough down, and she quits for "
                          "good.",
                          "Now let it recover, all the way back to where it started.",
                          "She does not come back. Because coming back means paying the "
                          "whole sunk cost over again."])
        self.beat()
        with self.narrate("And the paper's own careful point. Sunk costs alone can "
                          "produce some of this. Adding uncertainty magnifies it "
                          "dramatically."):
            self.foot("sunk costs alone: some · uncertainty: far more", MUTED)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the payoff
        self.heading("Now go back to chapter three")
        ax = Axes(x_range=[1980, 1990, 2], y_range=[0, 3, 1], x_length=8.4,
                  y_length=3.2, axis_config=AXIS)
        St.place(ax, St.FULL, ay=-0.1)
        dollar = ax.plot_line_graph(
            x_values=[1980, 1982, 1984, 1985, 1986, 1987, 1989],
            y_values=[1.4, 1.9, 2.3, 2.2, 1.7, 1.45, 1.42],
            line_color=WAIT, add_vertex_dots=False, stroke_width=5)
        imports = ax.plot_line_graph(
            x_values=[1980, 1982, 1983, 1985, 1987, 1989],
            y_values=[0.55, 0.55, 0.7, 1.5, 2.1, 2.25],
            line_color=MONEY, add_vertex_dots=False, stroke_width=5)
        dl = Text("the dollar", font=FONT, font_size=T_SMALL, color=WAIT)
        dl.next_to(ax, UP, buff=0.12).shift(LEFT * 2.4)
        il = Text("imports", font=FONT, font_size=T_SMALL, color=MONEY)
        il.next_to(ax, RIGHT, buff=0.15).shift(UP * 0.7)
        with self.narrate("The dollar rose, and foreign firms poured into America — "
                          "years late, because they were waiting to be sure."):
            self.play(Create(ax), run_time=0.8)
            self.play(Create(dollar), FadeIn(dl), run_time=1.8)
            self.play(Create(imports), FadeIn(il), run_time=1.8)
        with self.narrate("Then the dollar fell back to where it had been. And they did "
                          "not leave. They had paid to get in, and leaving would mean "
                          "paying to get back in again later."):
            self.play(S.pulse(imports, MONEY, run_time=1.6))
        self.beat()
        with self.narrate("The cause reversed. The effect stayed. That is all "
                          "hysteresis is — and now you have watched it happen twice."):
            self.foot("cause reversed · effect stayed", TRIGGER)
        self.beat()

        self.close_chapter([
            "up past 1.10, nothing · past 1.62, she builds",
            "back to 1.00 — and she does not close",
            "the bar stays magnetic",
            "hysteresis explains the dollar and the imports",
        ])
