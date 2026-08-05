day = input("Please enter a week day: ")
match day:
    case "1":
        print("Monday")
    case "2":
        print("Tuesday")
    case "3":
        print("Wednesday")
    case "4":
        print("Thursday")
    case "5":
        print("Friday")
    case "6" | "7":
        print("weekend! 6 is Saturday, 7 is Sunday")
    case _:
        print("Invalid input")