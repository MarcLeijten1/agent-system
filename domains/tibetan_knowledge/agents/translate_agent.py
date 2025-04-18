import json

class TranslatorAgent:
    def run(self, query):
        with open("data/tib_wylie_dict.json", encoding="utf-8") as f:
            dictionary = json.load(f)

        result = dictionary.get(query)
        if result:
            print(f"🧾 Wylie transliteration: {result}")
        else:
            print("🙈 No entry found.")
