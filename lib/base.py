"""The Chapter base: narration, subtitles, staging, and the rules.

Everything a scene needs, and three rules it cannot break:

* a caption over sixty characters raises (`lib.stage`),
* text scaled below the readable minimum raises (`lib.stage`),
* a narrated beat that plays no animation raises (here).

The animation defaults are 3Blue1Brown's, taken from his published video
source: short labels are written on, outlines are drawn on, anything with
parts arrives staggered, and everything that fades drifts as it goes.
"""
import json
from contextlib import contextmanager
from pathlib import Path

from manim import (
    ThreeDScene, VGroup, VMobject, Text, MarkupText, Line, DashedLine, Arrow,
    Polygon, Circle, Rectangle, RoundedRectangle, FadeIn, FadeOut, Write,
    Create, DrawBorderThenFill, LaggedStartMap, Transform, FadeTransform,
    config, UP, DOWN, LEFT, RIGHT, UL, UR, ORIGIN, DEGREES,
)
from lib import cards, voice, stage as St
from lib import style as S
from lib.theme import (
    BG, CHALK, MUTED, FONT, T_BODY, T_SUB, BEAT, PAD, CARD_HOLD, LAG, apply,
    OPACITY_CONTEXT,
)

ROOT = Path(__file__).resolve().parent.parent
SUBDIR = ROOT / "build" / "subs"

DIMMED = 0.22          # what the rest of the scene fades to behind a card
SUBDIR.mkdir(parents=True, exist_ok=True)

apply()


def _all_text(m):
    if isinstance(m, (Text, MarkupText)):
        return True
    if isinstance(m, VGroup) and len(m) > 0:
        return all(_all_text(s) for s in m)
    return False


def _outline_only(m):
    if isinstance(m, (Line, DashedLine, Arrow)):
        return True
    if isinstance(m, VGroup) and 0 < len(m) <= 8:
        return all(_outline_only(s) for s in m)
    return False


def _drawable(m):
    try:
        if m.get_num_points() > 0:
            return True
        return any(sub.get_num_points() > 0 for sub in m.get_family())
    except Exception:
        return False


