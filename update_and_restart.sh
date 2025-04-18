#!/bin/bash

echo "🔄 Checking for updates..."
cd ~/annotation_assistant || exit

# If this is a Git repo:
if [ -d .git ]; then
    git pull origin main
else
    echo "⚠️ Not a git repo. Skipping pull."
fi

echo "🔁 Restarting agent session..."

tmux kill-session -t agent-session 2>/dev/null
tmux new-session -d -s agent-session '~/annotation_assistant/start_agent.sh'

echo "✅ Agent updated and restarted!"
