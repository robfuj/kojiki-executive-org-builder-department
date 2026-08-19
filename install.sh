#!/usr/bin/env bash
# Install THIS department together with the shared ontology (kojiki-ontology).
# Idempotent: clones only what is missing.
set -e
OWNER="robfuj"
HERE="$(cd "$(dirname "$0")" && pwd)"
PARENT="$(dirname "$HERE")"
ONT="kojiki-ontology"
if [ -d "$PARENT/$ONT" ]; then echo "ontology present: $PARENT/$ONT";
else
  echo "cloning ontology -> $PARENT/$ONT"
  git clone --depth 1 "https://github.com/$OWNER/$ONT.git" "$PARENT/$ONT"
fi
echo ""
echo "Installed: $ONT + 21-executive-org-builder"
echo "Next: follow AGENT.md (Orientation Protocol), then bots/install_bots.py <slugs>."
