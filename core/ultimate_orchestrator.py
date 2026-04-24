"""
ANTIGRAVITY ULTIMATE - The Production-Ready Autonomous System
Combines Research, Strategy, Scripting, Quality Control, and Memory.
Implements the "Self-Managing" loop from the vision document.
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
from agents.analytics import analyze
from agents.optimization import update_memory

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
    """A single production cycle: Research -> Script -> Quality -> Production -> Upload"""
    print(f"\n--- STARTING PRODUCTION CYCLE: {datetime.now().strftime('%H:%M:%S')} ---")
    memory = load_memory()
    
    # 1. RESEARCH & STRATEGY
    print("🔍 PHASE 1: RESEARCH & STRATEGY")
    research_data = research(niche=niche, memory=memory)
    ideas = generate_ideas(research_data["selected_topic"], niche=niche, transformation=research_data["transformation"])
    strategy = select_winning_idea(rank_ideas(ideas), research_data)
    print(f"✅ Selected Topic: {strategy['primary']['title']}")
    
    # 2. SCRIPT & QUALITY (with Fix & Retry Logic)
    print("✍️ PHASE 2: SCRIPTING & QUALITY CONTROL")
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

    # 3. PRODUCTION
    print("🎬 PHASE 3: PRODUCTION (VOICE & VIDEO)")
    voice_plan = voice_agent(script, niche=niche)
    video_plan = video_agent(script, voice_plan, niche=niche)
    print(f"✅ Production Plans Ready. Est. Duration: {video_plan['target_duration']}")
    
    # 4. DISTRIBUTION & MEMORY
    print("📤 PHASE 4: DISTRIBUTION & MEMORY UPDATE")
    upload_package = upload_video(video_plan, script, strategy, niche=niche, timing_data=research_data["timing"])
    
    # Update memory
    memory["videos_produced"].append({
        "title": strategy['primary']['title'],
        "date": datetime.now().isoformat(),
        "quality_score": quality['score'],
        "niche": niche,
        "status": "ready_for_upload",
        "scheduled_time": upload_package['schedule']['datetime_est']
    })
    
    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=2)
        
    print(f"✅ CYCLE COMPLETE. Scheduled for: {upload_package['schedule']['datetime_est']}")
    return True

def run_autonomous_loop(interval_hours=6):
    """The 24/7 Autonomous Loop as requested in the vision document"""
    print(f"🚀 ANTIGRAVITY AI OS INITIALIZED - RUNNING EVERY {interval_hours} HOURS")
    while True:
        success = run_production_cycle()
        print(f"\nCycle finished. Sleeping for {interval_hours} hours...")
        # In a real environment, this would be a cron job or a long-running process
        # For this simulation, we'll just show the logic
        break 

if __name__ == "__main__":
    # Default to a single cycle for demonstration, but capable of full loop
    run_production_cycle()
