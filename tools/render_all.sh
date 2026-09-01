#!/bin/bash
# Render every chapter. Each worker gets its own media directory, because
# manim's text cache is shared state and two workers racing on it can delete a
# file the other is still using. Four at a time at 1080p: eight ran the box out
# of memory and the kernel killed them mid-frame.
cd /home/user/Animated-video-lesson
Q="${Q:--r 1920,1080 --fps 30}"; DIR="${DIR:-1080p30}"; N="${N:-4}"
LIST="${*:-$(seq -w 0 49)}"
for n in $LIST; do
  while [ "$(jobs -rp | wc -l)" -ge "$N" ]; do wait -n; done
  (
    W="/tmp/mw_$n"; rm -rf "$W"
    .venv/bin/manim $Q --disable_caching --media_dir "$W" -o "ch$n.mp4" \
      "chapters/ch$n.py" "Chapter$n" > "/tmp/r_ch$n.log" 2>&1
    SRC="$W/videos/ch$n/$DIR/ch$n.mp4"
    if [ -f "$SRC" ]; then
      mkdir -p "build/media/videos/ch$n/$DIR"
      mv "$SRC" "build/media/videos/ch$n/$DIR/ch$n.mp4"
      .venv/bin/python -c "
import json;d=json.load(open('build/subs/ch$n.json'))
bad=sum(len(d.get(k,[])) for k in ('collisions','too_small','silent_beats','off_frame'))
print('ch$n %s %6.1fs  col %d  small %d  silent %d  off %d'%(
    'OK ' if not bad else 'BAD', d['duration'], len(d['collisions']),
    len(d['too_small']), len(d.get('silent_beats',[])), len(d.get('off_frame',[]))))"
    else
      echo "ch$n FAILED"; tail -3 "/tmp/r_ch$n.log" | tr -d '│─╭╮╯╰'
    fi
    rm -rf "$W"
  ) &
done
wait
