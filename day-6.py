""" AoC 2023 - Day 6 """

import logging
import logging.config

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
log = logging.getLogger("day-6")

import re
import lib

from functools import reduce
from operator import mul

def try_convert(text):
    try:
        int(text)
    except:
        return False

    return True

@lib.timer
#@lib.aoc_sample
@lib.aoc_input
def part_1(text=""):
    log.debug("Running part_1")

    lines = text.split("\n")

    times = [int(time) for time in lines[0].split(" ")[1:] if try_convert(time)]
    distances = [int(dist) for dist in lines[1].split(" ")[1:] if try_convert(dist)]

    races = list(zip(times, distances))
    log.debug(f"Races: {races}")

    win_amounts = []
    for race in races:
        log.debug(f"Handling race: {race}")
        wins = 0
        for secs in range(race[0]):
            time = race[0] - secs
            speed = secs
            dist = time*speed
            
            if dist > race[1]:
                #log.debug(f"T: {time}, V: {speed}, S: {dist}")
                wins += 1

        log.debug(f"  Wins {wins} times")
        win_amounts.append(wins)

    return reduce(mul, win_amounts)
            


@lib.timer
#@lib.aoc_sample
@lib.aoc_input
def part_2(text=""):
    log.debug("Running part_1")

    lines = text.split("\n")

    time = int(lines[0].replace(" ", "").split(":")[1])
    wanted_dist = int(lines[1].replace(" ", "").split(":")[1])

    log.debug(f"Time: {time}, dist: {wanted_dist}")    

    low_bound = 0
    for wait_time in range(time):
        time_left = time - wait_time
        speed = wait_time
        dist = time_left * speed

        if dist > wanted_dist:
            log.debug(f"Low bound {wait_time}")
            low_bound = wait_time
            break

    hi_bound = 0
    for wait_time in range(time, 0, -1):
        time_left = time - wait_time
        speed = wait_time
        dist = time_left * speed

        if dist > wanted_dist:
            log.debug(f"High bound {wait_time}")
            hi_bound = wait_time
            break

    wins = (hi_bound - low_bound) + 1

    return wins

def main():
    p1 = part_1()
    print(f"Day 6 - Part 1 result: {p1}")

    print()

    p2 = part_2()
    print(f"Day 6 - Part 2 result: {p2}")

main()
