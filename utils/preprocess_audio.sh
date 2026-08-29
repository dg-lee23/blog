#!/bin/bash
# preprocess_audios.sh — trim each .mp3 in static/audio/ to first 30s, overwrite in place
set -e
AUDIO_DIR="static/audio"

for f in "$AUDIO_DIR"/*.mp3; do
    tmp="${f%.mp3}.tmp.mp3"
    ffmpeg -y -i "$f" -t 30 -c copy "$tmp" -loglevel error
    mv "$tmp" "$f"
    echo "trimmed: $(basename "$f")"
done