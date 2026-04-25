
"""
Voice Agent v2
Generates audio plan with cinematic sound design.
"""

VOICE_PROFILES = {
    "horror_true_crime": {
        "voice_type": "deep_male",
        "pacing": "measured_with_pauses",
        "emotion": "gravitas_with_tension",
        "pitch_range": "low_mid",
        "speed_wpm": 145,
        "pause_strategy": "2s after hook, 1.5s before reveals, 0.5s between sentences",
        "tools": ["elevenlabs_v2", "azure_neural", "coqui_tts"],
    },
    "haunted_history": {
        "voice_type": "authoritative_male",
        "pacing": "steady_dramatic",
        "emotion": "scholarly_dread",
        "pitch_range": "mid_low",
        "speed_wpm": 140,
        "pause_strategy": "1.5s between paragraphs, emphasis on dates and names",
        "tools": ["elevenlabs_v2", "google_wavenet"],
    },
    "mystery_crime": {
        "voice_type": "dramatic_female",
        "pacing": "dynamic",
        "emotion": "building_outrage",
        "pitch_range": "mid_high",
        "speed_wpm": 155,
        "pause_strategy": "Dramatic pauses before betrayals, quick pace during action",
        "tools": ["elevenlabs_v2", "murf_ai"],
    }
}

def voice_agent(script, niche="horror_true_crime"):
    """Generate voice plan and audio metadata."""
    profile = VOICE_PROFILES.get(niche, VOICE_PROFILES["horror_true_crime"])
    total_words = _count_script_words(script)
    estimated_duration = total_words / profile["speed_wpm"] * 60

    return {
        "voice_profile": profile,
        "total_words": total_words,
        "estimated_duration_seconds": round(estimated_duration, 1),
        "target_duration_seconds": 660,
        "speed_adjustment": round(660 / estimated_duration, 2) if estimated_duration > 0 else 1.0,
        "audio_segments": _generate_audio_segments(script, profile),
        "music_plan": _generate_music_plan(),
        "sfx_plan": _generate_sfx_plan(),
        "output_file": "voice_track.mp3",
        "format": "mp3_192kbps_stereo",
    }

def _count_script_words(script):
    count = 0
    hook = script.get("hook", {})
    count += len(hook.get("text", "").split())
    stakes = script.get("stakes_setup", {})
    count += len(stakes.get("text", "").split())
    backstory = script.get("backstory", {})
    for seg in backstory.get("segments", []):
        count += len(seg.get("text", "").split())
    investigation = script.get("investigation", {})
    for seg in investigation.get("segments", []):
        count += len(seg.get("text", "").split())
    revelation = script.get("revelation", {})
    count += len(revelation.get("text", "").split())
    aftermath = script.get("aftermath", {})
    count += len(aftermath.get("text", "").split())
    cta = script.get("cta", {})
    count += len(cta.get("text", "").split())
    return count

def _generate_audio_segments(script, profile):
    return [
        {"name": "hook", "timestamp": "0:00-0:03", "delivery": "Whispered, intimate", "volume": "85%", "effect": "slight_reverb", "instruction": "Speak as if telling a secret. Pause 2s after."},
        {"name": "stakes", "timestamp": "0:03-0:15", "delivery": "Building intensity", "volume": "90%", "effect": "none", "instruction": "Speed up on 'warning'. Drop to silence after."},
        {"name": "backstory", "timestamp": "0:15-1:30", "delivery": "Conversational but weighted", "volume": "95%", "effect": "none", "instruction": "Warm tone for victim. Tighten on 'trap'."},
        {"name": "investigation", "timestamp": "1:30-7:00", "delivery": "Methodical, then accelerating", "volume": "95%", "effect": "none", "instruction": "Slow on evidence. Fast on connections."},
        {"name": "revelation", "timestamp": "7:00-9:00", "delivery": "Revelatory, then urgent", "volume": "100%", "effect": "slight_compression", "instruction": "Peak volume on 'digital footprint'."},
        {"name": "aftermath", "timestamp": "9:00-10:30", "delivery": "Somber, then chilling", "volume": "90%", "effect": "subtle_reverb", "instruction": "Gentle on family. Ice cold on final line."},
        {"name": "cta", "timestamp": "10:30-11:00", "delivery": "Confident, inviting", "volume": "95%", "effect": "none", "instruction": "Warm smile in voice. Clear CTA."},
    ]

def _generate_music_plan():
    return [
        {"segment": "hook", "music": "low_drone_heartbeat", "volume": "30%", "fade": "in"},
        {"segment": "backstory", "music": "melancholic_piano", "volume": "25%", "fade": "smooth"},
        {"segment": "investigation", "music": "tension_building_strings", "volume": "35%", "fade": "gradual"},
        {"segment": "revelation", "music": "crescendo_orchestral", "volume": "45%", "fade": "peak"},
        {"segment": "aftermath", "music": "solo_piano_minor", "volume": "20%", "fade": "out"},
        {"segment": "cta", "music": "ambient_pad", "volume": "15%", "fade": "out"},
    ]

def _generate_sfx_plan():
    return [
        {"timestamp": "0:02", "sfx": "hard_cut_impact", "volume": "80%"},
        {"timestamp": "0:30", "sfx": "phone_ring_vintage", "volume": "60%"},
        {"timestamp": "1:00", "sfx": "bass_drop_sub", "volume": "70%"},
        {"timestamp": "1:25", "sfx": "single_piano_note", "volume": "50%"},
        {"timestamp": "2:15", "sfx": "camera_shutter_rapid", "volume": "40%"},
        {"timestamp": "3:45", "sfx": "color_shift_tone", "volume": "55%"},
        {"timestamp": "5:15", "sfx": "digital_glitch", "volume": "45%"},
        {"timestamp": "6:45", "sfx": "silence_then_piano", "volume": "50%"},
        {"timestamp": "7:30", "sfx": "data_cascade_digital", "volume": "60%"},
        {"timestamp": "10:15", "sfx": "slow_motion_whoosh", "volume": "65%"},
    ]
