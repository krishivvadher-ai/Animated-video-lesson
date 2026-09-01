import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W, style as S, stage as St
from lib.theme import *


class Chapter48(Chapter):
    CH = 48
    TITLE = "The management half"
    PART = "PART THREE — THE ARGUMENT"
    RECAP_ICONS = ["queue", "door", "people", "clock"]

    def body(self):
        # ------------------------------------------------ the company grows
        self.heading("Grow the factory into a company")
        small = W.factory(CHALK, size=0.8)
        St.place(small, St.STAGE, ax=-0.5, ay=0.0)
        with self.narrate("Grow Nell's factory into a large company, with several "
                          "separately run parts."):
            self.play(Create(small), run_time=1.0)
            big = W.building(CHALK, size=1.0, kind="office")
            big.move_to(small)
            self.play(FadeTransform(small, big), run_time=1.4)
            divs = VGroup(*[Square(side_length=0.42, color=WAIT, stroke_width=3)
                            for _ in range(4)])
            divs.arrange(RIGHT, buff=0.3).next_to(big, DOWN, buff=0.5)
            self.play(S.lag_map(FadeIn, divs, lag=0.15), run_time=1.0)
        self.beat()

        kind = St.caption("not how high the number is —\nwhat kind of number it is",
                          SRC_KIT, T_BODY, width=24)
        St.place(kind, St.SIDE, ay=0.4)
        with self.narrate("So say this explicitly, because it is easy to miss. Kit's "
                          "dispute is not about how high the number is. It is about "
                          "what kind of number it is.", v="c"):
            self.play(FadeIn(kind), run_time=0.9)
            self.play(S.flash_around(kind, SRC_KIT))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the queue
        self.heading("A queue at the boardroom door")
        door = W.door(SUNK, w=1.1, h=2.2)
        St.place(door, St.STAGE, ax=0.75, ay=-0.1)
        dl = Text("the board", font=FONT, font_size=T_SMALL, color=SUNK)
        dl.next_to(door, DOWN, buff=0.28)
        queue = VGroup(*[VGroup(
            Rectangle(width=0.85, height=0.5, color=WAIT, stroke_width=3,
                      fill_color=WAIT, fill_opacity=0.2),
            Text(f"{i+1}", font=FONT, font_size=T_TINY, color=WAIT))
            for i in range(5)])
        for g in queue:
            g[1].move_to(g[0].get_center())
        queue.arrange(LEFT, buff=0.28)
        queue.next_to(door, LEFT, buff=0.5)
        with self.narrate("And here is the mechanism, as an actual queue of projects at "
                          "the boardroom door."):
            self.play(Create(door), FadeIn(dl), run_time=0.9)
            self.play(S.lag_map(FadeIn, queue, lag=0.12), run_time=1.4)

        assume = St.points(["money is not what runs out",
                            "management is"],
                           colour=CHALK, dot_colour=TRIGGER, size=T_BODY, width=20)
        St.place(assume, St.SIDE, ay=0.6)
        with self.narrate("State the assumption openly, because it is doing a lot of "
                          "work and it might be wrong. In a large company the thing "
                          "that runs out first is not money. It is management."):
            self.play(FadeIn(assume[0]), run_time=0.7)
            self.play(FadeIn(assume[1]), run_time=0.7)
        self.beat()

        tied = St.caption("the bar is tied to the next\nproject in the queue", TRIGGER,
                          T_BODY, width=22)
        St.place(tied, St.SIDE, ay=-0.4)
        with self.narrate("A minimum return set to solve that problem is tied to the "
                          "next project in the queue — the best thing the company would "
                          "have to drop in order to take this one on."):
            self.play(FadeIn(tied), run_time=0.9)
            self.play(S.flash_around(queue[1], TRIGGER))
        with self.narrate("And that is an internal quantity. It depends on how many "
                          "good ideas the business is generating, and how many capable "
                          "people it has spare."):
            self.play(S.pulse(queue, TRIGGER))
        self.beat()

        # ------------------------------------------------ the yield falls
        self.heading("So drop the yield, and watch")
        self.play(FadeOut(assume), FadeOut(tied), run_time=0.5)
        ax = Axes(x_range=[0, 6, 1], y_range=[0, 3, 1], x_length=3.4, y_length=1.7,
                  axis_config=AXIS)
        St.place(ax, St.SIDE, ay=0.55, fill=False)
        curve = ax.plot(lambda x: 2.4 - 0.3 * x, x_range=[0, 6], color=SRC_BR,
                        stroke_width=5)
        cl = Text("gilt yield", font=FONT, font_size=T_TINY, color=SRC_BR)
        cl.next_to(ax, DOWN, buff=0.16)
        with self.narrate("A fall in the return on government debt does not lengthen "
                          "anybody's working week."):
            self.play(Create(ax), FadeIn(cl), run_time=0.7)
            self.play(Create(curve), run_time=1.3)
        with self.narrate("The yield falls. And the queue does not move."):
            self.play(S.flash_around(queue, MUTED, run_time=2.0))
        self.beat()
        self.clear_stage()

        # ------------------------------------------------ the defensible version
        self.heading("The version he can defend")
        clocks = VGroup(
            VGroup(cards.icon("clock", SRC_BR, 1.5),
                   St.caption("the central bank's clock:\nmonths", SRC_BR,
                              T_SMALL, width=20)).arrange(DOWN, buff=0.28),
            VGroup(cards.icon("queue", SRC_KIT, 1.5),
                   St.caption("the company's clock:\nyears", SRC_KIT,
                              T_SMALL, width=20)).arrange(DOWN, buff=0.28),
        ).arrange(RIGHT, buff=2.6)
        St.place(clocks, St.FULL, ay=0.3)
        with self.narrate("So here is the version he can defend. Not that the number "
                          "never moves. But that it moves on the company's clock rather "
                          "than the central bank's.", v="c"):
            self.play(FadeIn(clocks[0]), run_time=0.8)
            self.play(FadeIn(clocks[1]), run_time=0.8)

        close = St.caption("close enough to failure to matter —\nbut not never",
                           CHALK, T_SUB, width=40)
        St.place(close, St.FULL, ay=-0.7)
        with self.narrate("Changing as the pipeline of ideas and the stock of managers "
                          "change, over years. For a policy meant to work inside a "
                          "downturn, that is close enough to failure to matter. But it "
                          "is not the same as never, and he will not say never.",
                          v="c"):
            self.play(FadeIn(close), run_time=1.0)
        self.beat()
        self.clear_stage()

        self.heading("And the attribution, plainly")
        rows = VGroup(
            VGroup(cards.source_tag("a hurdle rate as rationing", MUTED),
                   St.caption("not Kit's idea", MUTED, T_BODY, width=16)
                   ).arrange(RIGHT, buff=0.6),
            VGroup(cards.source_tag("the use he has put it to", SRC_KIT),
                   St.caption("that is his", SRC_KIT, T_BODY, width=16)
                   ).arrange(RIGHT, buff=0.6),
        ).arrange(DOWN, buff=0.7, aligned_edge=LEFT)
        St.place(rows, St.FULL, ay=0.2)
        with self.narrate("Treating a hurdle rate as a rationing device rather than a "
                          "calculation is not an idea Kit invented."):
            self.play(FadeIn(rows[0]), run_time=0.9)
        with self.narrate("What he would claim is the use he has put it to."):
            self.play(FadeIn(rows[1]), run_time=0.9)
        self.beat()

        self.close_chapter([
            "a big company rations management, not money",
            "so the bar is tied to the next project in the queue",
            "the yield falls, and the queue does not move",
            "it moves on the company's clock, not the Bank's",
        ])
