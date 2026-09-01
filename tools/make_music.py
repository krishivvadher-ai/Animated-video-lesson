"""Original background score, synthesised from scratch with numpy.

No sample, loop or recording is used: every note is generated here. Six cues,
written to the shape of the argument, sparse and slow, with the opening motif
returning at the end.
"""
import numpy as np
from scipy.io import wavfile
from pathlib import Path

SR = 44100
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "audio" / "music"
OUT.mkdir(parents=True, exist_ok=True)


def note(freq, dur, amp=0.25, attack=0.55, release=1.8, detune=0.004):
    n = int(SR * (dur + release))
    t = np.linspace(0, dur + release, n, endpoint=False)
    # a soft bell/pad: a few partials, gently detuned, all low
    w = np.zeros(n)
    for k, g in ((1, 1.0), (2, 0.28), (3, 0.11), (4, 0.05)):
        w += g * np.sin(2 * np.pi * freq * k * (1 + detune * (k - 1)) * t)
        w += 0.4 * g * np.sin(2 * np.pi * freq * k * (1 - detune * k) * t)
    env = np.ones(n)
    a = int(SR * attack)
    env[:a] = np.linspace(0, 1, a) ** 1.6
    r = int(SR * release)
    env[-r:] = np.linspace(1, 0, r) ** 2.2
    body = int(SR * dur)
    env[a:body] *= np.linspace(1.0, 0.72, max(0, body - a))
    return w * env * amp / 2.4


def render(events, length):
    """events: (start_seconds, midi, duration, amplitude)"""
    buf = np.zeros(int(SR * length) + SR * 8)
    for start, midi, dur, amp in events:
        f = 440.0 * 2 ** ((midi - 69) / 12.0)
        w = note(f, dur, amp)
        i = int(start * SR)
        j = min(i + len(w), len(buf))
        if j > i:
            buf[i:j] += w[:j - i]
    return buf[:int(SR * length)]


def write(name, buf, target_peak=0.5):
    peak = float(np.max(np.abs(buf))) or 1.0
    buf = buf / peak * target_peak
    # gentle low-pass so nothing in the music competes with speech
    k = 220
    kernel = np.hanning(k) / np.hanning(k).sum()
    buf = np.convolve(buf, kernel, mode="same")
    wavfile.write(str(OUT / f"{name}.wav"), SR, (buf * 32767).astype(np.int16))
    return len(buf) / SR


# The opening motif -- five notes, unresolved. Everything else is built from it.
MOTIF = [0, 7, 3, 10, 5]          # scale degrees, A minor pentatonic-ish
MINOR = [0, 2, 3, 5, 7, 8, 10]


def deg(root, d):
    return root + 12 * (d // 7) + MINOR[d % 7]


def cue(name, length, root=45, pace=6.4, amp=0.22, density=1.0, resolve=False,
        seed=1, bass=True):
    rng = np.random.default_rng(seed)
    ev = []
    t = 0.0
    i = 0
    while t < length:
        d = MOTIF[i % len(MOTIF)] + (0 if not resolve else 0)
        m = deg(root + 12, d)
        if rng.random() < density:
            ev.append((t, m, pace * 0.9, amp))
        if bass and i % 4 == 0:
            ev.append((t, root - 12 + (0 if (i // 4) % 2 == 0 else 5),
                       pace * 2.4, amp * 0.55))
        if rng.random() < 0.35 * density:
            ev.append((t + pace * 0.5, deg(root + 24, MOTIF[(i + 2) % 5]),
                       pace * 0.7, amp * 0.42))
        t += pace
        i += 1
    if resolve:
        ev.append((max(0.0, length - 9.0), deg(root + 12, 0), 8.0, amp * 1.15))
        ev.append((max(0.0, length - 9.0), deg(root, 0), 8.0, amp * 0.7))
        ev.append((max(0.0, length - 9.0), deg(root + 12, 4), 8.0, amp * 0.6))
    return write(name, render(ev, length))


if __name__ == "__main__":
    cues = [
        ("open",   180, dict(root=45, pace=6.0, amp=0.23, density=1.0, seed=1)),
        ("build",  180, dict(root=45, pace=7.2, amp=0.20, density=0.85, seed=2)),
        ("turn",   180, dict(root=43, pace=7.8, amp=0.21, density=0.8, seed=3)),
        ("policy", 180, dict(root=48, pace=8.4, amp=0.19, density=0.75, seed=4)),
        ("doubt",  180, dict(root=41, pace=9.6, amp=0.18, density=0.6, seed=5)),
        ("close",  180, dict(root=45, pace=6.0, amp=0.23, density=1.0, seed=1,
                             resolve=True)),
    ]
    for name, length, kw in cues:
        d = cue(name, length, **kw)
        print(f"{name}: {d:.1f}s")
