
"""
ANTIGRAVITY v2 - Main Orchestrator
Fully autonomous cinematic video media operating system.
16-section output format.
"""
import sys
import os
import json
from datetime import datetime

BASE_DIR = "/mnt/agents/output/antigravity_v2"
MEMORY_PATH = os.path.join(BASE_DIR, "memory", "system_memory.json")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

sys.path.insert(0, BASE_DIR)
from agents.research import research
from agents.strategy import generate_ideas, rank_ideas, select_winning_idea
from agents.script import script_agent
from agents.quality import quality_check, improve_script
from agents.voice import voice_agent
from agents.video import video_agent
from agents.upload import upload_video
from agents.analytics import analyze, identify_winners
from agents.distribution import distribute
from agents.monetization import monetize, calculate_break_even
from agents.optimization import optimize, update_memory

def ensure_dirs():
    os.makedirs(os.path.dirname(MEMORY_PATH), exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_memory():
    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, "r") as f:
            return json.load(f)
    return {
        "videos_produced": [],
        "top_performers": [],
        "failed_videos": [],
        "title_patterns_that_work": [],
        "hook_patterns_that_work": [],
        "niche_performance": {},
        "last_run": None,
        "total_revenue_estimate": 0.0,
        "audience_retention_avg": 0.0,
        "optimization_history": [],
    }

def save_memory(memory):
    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=2)

