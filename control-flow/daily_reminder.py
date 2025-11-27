# Daily Reminder Program

print("---- Personal Daily Reminder ----")

while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Task cannot be empty. Please try again.\n")

while True:
    priority = input("Priority (high/medium/low): ").lower().strip()
    if priority in ["high", "medium", "low"]:
        break
    print("Invalid priority. Enter high, medium, or low.\n")

while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    if time_bound in ["yes", "no"]:
        break
    print("Please answer yes or no.\n")


match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' is a task"


if time_bound == "yes":
    final_message = base_message + " that requires immediate attention today!"
else:
    final_message = (
        "Note: " + base_message + ". Consider completing it when you have free time."
    )


print("\nReminder:", final_message)
