#!/usr/bin/python3

from zipfile import ZipFile
import os
import sys
import getopt

def get_all_file_paths(directory): 
  
    # initializing empty file paths list 
    file_paths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
  
    # returning all file paths 
    return file_paths    

def rename_file(filename, root):
    temp = os.path.splitext(filename)[0].zfill(3) + os.path.splitext(filename)[1]
    temp = os.path.join(root, temp) 
    filepath = os.path.join(root, filename) 
    os.rename(filepath, temp)
    return temp

def rename_files_and_get_path(directory):
    arr = []
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            file = rename_file(filename, root)
            arr.append(file)
    return arr

def zip_file(files, name):
    with ZipFile(name,'w') as zip: 
        # writing each file one by one 
        for file in files: 
            zip.write(file)

def get_filename_and_path(directory):
    if not directory.endswith('/'):
        directory = directory + "/"
    a = directory.split('/')
    temp = a[len(a) - 2].zfill(3) + ".cbr"
    t = os.path.dirname(os.path.dirname(directory)) + "/"
    full_filename = t + temp
    return full_filename

def current_folder(directory):
    files = rename_files_and_get_path(directory)
    if len(files) > 0:
        file = get_filename_and_path(directory)
        zip_file(files, file)
        print("Zipped file " + file)

def subfolders(directory):
    a = directory.split('/')
    if len(a[len(a)- 1]) == 0:
        a = a[len(a)- 2].split('-')
    else:
        a = a[len(a)- 1].split('-')
    i = int(a[0])
    j = int(a[1])
    while (i <= j):
        temp = directory
        if not temp.endswith('/'):
            temp = temp + '/' + str(i) + '/'
        else:
            temp = temp + str(i) + '/'
        current_folder(temp)
        i += 1

opts, args = getopt.getopt(sys.argv[1:], 'm:s:', ['multiple=', 'single='])

def main(argv): 
    # path to folder which needs to be zipped 
    if len(argv) > 2:
        for opt, arg in opts:
            if opt in ('-m', '--multiple'):
                # print(arg)
                subfolders(arg)
                print('Multiple folders zipped successfully!')            
            elif opt in ('-s', '--single'):
                current_folder(arg)
                # print(arg)
                print('Single folder zipped successfully!')
    else:         
        print('no args given')

if __name__ == "__main__": 
    main(sys.argv) 