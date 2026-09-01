"""The checks in section 9 of the brief, run as a script."""
import ast, json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CH = ROOT / "chapters"
DOCS = ROOT / "docs"
BUILD = ROOT / "build"
FINAL = ROOT / "final"
SUBS = BUILD / "subs"

EXCLUDED = ["Sharpe", "Suarez", "Penrose", "Wallace", "Jagannathan",
            "Reserve Bank of Australia", "Gormsen", "Huber", "Fabo", "De Luigi",
            "House of Lords", "Eggertsson", "Woodford", "Tobin", "Brunner",
            "Meltzer", "Vayanos", "Vila", "Yellen", "Joyce", "Bean", "Congdon",
            "Krugman", "Modigliani", "Miller", "Ricardian", "Bagehot", "Farmer",
            "Breedon", "Chadha", "Waters", "Cobham", "Allen", "Cour-Thimann",
            "Winkler", "Goodhart", "Ashworth", "Sinclair", "Ellis", "Summers",
            "Marshall,", "Black", "Scholes", "Brownian", "smooth pasting",
            "Hamermesh", "Soss", "Micawber", "Nalebuff", "Dertouzas", "Pindyck",
            "McDonald", "Siegel", "Leahy", "Stiglitz", "Mankiw", "Akerlof",
            "Bentolila", "Bertola", "Baldwin", "Frankel", "Meese", "Schwartz"]
ALLOWED_MENTION = ["Bernanke"]   # only ever as "Dixit, quoting Bernanke"

TERMS = None


