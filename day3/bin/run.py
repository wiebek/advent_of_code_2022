#!/usr/bin/env python

import sys


def part1(file_):
    """Give the sum score for all the items that is in each of the halves of the string

    Args:
        file_ (file path): Path to the file
    """
    score = 0
    with open(file_) as f:
        for line in f:
            firstpart, secondpart = (
                line[: len(line) // 2],
                line[len(line) // 2 :].strip(),
            )

            cs = list(set([c for c in firstpart if c in secondpart]))
            for c in cs:
                if c.islower():
                    score += ord(c) - 96
                else:
                    score += ord(c) - 64 + 26

    print(score)


def main(file_):
    """
    05-12-2022
    Day 3: Rucksack Reorganization
    """
    part1(file_)
    data = open(file_, "r").readlines()
    data = [t.strip() for t in data]

    s = []
    score = 0
    for i in range(0, len(data), 3):
        temp = data[i : i + 3]
        s = s + list(set([c for c in temp[0] if c in temp[1] and c in temp[2]]))

    for c in s:
        if c.islower():
            score += ord(c) - 96
        else:
            score += ord(c) - 64 + 26

    print(score)


if __name__ == "__main__":
    main(sys.argv[1])
