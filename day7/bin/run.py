#!/usr/bin/env python

import sys
import os


def compute_dirsize(dirname: str, direct_directory_size: dict, subdirs: dict):
    dirsize = direct_directory_size[
        dirname
    ]  # initialise the size by the size of the directory excluding the subdirectories
    for ii in subdirs[dirname]:  # go through all the subdirectories
        if ii in subdirs:
            dirsize += compute_dirsize(
                ii, direct_directory_size, subdirs
            )  # looping the subdirectory size addition until we no longer find the subdirectories
    return dirsize


def main(file_):
    """
    07-12-2022
    Day 7: No Space Left On Device
    https://www.youtube.com/watch?v=Io6AfTzadME&ab_channel=StudyingAsYouWere
    """

    with open(file_, "r") as file:
        data = file.read().strip().split("\n")

    # initialise dicts
    subdirs = {}  # store the subdirectories here
    direct_directory_size = (
        {}
    )  # store the directory sizes here (excluding all the subdirectories)

    # extracting the folder structure
    for line in data:
        if line[0] == "$":
            ds, cmd, *ddir = line.split()
            if cmd == "cd":
                path = ddir[0]
                if path == "/":  # for the top directory
                    curdir = path  # this is the current directory
                else:
                    curdir = os.path.normpath(os.path.join(curdir, path))
                if (
                    curdir not in subdirs
                ):  # if we have not seen our current directory before
                    subdirs[curdir] = []
                    direct_directory_size[curdir] = 0

        else:  # if we get 'dir' or numbers instead of '$'
            fsize, fname = line.split()
            if fsize != "dir":  # if we get numbers
                direct_directory_size[curdir] += int(fsize)
            else:  # if we get a new directory
                subdirs[curdir].append(os.path.normpath(os.path.join(curdir, fname)))

    # size calculation function

    # Part 1: Sum of all the directories with a total size of at most 100000.
    sol_pt1 = 0
    for ii in subdirs:
        dirsize = compute_dirsize(
            dirname=ii, direct_directory_size=direct_directory_size, subdirs=subdirs
        )
        if dirsize <= 100000:
            sol_pt1 += dirsize
    print("The answer to the first questions is: " + str(sol_pt1))

    # Part 2: The smallest possible file to delete to free up the required space.
    total_space = 70000000
    space_required = 30000000
    space_used = compute_dirsize("/", direct_directory_size, subdirs)

    delete_this_directory = total_space
    for ii in direct_directory_size:
        dirsize = compute_dirsize(ii, direct_directory_size, subdirs)
        if (
            dirsize >= space_required - (total_space - space_used)
            and dirsize <= delete_this_directory
        ):
            delete_this_directory = dirsize
    print("The answer to the first questions is: " + str(delete_this_directory))


if __name__ == "__main__":
    main(sys.argv[1])
