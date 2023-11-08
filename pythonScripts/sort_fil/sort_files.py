#!/usr/bin/python3

import os
import sys
import getopt
from difflib import SequenceMatcher

def usage():
    print('python3 creator.py -t folder // python3 creator --type folder')
    print('OR')
    print('python3 creator.py -n folder // python3 creator --name folder')

try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:t:', ['name=', 'type='])
except getopt.GetoptError:
    usage()
    sys.exit(2)

def sort_by_name(arg):
    print(arg)
    for root, directories, files in os.walk(arg):
        # print(directories)
        if (root == arg):
            for filename in files:
                print(filename)



def sort_by_file_type(arg):
    print(arg)
    sorted_files = []
    file_types = []
    for root, directories, files in os.walk(arg):
        if (root == arg):
            for filename in files:
                temp = os.path.splitext(filename)[1].lower()
                if temp not in file_types:
                    file_types.append(temp)
                    sorted_files.append([])

def main(argv):
    if len(argv) > 2:
        for opt, arg in opts:
            if opt in ('-n', '--name'):
                # print(arg)
                sort_by_name(arg)
                print('Multiple folders zipped successfully!')
            elif opt in ('-t', '--type'):
                sort_by_file_type(arg)
                # print(arg)
                print('Single folder zipped successfully!')
    else:
        print('no args given')

if __name__ == "__main__":
    main(sys.argv)
