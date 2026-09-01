import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.scale import MasterScale
from lib.theme import *


class Chapter06(Chapter):
    CH = 6
    TITLE = "So how high is high enough?"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["clock", "scale", "voucher", "door"]

    def body(self):
        # ------------------------------------------------ waiting is not free
        self.heading("Waiting is not free")
        ava = stick.ava(scale=0.9)
        St.place(ava, St.STAGE, ax=-0.8, ay=-0.35)
        with self.narrate("If waiting is worth money, why does she ever build at all? "
                          "Why not wait for ever?", v="c"):
            self.play(FadeIn(ava), run_time=0.6)

        clock = cards.icon("clock", COST, 3.0)
        St.place(clock, St.STAGE, ax=0.25, ay=0.15)
        cost = St.caption("every month of waiting\nis a month of profit given up",
                          COST, T_BODY, width=24)
        St.place(cost, St.SIDE, ay=0.2)
        with self.narrate("Because waiting is not free. Every month she waits, she "
                          "gives up a month of profit she could have been making."):
            self.play(Create(clock), run_time=0.9)
            self.play(FadeIn(cost), run_time=0.8)
            self.play(S.pulse(clock, COST))
        self.beat()
        self.clear_stage()

        self.define("the trigger", "The level the money coming in must reach before "
                    "building is right.", "scale", TRIGGER, hold=4.2)

        # ------------------------------------------------ the line slides up
        self.heading("The real line is higher")
        sc = MasterScale(x=-4.6, y=-0.45, height=4.3)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), FadeIn(sc.title),
                  run_time=1.0)

        mline = sc.add_level("M", 1.10, "Marshall's line", COST, width=2.8)
        with self.narrate("Here is Marshall's line again, where we left it."):
            self.play(Create(mline[0]), FadeIn(mline[1]), run_time=0.9)

        hline = sc.add_level("H", 1.62, "the real build-line", TRIGGER, width=2.8, sw=5)
        start_line = sc.level_line(1.10, TRIGGER, width=2.8, sw=5)
        start_lab = hline[1].copy().next_to(start_line, RIGHT, buff=0.28)
        self.remove(hline[0], hline[1])
        self.add(start_line, start_lab)
        with self.narrate("Marshall's line stays exactly where it is. It is not wrong "
                          "about arithmetic. But the line where Nell should actually "
                          "build slides up above it."):
            self.play(Transform(start_line, hline[0]),
                      Transform(start_lab, hline[1]), run_time=2.2)
        self.beat()

        gap = sc.brace_between(1.10, 1.62, "the gap", WAIT)
        with self.narrate("And that gap has a meaning. It is the value of the chance to "
                          "wait — the thing she destroys the moment she builds."):
            self.play(FadeIn(gap), run_time=1.0)
            self.play(S.flash_around(gap, WAIT))
        self.beat()

        note = St.caption("build now, and the chance is gone", WAIT, T_BODY, width=22)
        St.place(note, St.SIDE, ay=0.55)
        with self.narrate("Build now, and the chance to wait is gone for ever. She has "
                          "to be paid for that, and the gap is the price."):
            self.play(FadeIn(note), run_time=0.8)
        self.beat()

        # ------------------------------------------------ the mirror
        mirror = St.caption("and the mirror image, downwards", CHALK, T_BODY, width=22)
        St.place(mirror, St.SIDE, ay=-0.15)
        with self.narrate("There is a mirror image of this on the way down, and chapter "
                          "fifteen builds it properly."):
            self.play(FadeIn(mirror), run_time=0.8)

        cline = sc.add_level("C", 1.00, "Marshall's quit-line", SUNK, width=2.8,
                             dashed=True, sw=3)
        with self.narrate("Marshall says: shut down when the money stops covering the "
                          "day-to-day costs."):
            self.play(Create(cline[0]), FadeIn(cline[1]), run_time=0.9)

        lline = sc.add_level("L", 0.72, "the real quit-line", TRIGGER, width=2.8, sw=5)
        with self.narrate("The right answer is lower. She should absorb real losses "
                          "before she gives up — because giving up throws away the "
                          "chance of things getting better."):
            self.play(Create(lline[0]), FadeIn(lline[1]), run_time=1.3)
        self.beat()

        self.close_chapter([
            "waiting costs the profit given up",
            "so there is a trigger: high enough to act",
            "the trigger sits above the textbook line",
            "and the mirror image on the way down",
        ])
