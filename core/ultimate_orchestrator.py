"""
ANTIGRAVITY ULTIMATE - Mythos AI OS (Full Distillation Edition)
The "One System, Two Brains" MNC-style production pipeline.
Implements the full distillation, training, and RAG memory logic.
"""
import os
import json
import sys
from datetime import datetime

# Add parent directory to path to import agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.mythos_orchestrator import MythosOrchestrator
from agents.multi_ai_team import MultiAITeam
from agents.training_bridge import TrainingBridge
from agents.distillation_pipeline import DistillationPipeline
from system.memory_core import MemoryCore
from agents.quality import quality_check, improve_script
from agents.voice import voice_agent
from agents.video import video_agent
from agents.upload import upload_video
from agents.hollywood_production import apply_hollywood_standards

def run_mythos_production_cycle(niche="horror_true_crime"):
    print(f"\n🌌 [MYTHOS AI OS] INITIALIZING FULL DISTILLATION CYCLE [{datetime.now().strftime('%H:%M:%S')}]")
    
    mythos = MythosOrchestrator()
    team = MultiAITeam()
    bridge = TrainingBridge()
    memory_core = MemoryCore()
    distill_pipeline = DistillationPipeline()
    
    # 1. RAG CHECK (Check if we already solved this)
    print("\n--- PHASE 1: RAG MEMORY RETRIEVAL ---")
    past_logic = memory_core.retrieve_similar_logic("Cinematic Narrative")
    if past_logic:
        print(f"📚 [RAG] Found similar past solution. Using stored reasoning...")
    
    # 2. ROUTING & RESEARCH (Gemini)
    print("\n--- PHASE 2: STRATEGIC RESEARCH (Gemini) ---")
    research_trace = mythos.process_task("Niche & Competitor Research", 80)
    research_data = team.run_research_phase(niche)
    if research_trace["brain"] == "PRO":
        bridge.distill_reasoning(research_trace)
        memory_core.store_experience(research_trace["task"], research_trace["reasoning"], research_trace["result"])

    # 3. STORYTELLING (Claude)
    print("\n--- PHASE 3: CINEMATIC STORYTELLING (Claude) ---")
    story_trace = mythos.process_task("Cinematic Narrative Architecture", 90)
    story_data = team.run_storytelling_phase(research_data)
    if story_trace["brain"] == "PRO":
        bridge.distill_reasoning(story_trace)
        memory_core.store_experience(story_trace["task"], story_trace["reasoning"], story_trace["result"])

    # 4. REFINEMENT (GPT-OSS 120B)
    print("\n--- PHASE 4: REFINEMENT & POLISH (GPT-OSS) ---")
    refine_trace = mythos.process_task("Script Refinement & Quality Polish", 75)
    refined_data = team.run_refinement_phase(story_data["script"])
    if refine_trace["brain"] == "PRO":
        bridge.distill_reasoning(refine_trace)
        memory_core.store_experience(refine_trace["task"], refine_trace["reasoning"], refine_trace["result"])

    # 5. EXECUTION (Python)
    print("\n--- PHASE 5: TECHNICAL EXECUTION (Python) ---")
    from agents.script import script_agent
    script = script_agent({"topic": "Tinley Park 5 Massacre"}, "The Unsolved Mystery", "long_form", niche=niche)
    
    quality = quality_check(script)
    if not quality['passed']:
        print("⚠️ Quality Check Failed. Triggering Auto-Improvement...")
        script = improve_script(script, quality)
    
    # 6. HOLLYWOOD PRODUCTION
    print("\n--- PHASE 6: HOLLYWOOD CINEMATIC ASSEMBLY ---")
    voice_plan = voice_agent(script, niche=niche)
    video_plan = video_agent(script, voice_plan, niche=niche)
    hollywood_plan = apply_hollywood_standards(video_plan)
    
    # 7. DISTRIBUTION & DISTILLATION EXPORT
    print("\n--- PHASE 7: DISTRIBUTION & DISTILLATION EXPORT ---")
    upload_package = upload_video(hollywood_plan, script, {"primary": {"title": "The Unsolved Mystery"}}, niche=niche, timing_data={"recommended_day": "Tuesday", "local_time": "2:00 PM"})
    
    # Simulate the "Final Export" before losing Pro access
    export_package = bridge.prepare_export()
    
    print(f"\n✅ [MYTHOS] CYCLE COMPLETE. System has distilled intelligence and updated RAG memory.")
    print(f"📦 Final Standalone Package: {export_package}")
    return True

if __name__ == "__main__":
    run_mythos_production_cycle()
