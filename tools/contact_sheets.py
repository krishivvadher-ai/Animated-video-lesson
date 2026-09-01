"""Contact sheets of every chapter, sampled where the picture has settled.

Frames are taken at the end of a narrated line rather than at even intervals,
because an even interval lands mid-animation about half the time and a
half-drawn diagram tells you nothing about whether the finished one is any
good."""
import json, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
OUT = BUILD / "sheets"
OUT.mkdir(parents=True, exist_ok=True)
FR = BUILD / "frames"
FR.mkdir(parents=True, exist_ok=True)

PER_CHAPTER = int(sys.argv[1]) if len(sys.argv) > 1 else 4
QUAL = sys.argv[2] if len(sys.argv) > 2 else "480p15"
TW, TH = 480, 270
COLS, ROWS = 3, 4


def settled_times(n, k):
    """k moments spread through the chapter, each just after a line ends."""
    f = BUILD / "subs" / f"ch{n:02d}.json"
    data = json.loads(f.read_text())
    cues = data["cues"]
    dur = data["duration"]
    if not cues:
        return [dur * (i + 0.5) / k for i in range(k)]
    picks = []
    for i in range(k):
        want = dur * (i + 0.7) / k
        best = min(cues, key=lambda c: abs(c["end"] - want))
        t = min(best["end"] + 0.25, dur - 0.2)
        picks.append(round(t, 2))
    return picks


def grab(n, times):
    mp4 = BUILD / "media" / "videos" / f"ch{n:02d}" / QUAL / f"ch{n:02d}.mp4"
    if not mp4.exists():
        return []
    out = []
    for i, t in enumerate(times):
        p = FR / f"c{n:02d}_{i}.png"
        subprocess.run(f'ffmpeg -y -v error -ss {t} -i "{mp4}" -frames:v 1 "{p}"',
                       shell=True)
        if p.exists():
            out.append((p, t))
    return out


def main():
    tiles = []
    for n in range(44):
        for p, t in grab(n, settled_times(n, PER_CHAPTER)):
            tiles.append((n, t, p))
    per = COLS * ROWS
    for s in range(0, len(tiles), per):
        batch = tiles[s:s + per]
        sheet = Image.new("RGB", (TW * COLS, TH * ROWS), (18, 18, 18))
        d = ImageDraw.Draw(sheet)
        for i, (n, t, p) in enumerate(batch):
            im = Image.open(p).convert("RGB").resize((TW, TH))
            x, y = TW * (i % COLS), TH * (i // COLS)
            sheet.paste(im, (x, y))
            d.rectangle([x, y, x + TW - 1, y + TH - 1], outline=(70, 70, 70))
            d.text((x + 6, y + 4), f"ch{n:02d} @{t:.0f}s", fill=(255, 220, 120))
        out = OUT / f"sheet{s // per:02d}.png"
        sheet.save(out)
        print(out, len(batch))


if __name__ == "__main__":
    main()
