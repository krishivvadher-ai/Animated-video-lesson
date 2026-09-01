#!/bin/bash
# The captioned film as one playable file under GitHub's 100 MB blob limit.
#
# Encoded from the original master with the caption band added and the captions
# burned in the same pass, so the picture takes one generation of loss rather
# than two -- re-compressing the already-encoded captioned master would stack
# two lossy passes on top of each other for no reason.
set -e
cd /home/user/Animated-video-lesson
SRC=final/film-complete.mp4
ASS=build/film-complete.ass
OUT=final/film-complete-1080p-captioned.mp4
LIMIT=$((100 * 1024 * 1024))

for CRF in 34 36 38; do
  echo "encoding at crf $CRF ..."
  ffmpeg -y -v error -i "$SRC" \
    -vf "pad=iw:ih+200:0:0:color=black,subtitles=$ASS" \
    -c:v libx264 -crf $CRF -preset medium -tune animation -pix_fmt yuv420p \
    -c:a libopus -b:a 24k -ac 1 -movflags +faststart "$OUT"
  SZ=$(stat -c%s "$OUT")
  echo "crf $CRF -> $(python3 -c "print(round($SZ/1048576,2))") MiB"
  [ "$SZ" -lt "$LIMIT" ] && { echo "fits at crf $CRF"; break; }
  echo "over the limit, stepping up"
done

echo "--- verify ---"
echo "duration: $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT")"
echo "video:    $(ffprobe -v error -select_streams v -show_entries stream=width,height,r_frame_rate -of csv=p=0 "$OUT")"
echo "audio:    $(ffprobe -v error -select_streams a -show_entries stream=codec_name,channels -of csv=p=0 "$OUT")"
ffmpeg -v error -xerror -i "$OUT" -f null - 2>/tmp/dec2.err && echo "decode:   clean" || { echo "decode: ERRORS"; head -3 /tmp/dec2.err; exit 1; }
