import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.theme import *


class Chapter33(Chapter):
    CH = 33
    TITLE = "One sentence, two different kinds of claim"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["shield", "people", "queue", "risk"]

    def body(self):
        kit = stick.kit(scale=0.8).move_to(LEFT * 5.4 + DOWN * 1.9)
        self.play(FadeIn(kit), run_time=0.5)

        q = cards.quote_card(
            "This fall in the cost of capital should boost consumption and investment "
            "by increasing incentives to borrow and reducing incentives to save.",
            "Bowdler & Radia (2012), p. 612", SRC_BR, width=44)
        q.move_to(UP * 2.0)
        if q.width > 11.6:
            q.scale(11.6 / q.width)
        with self.narrate("Here is the sentence the whole of Part Two turns on. It is "
                          "on page six hundred and twelve, and these are the authors' "
                          "exact words."):
            self.play(FadeIn(q), run_time=1.2)
        self.beat()

        # -------------------------------------------------- split it in two
        lbox = RoundedRectangle(width=5.6, height=1.5, corner_radius=0.16,
                                color=SRC_BR, stroke_width=3)
        ltxt = cards.body("Does cheaper money ARRIVE at a firm?", size=T_BODY,
                          color=CHALK, width=24)
        ltxt.move_to(lbox.get_center())
        left = VGroup(lbox, ltxt).move_to(LEFT * 3.1 + UP * 0.1)

        rbox = RoundedRectangle(width=5.6, height=1.5, corner_radius=0.16,
                                color=SRC_BR, stroke_width=3)
        rtxt = cards.body("What does a firm DO once it has?", size=T_BODY,
                          color=CHALK, width=24)
        rtxt.move_to(rbox.get_center())
        right = VGroup(rbox, rtxt).move_to(RIGHT * 3.1 + UP * 0.1)

        with self.narrate("It contains two completely different kinds of claim, stitched "
                          "together. Split it in half."):
            self.play(FadeIn(left), FadeIn(right), run_time=1.0)
        with self.narrate("The first half is a question about prices. Does the cheaper "
                          "money actually arrive at a firm? You can go and check that."):
            self.play(Indicate(left, color=SRC_BR, scale_factor=1.03), run_time=1.1)
        with self.narrate("The second half is a question about behaviour. What does a "
                          "firm do once the money has arrived? That is a different sort "
                          "of question entirely."):
            self.play(Indicate(right, color=SRC_BR, scale_factor=1.03), run_time=1.1)
        self.beat()

        # -------------------------------------------------- three shields
        shields = VGroup()
        texts = [
            "a damaged banking sector",
            "small firms cannot sell bonds",
            "a weak bank passes little on",
        ]
        says = [
            "Watch what the authors do to that first half. They attach a qualification "
            "to it. The banking sector was badly damaged when the policy was used, so "
            "anything travelling through it may be impaired.",
            "A second one. Households and smaller companies cannot borrow by selling "
            "bonds to investors, so they may not benefit from that route directly.",
            "And a third. If banks are short of capital of their own, a cheaper funding "
            "cost may barely move the price of the credit they charge.",
        ]
        for i in range(3):
            sh = W.shield(SRC_BR, None, 0.8)
            sh.move_to(left.get_center() + DOWN * 2.0 + RIGHT * (i - 1) * 1.7)
            t = cards.body(texts[i], size=T_SMALL, color=SRC_BR, width=22)
            t.move_to(RIGHT * 3.1 + DOWN * 2.1)
            with self.narrate(says[i]):
                self.play(FadeIn(sh, scale=0.8), run_time=0.6)
                self.play(FadeIn(t), run_time=0.6)
                self.wait(0.5)
                self.play(FadeOut(t), run_time=0.4)
            shields.add(sh)
        self.beat()

        fair = cards.body("three further routes are named",
                          size=T_SMALL, color=SRC_BR, width=30)
        fair.move_to(RIGHT * 3.1 + DOWN * 2.1)
        with self.narrate("And be fair to them. These are honest, careful "
                          "qualifications. They also name several other routes by which "
                          "small firms might still benefit — through supply chains, "
                          "through a cheaper currency helping exporters, and through "
                          "banks passing on lower rates. All of that is in the article."):
            self.play(FadeIn(fair), run_time=1.2)
        self.beat()
        self.play(FadeOut(fair), run_time=0.5)

        # -------------------------------------------------- the missing shield
        wait_t = cards.body("Kit waits for one on the other half.", size=T_BODY,
                            color=SRC_KIT, width=24)
        wait_t.move_to(RIGHT * 3.1 + DOWN * 2.1)
        with self.narrate("Now Kit waits for the same thing to happen to the other half.",
                          v="c"):
            self.play(FadeIn(wait_t), kit.mood("thinking"), run_time=0.8)

        # --- scripted silence #3: none appears
        self.wait(3.6)
        none_t = cards.body("None appears.", size=T_HEAD, color=SRC_KIT, width=20)
        none_t.move_to(RIGHT * 3.1 + DOWN * 2.2)
        self.play(FadeOut(wait_t), FadeIn(none_t), run_time=0.9)
        self.wait(2.6)

        with self.narrate("One half of that sentence is hedged three times. The other "
                          "half is not hedged once."):
            self.play(Indicate(shields, color=SRC_BR, scale_factor=1.2), run_time=1.4)
        self.beat()

        # -------------------------------------------------- Kit's first reaction
        self.clear_stage()
        head = Text("And Kit's first reaction is not disagreement",
                    font=FONT, font_size=T_SUB, color=SRC_KIT).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)
        first = cards.body("two halves. One kind of trust.", size=T_SUB, color=CHALK, width=40)
        first.move_to(UP * 0.6)
        with self.narrate("His first reaction is not disagreement, and that matters for "
                          "everything that follows. His first reaction is that two "
                          "halves of one sentence are not the same kind of statement, "
                          "and are being given the same amount of trust."):
            self.play(FadeIn(first), run_time=1.2)
        self.beat()

        # -------------------------------------------------- the diagnosis
        self.play(FadeOut(first), FadeOut(head), run_time=0.5)
        head2 = Text("And here is the diagnosis — be generous about it",
                     font=FONT, font_size=T_SUB, color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head2), run_time=0.5)

        machine = VGroup(
            Rectangle(width=3.4, height=2.2, color=MUTED, stroke_width=4),
            Rectangle(width=0.8, height=0.16, color=MONEY, stroke_width=3).shift(UP * 0.75),
            VGroup(Line(ORIGIN, RIGHT * 0.7, color=MUTED, stroke_width=6),
                   Dot(RIGHT * 0.7, radius=0.09, color=MUTED)).shift(RIGHT * 1.7 + DOWN * 0.3),
        )
        machine.move_to(LEFT * 2.6 + DOWN * 0.4)
        ml = Text("a firm", font=FONT, font_size=T_BODY, color=MUTED)
        ml.move_to(machine[0].get_center())
        slot = Text("numbers in", font=FONT, font_size=T_SMALL, color=MONEY)
        slot.next_to(machine[1], UP, buff=0.25)
        out = Text("decision out", font=FONT, font_size=T_SMALL, color=MONEY)
        out.next_to(machine[2], RIGHT, buff=0.25)

        with self.narrate("This is not carelessness. It is what a certain kind of "
                          "economics does by construction. It models markets in "
                          "enormous detail, and it treats a firm as a machine. Numbers "
                          "in. Decision out."):
            self.play(Create(machine), FadeIn(ml), run_time=1.2)
            self.play(FadeIn(slot), FadeIn(out), run_time=0.8)

        ok = cards.body("a simplification, not a fault", size=T_BODY, color=CHALK, width=26)
        ok.move_to(RIGHT * 3.6 + UP * 0.8)
        with self.narrate("There is nothing dishonest in that. It is a simplification, "
                          "and simplifications are how anyone thinks about anything "
                          "complicated."):
            self.play(FadeIn(ok), run_time=1.0)
        self.beat()
        but = cards.body("so the last link is never examined", size=T_SUB, color=SRC_KIT, width=26)
        but.move_to(RIGHT * 3.6 + DOWN * 1.6)
        with self.narrate("But it does mean that the last link in the chain is the only "
                          "one nobody examines."):
            self.play(FadeIn(but), run_time=1.0)
        self.beat()

        self.close_chapter([
            "one sentence, two kinds of claim",
            "“does it arrive?” — hedged 3 times",
            "“what does a firm do?” — not hedged",
            "a firm modelled as a machine",
        ])
