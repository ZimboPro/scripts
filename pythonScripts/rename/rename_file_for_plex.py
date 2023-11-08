#!/usr/bin/python3
import typing
import os
import sys
import getopt
import re

import rename_common

try:
    opts, args = getopt.getopt(sys.argv[1:], "cf:d", ["current", "folder=", "dryrun"])
except getopt.GetoptError:
    usage()
    sys.exit(2)


def usage():
    print(
        "-c (--current) to start running in current dir and use parent folder as series name"
    )
    print(
        "-f folder (--folder) to start running in folder argument and use passed in folder as series name"
    )


def check_if_exists_and_combine(folder: str):
    path = os.path.join(os.curdir, folder)
    if os.path.isdir(path):
        return path
    else:
        raise Exception("Folder '" + folder + "' does not exist")


def get_episode_number(path):
    return re.search(r"""(?ix)(?:e|x|episode|^)\s*(\d{1,3})""", path)


def get_season_number(path):
    return re.search(r"""(?ix)(?:s|season|^)\s*(\d{1,3})""", path)


def print_and_get_input(message):
    print(message)
    input_val = input()
    return input_val


def get_lowest_number(files: list):
    lowest = 100000
    for file in files:
        file = str(file)
        n = get_episode_number(file)
        if n < lowest:
            lowest = n


def rename_recursive(path):
    files = rename_common.get_files_in_dir(path)


def main():
    try:
        if len(opts) > 0:
            for opt, arg in opts:
                if opt in ("-c", "--current"):
                    setRemove(arg)
                elif opt in ("-f", "--folder"):
                    path = check_if_exists_and_combine(arg)
        else:
            usage()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
