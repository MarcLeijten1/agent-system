# agents/sanskrit_agent.py

import json

class SanskritAgent:
    def __init__(self):
        with open("data/tib_skt_map.json", encoding="utf-8") as f:
            self.skt_map = json.load(f)

    def handle(self, cmd):
        parts = cmd.split(maxsplit=1)
        if len(parts) < 2:
            print("⚠️  Please provide a Tibetan word to look up.")
            return

        tib_word = parts[1].strip()
        skt_word = self.skt_map.get(tib_word)
        if skt_word:
            print(f"🕉️  Sanskrit equivalent: {skt_word}")
        else:
            print("🙈 No Sanskrit equivalent found.")
