import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.theme import *


class Chapter03(Chapter):
    CH = 3
    TITLE = "Three facts that don’t fit"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ['scale', 'money', 'border']

    def body(self):
        ava = stick.ava(scale=1.0).shift(LEFT * 5.2 + DOWN * 0.8)
        with self.narrate("Marshall's rule is clear, and it is wrong. Here are three "
                          "facts that do not fit it. All three come straight out of "
                          "the paper we are following."):
            self.play(FadeIn(ava), run_time=0.7)

        # ------------------------------------------------------- 1 hurdle rates
        one = cards.section_title("One — the bar firms actually use", color=CHALK, size=T_SUB)
        self.play(FadeIn(one), run_time=0.5)

        self.define("hurdle rate", "What a firm insists a project promises.", "scale", TRIGGER,
                    narration="First, a new term. A hurdle rate is the return a firm "
                              "insists a project must promise before it will pay for it.",
                    at=DOWN * 0.4, hold=4.0)

        base = Rectangle(width=1.1, height=0.7, color=WAIT, stroke_width=3,
                         fill_color=WAIT, fill_opacity=0.25).shift(LEFT * 2.0 + DOWN * 1.4)
        bl = Text("what the money\ncosts them", font=FONT, font_size=T_SMALL,
                  color=WAIT, line_spacing=0.9).next_to(base, DOWN, buff=0.22)
        with self.narrate("Here is what a firm's money costs it."):
            self.play(GrowFromEdge(base, DOWN), FadeIn(bl), run_time=0.9)

        tall = Rectangle(width=1.1, height=2.45, color=TRIGGER, stroke_width=3,
                         fill_color=TRIGGER, fill_opacity=0.25)
        tall.move_to(RIGHT * 1.2 + DOWN * 1.75 + UP * 2.45 / 2 + DOWN * 0.0)
        tall.align_to(base, DOWN)
        tl = Text("what they insist\na project promises", font=FONT, font_size=T_SMALL,
                  color=TRIGGER, line_spacing=0.9).next_to(tall, DOWN, buff=0.22)
        with self.narrate("And here is what they insist a project promises before they "
                          "will build it. Three or four times as much."):
            self.play(GrowFromEdge(tall, DOWN), FadeIn(tl), run_time=1.4)
            self.play(ava.mood("surprised"), run_time=0.4)
        self.beat()

        nums = cards.body("8 – 30%    median 15    mean 17",
                          size=T_BODY, color=CHALK, width=38)
        nums.next_to(one, DOWN, buff=0.5)
        with self.narrate("Asked directly, firms named rates from eight to thirty per "
                          "cent. The middle answer was fifteen per cent. The average "
                          "was seventeen."):
            self.play(FadeIn(nums), run_time=0.8)
        self.beat()
        cheap = cards.note("safe cost of capital: 4% nominal, ~0% real",
                           width=64)
        cheap.next_to(nums, DOWN, buff=0.4)
        with self.narrate("And the safe cost of their money at the time? A nominal "
                          "rate of four per cent, and a real rate close to zero."):
            self.play(FadeIn(cheap), run_time=0.8)
        self.beat()
        self.clear_stage(keep=[ava])

        # ------------------------------------------------------- 2 farmers
        two = cards.section_title("Two — the farmers who would not stop", color=CHALK, size=T_SUB)
        self.play(FadeIn(two), run_time=0.5)

        farmer = stick.StickFigure("A farmer", CHALK, hat="flat", scale=1.0)
        farmer.shift(LEFT * 1.6 + DOWN * 0.8)
        with self.narrate("Second. In the middle of the nineteen-eighties, American "
                          "farmers stayed open through long stretches of losses."):
            self.play(FadeIn(farmer), run_time=0.6)
            self.play(farmer.mood("worried"), run_time=0.4)

        b1 = Rectangle(width=1.0, height=0.55, color=MONEY, stroke_width=3,
                       fill_color=MONEY, fill_opacity=0.25).shift(RIGHT * 2.2 + DOWN * 1.5)
        b1.align_to(farmer, DOWN)
        t1 = Text("$6,000", font=FONT, font_size=T_BODY, color=MONEY).next_to(b1, UP, buff=0.14)
        c1 = Text("average income\nper farm, 1983", font=FONT, font_size=T_SMALL,
                  color=MUTED, line_spacing=0.9).next_to(b1, DOWN, buff=0.2)
        with self.narrate("In nineteen eighty-three the average net income for a farm "
                          "operator was six thousand dollars for the year."):
            self.play(GrowFromEdge(b1, DOWN), FadeIn(t1), FadeIn(c1), run_time=1.1)
        self.beat()

        b2 = Rectangle(width=1.0, height=1.24, color=MONEY, stroke_width=3,
                       fill_color=MONEY, fill_opacity=0.25).shift(RIGHT * 4.4)
        b2.align_to(b1, DOWN)
        t2 = Text("$13,500", font=FONT, font_size=T_BODY, color=MONEY).next_to(b2, UP, buff=0.14)
        c2 = Text("even leaving out rent\nand mortgage", font=FONT, font_size=T_SMALL,
                  color=MUTED, line_spacing=0.9).next_to(b2, DOWN, buff=0.2)
        with self.narrate("Even if you leave out the rent on the land and the mortgage "
                          "payments altogether, it only rises to thirteen and a half "
                          "thousand. For a year's work, for a whole family."):
            self.play(GrowFromEdge(b2, DOWN), FadeIn(t2), FadeIn(c2), run_time=1.1)
        self.beat()
        with self.narrate("Marshall's rule says: stop. They did not stop."):
            self.play(farmer.pace(1, run_time=1.8))
        self.clear_stage(keep=[ava])

        # ------------------------------------------------------- 3 dollar
        three = cards.section_title("Three — the dollar and the imports", color=CHALK, size=T_SUB)
        self.play(FadeIn(three), run_time=0.5)

        self.define("exchange rate", "How much of one country's money another "
                    "country's money will buy.", "border", WAIT,
                    narration="Two terms first. An exchange rate is how much of one "
                              "country's money another country's money will buy.",
                    at=DOWN * 0.2, hold=3.6)
        self.define("imports", "Goods made abroad and sold here.", "border", MONEY,
                    narration="And imports are simply goods made abroad and sold here.",
                    at=DOWN * 0.2, hold=3.2)

        border = DashedLine(UP * 1.6 + LEFT * 0.0, DOWN * 2.2, color=MUTED, stroke_width=3)
        abroad = Text("abroad", font=FONT, font_size=T_SMALL, color=MUTED).move_to(LEFT * 3.6 + UP * 1.4)
        home = Text("America", font=FONT, font_size=T_SMALL, color=MUTED).move_to(RIGHT * 3.6 + UP * 1.4)
        box = Rectangle(width=0.7, height=0.5, color=MONEY, stroke_width=3).move_to(LEFT * 3.4 + DOWN * 0.3)
        tag = Text("£", font=FONT, font_size=22, color=MONEY).next_to(box, UP, buff=0.1)
        with self.narrate("A strong dollar makes foreign goods cheap in America. From "
                          "nineteen-eighty to the end of nineteen eighty-four, the "
                          "dollar rose by about fifty per cent."):
            self.play(Create(border), FadeIn(abroad), FadeIn(home), run_time=0.9)
            self.play(FadeIn(box), FadeIn(tag), run_time=0.6)

        ax = Axes(x_range=[1980, 1990, 1], y_range=[0, 3, 1], x_length=7.4, y_length=2.6,
                  axis_config=AXIS)
        ax.shift(DOWN * 1.0 + RIGHT * 0.6)
        xl = Text("1980            1983         1985                    1987      1989",
                  font=FONT, font_size=T_TINY, color=MUTED)
        xl.next_to(ax, DOWN, buff=0.16)
        self.play(FadeOut(box), FadeOut(tag), FadeOut(border), FadeOut(abroad),
                  FadeOut(home), run_time=0.5)
        self.play(Create(ax), FadeIn(xl), run_time=1.0)

        dollar = ax.plot_line_graph(
            x_values=[1980, 1982, 1984, 1985, 1986, 1987, 1989],
            y_values=[1.4, 1.9, 2.3, 2.2, 1.7, 1.45, 1.42],
            line_color=WAIT, add_vertex_dots=False, stroke_width=5)
        dl = Text("the dollar", font=FONT, font_size=T_SMALL, color=WAIT)
        dl.next_to(dollar, UP, buff=0.1).shift(LEFT * 1.6)
        with self.narrate("Here is the dollar. Up sharply to the end of nineteen "
                          "eighty-four, then falling from early nineteen eighty-five, "
                          "until by the end of nineteen eighty-seven it was almost back "
                          "where it had been in nineteen seventy-eight."):
            self.play(Create(dollar), FadeIn(dl), run_time=2.6)

        imports = ax.plot_line_graph(
            x_values=[1980, 1982, 1983, 1985, 1987, 1989],
            y_values=[0.55, 0.55, 0.7, 1.5, 2.1, 2.25],
            line_color=MONEY, add_vertex_dots=False, stroke_width=5)
        il = Text("imports", font=FONT, font_size=T_SMALL, color=MONEY)
        il.next_to(ax, RIGHT, buff=0.1).shift(UP * 0.5)
        with self.narrate("And here are the imports. Flat for three years while the "
                          "dollar climbed. Then rising — and still rising, long after "
                          "the reason for it had gone away. They did not fall for "
                          "another two years, and if anything they rose a little."):
            self.play(Create(imports), FadeIn(il), run_time=3.0)
        self.beat()

        amb = cards.note("p. 108: “1978 level”   ·   p. 122: “1980 level”",
                         width=68)
        amb.to_edge(DOWN, buff=0.62)
        self.play(FadeIn(amb), run_time=0.6)
        self.wait(1.4)
        self.play(FadeOut(amb), run_time=0.4)

        self.clear_stage(keep=[ava])
        puzzle = cards.body("All three look like stupidity.", size=T_SUB, color=CHALK, width=26)
        puzzle.move_to(RIGHT * 1.4 + UP * 0.3)
        with self.narrate("Put the three together. On the textbook's own terms, all "
                          "three of these are firms behaving stupidly."):
            self.play(ava.animate.move_to(LEFT * 4.6 + DOWN * 1.4), run_time=0.5)
            self.play(FadeIn(puzzle), run_time=0.9)
        with self.narrate("They are not. And the next four chapters explain why.", v="c"):
            self.play(ava.mood("thinking"), run_time=0.5)

        self.close_chapter([
            "hurdle rates: 3–4× the cost of capital",
            "farmers absorbed years of losses",
            "imports arrived late — and stayed",
        ])
