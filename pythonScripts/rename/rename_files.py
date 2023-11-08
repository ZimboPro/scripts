#!/usr/bin/python3
import os
import sys
import getopt

try:
    opts, args = getopt.getopt(
        sys.argv[1:], "d:r:R", ["delete=", "replace=", "recursive"]
    )
except getopt.GetoptError:
    usage()
    sys.exit(2)

removeStr = ""
replaceStr = ""
flags = 0
recursive = False


def usage():
    print(
        'python3 rename_files.py -d "string" // python3 rename_files.py --delete "string"'
    )
    print("OR")
    print(
        'python3 rename_files.py -r "string" // python3 rename_files.py --replace "string"'
    )
    print(
        "NOTE: The --replace/-r flag needs to be used in junction with the --delete/-d flag"
    )


def setReplace(arg):
    global replaceStr
    global flags
    flags = flags + 2
    replaceStr = arg


def getDirs(path):
    root, dirs, files = os.walk(path)
    folders = []
    for folder in dirs:
        folders.append(os.path.join(root, folder))
    return folders


def setRemove(arg):
    global removeStr
    global flags
    global recursive
    flags = flags + 1
    removeStr = arg


def getFiles(path):
    return os.listdir(path)


def removeStringDir(path):
    global removeStr
    global replaceStr
    files = getFiles(path)
    for f in files:
        if removeStr in f:
            newName = f.replace(removeStr, replaceStr, 1)
            f = os.path.join(path, f)
            newName = os.path.join(path, newName)
            os.rename(f, newName)


def removeString(path):
    global removeStr
    global recursive
    if recursive:
        removeStringDir(path)
        files = getFiles(path)
        for file in files:
            newPath = os.path.join(path, file)
            if os.path.isdir(newPath):
                removeString(newPath)
    else:
        removeStringDir(path)


def executeFlags():
    if flags == 1:
        removeString(os.curdir)
    elif flags == 3:
        removeString(os.curdir)
    elif flags == 2:
        print(
            "The --replace/-r flag needs to be used in junction with the --delete/-d flag"
        )
    else:
        print("Invalid flags")
        usage()


def main(argv):
    if len(argv) > 2:
        for opt, arg in opts:
            if opt in ("-d", "--delete"):
                setRemove(arg)
            elif opt in ("-r", "--replace"):
                setReplace(arg)
            elif opt in ("-R", "--recursive"):
                global recursive
                recursive = True
        executeFlags()
    else:
        usage()


if __name__ == "__main__":
    main(sys.argv)
