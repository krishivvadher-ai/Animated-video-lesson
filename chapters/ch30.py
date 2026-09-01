import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.theme import *


class Chapter30(Chapter):
    CH = 30
    TITLE = "The result that says none of it works"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["shield", "people", "risk", "signal"]

    def body(self):
        with self.narrate("The authors do something in this section that a less honest "
                          "article would have left out. They set out, at length, a "
                          "well-known result which says the whole policy does nothing "
                          "at all."):
            pass

        # ---------------------------------------------------- the setup
        head = Text("Start with what everything so far assumed",
                    font=FONT, font_size=T_SUB, color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)
        a = VGroup(W.ticket(WAIT, "a long gilt", 0.8),
                   Text("risky", font=FONT, font_size=T_SMALL, color=COST))
        a[1].next_to(a[0], DOWN, buff=0.25)
        b = VGroup(W.money_bag(MONEY, 0.9),
                   Text("safe", font=FONT, font_size=T_SMALL, color=MONEY))
        b[1].next_to(b[0], DOWN, buff=0.25)
        swap = VGroup(a, b).arrange(RIGHT, buff=3.2).move_to(UP * 0.4)
        arr = Arrow(a.get_right() + RIGHT * 0.2, b.get_left() + LEFT * 0.2,
                    color=MUTED, buff=0, stroke_width=5)
        with self.narrate("The seller hands over something risky and gets back "
                          "something safe. Every channel so far has assumed that "
                          "changes how much risk the private sector is carrying."):
            self.play(FadeIn(swap), Create(arr), run_time=1.2)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- the objection
        head2 = Text("But where did the risk actually go?",
                     font=FONT, font_size=T_SUB, color=COST).to_edge(UP, buff=0.7)
        self.play(FadeIn(head2), run_time=0.5)

        cb = W.building(SRC_BR, 0.7, "bank", "the central bank").move_to(
            LEFT * 3.8 + UP * 0.6)
        risk = VGroup(cards.icon("risk", COST, 2.2),
                      Text("the risk", font=FONT, font_size=T_SMALL, color=COST))
        risk[1].next_to(risk[0], DOWN, buff=0.2)
        risk.move_to(RIGHT * 3.6 + UP * 1.2)
        with self.narrate("It did not disappear. It moved onto the central bank's own "
                          "books."):
            self.play(FadeIn(cb), run_time=0.9)
            self.play(risk.animate.move_to(cb.get_center() + UP * 0.1).scale(0.7),
                      run_time=1.4)
        self.beat()

        houses = VGroup(*[W.building(CHALK, 0.5, "house") for _ in range(4)])
        houses.arrange(RIGHT, buff=0.7).move_to(DOWN * 2.0)
        hl = Text("households", font=FONT, font_size=T_SMALL, color=MUTED)
        hl.next_to(houses, DOWN, buff=0.25)
        link = Line(cb.get_bottom() + DOWN * 0.15, houses.get_top() + UP * 0.15,
                    color=MUTED, stroke_width=3).add_tip(tip_length=0.16)
        tax = Text("future taxes", font=FONT, font_size=T_SMALL, color=COST)
        tax.next_to(link, RIGHT, buff=0.25)
        with self.narrate("And who owns the central bank? The government. And who pays "
                          "for the government? Households, through the taxes they will "
                          "pay in future."):
            self.play(FadeIn(houses), FadeIn(hl), run_time=0.9)
            self.play(Create(link), FadeIn(tax), run_time=1.0)
        self.beat()

        # ---------------------------------------------------- the concrete example
        self.clear_stage()
        head3 = Text("The example the authors give", font=FONT, font_size=T_SUB,
                     color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head3), run_time=0.5)
        steps = cards.bullet_list([
            "the bank buys assets tied to house prices",
            "house prices crash",
            "the bank earns less",
            "so it hands less to the Treasury",
            "so taxes are higher",
        ], color=CHALK, width=30, dotc=COST)
        steps.move_to(LEFT * 3.0)
        says = ["Suppose the central bank buys assets tied to house prices.",
                "Now suppose house prices crash.",
                "The central bank earns less.",
                "So it hands less over to the Treasury.",
                "So taxes end up higher. And the household is worse off in the crash "
                "either way — whether it held those assets or the central bank did."]
        for i in range(5):
            with self.narrate(says[i]):
                self.play(FadeIn(steps[i], shift=RIGHT * 0.2), run_time=0.6)
        self.beat()

        concl = cards.body("So the household's risk, taken as a whole, has not changed. "
                           "Nothing needs rebalancing. The policy does nothing.",
                           size=T_SUB, color=COST, width=26)
        concl.move_to(RIGHT * 3.4)
        if concl.width > 5.6:
            concl.scale(5.6 / concl.width)
        with self.narrate("So the household's risk, taken as a whole, has not changed. "
                          "There is nothing to rebalance. And the policy does nothing "
                          "at all."):
            self.play(FadeIn(concl), run_time=1.0)
        self.beat()
        self.define("the irrelevance proposition", "The result that says asset "
                    "purchases cannot work, because the risk never really moves.",
                    "shield", COST, at=DOWN * 2.4, hold=4.8)

        # ---------------------------------------------------- how strong is it
        self.clear_stage()
        head4 = Text("How much weight will it bear?", font=FONT, font_size=T_SUB,
                     color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head4), run_time=0.5)
        person = stick.StickFigure("a household", CHALK, scale=0.9).move_to(
            LEFT * 4.2 + DOWN * 0.4)
        self.play(FadeIn(person), run_time=0.6)
        needs = cards.bullet_list([
            "sees through to the government's books",
            "works out the future tax bill",
            "and adjusts today",
        ], color=CHALK, width=26, dotc=MUTED)
        needs.move_to(RIGHT * 1.2 + UP * 0.6)
        says2 = ["For that to work, a household has to see through to the government's "
                 "own books.",
                 "Work out what its future tax bill will be.",
                 "And adjust what it does today, accordingly."]
        for i in range(3):
            with self.narrate(says2[i]):
                self.play(FadeIn(needs[i], shift=RIGHT * 0.2), run_time=0.6)
                self.play(person.mood(["thinking", "thinking", "surprised"][i]),
                          run_time=0.3)
        self.beat()
        strong = cards.body("The authors say it plainly: those assumptions are very "
                            "strong.", size=T_SUB, color=SRC_BR, width=40)
        strong.to_edge(DOWN, buff=0.8)
        with self.narrate("And the authors say it plainly. Those assumptions are very "
                          "strong."):
            self.play(FadeIn(strong), run_time=0.9)
        self.beat()

        # ---------------------------------------------------- what to do instead
        self.clear_stage()
        head5 = Text("And if you believe it, you do something else instead",
                     font=FONT, font_size=T_SUB, color=WAIT).to_edge(UP, buff=0.7)
        self.play(FadeIn(head5), run_time=0.5)

        chain = cards.bullet_list([
            "at zero, the only way to make borrowing cheaper in real terms is to "
            "raise what people expect prices to do",
            "so promise to run policy looser than usual, for longer",
            "which means promising to overshoot the inflation target later",
            "to avoid a bigger undershoot now",
        ], color=CHALK, width=40, dotc=WAIT)
        chain.move_to(UP * 0.4)
        says3 = ["When the rate is already at zero, the only way left to make borrowing "
                 "cheaper in real terms is to raise what people expect prices to do.",
                 "So the central bank promises to run policy looser than it otherwise "
                 "would, for longer.",
                 "Which means promising to let inflation overshoot its target later.",
                 "In order to avoid a much bigger undershoot now."]
        for i in range(4):
            with self.narrate(says3[i]):
                self.play(FadeIn(chain[i], shift=RIGHT * 0.2), run_time=0.7)
        self.beat()

        # ---------------------------------------------------- time inconsistency
        self.play(FadeOut(chain), run_time=0.5)
        gov = stick.governor(scale=0.9).move_to(LEFT * 4.0 + DOWN * 0.6)
        crowd = stick.crowd(4, spacing=1.4, scale=0.5).move_to(RIGHT * 2.4 + DOWN * 0.6)
        self.play(FadeIn(gov), FadeIn(crowd), run_time=0.8)
        promise = gov.say("I promise to keep\nrates low.", direction=UP, width=3.2)
        with self.narrate("And here is the catch, which the authors are careful about. "
                          "The promise has to be believed."):
            self.play(FadeIn(promise), run_time=0.8)
        with self.narrate("But once the economy has recovered — precisely because "
                          "everyone believed the promise — the central bank has no "
                          "reason left to keep it."):
            self.play(*[f.mood("thinking") for f in crowd], run_time=0.6)
            self.play(FadeOut(promise), run_time=0.5)
            doubt = crowd[1].think("Will they, though?", direction=UP, width=2.8,
                                   color=COST)
            self.play(FadeIn(doubt), run_time=0.8)
        self.beat()
        name = cards.body("A promise nobody has to keep is a promise nobody believes.",
                          size=T_SUB, color=COST, width=36)
        name.to_edge(DOWN, buff=0.8)
        with self.narrate("A promise nobody has to keep is a promise nobody believes. "
                          "Which is why one reading of quantitative easing is that its "
                          "real job was the signalling all along — an action, rather "
                          "than a promise, and actions are harder to take back."):
            self.play(FadeIn(name), run_time=1.2)
        self.beat()

        self.close_chapter([
            "one well-known result says asset purchases cannot work at all",
            "because the risk only moves to the government, and back through taxes",
            "its assumptions are very strong, and the authors say so",
            "on that view, what matters is a promise about the future — which is hard to believe",
        ])
