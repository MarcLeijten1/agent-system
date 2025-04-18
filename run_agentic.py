# run_agentic.py
from agents.lead_agent import LeadAgent

if __name__ == "__main__":
    print("\n🤖 Welcome to the Agentic Dictionary Assistant!\n")
    lead = LeadAgent()
    while True:
        cmd = input("🗣️  What do you want to do? (or 'q' to quit)\n> ")
        if cmd.strip().lower() in ["q", "quit", "exit"]:
            print("👋 Goodbye!")
            break
        lead.handle_request(cmd)
