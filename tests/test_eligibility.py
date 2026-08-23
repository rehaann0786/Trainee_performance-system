from src.eligibility import check_eligibility


def test_eligible_trainee():
    eligible, reasons = check_eligibility(85, 75, "Submitted")

    assert eligible is True
    assert reasons == ["Trainee is eligible."]


def test_low_attendance():
    eligible, reasons = check_eligibility(79, 75, "Submitted")

    assert eligible is False
    assert "Attendance is below 80%." in reasons


def test_low_score():
    eligible, reasons = check_eligibility(85, 59, "Submitted")

    assert eligible is False
    assert "Score is below 60." in reasons


def test_assignment_not_submitted():
    eligible, reasons = check_eligibility(85, 75, "Pending")

    assert eligible is False
    assert "Assignment is not submitted." in reasons


def test_boundary_values():
    eligible, reasons = check_eligibility(80, 60, "Submitted")

    assert eligible is True
    assert reasons == ["Trainee is eligible."]