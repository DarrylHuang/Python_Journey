balance = 10000.0

print("Welcome to the withdrawal program.")
print("Current balance: $%.2f" % balance)
print("Tip: type exit to quit.")

while True:
    user_input = input("\nEnter withdrawal amount: ").strip()

    if user_input.lower() == "exit":
        print("Program exited. Final balance: $%.2f" % balance)
        break

    try:
        amount = float(user_input)
    except ValueError:
        print("Invalid input. Enter a number, or type exit to quit.")
        continue

    if amount <= 0:
        print("Withdrawal amount cannot be less than or equal 0. Please try again.")
        continue

    if amount > balance:
        print("Withdrawal amount is greater than the current balance: $%.2f" % balance)
        print("Please enter a new amount, or type exit to quit.")
        continue

    balance -= amount
    print("Withdrawal successful. Amount: $%.2f. Remaining balance: $%.2f" % (amount, balance))

    if balance == 0:
        print("Balance is now 0. Type exit if you want to quit.")
        continue

    answer = input("Do you want to continue? Type Y to continue, or exit to quit: ").strip().lower()

    if answer == "exit":
        print("Program exited. Final balance: $%.2f" % balance)
        break

    if answer != "Y":
        print("Input is not Y. Program ended. Final balance: $%.2f" % balance)
        break
