#!/bin/bash
# Render every title card and every chapter at final quality, four at a time.
cd "$(dirname "$0")/.."
R="-r 1920,1080 --fps 30"
JOBS="${JOBS:-4}"

# every narrated line is generated once first, so parallel workers never race
.venv/bin/python tools/prewarm_audio.py | tail -1

render_one() {
  f="$1"
  n=$(basename "$f" .py)
  if [ "$n" = "titles" ]; then return; fi
  out="build/media/videos/$n/1080p30/$n.mp4"
  .venv/bin/manim --disable_caching --media_dir build/media \
    -r 1920,1080 --fps 30 -o "$n.mp4" "$f" "Chapter${n#ch}" > "/tmp/r_$n.log" 2>&1
  if [ -f "$out" ]; then
    echo "$n OK $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$out")"
  else
    echo "$n FAILED"
    grep -E "Error|chapters/|lib/" "/tmp/r_$n.log" | tail -4
  fi
}
export -f render_one

for t in TitleFilm:titles_film TitleOne:titles_one TitleTwo:titles_two \
         TitleThree:titles_three Interval:titles_interval EndCard:titles_end; do
  cls=${t%%:*}; out=${t##*:}
  .venv/bin/manim --disable_caching --media_dir build/media $R \
    -o "$out.mp4" chapters/titles.py "$cls" > "/tmp/r_$out.log" 2>&1
  [ -f "build/media/videos/titles/1080p30/$out.mp4" ] && echo "$out OK" \
    || { echo "$out FAILED"; tail -4 "/tmp/r_$out.log"; }
done

ls chapters/ch*.py | xargs -P "$JOBS" -I{} bash -c 'render_one "$@"' _ {}
echo "RENDER DONE"
