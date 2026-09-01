"""Burn the captions into a copy of a finished master.

Kept separate from assembly so a caption change costs one encode rather than a
whole rebuild. The captions are drawn into a black band added below the
picture, so they can never sit on top of a diagram.

The script is written as ASS rather than handed to ffmpeg as SRT, because
ffmpeg converts an SRT at a script resolution of 384x288 and libass then scales
that up to the frame -- which multiplies any font size by about four and a half
and throws the text across the picture.
"""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FINAL = ROOT / "final"
BUILD = ROOT / "build"
BAND = 200


def ass_time(sec):
    h = int(sec // 3600); m = int(sec % 3600 // 60); s = sec % 60
    return f"{h:d}:{m:02d}:{s:05.2f}"


def srt_seconds(t):
    h, m, rest = t.strip().split(":")
    s, ms = rest.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def cues_from_srt(path):
    out = []
    for block in path.read_text().strip().split("\n\n"):
        rows = [r for r in block.splitlines() if r.strip()]
        if len(rows) < 3 or "-->" not in rows[1]:
            continue
        a, b = rows[1].split("-->")
        out.append((srt_seconds(a), srt_seconds(b), "\n".join(rows[2:])))
    return out


def build_ass(name, cues, w, h):
    margin_v = max((BAND - 108) // 2, 18)
    head = (
        "[Script Info]\n"
        "ScriptType: v4.00+\n"
        f"PlayResX: {w}\nPlayResY: {h}\n"
        "WrapStyle: 2\nScaledBorderAndShadow: yes\n\n"
        "[V4+ Styles]\n"
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, "
        "OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, "
        "ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
        "Alignment, MarginL, MarginR, MarginV, Encoding\n"
        "Style: Band,CMU Serif,44,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,"
        f"0,0,0,0,100,100,0,0,1,0,0,2,140,140,{margin_v},1\n\n"
        "[Events]\n"
        "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, "
        "Effect, Text\n")
    body = "".join(
        f"Dialogue: 0,{ass_time(a)},{ass_time(b)},Band,,0,0,0,,"
        f"{t.replace(chr(10), chr(92) + 'N')}\n" for a, b, t in cues)
    p = BUILD / f"{name}.ass"
    p.write_text(head + body)
    return p


def burn(name):
    master, srt = FINAL / f"{name}.mp4", FINAL / f"{name}.srt"
    if not master.exists() or not srt.exists():
        print(f"{name}: missing master or srt")
        return
    ass = build_ass(name, cues_from_srt(srt), 1920, 1080 + BAND)
    out = FINAL / f"{name}-subtitled.mp4"
    r = subprocess.run(
        f'ffmpeg -y -v error -i "{master}" -vf '
        f'"pad=iw:ih+{BAND}:0:0:color=black,subtitles={ass}" '
        f'-c:a copy -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p '
        f'"{out}"', shell=True, capture_output=True, text=True)
    print(f"{name}: {'OK' if r.returncode == 0 else 'FAILED'}")
    if r.returncode:
        print(r.stderr[-800:])


if __name__ == "__main__":
    for n in (sys.argv[1:] or ["part-one", "part-two", "part-three"]):
        burn(n)
