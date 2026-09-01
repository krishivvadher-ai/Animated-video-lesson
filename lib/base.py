"""The Chapter scene base: narration, subtitles, title card, recap, progress."""
import json
import os
from contextlib import contextmanager
from pathlib import Path

from manim import (
    ThreeDScene, VGroup, VMobject, FadeIn, FadeOut, Write, Create, Text, MarkupText,
    Line, DashedLine, Arrow, Polygon, Circle, Rectangle, RoundedRectangle,
    DrawBorderThenFill, config, UP, DOWN, LEFT, RIGHT, ORIGIN,
)


def _all_text(m):
    """True for a Text, or a group made only of Text."""
    if isinstance(m, (Text, MarkupText)):
        return True
    if isinstance(m, VGroup) and len(m) > 0:
        return all(_all_text(s) for s in m)
    return False


def _outline_only(m):
    """A stroked shape with no fill -- the kind that reads well drawn on."""
    if isinstance(m, (Line, DashedLine, Arrow)):
        return True
    if isinstance(m, VGroup) and 0 < len(m) <= 8:
        return all(_outline_only(s) for s in m)
    return False
from lib import cards, voice
from lib.theme import (
    BG, CHALK, MUTED, FONT, T_BODY, BEAT, PAD, CARD_HOLD, apply,
)

ROOT = Path(__file__).resolve().parent.parent
SUBDIR = ROOT / "build" / "subs"
SUBDIR.mkdir(parents=True, exist_ok=True)

apply()


