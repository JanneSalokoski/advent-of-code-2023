""" AoC 2023 - Day 5 """

import logging
import logging.config

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
log = logging.getLogger("day-5")

import re
import lib

class SeedRange:
    def __init__(self, start, range):
        self.lo = start
        self.hi = start + range

    def in_range(self, num):
        return num in range(self.lo, self.hi)

    def __repr__(self):
        return f"SeedRange ({self.lo}..{self.hi})"

    def __str__(self):
        return f"SeedRange ({self.lo}..{self.hi})"

class Mapping:
    def __init__(self, text):
        nums = [int(num) for num in text.split(" ")]
        self.src = nums[1]
        self.dst = nums[0]
        self.rng = nums[2]

        self.diff = self.dst - self.src

        self.lo = self.src
        self.hi = self.src + self.rng

    def in_range(self, num):
        return num in range(self.lo, self.hi)

    def map(self, num):
        if self.in_range(num):
            return num + self.diff

        raise ValueError(f"{num} not in range {self.lo}..{self.hi}")

    def __repr__(self):
        return f"Mapping ({self.lo}..{self.hi}) -> ({self.lo+self.diff}..{self.hi+self.diff})"

    def __str__(self):
        return f"Mapping ({self.lo}..{self.hi}) -> ({self.lo+self.diff}..{self.hi+self.diff})"

class Map:
    def __init__(self, text):
        lines = text.split("\n")
        self.src = lines[0].split("-")[0]
        self.dst = lines[0].split(" ")[0].split("-")[2]

        self.mappings = self.get_mappings(lines[1:])

    def get_mappings(self, lines):
        return [Mapping(line) for line in lines]

    def get_matching_mappings(self, num):
        return [mapping for mapping in self.mappings if mapping.in_range(num)]

    def map(self, num):
        for mapping in self.mappings:
            if mapping.in_range(num):
                return mapping.map(num)

        return num

    def __repr__(self):
        return f"Map {self.src} -> {self.dst}"

    def __str__(self):
        return f"Map {self.src} -> {self.dst}"


def seed_to_loc(seed, maps):
    for map in maps:
        seed = map.map(seed)

    return seed


#inp = lib.aoc_sample
inp = lib.aoc_input

@inp
def get_seeds(text=""):
    return [int(num) for num in text.split("\n")[0].split(": ")[1].split(" ")]

def get_seed_ranges(seeds):
    return [SeedRange(pair[0], pair[1]) for pair in zip(seeds[0::2], seeds[1::2])]


@inp
def get_maps(text=""):
    return [Map(group) for group in text.split("\n\n")[1:]]

@lib.timer
def part_1(maps, seeds):
    log.debug("Running part_1")

    return min([seed_to_loc(seed, maps) for seed in seeds])

@lib.timer
def part_2(maps, seed_ranges):
    log.debug("Running part_2")

    #s_lo = seed_ranges[0].lo

    #log.debug(f"Finding {s_lo}")
    #matches = maps[0].get_matching_mappings(s_lo)
    #los = [match.map(match.lo) for match in matches]
    #log.debug(f"los: {los}")


    def transform(map, nums):
        res = []
        for num in nums:
            matching = map.get_matching_mappings(num)
            for match in matching:
                res.append(match.map(match.lo))



        if len(res) >= 1:
            log.debug(f"{map} :: >> :: {res} ({len(res)})")
            return res

        log.debug(f"{map} :: == :: {nums} ({len(nums)})")
        return nums

    los = transform(maps[0], seed_ranges)
    los2 = transform(maps[1], los)
    los3 = transform(maps[2], los2)
    los4 = transform(maps[3], los3)
    los5 = transform(maps[4], los4)
    los6 = transform(maps[5], los5)
    los7 = transform(maps[6], los6)

    return 0

def main():
    seeds = get_seeds()
    maps = get_maps()

    p1 = part_1(maps, seeds)
    print(f"Day 5 - Part 1 result: {p1}")

    print()

    p2 = part_2(maps, get_seed_ranges(seeds))
    print(f"Day 5 - Part 2 result: {p2}")

main()
