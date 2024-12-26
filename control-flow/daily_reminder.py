task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time bound?: ")
match priority:
    case "high":
        if time_bound:
            print(variable + " is a " + priority + "  task that requires immediate attention today!" )
        else:
            print(variable + " is a " + priority +  " priority task.Consider completing it when you have free time")
    case "medium":
        if time_bound:
            print(variable + " is a " + priority + " priority task that requires immediate attention today")
        else:
            print(variable + " is a " + priority +  " priority task.Consider completing it when you have free time.")
    case "low":
        if time_bound:
            print(variable + " is a " + priority +" priority task that.requires immediate attention today")
                  
        else:
            print(variable + " is a " + priority +  " priority task.Consider completing it when you have free time.")
    case _:
        print("Invalid data entered")




