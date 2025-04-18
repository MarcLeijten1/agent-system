import json

# Load dictionaries
with open("data/tib_wylie_dict.json", encoding="utf-8") as f:
    tib_wylie = json.load(f)

with open("data/tib_skt_map.json", encoding="utf-8") as f:
    tib_skt = json.load(f)

with open("data/short_long_pairs.json", encoding="utf-8") as f:
    short_long = json.load(f)

def lookup(word):
    print(f"\n🔍 Looking up: {word}\n")

    wylie = tib_wylie.get(word)
    sanskrit = tib_skt.get(word)
    long_form = short_long.get(word)

    if wylie:
        print(f"📜 Wylie transliteration: {wylie}")
    if sanskrit:
        print(f"🕉️ Sanskrit equivalent: {sanskrit}")
    if long_form:
        print(f"🔗 Full form: {long_form}")

    if not any([wylie, sanskrit, long_form]):
        print("🙈 No entry found.")

if __name__ == "__main__":
    while True:
        query = input("\nEnter a Tibetan word (or 'q' to quit): ")
        if query.lower() == "q":
            break
        lookup(query)