def run(niche="horror_true_crime", skip_competitor=False):
    ensure_dirs()
    memory = load_memory()

    print("=" * 70)
    print("ANTIGRAVITY v2 - AUTONOMOUS CINEMATIC VIDEO SYSTEM")
    print("=" * 70)
    print(f"\nProduction started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Niche: {niche}")
    print(f"Previous videos: {len(memory.get('videos_produced', []))}")
    print(f"Total revenue estimate: ${memory.get('total_revenue_estimate', 0):.2f}")

    # ============================================================
    # PHASE 1: RESEARCH (5 Specialist Roles)
    # ============================================================
    print("\n" + "=" * 70)
    print("PHASE 1: RESEARCH TEAM ANALYSIS")
    print("=" * 70)

    research_data = research(niche=niche, memory=memory)

    # 1. NICHE RESEARCH ANALYST
    print(f"\n[Niche Research Analyst]")
    niche_health = research_data["niche_health"]
    print(f"  Niche: {niche_health['niche']}")
    print(f"  View Potential: {niche_health['view_potential']}")
    print(f"  Retention Potential: {niche_health['retention_potential']}")
    print(f"  RPM Range: {niche_health['rpm_potential']}")
    print(f"  Competition: {niche_health['competition_intensity']}")
    print(f"  Production Cost: {niche_health['production_cost']}")
    print(f"  Overall Score: {niche_health['overall_score']}/10")
    print(f"  Verdict: {niche_health['recommendation']}")

    # 2. COMPETITOR ANALYST
    print(f"\n[Competitor Analyst]")
    print(f"  Channels Discovered: {len(research_data['competitors'])}")
    for comp in research_data['competitors'][:5]:
        print(f"    - {comp['channel']} ({comp['subscribers']} subs, {comp['avg_views']} avg views)")
    print(f"  Patterns Extracted: {len(research_data['patterns']['title_patterns'])} title patterns")

    # 3. UPLOAD TIMING ANALYST
    print(f"\n[Upload Timing Analyst]")
    timing = research_data["timing"]
    print(f"  Recommended: {timing['recommended_day']} {timing['recommended_local_time']}")
    print(f"  UTC: {timing['recommended_utc']}")
    print(f"  Confidence: {timing['confidence_level']*100:.0f}%")
    print(f"  Reason: {timing['reason']}")
    print(f"  Test Plan: {timing['testing_plan']}")

    # 4. TREND ANALYST
    print(f"\n[Trend Analyst]")
    trends = research_data["trends"]
    for k, v in trends.items():
        print(f"  {k}: {v}")

    # 5. CONTENT STRATEGIST
    print(f"\n[Content Strategist]")
    transformation = research_data["transformation"]
    print(f"  Pattern: {transformation['competitor_pattern']}")
    print(f"  Insight: {transformation['insight']}")
    print(f"  New Angle: {transformation['new_angle']}")
    print(f"  Original Content: {transformation['original_content']}")
    print(f"  Execution: {transformation['improved_execution']}")

    # ============================================================
    # PHASE 2: STRATEGY
    # ============================================================
    print("\n" + "=" * 70)
    print("PHASE 2: STRATEGY & IDEA GENERATION")
    print("=" * 70)

    ideas = generate_ideas(research_data["selected_topic"], niche=niche, transformation=research_data["transformation"])
    ranked = rank_ideas(ideas)
    strategy = select_winning_idea(ranked, research_data)

    print(f"\nGenerated {len(ideas)} ideas")
    print(f"\nWINNING IDEA:")
    print(f"  Title: {strategy['primary']['title']}")
    print(f"  Format: {strategy['primary']['format']}")
    print(f"  CTR: {strategy['primary']['ctr_potential']}/10")
    print(f"  Retention: {strategy['primary']['retention_potential']}/10")
    print(f"  RPM: ${strategy['primary']['rpm_potential']}")
    print(f"  Ease of Production: {strategy['primary']['ease_of_production']}/10")
    print(f"  Composite Score: {strategy['primary']['composite_score']}")
    print(f"  Expected Revenue/100K: ${strategy['expected_revenue_per_100k']}")
    print(f"  Production Difficulty: {strategy['production_difficulty']}")
    print(f"  Series Potential: {strategy['series_potential']}")

    # ============================================================
    # PHASE 3: SCRIPT PRODUCTION
    # ============================================================
    print("\n" + "=" * 70)
    print("PHASE 3: CINEMATIC SCRIPT PRODUCTION")
    print("=" * 70)

    script = script_agent(research_data["selected_topic"], strategy['primary']['title'], "long_form", niche=niche)

    print(f"\nCinematic Script Generated:")
    print(f"  Target Duration: {script['metadata']['target_duration']}")
    print(f"  Target Retention: {script['metadata']['target_retention']}")
    print(f"  Cinematic Grade: {script['metadata']['cinematic_grade']}")
    print(f"  Subtitle Policy: {script['metadata']['subtitle_policy']}")
    print(f"  Cut Policy: {script['metadata']['cut_policy']}")
    print(f"  Scenes: {len(script['scene_breakdown'])}")
    print(f"  Pattern Interrupts: {script['editing_plan']['pattern_interrupts']}")
    print(f"  Curiosity Loops: {script['editing_plan']['curiosity_loops']}")
    print(f"  Visual Changes/Min: {script['editing_plan']['visual_changes_per_minute']}")
    print(f"  Cuts/Min: {script['editing_plan']['cuts_per_minute']}")

    print(f"\nHOOK (0:00-0:03):")
    print(f"  {script['hook']['text']}")
    print(f"  Motion: {script['hook']['motion_direction']}")

    # ============================================================
    # PHASE 4: QUALITY CHECK
    # ============================================================
    print("\n" + "=" * 70)
    print("PHASE 4: QUALITY ASSURANCE")
    print("=" * 70)

    quality = quality_check(script)

    print(f"\nQuality Report:")
    print(f"  Grade: {quality['grade']}")
    print(f"  Score: {quality['score']}/100")
    print(f"  Passed: {'YES' if quality['passed'] else 'NO'}")
    print(f"  Cinematic Compliant: {'YES' if quality['cinematic_compliant'] else 'NO'}")

    if quality['issues']:
        print(f"\nIssues Found:")
        for issue in quality['issues']:
            print(f"    - {issue}")

    if quality['improvements']:
        print(f"\nImprovements Applied:")
        for imp in quality['improvements']:
            print(f"    - {imp}")

    if not quality['passed']:
        print("\nImproving script...")
        script = improve_script(script, quality)
        quality = quality_check(script)
        print(f"  New Grade: {quality['grade']} | New Score: {quality['score']}/100")

    # ============================================================
    # PHASE 5: VOICE PRODUCTION
    # ============================================================
    print("\n" + "=" * 70)
    print("PHASE 5: VOICE & SOUND DESIGN")
    print("=" * 70)

    voice_plan = voice_agent(script, niche=niche)

    print(f"\nVoice Profile: {voice_plan['voice_profile']['voice_type']}")
    print(f"  Speed: {voice_plan['voice_profile']['speed_wpm']} WPM")
    print(f"  Total Words: {voice_plan['total_words']}")
    print(f"  Est. Duration: {voice_plan['estimated_duration_seconds']}s")
    print(f"  Target Duration: {voice_plan['target_duration_seconds']}s")
    print(f"  Speed Adjustment: {voice_plan['speed_adjustment']}x")
    print(f"  Music Cues: {len(voice_plan['music_plan'])}")
    print(f"  SFX Cues: {len(voice_plan['sfx_plan'])}")

    # ============================================================
    # PHASE 6: VIDEO ASSEMBLY
    # ============================================================
    print("\n" + "=" * 70)
    print("PHASE 6: CINEMATIC VIDEO ASSEMBLY")
    print("=" * 70)

    video_plan = video_agent(script, voice_plan, niche=niche)

    print(f"\nFormat: {video_plan['format']} ({video_plan['resolution']})")
    print(f"  Target Duration: {video_plan['target_duration']}")
    print(f"  Color Grade: {video_plan['color_grade']}")
    print(f"  Cinematic Enforcement: {video_plan['cinematic_enforcement']}")
    print(f"  Subtitles: {video_plan['subtitle_config']['enabled']} ({video_plan['subtitle_config']['style']})")
    print(f"  Scenes: {len(video_plan['scenes'])}")
    print(f"  Transitions: {len(video_plan['transitions'])}")
    print(f"  Text Overlays: {len(video_plan['text_overlays'])}")
    print(f"  Stock Clips: {len(video_plan['stock_footage_plan']['required_clips'])}")
    print(f"  Est. Stock Cost: {video_plan['stock_footage_plan']['estimated_cost']}")
    print(f"  Render Time: {video_plan['render_pipeline']['estimated_render_time']}")

    print(f"\nThumbnail Plan:")
    thumb = video_plan['thumbnail_plan']
    print(f"  Concept: {thumb['concept']}")
    print(f"  Primary Text: '{thumb['text_primary']}'")
    print(f"  Secondary Text: '{thumb['text_secondary']}'")
    print(f"  Psychology: {thumb['psychology']}")

    # ============================================================
    # PHASE 7: UPLOAD & DISTRIBUTION
    # ============================================================
    print("\n" + "=" * 70)
    print("PHASE 7: UPLOAD & DISTRIBUTION")
    print("=" * 70)

    upload_package = upload_video(video_plan, script, strategy, niche=niche, timing_data=research_data["timing"])
    dist_plan = distribute(upload_package, video_plan, strategy)

    print(f"\nPrimary Upload:")
    print(f"  Platform: {upload_package['platform']}")
    print(f"  Schedule: {upload_package['schedule']['datetime_est']}")
    print(f"  Day: {upload_package['schedule']['day']}")
    print(f"  Local Time: {upload_package['schedule']['local_time']}")
    print(f"  UTC: {upload_package['schedule']['utc_time']}")
    print(f"  Confidence: {upload_package['schedule']['confidence_level']*100:.0f}%")
    print(f"  Rationale: {upload_package['schedule']['rationale']}")
    print(f"  Testing Plan: {upload_package['schedule']['testing_plan']}")

    print(f"\nMetadata:")
    print(f"  Title: {upload_package['metadata']['title']}")
    print(f"  Tags: {len(upload_package['metadata']['tags'])} tags")

    print(f"\nDistribution Plan:")
    for platform in dist_plan['platforms']:
        print(f"  {platform['platform']}: {platform['time']}")

    # ============================================================
    # PHASE 8: MONETIZATION
    # ============================================================
    print("\n" + "=" * 70)
    print("PHASE 8: MONETIZATION PROJECTIONS")
    print("=" * 70)

    monetization_strategy = monetize(upload_package)
    break_even = calculate_break_even(
        production_cost=180,
        rpm=monetization_strategy['projections']['views_100k']['ad_revenue'] / 100,
        expected_views=100000
    )

    print(f"\nRevenue Projections:")
    for level, data in monetization_strategy['projections'].items():
        views = level.replace("views_", "").replace("k", "000").replace("m", "000000")
        if "k" in level and "m" not in level:
            views = int(level.replace("views_", "").replace("k", "")) * 1000
        elif "m" in level:
            views = int(level.replace("views_", "").replace("m", "")) * 1000000
        print(f"  {views:,} views: ${data['total']:,.2f} total")

    print(f"\nBreak-Even Analysis:")
    print(f"  Production Cost: ${break_even['production_cost']}")
    print(f"  Break-Even Views: {break_even['break_even_views']:,}")
    print(f"  Expected Views: {break_even['expected_views']:,}")
    print(f"  Expected Revenue: ${break_even['expected_revenue']:,.2f}")
    print(f"  Profit: ${break_even['profit']:,.2f}")
    print(f"  ROI: {break_even['roi_percent']}%")

    # ============================================================
    # PHASE 9: ANALYTICS
    # ============================================================
    print("\n" + "=" * 70)
    print("PHASE 9: PERFORMANCE ANALYTICS")
    print("=" * 70)

    video_id = f"AGv2_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    analytics = analyze(video_id, upload_package, MEMORY_PATH)

    print(f"\nPerformance Summary:")
    print(f"  Video ID: {video_id}")
    print(f"  Total Views: {analytics['views']['total']:,}")
    print(f"  24h Views: {analytics['views']['first_24h']:,}")
    print(f"  CTR: {analytics['engagement']['ctr']}%")
    print(f"  Avg View Duration: {analytics['engagement']['avg_view_duration']}")
    print(f"  Retention Rate: {analytics['engagement']['retention_rate']}%")
    print(f"  Watch Time: {analytics['engagement']['watch_time_hours']:,} hours")

    print(f"\nRevenue:")
    print(f"  RPM: ${analytics['revenue']['rpm']}")
    print(f"  Ad Revenue: ${analytics['revenue']['estimated_earnings']:,.2f}")
    print(f"  Affiliate: ${analytics['revenue']['affiliate_revenue']:,.2f}")
    print(f"  Sponsorship: ${analytics['revenue']['sponsorship_value']:,.2f}")
    print(f"  TOTAL: ${analytics['revenue']['total_estimated_revenue']:,.2f}")

    print(f"\nAudience:")
    for country in analytics['audience']['top_countries']:
        print(f"  {country}")
    print(f"  Age Demo: {analytics['audience']['age_demo']}")

    # ============================================================
    # PHASE 10: OPTIMIZATION
    # ============================================================
    print("\n" + "=" * 70)
    print("PHASE 10: SELF-IMPROVEMENT LOOP")
    print("=" * 70)

    optimization = optimize(analytics)
    update_memory(MEMORY_PATH, optimization)

    print(f"\nOverall Health: {optimization['overall_health']}")
    print(f"\nRecommendations:")
    for rec in optimization['recommendations']:
        print(f"  [{rec['priority']}] {rec['area']}: {rec['action']}")
        print(f"    Expected Impact: {rec['expected_impact']}")

    print(f"\nNext Video Adjustments:")
    for adj, val in optimization['next_video_adjustments'].items():
        print(f"  {adj}: {val}")

    # ============================================================
    # SAVE OUTPUT
    # ============================================================
    print("\n" + "=" * 70)
    print("SAVING PRODUCTION PACKAGE")
    print("=" * 70)

    production_package = {
        "production_id": video_id,
        "timestamp": datetime.now().isoformat(),
        "niche": niche,
        "research_data": research_data,
        "strategy": strategy,
        "script": script,
        "voice_plan": voice_plan,
        "video_plan": video_plan,
        "upload_package": upload_package,
        "distribution_plan": dist_plan,
        "monetization": monetization_strategy,
        "analytics": analytics,
        "optimization": optimization,
        "quality_report": quality,
    }

    output_file = os.path.join(OUTPUT_DIR, f"{video_id}_production_package.json")
    with open(output_file, "w") as f:
        json.dump(production_package, f, indent=2)

    print(f"\nProduction package saved: {output_file}")

    memory = load_memory()
    memory["last_run"] = datetime.now().isoformat()
    save_memory(memory)

    print(f"\nSYSTEM STATUS:")
    print(f"  Total Videos: {len(memory['videos_produced'])}")
    print(f"  Total Revenue: ${memory['total_revenue_estimate']:,.2f}")
    print(f"  Avg Retention: {memory['audience_retention_avg']:.1f}%")
    print(f"  Last Run: {memory['last_run']}")

    print("\n" + "=" * 70)
    print("PRODUCTION CYCLE COMPLETE")
    print("=" * 70)

    return production_package

if __name__ == "__main__":
    run()
