"""
    Inlämningsuppgift 3
    Magnus Sundström
    2016-09-06
"""

# Del 1: Input
persons = []
while True:
    choice = input("Choose: (1) Add person, (2) List all\n")
    if choice == "1":
        persons.append({'firstname': input("Type firstname: "),
                        'lastname': input("Type lastname: ") })
    elif choice == "2":
        for names in persons:
            print(names['firstname'] + " " + names['lastname'])
    else:
        print("Bye!")
        break


# Del 2: Filhantering
def add_player(firstname, lastname, country):
    file = open('players.txt', 'a')
    file.write(", ".join([firstname, lastname, country]) + "\n")
    file.close()

def print_players():
    try:
        file = open('players.txt', 'r')
        for line in file:
            print(line, end = "")
        file.close()
    except:
        print("No players")
    
def start():
    while True:
        choice = input("Choose: (1) Add player, (2) List all players\n")
        if choice == "1":
            add_player(input("Type firstname: "),
                       input("Type lastname: "),
                       input("Type country: ")) 
        elif choice == "2":
            print_players();
        else:
            break
start()


# Del 3: JSON
import json
def read_players():
    players = ["players"]
    try:
        file = open('players.json', 'r')
        players = json.loads(file.read())
        file.close()
    except:
        print("Could not read file or file is empty")
    return players

def write_players(players):
    try:
        file = open('players.json', 'w')
        file.write(json.dumps(players))
        file.close()
    except:
        print("Could not read file")

def add_player(firstname, lastname, country):
    players = read_players()
    players.append({'firstname': firstname,
                    'lastname': lastname,
                    'country': country})
    write_players(players)

def print_players():
    players = read_players()
    for i in range(1, len(players)):
        print(", ".join([players[i]["firstname"],
                         players[i]["lastname"],
                         players[i]["country"]]))
    
def start():
    while True:
        choice = input("Choose: (1) Add person, (2) List all\n")
        if choice == "1":
            add_player(input("Type firstname: "),
                       input("Type lastname: "),
                       input("Type country: ")) 
        elif choice == "2":
            print_players();
        else:
            break
start()
