"""
MYTHOS AI OS - Unified Orchestrator
Implements the "One System, Two Brains" architecture:
- Lite (7B-13B): Fast, local, subconscious thinking.
- Pro (70B+): Deep, conscious, reasoning-heavy thinking.
- Shared Memory: Experience and reasoning traces.
- Model Router: Automatic escalation based on complexity.
"""
import os
import json
import sys
from datetime import datetime

# Add parent directory to path to import agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.multi_ai_team import MultiAITeam
from agents.api_connectors import APIConnector

class MythosOrchestrator:
    def __init__(self):
        self.team = MultiAITeam()
        self.api = APIConnector()
        self.memory_path = "system/mythos_memory.json"
        self.lite_threshold = 70 # Complexity score threshold

    def load_memory(self):
        if os.path.exists(self.memory_path):
            with open(self.memory_path, "r") as f:
                return json.load(f)
        return {"reasoning_traces": [], "knowledge_base": {}, "experience_log": []}

    def save_memory(self, memory):
        with open(self.memory_path, "w") as f:
            json.dump(memory, f, indent=2)

    def route_task(self, task_complexity):
        """Automatic Model Router logic."""
        if task_complexity > self.lite_threshold:
            print("🧠 [ROUTER] Task complex. Escalating to PRO (70B+)...")
            return "PRO"
        else:
            print("⚡ [ROUTER] Task simple. Routing to LITE (7B-13B)...")
            return "LITE"

    def process_task(self, task_name, complexity):
        memory = self.load_memory()
        brain = self.route_task(complexity)
        
        print(f"🚀 [MYTHOS] Processing '{task_name}' using {brain} brain...")
        
        # Simulate reasoning trace generation for the "Learning Loop"
        trace = {
            "task": task_name,
            "brain": brain,
            "timestamp": datetime.now().isoformat(),
            "reasoning": f"Step-by-step logic for {task_name}...",
            "result": "Success"
        }
        
        memory["reasoning_traces"].append(trace)
        self.save_memory(memory)
        
        if brain == "PRO":
            # Pro reasoning updates the knowledge base for Lite to use later
            memory["knowledge_base"][task_name] = "Refined logic from Pro"
            self.save_memory(memory)
            print(f"📈 [LEARNING] Pro reasoning compressed into memory for Lite upgrade.")

        return trace

if __name__ == "__main__":
    mythos = MythosOrchestrator()
    mythos.process_task("Cinematic Script Generation", 85) # Complex
    mythos.process_task("Thumbnail Text Generation", 30)   # Simple
