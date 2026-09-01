import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.scale import MasterScale
from lib.theme import *


class Chapter17(Chapter):
    CH = 17
    TITLE = "Hysteresis"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ['scale', 'door', 'magnet', 'border']

    def body(self):
        sc = MasterScale(x=-5.6, y=-0.3, height=5.0)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), FadeIn(sc.title), run_time=0.9)
        levels = {}
        for k, v, t, c, sw in [("L", 0.72, "0.72", TRIGGER, 5),
                               ("M", 1.10, "1.10", COST, 3),
                               ("H", 1.62, "1.62", TRIGGER, 5)]:
            g = sc.add_level(k, v, t, c, width=11.0, sw=sw)
            g[1].next_to(g[0], LEFT, buff=0.18)
            levels[k] = g
            self.play(Create(g[0]), FadeIn(g[1]), run_time=0.5)

        with self.narrate("This is the chapter the paper is named after. Watch one "
                          "path, and watch what it leaves behind."):
            pass

        t = ValueTracker(1.00)
        dot = always_redraw(lambda: Dot(sc.pos(t.get_value()) + RIGHT * 0.0,
                                        radius=0.14, color=MONEY))
        trail = TracedPath(dot.get_center, stroke_color=MONEY, stroke_width=4)
        self.add(trail, dot)
        nell = stick.nell(scale=0.7).move_to(RIGHT * 5.6 + DOWN * 2.2)
        self.play(FadeIn(nell), run_time=0.4)

        # animate horizontally as well: move the whole scale left slowly is complex,
        # so instead sweep the dot's x with a second tracker
        xt = ValueTracker(0.0)
        self.remove(trail, dot)
        dot = always_redraw(lambda: Dot(sc.pos(t.get_value()) + RIGHT * xt.get_value(),
                                        radius=0.14, color=MONEY))
        trail = TracedPath(dot.get_center, stroke_color=MONEY, stroke_width=4)
        self.add(trail, dot)

        with self.narrate("She starts at one. Money coming in is exactly covering the "
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
        fac = W.factory(MONEY, 0.5).move_to(sc.pos(1.66) + RIGHT * 5.4 + UP * 1.0)
        self.play(FadeIn(fac), nell.mood("pleased"), run_time=0.7)

        with self.narrate("Now the money coming in starts to fall. Back past one point "
                          "six two. Back past one point one."):
            self.play(t.animate.set_value(1.20), xt.animate.set_value(7.6),
                      run_time=2.4, rate_func=linear)

        with self.narrate("All the way back down to one — exactly where it started."):
            self.play(t.animate.set_value(1.00), xt.animate.set_value(9.4),
                      run_time=2.2, rate_func=linear)

        self.beat()
        # --- scripted silence #2: the moment the path returns and she does not close
        stays = cards.body("She does not close.", size=T_HEAD, color=CHALK, width=20)
        stays.move_to(RIGHT * 3.4 + DOWN * 2.3)
        self.play(FadeIn(stays), run_time=0.8)
        self.wait(3.4)

        with self.narrate("The cause has completely reversed. The effect has not."):
            self.play(Indicate(fac, color=MONEY, scale_factor=1.2), run_time=1.4)
        self.beat()

        # ------------------------------------------------------ the physics
        self.clear_stage()
        head = Text("Why the paper borrows a word from physics",
                    font=FONT, font_size=T_SUB, color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)

        bar = W.iron_bar(CHALK).scale(1.2).move_to(UP * 0.6)
        with self.narrate("Take an iron bar, and loop a wire around it."):
            self.play(Create(bar), run_time=1.2)

        cur = Text("current on", font=FONT, font_size=T_BODY, color=SUNK)
        cur.next_to(bar, DOWN, buff=0.7)
        with self.narrate("Pass an electric current through the wire, and the iron "
                          "becomes magnetic."):
            self.play(FadeIn(cur), bar[1].animate.set_stroke(SUNK, width=7), run_time=1.0)
            mag = cards.icon("magnet", TRIGGER, 2.4).next_to(bar, UP, buff=0.5)
            self.play(FadeIn(mag), run_time=0.6)

        with self.narrate("Now switch the current off."):
            off = Text("current off", font=FONT, font_size=T_BODY, color=MUTED)
            off.move_to(cur)
            self.play(Transform(cur, off), bar[1].animate.set_stroke(MUTED, width=3),
                      run_time=1.0)

        with self.narrate("The magnetism does not go away. Some of it stays. The cause "
                          "was temporary. The effect lasted."):
            self.play(mag.animate.set_color(TRIGGER).scale(0.9), run_time=1.0)
        self.beat()

        self.define("hysteresis", "Cause reversed. Effect stays.", "magnet", TRIGGER,
                    narration="Hysteresis. When the cause is reversed and the effect "
                              "stays behind. The paper borrows the word directly.",
                    at=DOWN * 2.0, hold=4.4)

        # ------------------------------------------------------ the reverse
        self.clear_stage()
        rev = cards.body("And it works in reverse.", size=T_SUB, color=CHALK, width=24)
        rev.to_edge(UP, buff=0.8)
        self.play(FadeIn(rev), run_time=0.5)
        steps = cards.bullet_list([
            "push far enough down → she quits",
            "let it recover, all the way",
            "she does not come back",
        ], color=CHALK, width=40)
        steps.move_to(DOWN * 0.2)
        says = ["push down ⇒ she quits",
                "Now let it recover, all the way back to where it started.",
                "she does not come back"]
        for i in range(3):
            with self.narrate(says[i]):
                self.play(FadeIn(steps[i], shift=RIGHT * 0.2), run_time=0.6)
        self.beat()
        care = cards.note("sunk costs alone: some\nuncertainty: far more",
                          width=60)
        care.to_edge(DOWN, buff=0.5)
        with self.narrate("And the paper's own careful point. Sunk costs alone can "
                          "produce some of this. Adding uncertainty magnifies it "
                          "dramatically."):
            self.play(FadeIn(care), run_time=0.9)
        self.beat()

        # ------------------------------------------------------ the payoff
        self.clear_stage()
        pay = Text("Now go back to chapter three", font=FONT, font_size=T_SUB,
                   color=CHALK).to_edge(UP, buff=0.8)
        self.play(FadeIn(pay), run_time=0.5)

        ax = Axes(x_range=[1980, 1990, 1], y_range=[0, 3, 1], x_length=8.4, y_length=3.2,
                  axis_config={"color": MUTED, "stroke_width": 2,
                               "include_ticks": False, "include_tip": False})
        ax.shift(DOWN * 0.4)
        dollar = ax.plot_line_graph(
            x_values=[1980, 1982, 1984, 1985, 1986, 1987, 1989],
            y_values=[1.4, 1.9, 2.3, 2.2, 1.7, 1.45, 1.42],
            line_color=WAIT, add_vertex_dots=False, stroke_width=5)
        imports = ax.plot_line_graph(
            x_values=[1980, 1982, 1983, 1985, 1987, 1989],
            y_values=[0.55, 0.55, 0.7, 1.5, 2.1, 2.25],
            line_color=MONEY, add_vertex_dots=False, stroke_width=5)
        dl = Text("the dollar", font=FONT, font_size=T_SMALL, color=WAIT).next_to(ax, UP, buff=0.1).shift(LEFT*2.2)
        il = Text("imports", font=FONT, font_size=T_SMALL, color=MONEY).next_to(ax, RIGHT, buff=0.15).shift(UP*0.6)
        with self.narrate("The dollar rose, and foreign firms poured into America — "
                          "years late, because they were waiting to be sure."):
            self.play(Create(ax), run_time=0.7)
            self.play(Create(dollar), FadeIn(dl), run_time=1.6)
            self.play(Create(imports), FadeIn(il), run_time=1.6)
        with self.narrate("Then the dollar fell back to where it had been. And they did "
                          "not leave. They had paid to get in, and leaving would mean "
                          "paying to get back in again later."):
            self.play(Indicate(imports, color=MONEY, scale_factor=1.0), run_time=1.6)
        self.beat()
        final = cards.body("Cause reversed. Effect stayed.", size=T_SUB, color=CHALK, width=40)
        final.to_edge(DOWN, buff=0.5)
        with self.narrate("The cause reversed. The effect stayed. That is all "
                          "hysteresis is — and now you have watched it happen twice."):
            self.play(FadeIn(final), run_time=0.9)
        self.beat()

        self.close_chapter([
            "up past 1.10, nothing · past 1.62, she builds",
            "back to 1.00 — and she does not close",
            "the bar stays magnetic",
            "hysteresis explains the dollar and the imports",
        ])
