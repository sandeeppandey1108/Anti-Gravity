
"""
Optimization Agent v2
Analyzes performance and generates improvement strategies.
"""
from datetime import datetime

def optimize(analytics_data, memory_path=None):
    """Generate optimization recommendations."""

    engagement = analytics_data.get("engagement", {})
    content_analysis = analytics_data.get("content_analysis", {})

    recommendations = []

    retention = engagement.get("retention_rate", 0)
    if retention < 50:
        recommendations.append({
            "priority": "CRITICAL",
            "area": "retention",
            "issue": f"Retention at {retention}% - below 50% threshold",
            "action": "Add stronger hook in first 15s. Reduce backstory length by 30%.",
            "expected_impact": "+8-12% retention"
        })
    elif retention < 60:
        recommendations.append({
            "priority": "HIGH",
            "area": "retention",
            "issue": f"Retention at {retention}% - good but not great",
            "action": "Add curiosity loop at 50% mark. Tighten investigation segments.",
            "expected_impact": "+5-8% retention"
        })

    ctr = engagement.get("ctr", 0)
    if ctr < 5:
        recommendations.append({
            "priority": "HIGH",
            "area": "ctr",
            "issue": f"CTR at {ctr}% - below 5%",
            "action": "Redesign thumbnail with stronger contrast. Test title variations.",
            "expected_impact": "+1-2% CTR"
        })

    drop_points = content_analysis.get("retention_drop_points", [])
    for drop in drop_points:
        recommendations.append({
            "priority": "MEDIUM",
            "area": "pacing",
            "issue": f"Retention drop at {drop}",
            "action": f"Add pattern interrupt or visual change at {drop}",
            "expected_impact": "+3-5% retention in segment"
        })

    strongest = content_analysis.get("strongest_segment", "")
    if strongest:
        recommendations.append({
            "priority": "LOW",
            "area": "scaling",
            "issue": f"Strong performance in {strongest}",
            "action": f"Create follow-up video expanding on {strongest} content",
            "expected_impact": "Leverage proven format"
        })

    sentiment = content_analysis.get("comment_sentiment", "")
    if "negative" in sentiment:
        recommendations.append({
            "priority": "HIGH",
            "area": "content",
            "issue": "Negative comment sentiment detected",
            "action": "Review for factual errors or insensitive framing",
            "expected_impact": "Improve community trust"
        })

    return {
        "overall_health": "STRONG" if retention > 55 and ctr > 5 else "NEEDS_WORK",
        "recommendations": recommendations,
        "next_video_adjustments": _generate_adjustments(recommendations),
    }

def _generate_adjustments(recommendations):
    adjustments = {
        "hook_strength": "maintain",
        "backstory_length": "maintain",
        "pattern_interrupts": "maintain",
        "curiosity_loops": "maintain",
        "visual_density": "maintain",
        "cta_clarity": "maintain",
    }

    for rec in recommendations:
        if "hook" in rec["action"].lower():
            adjustments["hook_strength"] = "strengthen"
        if "backstory" in rec["action"].lower():
            adjustments["backstory_length"] = "reduce"
        if "pattern interrupt" in rec["action"].lower():
            adjustments["pattern_interrupts"] = "increase"
        if "curiosity loop" in rec["action"].lower():
            adjustments["curiosity_loops"] = "increase"
        if "visual" in rec["action"].lower():
            adjustments["visual_density"] = "increase"

    return adjustments

def update_memory(memory_path, optimization_data):
    """Update system memory with optimization insights."""
    import json
    import os

    if not os.path.exists(memory_path):
        return

    with open(memory_path, "r") as f:
        memory = json.load(f)

    memory["optimization_history"] = memory.get("optimization_history", [])
    memory["optimization_history"].append({
        "date": datetime.now().isoformat(),
        "recommendations": optimization_data["recommendations"],
        "adjustments": optimization_data["next_video_adjustments"],
    })

    with open(memory_path, "w") as f:
        json.dump(memory, f, indent=2)
