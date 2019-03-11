import json

try:
    with open("stats.json", "r") as read_file:
        stats = json.load(read_file)
except FileNotFoundError:
    with open("legends.json", "r") as read_file:
        stats = json.load(read_file)
    for legend in stats:
        legend["kills"] = 0
        legend["damage"] = 0
        legend["matches_played"] = 0
        legend["matches_won"] = 0
        legend["matches_top_three"] = 0
    with open("stats.json", "w") as outfile:
        json.dump(stats, outfile, indent=4)

print("Stat Tracker for Apex Legends\n")

def update_stats():
    name = input("Name of legend: ")
    for legend in stats:
        if legend["name"].lower() == str(name).lower():
            matches_won = int(input("Matches won: "))
            legend["matches_won"] = matches_won

            kills = int(input("Kills: "))
            legend["kills"] = kills

            damage = int(input("Damage: "))
            legend["damage"] = damage

            matches_played = int(input("Matches played: "))
            legend["matches_played"] = matches_played

            matches_top_three = int(input("Matches top three: "))
            legend["matches_top_three"] = matches_top_three

            print("-----------")
            
            with open("stats.json", "w") as outfile:
                json.dump(stats, outfile, indent=4)
            return
    print("Couldn't find legend named " + name)

def add_win():
    name = input("Name of legend: ")
    for legend in stats:
        if legend["name"].lower() == str(name).lower():
            legend["matches_won"] = legend["matches_won"] + 1
            print("-----------")
            return
    print("Couldn't find legend named " + name)

def add_match():
    name = input("Name of legend: ")
    for legend in stats:
        if legend["name"].lower() == str(name).lower():
            legend["matches_played"] = legend["matches_played"] + 1

            matches_won = int(input("Won this match: "))
            legend["matches_won"] = legend["matches_won"] + matches_won

            kills = int(input("Kills this match: "))
            legend["kills"] = legend["kills"] + kills

            damage = int(input("Damage this match: "))
            legend["damage"] = legend["damage"] + damage

            matches_top_three = int(input("Top three this match: "))
            legend["matches_top_three"] = legend["matches_top_three"] + matches_top_three

            print("-----------")
            return
    print("Couldn't find legend named " + name)

def view_stats():
    name = input("Name of legend: ")
    for legend in stats:
        if legend["name"].lower() == str(name).lower():
            print("-----------")
            print("Matches won: " + str(legend["matches_won"]))
            print("Kills: " + str(legend["kills"]))
            print("Damage: " + str(legend["damage"]))
            print("Matches played: " + str(legend["matches_played"]))
            print("Matches top three: " + str(legend["matches_top_three"]))
            if legend["matches_played"] > 0:
                kpm = legend["kills"] / legend["matches_played"]
                print("Kills per match: " + "%.2f" % (kpm))

                top_3_ratio = legend["matches_top_three"] / legend["matches_played"]
                print("Top 3 ratio: " + "%.2f" % (top_3_ratio))

                win_ratio = legend["matches_won"] / legend["matches_played"]
                print("Win ratio: " + "%.2f" % (win_ratio))

                adr = legend["damage"] / legend["matches_played"]
                print("ADR: " + "%.2f" % (adr))
            print("-----------")

while True:
    command = input("Update (u), view stats (v), add match (m), add win (a) or exit (e)?\n")
    if command == "u":
        update_stats()
    elif command == "m":
        add_match()
    elif command == "a":
        add_win()
    elif command == "v":
        view_stats()
    elif command == "e":
        break
    else:
        print("Not a valid command.")