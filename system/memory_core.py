"""
Mythos RAG Memory Core
Stores and retrieves experience, reasoning patterns, and solved problems.
Compensates for the absence of the Pro model after deployment.
"""
import json
import os

class MemoryCore:
    def __init__(self):
        self.memory_path = "system/mythos_experience.json"
        self.knowledge_base = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_path):
            with open(self.memory_path, "r") as f:
                return json.load(f)
        return {"solved_problems": {}, "reasoning_patterns": [], "successful_hooks": []}

    def store_experience(self, task, reasoning, result):
        """Stores a successful reasoning trace for future retrieval."""
        self.knowledge_base["solved_problems"][task] = {
            "reasoning": reasoning,
            "result": result
        }
        self.save_memory()

    def retrieve_similar_logic(self, task_query):
        """Simulates RAG retrieval of similar past solutions."""
        # In a real setup, this would use ChromaDB or similar vector search
        for task, data in self.knowledge_base["solved_problems"].items():
            if task_query.lower() in task.lower():
                return data
        return None

    def save_memory(self):
        with open(self.memory_path, "w") as f:
            json.dump(self.knowledge_base, f, indent=2)

if __name__ == "__main__":
    memory = MemoryCore()
    memory.store_experience("Cinematic Hook", "Use emotional trigger + visual push", "Success")
    print("Retrieved Logic:", memory.retrieve_similar_logic("Hook"))
