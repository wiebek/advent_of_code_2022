#!/usr/bin/env python

import sys


def main(file_):
    """
    2022/01: Calorie Counting
    Find the elf with the most calories
    """
    d = dict()
    elf = 1
    cal = 0
    with open(file_) as f:
        for line in f:
            line = line.strip()
            if line == "":
                d[elf] = cal
                elf += 1
                cal = 0
            if line != "":
                cal += int(line)
    d[elf] = cal
    elf += 1

    print(max(d.values()))
    print(sum(sorted(d.values(), reverse=True)[:3]))


if __name__ == "__main__":
    main(sys.argv[1])
