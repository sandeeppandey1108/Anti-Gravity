
"""
Strategy Agent
Generates 10 ideas, ranks by CTR, retention, monetization, ease of production.
"""

def generate_ideas(topic, niche="horror_true_crime", transformation=None):
    """Generate 10 content ideas from research data."""
    base = topic["topic"]
    angle = topic["angle"]

    ideas = [
        {
            "title": f"The {base}: What Police Refuse To Admit",
            "format": "long_form",
            "hook_type": "authority_contradiction",
            "ctr_potential": 9.2,
            "retention_potential": 8.8,
            "rpm_potential": topic["rpm_potential"],
            "ease_of_production": 7,
            "virality_score": 8.5,
            "series_potential": "HIGH",
        },
        {
            "title": f"5 Things Nobody Told You About {base}",
            "format": "long_form",
            "hook_type": "information_gap",
            "ctr_potential": 8.7,
            "retention_potential": 8.2,
            "rpm_potential": topic["rpm_potential"] * 0.9,
            "ease_of_production": 8,
            "virality_score": 7.8,
            "series_potential": "MEDIUM",
        },
        {
            "title": f"The Last 24 Hours of {base.split(':')[0] if ':' in base else base}",
            "format": "long_form",
            "hook_type": "countdown",
            "ctr_potential": 9.5,
            "retention_potential": 9.1,
            "rpm_potential": topic["rpm_potential"],
            "ease_of_production": 6,
            "virality_score": 9.0,
            "series_potential": "HIGH",
        },
        {
            "title": f"Why {base} Will Never Be Solved",
            "format": "long_form",
            "hook_type": "impossible_scenario",
            "ctr_potential": 9.0,
            "retention_potential": 8.9,
            "rpm_potential": topic["rpm_potential"],
            "ease_of_production": 7,
            "virality_score": 8.7,
            "series_potential": "MEDIUM",
        },
        {
            "title": f"I Spent 100 Hours Researching {base}. Here's The Truth.",
            "format": "long_form",
            "hook_type": "authority_investment",
            "ctr_potential": 8.3,
            "retention_potential": 8.5,
            "rpm_potential": topic["rpm_potential"] * 0.95,
            "ease_of_production": 9,
            "virality_score": 7.5,
            "series_potential": "LOW",
        },
        {
            "title": f"The {base} - But From The Killer's Perspective",
            "format": "long_form",
            "hook_type": "perspective_shift",
            "ctr_potential": 9.3,
            "retention_potential": 9.0,
            "rpm_potential": topic["rpm_potential"] * 1.1,
            "ease_of_production": 5,
            "virality_score": 9.2,
            "series_potential": "HIGH",
        },
        {
            "title": f"{base}: The Evidence They Buried",
            "format": "long_form",
            "hook_type": "conspiracy_reveal",
            "ctr_potential": 9.1,
            "retention_potential": 8.7,
            "rpm_potential": topic["rpm_potential"],
            "ease_of_production": 6,
            "virality_score": 8.8,
            "series_potential": "HIGH",
        },
        {
            "title": f"This {base.split()[0] if base.split() else 'Case'} Changed Everything",
            "format": "short_form",
            "hook_type": "transformation",
            "ctr_potential": 8.8,
            "retention_potential": 7.5,
            "rpm_potential": topic["rpm_potential"] * 0.6,
            "ease_of_production": 9,
            "virality_score": 9.5,
            "series_potential": "MEDIUM",
        },
        {
            "title": f"The {base} In 60 Seconds",
            "format": "short_form",
            "hook_type": "efficiency",
            "ctr_potential": 8.5,
            "retention_potential": 7.0,
            "rpm_potential": topic["rpm_potential"] * 0.5,
            "ease_of_production": 10,
            "virality_score": 9.8,
            "series_potential": "LOW",
        },
        {
            "title": f"3 Theories About {base} That Will Break Your Brain",
            "format": "long_form",
            "hook_type": "cognitive_challenge",
            "ctr_potential": 9.4,
            "retention_potential": 8.6,
            "rpm_potential": topic["rpm_potential"],
            "ease_of_production": 7,
            "virality_score": 9.1,
            "series_potential": "HIGH",
        },
    ]

    return ideas

def rank_ideas(ideas):
    """Rank ideas by composite score including ease of production."""
    for idea in ideas:
        idea["composite_score"] = round(
            idea["ctr_potential"] * 0.30 +
            idea["retention_potential"] * 0.30 +
            (idea["rpm_potential"] / 15) * 10 * 0.20 +
            idea["virality_score"] * 0.10 +
            (idea["ease_of_production"] / 10) * 5 * 0.10,
            2
        )

    ranked = sorted(ideas, key=lambda x: x["composite_score"], reverse=True)
    return ranked

def select_winning_idea(ranked_ideas, research_data=None):
    """Select winner with monetization and timing check."""
    winner = ranked_ideas[0]
    runner_up = ranked_ideas[1] if len(ranked_ideas) > 1 else None

    # Apply transformation if available
    if research_data and research_data.get("transformation"):
        winner["title"] = research_data["transformation"]["original_content"]

    return {
        "primary": winner,
        "secondary": runner_up,
        "strategy": "Lead with primary long-form, repurpose secondary as Short",
        "expected_rpm": winner["rpm_potential"],
        "expected_revenue_per_100k": round(winner["rpm_potential"] * 100, 2),
        "production_difficulty": "HIGH" if winner["ease_of_production"] < 6 else "MEDIUM" if winner["ease_of_production"] < 8 else "LOW",
        "series_potential": winner["series_potential"],
    }
