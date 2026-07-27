print("10 + 4 =", 10 + 4)
print("10 - 4 =", 10 - 4)
print("10 * 4 =", 10 * 4)
print("10 ÷ 4 =", 10 / 4)
print("⌊10 ÷ -4⌋ =", 10 // -4) # floor
print("10 mod 4 =", 10 % 4) # mod
print("10⁴", 10 ** 4)

print("10 & 4 =", 10 & 4)
print("10 | 4 =", 10 | 4)
print("10 ^ 4 =", 10 ^ 4)
print("~10 =", ~10 // 3)
print("10 << 4 =", 10 << 4)
print("10 >> 4 =", 10 >> 4)



# priority high to low, same level calc operator processing is left-to-right:
# level1: ()
# level2: **
# level3: *, /, // %
# level4: +, -
# level6: <<, >>
# level7: &
# level8: ^
# level9: |
# level10: ==, !=, >, <, >=, <=, is, is not, in, not in
# level11: not
# level12: and
# level13: or
# level14:
#     +--------------------------------+-----------------+-----------------+------------------------------------------+
#     | Category                       | Normal Form     | Augmented Form  | Equivalent Meaning                       |
#     +--------------------------------+-----------------+-----------------+------------------------------------------+
#     | Basic Assignment               | a = b           | N/A             | Direct assignment                        |
#     | Arithmetic Addition            | a = a + b       | a += b          | Addition                                 |
#     | Arithmetic Subtraction         | a = a - b       | a -= b          | Subtraction                              |
#     | Arithmetic Multiplication      | a = a * b       | a *= b          | Multiplication                           |
#     | Arithmetic Division            | a = a / b       | a /= b          | Division (float)                         |
#     | Arithmetic Floor Div           | a = a // b      | a //= b         | Floor division                           |
#     | Arithmetic Modulo              | a = a % b       | a %= b          | Modulo (remainder)                       |
#     | Arithmetic Exponentiation      | a = a ** b      | a **= b         | Exponentiation                           |
#     | Shift Left                     | a = a << b      | a <<= b         | Left shift                               |
#     | Shift Right                    | a = a >> b      | a >>= b         | Right shift                              |
#     | Bitwise AND                    | a = a & b       | a &= b          | Bitwise AND                              |
#     | Bitwise OR                     | a = a | b       | a |= b          | Bitwise OR                               |
#     | Bitwise XOR                    | a = a ^ b       | a ^= b          | Bitwise XOR                              |
#     | Special (Walrus)               | a = expression  | :=              | Assignment expr. (Python 3.8+)           |
#     +--------------------------------+-----------------+-----------------+------------------------------------------+

print(10 / 2 * 6)