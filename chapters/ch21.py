import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.scale import MasterScale
from lib.theme import *

RUNGS = [
    ("investment: spend now, earn later", "slab"),
    ("some of it is sunk — never got back", "slab"),
    ("the future arrives a bit at a time", "fog"),
    ("the chance usually keeps", "door"),
    ("so waiting pays: bad half cut, good half kept", "clock"),
    ("not about disliking risk", "people"),
    ("waiting costs profit ⇒ a level to act at", "clock"),
    ("the trigger sits above the textbook line", "scale"),
    ("how far: choppiness and the cost of money", "fog"),
    ("base case ≈ double · rough trade > 3×", "money"),
    ("cheaper money RAISES it", "money"),
    ("in reverse: absorb losses before quitting", "door"),
    ("the do-nothing band ≈ 9× wider", "scale"),
    ("up and back down — the effect stays", "magnet"),
    ("cushion the downside ⇒ early in", "shield"),
    ("many firms ⇒ an industry that looks frozen", "people"),
]


class Chapter21(Chapter):
    CH = 21
    TITLE = "Everything, in order"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["scale", "door", "chain"]

    def body(self):
        # ------------------------------------------------ the ladder
        self.heading("The whole ladder, in order")
        page = 4
        for start in range(0, len(RUNGS), page):
            chunk = RUNGS[start:start + page]
            rows = St.points([t for t, _ in chunk], colour=CHALK,
                             icons=[i for _, i in chunk], dot_colour=TRIGGER,
                             size=T_BODY, width=40, buff=0.7)
            St.place(rows, St.FULL, ay=0.0)
            step = Text(f"{start + 1}–{start + len(chunk)} of {len(RUNGS)}",
                        font=FONT, font_size=T_TINY, color=MUTED)
            step.to_corner(UL, buff=0.55)
            self.play(FadeIn(step), run_time=0.3)
            for k, (t, _) in enumerate(chunk):
                with self.narrate(t, pad=0.22):
                    self.play(FadeIn(rows[k]), run_time=0.6)
            self.wait(0.4)
            self.play(FadeOut(rows), FadeOut(step), run_time=0.5)

        # ------------------------------------------------ the final scale
        self.heading("The master scale, in its final form")
        sc = MasterScale(x=-3.0, y=-0.45, height=4.8)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), FadeIn(sc.title), run_time=0.9)
        for k, v, t, c, sw in [("L", 0.72, "0.72  give up", TRIGGER, 5),
                               ("C", 1.00, "1.00  day-to-day cost", SUNK, 3),
                               ("M", 1.10, "1.10  textbook", COST, 3),
                               ("H", 1.62, "1.62  build", TRIGGER, 5)]:
            g = sc.add_level(k, v, t, c, width=3.0, sw=sw)
            self.play(Create(g[0]), FadeIn(g[1]), run_time=0.45)
        band = sc.band(0.72, 1.62, TRIGGER, 0.14, width=3.0)
        with self.narrate("Give up at nought point seven two. Build at one point six "
                          "two. And in between, a wide stretch where the right thing to "
                          "do is nothing."):
            self.play(FadeIn(band), run_time=1.0)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ what it does not claim
        self.heading("What the paper does NOT claim")
        self.side(["not “firms are irrational”",
                   "not “waiting is always right”",
                   "not where a rival can snatch it"],
                  colour=CHALK, dot_colour=COST, width=26, region=St.FULL,
                  spoken=["It does not say firms are irrational. It says the opposite.",
                          "It does not say waiting is always right.",
                          "And it does not apply where a rival can snatch the "
                          "opportunity away from you."])
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ back to chapter 0
        self.heading("Back to the two we opened with")
        nell = stick.nell(scale=1.0)
        St.place(nell, St.STAGE, ax=-0.7, ay=-0.2)
        self.play(FadeIn(nell), run_time=0.6)
        f = St.caption("closing is final — staying keeps\nthe good years possible",
                       CHALK, T_BODY, width=26)
        St.place(f, St.SIDE, ay=0.5)
        with self.narrate("The farmer keeps going because closing is final. Staying "
                          "open keeps the good years possible, and that is worth more "
                          "to him than the losses are costing him."):
            self.play(FadeIn(f), run_time=1.0)
        self.beat()
        n = St.caption("building is final too — this year\nis not yet good enough",
                       CHALK, T_BODY, width=26)
        St.place(n, St.SIDE, ay=-0.3)
        with self.narrate("And I do not build, because building is final too. Waiting "
                          "another year is worth something, and this year's numbers are "
                          "not yet good enough to pay for it."):
            self.play(FadeIn(n), nell.mood("pleased"), run_time=1.0)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the hook
        self.drop_heading()
        hook = St.caption("a government spent billions\nassuming none of this", CHALK, T_HEAD, width=30)
        St.place(hook, St.WIDE, ay=0.2)
        with self.narrate("One more thing before we stop. A government somewhere spent "
                          "hundreds of billions of pounds on a policy that assumed none "
                          "of this was true."):
            self.play(Write(hook), run_time=2.6)
        self.beat()
        nxt = Text("Part Two", font=FONT, font_size=T_SUB, color=MUTED)
        St.place(nxt, St.FOOT, pad=0.06)
        self.play(FadeIn(nxt), run_time=0.7)
        self.wait(1.4)

        self.close_chapter([
            "the whole ladder, in order",
            "not irrational · not always right",
            "next: a policy that assumed none of it",
        ])
