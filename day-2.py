""" AoC 2023 - day 1 """

import re

def get_input():
    with open("./inputs/day1.txt", "r") as f:
        return f.read()

def round_1(text):
    total = 0

    maximums = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    lines = text.strip().split("\n")

    for line in lines:
        line_is_valid = True
        groups = line.split(";")

        for group in groups:
            colors = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }

            pairs = re.findall("(\d+?)\s(red|blue|green)", group)
            for pair in pairs:
                colors[pair[1]] += int(pair[0])

            if (colors["red"] > maximums["red"] or
                colors["green"] > maximums["green"] or
                colors["blue"] > maximums["blue"]):
                    line_is_valid = False
                    break

        if line_is_valid:
            id = int(re.findall("Game (\d+?):", line)[0])
            total += id

    print(f"Total: {total}")

def round_2(text):
    total = 0
    lines = text.strip().split("\n")

    for line in lines:
        line_is_valid = True

        minimums = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        pairs = re.findall("(\d+?)\s(red|blue|green)", line)
        for pair in pairs:
            if minimums[pair[1]] < int(pair[0]):
                minimums[pair[1]] = int(pair[0])

        power = minimums["red"] * minimums["green"] * minimums["blue"]
        total += power

    print(f"Total: {total}")

def main():
    text = get_input()

    #round_1(text)
    round_2(text)

main()
