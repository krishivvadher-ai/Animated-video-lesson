import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.scale import MasterScale
from lib.theme import *


class Chapter25(Chapter):
    CH = 25
    TITLE = "What a whole industry looks like"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["people", "scale", "clock", "risk"]

    def body(self):
        # ------------------------------------------------ entry and exit
        self.heading("Many firms, between two lines")
        sc = MasterScale(x=-5.4, y=-0.35, height=4.4)
        sc.title.become(Text("The price in\nthe market", font=FONT, font_size=T_SMALL,
                             color=MUTED, line_spacing=0.9).move_to(sc.title))
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), FadeIn(sc.title), run_time=1.0)
        h = sc.add_level("H", 1.62, "H — firms enter", TRIGGER, width=3.0, sw=5)
        l = sc.add_level("L", 0.72, "L — firms leave", TRIGGER, width=3.0, sw=5)
        m = sc.add_level("M", 1.10, "average cost", COST, width=3.0, dashed=True, sw=3)

        crowd = stick.crowd(6, spacing=1.5, scale=0.45)
        St.place(crowd, St.SIDE, ay=-0.62)
        with self.narrate("Six similar firms, all facing the same swinging demand."):
            self.play(S.lag_map(FadeIn, crowd, lag=0.15), run_time=1.2)

        extra = stick.crowd(2, spacing=1.5, scale=0.45)
        extra.next_to(crowd, UP, buff=0.5)
        with self.narrate("When the price rises to the entry line, new firms come in. "
                          "More supply, and the price stops rising. So it never gets "
                          "above that line."):
            self.play(Create(h[0]), FadeIn(h[1]), run_time=1.0)
            self.play(FadeIn(extra, shift=DOWN * 0.4), run_time=1.0)
        with self.narrate("And when the price falls to the exit line, firms leave. Less "
                          "supply, and the price stops falling. So it never gets below "
                          "that one either."):
            self.play(Create(l[0]), FadeIn(l[1]), run_time=1.0)
            self.play(FadeOut(extra, shift=UP * 0.4), run_time=1.0)
        self.beat()
        self.play(FadeOut(crowd), run_time=0.4)

        # ------------------------------------------------ why H is above cost
        self.play(Create(m[0]), FadeIn(m[1]), run_time=0.8)
        self.side(["cap the price at average cost",
                   "never better than normal",
                   "so on average, a loss",
                   "nobody would ever enter"],
                  colour=CHALK, dot_colour=TRIGGER, width=18,
                  spoken=["Why must the entry line sit above average cost? Suppose it "
                          "did not — suppose entry capped the price exactly at average "
                          "cost.",
                          "Then firms could never do better than normal, and bad spells "
                          "would still push them below it.",
                          "So on average they would lose. And nobody would enter at all.",
                          "Which means the entry line has to leave room for the good "
                          "spells to pay for the bad ones. The same argument upside "
                          "down holds the exit line below day-to-day cost."])
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the striking result
        self.heading("The striking part")
        same = St.caption("the market's two lines are the\nsingle firm's two lines",
                          CHALK, T_SUB, width=32)
        St.place(same, St.FULL, ay=0.55)
        with self.narrate("With these particular assumptions, the market's two lines "
                          "turn out to be exactly the ones a single firm on its own "
                          "would have chosen. So every number from chapter twenty-one "
                          "carries straight over."):
            self.play(FadeIn(same), run_time=1.1)
        self.beat()
        with self.narrate("Carry the caveat, because it matters later. That result "
                          "holds for identical, small, price-taking firms, under the "
                          "paper's particular assumptions. It is not a general truth."):
            self.foot("identical small price-takers only", MUTED)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the frozen industry
        self.heading("An industry sitting still")
        q = cards.quote_card(
            "significant periods of supernormal profits with no new entry, and of "
            "operating losses without exit", "Dixit (1992), p. 126", CHALK, width=40)
        St.place(q, St.FULL, ay=0.72)
        with self.narrate("So what should we expect to see? In the paper's own words: "
                          "significant periods of supernormal profits with no new "
                          "entry, and of operating losses without exit."):
            self.play(FadeIn(q), run_time=1.2)
        self.beat()

        firms = stick.crowd(6, spacing=1.7, scale=0.5)
        St.place(firms, St.FULL, ay=-0.55)
        tags = VGroup(*[Text(t, font=FONT, font_size=T_SMALL, color=c)
                        for t, c in [("profit", MONEY), ("profit", MONEY),
                                     ("profit", MONEY), ("loss", COST),
                                     ("loss", COST), ("profit", MONEY)]])
        for tg, f in zip(tags, firms):
            tg.next_to(f, DOWN, buff=0.22)
        with self.narrate("An industry sitting perfectly still. Profitable firms not "
                          "expanding. Loss-making firms not closing. And nothing wrong "
                          "anywhere."):
            self.play(S.lag_map(FadeIn, firms, lag=0.12), run_time=1.2)
            self.play(S.lag_map(FadeIn, tags, lag=0.12), run_time=1.0)
            self.foot("nothing happens — and nothing is wrong", MUTED)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the warning
        self.heading("The warning for anyone in charge")
        self.side(["profits without entry ≠ monopoly",
                   "selling below cost ≠ predation",
                   "a price cap ⇒ less entry ⇒ HIGHER long-run price",
                   "propping firms up draws extra entry"],
                  colour=CHALK, dot_colour=COST, width=26, region=St.FULL,
                  spoken=["A snapshot misleads. Firms making good profits with no new "
                          "entrants is not proof of monopoly.",
                          "Firms selling below day-to-day cost is not proof of "
                          "predatory pricing.",
                          "And there is a sting. An action aimed at those profits — an "
                          "antitrust case, a price cap — depresses entry. And the "
                          "reduced supply can actually raise the long-run average price.",
                          "And a government that props firms up in bad times will be "
                          "anticipated. That draws in extra entry, which makes the "
                          "losses worse when the bad times actually arrive."])
        self.beat()

        self.close_chapter([
            "entry caps at H · exit floors at L",
            "H above average cost, or nobody enters",
            "profits without entry · losses without exit",
            "so a snapshot misleads",
        ])
