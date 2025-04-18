#!/bin/bash

SESSION="agent-session"
ENV_NAME="tibetan-crawler"
PROJECT_DIR="$HOME/annotation_assistant"
LOCAL_API="local_agent_api.py"
CLIENT="agent_client.py"
TMUX=$(which tmux)

# Start a new tmux session
$TMUX new-session -d -s $SESSION -c "$PROJECT_DIR"

# Pane 1: Start local API with uvicorn
$TMUX send-keys -t $SESSION "conda activate $ENV_NAME" C-m
$TMUX send-keys -t $SESSION "python -m uvicorn $LOCAL_API:app --host 127.0.0.1 --port 8000" C-m

# Split vertically and start ngrok in pane 2
$TMUX split-window -h -t $SESSION
$TMUX send-keys -t $SESSION "cd $PROJECT_DIR" C-m
$TMUX send-keys -t $SESSION "ngrok http 8000" C-m

# Split pane 1 horizontally for the agent CLI (pane 3)
$TMUX select-pane -t $SESSION:0.0
$TMUX split-window -v -t $SESSION
$TMUX send-keys -t $SESSION "cd $PROJECT_DIR" C-m
$TMUX send-keys -t $SESSION "python $CLIENT" C-m

# Wait 5 seconds for ngrok to spin up
sleep 5

# Extract ngrok public URL (assumes API already running and local log)
NGROK_URL=$(curl --silent http://127.0.0.1:4040/api/tunnels | grep -o 'https://[0-9a-zA-Z.-]*ngrok-free.app')

# Extract token from .env
X_API_KEY=$(grep LOCAL_API_TOKEN "$PROJECT_DIR/.env" | cut -d '=' -f2)

# Final instructions to user
clear
echo "✅ Your agent is running in tmux session '$SESSION'"
echo "🌐 Public URL: ${NGROK_URL}/run"
echo "🔐 x-api-key: ${X_API_KEY}"
echo
echo "Paste this in ChatGPT:"
echo "This is my agent's endpoint: ${NGROK_URL}/run"
echo "Please send tasks using POST with JSON: { \"task\": \"...\" }"
echo "Include header: x-api-key: ${X_API_KEY}"
echo
echo "🧠 To reattach tmux: tmux attach -t $SESSION"
