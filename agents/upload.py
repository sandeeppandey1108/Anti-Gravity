
"""
Upload Agent v2
Handles platform upload with timing analysis integration.
"""
from datetime import datetime, timedelta

def upload_video(video_plan, script, strategy, niche="horror_true_crime", timing_data=None):
    """Generate complete upload package with timing analysis."""

    title = strategy["primary"]["title"]

    # Use timing data from research if available
    if timing_data:
        schedule = _calculate_optimal_time_from_analysis(timing_data)
    else:
        schedule = _calculate_default_time()

    return {
        "platform": "youtube",
        "schedule": schedule,
        "metadata": _generate_metadata(title, script, niche),
        "thumbnail": video_plan.get("thumbnail_plan", {}),
        "end_screen": _generate_end_screen(),
        "cards": _generate_cards(),
        "playlist": _select_playlist(niche),
        "monetization": _configure_monetization(),
        "seo": _generate_seo(title, niche),
        "repurpose_plan": _generate_repurpose_plan(strategy, script),
    }

def _calculate_optimal_time_from_analysis(timing_data):
    """Calculate upload time from research analysis."""
    peak = timing_data.get("recommended_day", "Tuesday")
    local_time = timing_data.get("recommended_local_time", "2:00-4:00 PM")
    utc_time = timing_data.get("recommended_utc", "19:00-21:00")
    confidence = timing_data.get("confidence_level", 0.85)

    now = datetime.now()
    days_map = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
    target_day = days_map.get(peak, 1)

    days_ahead = (target_day - now.weekday()) % 7
    if days_ahead == 0:
        days_ahead = 7

    optimal = now + timedelta(days=days_ahead)
    optimal = optimal.replace(hour=15, minute=0, second=0, microsecond=0)

    return {
        "datetime_utc": optimal.isoformat(),
        "datetime_est": optimal.strftime("%Y-%m-%d %I:%M %p EST"),
        "day": peak,
        "local_time": local_time,
        "utc_time": utc_time,
        "confidence_level": confidence,
        "rationale": timing_data.get("reason", "Peak audience overlap"),
        "testing_plan": timing_data.get("testing_plan", "Test 3 consecutive uploads at this time"),
        "next_test": timing_data.get("next_test", "Compare with alternative window"),
    }

def _calculate_default_time():
    """Fallback default time."""
    now = datetime.now()
    days_ahead = 0
    for i in range(7):
        check = now + timedelta(days=i)
        if check.weekday() in [1, 2, 3]:
            days_ahead = i
            break

    optimal = now + timedelta(days=days_ahead)
    optimal = optimal.replace(hour=15, minute=0, second=0, microsecond=0)

    return {
        "datetime_utc": optimal.isoformat(),
        "datetime_est": optimal.strftime("%Y-%m-%d %I:%M %p EST"),
        "day": optimal.strftime("%A"),
        "local_time": "2:00-4:00 PM",
        "utc_time": "19:00-21:00",
        "confidence_level": 0.75,
        "rationale": "Tuesday-Thursday 2-4 PM EST captures US East Coast lunch break + UK evening commute",
        "testing_plan": "Test 1PM vs 3PM vs 5PM EST over 3 weeks",
        "next_test": "Upload next 3 videos at this time, then compare",
    }

def _generate_metadata(title, script, niche):
    description = f"""{script.get("hook", {}).get("text", "")}

In this video, we dive deep into one of the most baffling unsolved cases of the last two decades. New evidence in 2026 may finally bring answers.

TIMESTAMPS:
0:00 - The Hook
0:15 - Background
1:30 - The Investigation
7:00 - The Breakthrough
9:00 - The Aftermath
10:30 - How You Can Help

This case remains active. If you have any information, please contact the appropriate authorities.

SUBSCRIBE for more unsolved mysteries every week.
LIKE if this case deserves more attention.
COMMENT with your theory.

#unsolved #truecrime #mystery #coldcase #investigation

AFFILIATE LINKS:
Recommended: "The Cases That Haunt Us" by John Douglas
Try Audible FREE for 30 days

DISCLAIMER: This video is for educational purposes only.
"""

    tags = [
        "true crime", "unsolved mystery", "cold case", "investigation",
        "horror stories", "real crime", "mystery", "unsolved",
        "crime documentary", "real mystery", "creepy", "scary",
        "canada crime", "real estate murder", "unsolved murder",
        "2026 documentary", "new evidence", "police investigation",
    ]

    return {
        "title": title,
        "description": description,
        "tags": tags,
        "category": "Education / Entertainment",
        "language": "en",
        "made_for_kids": False,
    }

