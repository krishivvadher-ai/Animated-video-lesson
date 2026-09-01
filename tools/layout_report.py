"""Report what the runtime layout audit recorded: captions that overlap, and
anything drawn low enough to sit under the caption band."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBS = ROOT / "build" / "subs"


def main():
    coll, low = [], []
    for f in sorted(SUBS.glob("ch*.json")):
        d = json.loads(f.read_text())
        for c in d.get("collisions", []):
            coll.append((f.stem, c))
        for c in d.get("low_content", []):
            low.append((f.stem, c))
    # collapse repeats: the same pair recorded on consecutive plays
    seen, uniq = set(), []
    for ch, c in coll:
        key = (ch, c["a"], c["b"])
        if key in seen:
            continue
        seen.add(key)
        uniq.append((ch, c))
    seen2, uniq2 = set(), []
    for ch, c in low:
        key = (ch, c["text"])
        if key in seen2:
            continue
        seen2.add(key)
        uniq2.append((ch, c))

    print(f"== overlapping captions ==  {len(uniq)} distinct pairs")
    for ch, c in uniq[:60]:
        print(f"  {ch}  t={c['t']:>7}  {c['overlap']:.0%}  "
              f"{c['a']!r}  vs  {c['b']!r}")
    print(f"\n== drawn under the caption band ==  {len(uniq2)} distinct")
    for ch, c in uniq2[:60]:
        print(f"  {ch}  bottom={c['bottom']}  {c['text']!r}")


if __name__ == "__main__":
    main()
