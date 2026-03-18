#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <links_txt_path> <gcs_target_prefix>"
  echo "Example: $0 data/links/yellow_2024_2025_links.txt gs://my-bucket/taxi-data/yellow"
  exit 1
fi

LINKS_FILE="$1"
GCS_PREFIX="$2"

if [[ ! -f "$LINKS_FILE" ]]; then
  echo "Links file not found: $LINKS_FILE"
  exit 1
fi

while IFS= read -r url; do
  [[ -z "$url" ]] && continue
  fname="$(basename "$url")"
  echo "Copying $fname -> ${GCS_PREFIX%/}/$fname"
  gsutil cp "$url" "${GCS_PREFIX%/}/$fname"
done < "$LINKS_FILE"

echo "Upload complete."
