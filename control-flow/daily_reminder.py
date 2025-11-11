task = input("Enter task description: ")
priority = input("(high, medium, low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
reminder = ""
match priority:
    case "high":
        reminder = f"{task} is a high priority task."
    case "medium":
        reminder = f"{task} is a low priority task."
    case "low":
        reminder = f"{task} is low priority task"
    case _:
        reminder = f"{task} is unknown"

time = ""
if time_bound == "yes":
    time = "that requires immediate attention today!"
else:
    time = "Consider completing it when you have free time."

print(f"{reminder}. {time}")