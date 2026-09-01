"""Catch over-long captions before spending three minutes on a render."""
import ast, sys, glob
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.stage import MAX_CAPTION, MAX_DEFINITION


def literal(node):
    try:
        v = ast.literal_eval(node)
        return v if isinstance(v, str) else None
    except Exception:
        return None


bad = 0
for f in sorted(glob.glob(str(Path(sys.argv[1] if len(sys.argv) > 1 else "chapters")
                              ) + "/ch*.py")):
    tree = ast.parse(open(f).read())
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        name = getattr(node.func, "attr", getattr(node.func, "id", ""))
        if name == "caption" and node.args:
            t = literal(node.args[0])
            if t and len(t.replace("\n", " ")) > MAX_CAPTION:
                print(f"{f}:{node.lineno}  caption {len(t)} > {MAX_CAPTION}: {t[:70]!r}")
                bad += 1
        elif name == "points" and node.args:
            try:
                items = ast.literal_eval(node.args[0])
            except Exception:
                continue
            for it in items:
                if len(str(it).replace("\n", " ")) > MAX_CAPTION:
                    print(f"{f}:{node.lineno}  point {len(it)}: {it[:70]!r}")
                    bad += 1
        elif name == "define" and len(node.args) > 1:
            d = literal(node.args[1])
            if d and len(d) > MAX_DEFINITION:
                print(f"{f}:{node.lineno}  definition {len(d)} > {MAX_DEFINITION}: "
                      f"{d[:70]!r}")
                bad += 1
        elif name == "close_chapter" and node.args:
            try:
                items = ast.literal_eval(node.args[0])
            except Exception:
                continue
            for it in items:
                if len(str(it)) > MAX_CAPTION:
                    print(f"{f}:{node.lineno}  bullet {len(it)}: {it[:70]!r}")
                    bad += 1
print(f"{bad} over-long strings")
sys.exit(1 if bad else 0)
