import os
from datetime import datetime

LOG_FILE = "agent_cli_history.log"

def parse_log_line(line):
    try:
        timestamp, rest = line.strip().split(" | TASK: ", 1)
        task, result = rest.split(" | RESULT: ", 1)
        return timestamp, task, result
    except ValueError:
        return None, None, None

def show_history(filter_keyword=None):
    if not os.path.exists(LOG_FILE):
        print("⚠️ No history log found.")
        return

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    print("\n📜 Task History Viewer")
    print("----------------------")

    for line in lines:
        timestamp, task, result = parse_log_line(line)
        if not timestamp:
            continue
        if filter_keyword and filter_keyword.lower() not in task.lower():
            continue

        print(f"🕒 {timestamp}")
        print(f"📝 Task: {task}")
        print(f"📤 Result: {result}\n")

if __name__ == "__main__":
    keyword = input("🔎 Enter a keyword to filter (press Enter to show all): ").strip()
    show_history(keyword if keyword else None)

