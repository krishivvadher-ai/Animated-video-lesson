import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.scale import MasterScale
from lib.theme import *


class Chapter06(Chapter):
    CH = 6
    TITLE = "So how high is high enough?"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ['clock', 'scale', 'voucher', 'door']

    def body(self):
        ava = stick.ava(scale=0.85).shift(LEFT * 5.4 + DOWN * 1.6)
        with self.narrate("If waiting is worth money, why does she ever build at all? "
                          "Why not wait for ever?", v="c"):
            self.play(FadeIn(ava), run_time=0.6)

        clock = cards.icon("clock", COST, 2.2).shift(RIGHT * 0.0 + UP * 1.4)
        cost = cards.body("Waiting costs a month of profit.", size=T_BODY, color=COST, width=34)
        cost.next_to(clock, DOWN, buff=0.6)
        with self.narrate("Because waiting is not free. Every month she waits, she "
                          "gives up a month of profit she could have been making."):
            self.play(FadeIn(clock), run_time=0.7)
            self.play(FadeIn(cost), run_time=0.8)
        self.beat()
        with self.narrate("So there is some level of money coming in that is high "
                          "enough that waiting any longer stops being worth it. That "
                          "level has a name."):
            pass
        self.clear_stage(keep=[ava])

        self.define("the trigger", "The level that makes building right.", "scale", TRIGGER,
                    narration="The trigger. The level the money coming in must reach "
                              "before building is actually the right thing to do.",
                    hold=4.2)

        # --------------------------------------------------- the master scale
        sc = MasterScale(x=-2.6, y=-0.3, height=4.6)
        self.play(FadeOut(ava), run_time=0.4)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), FadeIn(sc.title), run_time=1.1)

        mline = sc.add_level("M", 1.10, "Marshall's line", COST)
        with self.narrate("Here is Marshall's line again, where we left it."):
            self.play(Create(mline[0]), FadeIn(mline[1]), run_time=0.9)

        hline = sc.add_level("H", 1.62, "the real build-line", TRIGGER, sw=5)
        hcopy = sc.level_line(1.10, TRIGGER, sw=5)
        hlab = hline[1].copy().next_to(hcopy, RIGHT, buff=0.28)
        self.add(hcopy, hlab)
        self.remove(hline[0], hline[1])
        with self.narrate("Marshall's line stays exactly where it is. It is not wrong "
                          "about arithmetic. But the line where Nell should actually "
                          "build slides up above it."):
            self.play(Transform(hcopy, hline[0]), Transform(hlab, hline[1]),
                      run_time=2.2)
        self.beat()

        gap = sc.brace_between(1.10, 1.62, "the gap", WAIT)
        with self.narrate("And that gap has a meaning. It is the value of the chance "
                          "to wait — the thing she destroys the moment she builds."):
            self.play(FadeIn(gap), run_time=1.0)
        self.beat()

        note = cards.note("Build now → the chance is gone.", color=WAIT, size=T_BODY, width=30)
        note.move_to(RIGHT * 4.0 + UP * 2.9)
        with self.narrate("Build now, and the chance to wait is gone for ever. She has "
                          "to be paid for that, and the gap is the price."):
            self.play(FadeIn(note), run_time=0.8)
        self.beat()
        self.play(FadeOut(note), run_time=0.4)

        # --------------------------------------------------- the mirror
        mirror = cards.body("And there is a mirror image on the way down.",
                            size=T_SUB, color=CHALK, width=26)
        mirror.move_to(RIGHT * 4.0 + UP * 2.9)
        with self.narrate("There is a mirror image of this on the way down, and "
                          "chapter ten builds it properly."):
            self.play(FadeIn(mirror), run_time=0.8)

        lline = sc.add_level("L", 0.72, "the real quit-line", TRIGGER, sw=5)
        cline = sc.add_level("C", 1.00, "Marshall's quit-line", SUNK, dashed=True, sw=3)
        with self.narrate("Marshall says: shut down when the money stops covering the "
                          "day-to-day costs."):
            self.play(Create(cline[0]), FadeIn(cline[1]), run_time=0.9)
        with self.narrate("The right answer is lower. She should absorb real losses "
                          "before she gives up — because giving up throws away the "
                          "chance of things getting better."):
            self.play(Create(lline[0]), FadeIn(lline[1]), run_time=1.2)
        self.beat()

        self.close_chapter([
            "waiting costs forgone profit",
            "a trigger: high enough to stop waiting",
            "trigger above the textbook line",
            "and the mirror image on the way down",
        ])
