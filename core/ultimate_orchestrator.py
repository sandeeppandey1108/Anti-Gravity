"""
ANTIGRAVITY ULTIMATE - The Production-Ready Autonomous System
Combines Research, Strategy, Scripting, Quality Control, and Memory.
"""
import os
import json
import sys
from datetime import datetime

# Add parent directory to path to import agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.research import research
from agents.strategy import generate_ideas, rank_ideas, select_winning_idea
from agents.script import script_agent
from agents.quality import quality_check, improve_script
from agents.voice import voice_agent
from agents.video import video_agent
from agents.upload import upload_video
from agents.analytics import analyze
from agents.optimization import update_memory

MEMORY_PATH = "system/performance_memory.json"

def load_memory():
    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, "r") as f:
            return json.load(f)
    return {"videos_produced": [], "total_revenue": 0}

def run_ultimate_pipeline(niche="horror_true_crime"):
    print(f"🚀 INITIALIZING ANTIGRAVITY ULTIMATE SYSTEM [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    memory = load_memory()
    
    # 1. RESEARCH & STRATEGY
    print("\n🔍 PHASE 1: RESEARCH & STRATEGY")
    research_data = research(niche=niche, memory=memory)
    ideas = generate_ideas(research_data["selected_topic"], niche=niche, transformation=research_data["transformation"])
    strategy = select_winning_idea(rank_ideas(ideas), research_data)
    print(f"✅ Selected Topic: {strategy['primary']['title']}")
    
    # 2. SCRIPT & QUALITY
    print("\n✍️ PHASE 2: SCRIPTING & QUALITY CONTROL")
    script = script_agent(research_data["selected_topic"], strategy['primary']['title'], "long_form", niche=niche)
    quality = quality_check(script)
    
    if not quality['passed']:
        print(f"⚠️ Quality Check Failed (Score: {quality['score']}). Improving...")
        script = improve_script(script, quality)
        quality = quality_check(script)
        print(f"✅ Script Improved. New Score: {quality['score']}")
    else:
        print(f"✅ Quality Check Passed (Score: {quality['score']})")
        
    # 3. PRODUCTION
    print("\n🎬 PHASE 3: PRODUCTION (VOICE & VIDEO)")
    voice_plan = voice_agent(script, niche=niche)
    video_plan = video_agent(script, voice_plan, niche=niche)
    print(f"✅ Production Plans Ready. Est. Duration: {video_plan['target_duration']}")
    
    # 4. DISTRIBUTION & MEMORY
    print("\n📤 PHASE 4: DISTRIBUTION & MEMORY UPDATE")
    upload_package = upload_video(video_plan, script, strategy, niche=niche, timing_data=research_data["timing"])
    
    # Update memory with the new production
    memory["videos_produced"].append({
        "title": strategy['primary']['title'],
        "date": datetime.now().isoformat(),
        "quality_score": quality['score'],
        "niche": niche
    })
    
    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=2)
        
    print("\n✅ PIPELINE COMPLETE. SYSTEM UPDATED.")
    print(f"🔗 Ready for upload at: {upload_package['schedule']['datetime_est']}")

if __name__ == "__main__":
    run_ultimate_pipeline()
