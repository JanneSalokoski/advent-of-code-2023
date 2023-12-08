""" AoC 2023 - Day 8 """

import logging
import logging.config

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
log = logging.getLogger("day-8")

import re
import lib
import math

def inst(lines):
    i = 0
    while True:
        yield lines[i]

        if i+1 == len(lines):
            i = 0
        else:
            i += 1

@lib.timer
#@lib.aoc_sample
@lib.aoc_input
def part_1(text=""):
    lines = text.split("\n")
    instructions = inst(lines[0])

    steps = lines[2:]

    nodes = {}
    for step in steps:
        node = step.split(" ")[0]
        left = step.split("(")[1].split(",")[0]
        right = step.split(", ")[1][:-1]

        nodes[node] = (left, right)

    count = 0
    curr = nodes["AAA"]
    while True:
        count += 1

        instruction = next(instructions)     
        next_key = curr[0] if instruction == "L" else curr[1]

        if next_key == "ZZZ":
            break
        
        curr = nodes[next_key]

    return count


def get_steps(nodes, start, line):
    instructions = inst(line)

    count = 0
    curr = start
    while True:
        count += 1

        instruction = next(instructions)     
        next_key = curr[0] if instruction == "L" else curr[1]

        if next_key[2] == "Z":
            break
        
        curr = nodes[next_key]

    return count

@lib.timer
#@lib.aoc_sample
@lib.aoc_input
def part_2(text=""):
    log.debug("Running part_2")

    lines = text.split("\n")

    steps = lines[2:]

    nodes = {}
    for step in steps:
        node = step.split(" ")[0]
        left = step.split("(")[1].split(",")[0]
        right = step.split(", ")[1][:-1]

        nodes[node] = (left, right)

    counts = []
    start_nodes = [node for node in nodes if node[2] == "A"]
    for start in start_nodes:
        counts.append(get_steps(nodes, nodes[start], lines[0]))

    log.debug(counts)

    return math.lcm(*counts)

def main():
    p1 = part_1()
    print(f"Day 8 - Part 1 result: {p1}")

    print()

    p2 = part_2()
    print(f"Day 8 - Part 2 result: {p2}")

main()
