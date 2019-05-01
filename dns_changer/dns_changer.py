#!/usr/bin/python3
import os
import sys 
import time
import subprocess

file = "/etc/resolv.conf"

def runCommands():
    subprocess.run("sudo echo nameserver 208.67.222.123 > /etc/resolv.conf", shell=True)
    subprocess.run("sudo echo nameserver 208.67.220.123 >> /etc/resolv.conf", shell=True)
    subprocess.run("sudo /etc/init.d/networking stop", shell=True)
    subprocess.run("sudo /etc/init.d/networking start", shell=True)

def checkAndChangedFile():
    global file
    file_obj = open(file,"r+")
    text = file_obj.readlines()
    update = 0
    dns1 = False
    dns2 = False
    newLines = ["nameserver 208.67.222.123\n", "nameserver 208.67.220.123"]
    for line in text:
        if "nameserver" in line:
            update = update + 1
        if "208.67.222.123" in line:
            dns1 = True
        if "208.67.220.123" in line:
            dns2 = True
    file_obj.close()
    if update > 2:
        runCommands()
    if update == 2 & (dns1 == False | dns2 == False):
        runCommands()

def main():
    global file
    file_t1 = 0
    try:
        checkAndChangedFile()
        file_t1 = os.stat(file).st_mtime
    except :
        print('Unhandled error: %s' % sys.exc_info()[0])

    while True:
        time.sleep(2);
        try:
            file_t2 = os.stat(file).st_mtime
            if file_t1 != file_t2:
                file_t1 = file_t2 
                checkAndChangedFile()
        except :
            print('Unhandled error: %s' % sys.exc_info()[0])
            pass

if __name__ == "__main__": 
    main() 