import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.scale import MasterScale
from lib.theme import *

RUNGS = [
    "investment: spend now, earn later",
    "some of it is sunk — never got back",
    "the future arrives a bit at a time",
    "the chance usually keeps",
    "so waiting pays: bad half cut, good half kept",
    "not about disliking risk",
    "waiting costs profit ⇒ a level to act at",
    "the trigger sits above the textbook line",
    "how far: choppiness and the cost of money",
    "base case ≈ double · rough trade > 3×",
    "cheaper money RAISES it",
    "in reverse: absorb losses before quitting",
    "the do-nothing band ≈ 9× wider",
    "up and back down — the effect stays",
    "hysteresis — the dollar and the imports",
    "cushion the downside ⇒ early in; lift the upside ⇒ late out",
    "many firms ⇒ an industry that looks frozen",
]


class Chapter21(Chapter):
    CH = 21
    TITLE = "Everything, in order"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ['scale', 'door', 'chain']

    def body(self):
        with self.narrate("One rung at a time, from the bottom. Everything Part One "
                          "has built."):
            pass
        page = 4
        for start in range(0, len(RUNGS), page):
            chunk = RUNGS[start:start + page]
            rows = VGroup(*[cards.body(r, size=T_BODY, color=CHALK, width=46)
                            for r in chunk])
            rows.arrange(DOWN, buff=0.55, aligned_edge=LEFT)
            if rows.width > 11.6:
                rows.scale(11.6 / rows.width)
            rows.move_to(ORIGIN)
            step = Text(f"{start + 1}–{start + len(chunk)} of {len(RUNGS)}",
                        font=FONT, font_size=T_TINY, color=MUTED)
            step.to_corner(UP + LEFT, buff=0.6)
            self.play(FadeIn(step), run_time=0.3)
            for k, r in enumerate(chunk):
                with self.narrate(r, pad=0.25):
                    self.play(FadeIn(rows[k], shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.4)
            self.play(FadeOut(rows), FadeOut(step), run_time=0.5)

        # ------------------------------------------------------ final scale
        sc = MasterScale(x=-3.0, y=-0.3, height=5.0)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), FadeIn(sc.title), run_time=0.8)
        for k, v, t, c, sw in [("L", 0.72, "0.72  give up", TRIGGER, 5),
                               ("C", 1.00, "1.00  day-to-day cost", SUNK, 3),
                               ("M", 1.10, "1.10  textbook", COST, 3),
                               ("H", 1.62, "1.62  build", TRIGGER, 5)]:
            g = sc.add_level(k, v, t, c, sw=sw)
            self.play(Create(g[0]), FadeIn(g[1]), run_time=0.4)
        band = sc.band(0.72, 1.62, TRIGGER, 0.13)
        with self.narrate("And the master scale in its final form. Give up at nought "
                          "point seven two. Build at one point six two. And in between, "
                          "a wide stretch where the right thing to do is nothing."):
            self.play(FadeIn(band), run_time=1.0)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------------ what it does NOT claim
        head = cards.section_title("What the paper does not claim", color=COST, size=T_SUB)
        self.play(FadeIn(head), run_time=0.5)
        nots = cards.bullet_list([
            "not “firms are irrational”",
            "not “waiting is always right”",
            "not where a rival can snatch it",
        ], color=CHALK, width=44, dotc=COST)
        nots.move_to(UP * 0.3)
        says = ["It does not say firms are irrational. It says the opposite.",
                "It does not say waiting is always right.",
                "And it does not apply where a rival can snatch the opportunity away "
                "from you."]
        for i in range(3):
            with self.narrate(says[i]):
                self.play(FadeIn(nots[i], shift=RIGHT * 0.2), run_time=0.6)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------------ back to chapter 0
        nell = stick.nell(scale=1.0).shift(LEFT * 4.4 + DOWN * 0.6)
        self.play(FadeIn(nell), run_time=0.6)
        with self.narrate("So go back to the two people we opened with, and let Nell "
                          "explain them."):
            pass
        f = cards.body("“Closing is final.\nStaying keeps the good years possible.”",
                       size=T_BODY, color=CHALK, width=28)
        f.move_to(RIGHT * 1.8 + UP * 1.4)
        with self.narrate("The farmer keeps going because closing is final. Staying "
                          "open keeps the good years possible, and that is worth more "
                          "to him than the losses are costing him."):
            self.play(FadeIn(f), run_time=1.0)
        self.beat()
        n = cards.body("“Building is final too.\nThis year is not yet good enough "
                       "to pay for waiting.”", size=T_BODY, color=CHALK, width=28)
        n.move_to(RIGHT * 1.8 + DOWN * 1.4)
        with self.narrate("And I do not build, because building is final too. Waiting "
                          "another year is worth something, and this year's numbers are "
                          "not yet good enough to pay for it."):
            self.play(FadeIn(n), nell.mood("pleased"), run_time=1.0)
        self.beat()

        # ------------------------------------------------------ hook
        self.clear_stage()
        hook = cards.body("A government spent hundreds of billions assuming none of this.",
                          size=T_HEAD, color=CHALK, width=32)
        with self.narrate("One more thing before we stop. A government somewhere spent "
                          "hundreds of billions of pounds on a policy that assumed none "
                          "of this was true."):
            self.play(Write(hook), run_time=2.4)
        self.beat()
        nxt = Text("Part Two", font=FONT, font_size=T_SUB, color=MUTED)
        nxt.next_to(hook, DOWN, buff=0.9)
        self.play(FadeIn(nxt), run_time=0.7)
        self.wait(1.4)

        self.close_chapter([
            "the whole ladder, in order",
            "not irrational · not always right",
            "next: a policy that assumed none of it",
        ])