def spoken_and_shown():
    """Return (all spoken text, all on-screen text) as one string each."""
    spoken, shown = [], []
    for p in sorted(CH.glob("ch*.py")):
        tree = ast.parse(p.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr in ("narrate", "line") and node.args:
                    try:
                        v = ast.literal_eval(node.args[0])
                        if isinstance(v, str):
                            spoken.append(v)
                    except Exception:
                        pass
                if node.func.attr == "define":
                    for a in node.args[:2]:
                        try:
                            v = ast.literal_eval(a)
                            if isinstance(v, str):
                                shown.append(v)
                        except Exception:
                            pass
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                shown.append(node.value)
    return "\n".join(spoken), "\n".join(shown)


def check_attribution(spoken, shown):
    text = spoken + "\n" + shown
    hits = []
    for name in EXCLUDED:
        # whole words only: "Farmers absorb years of losses" is the occupation,
        # not the economist, and "Miller" must not fire on "Millers"
        pat = re.escape(name) if not name[-1].isalpha() \
            else r"\b" + re.escape(name) + r"\b"
        if re.search(pat, text):
            hits.append(name)
    print("\n== attribution check ==")
    if hits:
        print("  EXCLUDED NAMES PRESENT:", sorted(set(hits)))
    else:
        print("  0 hits for every excluded name. PASS")
    for name in ALLOWED_MENTION:
        n = text.count(name)
        ctx = re.findall(r".{0,40}" + name + r".{0,20}", text)
        print(f"  {name}: {n} mention(s)")
        for c in ctx:
            print("     …" + c.replace("\n", " ") + "…")
    return not hits


def check_screen_prose():
    """No paragraphs on screen.

    This reads the text that was actually put on screen during the render --
    captured by the Chapter base class -- rather than guessing from the source,
    so narration can never be mistaken for a caption.
    """
    LIMIT = 82
    ALLOWED = (
        "Waiting lets her avoid the downside",          # ch 5, the film's key sentence
        "of possible future outcomes",                  # hinge quotation 1
        "This fall in the cost of capital",             # hinge quotation 2
        "Their spending plans should therefore",        # hinge quotation 3
        "QE has proved effective in limiting",          # hinge quotation 4
        "increased GDP growth by around",
        "has proved effective in limiting",
        "QE, by itself, is not strong enough",
        "significant periods of supernormal",
        "Quantitative easing is not a weaker version",  # ch 30, the key sentence
    )
    bad = []
    for f in sorted(SUBS.glob("ch*.json")):
        data = json.loads(f.read_text())
        for t in data.get("screen_text", []):
            flat = " ".join(t.split())
            # Manim reports a Text's content with its spaces stripped, so the
            # comparison has to ignore spacing on both sides
            squashed = re.sub(r"\s+", "", flat).lstrip("\u201c\u2018\"'")
            allowed = tuple(re.sub(r"\s+", "", a).lstrip("\u201c\u2018\"'")
                            for a in ALLOWED)
            if len(flat) > LIMIT and not squashed.startswith(allowed):
                bad.append((f.stem, flat[:74]))
    print("\n== on-screen prose check ==")
    print(f"  captions over {LIMIT} characters on screen: {len(bad)}")
    for f, t in bad[:25]:
        print("   ", f, repr(t))
    return len(bad)


def check_terms(spoken):
    """Every defined term must not be used before its own chapter."""
    defs = {}
    order = []
    for p in sorted(CH.glob("ch*.py")):
        n = int(p.stem[2:])
        tree = ast.parse(p.read_text())
        chapter_text = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr == "define" and node.args:
                    try:
                        t = ast.literal_eval(node.args[0])
                        if isinstance(t, str) and t not in defs:
                            defs[t] = n
                    except Exception:
                        pass
                if node.func.attr in ("narrate", "line") and node.args:
                    try:
                        v = ast.literal_eval(node.args[0])
                        if isinstance(v, str):
                            chapter_text.append(v)
                    except Exception:
                        pass
        order.append((n, " ".join(chapter_text).lower()))
    print("\n== term coverage check ==")
    problems = []
    for term, cn in defs.items():
        head = term.split(",")[0].split(" or ")[0].strip().lower()
        if len(head.split()) > 3 or head in ("the trigger", "the chance keeps"):
            continue
        # a term whose head word was already defined earlier is not a new term
        earlier = [c for t2, c in defs.items()
                   if t2 != term and t2.split(",")[0].strip().lower() == head]
        if earlier and min(earlier) < cn:
            continue
        for n, text in order:
            if n < cn and re.search(r"\b" + re.escape(head) + r"\b", text):
                problems.append((term, cn, n))
                break
    if problems:
        for t, cn, n in problems:
            print(f"  '{t}' defined in ch{cn} but used in ch{n}")
    else:
        print(f"  {len(defs)} terms, none used before its own chapter. PASS")
    return problems


def check_numbers():
    print("\n== number check ==")
    txt = (DOCS / "2012-investment-and-hysteresis.txt").read_text()
    mm = (DOCS / "Group 5 - Quantitative Easing - A Sceptical Survey.txt").read_text()
    br = (DOCS / "Background Reading - Unconventional Monetary Policy - The Assessment.txt").read_text()
    checks = [
        ("1.86", txt), ("9.3", txt), ("2.61", txt), ("3.32", txt), ("16.6", txt),
        ("13.6", txt), ("3.9", txt), ("0.72", txt), ("1.62", txt), ("1.1", txt),
        ("2.15", txt), ("1.62", txt), ("1.58", txt), ("$6,000", txt),
        ("13,500", txt), ("8 to 30 percent", txt), ("median of 15", txt),
        ("mean of 17", txt), ("50 percent", txt),
        ("1–3 per cent", mm), ("200–300 bp", mm), ("tentative", mm),
        ("unsecured", mm),
        ("incentives to borrow", br), ("cyclical movements", br),
        ("375 billion", br), ("30 per cent", br),
    ]
    missing = []
    for needle, hay in checks:
        if needle not in hay:
            missing.append(needle)
    for needle, hay in checks:
        mark = "ok " if needle not in missing else "MISS"
        print(f"  [{mark}] {needle}")
    return missing


def check_sync():
    print("\n== sync check ==")
    bad = []
    for p in sorted((BUILD / "media" / "videos").glob("ch*")):
        f = list(p.glob("*/*.mp4"))
        if not f:
            continue
        f = f[0]
        out = subprocess.run(
            f'ffprobe -v error -show_entries stream=codec_type,duration '
            f'-of csv=p=0 "{f}"', shell=True, capture_output=True, text=True).stdout
        vals = {}
        for line in out.strip().splitlines():
            parts = line.split(",")
            if len(parts) == 2 and parts[1] not in ("N/A", ""):
                vals[parts[0]] = float(parts[1])
        if "video" in vals and "audio" in vals:
            d = abs(vals["video"] - vals["audio"])
            if d > 0.25:
                bad.append((p.name, round(d, 2)))
        elif "audio" not in vals:
            bad.append((p.name, "NO AUDIO"))
    if bad:
        for n, d in bad:
            print(f"  {n}: {d}")
    else:
        print("  every chapter has audio, matching video to within 0.25 s. PASS")
    return bad


if __name__ == "__main__":
    spoken, shown = spoken_and_shown()
    check_attribution(spoken, shown)
    check_screen_prose()
    check_terms(spoken)
    check_numbers()
    check_sync()
    check_durations()
    check_silences()
    check_audio()


def check_durations():
    print("\n== durations ==")
    total = 0.0
    parts = {"PART ONE": (0, 21), "PART TWO": (22, 32), "PART THREE": (33, 43)}
    for label, (a, b) in parts.items():
        sub = 0.0
        for n in range(a, b + 1):
            f = list((BUILD / "media" / "videos" / f"ch{n:02d}").glob("*/*.mp4"))
            if not f:
                print(f"  ch{n:02d}  MISSING")
                continue
            d = float(subprocess.run(
                f'ffprobe -v error -show_entries format=duration -of csv=p=0 "{f[0]}"',
                shell=True, capture_output=True, text=True).stdout.strip())
            print(f"  ch{n:02d}  {d/60:5.2f} min")
            sub += d
        print(f"  --- {label}: {sub/60:.1f} min")
        total += sub
    print(f"  === TOTAL (chapters only): {total/60:.1f} min")
    return total


def check_audio():
    print("\n== audio levels ==")
    for name in ("part-one", "part-two", "part-three"):
        f = FINAL / f"{name}.mp4"
        if not f.exists():
            print(f"  {name}: not built yet")
            continue
        out = subprocess.run(f'ffmpeg -v info -i "{f}" -af ebur128 -f null - 2>&1 | tail -22',
                             shell=True, capture_output=True, text=True).stdout
        i = re.search(r"I:\s+(-?[\d.]+) LUFS", out)
        p = re.search(r"Peak:\s+(-?[\d.]+) dBFS", out)
        print(f"  {name}: integrated {i.group(1) if i else '?'} LUFS, "
              f"true peak {p.group(1) if p else '?'} dBFS")


def check_silences():
    """The scripted silences must survive the mix."""
    print("\n== scripted silence check ==")
    want = {5: "the value of waiting lands",
            23: "the path falls back and she does not close",
            39: "Kit waits for a third shield",
            49: "the closing beat, after 'it is a boundary'"}
    for n, why in want.items():
        f = list((BUILD / "media" / "videos" / f"ch{n:02d}").glob("*/*.mp4"))
        if not f:
            print(f"  ch{n:02d}: not rendered"); continue
        out = subprocess.run(
            f'ffmpeg -v info -i "{f[0]}" -af silencedetect=n=-45dB:d=2.4 -f null - 2>&1 '
            f'| grep silence_duration | head -4', shell=True,
            capture_output=True, text=True).stdout.strip()
        found = len(out.splitlines())
        print(f"  ch{n:02d} ({why}): {found} silence(s) of 2.4 s or more "
              f"{'PASS' if found else 'CHECK'}")
