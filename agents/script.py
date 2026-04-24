
"""
Script Agent v2
Creates CINEMATIC video workflows only. Every output is a video plan.
No image-only deliverables.
"""

def script_agent(topic, title, format_type="long_form", competitor_patterns=None, niche="horror_true_crime"):
    """Generate a full cinematic script with scene breakdowns."""

    if format_type == "long_form":
        return _generate_long_form(topic, title, niche)
    else:
        return _generate_short_form(topic, title)

def _generate_long_form(topic, title, niche):
    """Generate 8-15 minute cinematic script."""
    base_topic = topic["topic"]

    script = {
        "metadata": {
            "target_duration": "10:00-12:00",
            "target_retention": "55%+",
            "word_count_target": 1500,
            "tone": "Serious, intimate, building tension",
            "voice_pacing": "Slightly faster during setup, slower during reveals",
            "cinematic_grade": "MANDATORY - Every scene must have motion",
            "subtitle_policy": "ALL DIALOGUE MUST HAVE SUBTITLES",
            "cut_policy": "CUT EVERY 2-5 SECONDS MAXIMUM",
        },
        "hook": {
            "timestamp": "0:00-0:03",
            "text": f"She walked into that house expecting a sale. She never walked out. This is the story of {base_topic}.",
            "visual": "Darkened house exterior, single light in window, SLOW ZOOM IN",
            "motion_direction": "Camera pushes forward through darkness",
            "audio": "Low drone + subtle heartbeat",
            "pattern_interrupt": "HARD CUT from black to crime scene photo at 0:02",
            "subtitle_style": "Bold white, slight shadow, fade in",
        },
        "stakes_setup": {
            "timestamp": "0:03-0:15",
            "text": f"In 2008, a 24-year-old real estate agent thought she was showing a property to potential buyers. Instead, she walked into a trap that remains unsolved to this day. {base_topic} isn't just a cold case. It's a warning.",
            "visual": "Split screen: happy photo vs crime scene tape, DISSOLVE BETWEEN",
            "motion_direction": "Left panel pushes right, right panel pulls back",
            "audio": "Music swells, then drops to silence",
            "pattern_interrupt": "SUDDEN SILENCE at 0:12",
            "subtitle_style": "Standard, emotional emphasis on 'warning'",
        },
        "backstory": {
            "timestamp": "0:15-1:30",
            "segments": [
                {
                    "timestamp": "0:15-0:45",
                    "text": f"{base_topic.split(':')[0] if ':' in base_topic else base_topic} was 24 years old, building her career in Victoria, Canada. Colleagues described her as ambitious, kind, and careful. On February 2nd, 2008, she received a call from a couple wanting to view a luxury property.",
                    "visual": "Victoria BC map animation PUSHING IN, photo of victim FADING UP, phone call visualization with RINGING MOTION",
                    "motion_direction": "Map zooms to street level, camera orbits victim photo",
                    "pattern_interrupt": "Phone RING sound effect + SCREEN SHAKE at 0:30",
                    "cut_count": 6,
                    "subtitle_style": "Standard",
                },
                {
                    "timestamp": "0:45-1:15",
                    "text": "The couple used a prepaid phone registered to a fake name. They knew exactly what they were doing. They chose a property that was vacant, isolated, and perfect for what they had planned.",
                    "visual": "Aerial view of property with CAMERA DESCENDING, phone trace animation with DATA FLOW, red X marking location with PULSE",
                    "motion_direction": "Drone shot descending to property, data streams horizontally",
                    "pattern_interrupt": "Screen shake + BASS DROP at 1:00",
                    "cut_count": 5,
                    "subtitle_style": "Red emphasis on 'fake name' and 'perfect'",
                },
                {
                    "timestamp": "1:15-1:30",
                    "text": "When she didn't show up for dinner with her boyfriend that evening, he knew something was wrong. He went to the property. What he found would haunt him for the rest of his life.",
                    "visual": "Clock ticking animation with HANDS SPINNING, boyfriend silhouette WALKING, door opening with CREAK MOTION",
                    "motion_direction": "Camera follows boyfriend silhouette, pushes through door",
                    "pattern_interrupt": "Black screen with text 'What he found' at 1:25",
                    "cut_count": 4,
                    "subtitle_style": "Large, dramatic on final line",
                },
            ]
        },
        "investigation": {
            "timestamp": "1:30-7:00",
            "segments": [
                {
                    "timestamp": "1:30-3:00",
                    "text": "She had been stabbed multiple times. The crime scene showed signs of planning, not passion. The killers had brought their own weapons, cleaned up after themselves, and vanished without a trace. But here's where it gets strange.",
                    "visual": "Crime scene diagram with MARKERS APPEARING SEQUENTIALLY, evidence markers with NUMBER COUNT-UP, knife silhouette with SLOW ROTATION",
                    "motion_direction": "Camera pans across crime scene, pushes into evidence",
                    "pattern_interrupt": "Fast zoom into evidence photo at 2:15",
                    "curiosity_loop": "What strange detail did police find?",
                    "cut_count": 8,
                    "subtitle_style": "Red stamp on 'strange'",
                },
                {
                    "timestamp": "3:00-4:30",
                    "text": "The couple was seen by witnesses leaving the property. They were described as well-dressed, calm, and completely unremarkable. Professional. But professional killers don't typically target real estate agents showing houses. Unless the house wasn't the target. Unless she was.",
                    "visual": "Police sketch animation with LINES DRAWING, witness interview clips with B&W TREATMENT, suspect board with PHOTOS PINNING",
                    "motion_direction": "Sketch draws itself, camera pushes into suspect board",
                    "pattern_interrupt": "Color shift to RED at 3:45 when 'Unless she was' is spoken",
                    "curiosity_loop": "Who wanted her dead?",
                    "cut_count": 9,
                    "subtitle_style": "Red glow on 'Unless she was'",
                },
                {
                    "timestamp": "4:30-6:00",
                    "text": "Police investigated her boyfriend. He was the last person to see her alive. He had an alibi, but it was thin. He passed a polygraph, but those aren't admissible in court for a reason. And then there were the rumors. Rumors about a drug cartel connection. Rumors about a previous relationship. Rumors that someone in her circle knew exactly what was coming.",
                    "visual": "Relationship web diagram with LINES CONNECTING, polygraph needle animation with JITTER, newspaper headlines with TYPEWRITER EFFECT",
                    "motion_direction": "Web expands outward, needle shakes, headlines type on",
                    "pattern_interrupt": "Glitch effect on 'rumors' at 5:15",
                    "curiosity_loop": "Which rumor was true?",
                    "cut_count": 10,
                    "subtitle_style": "Glitch text on 'rumors'",
                },
                {
                    "timestamp": "6:00-7:00",
                    "text": "Eighteen years later, no one has been charged. The case remains active, but the trail is colder than the Canadian winter where it happened. Or is it? Because in 2026, something changed. Something that might finally crack this case wide open.",
                    "visual": "Calendar flipping 2008-2026 with PAGES TEARING, snow falling with PARTICLES, file folder marked 'ACTIVE' with STAMP",
                    "motion_direction": "Calendar pages fly past camera, snow falls toward lens",
                    "pattern_interrupt": "Sudden silence at 6:45, then single piano note",
                    "curiosity_loop": "What changed in 2026?",
                    "cut_count": 6,
                    "subtitle_style": "Large, building anticipation",
                },
            ]
        },
        "revelation": {
            "timestamp": "7:00-9:00",
            "text": "In February 2026, cold case investigators announced they were pursuing new digital evidence. The prepaid phone used to contact her? Modern forensic technology can now extract data that was impossible to access in 2008. Cell tower records, GPS metadata, even deleted messages. The killers left a digital footprint. They just didn't know it yet.",
            "visual": "Phone data extraction animation with BINARY RAIN, cell tower map with SIGNAL PULSING, binary code rain with VERTICAL SCROLL",
            "motion_direction": "Data cascades down screen, signals pulse outward from towers",
            "pattern_interrupt": "Matrix-style data cascade at 7:30",
            "cut_count": 8,
            "subtitle_style": "Neon green, tech style",
        },
        "aftermath": {
            "timestamp": "9:00-10:30",
            "text": "Her family still waits. Her mother posts updates every anniversary. Her colleagues still remember the young woman who loved real estate and trusted too easily. And somewhere out there, two people who looked like any other couple house-hunting on a Saturday afternoon are living with what they did. Or maybe they're still killing. Because here's the terrifying truth: whoever murdered her knew her schedule, knew the property, and knew exactly how to disappear. That's not random. That's personal. And personal killers don't stop at one.",
            "visual": "Family photo montage with SLOW DISSOLVES, candle vigil with FLICKERING, dark silhouette walking away with DEPTH",
            "motion_direction": "Photos dissolve slowly, candle flames flicker, silhouette walks away from camera",
            "pattern_interrupt": "Slow motion on 'personal killers don't stop at one' at 10:15",
            "cut_count": 7,
            "subtitle_style": "Bold white, red glow on final line",
        },
        "cta": {
            "timestamp": "10:30-11:00",
            "text": "If you know anything about this case, contact Victoria Crime Stoppers. And if you want more stories like this, subscribe. We cover the cases that keep investigators awake at night. Because some stories demand to be told. Even if the ending hasn't been written yet.",
            "visual": "Contact info overlay with TYPE-ON, subscribe animation with BUTTON PULSE, next video teaser with THUMBNAIL WIPE",
            "motion_direction": "Text types on, button pulses, thumbnail wipes in from right",
            "cut_count": 3,
            "subtitle_style": "Standard, warm tone",
        },
        "scene_breakdown": [
            {"scene": 1, "time": "0:00-0:15", "type": "Hook", "visuals": 3, "audio_cues": 2, "cuts": 4, "motion": "Camera push + hard cut"},
            {"scene": 2, "time": "0:15-1:30", "type": "Backstory", "visuals": 8, "audio_cues": 4, "cuts": 15, "motion": "Map zoom + orbit + descend"},
            {"scene": 3, "time": "1:30-3:00", "type": "Investigation", "visuals": 6, "audio_cues": 3, "cuts": 8, "motion": "Pan + push into evidence"},
            {"scene": 4, "time": "3:00-4:30", "type": "Investigation", "visuals": 7, "audio_cues": 4, "cuts": 9, "motion": "Sketch draws + push into board"},
            {"scene": 5, "time": "4:30-6:00", "type": "Investigation", "visuals": 8, "audio_cues": 5, "cuts": 10, "motion": "Web expands + needle shakes"},
            {"scene": 6, "time": "6:00-7:00", "type": "Transition", "visuals": 5, "audio_cues": 3, "cuts": 6, "motion": "Pages fly + snow falls"},
            {"scene": 7, "time": "7:00-9:00", "type": "Revelation", "visuals": 10, "audio_cues": 6, "cuts": 8, "motion": "Data cascade + signal pulse"},
            {"scene": 8, "time": "9:00-10:30", "type": "Aftermath", "visuals": 7, "audio_cues": 4, "cuts": 7, "motion": "Slow dissolves + silhouette walk"},
            {"scene": 9, "time": "10:30-11:00", "type": "CTA", "visuals": 4, "audio_cues": 2, "cuts": 3, "motion": "Type-on + pulse + wipe"},
        ],
        "editing_plan": {
            "total_scenes": 9,
            "pattern_interrupts": 9,
            "curiosity_loops": 4,
            "visual_changes_per_minute": 4.2,
            "cuts_per_minute": 12,
            "music_changes": 5,
            "color_grading": "Cool blues for backstory, warm amber for investigation, desaturated for aftermath",
            "text_overlays": 23,
            "sound_effects": 15,
            "subtitle_tracks": 1,
            "subtitle_style": "Bold white, slight shadow, consistent throughout",
            "motion_graphics": 8,
            "cinematic_enforcement": "EVERY SCENE MUST HAVE CAMERA MOTION OR OBJECT MOTION",
        }
    }

    return script

