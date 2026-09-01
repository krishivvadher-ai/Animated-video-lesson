"""Frame audit: pull evenly-spaced frames from every chapter and check them
mechanically for text running off screen and for empty frames."""
import subprocess, sys
from pathlib import Path
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build" / "media" / "videos"
OUT = ROOT / "build" / "frames"
OUT.mkdir(parents=True, exist_ok=True)

BG = (14, 20, 32)


def frames_for(mp4, n=5):
    d = float(subprocess.run(
        f'ffprobe -v error -show_entries format=duration -of csv=p=0 "{mp4}"',
        shell=True, capture_output=True, text=True).stdout.strip())
    out = []
    for i in range(n):
        t = d * (i + 0.5) / n
        p = OUT / f"{mp4.parent.parent.name}_{i}.png"
        subprocess.run(f'ffmpeg -y -v error -ss {t:.2f} -i "{mp4}" -frames:v 1 "{p}"',
                       shell=True)
        out.append(p)
    return out


def audit(p):
    im = np.asarray(Image.open(p).convert("RGB")).astype(int)
    h, w, _ = im.shape
    diff = np.abs(im - np.array(BG)).sum(axis=2)
    ink = diff > 40
    m = max(2, int(w * 0.012))
    edges = {
        "left": ink[:, :m].sum(), "right": ink[:, -m:].sum(),
        "top": ink[:m, :].sum(), "bottom": ink[-m:, :].sum(),
    }
    coverage = ink.mean()
    return coverage, edges


if __name__ == "__main__":
    bad, empty = [], []
    for d in sorted(BUILD.glob("ch*")):
        mp4 = list(d.glob("*/*.mp4"))
        if not mp4:
            continue
        for f in frames_for(mp4[0]):
            cov, edges = audit(f)
            if cov < 0.0015:
                empty.append((f.name, round(cov, 5)))
            hot = {k: int(v) for k, v in edges.items() if v > 260}
            if hot:
                bad.append((f.name, hot))
    print(f"\n== frame audit ==  {len(list(OUT.glob('*.png')))} frames looked at")
    print(f"  frames with ink in the outer 1.2% of the frame: {len(bad)}")
    for n, e in bad[:25]:
        print("   ", n, e)
    print(f"  near-empty frames: {len(empty)}")
    for n, c in empty[:25]:
        print("   ", n, c)
