# Data Dictionary

## Trainee Table

| Column | Type | Description |
|---|---|---|
| trainee_id | VARCHAR | Unique identifier for the trainee |
| name | VARCHAR | Trainee's full name |
| specialization | VARCHAR | Data Science or Data Engineering |
| attendance | NUMERIC | Attendance percentage from 0 to 100 |
| score | NUMERIC | Performance score from 0 to 100 |
| assignment_status | VARCHAR | Submitted or Pending |

## CSV Input Columns

| Column | Required | Validation |
|---|---|---|
| trainee_id | Yes | Must be present and unique |
| name | Yes | Must not be empty |
| specialization | Yes | Data Science or Data Engineering |
| attendance | Yes | Number between 0 and 100 |
| score | Yes | Number between 0 and 100 |
| assignment_status | Yes | Submitted or Pending |

## Rejected Records

Invalid CSV records are written to:

`rejected/rejected_records.csv`

Each rejected record contains a `reason` field describing the validation failure.