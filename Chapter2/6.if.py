score = int(input("Enter the a number: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score < 60 and score >= 40:
    print("E")
else:
    pass
    print("F")

electric_value = 0
electric = "-" if 0 == electric_value else "+"
print(electric)

print(electric_value == "0")
print(electric_value == int("0"))

while True:
    text = input("Enter the correct passcode: ")
    if text == "python" or text == "python3": # The vertical pipe operator will be recognized as a calculate operation rather than "or" logic in if statements, you must use the key word "or" to make it.
        print("passcode is correct!")
        break
    else:
        print("passcode is incorrect，please try again.")