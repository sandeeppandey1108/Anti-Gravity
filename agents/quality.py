
"""
Quality Agent v2
Ensures CINEMATIC video output. Rejects image-only or static content.
"""

def quality_check(script):
    """
    Comprehensive quality check with cinematic enforcement.
    Returns: dict with passed, score, issues, improvements, grade
    """
    issues = []
    improvements = []
    score = 100.0

    # CINEMATIC ENFORCEMENT - CRITICAL
    metadata = script.get("metadata", {})
    if metadata.get("cinematic_grade", "") != "MANDATORY - Every scene must have motion":
        issues.append("CRITICAL: Not a cinematic video workflow - static content detected")
        score -= 40
        improvements.append("Add camera motion or object motion to EVERY scene")

    # Check subtitle policy
    if "subtitle_policy" not in metadata or "ALL DIALOGUE MUST HAVE SUBTITLES" not in metadata.get("subtitle_policy", ""):
        issues.append("CRITICAL: Missing subtitle track - violates cinematic rules")
        score -= 20
        improvements.append("Add full subtitle track for all dialogue")

    # Check cut policy
    if "cut_policy" not in metadata or "CUT EVERY 2-5 SECONDS" not in metadata.get("cut_policy", ""):
        issues.append("CRITICAL: Cut frequency too low - will lose attention")
        score -= 15
        improvements.append("Increase cuts to every 2-5 seconds maximum")

    # Hook in first 3 seconds
    hook = script.get("hook", {})
    if not hook:
        issues.append("CRITICAL: No hook section found")
        score -= 30
    else:
        hook_text = hook.get("text", "")
        if len(hook_text) > 200:
            issues.append("Hook too long - must be punchy within 3 seconds")
            score -= 15
            improvements.append("Trim hook to under 25 words")

        trigger_words = ["never", "killed", "murdered", "vanished", "secret", "truth", "warning"]
        if not any(w in hook_text.lower() for w in trigger_words):
            issues.append("Hook lacks emotional trigger word")
            score -= 10
            improvements.append("Add trigger word: never, killed, vanished, secret")

        # Check motion direction
        if "motion_direction" not in hook:
            issues.append("Hook missing camera motion direction")
            score -= 10
            improvements.append("Add explicit camera motion: push, pull, orbit, pan")

    # Pattern interrupts
    editing_plan = script.get("editing_plan", {})
    pattern_interrupts = editing_plan.get("pattern_interrupts", 0)
    if pattern_interrupts < 5:
        issues.append(f"Only {pattern_interrupts} pattern interrupts - need minimum 5")
        score -= 15
        improvements.append("Add pattern interrupt every 60-90 seconds")

    # Curiosity loops
    curiosity_loops = editing_plan.get("curiosity_loops", 0)
    if curiosity_loops < 3:
        issues.append(f"Only {curiosity_loops} curiosity loops - need minimum 3")
        score -= 10
        improvements.append("Add curiosity loop at 25%, 50%, and 75% marks")

    # Visual density
    visual_changes = editing_plan.get("visual_changes_per_minute", 0)
    if visual_changes < 3:
        issues.append(f"Only {visual_changes} visual changes/min - need 3+")
        score -= 10
        improvements.append("Increase visual changes to 3+ per minute")

    # Cuts per minute
    cuts_per_minute = editing_plan.get("cuts_per_minute", 0)
    if cuts_per_minute < 8:
        issues.append(f"Only {cuts_per_minute} cuts/min - need 8+ for cinematic pacing")
        score -= 10
        improvements.append("Increase cuts to 8+ per minute")

    # CTA presence
    cta = script.get("cta", {})
    if not cta:
        issues.append("No CTA section")
        score -= 10
        improvements.append("Add CTA with subscribe + affiliate mention")

    # Scene breakdown completeness
    scene_breakdown = script.get("scene_breakdown", [])
    if len(scene_breakdown) < 5:
        issues.append(f"Only {len(scene_breakdown)} scenes - need detailed breakdown")
        score -= 10
        improvements.append("Break into 7-10 distinct scenes")

    # Check each scene has motion
    for scene in scene_breakdown:
        if "motion" not in scene or not scene["motion"]:
            issues.append(f"Scene {scene.get('scene', '?')} missing motion direction")
            score -= 5
            improvements.append(f"Add camera motion to scene {scene.get('scene', '?')}")

    passed = score >= 75

    return {
        "passed": passed,
        "score": round(max(0, score), 1),
        "issues": issues,
        "improvements": improvements,
        "grade": "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F",
        "cinematic_compliant": score >= 85,
    }

def improve_script(script, feedback):
    """Apply improvements based on quality feedback."""
    improved = script.copy()

    for improvement in feedback.get("improvements", []):
        if "trigger word" in improvement.lower():
            hook = improved.get("hook", {})
            hook["text"] = hook.get("text", "") + " The truth is darker than you think."
            improved["hook"] = hook

        if "pattern interrupt" in improvement.lower():
            editing = improved.get("editing_plan", {})
            editing["pattern_interrupts"] = editing.get("pattern_interrupts", 0) + 2
            improved["editing_plan"] = editing

        if "curiosity loop" in improvement.lower():
            editing = improved.get("editing_plan", {})
            editing["curiosity_loops"] = editing.get("curiosity_loops", 0) + 1
            improved["editing_plan"] = editing

        if "camera motion" in improvement.lower() or "motion" in improvement.lower():
            # Add default motion to scenes missing it
            for scene in improved.get("scene_breakdown", []):
                if "motion" not in scene or not scene["motion"]:
                    scene["motion"] = "Slow push in or gentle orbit"

    return improved
