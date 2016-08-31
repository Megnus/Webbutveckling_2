# Uppgift 6
# Max
# print(max(12, 17)) # => 17
# print(max(15, 15)) # => 15
# print(max(20, 3)) # => 20

# Min
# print(min(12, 17)) # => 12
# print(min(15, 15)) # => 15
# print(min(20, 3)) # => 3

def max(a, b):
    return a if a > b else b

def min(a, b):
    return a if a < b else b
