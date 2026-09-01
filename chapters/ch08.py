import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib import surface as SF
from lib.scale import MasterScale
from lib.theme import *


class Chapter08(Chapter):
    CH = 8
    TITLE = "Putting numbers on it"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["fog", "scale", "money", "people"]

    def body(self):
        # ------------------------------------------------ the sealed machine
        self.heading("Two dials, one number out")
        ava = stick.ava(scale=0.8)
        St.place(ava, St.STAGE, ax=-0.88, ay=-0.65)
        with self.narrate("So far this is a story. Is the effect big enough to matter, "
                          "or is it a curiosity?", v="c"):
            self.play(FadeIn(ava), run_time=0.6)

        box = RoundedRectangle(width=5.6, height=2.4, corner_radius=0.18,
                               color=MUTED, stroke_width=3)
        St.place(box, St.STAGE, ax=0.15, ay=0.35)
        blab = Text("the machine", font=FONT, font_size=T_SMALL, color=MUTED)
        blab.next_to(box, UP, buff=0.22)
        with self.narrate("The paper answers that with arithmetic. There is mathematics "
                          "behind it, and for now we leave it sealed in a box. Two "
                          "dials go in. One number comes out."):
            self.play(Create(box), FadeIn(blab), run_time=1.2)

        d1 = W.Dial("how choppy the\nrevenue is", "20% a year", frac=0.4, color=WAIT,
                    r=0.68)
        d2 = W.Dial("the cost of\ncapital", "5% a year", frac=0.35, color=MONEY, r=0.68)
        dials = VGroup(d1, d2).arrange(RIGHT, buff=1.1)
        dials.move_to(box.get_center())
        with self.narrate("Dial one. How choppy the revenue is — how much the money "
                          "coming in swings around in a typical year."):
            self.play(FadeIn(d1), run_time=0.9)
        anchors = St.points(["10% with exchange rates",
                             "25–40% an oil well or a mine",
                             "the base case sits at 20%"],
                            colour=WAIT, dot_colour=WAIT, size=T_BODY, width=20)
        St.place(anchors, St.SIDE, ay=0.35)
        with self.narrate("The paper gives anchors. About ten per cent a year for "
                          "revenue that moves with exchange rates. Twenty-five to forty "
                          "for an oil well or a copper mine. The base case sits between, "
                          "at twenty."):
            self.play(S.lag_map(FadeIn, anchors, lag=0.25), run_time=1.8)
        self.beat()
        self.play(FadeOut(anchors), run_time=0.5)
        with self.narrate("Dial two is the cost of capital, from chapter two. What the "
                          "money has to earn to be worth using."):
            self.play(FadeIn(d2), run_time=0.9)

        out = St.caption("a multiplier", TRIGGER, T_SUB, width=18)
        St.place(out, St.SIDE, ay=0.1)
        with self.narrate("And out of the box comes one number. A multiplier. The money "
                          "coming in must reach that multiplier, times the break-even "
                          "level, before building is right."):
            self.play(FadeIn(out), run_time=0.8)
            self.play(S.flash_around(out, TRIGGER))
        self.beat()
        self.play(FadeOut(box), FadeOut(blab), FadeOut(out), FadeOut(ava), run_time=0.6)

        # ------------------------------------------------ on the scale
        self.heading("The numbers, on the scale")
        # moved, not shrunk: shrinking a dial takes its label below legibility
        stacked = dials.copy().arrange(DOWN, buff=0.35)
        stacked.move_to(St.STAGE.point(-0.82, 0.0))
        self.play(Transform(dials, stacked), run_time=1.0)
        sc = MasterScale(x=-1.3, y=-0.45, height=4.6, lo=0.0, hi=3.7)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), run_time=0.9)
        base = sc.add_level("M", 1.00, "break-even", COST, width=2.2)
        self.play(Create(base[0]), FadeIn(base[1]), run_time=0.8)

        h1 = sc.add_level("H1", 1.86, "1.86 ×", TRIGGER, width=2.2, sw=5)
        with self.narrate("Base case. Cost of capital five per cent, choppiness twenty "
                          "per cent. The multiplier is one point eight six."):
            self.play(Create(h1[0]), FadeIn(h1[1]), run_time=1.2)
        self.beat()
        near = St.caption("nearly double break-even", CHALK, T_BODY, width=20)
        St.place(near, St.SIDE, ay=0.6)
        alt = St.caption("a 9.3% hurdle\nagainst a true 5%", TRIGGER, T_BODY, width=20)
        St.place(alt, St.SIDE, ay=0.1)
        with self.narrate("The money coming in must nearly double the break-even level "
                          "before she should build."):
            self.play(FadeIn(near), run_time=0.8)
        with self.narrate("Said the other way round, that is a hurdle rate of nine point "
                          "three per cent, against a true cost of capital of five."):
            self.play(FadeIn(alt), run_time=0.8)
        self.beat()
        self.play(FadeOut(near), FadeOut(alt), run_time=0.5)

        with self.narrate("Now turn the choppiness dial up. Forty per cent a year — an "
                          "oil well, a copper mine, a trade where prices swing hard."):
            self.play(d1.turn_to(0.8, "40% a year"), run_time=1.4)
        h2 = sc.add_level("H2", 3.32, "3.32 ×", TRIGGER, width=2.2, sw=5)
        big = St.caption("a 16.6% hurdle rate", TRIGGER, T_SUB, width=18)
        St.place(big, St.SIDE, ay=0.6)
        with self.narrate("The multiplier jumps to three point three two. The hurdle "
                          "rate to sixteen point six per cent."):
            self.play(Create(h2[0]), FadeIn(h2[1]), run_time=1.2)
            self.play(FadeIn(big), run_time=0.7)
        self.beat()
        self.play(FadeOut(big), FadeOut(h2), d1.turn_to(0.4, "20% a year"), run_time=1.0)

        # ------------------------------------------------ the strange one
        stop = St.caption("slow down here", CHALK, T_SUB, width=18)
        St.place(stop, St.SIDE, ay=0.75)
        self.play(FadeIn(stop), run_time=0.7)
        self.beat()
        with self.narrate("Now turn the other dial. Not up — down. Make money cheaper. "
                          "Cost of capital two per cent instead of five."):
            self.play(d2.turn_to(0.14, "2% a year"), run_time=1.6)
        h3 = sc.add_level("H3", 2.61, "2.61 ×", TRIGGER, width=2.2, sw=6)
        with self.narrate("And the multiplier goes up. Two point six one. Cheaper money "
                          "makes her more reluctant to build, not less."):
            self.play(Create(h3[0]), FadeIn(h3[1]), run_time=1.4)
            self.play(S.spark(h3[1], TRIGGER))
        self.beat()
        self.play(FadeOut(stop), run_time=0.4)
        twice = St.caption("cheaper money makes\nwaiting more attractive", TRIGGER,
                           T_SUB, width=20)
        St.place(twice, St.SIDE, ay=0.55)
        with self.narrate("Say that again, because it is the strangest result in the "
                          "paper. Cheaper money makes waiting more attractive."):
            self.play(FadeIn(twice), run_time=0.8)
        self.beat()
        why = St.caption("the future matters more,\nso learning about it is worth more",
                         CHALK, T_BODY, width=22)
        St.place(why, St.SIDE, ay=-0.35)
        with self.narrate("Here is why. When money is cheap, the future matters more to "
                          "you. And if the future matters more, then finding things out "
                          "about it is worth more. So waiting to find out is worth more."):
            self.play(FadeIn(why), run_time=1.0)
        self.beat()
        self.play(FadeOut(twice), FadeOut(why), run_time=0.5)

        # ------------------------------------------------ the limits
        ext = St.points(["very certain → multiplier 1, Marshall right",
                         "more uncertainty → it grows without limit"],
                        colour=CHALK, dot_colour=TRIGGER, size=T_BODY, width=22)
        St.place(ext, St.SIDE, ay=0.35)
        says = ["If the world is very certain, or the future is barely valued at all, "
                "the multiplier collapses to one — and Marshall is simply right.",
                "And as uncertainty grows, or money becomes nearly free, it grows "
                "without limit. In the paper's own words, the textbook analysis becomes "
                "totally misleading."]
        for i, row in enumerate(ext):
            with self.narrate(says[i]):
                self.play(FadeIn(row), run_time=0.8)
        self.beat()
        self.play(FadeOut(ext), run_time=0.4)

        gro = St.caption("growth 2% → 13.6% hurdle\ntrigger 3.9 × break-even",
                         CHALK, T_BODY, width=22)
        St.place(gro, St.SIDE, ay=0.35)
        h4 = sc.add_level("H4", 3.60, "3.9 ×", TRIGGER, width=2.2, sw=4)
        with self.narrate("One footnote. If the revenue is also growing — say two per "
                          "cent a year — two things pull against each other, and the "
                          "waiting effect wins. The hurdle rate goes to thirteen point "
                          "six per cent, and the trigger to three point nine times "
                          "break-even."):
            self.play(FadeIn(gro), run_time=0.8)
            self.play(Create(h4[0]), FadeIn(h4[1]), run_time=1.0)
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the sheet, in 3D
        self.drop_heading()
        with self.narrate("One last way of seeing all of that at once. The multiplier "
                          "depends on two things and two things only. Two things in, "
                          "one number out. That is a shape.", hold=True):
            pass
        ax3 = SF.axes()
        self.set_camera_orientation(phi=68 * DEGREES, theta=-52 * DEGREES, zoom=0.95)
        self.play(Create(ax3), run_time=1.3)
        xl = Text("choppier revenue →", font=FONT, font_size=T_SMALL, color=WAIT)
        yl = Text("cheaper money →", font=FONT, font_size=T_SMALL, color=MONEY)
        zl = Text("a higher bar", font=FONT, font_size=T_SMALL, color=TRIGGER)
        col = VGroup(zl, yl, xl).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        col.to_corner(DL, buff=0.6)
        self.add_fixed_in_frame_mobjects(col)
        self.remove(col)
        with self.narrate("Along one way, the revenue gets choppier. Along the other, "
                          "the money gets cheaper. And upwards is a higher bar."):
            self.play(S.lag_map(FadeIn, col, lag=0.25), run_time=1.2)

        sheet = SF.sheet(ax3)
        with self.narrate("And here is the shape."):
            self.play(Create(sheet), run_time=3.0)
        mesh = SF.gridlines(ax3)
        self.play(Create(mesh), run_time=1.6)
        self.beat()

        with self.narrate("Look at the near corner. Calm revenue, expensive money. The "
                          "sheet is almost flat, and the multiplier is almost one. That "
                          "is Marshall's world, and in it he is right."):
            self.move_camera(phi=64 * DEGREES, theta=-20 * DEGREES, run_time=3.0)
        self.beat()
        with self.narrate("Now follow it away from that corner. Every step towards "
                          "choppier revenue, and every step towards cheaper money, "
                          "lifts the sheet. The two effects do not cancel. They add."):
            self.move_camera(phi=58 * DEGREES, theta=-110 * DEGREES, run_time=4.0)
        self.beat()

        d_base = Dot3D(SF.point(ax3, 0.20, 0.05), radius=0.10, color=CHALK)
        d_chop = Dot3D(SF.point(ax3, 0.40, 0.05), radius=0.10, color=WAIT)
        d_cheap = Dot3D(SF.point(ax3, 0.20, 0.02), radius=0.10, color=MONEY)
        marks = VGroup(
            Text("1.86  the base case", font=FONT, font_size=T_SMALL, color=CHALK),
            Text("3.32  choppier", font=FONT, font_size=T_SMALL, color=WAIT),
            Text("2.61  cheaper money", font=FONT, font_size=T_SMALL, color=MONEY),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        marks.to_corner(UL, buff=0.6)
        self.add_fixed_in_frame_mobjects(marks)
        self.remove(marks)
        for dot, mark, say in ((d_base, marks[0], "The three numbers you just watched "
                                                  "are three points on this one sheet. "
                                                  "The base case."),
                               (d_chop, marks[1], "Choppier revenue — further along."),
                               (d_cheap, marks[2], "And cheaper money — further along "
                                                   "the other way.")):
            with self.narrate(say):
                self.play(FadeIn(dot), FadeIn(mark), run_time=0.9)
        self.beat()
        with self.narrate("Hold that picture. In chapter thirty-five we come back to "
                          "this exact sheet, and watch a firm walked across it — in the "
                          "wrong direction."):
            self.move_camera(phi=62 * DEGREES, theta=-160 * DEGREES, run_time=4.0)
        self.beat()
        self.play(FadeOut(sheet), FadeOut(mesh), FadeOut(ax3), FadeOut(d_base), FadeOut(d_chop),
                  FadeOut(d_cheap), FadeOut(marks), FadeOut(col), run_time=1.0)
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES, zoom=1.0)

        # ------------------------------------------------ resolve puzzle one
        res = St.caption("15% hurdle rates are arithmetic,\nnot stupidity", CHALK,
                         T_HEAD, width=34)
        St.place(res, St.WIDE, ay=0.1)
        with self.narrate("And that resolves the first of our three puzzles. Firms "
                          "demanding fifteen per cent when their money costs them five "
                          "are not being short-sighted. They are being correct."):
            self.play(Write(res), run_time=2.4)
        self.beat()

        self.close_chapter([
            "two dials → one multiplier",
            "base case 1.86× · 9.3% against a true 5%",
            "choppier → 3.32 · cheaper money → 2.61",
            "15% is arithmetic, not stupidity",
        ])
