import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter03(Chapter):
    CH = 3
    TITLE = "Three facts that don’t fit"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ["scale", "money", "border"]

    def body(self):
        ava = stick.ava(scale=0.85)
        St.place(ava, St.STAGE, ax=-0.9, ay=-0.55)
        with self.narrate("Marshall's rule is clear, and it is wrong. Here are three "
                          "facts that do not fit it. All three come straight out of "
                          "the paper we are following."):
            self.play(FadeIn(ava), run_time=0.7)

        # ---------------------------------------------------- 1 hurdle rates
        self.heading("One — the bar firms actually use")
        self.define("hurdle rate", "The return a firm insists a project must promise.",
                    "scale", TRIGGER, at=UP * 0.4, hold=4.0)

        base = Rectangle(width=1.2, height=0.75, color=WAIT, stroke_width=3,
                         fill_color=WAIT, fill_opacity=0.30)
        tall = Rectangle(width=1.2, height=2.6, color=TRIGGER, stroke_width=3,
                         fill_color=TRIGGER, fill_opacity=0.30)
        pair = VGroup(base, tall).arrange(RIGHT, buff=2.0, aligned_edge=DOWN)
        St.place(pair, St.STAGE, ax=0.2, ay=-0.15)
        l1 = Text("what money costs", font=FONT, font_size=T_SMALL, color=WAIT)
        l1.next_to(base, DOWN, buff=0.25)
        l2 = Text("what they demand", font=FONT, font_size=T_SMALL, color=TRIGGER)
        l2.next_to(tall, DOWN, buff=0.25)
        for b in (base, tall):
            b.save_state(); b.stretch(0.0001, 1, about_edge=DOWN)

        with self.narrate("Here is what a firm's money costs it."):
            self.play(Restore(base), FadeIn(l1), run_time=1.0)
        with self.narrate("And here is what firms insist a project promises before they "
                          "will build it. Three or four times as much."):
            self.play(Restore(tall), FadeIn(l2), run_time=1.4)
            self.play(ava.mood("surprised"), run_time=0.4)
        self.beat()

        nums = St.caption("8 – 30%\nmedian 15\nmean 17", TRIGGER, T_SUB, width=14)
        St.place(nums, St.SIDE, ay=0.45)
        with self.narrate("Asked directly, firms named rates from eight to thirty per "
                          "cent. The middle answer was fifteen. The average was "
                          "seventeen."):
            self.play(FadeIn(nums), run_time=0.9)
        self.beat()
        cheap = St.caption("safe cost of money\nabout 4%", WAIT, T_BODY, width=18)
        St.place(cheap, St.SIDE, ay=-0.35)
        with self.narrate("And the safe cost of their money at the time? A nominal rate "
                          "of four per cent, and a real rate close to zero."):
            self.play(FadeIn(cheap), run_time=0.9)
            self.play(S.flash_around(nums, TRIGGER))
        self.beat()
        self.clear_stage(keep=[ava])

        # ---------------------------------------------------- 2 the farmers
        self.heading("Two — the farmers who would not stop")
        farmer = stick.StickFigure("A farmer", CHALK, hat="flat", scale=0.95)
        St.place(farmer, St.STAGE, ax=-0.6, ay=-0.2)
        with self.narrate("Second. In the middle of the nineteen-eighties, American "
                          "farmers stayed open through long stretches of losses."):
            self.play(FadeIn(farmer), run_time=0.7)
            self.play(farmer.mood("worried"), run_time=0.4)

        b1 = Rectangle(width=1.1, height=0.62, color=MONEY, stroke_width=3,
                       fill_color=MONEY, fill_opacity=0.30)
        b2 = Rectangle(width=1.1, height=1.40, color=MONEY, stroke_width=3,
                       fill_color=MONEY, fill_opacity=0.30)
        bars = VGroup(b1, b2).arrange(RIGHT, buff=1.5, aligned_edge=DOWN)
        St.place(bars, St.STAGE, ax=0.55, ay=-0.2)
        n1 = Text("$6,000", font=FONT, font_size=T_BODY, color=MONEY)
        n1.next_to(b1, UP, buff=0.18)
        n2 = Text("$13,500", font=FONT, font_size=T_BODY, color=MONEY)
        n2.next_to(b2, UP, buff=0.18)
        c1 = Text("a year, 1983", font=FONT, font_size=T_TINY, color=MUTED)
        c1.next_to(b1, DOWN, buff=0.2)
        c2 = Text("rent and mortgage\nleft out", font=FONT, font_size=T_TINY,
                  color=MUTED, line_spacing=0.9)
        c2.next_to(b2, DOWN, buff=0.2)
        for b in (b1, b2):
            b.save_state(); b.stretch(0.0001, 1, about_edge=DOWN)

        with self.narrate("In nineteen eighty-three the average net income for a farm "
                          "operator was six thousand dollars. For the year."):
            self.play(Restore(b1), FadeIn(n1), FadeIn(c1), run_time=1.1)
        self.beat()
        with self.narrate("Even leaving out the rent on the land and the mortgage "
                          "payments altogether, it only rises to thirteen and a half "
                          "thousand. For a whole family, for a year's work."):
            self.play(Restore(b2), FadeIn(n2), FadeIn(c2), run_time=1.2)
        self.beat()
        with self.narrate("Marshall's rule says: stop. They did not stop."):
            self.play(farmer.pace(1, run_time=1.8))
        self.clear_stage(keep=[ava])

        # ---------------------------------------------------- 3 the dollar
        self.heading("Three — the dollar and the imports")
        self.define("exchange rate", "How much of one country's money another's will "
                    "buy.", "border", WAIT, at=UP * 0.3, hold=3.6)
        self.define("imports", "Goods made abroad and sold here.", "border", MONEY,
                    at=UP * 0.3, hold=3.0)

        ax = Axes(x_range=[1980, 1990, 2], y_range=[0, 3, 1], x_length=7.6,
                  y_length=3.2, axis_config=AXIS)
        St.place(ax, St.STAGE, ay=0.05)
        xl = Text("1980            1984            1988", font=FONT,
                  font_size=T_TINY, color=MUTED)
        xl.next_to(ax, DOWN, buff=0.2)
        self.play(Create(ax), FadeIn(xl), run_time=1.1)

        dollar = ax.plot_line_graph(
            x_values=[1980, 1982, 1984, 1985, 1986, 1987, 1989],
            y_values=[1.4, 1.9, 2.3, 2.2, 1.7, 1.45, 1.42],
            line_color=WAIT, add_vertex_dots=False, stroke_width=5)
        dl = St.caption("the dollar", WAIT, T_BODY, width=14)
        St.place(dl, St.SIDE, ay=0.65)
        with self.narrate("Here is the dollar. Up sharply to the end of nineteen "
                          "eighty-four — it rose by about fifty per cent — then falling "
                          "from early nineteen eighty-five, until by the end of "
                          "eighty-seven it was almost back where it had been in "
                          "seventy-eight."):
            self.play(Create(dollar), FadeIn(dl), run_time=2.8)

        imports = ax.plot_line_graph(
            x_values=[1980, 1982, 1983, 1985, 1987, 1989],
            y_values=[0.55, 0.55, 0.7, 1.5, 2.1, 2.25],
            line_color=MONEY, add_vertex_dots=False, stroke_width=5)
        il = St.caption("imports", MONEY, T_BODY, width=14)
        St.place(il, St.SIDE, ay=0.15)
        with self.narrate("And here are the imports. Flat for three years while the "
                          "dollar climbed. Then rising — and still rising, long after "
                          "the reason for it had gone away."):
            self.play(Create(imports), FadeIn(il), run_time=2.8)
        self.beat()

        amb = St.caption("p. 108 says 1978 · p. 122 says 1980", MUTED, T_SMALL, width=26)
        St.place(amb, St.SIDE, ay=-0.5)
        with self.narrate("The paper gives that level two different ways on two "
                          "different pages. We use the first."):
            self.play(FadeIn(amb), run_time=0.8)
        self.beat()
        self.clear_stage(keep=[ava])

        # ---------------------------------------------------- the puzzle
        self.heading("All three look like stupidity")
        puzzle = St.points(["firms turn down profitable work",
                            "farmers absorb years of losses",
                            "imports arrive late, and stay"],
                           colour=CHALK, dot_colour=COST, size=T_SUB, width=34)
        St.place(puzzle, St.FULL, ay=0.1)
        says = ["Firms turn down work that is profitable on paper.",
                "Farmers absorb years of losses rather than shut.",
                "And imports arrive years late, then refuse to leave."]
        for i, row in enumerate(puzzle):
            with self.narrate(says[i]):
                self.play(FadeIn(row), run_time=0.7)
        with self.narrate("They are not being stupid. The next four chapters explain "
                          "why.", v="c"):
            self.play(ava.mood("thinking"), run_time=0.5)
            self.play(S.flash_around(puzzle, COST, run_time=2.0))
        self.beat()

        self.close_chapter([
            "hurdle rates: 3–4× the cost of capital",
            "farmers absorbed years of losses",
            "imports arrived late — and stayed",
        ])
