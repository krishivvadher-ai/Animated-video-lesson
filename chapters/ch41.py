import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.theme import *


class Chapter41(Chapter):
    CH = 41
    TITLE = "The rivals Kit cannot beat"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["door", "clock", "people", "fog"]

    def door_scene(self, n, title, colour, points, spoken, kit):
        d = W.door(colour, 1.5, 3.0, None).move_to(LEFT * 5.0 + UP * 0.2)
        num = Text(f"Door {n}", font=FONT, font_size=T_SMALL, color=colour)
        num.next_to(d, DOWN, buff=0.3)
        head = cards.body(title, size=T_SUB, color=colour, width=34)
        head.to_edge(UP, buff=0.6)
        self.play(Create(d), FadeIn(num), FadeIn(head), run_time=0.9)
        rows = cards.bullet_list(points, color=CHALK, width=40, dotc=colour)
        rows.move_to(RIGHT * 1.4 + DOWN * 0.2)
        if rows.height > 4.2:
            rows.scale(4.2 / rows.height)
            rows.move_to(RIGHT * 1.4 + DOWN * 0.2)
        for i, s in enumerate(spoken):
            with self.narrate(s):
                self.play(FadeIn(rows[i], shift=RIGHT * 0.2), run_time=0.6)
        self.beat()
        left_open = Text("still open", font=FONT, font_size=T_SMALL, color=colour)
        left_open.next_to(num, DOWN, buff=0.3)
        self.play(FadeIn(left_open), run_time=0.5)
        self.wait(0.6)
        self.play(FadeOut(VGroup(d, num, head, rows, left_open)), run_time=0.6)

    def body(self):
        kit = stick.kit(scale=0.7).to_corner(DOWN + RIGHT, buff=0.62)
        self.play(FadeIn(kit), run_time=0.5)
        with self.narrate("Four doors. Kit opens each one, and cannot close it again. "
                          "This is the chapter where the film earns its credibility, so "
                          "none of these gets knocked down."):
            pass

        self.door_scene(
            1, "It is just a small dose.", SRC_MM,
            ["200–300 basis points, first round",
             "Later programmes did little.",
             "enough to cushion, not to reverse",
             "differs in principle · untestable in practice"],
            ["Martin and Milas have their own explanation. The very large initial "
             "programmes had effects comparable to a cut in the policy rate of two to "
             "three hundred basis points — that is, two to three percentage points.",
             "And later programmes did very little.",
             "A dose that size might well be enough to cushion a fall and not enough to "
             "reverse one. That is a complete answer, and it needs nothing at all from "
             "Dixit.",
             "Kit's account does differ in principle. His says the same dose would work "
             "better in calm conditions. But he cannot test that difference, because "
             "the policy is only ever used in a crisis. So the two are rivals in "
             "principle, and cannot be told apart in practice."],
            kit)

        self.door_scene(
            2, "Firms thought it was temporary.", SRC_BR,
            ["from Kit's own hinge quotation",
             "firms read it as temporary",
             "nobody rebuilds around a rate they think will go",
             "inside the authors' own framework"],
            ["Door two is the strongest objection against him, and it comes straight "
             "out of his own hinge quotation.",
             "If a long-horizon planner ignores a change because the change is "
             "temporary, then the simplest explanation of why firms did not respond is "
             "that they read the policy as temporary too.",
             "Rates were pushed down. Everybody expected them to be pushed back up. And "
             "nobody rebuilds a factory around a rate they do not expect to last.",
             "It needs nothing from Dixit and nothing from management. It sits entirely "
             "inside the original article's own framework."],
            kit)

        # Kit's three replies, and none of them is a refutation
        head = cards.section_title("Kit has three things to say, and none is a refutation", color=SRC_KIT, size=T_SUB)
        self.play(FadeIn(head), run_time=0.5)
        rep = cards.bullet_list([
            "not exclusive",
            "different predictions",
            "Dixit STRENGTHENS the rival",
        ], color=CHALK, width=42, dotc=SRC_KIT)
        rep.move_to(DOWN * 0.2)
        says = ["The two stories are not exclusive. A change that looked permanent "
                "would still meet a gate inside the firm.",
                "They predict different things. The temporary story says firms would "
                "respond fully to a change they believed would last.",
                "And Dixit's reasoning actually strengthens the temporary story rather "
                "than competing with it — because a change you think might not last is "
                "precisely what makes waiting attractive."]
        for i in range(3):
            with self.narrate(says[i]):
                self.play(FadeIn(rep[i], shift=RIGHT * 0.2), run_time=0.7)
        self.beat()
        unsettled = cards.body("unsettled",
                               size=T_SUB, color=SRC_KIT, width=40)
        unsettled.to_edge(DOWN, buff=0.62)
        with self.narrate("Which of the two does more of the work is a question this "
                          "argument does not settle."):
            self.play(FadeIn(unsettled), run_time=0.9)
        self.beat()
        self.play(FadeOut(head), FadeOut(rep), FadeOut(unsettled), run_time=0.6)

        self.door_scene(
            3, "Most of this does not apply.", SRC_MM,
            ["no effect on SME and household rates",
             "unsecured rates ROSE in 2008–9",
             "the money never arrived",
             "scope: large firms only"],
            ["Door three shrinks him. Martin and Milas report that the policy does not "
             "appear to have affected the rates facing small and medium-sized companies "
             "and households at all.",
             "For borrowing with nothing pledged against it — no property, no equipment "
             "a lender can take — rates actually rose in two thousand and eight and "
             "two thousand and nine. Lenders raised their charge for risky borrowers "
             "faster than the policy rate came down.",
             "For those borrowers the money never arrived, and the original article's "
             "own qualification covers them completely. There is nothing left for Kit "
             "to explain.",
             "So his argument is scoped, honestly, to large firms that did see the "
             "cheaper price — which is, as it happens, where the rest of it is "
             "strongest anyway."],
            kit)

        self.door_scene(
            4, "How good is the evidence?", SRC_MM,
            ["limited · similar methods · mostly central banks",
             "the 1–3% he is explaining comes from it",
             "and they call it tentative",
             "softer ground than he assumed"],
            ["Door four is about the floor under all of it. Martin and Milas warn, in "
             "their own abstract, that the literature is limited, relies on similar "
             "methods, and largely originates in central banks — which are not neutral "
             "parties.",
             "The one to three per cent figure that Kit is treating as a fact to be "
             "explained comes largely from that research.",
             "And the authors call their own conclusion tentative.",
             "So the ground he is standing on is softer than he assumed it was."],
            kit)

        # ---------------------------------------------------- Dixit's own limit
        head2 = cards.section_title("And one more limit — this one is Dixit's own", color=SRC_DX, size=T_SUB)
        self.play(FadeIn(head2), run_time=0.5)
        nell = stick.nell(scale=0.85).move_to(LEFT * 3.4 + DOWN * 0.6)
        d = W.door(MONEY, 1.2, 2.4, "one site, one licence").move_to(RIGHT * 1.0 + DOWN * 0.2)
        rival = stick.StickFigure("a rival", CHALK, scale=0.85).move_to(RIGHT * 5.4 + DOWN * 0.6)
        with self.narrate("If several firms are racing for the same opportunity, "
                          "waiting is not possible, and the textbook is right after all."):
            self.play(FadeIn(nell), Create(d), FadeIn(rival), run_time=0.9)
            self.play(rival.walk_to(RIGHT * 1.0 + DOWN * 0.6, run_time=1.8))
        scope = cards.body("not a race",
                           size=T_SUB, color=CHALK, width=40)
        scope.to_edge(DOWN, buff=0.62)
        with self.narrate("The argument applies to investment a company can take its "
                          "time over. Not to a race."):
            self.play(FadeIn(scope), run_time=0.9)
        self.beat()

        self.close_chapter([
            "a small dose explains it too",
            "“they thought it temporary” — unrefuted",
            "small firms never got the price",
            "and the evidence itself is thin",
        ])
