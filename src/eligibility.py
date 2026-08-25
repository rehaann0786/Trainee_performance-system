def check_eligibility(attendance, score, assignment_status):
    reasons = []

    if attendance < 80:
        reasons.append("Attendance is below 80%.")

    if score < 60:
        reasons.append("Score is below 60.")

    if assignment_status != "Submitted":
        reasons.append("Assignment is not submitted.")

    if reasons:
        return False, reasons

    return True, ["Trainee is eligible."]

def calculate_rating(score):
    score = float(score)

    if score >= 90:
        return "Outstanding"
    elif score >= 80:
        return "Very Good"
    elif score >= 70:
        return "Good"
    elif score >= 60:
        return "Needs Improvement"
    else:
        return "Retraining Required"