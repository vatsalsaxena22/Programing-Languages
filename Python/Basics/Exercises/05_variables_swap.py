# Task: Swap the values of two variables without using a third variable
x = 5
y = 10

# After swapping, x should be 10 and y should be 5
x = x + y
y = x - y
x = x - y

print(x)
print(y)

# Pythonic way for swapping
x, y = y, x

print(x)
print(y)