""" AoC 2023 - Day 9 """
import logging
import logging.config

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
log = logging.getLogger("day-9")

import re
import lib

def extrapolate(lines, idx):
    total = 0
    for line in lines:
        nums = [int(n) for n in line.split(" ")]
        #log.debug(f"Sequence: {nums}")

        sequences = [nums]

        while not set(nums) == set([0]):
            pairs = list(zip(nums[0:], nums[1:]))

            tmp = []
            for pair in pairs:
                diff = pair[1] - pair[0]
                tmp.append(diff)

            sequences.append(tmp)
            nums = tmp

        for i, seq in enumerate(reversed(sequences)):
            if set(seq) == set([0]):
                if not idx >= 0:
                    seq.append(0)
                else:
                    seq.insert(0, 0)
            else:
                this_num = seq[idx]
                prev_num = list(reversed(sequences))[i-1][idx]
                if not idx >= 0:
                    seq.append(this_num + prev_num)
                else:
                    seq.insert(0, this_num - prev_num)

        new = sequences[0][idx]
        #log.debug(f"Next value: {next}")
        total += new

    return total

@lib.timer
#@lib.aoc_sample
@lib.aoc_input
def part_1(text=""):
    log.debug("Running part_1")
    return extrapolate(text.split("\n"), -1)

@lib.timer
#@lib.aoc_sample
@lib.aoc_input
def part_2(text=""):
    log.debug("Running part_2")
    return extrapolate(text.split("\n"), 0)

def main():
    p1 = part_1()
    print(f"Day 9 - Part 1 result: {p1}")

    print()

    p2 = part_2()
    print(f"Day 9 - Part 2 result: {p2}")

main()
