from pathlib import Path
import json

def load_prompt():
    return Path("docs/master_prompt.md").read_text(encoding="utf-8")

def research_topic():
    # Replace with YouTube API / competitor discovery / niche scoring
    return "The haunted house that was sealed forever"

def build_brief(topic: str):
    return {
        "topic": topic,
        "title": "The Haunted House That Was Sealed Forever",
        "hook": "They sealed this house forever... but something stayed inside.",
        "prompt": load_prompt()
    }

def main():
    topic = research_topic()
    brief = build_brief(topic)
    Path("outputs").mkdir(exist_ok=True)
    Path("outputs/brief.json").write_text(json.dumps(brief, indent=2), encoding="utf-8")
    print("Brief created:", brief["title"])

if __name__ == "__main__":
    main()