import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.theme import *


class Chapter26(Chapter):
    CH = 26
    TITLE = "Channel one: the hot potato"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["ticket", "people", "risk", "border"]

    def body(self):
        with self.narrate("Leg one of the chain has three channels, and this is the "
                          "big one. The one the Bank of England itself puts first."):
            pass

        # ---------------------------------------------------- perfect substitutes
        head = Text("First, the case where NOTHING happens",
                    font=FONT, font_size=T_SUB, color=COST).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)

        a = VGroup(W.ticket(MUTED, "short-dated\ngilt", 0.75),
                   Text("pays almost nothing", font=FONT, font_size=T_SMALL, color=MUTED))
        a[1].next_to(a[0], DOWN, buff=0.25)
        b = VGroup(W.money_bag(MUTED, 1.0),
                   Text("money — pays nothing", font=FONT, font_size=T_SMALL, color=MUTED))
        b[1].next_to(b[0], DOWN, buff=0.25)
        pair = VGroup(a, b).arrange(RIGHT, buff=2.4).move_to(UP * 0.5)
        eq = Text("≈", font=FONT, font_size=60, color=MUTED).move_to(pair.get_center())
        with self.narrate("At the zero lower bound, money pays nothing. And a piece of "
                          "government debt that matures next month, at a rate of "
                          "practically zero, also pays nothing."):
            self.play(FadeIn(pair), run_time=1.0)
            self.play(FadeIn(eq), run_time=0.6)

        self.define("perfect substitutes", "Two things a holder simply does not care "
                    "between.", "scale", COST, at=DOWN * 2.0, hold=4.0)
        with self.narrate("If the seller does not care which of those two it holds, the "
                          "story ends right there. It takes the money, puts it in a "
                          "drawer, and nothing else moves."):
            self.play(pair.animate.set_opacity(0.35), run_time=1.0)
        trap = cards.body("a trap", size=T_BODY, color=COST, width=44)
        trap.to_edge(DOWN, buff=0.8)
        with self.narrate("Economists have a name for that. And buying short-dated "
                          "debt with money — what is sometimes called pure quantitative "
                          "easing — can run straight into it. Japan did exactly that "
                          "between two thousand and one and two thousand and six."):
            self.play(FadeIn(trap), run_time=1.2)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- imperfect substitutes
        head2 = Text("So buy something that is NOT like money",
                    font=FONT, font_size=T_SUB, color=MONEY).to_edge(UP, buff=0.7)
        self.play(FadeIn(head2), run_time=0.5)

        ladder = VGroup()
        rungs = [("money", MUTED), ("short gilt", MUTED), ("10-year gilt", WAIT),
                 ("corporate bond", TRIGGER), ("shares", MONEY)]
        for i, (name, col) in enumerate(rungs):
            r = VGroup(RoundedRectangle(width=2.6, height=0.62, corner_radius=0.1,
                                        color=col, stroke_width=3),
                       Text(name, font=FONT, font_size=T_SMALL, color=col))
            r[1].move_to(r[0].get_center())
            ladder.add(r)
        ladder.arrange(UP, buff=0.28).move_to(LEFT * 4.2 + DOWN * 0.2)
        arrow = Arrow(ladder.get_bottom() + DOWN * 0.25 + LEFT * 1.9,
                      ladder.get_top() + UP * 0.25 + LEFT * 1.9, color=MUTED,
                      buff=0, stroke_width=4)
        al = Text("riskier", font=FONT, font_size=T_TINY, color=MUTED)
        al.next_to(arrow, LEFT, buff=0.15)
        with self.narrate("Line up the things somebody can hold, from the safest at the "
                          "bottom to the riskiest at the top."):
            self.play(LaggedStart(*[FadeIn(r) for r in ladder], lag_ratio=0.2),
                      run_time=2.0)
            self.play(Create(arrow), FadeIn(al), run_time=0.6)

        with self.narrate("A ten-year gilt pays more than money. Sell it and hold the "
                          "money instead, and the return on your whole portfolio drops."):
            self.play(Indicate(ladder[2], color=WAIT, scale_factor=1.08), run_time=1.2)

        reasons = cards.bullet_list([
            "its preferred habitat",
            "pushed out of that habitat",
            "fewer left ⇒ price up, yield down",
        ], color=CHALK, width=32, dotc=WAIT)
        reasons.move_to(RIGHT * 2.4 + UP * 0.6)
        if reasons.height > 3.6:
            reasons.scale(3.6 / reasons.height)
            reasons.move_to(RIGHT * 2.4 + UP * 0.6)
        says = ["And there is a second reason. A pension fund likes to hold long-dated "
                "assets, so that they mature at about the time it has to pay its "
                "pensioners. Economists call that its preferred habitat.",
                "Selling its gilts moves it away from that habitat.",
                "And because the central bank has taken long gilts out of the market, "
                "there are fewer left. The price of the ones remaining rises, and their "
                "yield falls. That is called a local supply effect."]
        for i in range(3):
            with self.narrate(says[i]):
                self.play(FadeIn(reasons[i], shift=RIGHT * 0.2), run_time=0.7)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- duration
        head3 = Text("And a second effect, on risk itself",
                     font=FONT, font_size=T_SUB, color=TRIGGER).to_edge(UP, buff=0.7)
        self.play(FadeIn(head3), run_time=0.5)
        self.define("duration", "How much its price swings with rates.", "ticket", TRIGGER, hold=4.4)
        self.define("term premium", "The extra return for bearing that swing.", "risk", TRIGGER, hold=4.4)

        pool = Circle(radius=1.8, color=TRIGGER, stroke_width=4, fill_color=TRIGGER,
                      fill_opacity=0.18).move_to(LEFT * 3.0 + DOWN * 0.3)
        pl = cards.body("all the interest-rate risk in the market", size=T_SMALL,
                        color=TRIGGER, width=18)
        pl.next_to(pool, DOWN, buff=0.3)
        with self.narrate("Think of all the interest-rate risk in the bond market as one "
                          "pool, which somebody has to carry."):
            self.play(Create(pool), FadeIn(pl), run_time=1.0)
        small = Circle(radius=1.15, color=TRIGGER, stroke_width=4, fill_color=TRIGGER,
                       fill_opacity=0.18).move_to(pool.get_center())
        with self.narrate("When the central bank buys long-dated bonds, it carries some "
                          "of that risk itself. So there is less left for everybody "
                          "else to carry."):
            self.play(Transform(pool, small), run_time=1.6)
        less = cards.body("less risk to carry ⇒ lower long rates",
                          size=T_BODY, color=TRIGGER, width=26)
        less.move_to(RIGHT * 3.2 + DOWN * 0.2)
        with self.narrate("And so the extra return they demand for carrying it falls, "
                          "which pushes longer-term real interest rates down. That is "
                          "the thinking behind the American programme nicknamed "
                          "operation twist."):
            self.play(FadeIn(less), run_time=1.0)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- the hot potato
        head4 = Text("And then it spreads", font=FONT, font_size=T_SUB,
                     color=MONEY).to_edge(UP, buff=0.7)
        self.play(FadeIn(head4), run_time=0.5)

        holders = VGroup(*[stick.StickFigure("", CHALK, scale=0.55) for _ in range(5)])
        holders.arrange(RIGHT, buff=1.6).move_to(DOWN * 0.6)
        labels = VGroup(*[Text(t, font=FONT, font_size=T_TINY, color=MUTED)
                          for t in ["sells gilts", "buys corporate\nbonds",
                                    "buys foreign\nbonds", "buys shares",
                                    "prices adjust"]])
        for l, h in zip(labels, holders):
            l.next_to(h, DOWN, buff=0.25)
        self.play(FadeIn(holders), run_time=0.8)

        potato = Dot(holders[0].get_top() + UP * 0.4, radius=0.16, color=MONEY)
        with self.narrate("The seller has money it did not want. So it goes looking for "
                          "something else to hold — something a little riskier, which "
                          "is now relatively cheap."):
            self.play(FadeIn(potato), FadeIn(labels[0]), run_time=0.8)
        for i in range(1, 5):
            with self.narrate(["It buys company debt. Now whoever sold that has money "
                               "it did not want.",
                               "That one buys foreign government bonds. Which, by the "
                               "way, pushes the pound down and helps exporters.",
                               "That one buys shares.",
                               "And it carries on until every price has moved far "
                               "enough that, taken together, everybody is content to "
                               "hold what there is."][i - 1]):
                self.play(potato.animate.move_to(holders[i].get_top() + UP * 0.4),
                          FadeIn(labels[i]), run_time=1.2)
        self.beat()
        name = cards.body("a hot potato", size=T_SUB, color=MONEY, width=40)
        name.to_edge(DOWN, buff=0.7)
        with self.narrate("The authors call it passing the money around like a hot "
                          "potato. Nobody wants to be left holding it."):
            self.play(FadeIn(name), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- what limits it
        head5 = Text("And here is what can stop it working",
                     font=FONT, font_size=T_SUB, color=COST).to_edge(UP, buff=0.7)
        self.play(FadeIn(head5), run_time=0.5)
        limits = [
            ("risk", "no appetite → nobody climbs the ladder"),
            ("shield", "a safety premium works against it"),
            ("fog", "uncertainty makes shares a worse substitute"),
            ("queue", "rules can force them to hold gilts"),
        ]
        rows = VGroup()
        for kind, text in limits:
            ic = cards.icon(kind, COST, 1.5)
            t = cards.body(text, size=T_SMALL, color=CHALK, width=42)
            r = VGroup(ic, t).arrange(RIGHT, buff=0.4, aligned_edge=UP)
            rows.add(r)
        rows.arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to(DOWN * 0.2)
        if rows.height > 4.4:
            rows.scale(4.4 / rows.height)
            rows.move_to(DOWN * 0.2)
        says = ["If investors have no appetite for risk, they simply will not climb the "
                "ladder. And money flowed away from risky assets in this period, not "
                "towards them.",
                "In a panic, people pay extra for things that are safe and easy to "
                "sell. A safety premium, which works directly against the whole idea.",
                "Heightened uncertainty about what shares will pay makes them a worse "
                "substitute for gilts, not a better one.",
                "And rules facing pension funds and insurers can require them to hold "
                "government debt — so they cannot move even if they would like to."]
        for i in range(4):
            with self.narrate(says[i]):
                self.play(FadeIn(rows[i], shift=RIGHT * 0.2), run_time=0.7)
        self.beat()

        self.close_chapter([
            "same thing to the holder ⇒ nothing happens",
            "so buy long gilts, company debt, mortgages",
            "the hot potato, until prices adjust",
            "fear and rules can stop it",
        ])
