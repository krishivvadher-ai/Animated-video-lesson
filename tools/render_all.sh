#!/bin/bash
# Render every title card and every chapter at final quality.
cd "$(dirname "$0")/.."
R="-r 1920,1080 --fps 30"
for t in TitleFilm:titles_film TitleOne:titles_one TitleTwo:titles_two \
         TitleThree:titles_three Interval:titles_interval EndCard:titles_end; do
  .venv/bin/manim --disable_caching --media_dir build/media $R \
    -o "${t##*:}.mp4" chapters/titles.py "${t%%:*}" >/dev/null 2>&1 && echo "${t##*:} ok"
done
for f in chapters/ch*.py; do
  n=$(basename "$f" .py)
  .venv/bin/manim --disable_caching --media_dir build/media $R \
    -o "$n.mp4" "$f" "Chapter${n#ch}" >/dev/null 2>&1 && echo "$n ok" || echo "$n FAILED"
done
