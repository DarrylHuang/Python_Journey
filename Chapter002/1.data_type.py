# int
print(100)
print(-100)

# float
print(3.14)

# str
print("Hello Python")

# bool
print(True)
print(False)

# NoneType
print(None)

print(type("Hello Python"))
print(isinstance("Hello Python", bool))

# the bool value is not only bool type but int type
print(isinstance(True, int))
print(isinstance(False, bool))

# str definition ways
single_quotation = 'Hello\n'
# recommended
double_quotation = "Python"
multiple_rows = """
    Hello
    Python
    !
"""
print(single_quotation)
print(double_quotation)
print("Hello\nWorld")

print(single_quotation, double_quotation, multiple_rows)
print("Hello\tPython")
