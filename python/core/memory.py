from pathlib import Path
import json

MEMORY_FILE = Path("outputs/memory.jsonl")
MEMORY_FILE.parent.mkdir(exist_ok=True)

def store_memory(data):
    with MEMORY_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(data) + "\n")
