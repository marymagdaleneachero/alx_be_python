task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound =="yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that needs to be completed today.")
        else:
            print(f"Reminder: {task} is a medium priority task. Try to fit it into your day.")
    case "low":
        if time_bound =="yes":
            print(f"Reminder: {task} is a low priority task but it's time sensitve. Don't delay")
        else:
            print(f"Note: {priority} is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"{priority} isn't a recognized priority level. Please enter high, medium or low")
        