import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S
from lib.theme import *


class Chapter04(Chapter):
    CH = 4
    TITLE = "The three ingredients"
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = ['slab', 'fog', 'door', 'clock']

    def body(self):
        nell = stick.nell(scale=1.05).shift(LEFT * 4.8 + DOWN * 0.9)
        nl = nell.label()
        with self.narrate("Everything that follows rests on three things being true at "
                          "once. Three ingredients. Each one gets a picture, and each "
                          "one gets an icon you will see again whenever it is in play."):
            self.play(FadeIn(nell), FadeIn(nl), run_time=0.8)

        # ------------------------------------------------------ 1 sunk cost
        head = cards.section_title("One", color=SUNK, size=T_SUB)
        self.play(FadeIn(head), run_time=0.4)

        slab = Rectangle(width=3.0, height=0.5, color=SUNK, stroke_width=4,
                         fill_color=SUNK, fill_opacity=0.20).shift(RIGHT * 1.4 + DOWN * 1.6)
        slabel = Text("concrete foundation", font=FONT, font_size=T_SMALL,
                      color=SUNK).next_to(slab, DOWN, buff=0.2)
        bag = W.money_bag(SUNK, 1.0).move_to(RIGHT * 1.4 + UP * 1.4)

        with self.narrate("Nell pays for the concrete foundation of her new factory. "
                          "The money leaves her hands, and the slab appears."):
            self.play(FadeIn(bag), run_time=0.6)
            self.play(bag.animate.move_to(slab.get_center()).scale(0.4).set_opacity(0),
                      GrowFromEdge(slab, DOWN), FadeIn(slabel), run_time=1.4)
            self.remove(bag)

        with self.narrate("Now she changes her mind. She tries to sell the foundation "
                          "back. And nobody wants a hole in a field with concrete in it."):
            self.play(nell.mood("worried"), run_time=0.4)
            cross = VGroup(
                Line(LEFT * 0.4 + UP * 0.4, RIGHT * 0.4 + DOWN * 0.4, color=COST, stroke_width=6),
                Line(LEFT * 0.4 + DOWN * 0.4, RIGHT * 0.4 + UP * 0.4, color=COST, stroke_width=6),
            ).move_to(slab.get_center() + UP * 1.1)
            back = W.flow_arrow(slab.get_center() + UP * 0.4,
                                slab.get_center() + UP * 1.6, MUTED, sw=4)
            self.play(Create(back), run_time=0.6)
            self.play(FadeIn(cross), run_time=0.5)
            self.play(FadeOut(back), run_time=0.4)

        self.define("sunk cost", "Money you cannot get back.", "slab", SUNK,
                    narration="That is a sunk cost. Money that cannot be got back if "
                              "you change your mind later.",
                    at=UP * 1.4 + RIGHT * 1.4, hold=4.2)

        note = cards.note("sunk ≠ expensive", width=54)
        note.move_to(UP * 1.2 + RIGHT * 1.4)
        with self.narrate("And be careful. Sunk is not the same as expensive. A lorry "
                          "is expensive and you can sell it again. A hole in the ground "
                          "is cheap, and you cannot."):
            self.play(FadeIn(note), run_time=0.8)
        self.beat()
        self.play(FadeOut(note), FadeOut(cross), FadeOut(slab), FadeOut(slabel),
                  FadeOut(head), run_time=0.6)

        # ------------------------------------------------------ 2 uncertainty
        head2 = cards.section_title("Two", color=WAIT, size=T_SUB)
        self.play(FadeIn(head2), run_time=0.4)

        future = VGroup(
            Text("next year's\ncustomers", font=FONT, font_size=T_BODY, color=CHALK,
                 line_spacing=0.9))
        future.move_to(RIGHT * 1.8 + UP * 0.2)
        cloud = W.fog(width=6.0, height=3.0, n=9)
        cloud.move_to(future)

        with self.narrate("Second ingredient. Nell does not know what next year holds. "
                          "Will there be customers? How many? At what price?"):
            self.play(FadeIn(future), run_time=0.6)
            self.play(FadeIn(cloud), nell.mood("thinking"), run_time=1.0)

        with self.narrate("But — and this is the part that matters — the fog thins. "
                          "Every month that passes tells her a little more than she "
                          "knew the month before."):
            for i in range(3):
                self.play(cloud.animate.set_opacity(0.55 - 0.17 * (i + 1)), run_time=0.9)

        self.define("ongoing uncertainty", "You do not know what is coming — and you "
                    "learn a little more as time passes.", "fog", WAIT,
                    narration="Ongoing uncertainty, with information arriving "
                              "gradually. You do not know what is coming, and you learn "
                              "a little more as time passes.",
                    at=DOWN * 2.0, hold=4.2)
        self.play(FadeOut(cloud), FadeOut(future), FadeOut(head2), run_time=0.6)

        # ------------------------------------------------------ 3 the door
        head3 = cards.section_title("Three", color=MONEY, size=T_SUB)
        self.play(FadeIn(head3), run_time=0.4)

        d = W.door(MONEY, 1.3, 2.6, "the chance to build").move_to(RIGHT * 2.4 + UP * 0.1)
        with self.narrate("Third. If she does not build this year, the chance is "
                          "generally still there next year. The door stays open."):
            self.play(Create(d), run_time=1.0)
            self.play(nell.mood("neutral"), run_time=0.4)

        years = VGroup(*[Text(y, font=FONT, font_size=T_SMALL, color=MUTED)
                         for y in ("this year", "next year", "the year after")])
        years.arrange(DOWN, buff=0.5).next_to(d, RIGHT, buff=1.0)
        with self.narrate("This year. Next year. The year after that. Still open."):
            for y in years:
                self.play(FadeIn(y, shift=RIGHT * 0.2), run_time=0.5)

        self.define("the chance keeps", "The opportunity does not usually vanish if "
                    "you do not take it today.", "door", MONEY,
                    narration="The opportunity does not usually vanish if you do not "
                              "take it today.", at=DOWN * 2.2, hold=3.6)

        # ------------------------------------------------------ the payoff
        self.clear_stage()
        icons = VGroup(
            VGroup(cards.icon("slab", SUNK, 1.6),
                   cards.body("money you cannot get back", size=T_SMALL, color=SUNK, width=18)),
            VGroup(cards.icon("fog", WAIT, 1.6),
                   cards.body("a future you learn about slowly", size=T_SMALL, color=WAIT, width=18)),
            VGroup(cards.icon("door", MONEY, 1.6),
                   cards.body("a chance that keeps", size=T_SMALL, color=MONEY, width=18)),
        )
        for g in icons:
            g.arrange(DOWN, buff=0.4)
        icons.arrange(RIGHT, buff=1.5).shift(UP * 1.0)

        with self.narrate("Put those three together."):
            self.play(FadeIn(icons), run_time=1.0)

        payoff = cards.body("When all three are true, waiting is worth money.",
                            size=T_HEAD, color=CHALK, width=30)
        payoff.shift(DOWN * 1.7)
        with self.narrate("When all three are true, waiting is worth money."):
            self.play(FadeIn(payoff), run_time=0.8)
        self.beat()
        with self.narrate("And when any one of them is missing, it is not. Remember "
                          "that, because in chapter nine we take the third one away, "
                          "and the whole conclusion flips over."):
            self.play(Indicate(icons[2], color=COST, scale_factor=1.15), run_time=1.4)
        self.beat()

        self.close_chapter([
            "Sunk cost: money that cannot be got back.",
            "a future you learn a bit at a time",
            "the chance keeps",
            "all three → waiting pays",
        ])
