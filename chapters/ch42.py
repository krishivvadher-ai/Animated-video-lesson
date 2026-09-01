import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.theme import *


class Chapter42(Chapter):
    CH = 42
    TITLE = "The management half: a queue, not a calculation"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["queue", "people", "clock", "scale"]

    def body(self):
        # ---------------------------------------------------- grow the firm
        small = W.factory(CHALK, 0.6).move_to(LEFT * 4.6 + UP * 0.4)
        with self.narrate("Grow Nell's factory into a large company, with several "
                          "separately run parts."):
            self.play(FadeIn(small), run_time=0.7)
        big = VGroup(*[W.factory(CHALK, 0.42) for _ in range(4)])
        big.arrange_in_grid(2, 2, buff=0.7).move_to(LEFT * 4.0 + UP * 0.4)
        self.play(ReplacementTransform(small, big), run_time=1.4)

        self.define("division", "A separately run part of a company.", "people", CHALK,
                    at=RIGHT * 2.4, hold=4.0)
        self.define("capital budget", "The pot a board shares out.", "money", MONEY, at=RIGHT * 2.4, hold=4.0)
        self.define("hurdle rate, as an object", "A minimum return, written down.", "scale", SRC_KIT, at=RIGHT * 2.0, hold=5.4)

        # ---------------------------------------------------- concede Dixit
        self.clear_stage()
        head = Text("First, concede Dixit — entirely", font=FONT, font_size=T_SUB,
                    color=SRC_DX).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)
        conc = cards.bullet_list([
            "he explains why it is high",
            "worked out from OUTSIDE things",
            "an outside price in disguise",
        ], color=CHALK, width=42, dotc=SRC_DX)
        conc.move_to(UP * 0.6)
        says = ["Dixit already explains why that number is high, and he does it well.",
                "In his model it is worked out from things outside the company. The "
                "cost of its money, how choppy its market is, how fast that market is "
                "growing.",
                "It is an outside price wearing a disguise. And if the outside price "
                "moves, the number moves."]
        for i in range(3):
            with self.narrate(says[i]):
                self.play(FadeIn(conc[i], shift=RIGHT * 0.2), run_time=0.7)
        self.beat()
        disp = cards.body("not HOW HIGH — what KIND",
                          size=T_SUB, color=SRC_KIT, width=40)
        disp.to_edge(DOWN, buff=0.8)
        with self.narrate("So say this explicitly, because it is easy to miss. Kit's "
                          "dispute is not about how high the number is. It is about "
                          "what kind of number it is."):
            self.play(FadeIn(disp), run_time=1.0)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- the queue
        boardroom = W.door(CHALK, 1.4, 2.8, "the boardroom").move_to(RIGHT * 4.6 + UP * 0.1)
        self.play(Create(boardroom), run_time=0.8)
        projects = VGroup(*[
            VGroup(RoundedRectangle(width=1.5, height=0.8, corner_radius=0.1,
                                    color=WAIT, stroke_width=3),
                   Text(f"project {i+1}", font=FONT, font_size=T_TINY, color=WAIT))
            for i in range(5)])
        for p in projects:
            p[1].move_to(p[0].get_center())
        projects.arrange(LEFT, buff=0.45).next_to(boardroom, LEFT, buff=0.7)
        with self.narrate("And here is the mechanism, as an actual queue of projects at "
                          "the boardroom door."):
            self.play(LaggedStart(*[FadeIn(p, shift=LEFT * 0.3) for p in projects],
                                  lag_ratio=0.25), run_time=2.0)

        assum = cards.body("what runs out first is MANAGEMENT, not money",
                           size=T_BODY, color=SRC_KIT, width=44)
        assum.to_edge(DOWN, buff=0.7)
        with self.narrate("State the assumption openly, because it is doing a lot of "
                          "work and it might be wrong. In a large company the thing "
                          "that runs out first is not money. It is management."):
            self.play(FadeIn(assum), run_time=1.2)
        self.beat()
        self.play(FadeOut(assum), run_time=0.4)

        chain = cards.bullet_list([
            "more ideas than capable people",
            "managers argue for their own",
            "the board cannot check",
            "the problem is CHOOSING",
        ], color=CHALK, width=34, dotc=SRC_KIT)
        chain.move_to(LEFT * 2.0 + DOWN * 1.6)
        if chain.height > 3.0:
            chain.scale(3.0 / chain.height)
            chain.move_to(LEFT * 2.0 + DOWN * 1.6)
        says = ["There are always more ideas than there are people capable of running "
                "them properly.",
                "Divisional managers push their own projects, and present them "
                "optimistically, because that is what advocating for your division "
                "looks like.",
                "And the board cannot verify what it is told.",
                "So the board's real problem is not working out what each project is "
                "worth. It is choosing between them."]
        for i in range(4):
            with self.narrate(says[i]):
                self.play(FadeIn(chain[i], shift=RIGHT * 0.2), run_time=0.6)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- the yield falls
        head2 = Text("A minimum return set to solve THAT problem",
                     font=FONT, font_size=T_SUB, color=SRC_KIT).to_edge(UP, buff=0.7)
        self.play(FadeIn(head2), run_time=0.5)
        tied = cards.body("tied to the NEXT project in the queue",
                          size=T_BODY, color=CHALK, width=42)
        tied.move_to(UP * 1.2)
        with self.narrate("A minimum return set to solve that problem is tied to the "
                          "next project in the queue — the best thing the company would "
                          "have to drop in order to take this one on. And that is an "
                          "internal quantity. It depends on how many good ideas the "
                          "business is generating, and how many capable people it has "
                          "spare."):
            self.play(FadeIn(tied), run_time=1.4)
        self.beat()

        yld = VGroup(
            Text("the return on government debt", font=FONT, font_size=T_SMALL, color=SRC_BR),
            Arrow(UP * 0.6, DOWN * 0.6, color=SRC_BR, buff=0, stroke_width=6))
        yld.arrange(DOWN, buff=0.3).move_to(LEFT * 3.4 + DOWN * 1.6)
        queue = VGroup(*[RoundedRectangle(width=0.9, height=0.5, corner_radius=0.08,
                                          color=WAIT, stroke_width=3)
                         for _ in range(4)]).arrange(RIGHT, buff=0.3)
        queue.move_to(RIGHT * 2.6 + DOWN * 1.6)
        ql = Text("the queue", font=FONT, font_size=T_SMALL, color=WAIT)
        ql.next_to(queue, DOWN, buff=0.25)
        with self.narrate("A fall in the return on government debt does not lengthen "
                          "anybody's working week."):
            self.play(FadeIn(yld), FadeIn(queue), FadeIn(ql), run_time=1.0)
            self.play(Indicate(yld[1], color=SRC_BR), run_time=1.0)
        still = Text("the queue does not move", font=FONT, font_size=T_BODY, color=MUTED)
        still.next_to(ql, DOWN, buff=0.3)
        with self.narrate("The yield falls. And the queue does not move."):
            self.play(FadeIn(still), run_time=1.0)
        self.beat()

        # ---------------------------------------------------- the three holes
        self.clear_stage()
        kit = stick.kit(scale=0.75).to_corner(DOWN + LEFT, buff=0.5)
        self.play(FadeIn(kit), kit.mood("thinking"), run_time=0.5)
        head3 = Text("And now the holes — Kit points at them himself",
                     font=FONT, font_size=T_SUB, color=SRC_KIT).to_edge(UP, buff=0.6)
        self.play(FadeIn(head3), run_time=0.5)

        holes = [
            ("scarce: TIME.  rationed by: MONEY.",
             "Here is the first hole. What is actually scarce, on his own account, is "
             "his managers' time. But the tool the company uses to ration it is a "
             "percentage return on money. Those are not the same thing at all. A large "
             "simple purchase can swallow a lot of money and very little management. A "
             "small fiddly reorganisation can do the reverse."),
            ("crude on purpose — or the wrong scarce thing?",
             "He thinks the crudeness is telling rather than damning. A rule a board "
             "can apply to proposals it cannot verify has to be simple, uniform and "
             "hard to argue with. But a critic could read exactly the same fact the "
             "other way, and conclude he has named the wrong scarce thing."),
            ("no observation tells it apart from “rules are slow”",
             "Second hole, and it is worse. He cannot name a single observation that "
             "would tell his version apart from a much simpler story. That any "
             "published rule is slow to change, whatever it was based on, because a "
             "number that moves every month stops being a rule and becomes something to "
             "argue about. On that story the threshold could be exactly what Dixit says "
             "it is, and still sit still for years."),
            ("cheaper money reshuffles the queue",
             "And a third. If the queue is ranked by how valuable each project is, then "
             "a fall in the cost of money lifts every project a bit, and reshuffles the "
             "order. So the next project in the queue is not quite independent of "
             "interest rates after all."),
        ]
        for text, say in holes:
            card = cards.body(text, size=T_BODY, color=CHALK, width=48)
            card.move_to(UP * 0.2)
            if card.height > 4.0:
                card.scale(4.0 / card.height)
            with self.narrate(say):
                self.play(FadeIn(card), run_time=1.0)
            self.beat(0.6)
            self.play(FadeOut(card), run_time=0.5)

        # ---------------------------------------------------- what he can defend
        self.clear_stage()
        defend = cards.body("It moves on the COMPANY's clock, not the BANK's.",
                            size=T_HEAD, color=SRC_KIT, width=34)
        defend.move_to(UP * 0.8)
        with self.narrate("So here is the version he can defend. Not that the number "
                          "never moves. But that it moves on the company's clock rather "
                          "than the central bank's."):
            self.play(Write(defend), run_time=2.8)
        self.beat()
        clock = cards.body("years, not months",
                           size=T_BODY, color=CHALK, width=44)
        clock.move_to(DOWN * 1.5)
        with self.narrate("Changing as the pipeline of ideas and the stock of managers "
                          "change, over years. For a policy meant to work inside a "
                          "downturn, that is close enough to failure to matter. But it "
                          "is not the same as never, and he will not say never."):
            self.play(FadeIn(clock), run_time=1.4)
        self.beat()

        self.clear_stage()
        attr = cards.body("the IDEA is not Kit's. The USE is.", size=T_SUB, color=SRC_KIT, width=40)
        with self.narrate("And the attribution, stated plainly. Treating a hurdle rate "
                          "as a rationing device rather than a calculation is not an "
                          "idea Kit invented. What he would claim is the use he has put "
                          "it to."):
            self.play(FadeIn(attr), run_time=1.4)
        self.beat()

        self.close_chapter([
            "Dixit's account: conceded",
            "what KIND of number, not how high",
            "it rations management, not money",
            "three holes, pointed at by him",
        ])