class Chapter(ThreeDScene):
    """One chapter. Subclasses set CH / TITLE / PART and implement body()."""

    CH = 0
    TITLE = ""
    PART = "PART ONE — THE PAPER"
    RECAP_ICONS = None

    # ------------------------------------------------------------ lifecycle
    def setup(self):
        self.cues = []
        self.screen_text = []
        self.collisions = []
        self.low_content = []
        self.off_frame = []
        self.too_small = []
        self.silent_beats = []
        self._progress = None
        self._heading = None
        self._plays_in_beat = 0

    def construct(self):
        self.open_chapter()
        self.body()
        self._write_cues()

    def body(self):
        raise NotImplementedError

    # ------------------------------------------------------------ narration
    @contextmanager
    def narrate(self, text, v="n", pad=PAD, hold=False):
        """Speak a line. Something must move while it is spoken."""
        path, dur = voice.speak(text, v)
        t0 = self.renderer.time
        self.add_sound(path)
        self.cues.append({"start": t0, "end": t0 + dur, "text": text, "voice": v})
        before = self._plays_in_beat
        yield dur
        moved = self._plays_in_beat > before
        if not moved and not hold:
            self.silent_beats.append({"t": round(t0, 2), "text": text[:70]})
        used = self.renderer.time - t0
        if used < dur + pad - 1e-3:
            self.wait(dur + pad - used)

    def line(self, text, v="n", pad=PAD):
        """Narration over a held picture. Used sparingly and declared."""
        with self.narrate(text, v, pad, hold=True):
            pass

    def beat(self, t=BEAT):
        if t > 1e-3:
            self.wait(t)

    # ------------------------------------------------------------ house style
    def play(self, *anims, **kw):
        from lib.theme import LAG as _LAG
        out = []
        rt = kw.get("run_time")
        for a in anims:
            m = getattr(a, "mobject", None)
            if type(a) is FadeIn and m is not None:
                if _all_text(m) and len(str(getattr(m, "text", "x" * 200))) <= 90:
                    out.append(Write(m, run_time=rt) if rt else Write(m))
                    continue
                if _outline_only(m):
                    out.append(Create(m, run_time=rt) if rt else Create(m))
                    continue
                if (isinstance(m, VGroup) and 2 < len(m) <= 14
                        and all(_drawable(sub) for sub in m)):
                    out.append(S.lag_map(FadeIn, m, shift=UP * 0.25, lag=_LAG,
                                         run_time=rt))
                    continue
                out.append(FadeIn(m, shift=UP * 0.5,
                                  **({"run_time": rt} if rt else {})))
                continue
            if type(a) is FadeOut and m is not None:
                out.append(FadeOut(m, shift=DOWN * 0.12,
                                   **({"run_time": rt} if rt else {})))
                continue
            out.append(a)
        self._plays_in_beat += 1
        self._record(*[getattr(a, "mobject", None) for a in out])
        result = super().play(*out, **kw)
        self._check_layout()
        return result

    def add(self, *mobs):
        self._record(*mobs)
        return super().add(*mobs)

    # ------------------------------------------------------------ staging
    def heading(self, text, colour=CHALK, run_time=1.2):
        """Put a section heading up, morphing from the one before it."""
        new = St.heading(text, colour)
        if self._heading is None:
            self.play(Write(new[0]), run_time=run_time * 0.8)
            self.play(Create(new[1]), run_time=0.5)
        else:
            self.play(FadeTransform(self._heading, new), run_time=run_time)
        self._heading = new
        return new

    def drop_heading(self):
        if self._heading is not None:
            self.play(FadeOut(self._heading), run_time=0.5)
            self._heading = None

    def show(self, mob, region=St.FULL, ax=0.0, ay=0.0, anim=None, run_time=1.0,
             pad=0.25):
        """Place a thing in a region and bring it on."""
        St.place(mob, region, ax, ay, pad)
        self.play(anim or FadeIn(mob), run_time=run_time)
        return mob

    def side(self, items, colour=CHALK, icons=None, size=T_BODY, width=20,
             dot_colour=None, spoken=None, region=St.SIDE):
        """A commentary column: short labels, one at a time, each narrated."""
        col = St.points(items, colour, size, width, dot_colour, icons)
        St.place(col, region)
        for i, row in enumerate(col):
            if spoken and i < len(spoken):
                with self.narrate(spoken[i]):
                    self.play(FadeIn(row), run_time=0.7)
            else:
                self.play(FadeIn(row), run_time=0.55)
        return col

    def foot(self, text, colour=CHALK, size=T_BODY, run_time=0.8):
        """One short line at the foot of the frame."""
        c = St.caption(text, colour, size, width=64)
        St.place(c, St.FOOT, pad=0.06)
        self.play(FadeIn(c), run_time=run_time)
        return c

    def park(self, mob, corner=UL, height=1.9, run_time=1.2, keep_text=False):
        """Shrink a finished diagram into a corner, the way he does.

        Its labels go first: at a third of the size they would be unreadable,
        and a parked diagram is a reminder of a shape, not a chart to read.
        """
        if not keep_text:
            labels = [x for x in mob.get_family()
                      if isinstance(x, Text)
                      and len(str(getattr(x, "text", "")).strip()) >= 3]
            if labels:
                self.play(*[FadeOut(x) for x in labels], run_time=0.45)
                for x in labels:
                    x._stage_ignore = True    # no longer on screen to be read
        # a parked diagram is context now, not the thing being said, so it
        # sits back to the contextual layer rather than competing at full weight
        self.play(St.park(mob, corner, height, run_time),
                  mob.animate.set_stroke(opacity=OPACITY_CONTEXT))
        return mob

    def clear_stage(self, keep=None):
        keep = keep or []
        keepers = {id(m) for m in keep}
        if self._progress is not None:
            keepers.add(id(self._progress))
        if self._heading is not None:
            keepers.add(id(self._heading))
        junk = [m for m in self.mobjects if id(m) not in keepers]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=0.5)

    # ------------------------------------------------------------ camera
    def push_in(self, mob, zoom=1.8, run_time=1.6):
        c = mob.get_center()
        self.move_camera(zoom=zoom, frame_center=[c[0], c[1], 0], run_time=run_time)

    def pull_back(self, run_time=1.4):
        self.move_camera(zoom=1.0, frame_center=[0, 0, 0], run_time=run_time)

    # ------------------------------------------------------------ cards
    def symbol_key(self, keys, hold=3.4, region=None, ax=0.0, ay=0.0):
        """Put the key to the symbols back on screen.

        Every Greek letter here is a squiggle standing for an English phrase.
        The phrase is what gets said out loud, and this is the reminder of
        which squiggle is which -- shown again whenever a new one joins."""
        key = cards.symbol_key(keys)
        St.place(key, region or St.SIDE, ax=ax, ay=ay, fill=False)
        self.play(S.lag_map(FadeIn, key, shift=RIGHT * 0.2, lag=0.12),
                  run_time=1.0)
        self.wait(max(hold - 1.0, 0.4))
        self.play(FadeOut(key), run_time=0.5)

    def define(self, term, definition, icon_kind=None, colour=CHALK,
               narration=None, hold=CARD_HOLD, at=ORIGIN):
        """Every technical term gets a card before it is used in a sentence."""
        St.check_caption(definition, St.MAX_DEFINITION)
        card = cards.definition_card(term, definition, icon_kind, colour)
        if card.width > 12.2:
            card.scale(12.2 / card.width)
        card.move_to(at)
        behind = [m for m in self.mobjects
                  if m is not self._progress and m not in card.get_family()]
        # set_opacity() sets fill as well as stroke, so an outline drawing that
        # is dimmed and then restored to 1.0 comes back as a filled silhouette.
        # Remember what each piece actually had, and put exactly that back.
        was = []
        for m in behind:
            for sub in m.get_family():
                try:
                    was.append((sub, sub.get_fill_opacity(),
                                sub.get_stroke_opacity()))
                except Exception:
                    pass          # a bare Mobject has neither
        if behind:
            self.play(*[m.animate.set_opacity(DIMMED) for m in behind],
                      run_time=0.4)
        self.play(DrawBorderThenFill(card[0]), run_time=0.7)
        self.play(FadeIn(card[1]), run_time=0.6)
        spoken = narration or f"{term}. {definition}"
        with self.narrate(spoken, hold=True):
            pass
        self.beat()
        rest = hold - 3.2
        if rest > 1e-3:
            self.wait(rest)
        if behind:
            self.play(FadeOut(card),
                      *[sub.animate.set_fill(opacity=fo).set_stroke(opacity=so)
                        for sub, fo, so in was if sub.get_num_points()],
                      run_time=0.5)
        else:
            self.play(FadeOut(card), run_time=0.5)

    # ------------------------------------------------------------ furniture
    def open_chapter(self):
        card = cards.title_card(self.CH, self.TITLE, self.PART)
        num, rule, title = card[0], card[1], card[2]
        self.play(FadeIn(num, shift=DOWN * 0.2), run_time=0.6)
        self.play(Create(rule), run_time=0.5)
        self.play(Write(title), run_time=1.4)
        if len(card) > 3:
            self.play(FadeIn(card[3]), run_time=0.5)
        self.wait(1.0)
        self.play(FadeOut(card, shift=UP * 0.25), run_time=0.7)
        self._progress = cards.progress(self.CH)
        self.add(self._progress)
        self.add_fixed_in_frame_mobjects(self._progress)

    def close_chapter(self, bullets, heading="What we just established",
                      icons=None):
        self._heading = None
        self.clear_stage()
        icons = icons or self.RECAP_ICONS
        for b in bullets:
            St.check_caption(b)
        panel = cards.recap_panel(bullets, heading, icons)
        St.place(panel, St.WIDE)
        from manim import GrowFromCenter
        self.play(FadeIn(panel[0], shift=DOWN * 0.2), run_time=0.5)
        for i, row in enumerate(panel[1]):
            with self.narrate(bullets[i], pad=0.15):
                self.play(GrowFromCenter(row[0]), run_time=0.35)
                self.play(Write(row[1]), run_time=0.7)
        self.wait(0.8)
        self.play(FadeOut(panel), run_time=0.7)
        if self._progress:
            self.play(FadeOut(self._progress), run_time=0.3)
        self.wait(0.3)

    # ------------------------------------------------------------ audits
    def _record(self, *mobs):
        for m in mobs:
            if m is None:
                continue
            try:
                fam = m.get_family()
            except Exception:
                continue
            for sub in fam:
                t = getattr(sub, "text", None)
                if isinstance(t, str) and t.strip():
                    self.screen_text.append(t)

    def _boxes(self):
        items = []
        for m in self.mobjects:
            if self._progress is not None and m is self._progress:
                continue
            for sub in ([m] if not isinstance(m, VGroup) else list(m)):
                try:
                    if sub.get_num_points() == 0 and not sub.submobjects:
                        continue
                    w, h = sub.width, sub.height
                    if w <= 0.01 or h <= 0.01:
                        continue
                    c = sub.get_center()
                except Exception:
                    continue
                try:
                    if max(sub.get_stroke_opacity(), sub.get_fill_opacity()) < 0.35:
                        continue
                except Exception:
                    pass
                txt = getattr(sub, "text", None)
                if txt is None and isinstance(sub, VGroup):
                    parts = [getattr(x, "text", None) for x in sub]
                    parts = [q for q in parts if isinstance(q, str)]
                    txt = " ".join(parts) if parts else None
                items.append((txt, (c[0] - w / 2, c[1] - h / 2,
                                    c[0] + w / 2, c[1] + h / 2),
                              isinstance(txt, str)))
        return items

    def _check_layout(self):
        items = self._boxes()
        t = round(self.renderer.time, 2)
        for label, b, is_text in items:
            if not is_text or not label or len(label.strip()) < 3:
                continue
            if b[1] < -3.98:
                self.low_content.append({"t": t, "text": label[:60],
                                         "bottom": round(b[1], 2)})
            # anything reaching past the edge of the frame is being cut in half
            if b[0] < -7.02 or b[2] > 7.02 or b[3] > 4.02:
                self.off_frame.append({"t": t, "text": label[:60],
                                       "box": [round(v, 2) for v in b]})
        for m in self.mobjects:
            if self._progress is not None and m is self._progress:
                continue   # the corner indicator is furniture, not a caption
            for sub in m.get_family():
                if getattr(sub, "_stage_ignore", False):
                    continue          # faded out before the diagram was parked
                fs = St.effective_font_size(sub)
                if fs is not None and fs < St.MIN_FONT - 0.5:
                    self.too_small.append(
                        {"t": t, "text": str(getattr(sub, "text", ""))[:52],
                         "font_size": round(fs, 1)})
        texts = [(l, b) for l, b, is_text in items
                 if is_text and l and len(l.strip()) >= 3]
        for i, (l1, b1) in enumerate(texts):
            for l2, b2 in texts[i + 1:]:
                ox = min(b1[2], b2[2]) - max(b1[0], b2[0])
                oy = min(b1[3], b2[3]) - max(b1[1], b2[1])
                if ox <= 0 or oy <= 0:
                    continue
                inter = ox * oy
                a1 = (b1[2] - b1[0]) * (b1[3] - b1[1])
                a2 = (b2[2] - b2[0]) * (b2[3] - b2[1])
                if inter > 0.30 * min(a1, a2):
                    self.collisions.append(
                        {"t": t, "a": (l1 or "")[:44], "b": (l2 or "")[:44],
                         "overlap": round(inter / max(min(a1, a2), 1e-6), 2)})

    def _write_cues(self):
        out = SUBDIR / f"ch{self.CH:02d}.json"
        out.write_text(json.dumps(
            {"chapter": self.CH, "title": self.TITLE,
             "duration": self.renderer.time, "cues": self.cues,
             "screen_text": sorted(set(self.screen_text)),
             "collisions": self.collisions[:200],
             "low_content": self.low_content[:200],
             "off_frame": self.off_frame[:200],
             "too_small": self.too_small[:200],
             "silent_beats": self.silent_beats[:200]}, indent=1))
