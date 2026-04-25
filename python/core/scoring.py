def score_idea(idea):
    return (
        idea.get("ctr", 0) * 0.3 +
        idea.get("retention", 0) * 0.3 +
        idea.get("rpm", 0) * 0.2 +
        idea.get("sponsor", 0) * 0.2
    )

def rank_ideas(ideas):
    return sorted(ideas, key=score_idea, reverse=True)
