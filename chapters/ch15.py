import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.theme import *


class Chapter15(Chapter):
    CH = 15
    TITLE = "Outside business"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ['slab', 'door', 'signal']

    def body(self):
        three = VGroup(
            VGroup(cards.icon("slab", SUNK, 1.5),
                   cards.body("costly to reverse", size=T_SMALL, color=SUNK, width=16)),
            VGroup(cards.icon("fog", WAIT, 1.5),
                   cards.body("made under uncertainty", size=T_SMALL, color=WAIT, width=16)),
            VGroup(cards.icon("clock", MONEY, 1.5),
                   cards.body("the timing is a choice", size=T_SMALL, color=MONEY, width=16)),
        )
        for g in three:
            g.arrange(DOWN, buff=0.35)
        three.arrange(RIGHT, buff=1.6).shift(UP * 1.4)

        with self.narrate("The paper closes with an observation that reaches well "
                          "outside business. Many personal, social and political "
                          "decisions have exactly the same three features."):
            self.play(FadeIn(three), run_time=1.2)
        with self.narrate("Costly to reverse. Made under uncertainty. And the timing is "
                          "yours to choose. So the same inertia applies to them too."):
            pass
        self.beat()
        self.play(FadeOut(three), run_time=0.5)

        # ------------------------------------------------------- the two flats
        head = Text("An example the paper tells against economists",
                    font=FONT, font_size=T_SUB, color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)

        man = stick.StickFigure("an economist", CHALK, hat="specs", prop="book", scale=0.95)
        man.shift(LEFT * 3.6 + DOWN * 0.8)
        her = stick.StickFigure("his partner", CHALK, hair=True, scale=0.95)
        her.shift(RIGHT * 3.6 + DOWN * 0.8)
        f1 = W.factory(MUTED, 0.4).move_to(LEFT * 5.6 + UP * 1.6)
        f2 = W.factory(MUTED, 0.4).move_to(RIGHT * 5.6 + UP * 1.6)
        fl = Text("two rent-controlled flats", font=FONT, font_size=T_SMALL, color=MUTED)
        fl.move_to(UP * 1.6)

        with self.narrate("A man and his partner, in New York, each with a "
                          "rent-controlled flat. Their relationship reaches the point "
                          "where she suggests they give one of them up."):
            self.play(FadeIn(man), FadeIn(her), run_time=0.8)
            self.play(FadeIn(f1), FadeIn(f2), FadeIn(fl), run_time=0.8)

        b1 = her.say("Let's give one up.", direction=UP, width=3.0)
        with self.narrate("Let us give one of them up.", v="c"):
            self.play(FadeIn(b1), run_time=0.6)
        self.play(FadeOut(b1), run_time=0.3)

        b2 = man.say("It's unlikely we'd split up.\nBut given a positive\nprobability…",
                     direction=UP, width=3.6)
        with self.narrate("And he explains to her, at length, the importance of keeping "
                          "options alive. It is unlikely they would split up, he says, "
                          "but given a positive probability, and so on."):
            self.play(FadeIn(b2), man.mood("pleased"), run_time=0.8)
        self.beat()
        with self.narrate("She took it very badly, and ended the relationship."):
            self.play(FadeOut(b2), her.mood("worried"), run_time=0.6)
            self.play(her.walk_to(RIGHT * 6.4 + DOWN * 0.8, run_time=1.8))
            self.play(FadeOut(her), man.mood("surprised"), run_time=0.6)
        self.beat()

        # ------------------------------------------------------- the resolution
        self.clear_stage()
        head2 = Text("And the paper's resolution is the instructive part",
                     font=FONT, font_size=T_SUB, color=CHALK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head2), run_time=0.5)

        wrong = cards.body("not a decision problem — a signalling game", size=T_SUB, color=COST, width=40)
        wrong.move_to(UP * 1.4)
        with self.narrate("Financial economists who hear that story say it proves how "
                          "right he was. The paper says something better. He had misread "
                          "the situation entirely. It was not a decision problem under "
                          "uncertainty at all."):
            self.play(FadeIn(wrong), run_time=1.0)
        self.beat()

        self.define("signalling", "Costly, and that is what makes it believable.", "signal", MONEY,
                    narration="It was a signalling game. And signalling is a genuinely "
                              "useful idea, so here is the definition. Doing something "
                              "costly, because the cost is what makes it believable.",
                    at=DOWN * 0.6, hold=5.0)

        expl = cards.body("the costly, irreversible step WAS the message",
                          size=T_BODY, color=CHALK, width=42)
        expl.move_to(DOWN * 0.4)
        with self.narrate("She was unsure how much he valued her. And it was precisely "
                          "his willingness to take the costly, irreversible step of "
                          "giving up the flat that would have carried the message. "
                          "Anyone can say it. Only someone who means it will pay for it."):
            self.play(FadeIn(expl), run_time=1.2)
        self.beat()
        fence = cards.body("He sat on the fence, and fell off.",
                           size=T_SUB, color=CHALK, width=34)
        fence.next_to(expl, DOWN, buff=0.7)
        with self.narrate("He tried to sit on the fence, and fell off it."):
            self.play(FadeIn(fence), run_time=0.8)
        self.beat()

        self.clear_stage()
        point = cards.body("sometimes the irreversibility IS the message", size=T_SUB, color=CHALK, width=34)
        with self.narrate("And that gives the chapter a real point rather than a joke. "
                          "It shows a limit of the whole framework. Option value is not "
                          "always the right lens. Sometimes the irreversibility is the "
                          "message."):
            self.play(FadeIn(point), run_time=1.2)
        self.beat()

        self.close_chapter([
            "the same three features appear elsewhere",
            "keeping the option open can be the wrong move",
            "signalling: the cost is the message",
        ])
