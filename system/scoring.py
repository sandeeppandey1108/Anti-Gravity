
def score(idea):
    return idea["ctr"]*0.3 + idea["retention"]*0.3 + idea["rpm"]*0.2 + idea["sponsor"]*0.2
