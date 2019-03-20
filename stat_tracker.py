"""
A script to help track stats in the game Apex Legends
"""

import json

with open("legends.json", "r") as read_file:
    legends = json.load(read_file)

try:
    with open("stats.json", "r") as read_file:
        stats = json.load(read_file)
except FileNotFoundError:
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

def print_current_stats(legend):
    kpm, adr = calculate_stats(legend["kills"], 
                                legend["damage"],
                                legend["matches_played"])
    print("Current wins: " + str(legend["matches_won"]))
    print("Current kills per match: " + "%.2f" % kpm)
    print("Current ADR: " + "%.2f" % adr)
    print("----------")

def update_stats():
    name = input("Name of legend: ")
    for legend in stats:
        if legend["name"].lower() == str(name).lower():
            print_current_stats(legend)

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

            print_current_stats(legend)

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
            with open("stats.json", "w") as outfile:
                json.dump(stats, outfile, indent=4)
            return
    print("Couldn't find legend named " + name)

def add_match():
    name = input("Name of legend: ")
    for legend in stats:
        if legend["name"].lower() == str(name).lower():
            print_current_stats(legend)

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

            print_current_stats(legend)

            with open("stats.json", "w") as outfile:
                json.dump(stats, outfile, indent=4)
            return
    print("Couldn't find legend named " + name)

def calculate_stats(kills, damage, matches_played, matches_won=None, matches_top_three=None):
    kpm = 0
    top_3_ratio = 0
    win_ratio = 0
    adr = 0
    if matches_played > 0:
        kpm = kills / matches_played
        adr = damage / matches_played
        if (matches_won is None or matches_top_three is None):
            return kpm, adr
        top_3_ratio = matches_top_three / matches_played
        win_ratio = matches_won / matches_played
        return kpm, top_3_ratio, win_ratio, adr
    return kpm, adr

def view_stats():
    name = input("Name of legend: ")
    for legend in stats:
        if legend["name"].lower() == str(name).lower():
            print_stats(legend["kills"], 
                        legend["damage"],
                        legend["matches_played"],
                        legend["matches_won"],
                        legend["matches_top_three"])

def view_all_stats():
    matches_won = 0
    kills = 0
    damage = 0
    matches_played = 0
    matches_top_three = 0

    for legend in stats:
        matches_won = matches_won + legend["matches_won"]
        kills = kills + legend["kills"]
        damage = damage + legend["damage"]
        matches_played = matches_played + legend["matches_played"]
        matches_top_three = matches_top_three + legend["matches_top_three"]
    print_stats(kills, damage, matches_played, matches_won, matches_top_three)

def print_stats(kills, damage, matches_played, matches_won, matches_top_three):
    print("-----------")
    print("Matches won: " + str(matches_won))
    print("Kills: " + str(kills))
    print("Damage: " + str(damage))
    print("Matches played: " + str(matches_played))
    print("Matches top three: " + str(matches_top_three))
    kpm, top_3_ratio, win_ratio, adr = calculate_stats(kills,
                                        damage,
                                        matches_played,
                                        matches_won,
                                        matches_top_three
                                        )
    print("Kills per match: " + "%.2f" % kpm)
    print("Top 3 ratio: " + "%.2f" % top_3_ratio)
    print("Win ratio: " + "%.2f" % win_ratio)
    print("ADR: " + "%.2f" % adr)
    print("-----------")

while True:
    command = input("Update (u),\n" +
            "View stats (v),\n" +
            "View all stats (s),\n" +
            "Add match (m),\n" +
            "Add win (w) or\n" +
            "Exit (e)?\n")
    if command == "u":
        update_stats()
    elif command == "m":
        add_match()
    elif command == "w":
        add_win()
    elif command == "v":
        view_stats()
    elif command == "s":
        view_all_stats()
    elif command == "e":
        break
    else:
        print("Not a valid command.")
