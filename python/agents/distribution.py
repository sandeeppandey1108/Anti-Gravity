
"""
Distribution Agent v2
Manages multi-platform distribution and scheduling.
"""
from datetime import datetime, timedelta

def distribute(upload_package, video_plan, strategy):
    """Generate distribution plan for all platforms."""

    primary = strategy["primary"]
    repurpose = upload_package.get("repurpose_plan", {})

    schedule = upload_package["schedule"]
    base_time = datetime.fromisoformat(schedule["datetime_utc"])

    distribution_plan = {
        "primary_platform": "youtube",
        "primary_upload": {
            "time": schedule["datetime_est"],
            "content": upload_package["metadata"]["title"],
            "format": "16:9_1080p",
        },
        "platforms": [],
        "cross_promotion": [],
        "email_sequence": [],
    }

    if repurpose.get("youtube_shorts", {}).get("enabled"):
        shorts_time = base_time + timedelta(hours=2)
        distribution_plan["platforms"].append({
            "platform": "youtube_shorts",
            "time": shorts_time.strftime("%Y-%m-%d %I:%M %p EST"),
            "content": repurpose["youtube_shorts"]["content"],
            "format": "9:16_vertical",
            "hook": repurpose["youtube_shorts"]["hook"],
            "hashtags": repurpose["youtube_shorts"]["hashtags"],
            "strategy": "Drive traffic to main video via end card",
        })

    if repurpose.get("tiktok", {}).get("enabled"):
        tiktok_time = base_time + timedelta(hours=4)
        distribution_plan["platforms"].append({
            "platform": "tiktok",
            "time": tiktok_time.strftime("%Y-%m-%d %I:%M %p EST"),
            "content": repurpose["tiktok"]["content"],
            "format": repurpose["tiktok"]["format"],
            "audio": repurpose["tiktok"]["trending_audio"],
            "strategy": "Viral hook in first 1s, link in bio to YouTube",
        })

    if repurpose.get("instagram_reels", {}).get("enabled"):
        reels_time = base_time + timedelta(days=1)
        distribution_plan["platforms"].append({
            "platform": "instagram_reels",
            "time": reels_time.strftime("%Y-%m-%d %I:%M %p EST"),
            "content": repurpose["instagram_reels"]["content"],
            "format": repurpose["instagram_reels"]["format"],
            "text_overlays": repurpose["instagram_reels"]["text_overlays"],
            "strategy": "Heavy text overlays for sound-off viewing",
        })

    if repurpose.get("podcast", {}).get("enabled"):
        podcast_time = base_time + timedelta(days=2)
        distribution_plan["platforms"].append({
            "platform": "podcast",
            "time": podcast_time.strftime("%Y-%m-%d %I:%M %p EST"),
            "content": repurpose["podcast"]["content"],
            "platforms": repurpose["podcast"]["platforms"],
            "strategy": "Extended version with bonus analysis",
        })

    if repurpose.get("blog_post", {}).get("enabled"):
        blog_time = base_time + timedelta(days=3)
        distribution_plan["platforms"].append({
            "platform": "blog",
            "time": blog_time.strftime("%Y-%m-%d %I:%M %p EST"),
            "content": repurpose["blog_post"]["content"],
            "seo_focus": repurpose["blog_post"]["seo_focus"],
            "strategy": "Long-form SEO content to capture organic search",
        })

    distribution_plan["cross_promotion"] = [
        {"day": 0, "action": "Post teaser on Twitter/X with thread"},
        {"day": 0, "action": "Share in relevant Reddit communities (r/UnresolvedMysteries)"},
        {"day": 1, "action": "Facebook post with native video clip"},
        {"day": 2, "action": "LinkedIn post about investigative journalism angle"},
        {"day": 3, "action": "Pinterest pin with thumbnail image"},
        {"day": 7, "action": "Community post: 'What theory do you believe?'"},
    ]

    distribution_plan["email_sequence"] = [
        {"day": 0, "subject": f"New Case: {primary['title']}", "content": "Full video + behind-the-scenes notes"},
        {"day": 3, "subject": "The theory everyone is talking about", "content": "Community discussion highlights"},
        {"day": 7, "subject": "Did you miss this detail?", "content": "Easter eggs and hidden clues breakdown"},
    ]

    return distribution_plan
