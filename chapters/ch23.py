import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from manim import *
from lib.base import Chapter
from lib import stick, cards, widgets as W
from lib.theme import *


class Chapter23(Chapter):
    CH = 23
    TITLE = "Leg two: cheaper money, and feeling richer"
    PART = "PART TWO — THE POLICY"
    RECAP_ICONS = ["money", "shield", "people", "bank"]

    def body(self):
        with self.narrate("Leg one moved the prices of things in financial markets. Leg "
                          "two has to turn that into somebody actually spending money. "
                          "And it does it in two ways."):
            pass
        two = VGroup(
            VGroup(cards.icon("money", MONEY, 2.2),
                   cards.body("borrowing gets cheaper", size=T_BODY, color=MONEY, width=16)),
            VGroup(cards.icon("scale", TRIGGER, 2.2),
                   cards.body("owners feel richer", size=T_BODY, color=TRIGGER, width=16)),
        )
        for g in two:
            g.arrange(DOWN, buff=0.4)
        two.arrange(RIGHT, buff=3.0)
        self.play(FadeIn(two), run_time=1.2)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- cost of capital
        head = Text("First — the cost of capital", font=FONT, font_size=T_SUB,
                    color=MONEY).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)

        steps = [
            ("borrowers are tied to safe rates",
             "The rates households and firms borrow at are tied to safe government "
             "rates at the same length of time."),
            ("safe rates down ⇒ their rates down",
             "So if the whole set of government rates comes down, those rates should "
             "come down too."),
            ("banks fund themselves more cheaply",
             "And if banks benefit from higher asset prices in the same way ordinary "
             "companies do, then their own cost of borrowing falls as well."),
            ("so loans get cheaper",
             "And a bank that funds itself more cheaply can lower the price of the "
             "loans it makes."),
        ]
        rows = VGroup(*[cards.body(a, size=T_BODY, color=CHALK, width=44)
                        for a, _ in steps])
        rows.arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 0.4)
        for i, (_, say) in enumerate(steps):
            with self.narrate(say):
                self.play(FadeIn(rows[i], shift=RIGHT * 0.2), run_time=0.7)
        self.beat()

        self.play(FadeOut(rows), run_time=0.5)
        q = cards.quote_card(
            "This fall in the cost of capital should boost consumption and investment "
            "by increasing incentives to borrow and reducing incentives to save.",
            "Bowdler & Radia (2012), p. 612", SRC_BR, width=44)
        q.move_to(UP * 0.4)
        if q.width > 11.4:
            q.scale(11.4 / q.width)
        with self.narrate("And that gives the sentence the whole policy rests on. Their "
                          "words: this fall in the cost of capital should boost "
                          "consumption and investment, by increasing incentives to "
                          "borrow and reducing incentives to save."):
            self.play(FadeIn(q), run_time=1.4)
        self.beat()
        remember = cards.note("Part Three begins here",
                              width=50)
        remember.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(remember), run_time=0.6)
        self.wait(1.4)
        self.clear_stage()

        # ---------------------------------------------------- the qualifications
        head2 = Text("And the authors immediately qualify it — three times",
                     font=FONT, font_size=T_SUB, color=SRC_BR).to_edge(UP, buff=0.7)
        self.play(FadeIn(head2), run_time=0.5)

        shields = VGroup()
        texts = [
            "the banking sector was damaged",
            "small firms cannot sell bonds",
            "a weak bank may keep the saving",
        ]
        says = [
            "One. The banking sector was badly damaged at exactly the time the policy "
            "was used. So anything travelling through it may be impaired.",
            "Two. Households and smaller companies cannot borrow by selling bonds to "
            "investors in the first place. So they may not benefit from that route at "
            "all.",
            "Three. And a bank that is short of capital of its own may simply keep the "
            "saving rather than pass it on.",
        ]
        for i in range(3):
            sh = W.shield(SRC_BR, None, 0.9)
            sh.move_to(LEFT * 3.6 + RIGHT * i * 2.2 + UP * 1.4)
            t = cards.body(texts[i], size=T_BODY, color=SRC_BR, width=42)
            t.move_to(DOWN * 1.2)
            with self.narrate(says[i]):
                self.play(FadeIn(sh, scale=0.85), run_time=0.6)
                self.play(FadeIn(t), run_time=0.7)
                self.wait(0.4)
                self.play(FadeOut(t), run_time=0.4)
            shields.add(sh)
        self.beat()

        # and the routes that survive
        routes = cards.bullet_list([
            "supply chains",
            "a cheaper pound helps exporters",
            "banks may pass it on anyway",
        ], color=MONEY, width=42, dotc=MONEY)
        routes.move_to(DOWN * 1.0)
        with self.narrate("And be fair to them, because they do not leave it there. "
                          "They name three further routes by which small firms might "
                          "still benefit."):
            pass
        says2 = ["Supply-chain effects. A small firm tied to a large one benefits "
                 "either through extra demand, or through being paid more easily.",
                 "A cheaper pound makes a small exporter more competitive.",
                 "And falls in safe rates and in bank funding costs may be passed on to "
                 "all borrowers anyway."]
        for i in range(3):
            with self.narrate(says2[i]):
                self.play(FadeIn(routes[i], shift=RIGHT * 0.2), run_time=0.7)
        self.beat()
        self.clear_stage()

        # ---------------------------------------------------- the government
        head3 = Text("And then they ask about one borrower in particular",
                     font=FONT, font_size=T_SUB, color=SRC_BR).to_edge(UP, buff=0.7)
        self.play(FadeIn(head3), run_time=0.5)
        gov = stick.StickFigure("the government", CHALK, hat="collar", scale=0.9)
        gov.move_to(LEFT * 4.0 + DOWN * 0.4)
        gl = gov.label()
        self.play(FadeIn(gov), FadeIn(gl), run_time=0.7)
        with self.narrate("An obvious implication of a fall in gilt yields is that the "
                          "government's own cost of borrowing is now lower. Gilts are "
                          "exactly what was bought."):
            pass
        qq = cards.quote_card(
            "Their spending plans should therefore be unaffected by cyclical movements "
            "in interest rates.", "Bowdler & Radia (2012), p. 613", SRC_BR, width=36)
        qq.move_to(RIGHT * 1.6 + UP * 0.4)
        if qq.width > 8.4:
            qq.scale(8.4 / qq.width)
        with self.narrate("And their answer is that it will not change what the "
                          "government does. Governments take a longer-term view. Their "
                          "spending plans should therefore be unaffected by cyclical "
                          "movements in interest rates."):
            self.play(FadeIn(qq), run_time=1.2)
        self.beat()
        keep = cards.note("Part Three spends a chapter on this",
                          width=52)
        keep.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(keep), run_time=0.6)
        self.wait(1.4)
        self.clear_stage()

        # ---------------------------------------------------- wealth
        head4 = Text("Second — wealth", font=FONT, font_size=T_SUB,
                     color=TRIGGER).to_edge(UP, buff=0.7)
        self.play(FadeIn(head4), run_time=0.5)

        house = VGroup(W.factory(TRIGGER, 0.5))
        shares = VGroup(cards.icon("scale", TRIGGER, 2.0))
        owner = stick.StickFigure("an owner", CHALK, scale=0.8)
        row = VGroup(house, shares, owner).arrange(RIGHT, buff=2.0).move_to(UP * 0.8)
        with self.narrate("When asset prices go up, the people who own those assets are "
                          "richer. And higher wealth should mean more spending."):
            self.play(FadeIn(row), run_time=1.0)
            self.play(owner.mood("pleased"), run_time=0.4)

        fig = cards.body("£375bn → about +30% to household financial wealth", size=T_BODY, color=SRC_BR, width=44)
        fig.move_to(DOWN * 0.6)
        with self.narrate("They put a number on it. Three hundred and seventy-five "
                          "billion pounds of announced purchases will eventually boost "
                          "British households' net financial wealth by about thirty per "
                          "cent."):
            self.play(FadeIn(fig), run_time=1.2)
        self.beat()

        dist = cards.bullet_list([
            "gains go to the biggest holders",
            "for most pensions, the effects cancel",
            "an underfunded scheme gets worse",
        ], color=CHALK, width=44, dotc=SRC_BR)
        dist.move_to(DOWN * 0.6)
        self.play(FadeOut(fig), run_time=0.4)
        says3 = ["And they are open about who gets them. Those gains go largely to "
                 "whoever holds the most financial assets. In particular, older and "
                 "more affluent households.",
                 "For most pensions the two effects roughly cancel. The rate you can "
                 "buy an income at falls with gilt yields — but the pot itself is worth "
                 "more, for exactly the same reason.",
                 "But a scheme that was already short of money is likely to have been "
                 "made worse off. Its assets and its promises both rose in value, which "
                 "widened the gap between them."]
        for i in range(3):
            with self.narrate(says3[i]):
                self.play(FadeIn(dist[i], shift=RIGHT * 0.2), run_time=0.8)
        self.beat()
        fairness = cards.body("winners and losers", size=T_SUB, color=SRC_BR, width=40)
        fairness.to_edge(DOWN, buff=0.6)
        with self.narrate("As with all monetary policy, they say, there are winners and "
                          "losers."):
            self.play(FadeIn(fairness), run_time=0.9)
        self.beat()

        self.close_chapter([
            "safe rates down ⇒ borrowing cheaper",
            "hedged three times · three more routes",
            "the government: cheaper, and unmoved",
            "+30% wealth, unevenly shared",
        ])
