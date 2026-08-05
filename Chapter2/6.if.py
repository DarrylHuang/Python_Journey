score = 50
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score < 60 or score >= 40:
    print("D")
elif score < 60 | score >= 40:
    print("D") # also allowed
else:
    pass
    print("F")

electric_value = 0
electric = "-" if 0 == electric_value else "+"
print(electric)

print(electric_value == "0")
print(electric_value == int("0"))
