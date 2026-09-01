import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.theme import *


class Chapter39(Chapter):
    CH = 39
    TITLE = "The evidence, read twice"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["ticket", "scale", "risk", "clock"]

    def body(self):
        pair = VGroup(
            stick.StickFigure("", CHALK, prop="printout", scale=0.75),
            stick.StickFigure("", CHALK, hat="specs", prop="book", scale=0.75),
        ).arrange(RIGHT, buff=0.6)
        plabel = Text("Martin & Milas (2012)", font=FONT, font_size=T_SMALL, color=SRC_MM)
        plabel.next_to(pair, DOWN, buff=0.25)
        grp = VGroup(pair, plabel).move_to(LEFT * 4.4 + UP * 1.4)
        with self.narrate("A third article, and a third pair of authors. Christopher "
                          "Martin and Costas Milas. Their job was to gather up the "
                          "studies of what the policy actually achieved. Their colour "
                          "is green."):
            self.play(FadeIn(grp), run_time=1.0)
        self.beat()

        lines = [
            ("increased GDP growth by around 1–3 per cent with a similar effect on "
             "inflation", MONEY),
            ("has proved effective in limiting the scale of the downturn", MONEY),
            ("QE, by itself, is not strong enough to spark an economic recovery", COST),
            ("Of course, this conclusion is tentative.", MUTED),
        ]
        says = ["It increased the country's rate of growth by around one to three per "
                "cent, with a similar effect on prices.",
                "It has proved effective in limiting the scale of the downturn.",
                "But, by itself, it is not strong enough to spark an economic recovery.",
                "And carry this last word, because it is theirs. Of course, this "
                "conclusion is tentative."]
        block = VGroup()
        for (t, c), s in zip(lines, says):
            card = cards.body("“" + t + "”", size=T_BODY, color=c, width=40)
            block.add(card)
        block.arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(RIGHT * 2.0 + UP * 0.2)
        bar = Line(block.get_top(), block.get_bottom(), color=SRC_MM, stroke_width=6)
        bar.next_to(block, LEFT, buff=0.35)
        self.play(Create(bar), run_time=0.5)
        for i, s in enumerate(says):
            with self.narrate(s):
                self.play(FadeIn(block[i], shift=RIGHT * 0.2), run_time=0.7)
        src = cards.note("Martin & Milas (2012), p. 762", width=40)
        src.next_to(block, DOWN, buff=0.4).align_to(block, LEFT)
        self.play(FadeIn(src), run_time=0.4)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------- the first reading
        kit = stick.kit(scale=0.95).move_to(LEFT * 4.4 + DOWN * 0.6)
        self.play(FadeIn(kit), run_time=0.5)
        first = cards.body("first reading: a result. Move on.",
                           size=T_SUB, color=MUTED, width=30)
        first.move_to(RIGHT * 1.8 + UP * 1.4)
        with self.narrate("The first time Kit read that, he treated it as a result. "
                          "Here is what the numbers say. Write it down, move on."):
            self.play(FadeIn(first), kit.mood("neutral"), run_time=0.9)
        self.beat()

        second = cards.body("second reading: he cannot let it alone",
                            size=T_SUB, color=SRC_KIT, width=30)
        second.move_to(RIGHT * 1.8 + DOWN * 0.2)
        with self.narrate("Reading it again, after Dixit, he cannot let it alone."):
            self.play(FadeIn(second), kit.mood("thinking"), run_time=0.9)

        qn = cards.body("Good at stopping a fall. Bad at starting a rise. Why?",
                        size=T_BODY, color=CHALK, width=30)
        qn.move_to(RIGHT * 1.8 + DOWN * 1.9)
        with self.narrate("Why would one policy be good at stopping a fall and bad at "
                          "starting a rise? Those are not obviously different jobs.",
                          v="c"):
            self.play(FadeIn(qn), run_time=1.0)
        self.beat()

        unc = cards.body("uncomfortable with himself",
                         size=T_BODY, color=SRC_KIT, width=40)
        unc.to_edge(DOWN, buff=0.62)
        with self.narrate("And he is uncomfortable. Not with the article — with "
                          "himself, for having read that sentence once already and "
                          "never asked whether there was a reason behind it."):
            self.play(FadeOut(first), FadeOut(second), FadeOut(qn), run_time=0.4)
            self.play(kit.mood("worried"), FadeIn(unc), run_time=1.0)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------- the two-row table
        head = cards.section_title("Two jobs, pulling on the same thing in opposite directions", color=CHALK, size=T_SUB)
        self.play(FadeIn(head), run_time=0.5)

        r1a = cards.body("PREVENTING A COLLAPSE", size=T_BODY, color=MONEY, width=20)
        r1b = cards.body("the UPSIDE held up\n(good news principle)\nstrongest when frightening", size=T_SMALL, color=CHALK, width=40)
        r2a = cards.body("STARTING A RECOVERY", size=T_BODY, color=COST, width=20)
        r2b = cards.body("the DOWNSIDE faced\n(bad news principle)\nstrongest when calm", size=T_SMALL, color=CHALK, width=40)
        col_a = VGroup(r1a, r2a).arrange(DOWN, buff=2.0, aligned_edge=LEFT)
        col_b = VGroup(r1b, r2b).arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        table = VGroup(col_a, col_b).arrange(RIGHT, buff=0.9, aligned_edge=UP)
        table.move_to(DOWN * 0.3)
        if table.height > 4.6:
            table.scale(4.6 / table.height)
        rule = Line(table.get_left(), table.get_right(), color=MUTED, stroke_width=2)
        rule.move_to(table.get_center())

        with self.narrate("Preventing a collapse needs markets that keep working and "
                          "the upside held up. And by the good news principle, that is "
                          "exactly what stops a struggling firm closing. It is "
                          "strongest when things are frightening, because there is most "
                          "to repair and most upside to restore."):
            self.play(FadeIn(r1a), run_time=0.6)
            self.play(FadeIn(r1b), run_time=1.0)
        self.play(Create(rule), run_time=0.5)
        with self.narrate("Starting a recovery needs firms to commit money they cannot "
                          "get back. By the bad news principle, that turns on the "
                          "downside — which is exactly what fear makes them least "
                          "willing to face. It is strongest when things are calm."):
            self.play(FadeIn(r2a), run_time=0.6)
            self.play(FadeIn(r2b), run_time=1.0)
        self.beat()

        self.clear_stage()
        land = cards.body("used where job one is easiest and job two hardest",
                          size=T_SUB, color=CHALK, width=34)
        land.move_to(UP * 0.9)
        with self.narrate("So the policy is used in exactly the state where the first "
                          "job is easiest and the second is hardest."):
            self.play(FadeIn(land), run_time=1.0)
        self.beat()
        steady = cards.body("It steadies without starting.", size=T_HEAD,
                            color=SRC_KIT, width=26)
        steady.move_to(DOWN * 0.9)
        with self.narrate("It steadies without starting."):
            self.play(Write(steady), run_time=1.8)
        self.beat()

        # ------------------------------------------------- whose is whose
        self.clear_stage()
        flag = cards.body("KIT'S, not Dixit's:\n\n· “best when frightening”\n\n· “the jobs pull apart”",
                          size=T_BODY, color=SRC_KIT, width=44)
        with self.narrate("And flag clearly which parts of that are Kit's and not "
                          "Dixit's. That propping up the upside works best when things "
                          "are frightening, and that the two jobs therefore pull apart, "
                          "are steps Kit has added. Dixit's own text does not contain "
                          "them."):
            self.play(FadeIn(flag), run_time=1.6)
        self.beat()

        self.close_chapter([
            "1–3% growth · downturn limited",
            "not enough to spark a recovery — tentative",
            "the two jobs pull opposite ways",
            "it steadies without starting",
        ])
