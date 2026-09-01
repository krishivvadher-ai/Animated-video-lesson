import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.theme import *


class Chapter27(Chapter):
    CH = 27
    TITLE = "Channels two and three: saying so, and oiling the wheels"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["signal", "clock", "risk", "people"]

    def body(self):
        # ---------------------------------------------------- signalling
        head = Text("Channel two — signalling", font=FONT, font_size=T_SUB,
                    color=WAIT).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)

        gov = stick.governor(scale=0.95).move_to(LEFT * 4.4 + DOWN * 0.6)
        self.play(FadeIn(gov), run_time=0.6)
        with self.narrate("The second channel does not need the money to go anywhere at "
                          "all. It works purely through what the action tells everybody."):
            pass

        waves = VGroup(*[Arc(radius=r, start_angle=-PI / 2.6, angle=PI * 0.75,
                             color=WAIT, stroke_width=4)
                         .move_to(gov.get_right() + RIGHT * r * 0.5)
                         for r in (0.9, 1.5, 2.1)])
        msgs = cards.bullet_list([
            "“We expect to keep rates low for a long time yet.”",
            "“Here is our reading of how bad things are.”",
            "“And we are committed to hitting our target, even down here.”",
        ], color=WAIT, width=30, dotc=WAIT)
        msgs.move_to(RIGHT * 2.2 + UP * 0.5)
        says = ["By loosening policy this much, the Bank is saying it expects to keep "
                "rates low for a long time yet.",
                "It is revealing its own reading of how bad things are.",
                "And by acting at all, it is showing that it is still committed to its "
                "target, and still confident it can hit it — even down at the floor."]
        for i in range(3):
            with self.narrate(says[i]):
                self.play(FadeIn(waves[i]), FadeIn(msgs[i], shift=RIGHT * 0.2),
                          run_time=0.9)
        self.beat()
        anchor = cards.body("expectations stay anchored",
                            size=T_BODY, color=WAIT, width=44)
        anchor.to_edge(DOWN, buff=0.7)
        with self.narrate("Which helps keep people's expectations of future inflation "
                          "anchored. And expectations, as chapter twenty-five will "
                          "show, are themselves a lever."):
            self.play(FadeIn(anchor), run_time=1.0)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- liquidity
        head2 = Text("Channel three — liquidity", font=FONT, font_size=T_SUB,
                     color=MONEY).to_edge(UP, buff=0.7)
        self.play(FadeIn(head2), run_time=0.5)

        self.define("liquidity", "How easily you can sell it.", "flow", MONEY, hold=4.2)

        seller = stick.StickFigure("", CHALK, scale=0.8).move_to(LEFT * 4.0 + DOWN * 0.4)
        asset = W.ticket(MUTED, "something\nto sell", 0.7).move_to(LEFT * 1.4 + DOWN * 0.4)
        empty = cards.body("no buyers", size=T_SUB, color=COST, width=16)
        empty.move_to(RIGHT * 2.4 + DOWN * 0.4)
        with self.narrate("When markets seize up, you may not be able to find a buyer "
                          "at all. So investors demand a higher return to compensate "
                          "them for that risk."):
            self.play(FadeIn(seller), FadeIn(asset), run_time=0.8)
            self.play(FadeIn(empty), seller.mood("worried"), run_time=0.8)
        self.define("liquidity premium", "The extra return for maybe not being able to sell.", "risk", COST,
                    at=UP * 1.8, hold=4.4)

        buyers = VGroup(*[stick.StickFigure("", CHALK, scale=0.5) for _ in range(4)])
        buyers.arrange(RIGHT, buff=0.7).move_to(RIGHT * 2.6 + DOWN * 0.4)
        with self.narrate("A central bank buying on a very large scale is, among other "
                          "things, a buyer. It puts trading back into the market, and "
                          "that premium comes down."):
            self.play(FadeOut(empty), FadeIn(buyers), seller.mood("pleased"),
                      run_time=1.0)
        self.beat()
        small = cards.body("probably only while the buying lasts", size=T_BODY, color=SRC_BR, width=46)
        small.to_edge(DOWN, buff=0.7)
        with self.narrate("But the authors are careful about this one. The effect "
                          "probably lasts only while the purchases are going on. And in "
                          "gilt markets, which are normally very liquid anyway, it may "
                          "be small."):
            self.play(FadeIn(small), run_time=1.2)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- what we can see
        head3 = Text("So which of the three actually did the work?",
                     font=FONT, font_size=T_SUB, color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head3), run_time=0.5)

        three = VGroup(
            VGroup(cards.icon("people", TRIGGER, 1.8),
                   cards.body("portfolio rebalancing", size=T_SMALL, color=TRIGGER, width=14)),
            VGroup(cards.icon("signal", WAIT, 1.8),
                   cards.body("signalling", size=T_SMALL, color=WAIT, width=14)),
            VGroup(cards.icon("flow", MONEY, 1.8),
                   cards.body("liquidity", size=T_SMALL, color=MONEY, width=14)),
        )
        for g in three:
            g.arrange(DOWN, buff=0.35)
        three.arrange(RIGHT, buff=1.8).move_to(UP * 1.0)
        self.play(FadeIn(three), run_time=1.0)

        seen = cards.bullet_list([
            "seen: yields fell, share prices rose",
            "unseen: which channel did it",
        ], color=CHALK, width=44)
        seen.move_to(DOWN * 1.4)
        says = ["Here is what the research can see. Government bond yields fell after "
                "the purchases. Company bond yields fell. Share prices rose.",
                "And here is what it cannot see. Which of those three channels did it. "
                "They are very hard to tell apart, and the authors say so."]
        for i in range(2):
            with self.narrate(says[i]):
                self.play(FadeIn(seen[i], shift=RIGHT * 0.2), run_time=0.8)
        self.beat()
        dis = cards.note("size and persistence: disputed", width=58)
        dis.to_edge(DOWN, buff=0.4)
        with self.narrate("There is also disagreement about how big those effects were "
                          "and how long they lasted. And the effects on wider classes "
                          "of assets are less marked than on company bonds."):
            self.play(FadeIn(dis), run_time=1.0)
        self.beat()

        self.close_chapter([
            "signalling: the act is the message",
            "liquidity: a very large buyer",
            "yields fell · share prices rose",
            "which channel? hard to tell",
        ])
