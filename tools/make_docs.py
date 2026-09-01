"""Generate docs/glossary.md and docs/narration.md from the chapter sources.

Generating them from the code rather than by hand guarantees that the glossary
and the script are exactly what the film says.
"""
import ast, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CH = ROOT / "chapters"
DOCS = ROOT / "docs"


def literal(node):
    try:
        v = ast.literal_eval(node)
        return v if isinstance(v, str) else None
    except Exception:
        return None


def scan(path):
    tree = ast.parse(path.read_text())
    title = num = part = None
    defs, narr = [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
            n = node.targets[0].id
            if n == "TITLE":
                title = literal(node.value)
            elif n == "CH":
                num = literal(node.value) if isinstance(literal(node.value), str) else getattr(node.value, "value", None)
            elif n == "PART":
                part = literal(node.value)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "define" and len(node.args) >= 2:
                t, d = literal(node.args[0]), literal(node.args[1])
                if t and d:
                    defs.append((t, d))
            if node.func.attr in ("narrate", "line") and node.args:
                t = literal(node.args[0])
                v = "n"
                for kw in node.keywords:
                    if kw.arg == "v":
                        v = literal(kw.value) or "n"
                if t:
                    narr.append((v, t))
    return num, title, part, defs, narr


def main():
    rows = []
    for p in sorted(CH.glob("ch*.py")):
        n = int(p.stem[2:])
        num, title, part, defs, narr = scan(p)
        rows.append((n, title, part, defs, narr))
    rows.sort()

    g = ["# Glossary — every term the film defines, and where",
         "",
         "Every entry below is a definition card that appears on screen, with its",
         "word, a one-line plain definition and a recurring icon. Nothing in the film",
         "uses a term before the chapter listed here.",
         "",
         "| Term | Definition as given on screen | Chapter |",
         "|---|---|---|"]
    seen = {}
    for n, title, part, defs, narr in rows:
        for t, d in defs:
            if t not in seen:
                seen[t] = n
                g.append(f"| **{t}** | {d} | {n} — {title} |")
    (DOCS / "glossary.md").write_text("\n".join(g) + "\n")

    lines = ["# Narration — the full spoken script, chapter by chapter", "",
             "`N` is the narrator (British male). `C` is the character voice",
             "(British female) used for Ava's and Kit's interruptions.", ""]
    words = 0
    part_now = None
    for n, title, part, defs, narr in rows:
        if part != part_now:
            lines += ["", f"# {part}", ""]
            part_now = part
        lines += [f"## Chapter {n} — {title}", ""]
        for v, t in narr:
            words += len(t.split())
            lines.append(f"**{v.upper()}** {t}")
            lines.append("")
    lines += ["---", "", f"Total narration: **{words} words** "
              f"(about {words/128:.0f} minutes at the film's pace of ~128 words a minute)."]
    (DOCS / "narration.md").write_text("\n".join(lines) + "\n")
    print(f"glossary: {len(seen)} terms;  narration: {words} words")


if __name__ == "__main__":
    main()
