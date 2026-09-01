import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.scale import MasterScale
from lib.theme import *


class Chapter18(Chapter):
    CH = 18
    TITLE = "Two countries"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ['people', 'scale', 'shield', 'signal']

    def body(self):
        nell = stick.nell(scale=0.9).shift(LEFT * 4.0 + DOWN * 0.4)
        nl = Text("an American firm", font=FONT, font_size=T_SMALL, color=MUTED)
        nl.next_to(nell, DOWN, buff=0.2)
        kenji = stick.kenji(scale=0.9).shift(RIGHT * 4.0 + DOWN * 0.4)
        kl = Text("a Japanese firm", font=FONT, font_size=T_SMALL, color=MUTED)
        kl.next_to(kenji, DOWN, buff=0.2)

        with self.narrate("This is a detective story, so let us tell it as one. Here is "
                          "Nell, in America. And here is Kenji, running a similar "
                          "factory in Japan."):
            self.play(FadeIn(nell), FadeIn(nl), run_time=0.7)
            self.play(FadeIn(kenji), FadeIn(kl), run_time=0.7)

        obs = cards.body("The observation others made about the period", size=T_SUB,
                         color=CHALK, width=30).to_edge(UP, buff=0.7)
        self.play(FadeIn(obs), run_time=0.5)

        us = cards.bullet_list([
            "demanded very high returns before building",
            "quit after short losses",
        ], color=COST, width=20)
        us.next_to(nell, DOWN, buff=0.9)
        jp = cards.bullet_list([
            "invested aggressively",
            "and hung on through losses",
        ], color=MONEY, width=20)
        jp.next_to(kenji, DOWN, buff=0.9)

        with self.narrate("American firms of the period demanded very high returns "
                          "before they would build — and then abandoned whole fields "
                          "after short stretches of losses. Colour televisions. Video "
                          "recorders. Semiconductors."):
            self.play(FadeIn(us), nell.mood("worried"), run_time=1.0)
        with self.narrate("Japanese firms did the opposite on both counts. They "
                          "invested aggressively, and they hung on."):
            self.play(FadeIn(jp), kenji.mood("neutral"), run_time=1.0)
        self.beat()

        # ------------------------------------------------- why option value fails alone
        self.clear_stage()
        head = Text("Why the waiting story cannot explain that on its own",
                    font=FONT, font_size=T_SUB, color=CHALK).to_edge(UP, buff=0.6)
        self.play(FadeIn(head), run_time=0.5)

        sc = MasterScale(x=-3.0, y=-0.6, height=4.0)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), run_time=0.6)
        self.play(FadeOut(sc.title), run_time=0.1) if False else None
        h = sc.add_level("H", 1.45, "build-line", TRIGGER, width=2.6, sw=5)
        l = sc.add_level("L", 0.85, "quit-line", TRIGGER, width=2.6, sw=5)
        self.play(Create(h[0]), FadeIn(h[1]), Create(l[0]), FadeIn(l[1]), run_time=1.0)

        with self.narrate("Remember what uncertainty does to the two lines. It raises "
                          "the build-line and lowers the quit-line. Together. It cannot "
                          "do one without the other."):
            self.play(h[0].animate.shift(UP * 0.5), l[0].animate.shift(DOWN * 0.5),
                      h[1].animate.shift(UP * 0.5), l[1].animate.shift(DOWN * 0.5),
                      run_time=1.6)
        self.beat()
        contra = cards.body("hesitant to enter ⇒ MORE willing to stay. Not less.",
                            size=T_BODY, color=COST, width=26)
        contra.move_to(RIGHT * 3.8 + UP * 0.6)
        with self.narrate("So a firm too hesitant to invest should be more willing to "
                          "ride out bad periods, not less. The American firms were the "
                          "opposite on both counts. The story does not fit."):
            self.play(FadeIn(contra), run_time=1.1)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------- the popular explanation
        head2 = Text("And the popular explanation fails on its own terms",
                     font=FONT, font_size=T_SUB, color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head2), run_time=0.5)
        chain = cards.bullet_list([
            "lifetime employment ⇒ labour quasi-fixed",
            "lower variable cost ⇒ quit later ✓",
            "but bigger sunk stakes ⇒ reluctant to enter ✗",
            "they were the opposite",
        ], color=CHALK, width=44)
        chain.move_to(DOWN * 0.1)
        says = ["The usual explanation is lifetime employment, which makes labour a "
                "cost you carry whether you use it or not.",
                "Lower day-to-day costs do mean revenue has to fall further before "
                "quitting makes sense. So far so good.",
                "But larger fixed and sunk commitments should make those same firms "
                "reluctant investors.",
                "And they were the opposite. Particularly aggressive ones. So that "
                "explanation does not work either."]
        for i in range(4):
            with self.narrate(says[i]):
                self.play(FadeIn(chain[i], shift=RIGHT * 0.2), run_time=0.6)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------- the resolution
        head3 = Text("The resolution: their uncertainty was lopsided",
                     font=FONT, font_size=T_SUB, color=MONEY).to_edge(UP, buff=0.7)
        self.play(FadeIn(head3), run_time=0.5)

        ax = NumberLine(x_range=[-3, 3, 1], length=8.0, color=MUTED,
                        include_numbers=False, include_ticks=False)
        ax.shift(DOWN * 0.4)
        lab_bad = Text("bad futures", font=FONT, font_size=T_SMALL, color=COST)
        lab_bad.next_to(ax, LEFT, buff=0.25)
        lab_good = Text("good futures", font=FONT, font_size=T_SMALL, color=MONEY)
        lab_good.next_to(ax, RIGHT, buff=0.25)
        curve = FunctionGraph(lambda x: 1.5 * np.exp(-x * x / 1.4), x_range=[-3, 3],
                              color=WAIT, stroke_width=4).move_to(ax.get_center() + UP * 0.75)
        self.play(Create(ax), FadeIn(lab_bad), FadeIn(lab_good), Create(curve), run_time=1.4)

        with self.narrate("Here is the spread of possible futures for a firm. Bad ones "
                          "to the left, good ones to the right."):
            pass
        cushion = Polygon(*[ax.n2p(x) + UP * 0.02 for x in np.linspace(-3, 0, 12)] +
                          [ax.n2p(0), ax.n2p(-3)], color=SUNK, stroke_width=0,
                          fill_color=SUNK, fill_opacity=0.0)
        cut = Line(ax.n2p(-1.6) + DOWN * 0.3, ax.n2p(-1.6) + UP * 2.2,
                   color=SUNK, stroke_width=5)
        ctext = Text("government support,\ntolerated cartels in recessions",
                     font=FONT, font_size=T_SMALL, color=SUNK, line_spacing=0.9)
        ctext.next_to(cut, DOWN, buff=0.35).shift(LEFT * 0.4)
        with self.narrate("For the Japanese firms, the bad half was cushioned. "
                          "Government support, and cartels tolerated in recessions, cut "
                          "off the worst outcomes."):
            self.play(Create(cut), FadeIn(ctext), run_time=1.2)
            self.play(curve.animate.set_stroke(opacity=0.35), run_time=0.6)
        self.beat()

        e1 = cards.body("less bad news ⇒ less waiting ⇒ early in",
                        size=T_BODY, color=MONEY, width=44)
        e1.to_edge(DOWN, buff=1.3)
        with self.narrate("Now use the bad news principle. Waiting is worth less when "
                          "there is less bad news to wait out. So they entered early."):
            self.play(FadeIn(e1), run_time=0.9)
        self.beat()

        self.define("the good news principle", "The decision to stay is governed by the "
                    "good possible outcomes — because staying is what preserves them.",
                    "signal", MONEY,
                    narration="And its mirror image, which the paper names. The good "
                              "news principle. The decision to stay is governed by the "
                              "good possible outcomes — because staying is what "
                              "preserves them.", at=UP * 1.4, hold=4.6)

        e2 = cards.body("upside worth more ⇒ late out",
                        size=T_BODY, color=MONEY, width=44)
        e2.next_to(e1, UP, buff=0.5)
        with self.narrate("And because the upside mattered relatively more for them, "
                          "they stayed late as well. One lopsided distribution, both "
                          "puzzles solved."):
            self.play(FadeIn(e2), run_time=0.9)
        self.beat()

        # ------------------------------------------------- the two policy rules
        self.clear_stage()
        r1 = cards.body("to get investment: cut the downside",
                        size=T_SUB, color=MONEY, width=34)
        r2 = cards.body("to stop exit: lift the upside",
                        size=T_SUB, color=WAIT, width=34)
        rules = VGroup(r1, r2).arrange(DOWN, buff=1.1)
        with self.narrate("Which gives two rules, and they are probably the most "
                          "practically useful sentences in the whole article."):
            pass
        with self.narrate("To get firms to invest sooner, reduce the downside risk."):
            self.play(FadeIn(r1), run_time=0.8)
        self.beat()
        with self.narrate("To stop firms leaving, improve the upside."):
            self.play(FadeIn(r2), run_time=0.8)
        self.beat()
        diff = cards.body("different jobs, different instruments",
                          size=T_BODY, color=CHALK, width=40)
        diff.next_to(rules, DOWN, buff=0.9)
        with self.narrate("Different instruments, for different jobs. Remember that. "
                          "Part Two is built on it."):
            self.play(FadeIn(diff), run_time=0.8)
        self.beat()

        self.close_chapter([
            "US: late in, early out · Japan: the reverse",
            "option value moves both lines together",
            "cushioned downside → early in, late out",
            "downside → entry · upside → staying",
        ])
