s1 = "Hello World"  +  "Hello python" ", OK"
print(s1)

msg1 = "Hello"
msg2 = "World"
print(msg1 + msg2)

# plus operator can only concatenate str (not "int") to str, besides, you can use comma.
name = "Darryl"
age = 29
print(name + " is " +  str(age) + " years old.")
print(name, "is" , age , "years old.")
# wrong example:
# print(name + " is " +  age + " years old.")

# template str will force change non-str variable to str class
print("template1: My name is %s, I am %d years old. " % (name, age))
print("template2: My name is %s, I am %s years old. " % (name, age))

# format str is recommended, variable and expression is supported
print(f"format: My name is {name}, I am {age} years old. ")
print(f"format: My name is {name}, I am {age + 1} years old. ")