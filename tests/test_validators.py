from src.validators import (
    validate_trainee_id,
    validate_name,
    validate_specialization,
    validate_attendance,
    validate_score,
    validate_assignment_status
)


def test_valid_trainee_id():
    assert validate_trainee_id("T001")[0] is True


def test_empty_trainee_id():
    assert validate_trainee_id("")[0] is False


def test_valid_name():
    assert validate_name("Rahul Khan")[0] is True


def test_empty_name():
    assert validate_name("")[0] is False


def test_valid_specialization():
    assert validate_specialization("Data Engineering")[0] is True


def test_invalid_specialization():
    assert validate_specialization("Web Development")[0] is False


def test_valid_attendance():
    assert validate_attendance(85)[0] is True


def test_invalid_attendance():
    assert validate_attendance(120)[0] is False


def test_valid_score():
    assert validate_score(75)[0] is True


def test_invalid_score():
    assert validate_score(110)[0] is False


def test_valid_assignment_status():
    assert validate_assignment_status("Submitted")[0] is True


def test_invalid_assignment_status():
    assert validate_assignment_status("Not Started")[0] is False