class Chapter(ThreeDScene):
    """One chapter. Subclasses set CH/TITLE/PART and implement body()."""

    CH = 0
    TITLE = ""
    PART = "PART ONE — THE PAPER"

    def setup(self):
        self.cues = []
        self.screen_text = []
        self._progress = None

    def _record(self, *mobs):
        """Record every word that actually reaches the screen, for the audit."""
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

    # ------------------------------------------------------------ house style
    def play(self, *anims, **kw):
        """3Blue1Brown's defaults, applied to every animation in the film.

        Short labels are written on. Outlines are drawn on. Anything with
        several parts arrives staggered rather than all at once. Everything
        that fades drifts a little as it goes -- his `FadeIn(mob, UP)`.
        """
        from manim import LaggedStartMap
        from lib.theme import LAG
        out = []
        rt = kw.get("run_time")
        for a in anims:
            m = getattr(a, "mobject", None)
            if type(a) is FadeIn and m is not None:
                short = _all_text(m) and len(str(getattr(m, "text", "x" * 200))) <= 90
                if short:
                    out.append(Write(m, run_time=rt) if rt else Write(m))
                    continue
                if _outline_only(m):
                    out.append(Create(m, run_time=rt) if rt else Create(m))
                    continue
                if isinstance(m, VGroup) and 2 < len(m) <= 14:
                    out.append(LaggedStartMap(FadeIn, m, shift=UP * 0.22,
                                              lag_ratio=LAG,
                                              **({"run_time": rt} if rt else {})))
                    continue
                out.append(FadeIn(m, shift=UP * 0.22,
                                  **({"run_time": rt} if rt else {})))
                continue
            if type(a) is FadeOut and m is not None:
                out.append(FadeOut(m, shift=DOWN * 0.12,
                                   **({"run_time": rt} if rt else {})))
                continue
            out.append(a)
        self._record(*[getattr(a, "mobject", None) for a in out])
        return super().play(*out, **kw)

    def add(self, *mobs):
        self._record(*mobs)
        return super().add(*mobs)

    # ------------------------------------------------------------ narration
    @contextmanager
    def narrate(self, text, v="n", pad=PAD):
        """Speak a line; the animations inside the block run underneath it."""
        path, dur = voice.speak(text, v)
        t0 = self.renderer.time
        self.add_sound(path)
        self.cues.append({"start": t0, "end": t0 + dur, "text": text, "voice": v})
        yield dur
        used = self.renderer.time - t0
        if used < dur + pad - 1e-3:
            self.wait(dur + pad - used)

    def line(self, text, v="n", pad=PAD):
        """Speak with nothing happening on screen (use sparingly)."""
        with self.narrate(text, v, pad):
            pass

    def beat(self, t=BEAT):
        """A full beat of silence -- after a new term, after a number."""
        if t > 1e-3:
            self.wait(t)

    # ------------------------------------------------------------ furniture
    def open_chapter(self, subtitle=None):
        from manim import Write, GrowFromCenter, Line, LEFT, RIGHT
        card = cards.title_card(self.CH, self.TITLE, self.PART)
        num, rule, title = card[0], card[1], card[2]
        self.play(FadeIn(num, shift=DOWN * 0.2), run_time=0.6)
        self.play(GrowFromCenter(rule), run_time=0.5)
        self.play(Write(title), run_time=1.4)
        if len(card) > 3:
            self.play(FadeIn(card[3]), run_time=0.5)
        self.wait(1.1)
        self.play(FadeOut(card, shift=UP * 0.25), run_time=0.7)
        self._progress = cards.progress(self.CH)
        self.add(self._progress)
        # the indicator belongs to the screen, not to the scene's 3D space
        self.add_fixed_in_frame_mobjects(self._progress)

    RECAP_ICONS = None

    def close_chapter(self, bullets, heading="What we just established", icons=None):
        self.clear_stage()
        icons = icons or self.RECAP_ICONS
        panel = cards.recap_panel(bullets, heading, icons)
        panel.move_to(ORIGIN)
        if panel.height > 5.4:
            panel.scale(5.4 / panel.height)
        from manim import GrowFromCenter, Write
        self.play(FadeIn(panel[0], shift=DOWN * 0.2), run_time=0.5)
        for i, row in enumerate(panel[1]):
            with self.narrate(bullets[i], pad=0.15):
                self.play(GrowFromCenter(row[0]), run_time=0.35)
                self.play(Write(row[1]), run_time=0.7)
        self.wait(0.9)
        self.play(FadeOut(panel), run_time=0.7)
        if self._progress:
            self.play(FadeOut(self._progress), run_time=0.3)
        self.wait(0.35)

    # ------------------------------------------------------------ camera
    def push_in(self, mob, zoom=1.9, run_time=1.6):
        """Move the camera in on one thing -- the house move for a key beat."""
        c = mob.get_center()
        self.move_camera(zoom=zoom, frame_center=[c[0], c[1], 0], run_time=run_time)

    def pull_back(self, run_time=1.4):
        self.move_camera(zoom=1.0, frame_center=[0, 0, 0], run_time=run_time)

    def spotlight(self, keep, run_time=0.7, dim=0.22):
        """Dim everything except one thing -- the house move for a hard beat."""
        keep_ids = {id(m) for m in (keep if isinstance(keep, (list, tuple)) else [keep])}
        if self._progress is not None:
            keep_ids.add(id(self._progress))
        others = [m for m in self.mobjects if id(m) not in keep_ids]
        if others:
            self.play(*[m.animate.set_opacity(dim) for m in others], run_time=run_time)
        return others

    def unspotlight(self, others, run_time=0.6):
        if others:
            self.play(*[m.animate.set_opacity(1.0) for m in others], run_time=run_time)

    def flash(self, mob, color=None, run_time=1.2):
        """Draw the eye to something already on screen."""
        from manim import Circumscribe
        from lib.theme import CHALK as _C
        self.play(Circumscribe(mob, color=color or _C, buff=0.18,
                               stroke_width=4), run_time=run_time)

    def morph(self, a, b, run_time=1.4):
        """One thing becomes another, rather than one leaving and another arriving."""
        from manim import ReplacementTransform
        self.play(ReplacementTransform(a, b), run_time=run_time)
        return b

    def clear_stage(self, keep=None):
        keep = keep or []
        keepers = set(id(m) for m in keep)
        if self._progress is not None:
            keepers.add(id(self._progress))
        junk = [m for m in self.mobjects if id(m) not in keepers]
        if junk:
            self.play(*[FadeOut(m) for m in junk], run_time=0.5)

    # ------------------------------------------------------------ cards
    def define(self, term, definition, icon_kind=None, color=CHALK,
               narration=None, hold=CARD_HOLD, at=ORIGIN):
        """Every technical term gets a card before it is used in a sentence."""
        card = cards.definition_card(term, definition, icon_kind, color)
        if card.width > 12.4:
            card.scale(12.4 / card.width)
        card.move_to(at)
        self.play(FadeIn(card, scale=0.96), run_time=0.6)
        spoken = narration or f"{term}. {definition}"
        with self.narrate(spoken):
            pass
        self.beat()
        rest = hold - 3.0
        if rest > 1e-3:
            self.wait(rest)
        self.play(FadeOut(card), run_time=0.5)

    def show(self, mob, t=1.0, anim=None):
        self.play(anim or FadeIn(mob), run_time=t)

    # ------------------------------------------------------------ output
    def tear_down(self):
        pass

    def construct(self):
        self.open_chapter()
        self.body()
        self._write_cues()

    def body(self):
        raise NotImplementedError

    def _write_cues(self):
        out = SUBDIR / f"ch{self.CH:02d}.json"
        out.write_text(json.dumps(
            {"chapter": self.CH, "title": self.TITLE,
             "duration": self.renderer.time, "cues": self.cues,
             "screen_text": sorted(set(self.screen_text))}, indent=1))
