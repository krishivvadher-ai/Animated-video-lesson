import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.theme import *


class Chapter31(Chapter):
    CH = 31
    TITLE = "The other tools in the drawer"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["signal", "bank", "money", "clock"]

    def body(self):
        with self.narrate("Buying assets was not the only thing central banks did. The "
                          "authors group the rest into three, and each one is worth "
                          "knowing, because Part Three has to be fair about what else "
                          "was going on."):
            pass

        # ---------------------------------------------------- forward guidance
        head = Text("One — saying what you will do next",
                    font=FONT, font_size=T_SUB, color=WAIT).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)

        ax = Axes(x_range=[0, 6, 1], y_range=[0, 4, 1], x_length=8.6, y_length=2.8,
                  axis_config={"color": MUTED, "stroke_width": 2,
                               "include_ticks": False, "include_tip": False})
        ax.shift(DOWN * 0.4)
        yl = Text("the policy rate", font=FONT, font_size=T_SMALL, color=MUTED)
        yl.next_to(ax, LEFT, buff=0.2).rotate(PI / 2)
        flat = ax.plot_line_graph(x_values=[0, 6], y_values=[0.4, 0.4],
                                  line_color=MONEY, add_vertex_dots=False,
                                  stroke_width=5)
        expected = ax.plot_line_graph(x_values=[0, 2, 4, 6], y_values=[0.4, 1.4, 2.4, 3.2],
                                      line_color=COST, add_vertex_dots=False,
                                      stroke_width=4)
        el = Text("what people expected", font=FONT, font_size=T_SMALL, color=COST)
        el.next_to(expected, UP, buff=0.15).shift(LEFT * 1.0)
        gl = Text("what the Bank said would happen", font=FONT, font_size=T_SMALL,
                  color=MONEY)
        gl.next_to(flat, DOWN, buff=0.3)
        self.play(Create(ax), FadeIn(yl), run_time=0.9)
        with self.narrate("Left to themselves, people expect a rate that has been cut "
                          "to nothing to start rising again fairly soon."):
            self.play(Create(expected), FadeIn(el), run_time=1.4)
        with self.narrate("So the central bank simply tells them otherwise."):
            self.play(Create(flat), FadeIn(gl), run_time=1.4)
        self.beat()

        dates = cards.bullet_list([
            "December 2008: “for some time”",
            "March 2009: “an extended period”",
            "August 2011: “at least mid-2013”",
            "January 2012: “late 2014”",
            "September 2012: “a considerable time after the recovery strengthens”",
        ], color=WAIT, width=40, dotc=WAIT)
        dates.scale(0.8).move_to(RIGHT * 2.2 + UP * 1.4)
        says = ["In December two thousand and eight: rates would stay put for some time.",
                "By March two thousand and nine: for an extended period.",
                "By August two thousand and eleven: until at least the middle of "
                "twenty-thirteen.",
                "By January twenty-twelve: late twenty-fourteen.",
                "And in September twenty-twelve, further still — a highly accommodative "
                "stance would remain appropriate for a considerable time after the "
                "recovery strengthened."]
        self.play(FadeOut(el), FadeOut(gl), FadeOut(yl), run_time=0.4)
        self.play(VGroup(ax, flat, expected).animate.scale(0.6).to_corner(DOWN + LEFT,
                                                                         buff=0.8),
                  run_time=0.9)
        for i in range(5):
            with self.narrate(says[i]):
                self.play(FadeIn(dates[i], shift=RIGHT * 0.2), run_time=0.6)
        self.beat()
        honest = cards.body("It did move expectations — but markets never fully priced "
                            "the cuts in. And none of it was quite the promise to be "
                            "irresponsible that the theory calls for.",
                            size=T_BODY, color=SRC_BR, width=44)
        honest.to_edge(DOWN, buff=0.5)
        with self.narrate("And the authors are careful about how well it worked. It did "
                          "move expectations. But markets never fully priced in the cuts "
                          "the announcements implied. And none of it was quite the "
                          "promise to be irresponsible later that the theory in the last "
                          "chapter actually calls for."):
            self.play(FadeIn(honest), run_time=1.4)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- liquidity operations
        head2 = Text("Two — lending to banks that cannot borrow",
                     font=FONT, font_size=T_SUB, color=MONEY).to_edge(UP, buff=0.7)
        self.play(FadeIn(head2), run_time=0.5)

        cb = W.building(SRC_BR, 0.65, "bank", "the central bank").move_to(
            LEFT * 4.2 + UP * 0.3)
        banks = VGroup(*[W.building(CHALK, 0.45, "office") for _ in range(3)])
        banks.arrange(RIGHT, buff=1.0).move_to(RIGHT * 2.6 + UP * 0.3)
        self.play(FadeIn(cb), FadeIn(banks), run_time=1.0)
        with self.narrate("This one is the oldest job a central bank has, and it is not "
                          "really monetary policy at all. When a sound bank cannot "
                          "borrow simply because everyone has panicked, the central bank "
                          "lends to it — at a penal rate, and against good collateral."):
            arr = W.flow_arrow(cb.get_right() + RIGHT * 0.3,
                               banks.get_left() + LEFT * 0.3, MONEY)
            self.play(Create(arr), run_time=1.2)
        self.beat()
        kinds = cards.bullet_list([
            "standing facilities, widened to more collateral and more counterparties",
            "emergency lending to particular institutions in distress",
            "and longer-term swaps: good collateral lent out against weaker collateral",
        ], color=CHALK, width=42, dotc=MONEY)
        kinds.scale(0.9).move_to(DOWN * 1.9)
        says2 = ["Standing facilities, widened during the crisis to accept more kinds "
                 "of collateral from more kinds of institution.",
                 "Emergency lending to particular institutions in trouble.",
                 "And longer-term swaps, where the central bank lends out high-quality "
                 "securities against weaker collateral. Britain's Special Liquidity "
                 "Scheme lent roughly a hundred and eighty-five billion pounds of "
                 "Treasury bills that way, for up to three years."]
        for i in range(3):
            with self.narrate(says2[i]):
                self.play(FadeIn(kinds[i], shift=RIGHT * 0.2), run_time=0.7)
        self.beat()
        eu = cards.body("The European operations lent over €1 trillion for three years "
                        "— aimed, their central bank argued, at repairing the "
                        "transmission mechanism itself.",
                        size=T_BODY, color=SRC_BR, width=44)
        eu.to_edge(DOWN, buff=0.5)
        with self.narrate("And in the euro area, two operations in late twenty-eleven "
                          "and early twenty-twelve lent over a trillion euros for three "
                          "years — aimed, their central bank argued, at repairing the "
                          "transmission mechanism itself."):
            self.play(FadeOut(kinds), FadeIn(eu), run_time=1.2)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- credit easing
        head3 = Text("Three — paying banks to lend", font=FONT, font_size=T_SUB,
                     color=TRIGGER).to_edge(UP, buff=0.7)
        self.play(FadeIn(head3), run_time=0.5)

        with self.narrate("The third group exists because of the wedge from chapter "
                          "twenty-three. Banks looked risky, so their own funding was "
                          "dear, so what they charged households and firms stayed high."):
            pass

        one = VGroup(
            cards.body("a guarantee scheme", size=T_SUB, color=MONEY, width=18),
            cards.body("the government stands behind up to £20bn of bank debt, so "
                       "investors face gilt-like risk — and banks get cheaper funding "
                       "if they cut what they charge small firms",
                       size=T_SMALL, color=CHALK, width=26),
        ).arrange(DOWN, buff=0.4)
        two = VGroup(
            cards.body("funding for lending", size=T_SUB, color=TRIGGER, width=18),
            cards.body("four-year funding, at least 5 per cent of a bank's existing "
                       "loan book — about £80bn — and unlimited more if it lends more",
                       size=T_SMALL, color=CHALK, width=26),
        ).arrange(DOWN, buff=0.4)
        cols = VGroup(one, two).arrange(RIGHT, buff=1.4).move_to(UP * 0.6)
        with self.narrate("The first was a guarantee. The government stands behind up "
                          "to twenty billion pounds of bank debt, so an investor buying "
                          "it faces the same risk as buying a gilt. And the bank gets "
                          "that funding at a discount if it agrees to cut what it "
                          "charges smaller companies."):
            self.play(FadeIn(one), run_time=1.2)
        small = cards.note("But £20bn is only about 8 per cent of a year's gross "
                           "lending to small firms by the largest banks — so the scheme "
                           "is limited in scale, and the authors say so.", width=54)
        small.to_edge(DOWN, buff=0.6)
        with self.narrate("Though twenty billion is only about eight per cent of a "
                          "year's lending to small firms by the largest banks. Limited "
                          "in scale, as the authors put it."):
            self.play(FadeIn(small), run_time=1.0)
        self.beat()
        self.play(FadeOut(small), run_time=0.4)

        with self.narrate("The second was bigger, and cleverer. Four-year funding, of "
                          "at least five per cent of a bank's existing loan book — "
                          "around eighty billion pounds across the eligible banks."):
            self.play(FadeIn(two), run_time=1.2)

        fee = VGroup(
            Text("lend more  →  fee 0.25%", font=FONT, font_size=T_BODY, color=MONEY),
            Text("lend 5% less  →  fee 1.5%", font=FONT, font_size=T_BODY, color=COST),
        ).arrange(DOWN, buff=0.5).move_to(DOWN * 1.9)
        with self.narrate("And every extra pound a bank lent raised the amount it could "
                          "borrow under the scheme. A bank holding its lending steady "
                          "or growing it paid a quarter of one per cent. A bank "
                          "shrinking its lending by five per cent paid one and a half — "
                          "six times as much, on the whole amount."):
            self.play(FadeIn(fee), run_time=1.2)
        self.beat()

        self.close_chapter([
            "forward guidance: telling people what the rate will do next",
            "liquidity operations: lending to sound banks nobody else will fund",
            "credit easing: guarantees and cheap funding, priced to reward lending",
            "and none of these is the asset-purchase policy itself",
        ])
