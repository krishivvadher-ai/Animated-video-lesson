import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter39(Chapter):
    CH = 39
    TITLE = "The evidence, read twice"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["people", "scale", "fog", "signal"]

    def body(self):
        # ------------------------------------------------ the third pair
        self.heading("A third article, a third pair")
        pair = VGroup(stick.StickFigure("Martin", SRC_MM, scale=0.8),
                      stick.StickFigure("Milas", SRC_MM, scale=0.8)
                      ).arrange(RIGHT, buff=2.2)
        St.place(pair, St.STAGE, ay=-0.3)
        with self.narrate("A third article, and a third pair of authors. Christopher "
                          "Martin and Costas Milas. Their job was to gather up the "
                          "studies of what the policy actually achieved. Their colour "
                          "is green."):
            self.play(FadeIn(pair[0]), FadeIn(pair[0].label()), run_time=0.7)
            self.play(FadeIn(pair[1]), FadeIn(pair[1].label()), run_time=0.7)
        self.clear_stage()

        # ------------------------------------------------ what the studies found
        self.heading("What the studies actually found")
        ax = Axes(x_range=[0, 4, 1], y_range=[0, 4, 1], x_length=5.2, y_length=2.8,
                  axis_config=AXIS)
        St.place(ax, St.STAGE, ay=0.1, fill=False)
        yl = Text("extra GDP growth", font=FONT, font_size=T_TINY, color=SRC_MM)
        yl.next_to(ax, UP, buff=0.16)
        band = Rectangle(width=ax.x_length * 0.86, height=0.62, color=SRC_MM,
                         stroke_width=3, fill_color=SRC_MM, fill_opacity=0.22)
        band.move_to(ax.c2p(2.0, 2.0))
        lo = Text("1%", font=FONT, font_size=T_SMALL, color=SRC_MM)
        lo.next_to(band, LEFT, buff=0.2)
        hi = Text("3%", font=FONT, font_size=T_SMALL, color=SRC_MM)
        hi.next_to(band, RIGHT, buff=0.2)
        with self.narrate("Across the studies they gathered, quantitative easing raised "
                          "growth by somewhere between one and three per cent, with a "
                          "similar effect on inflation."):
            self.play(Create(ax), FadeIn(yl), run_time=1.0)
            self.play(GrowFromCenter(band), run_time=1.0)
            self.play(FadeIn(lo), FadeIn(hi), run_time=0.6)
            self.play(S.indicate(band, SRC_MM))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the verdict, verbatim
        self.heading("Their verdict, in their own words")
        q = cards.quote_card("QE has proved effective in limiting the scale of the "
                             "downturn. However, QE, by itself, is not strong enough "
                             "to spark an economic recovery.",
                             "Martin & Milas (2012)", SRC_MM)
        St.place(q, St.FULL, ay=0.55, fill=False)
        with self.narrate("And here is their verdict, in their own words. Quantitative "
                          "easing has proved effective in limiting the scale of the "
                          "downturn. However, by itself, it is not strong enough to "
                          "spark an economic recovery."):
            self.play(FadeIn(q), run_time=1.8)
        self.wait(1.6)
        hedge = St.caption("their own word: tentative", SUNK, T_SUB, width=28)
        St.place(hedge, St.FULL, ay=-0.65)
        with self.narrate("And they hedge it themselves. This conclusion, they say, is "
                          "tentative. There is relatively little evidence, and most of "
                          "it uses the same method."):
            self.play(FadeIn(hedge), run_time=0.9)
        self.beat()
        self.clear_stage()

        self.heading("Their verdict, in one line")
        verdict = St.caption("prevents a crisis — less good\nat starting a recovery",
                             SRC_MM, T_SUB, width=32)
        St.place(verdict, St.FULL, ay=0.6)
        with self.narrate("In one line: effective at preventing a deeper crisis, less "
                          "effective at promoting recovery."):
            self.play(Write(verdict), run_time=2.2)
        self.wait(1.0)

        kit = stick.kit(scale=0.7)
        St.place(kit, St.STAGE, ax=-0.7, ay=-0.7)
        with self.narrate("The first time Kit read that, he treated it as a result. "
                          "Here is what the numbers say. Write it down, move on.",
                          v="c"):
            self.play(FadeIn(kit), run_time=0.6)
        with self.narrate("Reading it again, after Dixit, he cannot let it alone.",
                          v="c"):
            self.play(kit.mood("thinking"), run_time=0.4)
        q = St.caption("why would one policy be good at one\nand bad at the other?",
                       SRC_KIT, T_SUB, width=36)
        St.place(q, St.FULL, ay=-0.35)
        with self.narrate("Why would one policy be good at stopping a fall and bad at "
                          "starting a rise? Those are not obviously different jobs.",
                          v="c"):
            self.play(FadeIn(q), run_time=1.0)
        with self.narrate("And he is uncomfortable. Not with the article — with "
                          "himself, for having read that sentence once already and "
                          "never asked whether there was a reason behind it.", v="c"):
            self.play(kit.slump(), run_time=1.0)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the two jobs
        self.heading("Two jobs, pulling apart")
        stop = VGroup(
            cards.icon("shield", MONEY, 1.6),
            St.caption("stopping a collapse", MONEY, T_BODY, width=18),
            St.points(["markets that keep working", "the upside held up",
                       "strongest when frightening"],
                      colour=MUTED, dot_colour=MONEY, size=T_SMALL, width=20,
                      buff=0.32),
        ).arrange(DOWN, buff=0.3)
        start = VGroup(
            cards.icon("slab", COST, 1.6),
            St.caption("starting a recovery", COST, T_BODY, width=18),
            St.points(["money you cannot get back", "turns on the downside",
                       "strongest when calm"],
                      colour=MUTED, dot_colour=COST, size=T_SMALL, width=20,
                      buff=0.32),
        ).arrange(DOWN, buff=0.3)
        two = VGroup(stop, start).arrange(RIGHT, buff=1.6)
        St.place(two, St.FULL, ay=0.0)
        with self.narrate("Preventing a collapse needs markets that keep working and "
                          "the upside held up. And by the good news principle, that is "
                          "exactly what stops a struggling firm closing. It is "
                          "strongest when things are frightening, because there is most "
                          "to repair and most upside to restore."):
            self.play(FadeIn(stop), run_time=1.4)
        with self.narrate("Starting a recovery needs firms to commit money they cannot "
                          "get back. By the bad news principle, that turns on the "
                          "downside — which is exactly what fear makes them least "
                          "willing to face. It is strongest when things are calm."):
            self.play(FadeIn(start), run_time=1.4)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the conclusion
        self.drop_heading()
        used = St.caption("used where job one is easiest\nand job two is hardest",
                          CHALK, T_SUB, width=32)
        St.place(used, St.WIDE, ay=0.75)
        with self.narrate("So the policy is used in exactly the state where the first "
                          "job is easiest and the second is hardest."):
            self.play(FadeIn(used), run_time=1.0)
        line = St.caption("it steadies without starting", SRC_KIT, T_HEAD, width=30)
        St.place(line, St.WIDE, ay=0.0)
        with self.narrate("It steadies without starting."):
            self.play(Write(line), run_time=2.0)
        self.wait(1.8)

        flag = St.caption("the last two steps are Kit's, not Dixit's", MUTED,
                          T_SUB, width=42)
        St.place(flag, St.FOOT, pad=0.06)
        with self.narrate("And flag clearly which parts of that are Kit's and not "
                          "Dixit's. That propping up the upside works best when things "
                          "are frightening, and that the two jobs therefore pull apart, "
                          "are steps Kit has added. Dixit's own text does not contain "
                          "them."):
            self.play(FadeIn(flag), run_time=1.0)
        self.beat()

        self.close_chapter([
            "their verdict: prevents a crisis, less so a recovery",
            "the two jobs need opposite halves of the spread",
            "and opposite conditions to work in",
            "it steadies without starting — Kit's step, not Dixit's",
        ])
