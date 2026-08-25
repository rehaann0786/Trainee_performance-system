from src.trainee_service import (
    add_trainee,
    search_trainee,
    update_trainee,
    get_all_trainees,
    get_report_data,
    get_specialization_report
)

from src.eligibility import check_eligibility

from src.validators import (
    validate_trainee_id,
    validate_name,
    validate_specialization,
    validate_attendance,
    validate_score,
    validate_assignment_status
)


def display_menu():
    print("\n======================================")
    print("Trainee Performance Management System")
    print("======================================")
    print("1. Add Trainee")
    print("2. Search Trainee")
    print("3. Update Trainee")
    print("4. Display All Trainees")
    print("5. Check Eligibility")
    print("6. Reports")
    print("7. Exit")


def display_trainee(trainee):
    print("\n--------------------------------------")
    print(f"Trainee ID: {trainee[0]}")
    print(f"Name: {trainee[1]}")
    print(f"Specialization: {trainee[2]}")
    print(f"Attendance: {trainee[3]}%")
    print(f"Score: {trainee[4]}")
    print(f"Assignment Status: {trainee[5]}")
    print("--------------------------------------")


def get_valid_input(prompt, validator):
    while True:
        value = input(prompt).strip()

        valid, message = validator(value)

        if valid:
            return value

        print(f"Invalid input: {message}")


def get_trainee_input():
    trainee_id = get_valid_input(
        "Enter trainee ID: ",
        validate_trainee_id
    )

    name = get_valid_input(
        "Enter trainee name: ",
        validate_name
    )

    specialization = get_valid_input(
        "Enter specialization (Data Science/Data Engineering): ",
        validate_specialization
    )

    attendance = get_valid_input(
        "Enter attendance: ",
        validate_attendance
    )

    score = get_valid_input(
        "Enter score: ",
        validate_score
    )

    assignment_status = get_valid_input(
        "Enter assignment status (Submitted/Pending): ",
        validate_assignment_status
    )

    return (
        trainee_id,
        name,
        specialization,
        attendance,
        score,
        assignment_status
    )


def main():
    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        try:
            # 1. Add Trainee
            if choice == "1":
                trainee_data = get_trainee_input()

                success, message = add_trainee(*trainee_data)

                print(message)

            # 2. Search Trainee
            elif choice == "2":
                search_value = input(
                    "Enter trainee ID or name to search: "
                ).strip()

                trainee = search_trainee(search_value)

                if trainee:
                    display_trainee(trainee)
                else:
                    print("Trainee not found.")

            # 3. Update Trainee
            elif choice == "3":
                trainee_id = get_valid_input(
                    "Enter trainee ID to update: ",
                    validate_trainee_id
                )

                name = get_valid_input(
                    "Enter trainee name: ",
                    validate_name
                )

                specialization = get_valid_input(
                    "Enter specialization (Data Science/Data Engineering): ",
                    validate_specialization
                )

                attendance = get_valid_input(
                    "Enter attendance: ",
                    validate_attendance
                )

                score = get_valid_input(
                    "Enter score: ",
                    validate_score
                )

                assignment_status = get_valid_input(
                    "Enter assignment status (Submitted/Pending): ",
                    validate_assignment_status
                )

                success, message = update_trainee(
                    trainee_id,
                    name,
                    specialization,
                    attendance,
                    score,
                    assignment_status
                )

                print(message)

            # 4. Display All Trainees
            elif choice == "4":
                trainees = get_all_trainees()

                if not trainees:
                    print("No trainees found.")
                else:
                    print("\n========== ALL TRAINEES ==========")

                    for trainee in trainees:
                        display_trainee(trainee)

            # 5. Check Eligibility
            elif choice == "5":
                trainee_id = get_valid_input(
                    "Enter trainee ID to check eligibility: ",
                    validate_trainee_id
                )

                trainee = search_trainee(trainee_id)

                if not trainee:
                    print("Trainee not found.")
                    continue

                eligible, reasons = check_eligibility(
                    float(trainee[3]),
                    float(trainee[4]),
                    trainee[5]
                )

                print("\n========== ELIGIBILITY ==========")
                print(f"Trainee: {trainee[1]}")

                if eligible:
                    print("Status: ELIGIBLE")
                else:
                    print("Status: NOT ELIGIBLE")
                    print("Reasons:")

                    for reason in reasons:
                        print(f"- {reason}")

            # 6. Reports
            elif choice == "6":
                report = get_report_data()

                total_trainees = report[0]
                average_attendance = report[1]
                average_score = report[2]
                eligible_trainees = report[3]

                print("\n========== BATCH REPORT ==========")
                print(f"Total Trainees: {total_trainees}")
                print(f"Average Attendance: {average_attendance}%")
                print(f"Average Score: {average_score}")
                print(f"Eligible Trainees: {eligible_trainees}")

                if total_trainees:
                    eligibility_rate = (
                        eligible_trainees / total_trainees
                    ) * 100

                    print(
                        f"Eligibility Rate: "
                        f"{eligibility_rate:.2f}%"
                    )

                print("\n====== SPECIALIZATION REPORT ======")

                specialization_report = get_specialization_report()

                for row in specialization_report:
                    print(f"\nSpecialization: {row[0]}")
                    print(f"Trainees: {row[1]}")
                    print(
                        f"Average Attendance: {row[2]}%"
                    )
                    print(
                        f"Average Score: {row[3]}"
                    )

            # 7. Exit
            elif choice == "7":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as error:
            print(f"An error occurred: {error}")
            print("Please try again.")


if __name__ == "__main__":
    main()