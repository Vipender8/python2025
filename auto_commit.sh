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

"""
# This script automatically commits and pushes changes to a Git repository every 5 minutes.
# It first stages all changes, checks if there are any changes to commit, and if so, it commits them with a timestamped message and pushes to the remote repository.
#
# Usage:./auto_commit.sh
"""