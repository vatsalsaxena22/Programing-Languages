# Python Syntax

print("Hello World!")

# Variables

x = 1
y = "Ram"

print(x)
print(y)

print("----------------")

# Data Types

x = "Hello World" # str
x = 20 # int
x = 20.5 # float
x = range(6) # range
x = True # bool
x = ["apple", "banana", "cherry"] # list
x = ("apple", "banana", "cherry") # tuple
x = {"name" : "John", "age" : 36} # dict
x = {"apple", "banana", "cherry"} # set
x = None # None

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
x = y # is not

# Membership Operators

x = ["apple", "banana"]
y = "apple"

print(y in x) # in
print(y not in x) # not in

print("----------------")

# Collections

# List

# ordered, changeable, allows duplicate values

my_list = ["apple", "banana", "cherry"]
print(my_list) 

# Tuple

# ordered, unchangeable, allows duplicate values

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# Set

# unordered, unindexed, no duplicate values

my_set = {"apple", "banana", "cherry"}
print(my_set)

# Dictionary

# unordered, changeable, indexed, no duplicate values

my_dict = {
    "name" : "John",
    "age" : 36
}
print(my_dict)

# If Else

a = 33
b = 200

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

print("----------------")

#  While Loop

i = 1
while i <= 5:
    print(i)
    i += 1

print("----------------")

# Break Statement

i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1

print("----------------")

# Continue Statement

i = 0
while i <= 5:
    i += 1
    if i == 3:
        continue
    print(i)

print("----------------")

# Else Statement

i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("i is now greater than 5")

print("----------------")

# For Loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

print("----------------")

# Looping Through a String
x = "banana"
for i in x:
    print(i)

print("----------------")

# The range() Function
x = range(6)
for i in x:
    print(i)

print("----------------")

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for i in adj:
    for j in fruits:
        print(i, j)

print("----------------")

# Pass Statement
for x in [0, 1, 2]:
    pass

# Functions

def my_function(): # Function creation
    print("Hello from a function")

my_function() # Function call

# Arguments or args

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")