def _generate_short_form(topic, title):
    """Generate 20-40 second cinematic Short."""
    base_topic = topic["topic"]
    return {
        "metadata": {
            "target_duration": "0:30-0:40",
            "format": "vertical_9_16",
            "cinematic_grade": "MANDATORY - Fast cuts, heavy motion",
            "subtitle_policy": "ALL TEXT ON SCREEN - sound-off viewing",
            "cut_policy": "CUT EVERY 1-2 SECONDS",
        },
        "hook": {
            "text": f"She showed a house to a couple. They were actually killers. {base_topic}.",
            "visual": "Quick cuts: house EXTERIOR PUSH, couple SILHOUETTE, knife silhouette FLASH",
            "motion": "Rapid push cuts",
            "duration": "0:00-0:03",
        },
        "body": {
            "text": f"18 years unsolved. New DNA tech in 2026 might finally catch them. The case isn't over.",
            "visual": "DNA helix SPINNING, calendar 2008-2026 FLIPPING, suspect sketch DRAWING",
            "motion": "Helix rotates, calendar pages tear, sketch lines appear",
            "duration": "0:03-0:08",
        },
        "cta": {
            "text": "Follow for more unsolved cases.",
            "visual": "Subscribe button PULSING, arrow POINTING",
            "motion": "Button pulse + arrow bounce",
            "duration": "0:08-0:10",
        }
    }
