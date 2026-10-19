text = input("please enter text: ")
print("=== print begin ===")
pass
for char in text:
    print(f"char is {char}")
else:
    print("=== print end ===")


n = 0
for i in range(1, 101):
    if i % 2 != 0:
        n += i
print(n)

columns = int(input("please enter column: "))
rows = int(input("please enter row: "))

for i in range(rows):
    for j in range(columns):
        print("*", end=" ")
    print()

for e in range(1, 10):
    for i in range(1, e + 1):
        print(f"{i} × {e} = {i * e}", end="\t")
    print()