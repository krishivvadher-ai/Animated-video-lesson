import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.theme import *


class Chapter34(Chapter):
    CH = 34
    TITLE = "The exception on page 613"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["bank", "clock", "people", "fog"]

    def body(self):
        kit = stick.kit(scale=0.85).move_to(LEFT * 5.2 + DOWN * 1.6)
        self.play(FadeIn(kit), run_time=0.5)

        with self.narrate("A page later, the authors ask a question about somebody "
                          "else. What does the government do when its own borrowing "
                          "gets cheaper?"):
            pass

        gov_fig = stick.StickFigure("the government", CHALK, hat="collar", scale=0.85)
        gov_fig.move_to(RIGHT * 3.4 + UP * 0.4)
        gl = gov_fig.label()
        first = cards.body("and its borrowing IS cheaper — gilts are what was bought",
                           size=T_BODY, color=SRC_BR, width=26)
        first.move_to(LEFT * 1.6 + UP * 1.6)
        with self.narrate("And notice what they open with. The government's borrowing "
                          "cost is now lower. Gilts are exactly what the Bank had been "
                          "buying. So if anyone got the cheaper price, the government "
                          "did."):
            self.play(FadeIn(gov_fig), FadeIn(gl), run_time=0.7)
            self.play(FadeIn(first), run_time=0.9)

        bag = W.money_bag(MONEY, 0.8).move_to(RIGHT * 0.2 + DOWN * 1.2)
        arr = W.flow_arrow(bag.get_right() + RIGHT * 0.2,
                           gov_fig.get_left() + LEFT * 0.3 + DOWN * 0.6, MONEY)
        with self.narrate("The money definitely arrives."):
            self.play(FadeIn(bag), run_time=0.5)
            self.play(Create(arr), run_time=0.9)
        self.beat()
        nothing = Text("and nothing happens", font=FONT, font_size=T_SUB, color=MUTED)
        nothing.next_to(gov_fig, DOWN, buff=1.1)
        with self.narrate("And nothing happens."):
            self.play(FadeIn(nothing), run_time=0.9)
            self.play(gov_fig.mood("neutral"), run_time=0.4)
        self.beat()

        self.play(FadeOut(first), FadeOut(nothing), FadeOut(bag), FadeOut(arr),
                  FadeOut(gov_fig), FadeOut(gl), run_time=0.6)

        q = cards.quote_card(
            "Their spending plans should therefore be unaffected by cyclical movements "
            "in interest rates.", "Bowdler & Radia (2012), p. 613", SRC_BR, width=40)
        q.move_to(UP * 1.4)
        if q.width > 11.4:
            q.scale(11.4 / q.width)
        with self.narrate("Here is what the authors say, in their own words. Their "
                          "spending plans should therefore be unaffected by cyclical "
                          "movements in interest rates."):
            self.play(FadeIn(q), run_time=1.2)
        self.beat()
        reason = cards.body("not access — the HORIZON of the decision", size=T_SUB, color=SRC_KIT, width=40)
        reason.move_to(DOWN * 1.2)
        with self.narrate("And look at the reason. It has nothing to do with access. "
                          "The money arrives. The reason is about the horizon the "
                          "decision is taken over. Governments plan a long way ahead."):
            self.play(FadeIn(reason), run_time=1.1)
        self.beat()

        # ---------------------------------------------------- Kit gets excited
        with self.narrate("Kit gets excited. Animate the excitement, because there is "
                          "about to be a correction and you need to have seen the "
                          "before."):
            self.play(kit.mood("surprised"), run_time=0.4)
            b = kit.say("A feature of the DECISION\nbreaks the link!", direction=UP,
                        width=3.8, color=SRC_KIT)
            self.play(FadeIn(b), run_time=0.6)
            self.play(kit.pace(2, run_time=2.0))
        self.beat()
        self.play(FadeOut(b), FadeOut(q), FadeOut(reason), run_time=0.6)

        # ---------------------------------------------------- and talks himself down
        head = cards.section_title("And then he reads it again", color=CHALK, size=T_SUB)
        self.play(FadeIn(head), kit.mood("thinking"), run_time=0.6)

        steps = cards.bullet_list([
            "“Cyclical” means short-term and temporary.",
            "long planners ignore passing changes",
            "an ordinary point about budgeting",
        ], color=CHALK, width=40, dotc=COST)
        steps.move_to(RIGHT * 1.2 + UP * 0.4)
        says = ["Cyclical means short-term and temporary.",
                "And economists have a standard idea that a long-term planner responds "
                "to lasting changes and ignores passing ones.",
                "So this is very likely an ordinary technical point about how "
                "governments budget. Not a claim about how organisations behave at all."]
        for i in range(3):
            with self.narrate(says[i]):
                self.play(FadeIn(steps[i], shift=RIGHT * 0.2), run_time=0.6)
        self.beat()

        cross = Line(steps.get_left() + LEFT * 0.2, steps.get_right() + RIGHT * 0.2,
                     color=COST, stroke_width=5)
        with self.narrate("So Kit crosses his own conclusion out. That is the first of "
                          "several times he will do that, and they are the best moments "
                          "in this half of the film."):
            self.play(Create(cross), kit.mood("worried"), run_time=1.2)
        self.beat()

        # ---------------------------------------------------- what survives
        self.clear_stage()
        head2 = cards.section_title("What survives is thinner", color=SRC_KIT, size=T_SUB)
        self.play(FadeIn(head2), run_time=0.5)

        surv = cards.body("the decision itself breaks the link — once",
                          size=T_BODY, color=CHALK, width=44)
        surv.move_to(UP * 0.9)
        with self.narrate("What survives is this, and it is thinner than he first "
                          "thought. A feature of the decision itself is allowed, once, "
                          "to break the link between a cheaper price and more spending. "
                          "And nobody then asks whether anything else about how a "
                          "decision gets made could do the same."):
            self.play(FadeIn(surv), run_time=1.4)
        self.beat()

        std = cards.body("A reason to look. Not evidence.", size=T_HEAD, color=SRC_KIT, width=30)
        std.move_to(DOWN * 1.6)
        with self.narrate("That is a reason to go and look. It is not evidence about "
                          "what you find."):
            self.play(Write(std), run_time=2.2)
        self.beat()
        note = cards.note("the standard for everything that follows",
                          width=56)
        note.to_edge(DOWN, buff=0.62)
        with self.narrate("That sentence is the intellectual standard the rest of the "
                          "film is held to. Everything Kit says from here has to meet it."):
            self.play(FadeIn(note), run_time=0.9)
        self.beat()

        self.close_chapter([
            "the government DOES get the cheaper price",
            "and its plans should not change",
            "the reason is the horizon, not access",
            "“cyclical” ⇒ a reason to look, not evidence",
        ])
