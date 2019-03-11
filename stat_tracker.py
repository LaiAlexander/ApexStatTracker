import json

with open("legends.json", "r") as read_file:
    legends = json.load(read_file)

try:
    with open("stats.json", "r") as read_file:
        stats = json.load(read_file)
except OSError:
    stats = legends
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
            kills = int(input("Kills: "))
            legend["kills"] = kills

            damage = int(input("Damage: "))
            legend["damage"] = damage

            matches_played = int(input("Matches played: "))
            legend["matches_played"] = matches_played

            matches_won = int(input("Matches won: "))
            legend["matches_won"] = matches_won

            matches_top_three = int(input("Matches top three: "))
            legend["matches_top_three"] = matches_top_three

            with open("stats.json", "w") as outfile:
                json.dump(stats, outfile, indent=4)
            return
    print("Couldn't find legend named " + name)

def add_win():
    name = input("Name of legend: ")
    for legend in stats:
        if legend["name"].lower() == str(name).lower():
            legend["matches_won"] = legend["matches_won"] + 1
            return
    print("Couldn't find legend named " + name)

def add_match():
    name = input("Name of legend: ")
    for legend in stats:
        if legend["name"].lower() == str(name).lower():
            legend["matches_played"] = legend["matches_played"] + 1

            kills = int(input("Kills: "))
            legend["kills"] = legend["kills"] + kills

            damage = int(input("Damage: "))
            legend["damage"] = legend["damage"] + damage

            matches_won = int(input("Won match: "))
            legend["matches_won"] = legend["matches_won"] + matches_won

            matches_top_three = int(input("Top three: "))
            legend["matches_top_three"] = legend["matches_top_three"] + matches_top_three
            return
    print("Couldn't find legend named " + name)

def view_stats():
    name = input("Name of legend: ")
    for legend in stats:
        if legend["name"].lower() == str(name).lower():
            print("Kills: " + str(legend["kills"]))
            print("Damage: " + str(legend["damage"]))
            print("Matches played: " + str(legend["matches_played"]))
            print("Matches won: " + str(legend["matches_won"]))
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
            return
    print("Couldn't find legend named " + name)

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