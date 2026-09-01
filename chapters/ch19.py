import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.scale import MasterScale
from lib.theme import *


class Chapter19(Chapter):
    CH = 19
    TITLE = "What a whole industry looks like"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ['people', 'scale', 'clock', 'risk']

    def body(self):
        with self.narrate("Everything so far has been about one firm. Now put a lot of "
                          "them in one market and see what the market does."):
            pass

        sc = MasterScale(x=-5.0, y=-0.4, height=4.6)
        sc.title.become(Text("The price in\nthe market", font=FONT, font_size=T_SMALL,
                             color=MUTED, line_spacing=0.9).move_to(sc.title))
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), FadeIn(sc.title), run_time=1.0)
        h = sc.add_level("H", 1.62, "H — new firms enter here", TRIGGER, width=3.4, sw=5)
        l = sc.add_level("L", 0.72, "L — firms leave here", TRIGGER, width=3.4, sw=5)
        m = sc.add_level("M", 1.10, "average cost", COST, width=3.4, dashed=True, sw=3)

        crowd = stick.crowd(6, spacing=1.5, scale=0.42)
        crowd.move_to(RIGHT * 2.6 + DOWN * 2.0)
        with self.narrate("Six similar firms, all facing the same swinging demand."):
            self.play(FadeIn(crowd), run_time=0.8)

        with self.narrate("When the price rises to the entry line, new firms come in. "
                          "More supply, and the price stops rising. So the price never "
                          "gets above that line."):
            self.play(Create(h[0]), FadeIn(h[1]), run_time=1.0)
            extra = stick.crowd(2, spacing=1.5, scale=0.42)
            extra.next_to(crowd, RIGHT, buff=0.5).align_to(crowd, DOWN)
            self.play(FadeIn(extra, shift=LEFT * 0.5), run_time=0.9)

        with self.narrate("And when the price falls to the exit line, firms leave. Less "
                          "supply, and the price stops falling. So it never gets below "
                          "that one either."):
            self.play(Create(l[0]), FadeIn(l[1]), run_time=1.0)
            self.play(FadeOut(extra, shift=RIGHT * 0.5), run_time=0.9)

        # -------------------------------------------------- why H is above cost
        ava = stick.ava(scale=0.7).move_to(RIGHT * 5.4 + DOWN * 1.9)
        with self.narrate("Why does the entry line have to sit above average cost? Why "
                          "not exactly at it?", v="c"):
            self.play(FadeIn(ava), Create(m[0]), FadeIn(m[1]), run_time=0.9)

        arg = cards.bullet_list([
            "suppose entry capped price at average cost",
            "never better than normal · sometimes worse",
            "on average: a loss ⇒ nobody enters",
            "so H must leave room for good spells",
        ], color=CHALK, width=32)
        arg.move_to(RIGHT * 1.6 + UP * 1.1)
        if arg.height > 4.0:
            arg.scale(4.0 / arg.height)
        says = ["Suppose entry capped the price exactly at average cost.",
                "Then firms could never do better than normal — and bad spells would "
                "still push them below it.",
                "So on average they would lose. And nobody would enter at all.",
                "Which means the entry line has to leave room for the good spells to "
                "pay for the bad ones. The same argument, upside down, holds the exit "
                "line below day-to-day cost."]
        self.play(FadeOut(crowd), run_time=0.4)
        for i in range(4):
            with self.narrate(says[i]):
                self.play(FadeIn(arg[i], shift=RIGHT * 0.2), run_time=0.6)
        self.beat()
        self.play(FadeOut(arg), FadeOut(ava), run_time=0.5)

        # -------------------------------------------------- the striking result
        same = cards.body("the market's lines = the single firm's lines",
                          size=T_BODY, color=CHALK, width=26)
        same.move_to(RIGHT * 3.4 + UP * 0.8)
        with self.narrate("And here is the striking part. With these particular "
                          "assumptions, the market's two lines turn out to be exactly "
                          "the ones a single firm on its own would have chosen. So "
                          "every number from chapter ten carries straight over."):
            self.play(FadeIn(same), run_time=1.1)
        self.beat()
        cav = cards.note("identical small price-takers only",
                         width=34)
        cav.next_to(same, DOWN, buff=0.5)
        with self.narrate("Carry the caveat, because it matters later. That result "
                          "holds for identical, small, price-taking firms, under the "
                          "paper's particular assumptions. It is not a general truth."):
            self.play(FadeIn(cav), run_time=1.0)
        self.beat()
        self.clear_stage()

        # -------------------------------------------------- the frozen industry
        quote = cards.quote_card(
            "supernormal profits with no new entry, and operating losses without exit",
            "Dixit (1992), p. 126", CHALK, width=40)
        quote.to_edge(UP, buff=0.8)
        if quote.width > 11.4:
            quote.scale(11.4 / quote.width)
        with self.narrate("So what should we expect to see? In the paper's own words: "
                          "significant periods of supernormal profits with no new entry, "
                          "and of operating losses without exit."):
            self.play(FadeIn(quote), run_time=1.1)
        self.beat()

        firms = stick.crowd(6, spacing=1.6, scale=0.5).shift(DOWN * 1.4)
        tags = VGroup(*[Text(t, font=FONT, font_size=T_SMALL, color=c)
                        for t, c in [("profit", MONEY), ("profit", MONEY),
                                     ("profit", MONEY), ("loss", COST),
                                     ("loss", COST), ("profit", MONEY)]])
        for tg, f in zip(tags, firms):
            tg.next_to(f, DOWN, buff=0.2)
        still = Text("nothing happens", font=FONT, font_size=T_SUB, color=MUTED)
        still.next_to(firms, UP, buff=0.9)
        with self.narrate("An industry sitting perfectly still. Profitable firms not "
                          "expanding. Loss-making firms not closing. And nothing wrong "
                          "anywhere."):
            self.play(FadeIn(firms), FadeIn(tags), run_time=1.0)
            self.play(FadeIn(still), run_time=0.7)
        self.beat()
        self.clear_stage()

        # -------------------------------------------------- the warning
        head = Text("The warning for anyone in charge", font=FONT, font_size=T_SUB,
                    color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)
        warns = cards.bullet_list([
            "profits without entry ≠ monopoly",
            "selling below cost ≠ predation",
            "a price cap ⇒ less entry ⇒ HIGHER long-run price",
            "propping up is anticipated ⇒ extra entry ⇒ worse losses",
        ], color=CHALK, width=48)
        warns.move_to(DOWN * 0.2)
        if warns.height > 4.6:
            warns.scale(4.6 / warns.height)
        says = ["A snapshot misleads. Firms making good profits with no new entrants is "
                "not proof of monopoly.",
                "Firms selling below day-to-day cost is not proof of predatory pricing.",
                "And there is a sting. An action aimed at those profits — an antitrust "
                "case, a price cap — depresses entry. And the reduced supply can "
                "actually raise the long-run average price.",
                "And a government that props firms up in bad times will be anticipated. "
                "That draws in extra entry, which makes the losses worse when the bad "
                "times actually arrive."]
        for i in range(4):
            with self.narrate(says[i]):
                self.play(FadeIn(warns[i], shift=RIGHT * 0.2), run_time=0.6)
        self.beat()

        self.close_chapter([
            "entry caps at H · exit floors at L",
            "H above average cost, or nobody enters",
            "profits without entry · losses without exit",
            "a snapshot misleads",
        ])
