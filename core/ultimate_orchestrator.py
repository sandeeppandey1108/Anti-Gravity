"""
ANTIGRAVITY ULTIMATE - The Production-Ready Autonomous System
Refined Version: Includes Hollywood Standards, API Connectors, and Fix-and-Retry logic.
"""
import os
import json
import sys
import time
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
from agents.hollywood_production import apply_hollywood_standards
from agents.api_connectors import APIConnector

MEMORY_PATH = "system/performance_memory.json"

def load_memory():
    if os.path.exists(MEMORY_PATH):
        try:
            with open(MEMORY_PATH, "r") as f:
                return json.load(f)
        except:
            pass
    return {"videos_produced": [], "total_revenue": 0, "failed_attempts": 0}

def run_production_cycle(niche="horror_true_crime"):
    """A single production cycle: Research -> Script -> Quality -> Hollywood Production -> Upload"""
    print(f"\n--- STARTING ULTIMATE PRODUCTION CYCLE: {datetime.now().strftime('%H:%M:%S')} ---")
    memory = load_memory()
    api = APIConnector()
    
    # 0. API CHECK
    print("🔌 PHASE 0: API CONNECTIVITY CHECK")
    print(f"  YouTube: {api.connect_youtube()}")
    print(f"  ElevenLabs: {api.connect_elevenlabs()}")
    
    # 1. RESEARCH & STRATEGY
    print("\n🔍 PHASE 1: RESEARCH & STRATEGY")
    research_data = research(niche=niche, memory=memory)
    ideas = generate_ideas(research_data["selected_topic"], niche=niche, transformation=research_data["transformation"])
    strategy = select_winning_idea(rank_ideas(ideas), research_data)
    print(f"✅ Selected Topic: {strategy['primary']['title']}")
    
    # 2. SCRIPT & QUALITY (with Fix & Retry Logic)
    print("\n✍️ PHASE 2: SCRIPTING & QUALITY CONTROL")
    script = script_agent(research_data["selected_topic"], strategy['primary']['title'], "long_form", niche=niche)
    
    max_retries = 3
    for attempt in range(max_retries):
        quality = quality_check(script)
        if quality['passed']:
            print(f"✅ Quality Check Passed (Score: {quality['score']}) on attempt {attempt + 1}")
            break
        else:
            print(f"⚠️ Quality Check Failed (Score: {quality['score']}). Attempting fix {attempt + 1}/{max_retries}...")
            script = improve_script(script, quality)
    else:
        print("❌ CRITICAL: Failed to reach quality standards after max retries. Aborting cycle.")
        memory["failed_attempts"] = memory.get("failed_attempts", 0) + 1
        return False

    # 3. HOLLYWOOD PRODUCTION
    print("\n🎬 PHASE 3: HOLLYWOOD PRODUCTION (VOICE & VIDEO)")
    voice_plan = voice_agent(script, niche=niche)
    video_plan = video_agent(script, voice_plan, niche=niche)
    
    # Apply Hollywood Standards (Effects, Transitions, Subtitles)
    hollywood_plan = apply_hollywood_standards(video_plan)
    print(f"✅ Hollywood Standards Applied: {hollywood_plan['color_grade']} grading, {len(hollywood_plan['transitions'])} transitions.")
    
    # 4. DISTRIBUTION & MEMORY
    print("\n📤 PHASE 4: DISTRIBUTION & MEMORY UPDATE")
    upload_package = upload_video(hollywood_plan, script, strategy, niche=niche, timing_data=research_data["timing"])
    
    # Update memory
    memory["videos_produced"].append({
        "title": strategy['primary']['title'],
        "date": datetime.now().isoformat(),
        "quality_score": quality['score'],
        "niche": niche,
        "status": "ready_for_upload",
        "scheduled_time": upload_package['schedule']['datetime_est'],
        "production_level": "Hollywood"
    })
    
    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=2)
        
    print(f"\n✅ ULTIMATE CYCLE COMPLETE. Scheduled for: {upload_package['schedule']['datetime_est']}")
    return True

if __name__ == "__main__":
    run_production_cycle()
