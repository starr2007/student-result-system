def get_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    else:
        return "F"


def validate_score(value):
    score = float(value)
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    return score