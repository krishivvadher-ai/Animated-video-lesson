"""Does each chapter open with something to look at?

His chapters start with a picture -- a shape, a scene, a graph -- and only
reach for a caption once there is something for the caption to be about. This
reports any chapter whose first animation is text."""
import ast, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXTY = {"caption", "points", "heading", "Text", "MarkupText", "body",
         "bullet_list", "section_title", "quote_card", "definition_card"}
VISUAL = {"Create", "DrawBorderThenFill", "GrowFromCenter", "GrowArrow",
          "ShowCreation"}


def first_play(fn):
    for node in ast.walk(fn):
        if isinstance(node, ast.Call) and getattr(node.func, "attr", "") == "play":
            return node
    return None


def names_in(node):
    out = []
    for x in ast.walk(node):
        if isinstance(x, ast.Name):
            out.append(x.id)
        elif isinstance(x, ast.Attribute):
            out.append(x.attr)
    return out


bad = []
for p in sorted(ROOT.glob("chapters/ch*.py")):
    tree = ast.parse(p.read_text())
    body = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "body":
            body = node
            break
    if body is None:
        continue
    call = first_play(body)
    if call is None:
        continue
    ns = names_in(call)
    visual = any(n in VISUAL for n in ns) or any(
        n in {"stick", "nell", "marshall", "ava", "kenji", "kit", "governor",
              "crowd", "factory", "building", "Bar", "icon", "ticket", "shield",
              "Axes", "MasterScale", "Chain", "door", "spring", "coin",
              "money_bag", "Dial", "fog", "iron_bar"} for n in ns)
    texty = any(n in TEXTY for n in ns)
    if texty and not visual:
        bad.append((p.stem, [n for n in ns if n in TEXTY]))

print(f"{len(bad)} chapter(s) open on text alone")
for stem, why in bad:
    print("  ", stem, why)
