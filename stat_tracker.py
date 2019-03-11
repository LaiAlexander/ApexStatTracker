import json

with open("legends.json", "r") as read_file:
    legends = json.load(read_file)

try:
    with open("stats.json", "r") as read_file:
        stats = json.load(read_file)
except OSError:
    stats = legends
    for legend in stats:
        legend["kills"] = "0"
        legend["damage"] = "0"
        legend["matches_played"] = "0"
        legend["matches_won"] = "0"
        legend["matches_top_three"] = "0"
    with open("stats.json", "w") as outfile:
        json.dump(stats, outfile, indent=4)

print("Stat Tracker for Apex Legends\n")

def update_stats():
    name = input("Name of legend: ")
    for legend in stats:
        if str(legend["name"]).lower() == str(name).lower():
            kills = input("Kills: ")
            legend["kills"] = kills

            damage = input("Damage: ")
            legend["damage"] = damage

            matches_played = input("Matches played: ")
            legend["matches_played"] = matches_played

            matches_won = input("Matches won: ")
            legend["matches_won"] = matches_won

            matches_top_three = input("Matches top three: ")
            legend["matches_top_three"] = matches_top_three

            with open("stats.json", "w") as outfile:
                json.dump(stats, outfile, indent=4)
    print("Couldn't find legend named " + name)

def view_stats():
    name = input("Name of legend: ")
    for legend in stats:
        if str(legend["name"]).lower() == str(name).lower():
            print("Kills: " + legend["kills"])
            print("Damage: " + legend["damage"])
            print("Matches played: " + legend["matches_played"])
            print("Matches won: " + legend["matches_won"])
            print("Matches top three: " + legend["matches_top_three"])
            if int(legend["matches_played"]) > 0:
                kpm = round(int(legend["kills"]) / int(legend["matches_played"]), 2)
                print("Kills per match: " + str(kpm))
                top_3_ratio = round(int(legend["matches_top_three"]) / int(legend["matches_played"]), 2)
                print("Top 3 ratio: " + str(top_3_ratio))
                win_ratio = round(int(legend["matches_won"]) / int(legend["matches_played"]), 2)
                print("Win ratio: " + str(win_ratio))
                adr = round(int(legend["damage"]) / int(legend["matches_played"]), 2)
                print("ADR: " + str(adr))
    print("Couldn't find legend named " + name)

while True:
    command = input("Update (u), view stats (v) or exit (e)?\n")
    if command == "u":
        update_stats()
    elif command == "v":
        view_stats()
    elif command == "e":
        break
    else:
        print("Not a valid command.")


for legend in stats:
    print("Name: " + legend["name"] + "\n" + "Kills: " + legend["kills"])