from scripts.ingest_csv import validate_record


def test_valid_record():
    record = {
        "trainee_id": "T100",
        "name": "Test Trainee",
        "specialization": "Data Engineering",
        "attendance": "85",
        "score": "75",
        "assignment_status": "Submitted",
    }

    errors = validate_record(record, set())

    assert errors == []


def test_duplicate_trainee_id():
    record = {
        "trainee_id": "T100",
        "name": "Test Trainee",
        "specialization": "Data Engineering",
        "attendance": "85",
        "score": "75",
        "assignment_status": "Submitted",
    }

    errors = validate_record(record, {"T100"})

    assert "Duplicate trainee ID." in errors


def test_invalid_attendance():
    record = {
        "trainee_id": "T101",
        "name": "Test Trainee",
        "specialization": "Data Engineering",
        "attendance": "150",
        "score": "75",
        "assignment_status": "Submitted",
    }

    errors = validate_record(record, set())

    assert "Attendance must be between 0 and 100." in errors


def test_invalid_score():
    record = {
        "trainee_id": "T102",
        "name": "Test Trainee",
        "specialization": "Data Engineering",
        "attendance": "85",
        "score": "150",
        "assignment_status": "Submitted",
    }

    errors = validate_record(record, set())

    assert "Score must be between 0 and 100." in errors


def test_invalid_specialization():
    record = {
        "trainee_id": "T103",
        "name": "Test Trainee",
        "specialization": "Python Development",
        "attendance": "85",
        "score": "75",
        "assignment_status": "Submitted",
    }

    errors = validate_record(record, set())

    assert (
        "Specialization must be "
        "'Data Science' or 'Data Engineering'."
    ) in errors


def test_invalid_assignment_status():
    record = {
        "trainee_id": "T104",
        "name": "Test Trainee",
        "specialization": "Data Engineering",
        "attendance": "85",
        "score": "75",
        "assignment_status": "Unknown",
    }

    errors = validate_record(record, set())

    assert (
        "Assignment status must be "
        "'Submitted' or 'Pending'."
    ) in errors