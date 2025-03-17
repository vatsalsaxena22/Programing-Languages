# Datatypes

x = frozenset({"apple", "banana", "cherry"}) # frozenset
x = 1j # complex
x = b"Hello" # bytes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview

# Operators

# Assignment Operators

x &= 3 # x = x & 3
x |= 3 # x = x | 3
x ^= 3 # x = x ^ 3
x >>= 3 # x = x >> 3
x <<= 3 # x = x << 3
print(x := 3) # Walrus operator print 3

# Bitwise Operators

print(10 & 5) # AND
print(10 | 5) # OR
print(10 ^ 5) # XOR
print(~10) # NOT
print(10 << 5) # Zero fill left shift
print(10 >> 5) # Signed right shift

# Functions

# Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
