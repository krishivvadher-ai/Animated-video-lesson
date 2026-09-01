import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter20(Chapter):
    CH = 20
    TITLE = "Outside business"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["slab", "door", "signal"]

    def body(self):
        # ------------------------------------------------ the three features
        self.heading("The same three features, elsewhere")
        icons = VGroup(
            VGroup(cards.icon("slab", SUNK, 2.0),
                   St.caption("costly to reverse", SUNK, T_SMALL, width=14)),
            VGroup(cards.icon("fog", WAIT, 2.0),
                   St.caption("made under uncertainty", WAIT, T_SMALL, width=14)),
            VGroup(cards.icon("clock", MONEY, 2.0),
                   St.caption("the timing is yours", MONEY, T_SMALL, width=14)),
        )
        for g in icons:
            g.arrange(DOWN, buff=0.4)
        icons.arrange(RIGHT, buff=1.7)
        St.place(icons, St.FULL, ay=0.35)
        with self.narrate("The paper closes with an observation that reaches well "
                          "outside business. Many personal, social and political "
                          "decisions have exactly the same three features. Costly to "
                          "reverse. Made under uncertainty. And the timing is yours to "
                          "choose."):
            self.play(S.lag_map(FadeIn, icons, shift=UP * 0.3, lag=0.25),
                      run_time=2.0)
        with self.narrate("So the same inertia applies to them too."):
            self.foot("so the same inertia applies", CHALK)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the two flats
        self.heading("An example told against economists")
        man = stick.StickFigure("an economist", CHALK, hat="specs", prop="book",
                                scale=0.9)
        St.place(man, St.STAGE, ax=-0.55, ay=-0.2)
        her = stick.StickFigure("his partner", CHALK, hair=True, scale=0.9)
        St.place(her, St.SIDE, ax=0.0, ay=-0.2)
        f1 = W.building(MUTED, 0.42, "house")
        f2 = W.building(MUTED, 0.42, "house")
        flats = VGroup(f1, f2).arrange(RIGHT, buff=2.6)
        St.place(flats, St.FULL, ay=0.72)
        fl = Text("two rent-controlled flats", font=FONT, font_size=T_SMALL, color=MUTED)
        fl.next_to(flats, DOWN, buff=0.25)
        with self.narrate("A man and his partner, in New York, each with a "
                          "rent-controlled flat. Their relationship reaches the point "
                          "where she suggests they give one of them up."):
            self.play(FadeIn(man), FadeIn(her), run_time=0.9)
            self.play(Create(flats), FadeIn(fl), run_time=1.0)

        b1 = her.say("Let's give one up.", direction=UP, width=3.0)
        with self.narrate("Let us give one of them up.", v="c"):
            self.play(FadeIn(b1), run_time=0.6)
            self.play(FadeOut(b1), run_time=0.35)
        b2 = man.say("Given a positive\nprobability…", direction=UP, width=3.2)
        with self.narrate("And he explains to her, at length, the importance of keeping "
                          "options alive. It is unlikely they would split up, he says, "
                          "but given a positive probability, and so on."):
            self.play(FadeIn(b2), man.mood("pleased"), run_time=0.8)
        self.beat()
        with self.narrate("She took it very badly, and ended the relationship."):
            self.play(FadeOut(b2), her.mood("worried"), run_time=0.6)
            self.play(her.walk_to(St.SIDE.point(1.6, -0.2), run_time=1.8))
            self.play(FadeOut(her), man.mood("surprised"), run_time=0.6)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the resolution
        self.heading("And the resolution is the instructive part")
        wrong = St.caption("not a decision under uncertainty —\na signalling game",
                           COST, T_SUB, width=34)
        St.place(wrong, St.FULL, ay=0.6)
        with self.narrate("Financial economists who hear that story say it proves how "
                          "right he was. The paper says something better. He had "
                          "misread the situation entirely. It was not a decision "
                          "problem under uncertainty at all."):
            self.play(FadeIn(wrong), run_time=1.1)
        self.beat()
        self.define("signalling", "Doing something costly, because the cost is what "
                    "makes it believable.", "signal", MONEY, at=DOWN * 0.9, hold=5.0)

        expl = St.points(["she was unsure how much he valued her",
                          "the costly, irreversible step WAS the message",
                          "he sat on the fence, and fell off"],
                         colour=CHALK, dot_colour=MONEY, size=T_BODY, width=34)
        St.place(expl, St.FULL, ay=-0.15)
        says = ["She was unsure how much he valued her.",
                "And it was precisely his willingness to take the costly, irreversible "
                "step of giving up the flat that would have carried the message. "
                "Anyone can say it. Only someone who means it will pay for it.",
                "He tried to sit on the fence, and fell off it."]
        for i, row in enumerate(expl):
            with self.narrate(says[i]):
                self.play(FadeIn(row), run_time=0.8)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the point
        self.drop_heading()
        point = St.caption("sometimes the irreversibility\nIS the message", CHALK,
                           T_HEAD, width=30)
        St.place(point, St.WIDE, ay=0.15)
        with self.narrate("And that gives the chapter a real point rather than a joke. "
                          "It shows a limit of the whole framework. Option value is not "
                          "always the right lens. Sometimes the irreversibility is the "
                          "message."):
            self.play(Write(point), run_time=2.4)
            self.play(S.flash_around(point, TRIGGER, run_time=2.0))
        self.beat()

        self.close_chapter([
            "the same three features appear elsewhere",
            "keeping the option open can be the wrong move",
            "signalling: the cost is the message",
        ])
