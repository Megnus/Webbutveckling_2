"""
    Inlämningsuppgift 1
    Magnus Sundström
    2016-09-06
"""

# Uppgift 1
print(5 * 2  <= 12)
print(55 > 22)
print(16 / 4 ==  4)
print(8 + 2  < 128)
print(32 * 8  != 255)


# Uppgift 2
# The name
name = "Sherlock Holmes"
# Number of characters
num_of_chars = len(name)
# Print the number of characters
print(num_of_chars)


# Uppgift 3
part_1 = "The area of a Triangle with a width of "
part_2 = 12
part_3 = " and a height of "
part_4 = 8
part_5 = " is: "
# Calculate the area with the variables part_2
# and part_4 (the area is: height * width / 2)
part_6 = part_2 * part_4 / 2

all_parts = part_1 + str(part_2) + part_3 + str(part_4) + part_5 + str(part_6)
print(all_parts)


# Uppgift 4
# Del 1
tisdag = "Tisdag"
burgare = "Hamburgare"
illBeBack = "I'll be back"
print(tisdag[:3])
print(burgare[3:])
print(illBeBack[5:])

# Del 2
itsLearning = "It's Learning"
theGoodParts = "Python: The Good Parts"
print(itsLearning[5:].upper())
print(theGoodParts[12:].lower())


# Uppgift 5
def calculate_triangle_area(width, height):
    return width * height / 2


# Uppgift 6
def max(a, b):
    return a if a > b else b

def min(a, b):
    return a if a < b else b


# Uppgift 7
def isEven(val):
    return val % 2 == 0

