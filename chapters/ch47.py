import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter47(Chapter):
    CH = 47
    TITLE = "The rivals Kit cannot beat"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["door", "people", "fog", "scale"]

    def body(self):
        kit = stick.kit(scale=0.8)
        St.place(kit, St.STAGE, ax=-0.8, ay=-0.5)
        with self.narrate("Four doors. Kit opens each one, and cannot close it again. "
                          "This is the chapter where the film earns its credibility, so "
                          "none of these gets knocked down.", v="c"):
            self.heading("Four doors he cannot close")
            self.play(FadeIn(kit), run_time=0.7)
        self.play(FadeOut(kit), run_time=0.4)

        doors = VGroup(*[W.door(SUNK, w=1.05, h=2.1) for _ in range(4)])
        doors.arrange(RIGHT, buff=0.85)
        St.place(doors, St.FULL, ay=0.45)
        labels = ["credit\nrationing", "demand,\nnot patience",
                  "a race for\nthe same job", "it did move\nprices"]
        labs = VGroup()
        for i, t in enumerate(labels):
            lt = Text(t, font=FONT, font_size=T_SMALL, color=SUNK, line_spacing=0.9)
            lt.next_to(doors[i], DOWN, buff=0.3)
            labs.add(lt)
        self.play(S.lag_map(Create, doors, lag=0.15), run_time=1.6)

        says = [
            "Door one. Firms may not have been short of confidence at all. They may "
            "simply have been unable to borrow. If the banks would not lend, no bar "
            "inside the firm was ever tested.",
            "Door two. They may have had no customers. If nobody is buying, patience "
            "has nothing to do with it. And which of the two does more of the work is a "
            "question this argument does not settle.",
            "Door three. If several firms are racing for the same opportunity, waiting "
            "is not possible, and the textbook is right after all.",
            "Door four. The policy did move prices in financial markets. That is the "
            "best-established finding in the whole body of research, and nothing here "
            "touches it.",
        ]
        for i, say in enumerate(says):
            with self.narrate(say):
                self.play(FadeIn(labs[i]), run_time=0.7)
                self.play(S.flash_around(doors[i], SUNK))
        self.beat()

        open_ = St.caption("all four left standing open", SUNK, T_SUB, width=30)
        St.place(open_, St.FOOT, pad=0.06)
        with self.narrate("All four are left standing open. Kit does not claim to have "
                          "closed any of them.", v="c"):
            self.play(FadeIn(open_), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the scope line
        self.drop_heading()
        scope = St.caption("investment a company can take\nits time over — not a race",
                           CHALK, T_HEAD, width=32)
        St.place(scope, St.WIDE, ay=0.2)
        with self.narrate("Which fixes the scope of the whole argument. It applies to "
                          "investment a company can take its time over. Not to a race."):
            self.play(Write(scope), run_time=2.6)
        self.wait(1.6)
        self.beat()

        self.close_chapter([
            "firms may have been unable to borrow",
            "or simply have had no customers",
            "a race removes the option to wait",
            "and the policy did move market prices",
        ])
