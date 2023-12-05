""" AoC 2023 - Day 4 """

import logging
import logging.config

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
log = logging.getLogger("day-4")

import re
import lib

import sys

import functools

def handle_line_1(line):
    sides = line.split("|")
    winning = list(map(lambda num: int(num),
                list(filter(lambda num: num != "",
                    sides[0]
                        .split(":")[1]
                        .strip()
                        .split(" ")))))

    yours = list(map(lambda num: int(num),
                list(filter(lambda num: num != "",
                    sides[1]
                        .strip()
                        .split(" ")))))

    score = 0
    for num in yours:
        if score > 0:
            score = score*2 if num in winning else score
        else:
            score = 1 if num in winning else score

    return score

@lib.timer
#@lib.aoc_sample
@lib.aoc_input
def part_1(text=""):
    scores = [handle_line_1(line) for line in text.split("\n")]
    return sum(scores)


completed_cards = {}

def handle_line_2(line, lines, depth):
    sides = line.split("|")

    card = int(sides[0].split(":")[0].replace(" ", "").replace("Card", ""))

    winning = list(map(lambda num: int(num),
                list(filter(lambda num: num != "",
                    sides[0]
                        .split(":")[1]
                        .strip()
                        .split(" ")))))

    yours = list(map(lambda num: int(num),
                list(filter(lambda num: num != "",
                    sides[1]
                        .strip()
                        .split(" ")))))

    amount = 0
    for num in yours:
        amount += 1 if num in winning else 0

    #log.debug(f"Amount: {amount}")

    score = 1

    for i in range(1, amount+1):
        
        if card+i in completed_cards:
            log.debug(f"{'  '*depth}Found {card} in completed")
            score += completed_cards[card+i]
        else:
            log.debug(f"{'  '*depth}Card {card} wins {amount} cards")
            #score += handle_line_2(lines[card+i-1], lines, depth+1)

    if amount == 0:
        log.debug(f"{'  '*depth}Card {card} -> completed")
        completed_cards[card] = score

    return score


@lib.timer
#@lib.aoc_sample
@lib.aoc_input
def part_2(text=""):
    lines = text.split("\n")

    def get_card_amounts(lines):
        cards = []
        for line in lines:
            card = int(line.split("|")[0].split(":")[0].replace(" ", "").replace("Card", ""))
            wins = line.split("|")[0].split(":")[1].strip().replace("  ", " ").split(" ")
            yours = line.split("|")[1].strip().replace("  ", " ").split(" ")
            winning = len([num for num in yours if num in wins])

            cards.append(winning)

        return cards

    cards = get_card_amounts(lines)

    handled = {}

    def handle_card(wins, idx, depth):
        #log.debug(f"{'  '*depth}{lines[idx]}")

        if idx in handled:
            log.debug(f"{'  '*depth}Card {idx+1} = {handled[idx]} (already handled)")
            return handled[idx]

        if wins == 0:
            log.debug(f"{'  '*depth}Card {idx+1} = 1")
            handled[idx] = 1
            return 1
        else:
            log.debug(f"{'  '*depth}Card {idx+1} wins {wins}:")
            total = 1
            for i in range(1, wins+1):
                new_amount = handle_card(cards[idx + i], idx+i, depth+1)
                log.debug(f"{'  '*depth}Card {idx+1} = {total+new_amount} ({total}+{new_amount}={total+new_amount})")
                total += new_amount

            handled[idx] = total

            print()
            return total


    score = 0
    for i, card in reversed(list(enumerate(cards))):
        new_score = handle_card(card, i, 0)
        score += new_score

    return score

    

def main():
    sys.setrecursionlimit(100000)

    p1 = part_1()
    print(f"Day 4 - Part 1 result: {p1}")

    print()

    p2 = part_2()
    print(f"Day 4 - Part 2 result: {p2}")

main()
