from pathlib import Path
import json

from agents.research_agent import research_topic
from agents.competitor_agent import discover_competitors
from agents.upload_time_agent import analyze_upload_time
from agents.niche_agent import score_niche
from agents.script_agent import generate_script
from agents.thumbnail_agent import generate_thumbnail_concept
from agents.video_agent import create_video
from agents.upload_agent import generate_metadata, upload_video
from agents.analytics_agent import log_video
from agents.compliance_agent import compliance_check
from agents.optimization_agent import optimize_next
from core.memory import store_memory

OUTPUT = Path("outputs")
OUTPUT.mkdir(exist_ok=True)

def run():
    niche = "horror / ghost / haunted"
    competitors = discover_competitors(niche)
    niche_score = score_niche(niche, competitors)
    best_time = analyze_upload_time(niche, competitors)

    topic = research_topic(niche, competitors)
    script = generate_script(topic)
    compliance = compliance_check(script)
    if not compliance["safe"]:
        script = generate_script(topic + " improved")

    thumbnail = generate_thumbnail_concept(topic)
    video_path = create_video(script, thumbnail)

    metadata = generate_metadata(topic, niche)
    video_id = upload_video(video_path, metadata["title"], metadata["description"], metadata["tags"])

    result = {
        "niche": niche,
        "topic": topic,
        "script": script,
        "thumbnail": thumbnail,
        "video_path": video_path,
        "video_id": video_id,
        "best_time": best_time,
        "niche_score": niche_score
    }

    store_memory(result)
    log_video(result)
    optimize_next(result)

    Path("outputs/last_run.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print("Pipeline complete:", result["video_id"])

if __name__ == "__main__":
    run()
