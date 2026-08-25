# Trainee Performance Management System

## Project Objective

The Trainee Performance Management System manages trainee records,
performance data, eligibility, and reporting using Python and PostgreSQL.

## Core Features

- Add trainee
- Search trainee by ID or name
- Update trainee
- Display all trainees
- Calculate performance rating
- Check trainee eligibility
- Display eligibility reasons
- Generate batch reports
- Generate specialization-wise reports
- Validate user input
- Log application activity and errors

## Data Engineering Features

- CSV trainee data ingestion
- CSV schema validation
- Record-level validation
- Duplicate trainee ID detection
- Missing trainee ID detection
- Invalid attendance detection
- Invalid score detection
- Invalid specialization detection
- Invalid assignment status detection
- Load valid records into PostgreSQL
- Store rejected records with rejection reasons

## Technology Stack

- Python
- PostgreSQL
- psycopg2
- pytest
- CSV
- Git/GitHub

## Testing

The project uses pytest for automated testing.

Current test suite:

- 23 tests
- All tests passing