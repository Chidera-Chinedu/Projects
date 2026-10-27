scores = [45, 12, 78, 33, 9, 61, 27]
for score in scores:
    if score >= 50:
        print(score, "Excellent")
    elif score >= 20 and score < 50:
        print(score, "Good")
    elif score < 20:
        print(score, "Needs Improvement")
