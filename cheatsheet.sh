#!/bin/bash
echo "🧠 Common Agent Commands"

echo ""
echo "▶ Start Everything:"
echo "./start_agent.sh"

echo ""
echo "▶ Resume Session if disconnected:"
echo "tmux attach -t agent-session"

echo ""
echo "▶ Start only individual parts:"
echo "conda activate tibetan-crawler"
echo "python agent_client.py"
echo "python -m uvicorn local_agent_api:app --host 127.0.0.1 --port 8000"
echo "ngrok http 8000"
