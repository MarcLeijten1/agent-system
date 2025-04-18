# 🧠 Annotation Assistant: GPT-Powered Pipeline for Dictionary Projects

This is a fully automated pipeline for managing dictionary annotation tasks using a multi-agent system powered by GPT and FastAPI.

## 🚀 Features

- 🌍 Public API exposed via Ngrok
- 🧠 GPT-based agents for translation, normalization, and multi-step reasoning
- 🪟 Auto-start using `tmux` session management
- 🔁 Relaunch the system with one command (`./relaunch.sh`)
- 📦 Easily deployable and Git-versioned

## 📂 Project Structure

```
├── agents/                   # Specialized GPT agents
├── data/                     # Input datasets (JSON, CSV)
├── domains/tibetan_knowledge/ # Custom domain logic
├── pipeline/                 # Task orchestration
├── relaunch.sh              # One-command relaunch script
├── start_agent.sh           # Starts the FastAPI server + ngrok
├── .gitignore               
├── requirements.txt         
└── README.md
```

## ⚙️ Setup

```bash
# Clone the repository
git clone https://github.com/MarcLeijten1/agent-system.git
cd agent-system

# Create & activate conda environment
conda create -n tibetan-crawler python=3.10
conda activate tibetan-crawler

# Install requirements
pip install -r requirements.txt
```

## 🧠 Run the Pipeline

```bash
# Start the system
./relaunch.sh
```

Or if you prefer:

```bash
make start
```

## 📡 Agent API

Once running, your agent is accessible at:

```
POST https://<your-ngrok-url>.ngrok-free.app/run
Headers:
  x-api-key: <your-token>
Body:
  { "task": "Translate this Tibetan sentence..." }
```

## 🛠 Scripts

- `start_agent.sh` – Launches FastAPI + ngrok tunnel
- `update_and_restart.sh` – Pull latest code and relaunch
- `view_history.py` – Review past tasks sent to the agent

## 📃 License

MIT License. See [LICENSE](LICENSE) for details.

---

Made with love and frustration 💖⚙️  
~ Marc Leijten & GPT
