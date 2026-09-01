"""Generate every narrated line once, before a parallel render starts, so no
two workers race to write the same cached file."""
import ast
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from lib import voice


def lines():
    out = []
    for p in sorted((ROOT / "chapters").glob("*.py")):
        tree = ast.parse(p.read_text())
        for node in ast.walk(tree):
            if not (isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Attribute)):
                continue
            attr = node.func.attr
            if attr in ("narrate", "line") and node.args:
                try:
                    text = ast.literal_eval(node.args[0])
                except Exception:
                    continue
                if not isinstance(text, str):
                    continue
                v = "n"
                for kw in node.keywords:
                    if kw.arg == "v":
                        try:
                            v = ast.literal_eval(kw.value)
                        except Exception:
                            v = "n"
                out.append((text, v))
            elif attr == "define":
                spoken = None
                for kw in node.keywords:
                    if kw.arg == "narration":
                        try:
                            spoken = ast.literal_eval(kw.value)
                        except Exception:
                            spoken = None
                if spoken is None and len(node.args) >= 2:
                    try:
                        spoken = (f"{ast.literal_eval(node.args[0])}. "
                                  f"{ast.literal_eval(node.args[1])}")
                    except Exception:
                        spoken = None
                if isinstance(spoken, str):
                    out.append((spoken, "n"))
            elif attr == "close_chapter" and node.args:
                try:
                    for b in ast.literal_eval(node.args[0]):
                        out.append((b, "n"))
                except Exception:
                    pass
    seen, uniq = set(), []
    for t, v in out:
        if (t, v) in seen:
            continue
        seen.add((t, v))
        uniq.append((t, v))
    return uniq


if __name__ == "__main__":
    ls = lines()
    made = 0
    for i, (t, v) in enumerate(ls):
        _, _, speed = voice.MODELS[v]
        key = hashlib.sha1(f"{v}|{speed}|{t}".encode()).hexdigest()[:20]
        if not (voice.CACHE / f"{key}.wav").exists():
            made += 1
        voice.speak(t, v)
        if i and i % 150 == 0:
            print(f"  {i}/{len(ls)}", flush=True)
    print(f"{len(ls)} lines cached ({made} newly generated)")
