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