"""
A script to help track stats in the game Apex Legends
"""

import json

with open("legends2.json", "r") as read_file:
    legends = json.load(read_file)

try:
    with open("stats2.json", "r") as read_file:
        stats = json.load(read_file)
        for legend in legends:
            if legend not in stats:
                stats[legend] = dict()
                stats[legend]["kills"] = 0
                stats[legend]["damage"] = 0
                stats[legend]["matches_played"] = 0
                stats[legend]["matches_won"] = 0
                stats[legend]["matches_top_three"] = 0
        with open("stats2.json", "w") as outfile:
            json.dump(stats, outfile, indent=4)
except FileNotFoundError:
    stats = legends
    for legend in stats:
        stats[legend]["kills"] = 0
        stats[legend]["damage"] = 0
        stats[legend]["matches_played"] = 0
        stats[legend]["matches_won"] = 0
        stats[legend]["matches_top_three"] = 0
    with open("stats2.json", "w") as outfile:
        json.dump(stats, outfile, indent=4)

def print_current_stats(legend):
    kpm, adr = calculate_stats(legend["kills"],
                               legend["damage"],
                               legend["matches_played"])
    print("Current wins: " + str(legend["matches_won"]))
    print("Current kills per match: " + "%.2f" % kpm)
    print("Current ADR: " + "%.2f" % adr)
    print("----------")

def update_stats():
    name = input("Name of legend: ").capitalize()
    legend = stats.get(name, False)
    if legend:
        print_current_stats(legend)
        legend["matches_won"] = take_input("Matches won: ")
        legend["kills"] = take_input("Kills: ")
        legend["damage"] = take_input("Damage: ")
        legend["matches_played"] = take_input("Matches played: ")
        legend["matches_top_three"] = take_input("Matches top three: ")
        print("-----------")

        print_current_stats(legend)

        with open("stats2.json", "w") as outfile:
            json.dump(stats, outfile, indent=4)
        return
    print("Couldn't find legend named " + name)

def take_input(text):
    entry = input(text)
    if entry.isdigit():
        entry = int(entry)
    else:
        entry = 0
    return entry

def add_win():
    name = input("Name of legend: ").capitalize()
    legend = stats.get(name, False)
    if legend:
        legend["matches_won"] = legend["matches_won"] + 1
        print("-----------")
        with open("stats2.json", "w") as outfile:
                json.dump(stats, outfile, indent=4)
        return
    print("Couldn't find legend named " + name)

def add_match():
    name = input("Name of legend: ").capitalize()
    legend = stats.get(name, False)
    if legend:
        print_current_stats(legend)

        legend["matches_played"] = legend["matches_played"] + 1
        legend["matches_won"] = (legend["matches_won"]
                                    + take_input("Won this match: "))
        legend["kills"] = (legend["kills"]
                            + take_input("Kills this match: "))
        legend["damage"] = (legend["damage"]
                            + take_input("Damage this match: "))
        legend["matches_top_three"] = (legend["matches_top_three"]
                                        + take_input("Top three this match: "))
        
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
        if matches_won is None or matches_top_three is None:
            return kpm, adr
        top_3_ratio = matches_top_three / matches_played
        win_ratio = matches_won / matches_played
    if matches_won is None or matches_top_three is None:
        return kpm, adr
    return kpm, top_3_ratio, win_ratio, adr

def view_stats():
    name = input("Name of legend: ").capitalize()
    legend = stats.get(name, False)
    if legend:
        print_stats(legend["kills"],
                    legend["damage"],
                    legend["matches_played"],
                    legend["matches_won"],
                    legend["matches_top_three"])
        return
    print("Couldn't find legend named " + name)

def view_all_stats():
    matches_won = 0
    kills = 0
    damage = 0
    matches_played = 0
    matches_top_three = 0

    for legend in stats:
        matches_won = matches_won + stats[legend]["matches_won"]
        kills = kills + stats[legend]["kills"]
        damage = damage + stats[legend]["damage"]
        matches_played = matches_played + stats[legend]["matches_played"]
        matches_top_three = matches_top_three + stats[legend]["matches_top_three"]
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
                                                       matches_top_three)
    print("Kills per match: " + "%.2f" % kpm)
    print("Top 3 ratio: " + "%.2f" % top_3_ratio)
    print("Win ratio: " + "%.2f" % win_ratio)
    print("ADR: " + "%.2f" % adr)
    print("-----------")

def run():
    print("Stat Tracker for Apex Legends\n")

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

run()
