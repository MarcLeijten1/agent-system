# agents/multistep_agent.py

class MultiStepAgent:
    def __init__(self, translator, sanskrit, normalizer):
        self.translator = translator
        self.sanskrit = sanskrit
        self.normalizer = normalizer

    def handle(self, cmd):
        parts = cmd.split(maxsplit=1)
        if len(parts) < 2:
            print("⚠️  Please enter a Tibetan word.")
            return

        tib_input = parts[1].strip()

        # Step 1: Normalize
        full_form = self.normalizer.pairs.get(tib_input, tib_input)
        if full_form != tib_input:
            print(f"🔗 Normalized form: {full_form}")
        else:
            print("🔍 No normalization needed.")

        # Step 2: Transliterate
        wylie = self.translator.dict.get(full_form)
        if wylie:
            print(f"📜 Wylie transliteration: {wylie}")
        else:
            print("🙈 No Wylie found.")
            return

        # Step 3: Sanskrit
        sanskrit = self.sanskrit.map.get(wylie)
        if sanskrit:
            print(f"🕉️ Sanskrit equivalent: {sanskrit}")
        else:
            print("📭 No Sanskrit match.")
