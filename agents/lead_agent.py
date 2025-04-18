from agents.translate_agent import TranslatorAgent
from agents.sanskrit_agent import SanskritAgent
from agents.normalize_agent import NormalizeAgent
from agents.multistep_agent import MultiStepAgent
from agents.builder_agent import BuilderAgent

class LeadAgent:
    def __init__(self):
        self.translator = TranslatorAgent()
        self.sanskrit = SanskritAgent()
        self.normalizer = NormalizeAgent()
        self.pipeline = MultiStepAgent(self.translator, self.sanskrit, self.normalizer)
        self.builder = BuilderAgent()

        self.agents = {
            "translate": self.translator,
            "translate skt": self.sanskrit,
            "normalize": self.normalizer,
            "pipeline": self.pipeline,
            "build": self.builder
        }

    def handle_request(self, cmd):
        for prefix, agent in self.agents.items():
            if cmd.startswith(prefix):
                return agent.handle(cmd)
        print("❓ Unknown command. Try: 'translate <word>', 'translate skt <word>', 'normalize <word>', 'pipeline <word>', or 'build <task>'")
