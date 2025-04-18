# agents/normalize_agent.py

import json

class NormalizeAgent:
    def __init__(self):
        with open("data/short_long_pairs.json", encoding="utf-8") as f:
            self.pairs = json.load(f)

    def handle(self, cmd):
        parts = cmd.split(maxsplit=1)
        if len(parts) < 2:
            print("⚠️  Please provide a Tibetan word.")
            return

        tib_word = parts[1].strip()
        normalized = self.pairs.get(tib_word)
        if normalized:
            print(f"🔗 Full form: {normalized}")
        else:
            print("🙈 No normalized form found.")
