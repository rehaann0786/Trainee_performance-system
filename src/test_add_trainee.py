from src.trainee_service import add_trainee


success, message = add_trainee(
    "T006",
    "Test User",
    "Data Engineering",
    85,
    70,
    "Submitted"
)

print(success)
print(message)