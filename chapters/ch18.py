import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.scale import MasterScale
from lib.theme import *


class Chapter18(Chapter):
    CH = 18
    TITLE = "Two countries"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["people", "scale", "shield", "signal"]

    def body(self):
        # ------------------------------------------------ the observation
        self.heading("A detective story")
        nell = stick.nell(scale=0.9)
        St.place(nell, St.STAGE, ax=-0.55, ay=0.1)
        nl = Text("an American firm", font=FONT, font_size=T_SMALL, color=MUTED)
        nl.next_to(nell, DOWN, buff=0.25)
        kenji = stick.kenji(scale=0.9)
        St.place(kenji, St.SIDE, ax=-0.1, ay=0.1)
        kl = Text("a Japanese firm", font=FONT, font_size=T_SMALL, color=MUTED)
        kl.next_to(kenji, DOWN, buff=0.25)
        with self.narrate("Here is Nell, in America. And here is Kenji, running a "
                          "similar factory in Japan."):
            self.play(FadeIn(nell), FadeIn(nl), run_time=0.8)
            self.play(FadeIn(kenji), FadeIn(kl), run_time=0.8)

        us = St.points(["demanded very high returns", "quit after short losses"],
                       colour=COST, dot_colour=COST, size=T_BODY, width=18)
        St.place(us, St.STAGE, ax=-0.5, ay=-0.72)
        jp = St.points(["invested aggressively", "hung on through losses"],
                       colour=MONEY, dot_colour=MONEY, size=T_BODY, width=18)
        St.place(jp, St.SIDE, ax=-0.1, ay=-0.72)
        with self.narrate("American firms of the period demanded very high returns "
                          "before they would build — and then abandoned whole fields "
                          "after short stretches of losses. Colour televisions. Video "
                          "recorders. Semiconductors."):
            self.play(S.lag_map(FadeIn, us, lag=0.25), nell.mood("worried"),
                      run_time=1.4)
        with self.narrate("Japanese firms did the opposite on both counts. They "
                          "invested aggressively, and they hung on."):
            self.play(S.lag_map(FadeIn, jp, lag=0.25), run_time=1.2)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ why waiting fails alone
        self.heading("Why the waiting story cannot explain that")
        sc = MasterScale(x=-4.2, y=-0.5, height=3.8)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), run_time=0.6)
        h = sc.add_level("H", 1.45, "build-line", TRIGGER, width=2.4, sw=5)
        l = sc.add_level("L", 0.85, "quit-line", TRIGGER, width=2.4, sw=5)
        self.play(Create(h[0]), FadeIn(h[1]), Create(l[0]), FadeIn(l[1]), run_time=1.0)
        with self.narrate("Remember what uncertainty does to the two lines. It raises "
                          "the build-line and lowers the quit-line. Together. It cannot "
                          "do one without the other."):
            self.play(h.animate.shift(UP * 0.55), l.animate.shift(DOWN * 0.55),
                      run_time=1.8)
        self.beat()
        contra = St.caption("hesitant to enter ⇒ MORE willing to stay", COST, T_BODY,
                            width=22)
        St.place(contra, St.SIDE, ay=0.4)
        with self.narrate("So a firm too hesitant to invest should be more willing to "
                          "ride out bad periods, not less. The American firms were the "
                          "opposite on both counts. The story does not fit."):
            self.play(FadeIn(contra), run_time=1.0)
            self.play(S.flash_around(contra, COST))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the popular explanation
        self.heading("And the usual explanation fails too")
        self.side(["lifetime employment ⇒ labour quasi-fixed",
                   "lower variable cost ⇒ quit later ✓",
                   "but bigger sunk stakes ⇒ reluctant to enter ✗",
                   "they were the opposite"],
                  colour=CHALK, dot_colour=COST, width=24, region=St.FULL,
                  spoken=["The usual explanation is lifetime employment, which makes "
                          "labour a cost you carry whether you use it or not.",
                          "Lower day-to-day costs do mean revenue has to fall further "
                          "before quitting makes sense. So far so good.",
                          "But larger fixed and sunk commitments should make those same "
                          "firms reluctant investors.",
                          "And they were the opposite. Particularly aggressive ones. So "
                          "that explanation does not work either."])
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the resolution
        self.heading("Their uncertainty was lopsided")
        ax = NumberLine(x_range=[-3, 3, 1], length=7.4, color=MUTED,
                        include_numbers=False, include_ticks=False)
        St.place(ax, St.STAGE, ay=-0.35)
        curve = FunctionGraph(lambda x: 1.5 * np.exp(-x * x / 1.4), x_range=[-3, 3],
                              color=WAIT, stroke_width=5)
        curve.move_to(ax.get_center() + UP * 0.75)
        bad = Text("bad", font=FONT, font_size=T_SMALL, color=COST)
        bad.next_to(ax, LEFT, buff=0.22)
        good = Text("good", font=FONT, font_size=T_SMALL, color=MONEY)
        good.next_to(ax, RIGHT, buff=0.22)
        with self.narrate("Here is the spread of possible futures for a firm. Bad ones "
                          "to the left, good ones to the right."):
            self.play(Create(ax), FadeIn(bad), FadeIn(good), run_time=0.9)
            self.play(Create(curve), run_time=1.4)

        cut = Line(ax.n2p(-1.6) + DOWN * 0.35, ax.n2p(-1.6) + UP * 2.3, color=SUNK,
                   stroke_width=6)
        ctext = St.caption("government support,\ntolerated cartels", SUNK, T_BODY,
                           width=18)
        St.place(ctext, St.SIDE, ay=0.55)
        with self.narrate("For the Japanese firms, the bad half was cushioned. "
                          "Government support, and cartels tolerated in recessions, cut "
                          "off the worst outcomes."):
            self.play(Create(cut), FadeIn(ctext), run_time=1.3)
            self.play(curve.animate.set_stroke(opacity=0.35), run_time=0.6)
        self.beat()

        e1 = St.caption("less bad news ⇒ less waiting ⇒ early in", MONEY, T_BODY,
                        width=22)
        St.place(e1, St.SIDE, ay=-0.1)
        with self.narrate("Now use the bad news principle. Waiting is worth less when "
                          "there is less bad news to wait out. So they entered early."):
            self.play(FadeIn(e1), run_time=0.9)
        self.beat()
        self.play(FadeOut(ctext), run_time=0.3)
        self.define("the good news principle", "Staying is governed by the good "
                    "possible outcomes.", "signal", MONEY, at=UP * 1.5, hold=4.4)
        e2 = St.caption("upside worth more ⇒ late out", MONEY, T_BODY, width=22)
        St.place(e2, St.SIDE, ay=-0.6)
        with self.narrate("And because the upside mattered relatively more for them, "
                          "they stayed late as well. One lopsided distribution, both "
                          "puzzles solved."):
            self.play(FadeIn(e2), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the two rules
        self.heading("Two rules, for two different jobs")
        r1 = St.caption("to get investment: cut the downside", MONEY, T_SUB, width=32)
        r2 = St.caption("to stop exit: lift the upside", WAIT, T_SUB, width=32)
        rules = VGroup(r1, r2).arrange(DOWN, buff=1.1)
        St.place(rules, St.FULL, ay=0.15)
        with self.narrate("Which gives two rules, and they are probably the most "
                          "practically useful sentences in the whole article. To get "
                          "firms to invest sooner, reduce the downside risk."):
            self.play(FadeIn(r1), run_time=0.9)
        self.beat()
        with self.narrate("To stop firms leaving, improve the upside."):
            self.play(FadeIn(r2), run_time=0.9)
        self.beat()
        with self.narrate("Different instruments, for different jobs. Remember that. "
                          "Part Three is built on it."):
            self.foot("different jobs, different instruments", CHALK)
            self.play(S.flash_around(rules, TRIGGER, run_time=2.0))
        self.beat()

        self.close_chapter([
            "US: late in, early out · Japan: the reverse",
            "option value moves both lines together",
            "cushioned downside ⇒ early in, late out",
            "downside → entry · upside → staying",
        ])
