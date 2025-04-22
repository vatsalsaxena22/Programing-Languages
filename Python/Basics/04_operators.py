# Operators

# Arithmetic Operators

print(10 + 5) # Addition
print(10 - 5) # Subtraction
print(10 * 5) # Multiplication
print(10 / 5) # Division
print(10 % 5) # Modulus
print(10 ** 5) # Exponentiation
print(10 // 5) # Floor division

# Assignment Operators

x = 5 # x = 5
x += 3 # x = x + 3
x -= 3 # x = x - 3
x *= 3 # x = x * 3
x /= 3 # x = x / 3
x %= 3 # x = x % 3
x //= 3 # x = x // 3
x **= 3 # x = x ** 3

# Comparison Operators

print(10 == 5) # Equal
print(10 != 5) # Not equal
print(10 > 5) # Greater than
print(10 < 5) # Less than
print(10 >= 5) # Greater than or equal to
print(10 <= 5) # Less than or equal to

# Logical Operators

print(10 > 5 and 10 < 5) # and
print(10 > 5 or 10 < 5) # or
print(not(10 > 5 and 10 < 5)) # not

# Identity Operators

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

x = z # is
x = y # is not because of different memory locations

# Membership Operators

x = ["apple", "banana"]
y = "apple"

print(y in x) # in
print(y not in x) # not in