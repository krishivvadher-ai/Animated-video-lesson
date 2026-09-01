import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter37(Chapter):
    CH = 37
    TITLE = "Two different kinds of fear"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["fog", "risk", "money", "people"]

    def body(self):
        # ------------------------------------------------ replay the principle
        self.heading("What decides whether she builds")
        dist = VMobject(color=WAIT, stroke_width=4)
        pts = [np.array([x, 1.5 * np.exp(-x * x / 1.6) - 1.2, 0])
               for x in np.linspace(-3.0, 3.0, 40)]
        dist.set_points_smoothly(pts)
        St.place(dist, St.STAGE, ay=0.2)
        bad = Polygon(*[p for p in pts if p[0] <= 0.0],
                      np.array([0.0, -1.2, 0]), np.array([-3.0, -1.2, 0]),
                      color=COST, fill_color=COST, fill_opacity=0.28, stroke_width=0)
        bad.move_to(dist.get_center() + LEFT * dist.width / 4 + DOWN * 0.0)
        with self.narrate("Replay the bad news principle. When you can wait, it is "
                          "mainly the bad possible outcomes that decide whether you "
                          "build now."):
            self.play(Create(dist), run_time=1.4)
            self.play(FadeIn(bad), run_time=0.9)
            self.play(S.flash_around(bad, COST))
        self.beat()

        q = St.caption("so what does the policy compress?", TRIGGER, T_SUB, width=36)
        St.place(q, St.FOOT, pad=0.06)
        with self.narrate("So the question to ask is: what does this policy actually "
                          "compress?"):
            self.play(FadeIn(q), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the spring
        self.heading("What it reaches directly")
        sp = W.spring(COST, turns=8, width=3.2, height=1.0, compressed=0.0)
        St.place(sp, St.STAGE, ay=0.4)
        sl = St.caption("the price at which risk trades", COST, T_BODY, width=24)
        sl.next_to(sp, DOWN, buff=0.45)
        with self.narrate("In financial markets, there is a price for carrying risk. "
                          "Quantitative easing pushes that price down. Squeeze the "
                          "spring."):
            self.play(Create(sp), FadeIn(sl), run_time=1.2)
            sp2 = W.spring(COST, turns=8, width=3.2, height=1.0, compressed=0.85)
            sp2.move_to(sp)
            self.play(Transform(sp, sp2), run_time=1.6)
        self.beat()

        # ------------------------------------------------ the other fear
        self.heading("And what it does not reach")
        nell = stick.nell(scale=0.85)
        St.place(nell, St.STAGE, ax=-0.7, ay=-0.45)
        bubble = nell.think("will anyone\nstill be buying\nin three years?",
                            direction=UR, width=3.4)
        with self.narrate("But the doubt inside a firm is a different thing. Will "
                          "anyone still be buying in three years? Will this factory "
                          "still make sense?"):
            self.play(FadeIn(nell), run_time=0.7)
            self.play(FadeIn(bubble), run_time=1.0)
            self.play(nell.mood("worried"), run_time=0.4)

        gap = St.caption("reached only indirectly, if at all", MUTED, T_SUB, width=30)
        St.place(gap, St.SIDE, ay=-0.5)
        with self.narrate("Those are different worries entirely. A central bank buying "
                          "government bonds reaches them only indirectly, if at all."):
            self.play(FadeIn(gap), run_time=0.9)
        self.beat()

        honest = St.caption("so the claim is about how directly — not whether",
                            SRC_KIT, T_SUB, width=46)
        St.place(honest, St.FOOT, pad=0.06)
        with self.narrate("So the honest version of his claim is about how directly, "
                          "not about whether.", v="c"):
            self.play(FadeIn(honest), run_time=0.9)
            self.play(S.flash_around(honest, SRC_KIT))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the two-row summary
        self.drop_heading()
        rows = VGroup(
            VGroup(cards.icon("money", MONEY, 1.5),
                   St.caption("the price of risk\n— reached directly", MONEY,
                              T_SMALL, width=20)).arrange(DOWN, buff=0.28),
            VGroup(cards.icon("fog", COST, 1.5),
                   St.caption("the doubt itself\n— at one or two removes", COST,
                              T_SMALL, width=22)).arrange(DOWN, buff=0.28),
        ).arrange(RIGHT, buff=2.6)
        St.place(rows, St.WIDE, ay=0.15)
        with self.narrate("What a central bank reaches directly is the price at which "
                          "risk trades."):
            self.play(FadeIn(rows[0]), run_time=0.9)
        with self.narrate("What it reaches at one or two removes is the doubt itself."):
            self.play(FadeIn(rows[1]), run_time=0.9)
        self.beat()

        self.close_chapter([
            "the bad half decides whether she builds now",
            "the policy squeezes the price of risk directly",
            "the doubt inside a firm, only indirectly",
            "so the claim is about how directly, not whether",
        ])
