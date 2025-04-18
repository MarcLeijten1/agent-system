#!/bin/bash

echo "🔄 Stopping tmux session if running..."
tmux kill-session -t agent-session 2>/dev/null

echo "🚀 Launching fresh agent session..."
tmux new-session -s agent-session './start_agent.sh'
