import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter33(Chapter):
    CH = 33
    TITLE = "Channels two and three"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["signal", "flow", "clock", "fog"]

    def body(self):
        # ------------------------------------------------ channel two: saying so
        self.heading("Channel two: saying so")
        gov = stick.governor(scale=0.9)
        St.place(gov, St.STAGE, ax=-0.75, ay=-0.3)
        with self.narrate("The second channel does not need the money to go anywhere at "
                          "all. It works purely through what the action tells "
                          "everybody."):
            self.play(FadeIn(gov), FadeIn(gov.label()), run_time=0.8)

        waves = VGroup(*[Arc(radius=r, start_angle=-PI / 3, angle=2 * PI / 3,
                             color=SRC_BR, stroke_width=4 - i * 0.5)
                         for i, r in enumerate((1.0, 1.6, 2.2, 2.8))])
        waves.move_to(gov.get_right() + RIGHT * 0.1)
        msg = St.caption("we are serious, and\nwe are not finished", SRC_BR,
                         T_BODY, width=22)
        St.place(msg, St.SIDE, ay=0.55)
        with self.narrate("A very large purchase is a signal. It says the central bank "
                          "is serious about getting the economy going, and that it will "
                          "keep rates low for a long time yet."):
            self.play(S.lag_map(Create, waves, lag=0.18), run_time=1.6)
            self.play(FadeIn(msg), run_time=0.7)

        crowd = stick.crowd(4, spacing=1.0, scale=0.42)
        St.place(crowd, St.FULL, ay=-0.82)
        with self.narrate("And if everybody believes that, they act on it now, before "
                          "anything else has happened at all."):
            self.play(FadeIn(crowd), run_time=0.8)
            self.play(S.pulse(crowd, SRC_BR))
        self.beat()

        anchor = St.caption("expectations of inflation, held down", TRIGGER,
                            T_SUB, width=36)
        St.place(anchor, St.FOOT, pad=0.06)
        with self.narrate("Which helps keep people's expectations of future inflation "
                          "anchored. And expectations, as a later chapter will show, "
                          "are themselves a lever."):
            self.play(FadeIn(anchor), run_time=0.8)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ channel three: liquidity
        self.heading("Channel three: oiling the wheels")
        self.define("liquidity", "How easily a thing can be sold without moving its "
                    "price.", "flow", WAIT, hold=4.2)

        market = Rectangle(width=5.0, height=2.6, color=MUTED, stroke_width=3)
        St.place(market, St.STAGE, ax=-0.1, ay=0.15)
        mlab = Text("the market", font=FONT, font_size=T_SMALL, color=MUTED)
        mlab.next_to(market, UP, buff=0.2)
        ice = W.fog(width=4.8, height=2.4, n=8, color=WAIT, opacity=0.5)
        ice.move_to(market.get_center())
        buyers = VGroup(*[stick.StickFigure("", CHALK, scale=0.4) for _ in range(3)])
        buyers.arrange(RIGHT, buff=0.9).move_to(market.get_center())
        with self.narrate("When markets seize up, you may not be able to find a buyer "
                          "at all. So investors demand a higher return to compensate "
                          "them for that risk."):
            self.play(Create(market), FadeIn(mlab), run_time=0.8)
            self.play(FadeIn(ice), run_time=1.0)

        prem = W.Bar(1.9, color=COST, width=0.8)
        St.place(prem, St.SIDE, ay=-0.25)
        pl = Text("extra return\ndemanded", font=FONT, font_size=T_TINY, color=COST,
                  line_spacing=0.9)
        pl.next_to(prem, DOWN, buff=0.2)
        St.collapse_bars(VGroup(prem))
        self.play(St.grow_bars(VGroup(prem)), FadeIn(pl))

        with self.narrate("A central bank buying on a very large scale is, among other "
                          "things, a buyer. It puts trading back into the market, and "
                          "that premium comes down."):
            self.play(FadeOut(ice), FadeIn(buyers), run_time=1.2)
            self.play(prem.rect.animate.stretch_to_fit_height(0.55).move_to(
                prem.rect.get_bottom() + UP * 0.275), run_time=1.2)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the caveats
        self.heading("And the authors' own hedges")
        hedges = [("clock", "probably only while the buying goes on", MUTED),
                  ("flow", "gilt markets are very liquid anyway", MUTED),
                  ("fog", "so this one may be small", COST)]
        cols = VGroup()
        for kind, text, col in hedges:
            cols.add(VGroup(cards.icon(kind, col, 1.5),
                            St.caption(text, col, T_SMALL, width=18)
                            ).arrange(DOWN, buff=0.3))
        cols.arrange(RIGHT, buff=1.1)
        St.place(cols, St.FULL, ay=0.15)
        says = ["But the authors are careful about this one. The effect probably lasts "
                "only while the purchases are going on.",
                "And in gilt markets, which are normally very liquid anyway,",
                "it may be small."]
        for i, c in enumerate(cols):
            with self.narrate(says[i]):
                self.play(FadeIn(c, shift=UP * 0.25), run_time=0.8)
        self.beat()

        disp = St.caption("how big, and for how long — disputed", MUTED, T_SUB, width=36)
        St.place(disp, St.FOOT, pad=0.06)
        with self.narrate("There is also disagreement about how big those effects were "
                          "and how long they lasted. And the effects on wider classes "
                          "of assets are less marked than on company bonds."):
            self.play(FadeIn(disp), run_time=0.8)
        self.beat()

        self.close_chapter([
            "channel two works purely through the signal",
            "channel three puts trading back in a frozen market",
            "and the authors hedge channel three hard",
        ])
