"""The recurring cast: one reusable stick figure with a real walk cycle.

Every abstract idea in this film happens to one of these before it becomes a
diagram, so this class is written first and used everywhere.
"""
import numpy as np
from manim import (
    VGroup, VMobject, Circle, Line, Dot, Arc, Rectangle, RoundedRectangle,
    Ellipse, Text, Polygon, ORIGIN, UP, DOWN, LEFT, RIGHT, PI, TAU,
    AnimationGroup, Succession, Rotate, MoveToTarget, FadeIn, FadeOut,
    Create, Write, ValueTracker, always_redraw, linear, there_and_back,
    smooth, rate_functions,
)
from lib.theme import CHALK, MUTED, BG, T_BODY, T_SMALL, FONT

HEAD_R = 0.30
BODY_L = 0.70
LEG_L = 0.55
ARM_L = 0.45
LW = 4.0


class StickFigure(VGroup):
    """A named figure that walks, gestures, changes expression and speaks."""

    def __init__(self, name, accent=CHALK, hat=None, prop=None, hair=False,
                 scale=1.0, tall=False, **kw):
        super().__init__(**kw)
        self.name_str = name
        self.accent = accent
        self.hat_kind = hat
        self.prop_kind = prop
        self.facing = 1          # +1 right, -1 left
        self._mood = "neutral"
        self._phase = 0.0
        self.tall = tall

        b = BODY_L * (1.12 if tall else 1.0)
        self.body_len = b

        self.head = Circle(radius=HEAD_R, color=accent, stroke_width=LW)
        self.head.move_to(UP * (b + HEAD_R))

        self.torso = Line(UP * b, ORIGIN, color=accent, stroke_width=LW)

        self.leg_l = Line(ORIGIN, DOWN * LEG_L + LEFT * 0.16, color=accent, stroke_width=LW)
        self.leg_r = Line(ORIGIN, DOWN * LEG_L + RIGHT * 0.16, color=accent, stroke_width=LW)

        sh = UP * (b * 0.78)
        self.arm_l = Line(sh, sh + DOWN * 0.22 + LEFT * ARM_L, color=accent, stroke_width=LW)
        self.arm_r = Line(sh, sh + DOWN * 0.22 + RIGHT * ARM_L, color=accent, stroke_width=LW)
        self.shoulder = sh

        self.face = VGroup()
        self._build_face("neutral")

        self.extras = VGroup()
        if hair:
            tuft = Arc(radius=0.16, start_angle=PI * 0.15, angle=PI * 0.7,
                       color=accent, stroke_width=LW)
            tuft.move_to(self.head.get_top() + UP * 0.07)
            self.extras.add(tuft)
        if hat == "flat":
            brim = Line(LEFT * 0.34, RIGHT * 0.34, color=accent, stroke_width=LW)
            crown = Rectangle(width=0.42, height=0.20, color=accent, stroke_width=LW)
            crown.next_to(brim, UP, buff=0)
            cap = VGroup(brim, crown).move_to(self.head.get_top() + UP * 0.12)
            self.extras.add(cap)
        if hat == "collar":
            col = Polygon(LEFT * 0.22 + UP * 0.10, ORIGIN, RIGHT * 0.22 + UP * 0.10,
                          color=accent, stroke_width=LW, fill_opacity=0)
            col.move_to(UP * (b - 0.05))
            self.extras.add(col)
        if hat == "specs":
            l = Rectangle(width=0.19, height=0.15, color=accent, stroke_width=3)
            r = l.copy()
            l.move_to(self.head.get_center() + LEFT * 0.11 + UP * 0.04)
            r.move_to(self.head.get_center() + RIGHT * 0.11 + UP * 0.04)
            bridge = Line(l.get_right(), r.get_left(), color=accent, stroke_width=3)
            self.extras.add(VGroup(l, r, bridge))
        if hat == "pack":
            pk = RoundedRectangle(width=0.30, height=0.42, corner_radius=0.07,
                                  color=accent, stroke_width=3)
            pk.move_to(UP * (b * 0.55) + LEFT * 0.26)
            self.extras.add(pk)

        self.prop = VGroup()
        self._build_prop(prop)

        self.add(self.torso, self.leg_l, self.leg_r, self.arm_l, self.arm_r,
                 self.head, self.face, self.extras, self.prop)
        if scale != 1.0:
            self.scale(scale)
        self.unit = scale
        self._seat_prop()

    # ------------------------------------------------------------- face
    def _build_face(self, mood):
        """Always exactly five parts -- two eyes, two brows, one mouth -- so a
        mood change is a clean transform whatever the expression."""
        c = self.head.get_center()
        r = HEAD_R
        eye_y = c + UP * r * 0.28
        el = Circle(radius=0.040, color=self.accent, stroke_width=3,
                    fill_color=self.accent, fill_opacity=1).move_to(eye_y + LEFT * r * 0.36)
        er = Circle(radius=0.040, color=self.accent, stroke_width=3,
                    fill_color=self.accent, fill_opacity=1).move_to(eye_y + RIGHT * r * 0.36)
        bl = Line(c + LEFT * r * 0.58 + UP * r * 0.60,
                  c + LEFT * r * 0.16 + UP * r * 0.60,
                  color=self.accent, stroke_width=3)
        br = Line(c + RIGHT * r * 0.16 + UP * r * 0.60,
                  c + RIGHT * r * 0.58 + UP * r * 0.60,
                  color=self.accent, stroke_width=3)
        bl.set_opacity(0.0)
        br.set_opacity(0.0)
        mo = c + DOWN * r * 0.34
        if mood == "pleased":
            m = Arc(radius=r * 0.46, start_angle=PI * 1.15, angle=PI * 0.7,
                    color=self.accent, stroke_width=3).move_to(mo)
        elif mood == "worried":
            m = Arc(radius=r * 0.46, start_angle=PI * 0.15, angle=PI * 0.7,
                    color=self.accent, stroke_width=3).move_to(mo)
            bl.set_opacity(1.0).rotate(-0.35)
            br.set_opacity(1.0).rotate(0.35)
        elif mood == "thinking":
            m = Line(c + LEFT * r * 0.24 + DOWN * r * 0.34,
                     c + RIGHT * r * 0.10 + DOWN * r * 0.44,
                     color=self.accent, stroke_width=3)
            bl.set_opacity(1.0).rotate(0.28)
        elif mood == "surprised":
            el.become(Circle(radius=0.058, color=self.accent, stroke_width=3)
                      .move_to(el.get_center()))
            er.become(Circle(radius=0.058, color=self.accent, stroke_width=3)
                      .move_to(er.get_center()))
            m = Ellipse(width=0.13, height=0.18, color=self.accent,
                        stroke_width=3).move_to(mo)
        else:
            m = Line(c + LEFT * r * 0.24 + DOWN * r * 0.36,
                     c + RIGHT * r * 0.24 + DOWN * r * 0.36,
                     color=self.accent, stroke_width=3)
        self.face.become(VGroup(el, er, bl, br, m))
        self._mood = mood

    def set_mood(self, mood):
        """Change expression in place. Returns self so it chains."""
        keep = self.get_center()
        sc = self.unit
        anchor = self.head.get_center()
        # rebuild in local coordinates then move onto the current head
        tmp = StickFigure(self.name_str, self.accent, self.hat_kind, None,
                          scale=1.0, tall=self.tall)
        tmp._build_face(mood)
        f = tmp.face
        f.scale(sc)
        f.move_to(anchor + (f.get_center() - tmp.head.get_center()) * 1.0)
        self.face.become(f)
        self._mood = mood
        return self

    def mood(self, mood):
        """Animation form of set_mood."""
        target = self.copy()
        target.set_mood(mood)
        return _Become(self.face, target.face)

    # ------------------------------------------------------------- prop
    def _build_prop(self, kind):
        self.prop.become(VGroup())
        sh = self.shoulder
        if kind == "clipboard":
            bd = Rectangle(width=0.34, height=0.44, color=self.accent, stroke_width=3)
            clip = Line(LEFT * 0.09, RIGHT * 0.09, color=self.accent, stroke_width=4)
            clip.move_to(bd.get_top())
            g = VGroup(bd, clip).move_to(sh + RIGHT * 0.52 + DOWN * 0.30)
            self.prop.add(g)
        elif kind == "book":
            bk = Rectangle(width=0.46, height=0.34, color=self.accent, stroke_width=3)
            spine = Line(bk.get_top(), bk.get_bottom(), color=self.accent, stroke_width=3)
            g = VGroup(bk, spine).move_to(sh + RIGHT * 0.55 + DOWN * 0.28)
            self.prop.add(g)
        elif kind == "printout":
            pg = Rectangle(width=0.32, height=0.42, color=self.accent, stroke_width=3)
            marks = VGroup(*[Line(LEFT * 0.10, RIGHT * 0.10, color=self.accent,
                                  stroke_width=2).shift(UP * y)
                             for y in (0.10, 0.0, -0.10)])
            g = VGroup(pg, marks).move_to(sh + RIGHT * 0.52 + DOWN * 0.30)
            self.prop.add(g)
        elif kind == "dial":
            d = Circle(radius=0.42, color=self.accent, stroke_width=3)
            nd = Line(ORIGIN, UP * 0.30, color=self.accent, stroke_width=3)
            g = VGroup(d, nd).move_to(sh + RIGHT * 0.75 + DOWN * 0.45)
            self.prop.add(g)
        elif kind == "question":
            q = Text("?", font=FONT, font_size=34, color=self.accent)
            q.move_to(sh + RIGHT * 0.55 + UP * 0.30)
            self.prop.add(q)

    # ------------------------------------------------------------- motion
    def _rest_legs(self):
        hip = self.torso.get_end()
        u = self.unit
        return (Line(hip, hip + DOWN * LEG_L * u + LEFT * 0.16 * u,
                     color=self.accent, stroke_width=LW),
                Line(hip, hip + DOWN * LEG_L * u + RIGHT * 0.16 * u,
                     color=self.accent, stroke_width=LW))

    def _rest_arms(self):
        sh = self.torso.get_start()
        u = self.unit
        return (Line(sh, sh + DOWN * 0.22 * u + LEFT * ARM_L * u,
                     color=self.accent, stroke_width=LW),
                Line(sh, sh + DOWN * 0.22 * u + RIGHT * ARM_L * u,
                     color=self.accent, stroke_width=LW))

    def rest(self):
        """Return to the neutral standing pose and re-seat the prop."""
        ll, rl = self._rest_legs()
        la, ra = self._rest_arms()
        self.leg_l.become(ll); self.leg_r.become(rl)
        self.arm_l.become(la); self.arm_r.become(ra)
        self._seat_prop()
        return self

    def _seat_prop(self):
        if len(self.prop) == 0:
            return
        hand = self.arm_r.get_end()
        off = {"clipboard": RIGHT * 0.12 + DOWN * 0.10,
               "book": RIGHT * 0.16 + DOWN * 0.04,
               "printout": RIGHT * 0.12 + DOWN * 0.10,
               "dial": RIGHT * 0.42 + DOWN * 0.20,
               "question": RIGHT * 0.55 + UP * 0.95}.get(self.prop_kind, RIGHT * 0.14)
        self.prop.move_to(hand + off * self.unit)

    def _legs_at(self, phase):
        """Return (left_leg, right_leg) lines for a walk-cycle phase."""
        hip = self.torso.get_end()
        sw = 0.42 * np.sin(phase)
        lift = 0.10 * max(0.0, np.sin(phase))
        l = Line(hip, hip + DOWN * (LEG_L * self.unit - lift) + RIGHT * sw * self.unit,
                 color=self.accent, stroke_width=LW)
        r = Line(hip, hip + DOWN * (LEG_L * self.unit - 0.10 * max(0.0, -np.sin(phase)))
                 - RIGHT * sw * self.unit,
                 color=self.accent, stroke_width=LW)
        return l, r

    def _arms_at(self, phase):
        sh = self.torso.get_start()
        sw = 0.30 * np.sin(phase + PI)
        u = self.unit
        l = Line(sh, sh + DOWN * 0.30 * u + RIGHT * (sw - 0.20) * u,
                 color=self.accent, stroke_width=LW)
        r = Line(sh, sh + DOWN * 0.30 * u - RIGHT * (sw - 0.20) * u,
                 color=self.accent, stroke_width=LW)
        return l, r

    def walk_to(self, point, run_time=1.6, steps=4):
        """A real walk cycle -- legs alternate, arms counter-swing."""
        start = self.get_center()
        target = np.array(point, dtype=float)
        target[1] = start[1] if abs(target[1] - start[1]) < 1e-9 else target[1]
        from manim import UpdateFromAlphaFunc

        def uf(m, alpha):
            a = alpha
            m.move_to(start + (target - start) * a)
            ph = a * steps * PI
            ll, rl = m._legs_at(ph)
            la, ra = m._arms_at(ph)
            m.leg_l.become(ll)
            m.leg_r.become(rl)
            m.arm_l.become(la)
            m.arm_r.become(ra)
            m._seat_prop()
            if alpha > 0.999:
                m.rest()
                m.move_to(target)

        return UpdateFromAlphaFunc(self, uf, run_time=run_time, rate_func=linear)

    def pace(self, n=2, span=1.1, run_time=2.6):
        """Indecision: step across and back again. Used constantly."""
        from manim import UpdateFromAlphaFunc
        start = self.get_center()

        def uf(m, alpha):
            off = span * np.sin(alpha * n * TAU) * 0.5
            m.move_to(start + RIGHT * off)
            ph = alpha * n * 4 * PI
            ll, rl = m._legs_at(ph)
            m.leg_l.become(ll)
            m.leg_r.become(rl)
            m._seat_prop()
            if alpha > 0.999:
                m.rest()
                m.move_to(start)

        return UpdateFromAlphaFunc(self, uf, run_time=run_time, rate_func=linear)

    def point_at(self, mobject, run_time=0.8):
        """Raise the near arm towards a target."""
        from manim import UpdateFromAlphaFunc
        sh = self.torso.get_start()
        tgt = mobject.get_center() if hasattr(mobject, "get_center") else np.array(mobject)
        d = tgt - sh
        d = d / (np.linalg.norm(d) or 1.0)
        rest_end = self.arm_r.get_end().copy()
        new_end = sh + d * (ARM_L * self.unit * 1.35)

        def uf(m, alpha):
            m.arm_r.become(Line(sh, rest_end + (new_end - rest_end) * alpha,
                                color=m.accent, stroke_width=LW))
            m._seat_prop()
        return UpdateFromAlphaFunc(self, uf, run_time=run_time)

    def shrug(self, run_time=1.0):
        from manim import UpdateFromAlphaFunc
        sh = self.torso.get_start()
        u = self.unit

        def uf(m, alpha):
            k = np.sin(alpha * PI)
            m.arm_l.become(Line(sh, sh + LEFT * ARM_L * u + UP * 0.34 * u * k,
                                color=m.accent, stroke_width=LW))
            m.arm_r.become(Line(sh, sh + RIGHT * ARM_L * u + UP * 0.34 * u * k,
                                color=m.accent, stroke_width=LW))
        return UpdateFromAlphaFunc(self, uf, run_time=run_time)

    def nod(self, run_time=0.9):
        from manim import UpdateFromAlphaFunc
        h0 = self.head.get_center().copy()
        f0 = self.face.get_center().copy()

        def uf(m, alpha):
            dy = -0.10 * self.unit * np.sin(alpha * TAU)
            m.head.move_to(h0 + UP * dy)
            m.face.move_to(f0 + UP * dy)
        return UpdateFromAlphaFunc(self, uf, run_time=run_time)

    def slump(self, run_time=0.9):
        from manim import UpdateFromAlphaFunc
        c0 = self.get_center().copy()

        def uf(m, alpha):
            m.move_to(c0 + DOWN * 0.18 * self.unit * alpha)
        return UpdateFromAlphaFunc(self, uf, run_time=run_time)

    def turn(self):
        """Flip to face the other way."""
        self.flip()
        self.facing *= -1
        return self

    # ------------------------------------------------------------- speech
    def _bubble(self, text, direction, thought, width, color, font_size):
        txt = Text(text, font=FONT, font_size=font_size, color=color,
                   line_spacing=0.9)
        if txt.width > width:
            txt.scale(width / txt.width)
        pad = 0.22
        box = RoundedRectangle(
            width=max(txt.width + 2 * pad, 0.9),
            height=txt.height + 2 * pad,
            corner_radius=0.28 if thought else 0.14,
            color=color, stroke_width=3,
            fill_color=BG, fill_opacity=0.92,
        )
        txt.move_to(box.get_center())
        g = VGroup(box, txt)
        anchor = self.head.get_center()
        g.move_to(anchor + direction * (g.height / 2 + 0.55) +
                  (RIGHT * self.facing * 0.9 if abs(direction[1]) > 0.5 else direction * 0.6))
        # tail
        if thought:
            p1 = Circle(radius=0.09, color=color, stroke_width=3,
                        fill_color=BG, fill_opacity=0.92)
            p2 = Circle(radius=0.055, color=color, stroke_width=3,
                        fill_color=BG, fill_opacity=0.92)
            mid = (anchor + box.get_bottom()) / 2
            p1.move_to(mid + UP * 0.10)
            p2.move_to(anchor + UP * 0.30)
            g.add(p1, p2)
        else:
            base = box.get_bottom() if direction[1] > 0 else box.get_left()
            tail = Polygon(base + LEFT * 0.14, base + RIGHT * 0.14,
                           anchor + UP * 0.30,
                           color=color, stroke_width=3,
                           fill_color=BG, fill_opacity=0.92)
            g.add(tail)
        return g

    def say(self, text, direction=UP, width=3.6, color=None, font_size=26):
        return self._bubble(text, direction, False, width, color or self.accent, font_size)

    def think(self, text, direction=UP, width=3.4, color=None, font_size=26):
        return self._bubble(text, direction, True, width, color or self.accent, font_size)

    def label(self, font_size=24, color=None, follow=True):
        """A name caption that tracks the figure as it moves."""
        fig = self
        t = Text(self.name_str, font=FONT, font_size=font_size, color=color or MUTED)
        t.next_to(fig, DOWN, buff=0.18)
        if follow:
            t.add_updater(lambda m: m.next_to(fig, DOWN, buff=0.18))
        return t


class _Become(AnimationGroup):
    """Swap one mobject's shape for another over time (used for moods)."""

    def __init__(self, source, target, **kw):
        from manim import Transform
        super().__init__(Transform(source, target), **kw)


# ------------------------------------------------------------------ cast
def nell(**kw):
    return StickFigure("Nell", CHALK, hair=True, prop="clipboard", **kw)


def marshall(**kw):
    return StickFigure("Marshall", CHALK, hat="specs", prop="book", **kw)


def ava(**kw):
    return StickFigure("Ava", CHALK, prop="question", tall=True, **kw)


def kenji(**kw):
    return StickFigure("Kenji", CHALK, hat="flat", prop="clipboard", **kw)


def kit(**kw):
    return StickFigure("Kit", CHALK, hat="pack", prop="printout", **kw)


def governor(**kw):
    return StickFigure("The Governor", CHALK, hat="collar", **kw)


def crowd(n=6, spacing=1.05, scale=0.5, color=CHALK):
    g = VGroup(*[StickFigure(f"", color, scale=scale) for _ in range(n)])
    g.arrange(RIGHT, buff=spacing * scale)
    return g
