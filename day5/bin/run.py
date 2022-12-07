#!/usr/bin/env python

import sys


def display_stacks(stacks):
    print("\n\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")


def load_stacks(stack_strings, indexes, stacks):
    for string in stack_strings[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] != " ":
                stacks[stack_num].insert(0, string[index])
            stack_num += 1
    return stacks


def empty_stacks(stacks):
    for stack_num in stacks:
        stacks[stack_num].clear()
    return stacks


def get_stack_ends(stacks):
    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer


def main(file_):
    """
    06-12-2022
    Day 5: Supply Stacks
    https://www.youtube.com/watch?v=LvH2DU1bARk&ab_channel=JefferyFrederic
    """
    with open(file_) as f:
        stack_strings, instructions = (
            i.splitlines() for i in f.read().strip("\n").split("\n\n")
        )

    stacks = {int(digit): [] for digit in stack_strings[-1].replace(" ", "")}
    indexes = [index for index, c in enumerate(stack_strings[-1]) if c != " "]
    load_stacks(stack_strings, indexes, stacks)

    # === PART 1 === #

    for instruction in instructions:
        instruction = instruction.strip().split(" ")
        crates, from_, to = (
            int(instruction[1]),
            int(instruction[3]),
            int(instruction[5]),
        )

        for _ in range(crates):
            crate_removed = stacks[from_].pop()
            stacks[to].append(crate_removed)

    print(f"Answer for part 1: {get_stack_ends(stacks)}")

    # === PART 2 === #
    empty_stacks(stacks)
    load_stacks(stack_strings, indexes, stacks)

    for instruction in instructions:
        instruction = instruction.strip().split(" ")
        crates, from_, to = (
            int(instruction[1]),
            int(instruction[3]),
            int(instruction[5]),
        )

        crates_to_remove = stacks[from_][-crates:]  # finding out which crates to remove
        stacks[from_] = stacks[from_][:-crates]  # removing crates

        for crate in crates_to_remove:
            stacks[to].append(crate)  # adding crates

    print(f"Answer for part 2: {get_stack_ends(stacks)}")


if __name__ == "__main__":
    main(sys.argv[1])
