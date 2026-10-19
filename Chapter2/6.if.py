# score = 40
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# elif score < 60:
#     print("E")
# else:
#     pass
#     print("F")
#
# electric_value = 0
# electric = "-" if 0 == electric_value else "+"
# print(electric)
#
# print(electric_value == "0")
# print(electric_value == int("0"))

while True:
    text = input("Enter the correct passcode: ")
    if text == "python" or text == "python3": # the vertical pipe can not able to represent "or" logic in if statements
        print("passcode is correct")
        break
    else:
        print("passcode is incorrect，please try again")