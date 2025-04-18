📘 Agent System: Quickstart Guide

This agent allows interaction via OpenAI API or local FastAPI, routed optionally through ngrok.

🔧 To launch the full system:
$ ./start_agent.sh

It will:
- activate the environment
- start your FastAPI server
- start ngrok to expose it
- launch the CLI interface to ChatGPT

🌍 Share this with ChatGPT:
"This is my agent's endpoint: https://xxxxx.ngrok-free.app/run
Please send tasks using POST with JSON: { "task": "..." } and header x-api-key: <your token>."

🧠 If disconnected, resume tmux session:
$ tmux attach -t agent-session
