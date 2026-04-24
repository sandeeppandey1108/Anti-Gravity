
"""
Video Agent v2
Assembles CINEMATIC video only. No image-only outputs.
"""

def video_agent(script, voice_plan, niche="horror_true_crime"):
    """Generate complete cinematic video assembly plan."""
    scene_breakdown = script.get("scene_breakdown", [])
    editing_plan = script.get("editing_plan", {})

    return {
        "format": "youtube_1080p",
        "resolution": "1920x1080",
        "fps": 24,
        "aspect_ratio": "16:9",
        "target_duration": script.get("metadata", {}).get("target_duration", "10:00-12:00"),
        "color_grade": editing_plan.get("color_grading", "neutral"),
        "cinematic_enforcement": "VIDEO ONLY - Every frame must have motion",
        "subtitle_config": {
            "enabled": True,
            "style": "Bold white, slight shadow, consistent throughout",
            "animation": "Fade in/out per sentence",
            "position": "Bottom center, safe margin",
        },
        "scenes": _build_scenes(scene_breakdown),
        "transitions": _build_transitions(scene_breakdown),
        "text_overlays": _build_text_overlays(script),
        "stock_footage_plan": _build_stock_plan(niche),
        "render_pipeline": _build_render_pipeline(),
        "output_file": "final_video.mp4",
        "thumbnail_plan": _build_thumbnail_plan(script),
    }

def _build_scenes(scene_breakdown):
    scenes = []
    for scene in scene_breakdown:
        scenes.append({
            "scene_number": scene["scene"],
            "timecode": scene["time"],
            "type": scene["type"],
            "visual_count": scene["visuals"],
            "audio_cues": scene["audio_cues"],
            "cuts": scene.get("cuts", 5),
            "motion": scene.get("motion", "Camera push or object motion"),
            "editing_notes": _get_scene_notes(scene["type"]),
            "required_assets": _get_scene_assets(scene["type"]),
        })
    return scenes

def _get_scene_notes(scene_type):
    notes = {
        "Hook": "Start black. Fade in from 0. Hard cut at 2s. No music for 1s. CAMERA MUST PUSH IN.",
        "Backstory": "Slow pans only. No fast movement. Let viewer settle. GENTLE ORBIT or PUSH.",
        "Investigation": "Quick cuts acceptable. Use motion graphics for data. PAN + TILT combinations.",
        "Transition": "Visual metaphor - clock, calendar, seasons changing. MATCH CUT on motion.",
        "Revelation": "Build to peak. Hold on key image for 3s. Let it breathe. SLOW ZOOM on reveal.",
        "Aftermath": "Slow everything down. Longer takes. Emotional weight. STATIC with SUBTLE BREATH.",
        "CTA": "Clean graphics. Clear text. Brighten overall grade by 10%. TYPE-ON animation.",
    }
    return notes.get(scene_type, "Standard editing with camera motion")

def _get_scene_assets(scene_type):
    assets = {
        "Hook": ["dark_house_exterior", "crime_scene_tape", "victim_photo"],
        "Backstory": ["victim_photos", "location_photos", "family_photos", "phone_visual"],
        "Investigation": ["police_docs", "evidence_photos", "suspect_board", "maps"],
        "Transition": ["calendar_animation", "time_lapse"],
        "Revelation": ["tech_visuals", "dna_animation", "data_visualization"],
        "Aftermath": ["candle_vigil", "family_photos", "memorial"],
        "CTA": ["subscribe_button", "contact_info", "next_video_thumb"],
    }
    return assets.get(scene_type, ["stock_footage"])

def _build_transitions(scene_breakdown):
    transitions = []
    for i in range(len(scene_breakdown) - 1):
        current = scene_breakdown[i]["type"]
        next_scene = scene_breakdown[i + 1]["type"]
        transition_type = "fade"
        if current == "Hook" and next_scene == "Backstory":
            transition_type = "hard_cut"
        elif current == "Investigation" and next_scene == "Revelation":
            transition_type = "whip_pan"
        elif current == "Revelation" and next_scene == "Aftermath":
            transition_type = "slow_fade"
        elif "Transition" in current:
            transition_type = "match_cut"
        transitions.append({"from": current, "to": next_scene, "type": transition_type, "duration": "0.5s"})
    return transitions

def _build_text_overlays(script):
    return [
        {"timestamp": "0:00-0:03", "text": script.get("hook", {}).get("text", "")[:50] + "...", "style": "bold_white_with_shadow", "position": "center", "animation": "fade_in_hold"},
        {"timestamp": "2:15-2:20", "text": "EVIDENCE #1", "style": "red_stamp", "position": "top_left", "animation": "stamp_in"},
        {"timestamp": "5:15-5:20", "text": "THE RUMORS", "style": "glitch_text", "position": "center", "animation": "glitch_appear"},
        {"timestamp": "7:30-7:35", "text": "2026 BREAKTHROUGH", "style": "neon_green", "position": "center", "animation": "pulse_in"},
        {"timestamp": "10:15-10:20", "text": "PERSONAL KILLERS DON'T STOP AT ONE", "style": "bold_white_red_glow", "position": "center", "animation": "slow_zoom"},
    ]

def _build_stock_plan(niche):
    return {
        "sources": ["storyblocks", "artgrid", "filmpac", "pexels"],
        "estimated_cost": "$45-80",
        "required_clips": [
            {"type": "dark_suburban_house", "duration": "5s", "mood": "ominous", "motion": "slow_push"},
            {"type": "victorian_canada_street", "duration": "8s", "mood": "nostalgic", "motion": "gentle_pan"},
            {"type": "real_estate_sign", "duration": "3s", "mood": "neutral", "motion": "static_with_breath"},
            {"type": "police_investigation_night", "duration": "10s", "mood": "tense", "motion": "handheld_shake"},
            {"type": "dna_lab_microscope", "duration": "6s", "mood": "clinical", "motion": "rack_focus"},
            {"type": "digital_data_stream", "duration": "8s", "mood": "tech", "motion": "vertical_scroll"},
            {"type": "candle_vigil_night", "duration": "7s", "mood": "somber", "motion": "slow_orbit"},
            {"type": "silhouette_walking_away", "duration": "5s", "mood": "mysterious", "motion": "tracking_shot"},
        ],
        "ai_generated_assets": [
            "suspect_composite_sketch",
            "crime_scene_diagram",
            "phone_data_visualization",
            "relationship_web_graphic",
        ],
    }

def _build_render_pipeline():
    return {
        "software": "ffmpeg + python_moviepy",
        "codec": "h264_nvenc",
        "bitrate": "8Mbps",
        "audio_codec": "aac_192kbps",
        "color_space": "rec709",
        "output_format": "mp4",
        "estimated_render_time": "12-18 minutes",
        "quality_preset": "slow",
    }

def _build_thumbnail_plan(script):
    return {
        "concept": "Face with extreme emotion + dark background + red accent",
        "layout": "Rule of thirds - subject left, text right",
        "background": "Darkened house exterior with single lit window",
        "subject": "Silhouette of woman at door, back to camera",
        "text_primary": "18 YEARS",
        "text_secondary": "NO ANSWERS",
        "text_style": "Bold sans-serif, red glow, slight distortion",
        "accent": "Red crime scene tape across bottom third",
        "expression": "Mystery and dread",
        "color_palette": ["#0a0a0a", "#ff1a1a", "#ffffff", "#1a1a2e"],
        "psychology": "Curiosity gap + fear + unsolved mystery = high CTR",
    }
