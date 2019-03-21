#!/usr/bin/python3
import os
import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], 'd:r:', ['delete=', 'replace='])
except getopt.GetoptError:
    usage()
    sys.exit(2)

removeStr = ""
replaceStr = ""
flags = 0

def usage():
    print("python3 rename_files.py -d \"string\" // python3 rename_files.py --delete \"string\"")
    print("OR")
    print("python3 rename_files.py -r \"string\" // python3 rename_files.py --replace \"string\"")
    print("NOTE: The --replace/-r flag needs to be used in junction with the --delete/-d flag")

def setReplace(arg):
    global replaceStr
    global flags
    flags = flags + 2
    replaceStr = arg

def setRemove(arg):
    global removeStr
    global flags
    flags = flags + 1
    removeStr = arg

def getFiles():
    return os.listdir(os.curdir)

def removeString():
    global removeStr
    files = getFiles()
    for f in files:
        if removeStr in f:
            newName = f.replace(removeStr, "", 1)
            os.rename(f, newName)

def replaceString():
    global replaceStr
    global removeStr
    files = getFiles()
    for f in files:
        if removeStr in f:
            newName = f.replace(removeStr, replaceStr, 1)
            os.rename(f, newName)

def executeFlags():
    if flags == 1:
        removeString()
    elif flags == 3:
        replaceString()
    elif flags == 2:
        print("The --replace/-r flag needs to be used in junction with the --delete/-d flag")
    else:
        print("Invalid flags")
        usage()
    

def main(argv):
    if len(argv) > 2:
        for opt, arg in opts:
            if opt in ('-d', '--delete'):
                setRemove(arg)         
            elif opt in ('-r', '--replace'):
                setReplace(arg)
        executeFlags()
    else:         
        usage()

if __name__ == "__main__": 
    main(sys.argv) 