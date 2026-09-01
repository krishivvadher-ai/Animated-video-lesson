import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter40(Chapter):
    CH = 40
    TITLE = "The exception on page 613"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["money", "clock", "door", "scale"]

    def body(self):
        # ------------------------------------------------ the question
        self.heading("A page later, they ask about somebody else")
        gov = W.building(SRC_BR, size=0.75, kind="government")
        St.place(gov, St.STAGE, ax=-0.5, ay=0.0)
        with self.narrate("A page later, the authors ask a question about somebody "
                          "else. What does the government do when its own borrowing "
                          "gets cheaper?"):
            self.play(Create(gov), run_time=1.2)

        note = St.caption("gilts are exactly what was bought", SRC_BR, T_BODY, width=22)
        St.place(note, St.SIDE, ay=0.55)
        with self.narrate("And notice what they open with. The government's borrowing "
                          "cost is now lower. Gilts are exactly what the Bank had been "
                          "buying. So if anyone got the cheaper price, the government "
                          "did."):
            self.play(FadeIn(note), run_time=0.9)

        arrive = W.flow_arrow(St.SIDE.point(-0.9, -0.3), gov.get_right() + RIGHT * 0.25,
                              MONEY)
        cheap = Text("cheaper money", font=FONT, font_size=T_SMALL, color=MONEY)
        cheap.next_to(arrive, DOWN, buff=0.2)
        with self.narrate("The money definitely arrives."):
            self.play(Create(arrive), FadeIn(cheap), run_time=0.8)
            self.play(S.flow_along(arrive, MONEY))
        self.beat()

        nothing = St.caption("and nothing happens", COST, T_HEAD, width=24)
        St.place(nothing, St.FOOT, pad=0.06)
        with self.narrate("And nothing happens."):
            self.play(FadeIn(nothing), run_time=1.0)
        self.wait(1.6)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ their words
        self.heading("Their words for why")
        q = cards.quote_card("Their spending plans should therefore be unaffected by "
                             "cyclical movements in interest rates.",
                             "Bowdler & Radia, p. 613", SRC_BR)
        St.place(q, St.FULL, ay=0.35)
        with self.narrate("Here is what the authors say, in their own words. Their "
                          "spending plans should therefore be unaffected by cyclical "
                          "movements in interest rates."):
            self.play(FadeIn(q), run_time=1.6)
        self.wait(1.8)

        why = VGroup(
            VGroup(cards.icon("door", MUTED, 1.4),
                   St.caption("not about access", MUTED, T_SMALL, width=16)
                   ).arrange(DOWN, buff=0.25),
            VGroup(cards.icon("clock", TRIGGER, 1.4),
                   St.caption("about the horizon", TRIGGER, T_SMALL, width=16)
                   ).arrange(DOWN, buff=0.25),
        ).arrange(RIGHT, buff=2.4)
        St.place(why, St.FULL, ay=-0.75)
        with self.narrate("And look at the reason. It has nothing to do with access. "
                          "The money arrives."):
            self.play(FadeIn(why[0]), run_time=0.8)
            x = Cross(why[0][0], stroke_color=COST, stroke_width=5).scale(0.6)
            self.play(Create(x), run_time=0.6)
        with self.narrate("The reason is about the horizon the decision is taken over. "
                          "Governments plan a long way ahead."):
            self.play(FadeIn(why[1]), run_time=0.8)
            self.play(S.flash_around(why[1], TRIGGER))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ Kit's overreach
        self.heading("Kit gets ahead of himself")
        kit = stick.kit(scale=0.95)
        St.place(kit, St.STAGE, ax=-0.65, ay=-0.35)
        self.play(FadeIn(kit), run_time=0.6)
        claim = St.caption("so they admit my whole point!", SRC_KIT, T_SUB, width=24)
        St.place(claim, St.SIDE, ay=0.4)
        with self.narrate("Kit gets excited. They have admitted, he says, that a feature "
                          "of how the decision is made can break the whole chain.",
                          v="c"):
            self.play(kit.mood("happy"), run_time=0.4)
            self.play(FadeIn(claim), run_time=0.8)
            self.play(kit.pace(1, run_time=1.6))
        self.beat()

        with self.narrate("And then he reads it again, and crosses his own conclusion "
                          "out. That is the first of several times he will do that.",
                          v="c"):
            strike = Line(claim.get_left(), claim.get_right(), color=COST,
                          stroke_width=5)
            self.play(Create(strike), run_time=0.9)
            self.play(kit.mood("worried"), run_time=0.4)
        self.beat()
        self.play(FadeOut(claim), FadeOut(strike), run_time=0.5)

        survives = St.points(["one feature of a decision",
                              "breaks the link, once",
                              "and nobody asks what else could"],
                             colour=CHALK, dot_colour=SRC_KIT, size=T_BODY, width=22)
        St.place(survives, St.SIDE, ay=0.0)
        says = ["What survives is this, and it is thinner than he first thought. A "
                "feature of the decision itself is allowed, once,",
                "to break the link between a cheaper price and more spending.",
                "And nobody then asks whether anything else about how a decision gets "
                "made could do the same."]
        for i, row in enumerate(survives):
            with self.narrate(says[i]):
                self.play(FadeIn(row), run_time=0.7)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the standard
        self.drop_heading()
        std = St.caption("a reason to go and look —\nnot evidence about what you find",
                         CHALK, T_HEAD, width=34)
        St.place(std, St.WIDE, ay=0.25)
        with self.narrate("That is a reason to go and look. It is not evidence about "
                          "what you find."):
            self.play(Write(std), run_time=2.6)
        self.wait(2.2)
        under = St.caption("everything Kit says has to meet that", SRC_KIT,
                           T_SUB, width=38)
        St.place(under, St.FOOT, pad=0.06)
        with self.narrate("That sentence is the intellectual standard the rest of the "
                          "film is held to. Everything Kit says from here has to meet "
                          "it."):
            self.play(FadeIn(under), run_time=0.9)
            self.play(S.flash_around(under, SRC_KIT, run_time=2.0))
        self.beat()

        self.close_chapter([
            "the government gets the cheaper money for certain",
            "and its plans are unaffected — their words",
            "the reason is the horizon, not access",
            "which is a reason to look, not a finding",
        ])
