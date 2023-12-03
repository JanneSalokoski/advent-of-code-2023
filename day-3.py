""" AoC 2023 - Day 3 """

import re
import lib

numbers_re = re.compile(r"(\D|^)(\d+?)(\D|$)")
symbol_re = re.compile(r"[^\d\.]")
num_re = re.compile(r"\d+")

def get_part_nums(text):
    lines = text.split("\n")
    index = 0

    selections = []
    for line in lines:
        line = f".{line}."

        matches = re.finditer(num_re, line)
        for match in matches:
            selection = match.group()
            span = match.span()

            possible_symbols = ""
            possible_symbols += line[span[0] - 1]
            possible_symbols += line[span[1]]

            if index > 1:
                prev_line = f".{lines[index-1]}."
                prev_sel = prev_line[span[0]-1:span[1]+1]
                #print(f"- {prev_sel}")
                possible_symbols += prev_sel

            #print(f"= {line[span[0]-1:span[1]+1]}")

            if index < (len(lines) - 1):
                next_line = f".{lines[index+1]}."
                next_sel = next_line[span[0]-1:span[1]+1]
                #print(f"+ {next_sel}")
                possible_symbols += next_sel

            symbols = re.findall(symbol_re, possible_symbols)
            if len(symbols) > 0:
                selections.append({
                    "selection": selection,
                    "span": span,
                    "line": index
                }) 

        index += 1

    return selections

@lib.timer
@lib.aoc_input
def part_1(text=""):
    part_nums = get_part_nums(text)
    total = 0
    for num in part_nums:
        total += int(num["selection"])

    return total


@lib.timer
@lib.aoc_input
#@lib.aoc_sample
def part_2(text=""):
    gear_re = re.compile(r"\*")
    part_nums = get_part_nums(text) 

    total = 0
    index = 0
    for line in text.split("\n"):
        gear_matches = re.finditer(gear_re, line)
        for match in gear_matches:
            def is_adjacent(part):
                p_num = part["selection"]
                p_pos = part["span"]
                #print(f"Testing part: {p_num} at {p_pos}", end=" ")
                g_pos = match.span()[0] + 1
                #print(f"Gear at {index+1}:{g_pos}", end=" ")

                if (p_pos[0] >= g_pos and p_pos[0] <= g_pos+1 or
                    p_pos[1] >= g_pos and p_pos[0] <= g_pos+1):
                    #print("-> True")
                    return True

                #print("-> False")
                return False

            neighbour_lines = list(filter(lambda part: part["line"] >= index-1 and part["line"] <= index+1, part_nums))
            adjacent_parts = list(filter(is_adjacent, neighbour_lines))

            #print(f"* at {index+1}:{match.span()[0]+1} has {len(adjacent_parts)} neighbour part numbers")
            if len(adjacent_parts) == 2:
                total += int(adjacent_parts[0]["selection"]) * int(adjacent_parts[1]["selection"])

        index += 1

    return total


def main():
    p1 = part_1()
    print(f"Day 3 - Part 1 result: {p1}")

    print()

    p2 = part_2()
    print(f"Day 3 - Part 2 result: {p2}")

main()
