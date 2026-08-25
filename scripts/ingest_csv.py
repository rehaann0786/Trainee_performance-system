import csv
import os

from src.database import get_connection
from src.validators import (
    validate_trainee_id,
    validate_name,
    validate_specialization,
    validate_attendance,
    validate_score,
    validate_assignment_status,
)


CSV_FILE = "data/trainees.csv"
REJECTED_FILE = "rejected/rejected_records.csv"


def validate_record(record, existing_ids):
    errors = []

    trainee_id = record.get("trainee_id", "").strip()
    name = record.get("name", "").strip()
    specialization = record.get("specialization", "").strip()
    attendance = record.get("attendance", "").strip()
    score = record.get("score", "").strip()
    assignment_status = record.get("assignment_status", "").strip()

    valid, message = validate_trainee_id(trainee_id)
    if not valid:
        errors.append(message)

    if trainee_id in existing_ids:
        errors.append("Duplicate trainee ID.")

    valid, message = validate_name(name)
    if not valid:
        errors.append(message)

    valid, message = validate_specialization(specialization)
    if not valid:
        errors.append(message)

    valid, message = validate_attendance(attendance)
    if not valid:
        errors.append(message)

    valid, message = validate_score(score)
    if not valid:
        errors.append(message)

    valid, message = validate_assignment_status(assignment_status)
    if not valid:
        errors.append(message)

    return errors


def ingest_csv():
    if not os.path.exists(CSV_FILE):
        raise FileNotFoundError(
            f"CSV file not found: {CSV_FILE}"
        )

    os.makedirs("rejected", exist_ok=True)

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT trainee_id FROM trainees;"
        )

        existing_ids = {
            row[0]
            for row in cursor.fetchall()
        }

        valid_records = []
        rejected_records = []

        with open(
            CSV_FILE,
            mode="r",
            newline="",
            encoding="utf-8",
        ) as file:

            reader = csv.DictReader(file)

            required_columns = {
                "trainee_id",
                "name",
                "specialization",
                "attendance",
                "score",
                "assignment_status",
            }

            if not reader.fieldnames:
                raise ValueError(
                    "CSV file has no header."
                )

            missing_columns = (
                required_columns
                - set(reader.fieldnames)
            )

            if missing_columns:
                raise ValueError(
                    "Missing CSV columns: "
                    + ", ".join(
                        sorted(missing_columns)
                    )
                )

            for record in reader:
                errors = validate_record(
                    record,
                    existing_ids,
                )

                if errors:
                    rejected_record = dict(record)
                    rejected_record["reason"] = "; ".join(
                        errors
                    )

                    rejected_records.append(
                        rejected_record
                    )

                    continue

                valid_records.append(record)

                existing_ids.add(
                    record["trainee_id"].strip()
                )

        insert_query = """
            INSERT INTO trainees (
                trainee_id,
                name,
                specialization,
                attendance,
                score,
                assignment_status
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        for record in valid_records:
            cursor.execute(
                insert_query,
                (
                    record["trainee_id"].strip(),
                    record["name"].strip(),
                    record["specialization"].strip(),
                    float(record["attendance"]),
                    float(record["score"]),
                    record["assignment_status"].strip(),
                ),
            )

        connection.commit()

        if rejected_records:
            with open(
                REJECTED_FILE,
                mode="w",
                newline="",
                encoding="utf-8",
            ) as file:

                fieldnames = [
                    "trainee_id",
                    "name",
                    "specialization",
                    "attendance",
                    "score",
                    "assignment_status",
                    "reason",
                ]

                writer = csv.DictWriter(
                    file,
                    fieldnames=fieldnames,
                )

                writer.writeheader()
                writer.writerows(
                    rejected_records
                )

        print("CSV ingestion completed.")
        print(
            f"Valid records inserted: "
            f"{len(valid_records)}"
        )
        print(
            f"Rejected records: "
            f"{len(rejected_records)}"
        )

        if rejected_records:
            print(
                "Rejected records written to: "
                f"{REJECTED_FILE}"
            )

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    ingest_csv()