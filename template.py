""" AoC 2023 - Day XXX """

import logging
import logging.config

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
log = logging.getLogger("day-XXX")

import re
import lib

@lib.timer
#@lib.aoc_sample
@lib.aoc_input
def part_1(text=""):
    log.debug("Running part_1")

@lib.timer
#@lib.aoc_sample
@lib.aoc_input
def part_2(text=""):
    log.debug("Running part_1")

def main():
    p1 = part_1()
    print(f"Day XXX - Part 1 result: {p1}")

    print()

    p2 = part_2()
    print(f"Day XXX - Part 2 result: {p2}")

main()
