import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.scale import MasterScale
from lib import surface as SF
from lib.theme import *


class Chapter08(Chapter):
    CH = 8
    TITLE = "Putting numbers on it"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ['fog', 'scale', 'money', 'people']

    def body(self):
        ava = stick.ava(scale=0.8).shift(LEFT * 5.6 + DOWN * 1.8)
        with self.narrate("So far this is a story. Is the effect big enough to matter, "
                          "or is it a curiosity?", v="c"):
            self.play(FadeIn(ava), run_time=0.6)

        box = RoundedRectangle(width=5.4, height=2.6, corner_radius=0.2,
                               color=MUTED, stroke_width=3)
        box.move_to(UP * 0.9)
        blab = Text("the machine", font=FONT, font_size=T_SMALL, color=MUTED)
        blab.next_to(box, UP, buff=0.2)
        with self.narrate("The paper answers that with arithmetic. There is "
                          "mathematics behind it, and we are going to leave the "
                          "mathematics sealed in a box. Two dials go in. One number "
                          "comes out."):
            self.play(Create(box), FadeIn(blab), run_time=1.1)

        d1 = W.Dial("how choppy the\nrevenue is", "20% a year", frac=0.4, color=WAIT, r=0.72)
        d1.move_to(LEFT * 1.3 + UP * 0.9)
        d2 = W.Dial("the cost of\ncapital", "5% a year", frac=0.35, color=MONEY, r=0.72)
        d2.move_to(RIGHT * 1.3 + UP * 0.9)

        with self.narrate("Dial one. How choppy the revenue is — how much the money "
                          "coming in swings around in a typical year."):
            self.play(FadeIn(d1), run_time=0.9)
        anchors = cards.note("10%  ·  25–40%  ·  base 20%", width=58)
        anchors.to_edge(DOWN, buff=0.7)
        with self.narrate("The paper gives anchors. About ten per cent a year for "
                          "revenue that moves with exchange rates. Twenty-five to forty "
                          "per cent for an oil well or a copper mine. The base case "
                          "sits between them, at twenty."):
            self.play(FadeIn(anchors), run_time=0.9)
        self.beat()
        self.play(FadeOut(anchors), run_time=0.4)

        with self.narrate("Dial two is the cost of capital, which we defined in chapter "
                          "two. What the money has to earn to be worth using."):
            self.play(FadeIn(d2), run_time=0.9)

        out = Text("a multiplier", font=FONT, font_size=T_SUB, color=TRIGGER)
        out.next_to(box, DOWN, buff=1.6)
        arr = Line(box.get_bottom() + DOWN * 0.1, out.get_top() + UP * 0.15,
                   color=MUTED, stroke_width=3).add_tip(tip_length=0.16)
        with self.narrate("And out of the box comes one number. A multiplier."):
            self.play(Create(arr), FadeIn(out), run_time=0.9)
        rule = cards.body("multiplier × break-even",
                          size=T_BODY, color=CHALK, width=44)
        rule.next_to(out, DOWN, buff=0.45)
        with self.narrate("The money coming in must reach the multiplier times the "
                          "break-even level before building is the right move."):
            self.play(FadeIn(rule), run_time=0.9)
        self.beat()

        # -------------------------------------------------- base case on the scale
        self.play(FadeOut(box), FadeOut(blab), FadeOut(out), FadeOut(arr),
                  FadeOut(rule), FadeOut(ava), run_time=0.6)
        self.play(d1.animate.scale(0.8).move_to(LEFT * 5.1 + UP * 1.6),
                  d2.animate.scale(0.8).move_to(LEFT * 5.1 + DOWN * 1.5), run_time=0.9)

        sc = MasterScale(x=-1.6, y=-0.3, height=4.9, lo=0.0, hi=3.7)
        self.play(Create(sc.axis), FadeIn(sc.arrow_head), FadeIn(sc.title), run_time=1.0)
        base = sc.add_level("M", 1.00, "break-even", COST, width=2.4)
        self.play(Create(base[0]), FadeIn(base[1]), run_time=0.8)

        side = RIGHT * 4.4
        h1 = sc.add_level("H1", 1.86, "1.86 ×", TRIGGER, width=2.4, sw=5)
        with self.narrate("Base case. Cost of capital five per cent, choppiness twenty "
                          "per cent. The multiplier is one point eight six."):
            self.play(Create(h1[0]), FadeIn(h1[1]), run_time=1.3)
        self.beat()
        near = cards.body("nearly double break-even", size=T_BODY, color=CHALK, width=22)
        near.move_to(side + UP * 1.7)
        with self.narrate("The money coming in must nearly double the break-even level "
                          "before she should build."):
            self.play(FadeIn(near), run_time=0.8)
        self.beat()
        alt = cards.body("9.3% hurdle vs a true 5%", size=T_BODY, color=TRIGGER, width=22)
        alt.move_to(side + DOWN * 0.9)
        with self.narrate("Said the other way round, that is a hurdle rate of nine "
                          "point three per cent, against a true cost of capital of five."):
            self.play(FadeIn(alt), run_time=0.9)
        self.beat()
        self.play(FadeOut(near), FadeOut(alt), run_time=0.4)

        # -------------------------------------------------- choppiness up
        with self.narrate("Now turn the choppiness dial up. Forty per cent a year — an "
                          "oil well, a copper mine, a trade where prices swing hard."):
            self.play(d1.turn_to(0.8, "40% a year"), run_time=1.4)
        h2 = sc.add_level("H2", 3.32, "3.32 ×", TRIGGER, width=2.4, sw=5)
        big = cards.body("A hurdle rate of 16.6 per cent.",
                         size=T_SUB, color=TRIGGER, width=20)
        big.move_to(side + UP * 1.9)
        with self.narrate("The multiplier jumps to three point three two. The hurdle "
                          "rate to sixteen point six per cent."):
            self.play(Create(h2[0]), FadeIn(h2[1]), run_time=1.2)
            self.play(FadeIn(big), run_time=0.7)
        self.beat()
        self.play(FadeOut(big), FadeOut(h2), d1.turn_to(0.4, "20% a year"), run_time=1.0)

        # -------------------------------------------------- the counter-intuitive one
        stop = cards.body("slow down here",
                          size=T_SUB, color=CHALK, width=20)
        stop.move_to(side + UP * 2.1)
        self.play(FadeIn(stop), run_time=0.7)
        self.beat()
        with self.narrate("Now turn the other dial. Not up — down. Make money cheaper. "
                          "Cost of capital two per cent instead of five."):
            self.play(d2.turn_to(0.14, "2% a year"), run_time=1.6)

        h3 = sc.add_level("H3", 2.61, "2.61 ×", TRIGGER, width=2.4, sw=6)
        with self.narrate("And the multiplier goes up. Two point six one. Cheaper "
                          "money makes her more reluctant to build, not less."):
            self.play(Create(h3[0]), FadeIn(h3[1]), run_time=1.4)
        self.beat()
        self.play(FadeOut(stop), run_time=0.3)

        twice = cards.body("Cheaper money makes waiting more attractive.",
                           size=T_SUB, color=TRIGGER, width=20)
        twice.move_to(side + UP * 1.9)
        with self.narrate("Say that again, because it is the strangest result in the "
                          "paper. Cheaper money makes waiting more attractive."):
            self.play(FadeIn(twice), run_time=0.8)
        self.beat()
        why = cards.body("cheaper future → information worth more",
                         size=T_BODY, color=CHALK, width=22)
        why.move_to(side + DOWN * 0.8)
        with self.narrate("Here is why. When money is cheap, the future matters more "
                          "to you. And if the future matters more, then finding things "
                          "out about the future is worth more. So waiting to find out "
                          "is worth more."):
            self.play(FadeIn(why), run_time=1.0)
        self.beat()
        self.play(FadeOut(twice), FadeOut(why), run_time=0.5)

        # -------------------------------------------------- the two extremes
        ext = cards.bullet_list([
            "very certain → multiplier 1 → Marshall right",
            "more uncertainty → multiplier grows without limit",
        ], color=CHALK, width=22)
        ext.move_to(side + UP * 1.2)
        with self.narrate("Two extremes are worth knowing. If the world is very "
                          "certain, or the future is barely valued at all, the "
                          "multiplier collapses to one — and Marshall is simply right."):
            self.play(FadeIn(ext[0]), run_time=0.8)
        with self.narrate("And as uncertainty grows, or money becomes nearly free, the "
                          "multiplier grows without limit. In the paper's own words, "
                          "the textbook analysis becomes totally misleading."):
            self.play(FadeIn(ext[1]), run_time=0.8)
        self.beat()
        self.play(FadeOut(ext), run_time=0.4)

        # -------------------------------------------------- growth footnote
        gro = cards.body("growth 2% → 13.6% hurdle, 3.9 × break-even", size=T_BODY, color=CHALK, width=22)
        gro.move_to(side + UP * 1.4)
        h4 = sc.add_level("H4", 3.60, "3.9 ×", TRIGGER, width=2.4, sw=4)
        with self.narrate("One footnote, worth a moment. If the revenue is also growing "
                          "— say two per cent a year — two things pull against each "
                          "other, and the waiting effect wins. The hurdle rate goes "
                          "from nine point three to thirteen point six per cent, and "
                          "the trigger to three point nine times break-even."):
            self.play(FadeIn(gro), run_time=0.9)
            self.play(Create(h4[0]), FadeIn(h4[1]), run_time=1.0)
        self.beat()
        self.play(FadeOut(gro), run_time=0.4)

        # -------------------------------------------------- the whole surface in 3D
        self.clear_stage()
        with self.narrate("One last way of seeing all of that at once. The multiplier "
                          "depends on two things and two things only — how choppy the "
                          "revenue is, and what the money costs. Two things in, one "
                          "number out. That is a shape."):
            pass

        ax = SF.axes()
        ax.move_to(ORIGIN)
        self.set_camera_orientation(phi=68 * DEGREES, theta=-52 * DEGREES, zoom=0.95)
        self.play(Create(ax), run_time=1.4)

        xl = Text("choppier revenue →", font=FONT, font_size=T_SMALL, color=WAIT)
        yl = Text("cheaper money →", font=FONT, font_size=T_SMALL, color=MONEY)
        zl = Text("a higher bar", font=FONT, font_size=T_SMALL, color=TRIGGER)
        xl.to_corner(DOWN + LEFT, buff=0.7)
        yl.next_to(xl, UP, buff=0.25).align_to(xl, LEFT)
        zl.next_to(yl, UP, buff=0.25).align_to(xl, LEFT)
        self.add_fixed_in_frame_mobjects(xl, yl, zl)
        with self.narrate("Along this way, the revenue gets choppier. Along that way, "
                          "the money gets cheaper. And upwards is a higher bar."):
            self.play(FadeIn(xl), run_time=0.4)
            self.play(FadeIn(yl), run_time=0.4)
            self.play(FadeIn(zl), run_time=0.4)

        sheet = SF.sheet(ax)
        with self.narrate("And here is the shape."):
            self.play(Create(sheet), run_time=3.0)
        self.beat()

        with self.narrate("Look at the corner nearest us. Calm revenue, expensive "
                          "money. The sheet is almost flat, and the multiplier is "
                          "almost one. That is Marshall's world, and in it he is right."):
            self.move_camera(phi=64 * DEGREES, theta=-20 * DEGREES, run_time=3.0)
        self.beat()

        with self.narrate("Now follow it away from that corner. Every step towards "
                          "choppier revenue, and every step towards cheaper money, "
                          "lifts the sheet. The two effects do not cancel. They add."):
            self.move_camera(phi=58 * DEGREES, theta=-110 * DEGREES, run_time=4.0)
        self.beat()

        d_base = Dot3D(SF.point(ax, 0.20, 0.05), radius=0.09, color=CHALK)
        d_chop = Dot3D(SF.point(ax, 0.40, 0.05), radius=0.09, color=CHALK)
        d_cheap = Dot3D(SF.point(ax, 0.20, 0.02), radius=0.09, color=CHALK)
        t_base = cards.body("1.86  ·  the base case", size=T_BODY, color=CHALK, width=22)
        t_chop = cards.body("3.32  ·  choppier revenue", size=T_BODY, color=WAIT, width=22)
        t_cheap = cards.body("2.61  ·  cheaper money", size=T_BODY, color=MONEY, width=22)
        for t, pos in ((t_base, UP * 2.5 + LEFT * 4.3),
                       (t_chop, UP * 1.6 + LEFT * 4.3),
                       (t_cheap, UP * 0.7 + LEFT * 4.3)):
            t.move_to(pos)
        self.add_fixed_in_frame_mobjects(t_base, t_chop, t_cheap)
        self.remove(t_base, t_chop, t_cheap)

        with self.narrate("The three numbers we just watched are three points on this "
                          "one sheet. The base case."):
            self.play(FadeIn(d_base), FadeIn(t_base), run_time=0.9)
        with self.narrate("Choppier revenue — further along."):
            self.play(FadeIn(d_chop), FadeIn(t_chop), run_time=0.9)
        with self.narrate("And cheaper money — further along the other way."):
            self.play(FadeIn(d_cheap), FadeIn(t_cheap), run_time=0.9)
        self.beat()

        with self.narrate("Hold that picture. In chapter twenty-two we come back to "
                          "this exact sheet, and we watch a firm walked across it — in "
                          "the wrong direction."):
            self.move_camera(phi=62 * DEGREES, theta=-160 * DEGREES, run_time=4.0)
        self.beat()
        self.play(FadeOut(sheet), FadeOut(ax), FadeOut(d_base), FadeOut(d_chop),
                  FadeOut(d_cheap), FadeOut(t_base), FadeOut(t_chop), FadeOut(t_cheap),
                  FadeOut(xl), FadeOut(yl), FadeOut(zl), run_time=1.0)
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES, zoom=1.0)

        # -------------------------------------------------- resolve puzzle one
        self.clear_stage()
        res = cards.body("15% hurdle rates are arithmetic.", size=T_HEAD, color=CHALK, width=30)
        with self.narrate("And that resolves the first of our three puzzles out loud. "
                          "Firms demanding fifteen per cent when their money costs them "
                          "five are not being short-sighted. They are being correct."):
            self.play(Write(res), run_time=2.2)
        self.beat()

        self.close_chapter([
            "two dials → one multiplier",
            "base case 1.86× · 9.3% vs a true 5%",
            "choppier → 3.32 · cheaper money → 2.61",
            "15% is arithmetic, not stupidity",
        ])
