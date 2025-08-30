#!/bin/bash

while true
do
    git add .

    # Commit only if there are changes
    if ! git diff --cached --quiet; then
        git commit -m "Auto-commit on $(date)"
        git push
    fi

    sleep 300  # Wait 300 seconds (5 minutes)
done
