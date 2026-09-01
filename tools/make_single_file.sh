#!/bin/bash
# One file, full length, full 1080p, under GitHub's 100 MB blob limit.
#
# Git LFS is blocked by this environment's egress policy, GitHub Releases are
# not permitted for this session type, and every external file host is blocked,
# so a single blob under 100 MB is the only way to hand over one playable file.
# The picture stays 1920x1080 and all 142 minutes are present; only the bitrate
# is reduced. Audio is Opus at 24 kbps mono -- speech only, and at this length
# anything higher would eat a third of the budget on its own.
set -e
cd /home/user/Animated-video-lesson
SRC=final/film-complete.mp4
OUT=final/film-complete-1080p.mp4
LIMIT=$((99 * 1024 * 1024))

for CRF in 29 31 33; do
  echo "encoding at crf $CRF ..."
  ffmpeg -y -v error -i "$SRC" \
    -c:v libx264 -crf $CRF -preset medium -tune animation -pix_fmt yuv420p \
    -c:a libopus -b:a 24k -ac 1 -movflags +faststart "$OUT"
  SZ=$(stat -c%s "$OUT")
  echo "crf $CRF -> $(python3 -c "print(round($SZ/1048576,1))") MiB"
  if [ "$SZ" -le "$LIMIT" ]; then
    echo "fits under 100 MB at crf $CRF"
    break
  fi
  echo "over the limit, trying a higher crf"
done

echo "--- result ---"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT"
ffprobe -v error -select_streams v -show_entries stream=width,height,r_frame_rate -of csv=p=0 "$OUT"
ffprobe -v error -select_streams a -show_entries stream=codec_name,channels -of csv=p=0 "$OUT"
