""" AoC 2023 - Day 7 """

import logging
import logging.config

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
log = logging.getLogger("day-7")

import re
import lib

import functools

from enum import Enum

class Card1(Enum):
    ACE = 14
    KING = 13
    QUEEN = 12
    JACK = 11
    TEN = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2

class Card2(Enum):
    ACE = 14
    KING = 13
    QUEEN = 12
    TEN = 11
    NINE = 10
    EIGHT = 9
    SEVEN = 8
    SIX = 7
    FIVE = 6
    FOUR = 5
    THREE = 4
    TWO = 3
    JOKER = 2

class Type(Enum):
    FIVE = 7
    FOUR = 6
    HOUSE = 5
    THREE = 4
    TWO_PAIR = 3
    PAIR = 2
    HIGH = 1

@functools.total_ordering
class Hand:
    def __init__(self, text, part=2):
        self.text = text.split(" ")[0]
        self.part = part

        self.cards = self.get_cards(text.split(" ")[0])
        self.bid = int(text.split(" ")[1])
        self.type = self.get_type(self.cards)

        log.debug(f"{self.text} -> {self.type}")

    def get_card(self, letter):
        if self.part == 1:
            match letter:
                case "A": return Card1.ACE
                case "K": return Card1.KING
                case "Q": return Card1.QUEEN
                case "J": return Card1.JACK
                case "T": return Card1.TEN
                case "9": return Card1.NINE
                case "8": return Card1.EIGHT 
                case "7": return Card1.SEVEN 
                case "6": return Card1.SIX 
                case "5": return Card1.FIVE 
                case "4": return Card1.FOUR 
                case "3": return Card1.THREE 
                case "2": return Card1.TWO 
                case _: raise ValueError

        match letter:
            case "A": return Card2.ACE
            case "K": return Card2.KING
            case "Q": return Card2.QUEEN
            case "T": return Card2.TEN
            case "9": return Card2.NINE
            case "8": return Card2.EIGHT 
            case "7": return Card2.SEVEN 
            case "6": return Card2.SIX 
            case "5": return Card2.FIVE 
            case "4": return Card2.FOUR 
            case "3": return Card2.THREE 
            case "2": return Card2.TWO 
            case "J": return Card2.JOKER
            case _: raise ValueError


    def get_cards(self, text):
        return [self.get_card(c) for c in text]

    def get_type(self, cards):
        amounts = [0]
        lst_of_cards = [card for card in cards if card.name != "JOKER"]
        set_of_cards = set(lst_of_cards)

        for card in set([card for card in cards if card.name != "JOKER"]):
            amounts.append(cards.count(card))

        maximum = max(amounts)

        max_index = amounts.index(maximum)
        for i in range(sum([1 for card in cards if card.name == "JOKER"])):
            amounts[max_index] += 1

        maximum = max(amounts)

        if maximum == 5:
            return Type.FIVE
        elif maximum == 4:
            return Type.FOUR
        elif 3 in amounts and 2 in amounts:
            return Type.HOUSE
        elif maximum == 3:
            return Type.THREE
        elif amounts.count(2) == 2:
            return Type.TWO_PAIR
        elif maximum == 2:
            return Type.PAIR
        else:
            return Type.HIGH

    def _is_valid_op(self, other):
        return isinstance(other, Hand)

    def __lt__(self, other):
        if not self._is_valid_op(other):
            return NotImplemented

        if not self.type.value == other.type.value:
            return self.type.value < other.type.value

        for i in range(len(self.cards)):
            if not self.cards[i].value == other.cards[i].value:
                return self.cards[i].value < other.cards[i].value

        return False

    def __eq__(self, other):
        if not self._is_valid_op(other):
            return NotImplemented

        return self.text == other.text

    def __repr__(self):
        return f"Hand {self.text} ({self.type.name})"

    def __str__(self):
        return self.__repr__()

#@lib.aoc_sample
@lib.aoc_input
def parse_input(text=""):
    #text = "23456 100\nJ2345 100\nJJ234 100"
    lines = text.split("\n")
    return [Hand(line) for line in lines]

@lib.timer
def part_1(hands):
    log.debug("Running part_1")

    score = 0

    sorted_hands = sorted(hands)
    for i, hand in enumerate(sorted_hands):
        rank = i+1
        log.debug(f"{hand} -> rank {rank} * bid {hand.bid} = {rank*hand.bid}")        
        score += rank * hand.bid

    return score

@lib.timer
def part_2(hands):
    log.debug("Running part_2")

    score = 0

    sorted_hands = sorted(hands)
    for i, hand in enumerate(sorted_hands):
        rank = i+1
        log.debug(f"{hand} -> rank {rank} * bid {hand.bid} = {rank*hand.bid}")        
        score += rank * hand.bid

    return score

def main():
    hands = parse_input()

    p1 = part_1(hands)
    print(f"Day 7 - Part 1 result: {p1}")

    print()

    p2 = part_2(hands)
    print(f"Day 7 - Part 2 result: {p2}")

main()
