#!/usr/bin/env python

import sys

d = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissor",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissor",
}

d_lose = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}

d_win = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}


def check_if_won(elf, me):
    """
    Check if you won the game
    """
    if elf == me:
        return 3
    elif (
        (elf == "Rock" and me == "Paper")
        or (elf == "Paper" and me == "Scissor")
        or (elf == "Scissor" and me == "Rock")
    ):
        return 6
    else:
        return 0


def score_gesture(me):
    """
    Return the score for the gesture given
    """
    if me == "Rock":
        return 1
    elif me == "Paper":
        return 2
    else:
        return 3


def part1(a, b, score):
    a, b = d[a], d[b]
    score += check_if_won(a, b)
    score += score_gesture(b)
    return score


def get_gesture(elf, me):
    """Based on "me" determine if we need to win, draw or lose

    Args:
        elf (string): gesture of the elf
        me (string): outcome determination
    """
    if me == "X":
        return d_lose[elf]
    elif me == "Z":
        return d_win[elf]
    else:
        return elf


def main(file_):
    """
    05-12-2022 WK
    Day 2: Rock Paper Scissors
    """
    # "X" = "lose"
    # "Y" = "draw"
    # "Z" = "win"

    score1 = 0
    score2 = 0
    with open(file_) as f:
        for line in f:
            a, b = line.strip().split()
            score1 = part1(a, b, score1)
            score2 = part1(a, get_gesture(a, b), score2)

    print(score1)
    print(score2)


if __name__ == "__main__":
    main(sys.argv[1])
