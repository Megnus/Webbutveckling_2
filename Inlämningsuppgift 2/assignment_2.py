# Uppgift 1
def printNumbers(val):
    for i in range(1, val + 1):
        print(i)


# Uppgift 2
def fooBar(val):
    for i in range(1, val + 1):
        if i % 15 == 0:
            print("FooBar")
        elif i % 3 == 0:
            print("Foo")
        elif i % 5 == 0:
            print("Bar")
        else:
            print(i)


# Uppgift 3
def calculate_average(numbers):
    sum = 0
    count = 0
    for i in numbers:
        sum += i
        count += 1
    return sum / count
    #return sum(numbers) / len(numbers)


# Uppgift 4
def filter_names_by_length(names, size):
    for i in range(len(names) - 1, 0, -1):
        if len(names[i]) <= size:
            del names[i]
    return names


# Uppgift 5
myself = {}
myself["firstname"] = "Sherlock"
myself["lastname"] = "Holmes"
myself["age"] = 35
myself["top_3_movies"] = ["Seven", "Gone Girl", "The Prestige"]


# Uppgift 6
def printPerson(personDic):
    print(personDic["firstname"] + " "
          + personDic["lastname"] + " "
          + str(personDic["age"]) + ", Top Movies: "
          + ', '.join(personDic["top_3_movies"]))


# Uppgift 7
def createPerson(firstname, lastname, age, top_3_movies):
    return {
        "firstname": firstname,
        "lastname": lastname,
        "age": age,
        "top_3_movies": top_3_movies
    }
