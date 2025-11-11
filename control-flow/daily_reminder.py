Task = input("Enter task description: ")
Priority = input("(high, medium, low): ").lower()
Time_Bound = input("Is it time-bound? (yes/no): ").lower()
reminder = ""
match Priority:
    case "high":
        reminder = f"{Task} is a high priority task."
    case "medium":
        reminder = f"{Task} is a low priority task."
    case "low":
        reminder = f"{Task} is low priority task"
    case _:
        reminder = f"{Task} is unknown"

time = ""
if Time_Bound == "yes":
    time = "that requires immediate attention today!"
else:
    time = "Consider completing it when you have free time."

print(f"{reminder}. {time}")