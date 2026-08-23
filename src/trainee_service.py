from src.database import get_connection


def add_trainee(
    trainee_id,
    name,
    specialization,
    attendance,
    score,
    assignment_status
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO trainees
            (trainee_id, name, specialization, attendance, score, assignment_status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                trainee_id,
                name,
                specialization,
                attendance,
                score,
                assignment_status
            )
        )

        connection.commit()

        return True, "Trainee added successfully."

    except Exception as error:
        connection.rollback()
        return False, str(error)

    finally:
        cursor.close()
        connection.close()

def search_trainee(trainee_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                trainee_id,
                name,
                specialization,
                attendance,
                score,
                assignment_status
            FROM trainees
            WHERE trainee_id = %s
        """

        cursor.execute(query, (trainee_id,))

        trainee = cursor.fetchone()

        return trainee

    finally:
        cursor.close()
        connection.close()        

def update_trainee(
    trainee_id,
    name,
    specialization,
    attendance,
    score,
    assignment_status
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            UPDATE trainees
            SET
                name = %s,
                specialization = %s,
                attendance = %s,
                score = %s,
                assignment_status = %s
            WHERE trainee_id = %s
        """

        cursor.execute(
            query,
            (
                name,
                specialization,
                attendance,
                score,
                assignment_status,
                trainee_id
            )
        )

        if cursor.rowcount == 0:
            connection.rollback()
            return False, "Trainee not found."

        connection.commit()

        return True, "Trainee updated successfully."

    except Exception as error:
        connection.rollback()
        return False, str(error)

    finally:
        cursor.close()
        connection.close()

def get_all_trainees():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                trainee_id,
                name,
                specialization,
                attendance,
                score,
                assignment_status
            FROM trainees
            ORDER BY trainee_id
        """

        cursor.execute(query)

        return cursor.fetchall()

    finally:
        cursor.close()
        connection.close()                