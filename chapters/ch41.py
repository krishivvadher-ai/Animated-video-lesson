import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib import surface as SF
from lib.theme import *


class Chapter41(Chapter):
    CH = 41
    TITLE = "Bringing Part One back"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["scale", "fog", "money", "risk"]

    def body(self):
        # ------------------------------------------------ two articles
        self.heading("Two articles, one quantity")
        left = VGroup(cards.icon("bank", SRC_BR, 1.6),
                      St.caption("cheaper money\nraises investment", SRC_BR,
                                 T_SMALL, width=20)).arrange(DOWN, buff=0.3)
        right = VGroup(cards.icon("scale", SRC_DX, 1.6),
                       St.caption("the bar is not\nthe cost of money", SRC_DX,
                                  T_SMALL, width=20)).arrange(DOWN, buff=0.3)
        two = VGroup(left, right).arrange(RIGHT, buff=3.0)
        St.place(two, St.FULL, ay=0.35)
        with self.narrate("Kit puts the two articles side by side, and notices they are "
                          "arguing about the same quantity from opposite sides."):
            self.play(FadeIn(left), run_time=0.8)
            self.play(FadeIn(right), run_time=0.8)
        with self.narrate("One of them asserts that a lower cost of capital raises "
                          "investment."):
            self.play(S.flash_around(left, SRC_BR))
        with self.narrate("And the other spends a whole article showing that the number "
                          "standing between the cost of capital and the decision is not "
                          "the cost of capital."):
            self.play(S.flash_around(right, SRC_DX))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the reminder
        self.heading("Fifteen seconds of the multiplier")
        base = W.Bar(1.5, color=WAIT, width=1.3)
        tall = W.Bar(2.79, color=TRIGGER, width=1.3)
        pair = VGroup(base, tall).arrange(RIGHT, buff=2.2, aligned_edge=DOWN)
        St.place(pair, St.STAGE, ay=-0.3)
        l1 = VGroup(Text("1.00", font=FONT, font_size=T_BODY, color=WAIT),
                    St.caption("break-even", MUTED, T_SMALL, width=14)
                    ).arrange(DOWN, buff=0.14)
        l1.next_to(base, DOWN, buff=0.22)
        l2 = VGroup(Text("1.86", font=FONT, font_size=T_BODY, color=TRIGGER),
                    St.caption("the real bar", MUTED, T_SMALL, width=14)
                    ).arrange(DOWN, buff=0.14)
        l2.next_to(tall, DOWN, buff=0.22)
        St.collapse_bars(pair)
        with self.narrate("The bar a project must clear is the textbook bar, "
                          "multiplied."):
            self.play(Restore(base), FadeIn(l1), run_time=0.9)
            self.play(Restore(tall), FadeIn(l2), run_time=1.2)

        grows = St.caption("and it grows as the world\ngets more uncertain",
                           COST, T_BODY, width=22)
        St.place(grows, St.SIDE, ay=0.3)
        with self.narrate("And the multiplier grows as the world becomes more "
                          "uncertain."):
            self.play(FadeIn(grows), run_time=0.8)
            self.play(tall.rect.animate.stretch_to_fit_height(4.2).move_to(
                tall.rect.get_bottom() + UP * 2.1), run_time=1.4)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the sheet, walked across
        self.drop_heading()
        with self.narrate("Which means we can go back to the sheet from chapter eight, "
                          "and watch what the policy actually does to a firm's bar.",
                          hold=True):
            pass

        ax3 = SF.axes()
        self.set_camera_orientation(phi=62 * DEGREES, theta=-48 * DEGREES, zoom=0.88)
        self.play(Create(ax3), run_time=1.2)
        col = VGroup(
            Text("a higher bar", font=FONT, font_size=T_SMALL, color=TRIGGER),
            Text("cheaper money →", font=FONT, font_size=T_SMALL, color=MONEY),
            Text("choppier revenue →", font=FONT, font_size=T_SMALL, color=WAIT),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT).to_corner(DL, buff=0.6)
        self.add_fixed_in_frame_mobjects(col)
        self.remove(col)
        self.play(S.lag_map(FadeIn, col, lag=0.25), run_time=1.0)
        sheet = SF.sheet(ax3)
        self.play(Create(sheet), run_time=2.6)
        mesh = SF.gridlines(ax3)
        self.play(Create(mesh), run_time=1.6)

        d = Dot3D(SF.point(ax3, 0.20, 0.05), radius=0.11, color=CHALK)
        read = Text("1.86", font=FONT, font_size=T_SUB, color=CHALK)
        read.to_corner(UR, buff=0.7)
        self.add_fixed_in_frame_mobjects(read)
        self.remove(read)
        with self.narrate("Here is a firm in ordinary times. Twenty per cent "
                          "choppiness, money at five per cent. Its bar is one point "
                          "eight six times break-even."):
            self.play(FadeIn(d), FadeIn(read), run_time=1.0)
        self.beat()

        d2 = Dot3D(SF.point(ax3, 0.20, 0.02), radius=0.11, color=MONEY)
        read2 = Text("2.61", font=FONT, font_size=T_SUB, color=MONEY)
        read2.to_corner(UR, buff=0.7)
        self.add_fixed_in_frame_mobjects(read2)
        self.remove(read2)
        with self.narrate("The policy makes money cheaper. So the firm slides this "
                          "way — and the sheet under it goes up, not down. Two point "
                          "six one."):
            self.play(Transform(d, d2), FadeTransform(read, read2), run_time=2.0)
            self.move_camera(phi=62 * DEGREES, theta=-96 * DEGREES, run_time=2.6)
        self.beat()

        d3 = Dot3D(SF.point(ax3, 0.40, 0.02), radius=0.11, color=COST)
        read3 = Text("3.32 and rising", font=FONT, font_size=T_SUB, color=COST)
        read3.to_corner(UR, buff=0.7)
        self.add_fixed_in_frame_mobjects(read3)
        self.remove(read3)
        with self.narrate("But the policy is only ever used in a crisis. So at the very "
                          "same moment, the firm is dragged the other way too — into "
                          "the choppiest part of the sheet."):
            self.play(Transform(d, d3), FadeTransform(read2, read3), run_time=2.2)
            self.move_camera(phi=64 * DEGREES, theta=-142 * DEGREES, run_time=3.0)
        self.beat()

        both = Text("both movements push the bar up", font=FONT, font_size=T_SUB,
                    color=TRIGGER)
        both.to_edge(UP, buff=0.6)
        self.add_fixed_in_frame_mobjects(both)
        self.remove(both)
        with self.narrate("Both movements push the bar up. Not one up and one down. "
                          "Both up."):
            self.play(FadeIn(both), run_time=1.0)
        self.beat()
        self.play(FadeOut(sheet), FadeOut(mesh), FadeOut(ax3), FadeOut(d), FadeOut(read3),
                  FadeOut(col), FadeOut(both), run_time=1.0)
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES, zoom=1.0)

        # ------------------------------------------------ the sentence
        line = St.caption("a rate cut, delivered where\nrate cuts are blunted",
                          CHALK, T_HEAD, width=30)
        St.place(line, St.WIDE, ay=0.2)
        with self.narrate("Which gives the sentence this chapter exists for. "
                          "Quantitative easing is not a weaker version of a rate cut. "
                          "It is a rate cut delivered in the one situation that blunts "
                          "rate cuts."):
            self.play(Write(line), run_time=3.0)
        self.wait(2.0)
        self.clear_stage()

        # ------------------------------------------------ attribution
        self.heading("And whose is whose")
        rows = VGroup(
            VGroup(cards.source_tag("the bar, and that it rises", SRC_DX),
                   St.caption("Dixit", SRC_DX, T_BODY, width=12)
                   ).arrange(RIGHT, buff=0.6),
            VGroup(cards.source_tag("putting it next to this policy", SRC_KIT),
                   St.caption("Kit", SRC_KIT, T_BODY, width=12)
                   ).arrange(RIGHT, buff=0.6),
        ).arrange(DOWN, buff=0.7, aligned_edge=LEFT)
        St.place(rows, St.FULL, ay=0.2)
        with self.narrate("And be clear about whose is whose. The bar, and the fact "
                          "that it rises with uncertainty, is Dixit's."):
            self.play(FadeIn(rows[0]), run_time=0.9)
        with self.narrate("Putting it next to this policy is Kit's."):
            self.play(FadeIn(rows[1]), run_time=0.9)
        self.beat()

        self.close_chapter([
            "one article asserts what the other spends pages on",
            "cheaper money moves the firm up the sheet",
            "and a crisis moves it up the other way too",
            "a rate cut delivered where rate cuts are blunted",
        ])
