import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.scale import MasterScale
from lib.theme import *


class Chapter15(Chapter):
    CH = 15
    TITLE = "When to give up"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ['slab', 'door', 'scale', 'clock']

    def body(self):
        # ------------------------------------------------ suspend vs abandon
        head = Text("Two words that are not the same",
                    font=FONT, font_size=T_SUB, color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)

        self.define("suspending", "Stopping, meaning to start again.",
                    "clock", WAIT, at=LEFT * 3.2 + UP * 0.6, hold=3.4)
        self.define("abandoning", "Stopping for good.", "door", COST,
                    at=RIGHT * 3.2 + UP * 0.6, hold=3.2)

        rust = cards.body("idle machinery rusts — totally, at once",
                          size=T_BODY, color=SUNK, width=44)
        rust.move_to(DOWN * 0.6)
        with self.narrate("To make the point sharp, the paper assumes that idle "
                          "machinery rusts. Totally, and immediately. So pausing and "
                          "quitting become the same thing, and starting again means "
                          "paying the whole sunk cost over again."):
            self.play(FadeIn(rust), run_time=1.0)
        self.beat()
        caveat = cards.note("the paper flags this as a simplification", width=62)
        caveat.to_edge(DOWN, buff=0.5)
        with self.narrate("And the paper flags that itself, as a deliberate "
                          "simplification. Where a firm really can mothball a factory "
                          "and restart it cheaply, this half of the argument gets "
                          "weaker. Hold on to that — Part Two needs it."):
            self.play(FadeIn(caveat), run_time=1.0)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the mirror argument
        nell = stick.nell(scale=0.9).shift(LEFT * 5.0 + DOWN * 1.2)
        self.play(FadeIn(nell), nell.mood("worried"), run_time=0.6)
        arg = cards.bullet_list([
            "She is losing money this month.",
            "closing is final",
            "staying keeps recovery alive",
            "so she absorbs real losses",
        ], color=CHALK, width=38)
        arg.move_to(RIGHT * 1.2 + UP * 0.3)
        texts = ["Nell is losing money this month.",
                 "closing is final",
                 "Staying open keeps alive the chance that trade recovers.",
                 "so she absorbs real losses"]
        for i in range(4):
            with self.narrate(texts[i]):
                self.play(FadeIn(arg[i], shift=RIGHT * 0.2), run_time=0.6)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the four levels
        sc = MasterScale(x=-3.0, y=-0.3, height=5.0)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), FadeIn(sc.title), run_time=1.0)
        units = cards.note("running cost 1 · sunk cost 2",
                           width=44)
        units.to_edge(UP, buff=0.4).shift(RIGHT * 2.8)
        self.play(FadeIn(units), run_time=0.6)

        lv = [
            ("L", 0.72, "0.72  give up here", TRIGGER, "the real quit-line"),
            ("C", 1.00, "1.00  day-to-day cost", SUNK, None),
            ("M", 1.10, "1.10  textbook build-line", COST, None),
            ("H", 1.62, "1.62  the real build-line", TRIGGER, None),
        ]
        say = [
            "Down here, at nought point seven two, she finally gives up. That is the "
            "real quit-line.",
            "At one, her day-to-day costs are exactly covered. That is where the "
            "textbook says stop.",
            "At one point one, the textbook says build — day-to-day costs plus the "
            "normal return on the money sunk into the building.",
            "And at one point six two, she should actually build.",
        ]
        objs = []
        for (k, v, t, c, _), s in zip(lv, say):
            g = sc.add_level(k, v, t, c, sw=5 if c == TRIGGER else 3)
            objs.append(g)
            with self.narrate(s):
                self.play(Create(g[0]), FadeIn(g[1]), run_time=1.1)
            self.beat(0.5)

        obs1 = cards.body("profit 0.62 at H — over 6× the normal return",
                          size=T_BODY, color=TRIGGER, width=24)
        obs1.move_to(RIGHT * 4.2 + UP * 1.8)
        with self.narrate("Two observations the paper makes about these numbers. At the "
                          "true build point her operating profit is nought point six "
                          "two — more than six times the normal return on the money "
                          "she has sunk in."):
            self.play(FadeIn(obs1), run_time=1.0)
        self.beat()
        obs2 = cards.body("at L: losses ≈ a third of day-to-day costs",
                          size=T_BODY, color=TRIGGER, width=24)
        obs2.move_to(RIGHT * 4.2 + DOWN * 1.4)
        with self.narrate("And at the quit point she is absorbing losses of nearly a "
                          "third of her day-to-day costs, month after month, before "
                          "she gives up."):
            self.play(FadeIn(obs2), run_time=1.0)
        self.beat()
        self.play(FadeOut(obs1), FadeOut(obs2), FadeOut(units), run_time=0.5)

        # ------------------------------------------------ comparative statics
        cs = Text("Now move one thing at a time", font=FONT, font_size=T_SUB,
                  color=CHALK).to_edge(UP, buff=0.5).shift(RIGHT * 2.8)
        self.play(FadeIn(cs), run_time=0.5)

        bigger = cards.body("A bigger sunk cost.", size=T_SUB, color=SUNK, width=20)
        bigger.move_to(RIGHT * 4.2 + UP * 2.0)
        with self.narrate("Suppose the building costs more to put up. A bigger sunk "
                          "cost. What happens to the two lines?"):
            self.play(FadeIn(bigger), run_time=0.7)

        hnew = sc.level_line(1.85, TRIGGER, sw=5)
        lnew = sc.level_line(0.60, TRIGGER, sw=5)
        with self.narrate("The build-line goes up. She is more reluctant to start."):
            self.play(Transform(objs[3][0].copy(), hnew), run_time=1.2)
        with self.narrate("And the quit-line goes down. She is more reluctant to stop."):
            self.play(Transform(objs[0][0].copy(), lnew), run_time=1.2)
        self.beat()
        twice = cards.body("slower to start AND slower to stop",
                           size=T_BODY, color=SUNK, width=22)
        twice.move_to(RIGHT * 4.2 + DOWN * 0.2)
        with self.narrate("Say that one twice, because it is not obvious. A bigger "
                          "stake to keep alive makes her slower to start and slower to "
                          "stop. Both at once, and for the same reason — there is more "
                          "to protect."):
            self.play(FadeIn(twice), run_time=1.0)
        self.beat()
        self.play(FadeOut(bigger), FadeOut(twice), FadeOut(hnew), FadeOut(lnew),
                  run_time=0.5)

        exit_ = cards.body("costly exit → higher build-line",
                           size=T_BODY, color=COST, width=22)
        exit_.move_to(RIGHT * 4.2 + UP * 1.4)
        with self.narrate("One more. If leaving is itself expensive — redundancy "
                          "payments, restoring the site of a mine — then the build-line "
                          "rises further still. She is more cautious about entering "
                          "something she may have to pay to escape."):
            self.play(FadeIn(exit_), run_time=1.0)
        self.beat()

        self.close_chapter([
            "stopping = ruin (a flagged simplification)",
            "staying keeps recovery alive",
            "0.72 · 1.00 · 1.10 · 1.62",
            "bigger sunk cost → slower both ways",
        ])
