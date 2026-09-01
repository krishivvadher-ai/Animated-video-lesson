"""Build the three parts and the complete film: concat, subtitles, music, mix."""
import json, subprocess, sys, os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
SUBS = BUILD / "subs"
FINAL = ROOT / "final"
MUSIC = ROOT / "audio" / "music"
FINAL.mkdir(exist_ok=True)

QUAL = os.environ.get("QUAL", "1080p30")

PARTS = {
    "part-one":   (list(range(0, 22)),  "Part One — The Paper",
                   "Avinash Dixit, ‘Investment and Hysteresis’ (1992)",
                   [("open", 0, 2), ("build", 2, 14), ("turn", 14, 22)]),
    "part-two":   (list(range(22, 33)), "Part Two — The Policy",
                   "Bowdler & Radia, ‘Unconventional Monetary Policy’ (2012)",
                   [("policy", 22, 33)]),
    "part-three": (list(range(33, 44)), "Part Three — The Argument",
                   "The gap at the last link",
                   [("doubt", 33, 43), ("close", 43, 44)]),
}


def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode:
        print("FAILED:", cmd)
        print(r.stderr[-3000:])
        sys.exit(1)
    return r.stdout


def chapter_path(n):
    return BUILD / "media" / "videos" / f"ch{n:02d}" / QUAL / f"ch{n:02d}.mp4"


def title_path(name):
    return BUILD / "media" / "videos" / "titles" / QUAL / f"{name}.mp4"


def duration(p):
    return float(run(f'ffprobe -v error -show_entries format=duration -of csv=p=0 "{p}"').strip())


SUB_LINE = 46          # characters per subtitle line
SUB_MAX_LINES = 2


