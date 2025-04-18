from openai import OpenAI
import os
import requests
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Constants
API_URL = os.getenv("API_URL", "http://localhost:8000/run")
API_TOKEN = os.getenv("LOCAL_API_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
AGENT_MODE = os.getenv("AGENT_MODE", "local")

LOG_FILE = "agent_cli_history.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

def log_task(task, result):
    if os.path.getsize(LOG_FILE) > 1000000:  # ~1MB
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        os.rename(LOG_FILE, f"logs/agent_cli_{timestamp}.log")
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now().isoformat()} | TASK: {task} | RESULT: {result}\n")

def send_task_local(task: str):
    headers = {
        "x-api-key": API_TOKEN,
        "Content-Type": "application/json"
    }
    response = requests.post(API_URL, json={"task": task}, headers=headers)

    if response.status_code == 200:
        result = response.json()["result"]
        print("✅ Result:")
        print(result)
        log_task(task, result)
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
        log_task(task, f"ERROR {response.status_code}: {response.text}")

def send_task_openai(task: str):
    from openai import OpenAI
    client = OpenAI(api_key=OPENAI_KEY)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": task}
        ]
    )

    result = response.choices[0].message.content.strip()
    print("✅ Result:")
    print(result)
    log_task(task, result)

def main():
    print("🤖 Local Agent CLI Client")
    while True:
        task = input("Enter task: ").strip()
        if task.lower() in ["exit", "quit"]:
            break
        try:
            if AGENT_MODE == "openai":
                send_task_openai(task)
            else:
                send_task_local(task)
        except Exception as e:
            print(f"❌ Error: {e}")
            log_task(task, f"Exception: {e}")

if __name__ == "__main__":
    main()
