#!/usr/bin/env python

import sys


def main(file_):
    """
    07-12-2022
    Day 6: Tuning Trouble
    """

    # === PART 1 === #
    with open(file_) as f:
        for line in f:
            line = line.strip()
            for i in range(0, len(line)):
                tmp = line[i : i + 4]
                if len(list(tmp)) == len(set(list(tmp))):
                    print(f"Answer for part 1: {i + 4}")
                    break

    # === PART 2 === #
    with open(file_) as f:
        for line in f:
            line = line.strip()
            for i in range(0, len(line)):
                tmp = line[i : i + 14]
                if len(list(tmp)) == len(set(list(tmp))):
                    print(f"Answer for part 2: {i + 14}")
                    break


if __name__ == "__main__":
    main(sys.argv[1])