def split_cue(text, start, end):
    """One narrated line becomes as many two-line captions as it needs, timed
    in proportion to their length. A caption never runs to three lines."""
    words = text.split()
    limit = SUB_LINE * SUB_MAX_LINES
    chunks, cur = [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > limit:
            chunks.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        chunks.append(cur)
    total = sum(len(c) for c in chunks) or 1
    out, t = [], start
    span = max(end - start, 0.4)
    for c in chunks:
        d = span * len(c) / total
        out.append((t, min(t + d, end), wrap_sub(c)))
        t += d
    return out


def wrap_sub(text):
    """Wrap one caption to at most two lines."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > SUB_LINE:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return "\n".join(lines[:SUB_MAX_LINES]) if len(lines) <= SUB_MAX_LINES \
        else "\n".join([lines[0], " ".join(lines[1:])])


def ts(sec):
    h = int(sec // 3600); m = int(sec % 3600 // 60); s = sec % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")


def build_part(name):
    chapters, title, subtitle, cues = PARTS[name]
    files = [title_path({"part-one": "titles_one", "part-two": "titles_two",
                         "part-three": "titles_three"}[name])] + \
            [chapter_path(n) for n in chapters]
    if name == "part-one":
        files.insert(0, title_path("titles_film"))
    if name == "part-three":
        files.append(title_path("titles_end"))
    missing = [f for f in files if not f.exists()]
    if missing:
        print("missing:", missing); sys.exit(1)

    # ---- concat
    lst = BUILD / f"{name}.txt"
    lst.write_text("".join(f"file '{f}'\n" for f in files))
    novo = FINAL / f"{name}-novo.mp4"
    run(f'ffmpeg -y -v error -f concat -safe 0 -i "{lst}" -c copy "{novo}"')

    # ---- subtitles, with cumulative offsets
    lines, idx, offset = [], 1, 0.0
    head = len(files) - len(chapters) - (1 if name == "part-three" else 0)
    offset = sum(duration(f) for f in files[:head])
    for n, f in zip(chapters, files[head:]):
        cue_file = SUBS / f"ch{n:02d}.json"
        if cue_file.exists():
            data = json.loads(cue_file.read_text())
            for c in data["cues"]:
                for a, b, txt in split_cue(c["text"], offset + c["start"],
                                           offset + c["end"]):
                    lines.append(f"{idx}\n{ts(a)} --> {ts(b)}\n{txt}\n")
                    idx += 1
        offset += duration(f)
    srt = FINAL / f"{name}.srt"
    srt.write_text("\n".join(lines))

    total = offset
    print(f"{name}: {total/60:.1f} min, {idx-1} subtitle cues")

    # ---- music bed: lay the cues end to end for this part's length
    bed = BUILD / f"{name}-music.wav"
    seg_files, filters, concat_in = [], [], []
    # work out where each cue starts and ends, in seconds
    marks = []
    acc = sum(duration(f) for f in files[:head])
    starts = {}
    for n, f in zip(chapters, files[head:]):
        starts[n] = acc
        acc += duration(f)
    for i, (cue, a, b) in enumerate(cues):
        s = starts.get(a, 0.0)
        e = starts.get(b, total) if b in starts else total
        marks.append((cue, s, max(e - s, 1.0)))
    inputs = " ".join(f'-i "{MUSIC / (c + ".wav")}"' for c, _, _ in marks)
    fl = []
    for i, (c, s, d) in enumerate(marks):
        fl.append(f"[{i}:a]aloop=loop=-1:size=2e9,atrim=0:{d:.2f},"
                  f"afade=t=in:st=0:d=3,afade=t=out:st={max(d-4,0):.2f}:d=4[m{i}]")
    fl.append("".join(f"[m{i}]" for i in range(len(marks))) +
              f"concat=n={len(marks)}:v=0:a=1[bed]")
    run(f'ffmpeg -y -v error {inputs} -filter_complex "{";".join(fl)}" '
        f'-map "[bed]" -ac 2 -ar 44100 "{bed}"')

    # ---- mix: music far under the voice, ducked by the voice itself
    out = FINAL / f"{name}.mp4"
    run(f'ffmpeg -y -v error -i "{novo}" -i "{bed}" -filter_complex '
        f'"[1:a]volume=0.13[m];'
        f'[0:a]aformat=channel_layouts=stereo,asplit=2[voice][key];'
        f'[m][key]sidechaincompress=threshold=0.04:ratio=8:attack=15:release=450[mduck];'
        f'[voice][mduck]amix=inputs=2:duration=first:normalize=0,'
        f'afade=t=in:st=0:d=3,afade=t=out:st={max(total-4,0):.2f}:d=4[out]" '
        f'-map 0:v -map "[out]" -c:v copy -c:a aac -b:a 192k "{out}"')

    # ---- burned-in subtitle cut
    # The picture keeps all 1080 of its lines. A 200-pixel band is added
    # underneath it and the captions are drawn into that band, so a caption
    # can never sit on top of a diagram, a label or a figure.
    sub_out = FINAL / f"{name}-subtitled.mp4"
    band = 200
    style = ("FontName=CMU Serif,FontSize=30,PrimaryColour=&H00FFFFFF,"
             "OutlineColour=&H00000000,BackColour=&H00000000,BorderStyle=1,"
             "Outline=0,Shadow=0,Alignment=2,MarginV=34,MarginL=90,MarginR=90")
    run(f'ffmpeg -y -v error -i "{out}" -vf '
        f'"pad=iw:ih+{band}:0:0:color=black,'
        f'subtitles={srt}:force_style=\'{style}\'" '
        f'-c:a copy -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p '
        f'"{sub_out}"')
    return total


if __name__ == "__main__":
    tot = 0
    for name in PARTS:
        tot += build_part(name)
    lst = FINAL / "all.txt"
    lst.write_text("".join(f"file '{FINAL / (n + '.mp4')}'\n" for n in PARTS))
    run(f'ffmpeg -y -v error -f concat -safe 0 -i "{lst}" -c copy "{FINAL}/film-complete.mp4"')
    lst2 = FINAL / "all-sub.txt"
    lst2.write_text("".join(f"file '{FINAL / (n + '-subtitled.mp4')}'\n" for n in PARTS))
    run(f'ffmpeg -y -v error -f concat -safe 0 -i "{lst2}" -c copy "{FINAL}/film-complete-subtitled.mp4"')
    print(f"TOTAL {tot/60:.1f} min")
