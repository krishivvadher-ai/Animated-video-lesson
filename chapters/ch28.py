import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter28(Chapter):
    CH = 28
    TITLE = "Leg two: cheaper money, and feeling richer"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["money", "shield", "people", "door"]

    def body(self):
        # ------------------------------------------------ two routes
        self.heading("From market prices to actual spending")
        routes = VGroup(
            VGroup(cards.icon("money", MONEY, 1.8),
                   St.caption("borrowing gets cheaper", MONEY, T_SMALL, width=18)
                   ).arrange(DOWN, buff=0.3),
            VGroup(cards.icon("people", TRIGGER, 1.8),
                   St.caption("owners feel richer", TRIGGER, T_SMALL, width=18)
                   ).arrange(DOWN, buff=0.3),
        ).arrange(RIGHT, buff=2.6)
        St.place(routes, St.FULL, ay=0.15)
        with self.narrate("Leg one moved the prices of things in financial markets. Leg "
                          "two has to turn that into somebody actually spending money. "
                          "And it does it in two ways."):
            self.play(FadeIn(routes[0]), run_time=0.8)
            self.play(FadeIn(routes[1]), run_time=0.8)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the hinge sentence
        self.heading("The sentence the policy rests on")
        q = cards.quote_card("This fall in the cost of capital should boost consumption "
                             "and investment by increasing incentives to borrow and "
                             "reducing incentives to save.",
                             "Bowdler & Radia, p. 612", SRC_BR)
        St.place(q, St.FULL, ay=0.1)
        with self.narrate("And that gives the sentence the whole policy rests on. Their "
                          "words: this fall in the cost of capital should boost "
                          "consumption and investment, by increasing incentives to "
                          "borrow and reducing incentives to save."):
            self.play(FadeIn(q), run_time=1.6)
        self.wait(1.6)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the hedges
        self.heading("And they hedge it, three times")
        firm = W.building(CHALK, size=0.55, kind="office")
        St.place(firm, St.STAGE, ax=-0.75, ay=-0.15)
        flab = Text("a small firm", font=FONT, font_size=T_SMALL, color=MUTED)
        flab.next_to(firm, DOWN, buff=0.28)
        self.play(Create(firm), FadeIn(flab), run_time=1.0)

        hedges = ["banks impaired",
                  "no market access",
                  "may not benefit"]
        says = ["Banks were badly damaged, so any route through them was likely "
                "impaired.",
                "Households and smaller companies have no access to capital markets at "
                "all.",
                "So they may not directly benefit from this channel."]
        shields = VGroup()
        for i, h in enumerate(hedges):
            shields.add(W.shield(SUNK, h, scale=0.9))
        shields.arrange(DOWN, buff=0.32)
        St.place(shields, St.SIDE, ay=0.05)
        for i, sh in enumerate(shields):
            with self.narrate(says[i]):
                self.play(FadeIn(sh, shift=UP * 0.3), run_time=0.8)
        self.beat()

        three = St.caption("hedged three times", SUNK, T_SUB, width=24)
        St.place(three, St.FOOT, pad=0.06)
        self.play(FadeIn(three), S.flash_around(shields, SUNK), run_time=1.4)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the fair-minded part
        self.heading("And they name three ways round it")
        others = [("chain", "supply chains", MONEY),
                  ("border", "a cheaper pound\nhelps exporters", MONEY),
                  ("bank", "banks passing on\nlower rates", MONEY)]
        cols = VGroup()
        for kind, text, col in others:
            cols.add(VGroup(cards.icon(kind, col, 1.5),
                            St.caption(text, col, T_SMALL, width=18)
                            ).arrange(DOWN, buff=0.3))
        cols.arrange(RIGHT, buff=1.1)
        St.place(cols, St.FULL, ay=0.15)
        with self.narrate("And be fair to them, because they do not leave it there. "
                          "They name three further routes by which small firms might "
                          "still benefit."):
            self.play(S.lag_map(FadeIn, cols, shift=UP * 0.25, lag=0.2),
                      run_time=1.6)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the government
        self.heading("What about the government's own borrowing?")
        gov = W.building(SRC_BR, size=0.7, kind="government")
        St.place(gov, St.STAGE, ax=-0.5, ay=0.1)
        ax = Axes(x_range=[0, 6, 1], y_range=[0, 4, 1], x_length=4.4, y_length=2.2,
                  axis_config=AXIS)
        St.place(ax, St.SIDE, ay=0.3)
        curve = ax.plot(lambda x: 3.2 - 0.34 * x, x_range=[0, 6], color=TRIGGER,
                        stroke_width=5)
        cl = Text("gilt yields", font=FONT, font_size=T_TINY, color=TRIGGER)
        cl.next_to(ax, DOWN, buff=0.18)
        with self.narrate("An obvious implication of a fall in gilt yields is that the "
                          "government's own cost of borrowing is now lower. Gilts are "
                          "exactly what was bought."):
            self.play(Create(gov), run_time=1.0)
            self.play(Create(ax), FadeIn(cl), run_time=0.8)
            self.play(Create(curve), run_time=1.2)

        ans = St.caption("plans unaffected —\ngovernments take a\nlonger-term view",
                         MUTED, T_BODY, width=20)
        St.place(ans, St.SIDE, ay=-0.65)
        with self.narrate("And their answer is that it will not change what the "
                          "government does. Governments take a longer-term view. Their "
                          "spending plans should therefore be unaffected by cyclical "
                          "movements in interest rates."):
            self.play(FadeIn(ans), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ wealth
        self.heading("The other route: feeling richer")
        house = W.building(TRIGGER, size=0.8, kind="house")
        St.place(house, St.STAGE, ax=-0.7, ay=-0.1)
        bar = W.Bar(1.0, color=TRIGGER, width=1.0)
        St.place(bar, St.STAGE, ax=0.55, ay=-0.45)
        blab = Text("what they own", font=FONT, font_size=T_SMALL, color=TRIGGER)
        blab.next_to(bar, DOWN, buff=0.24)
        with self.narrate("When asset prices go up, the people who own those assets are "
                          "richer. And higher wealth should mean more spending."):
            self.play(Create(house), run_time=0.9)
            self.play(FadeIn(bar), FadeIn(blab), run_time=0.7)
            self.play(bar.rect.animate.stretch_to_fit_height(2.3).move_to(
                bar.rect.get_bottom() + UP * 1.15), run_time=1.3)

        nums = VGroup(
            Text("£375bn", font=FONT, font_size=T_HEAD, color=SRC_BR),
            Text("of announced purchases", font=FONT, font_size=T_TINY, color=MUTED),
            Text("+30%", font=FONT, font_size=T_HEAD, color=MONEY),
            Text("net financial wealth", font=FONT, font_size=T_TINY, color=MUTED),
        ).arrange(DOWN, buff=0.18)
        St.place(nums, St.SIDE, ay=0.1)
        with self.narrate("They put a number on it. Three hundred and seventy-five "
                          "billion pounds of announced purchases will eventually boost "
                          "British households' net financial wealth by about thirty per "
                          "cent."):
            self.play(FadeIn(nums[0]), FadeIn(nums[1]), run_time=0.9)
            self.play(FadeIn(nums[2]), FadeIn(nums[3]), run_time=0.9)
        self.beat()

        wl = St.caption("largely to those holding the most", MUTED, T_SUB, width=34)
        St.place(wl, St.FOOT, pad=0.06)
        with self.narrate("Those gains went largely to the households holding the most "
                          "financial assets — in particular older and more affluent "
                          "ones. As with all monetary policy, they say, there are "
                          "winners and losers."):
            self.play(FadeIn(wl), run_time=0.9)
        self.beat()

        self.close_chapter([
            "cheaper borrowing, and owners feeling richer",
            "the cost-of-capital sentence, hedged three times",
            "and three named ways round the hedge",
            "£375bn → about +30% of net financial wealth",
        ])
