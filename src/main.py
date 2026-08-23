from src.trainee_service import (
    add_trainee,
    search_trainee,
    update_trainee
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


def main():
    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        # -------------------------------
        # 1. Add Trainee
        # -------------------------------
        if choice == "1":
            trainee_id = input("Enter trainee ID: ").strip()
            name = input("Enter trainee name: ").strip()
            specialization = input(
                "Enter specialization (Data Science/Data Engineering): "
            ).strip()
            attendance = input("Enter attendance: ").strip()
            score = input("Enter score: ").strip()
            assignment_status = input(
                "Enter assignment status (Submitted/Pending): "
            ).strip()

            success, message = add_trainee(
                trainee_id,
                name,
                specialization,
                attendance,
                score,
                assignment_status
            )

            print(message)

        # -------------------------------
        # 2. Search Trainee
        # -------------------------------
        elif choice == "2":
            trainee_id = input("Enter trainee ID to search: ").strip()

            trainee = search_trainee(trainee_id)

            if trainee:
                print("\nTrainee Found")
                print("------------------------------")
                print(f"Trainee ID: {trainee[0]}")
                print(f"Name: {trainee[1]}")
                print(f"Specialization: {trainee[2]}")
                print(f"Attendance: {trainee[3]}%")
                print(f"Score: {trainee[4]}")
                print(f"Assignment Status: {trainee[5]}")
            else:
                print("Trainee not found.")

        # -------------------------------
        # 3. Update Trainee
        # -------------------------------
        elif choice == "3":
            trainee_id = input("Enter trainee ID to update: ").strip()
            name = input("Enter trainee name: ").strip()
            specialization = input(
                "Enter specialization (Data Science/Data Engineering): "
            ).strip()
            attendance = input("Enter attendance: ").strip()
            score = input("Enter score: ").strip()
            assignment_status = input(
                "Enter assignment status (Submitted/Pending): "
            ).strip()

            success, message = update_trainee(
                trainee_id,
                name,
                specialization,
                attendance,
                score,
                assignment_status
            )

            print(message)

        # -------------------------------
        # 4. Display All Trainees
        # -------------------------------
        elif choice == "4":
            print("Display All Trainees selected.")

        # -------------------------------
        # 5. Check Eligibility
        # -------------------------------
        elif choice == "5":
            print("Check Eligibility selected.")

        # -------------------------------
        # 6. Reports
        # -------------------------------
        elif choice == "6":
            print("Reports selected.")

        # -------------------------------
        # 7. Exit
        # -------------------------------
        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()