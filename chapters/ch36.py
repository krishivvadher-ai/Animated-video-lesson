import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter36(Chapter):
    CH = 36
    TITLE = "The result that says none of it works"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["risk", "people", "signal", "clock"]

    def body(self):
        kit = stick.kit(scale=0.85)
        St.place(kit, St.STAGE, ax=-0.75, ay=-0.45)
        with self.narrate("The authors do something in this section that a less honest "
                          "article would have left out. They set out, at length, a "
                          "well-known result which says the whole policy does nothing "
                          "at all.", v="c"):
            self.heading("A result that says none of it works")
            self.play(FadeIn(kit), run_time=0.7)
            self.play(kit.mood("surprised"), run_time=0.4)
        self.play(FadeOut(kit), run_time=0.4)

        # ------------------------------------------------ the swap again
        self.heading("Every channel assumed one thing")
        seller = stick.StickFigure("the seller", MONEY, scale=0.75)
        St.place(seller, St.STAGE, ax=-0.8, ay=-0.4)
        risky = W.ticket(COST, "risky", scale=0.9)
        safe = VGroup(*[W.coin(MONEY, 0.19) for _ in range(3)]).arrange(RIGHT, buff=0.12)
        swap = VGroup(risky, safe).arrange(RIGHT, buff=1.6)
        St.place(swap, St.STAGE, ax=0.35, ay=0.45)
        with self.narrate("The seller hands over something risky and gets back "
                          "something safe. Every channel so far has assumed that "
                          "changes how much risk the private sector is carrying."):
            self.play(FadeIn(seller), FadeIn(seller.label()), run_time=0.8)
            self.play(FadeIn(risky), run_time=0.7)
            self.play(FadeTransform(risky.copy(), safe), run_time=1.1)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ risk moves round a circle
        self.heading("But follow the risk all the way round")
        nodes = []
        names = [("the private\nsector", MONEY), ("the central\nbank", SRC_BR),
                 ("the government", TRIGGER), ("households,\nin taxes", COST)]
        ring = VGroup()
        radius = 1.75
        for i, (name, col) in enumerate(names):
            ang = PI / 2 - i * TAU / 4
            c = Circle(radius=0.52, color=col, stroke_width=4,
                       fill_color=col, fill_opacity=0.16)
            c.move_to(radius * np.array([np.cos(ang), np.sin(ang), 0]) * 1.25)
            t = Text(name, font=FONT, font_size=T_SMALL, color=col,
                     line_spacing=0.92)
            t.next_to(c, DOWN if i in (2,) else UP, buff=0.22)
            if i == 1:
                t.next_to(c, RIGHT, buff=0.22)
            if i == 3:
                t.next_to(c, LEFT, buff=0.22)
            nodes.append(c)
            ring.add(VGroup(c, t))
        St.place(ring, St.FULL, ay=0.05)

        blob = Dot(nodes[0].get_center(), radius=0.2, color=COST)
        with self.narrate("Start with the risk sitting in the private sector."):
            self.play(FadeIn(ring[0]), run_time=0.7)
            self.play(GrowFromCenter(blob), run_time=0.5)

        says = ["It did not disappear. It moved onto the central bank's own books.",
                "And who owns the central bank? The government.",
                "And who pays for the government? Households, through the taxes they "
                "will pay in future."]
        for i in range(1, 4):
            with self.narrate(says[i - 1]):
                self.play(FadeIn(ring[i]), run_time=0.6)
                self.play(blob.animate.move_to(nodes[i].get_center()), run_time=0.9)
                self.play(S.spark(blob, COST), run_time=0.4)

        with self.narrate("And households are the private sector. The risk has gone all "
                          "the way round and come back to exactly where it started."):
            self.play(blob.animate.move_to(nodes[0].get_center()), run_time=1.2)
            self.play(S.flash_around(ring[0], COST))

        nothing = St.caption("nothing to rebalance, so nothing happens",
                             COST, T_SUB, width=44)
        St.place(nothing, St.FOOT, pad=0.06)
        with self.narrate("So the household's risk, taken as a whole, has not changed. "
                          "There is nothing to rebalance. And the policy does nothing "
                          "at all."):
            self.play(FadeIn(nothing), run_time=0.9)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the assumptions
        self.heading("It rests on very strong assumptions")
        assumptions = St.points(["people see through to the state's books",
                                 "no limits on who can hold what",
                                 "taxes fall on the very same people"],
                                colour=CHALK, dot_colour=MUTED, size=T_BODY, width=34)
        St.place(assumptions, St.FULL, ay=0.4)
        says = ["People have to see straight through to the state's own books.",
                "There must be no limits on who can hold what.",
                "And the future taxes must fall on the very same people."]
        for i, row in enumerate(assumptions):
            with self.narrate(says[i]):
                self.play(FadeIn(row), run_time=0.7)
        strong = St.caption("their words: very strong", SUNK, T_SUB, width=26)
        St.place(strong, St.FOOT, pad=0.06)
        with self.narrate("And the authors say it plainly. Those assumptions are very "
                          "strong."):
            self.play(FadeIn(strong), run_time=0.8)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the way out
        self.heading("The way out, and the catch in it")
        gov = stick.governor(scale=0.85)
        St.place(gov, St.STAGE, ax=-0.7, ay=-0.35)
        promise = gov.say("rates stay low\nlonger than you think", direction=UP,
                          width=3.4)
        with self.narrate("There is one way out of it, and it is a promise. The central "
                          "bank says it will hold rates low for longer than it "
                          "otherwise would — even once things have recovered."):
            self.play(FadeIn(gov), run_time=0.7)
            self.play(FadeIn(promise), run_time=0.9)

        believed = St.caption("but it has to be believed", TRIGGER, T_SUB, width=26)
        St.place(believed, St.SIDE, ay=0.7)
        with self.narrate("And here is the catch, which the authors are careful about. "
                          "The promise has to be believed."):
            self.play(FadeIn(believed), run_time=0.8)

        gone = St.caption("recovery removes the reason to keep it", COST,
                          T_BODY, width=24)
        St.place(gone, St.SIDE, ay=-0.2)
        with self.narrate("But once the economy has recovered — precisely because "
                          "everyone believed the promise — the central bank has no "
                          "reason left to keep it."):
            self.play(FadeOut(promise), run_time=0.5)
            self.play(FadeIn(gone), run_time=0.8)
        self.beat()

        self.clear_stage()
        line = St.caption("a promise nobody must keep\nis a promise nobody believes",
                          CHALK, T_HEAD, width=30)
        St.place(line, St.FULL, ay=0.15)
        with self.narrate("A promise nobody has to keep is a promise nobody believes."):
            self.play(Write(line), run_time=2.0)
        self.beat()
        self.clear_stage()

        self.heading("Which leaves the action itself")
        act = VGroup(cards.icon("signal", SRC_BR, 2.2),
                     St.caption("an action, not a promise", SRC_BR, T_SUB, width=26)
                     ).arrange(DOWN, buff=0.35)
        St.place(act, St.FULL, ay=0.2)
        with self.narrate("Which is why one reading of quantitative easing is that its "
                          "real job was the signalling all along — an action, rather "
                          "than a promise, and actions are harder to take back."):
            self.play(Create(act[0]), run_time=1.0)
            self.play(FadeIn(act[1]), run_time=0.8)
            self.play(S.flash_around(act, SRC_BR, run_time=2.0))
        self.beat()

        self.close_chapter([
            "risk moved to the state and back through taxes",
            "so in that world the policy does nothing",
            "the assumptions behind it are very strong",
            "and the way out is a promise nobody must keep",
        ])
