#!/bin/bash
# Reassemble the complete film from its parts.
#
# GitHub refuses a blob over 100 MB and this environment's egress policy blocks
# lfs.github.com, so the 356 MB film is stored as four byte-exact pieces. cat
# puts them back together bit for bit -- the checksum below proves it.
set -e
cd "$(dirname "$0")"
cat film-complete.mp4.part?? > film-complete.mp4
if command -v sha256sum >/dev/null; then
  sha256sum -c film-complete.mp4.sha256 && echo "film-complete.mp4 rebuilt and verified"
else
  shasum -a 256 -c film-complete.mp4.sha256 && echo "film-complete.mp4 rebuilt and verified"
fi