def _generate_end_screen():
    return {
        "elements": [
            {"type": "subscribe_button", "position": "bottom_left", "start_time": "10:30"},
            {"type": "video_suggestion", "position": "top_left", "start_time": "10:35", "style": "best_for_viewer"},
            {"type": "video_suggestion", "position": "top_right", "start_time": "10:35", "style": "playlist"},
            {"type": "channel_branding", "position": "center", "start_time": "10:40"},
        ],
        "duration": "20s",
    }

def _generate_cards():
    return [
        {"timestamp": "1:30", "type": "video", "message": "Watch: The Tinley Park 5 Case"},
        {"timestamp": "5:00", "type": "playlist", "message": "More Unsolved Mysteries"},
        {"timestamp": "9:00", "type": "link", "message": "Support Cold Case Investigations", "url": "https://example.com/donate"},
    ]

def _select_playlist(niche):
    playlists = {
        "horror_true_crime": "Unsolved Mysteries & Cold Cases",
        "haunted_history": "History's Darkest Secrets",
        "mystery_crime": "Stories of Betrayal",
    }
    return playlists.get(niche, "Featured Videos")

def _configure_monetization():
    return {
        "ads": {"pre_roll": True, "mid_roll": True, "post_roll": True, "overlay": True},
        "mid_roll_placements": ["3:00", "6:00", "9:00"],
        "sponsorship": {"enabled": True, "slot": "60s integrated at 2:00", "rate": "$800-1200 per 100k subs"},
        "affiliate_links": [
            {"product": "Audible", "commission": "$5-15 per signup"},
            {"product": "True Crime Books", "commission": "4-8%"},
        ],
        "memberships": {"enabled": True, "tiers": ["$4.99", "$9.99", "$24.99"], "perks": ["Early access", "Bonus cases", "Discord community"]},
    }

def _generate_seo(title, niche):
    return {
        "target_keywords": [
            "unsolved mystery 2026",
            "cold case new evidence",
            "true crime documentary",
            "real estate murder",
            "canada unsolved murder",
        ],
        "long_tail_keywords": [
            "why was lindsay buziak murdered",
            "unsolved real estate agent murder canada",
            "new dna technology cold cases 2026",
        ],
        "search_volume_estimate": "15K-45K monthly",
        "difficulty": "medium",
        "competition_level": "medium",
        "recommended_hashtags": ["#truecrime", "#unsolved", "#mystery", "#coldcase", "#2026"],
    }

def _generate_repurpose_plan(strategy, script):
    primary = strategy["primary"]
    secondary = strategy.get("secondary", {})

    return {
        "youtube_shorts": {"enabled": True, "content": secondary.get("title", "60s summary") if secondary else "60s summary", "hook": script.get("hook", {}).get("text", "")[:100], "hashtags": ["#shorts", "#truecrime", "#unsolved"]},
        "tiktok": {"enabled": True, "content": "30s hook + key evidence reveal", "format": "vertical_9_16", "trending_audio": "suspenseful_orchestral"},
        "instagram_reels": {"enabled": True, "content": "45s dramatic retelling", "format": "vertical_9_16", "text_overlays": "Heavy - every 3 seconds"},
        "podcast": {"enabled": True, "content": "Full audio track + extended interview style", "platforms": ["Spotify", "Apple Podcasts", "Google Podcasts"]},
        "blog_post": {"enabled": True, "content": "1500 word article with sources and images", "seo_focus": "Long-tail keywords for organic search"},
    }
