#!/usr/bin/env python

import sys


def check_if_full_contain(a1, a2, b1, b2):
    return (int(a1) <= int(b1) and int(a2) >= int(b2)) or (
        int(b1) <= int(a1) and int(b2) >= int(a2)
    )


def check_if_overlap_on_sides(a1, a2, b2):
    return int(a1) <= int(b2) and int(a2) >= int(b2)


def check_if_overlap_on_sides2(a2, b1, b2):
    return int(b1) <= int(a2) and int(b2) >= int(a2)


def main(file_):
    """
    05-12-2022
    Day 4: Camp Cleanup
    """
    score = 0
    score2 = 0
    with open(file_) as f:
        for line in f:
            line = line.strip()
            a, b = line.split(",")
            a1, a2 = a.split("-")
            b1, b2 = b.split("-")
            if check_if_full_contain(a1, a2, b1, b2):
                score += 1
            if (
                (check_if_overlap_on_sides(a1, a2, b2))
                or (check_if_overlap_on_sides2(a2, b1, b2))
                or (check_if_full_contain(a1, a2, b1, b2))
            ):
                score2 += 1

    print(score)
    print(score2)


if __name__ == "__main__":
    main(sys.argv[1])
