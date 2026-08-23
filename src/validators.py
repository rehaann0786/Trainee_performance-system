def validate_trainee_id(trainee_id):
    if not trainee_id or not trainee_id.strip():
        return False, "Trainee ID is required."

    return True, ""


def validate_name(name):
    if not name or not name.strip():
        return False, "Name is required."

    return True, ""

def validate_specialization(specialization):
    allowed = ["Data Science", "Data Engineering"]

    if specialization not in allowed:
        return False, "Specialization must be Data Science or Data Engineering."

    return True, ""


def validate_attendance(attendance):
    try:
        attendance = float(attendance)
    except (ValueError, TypeError):
        return False, "Attendance must be a number."

    if attendance < 0 or attendance > 100:
        return False, "Attendance must be between 0 and 100."

    return True, ""


def validate_score(score):
    try:
        score = float(score)
    except (ValueError, TypeError):
        return False, "Score must be a number."

    if score < 0 or score > 100:
        return False, "Score must be between 0 and 100."


    return True, ""


def validate_assignment_status(status):
    allowed = ["Submitted", "Pending"]

    if status not in allowed:
        return False, "Assignment status must be Submitted or Pending."

    return True, ""