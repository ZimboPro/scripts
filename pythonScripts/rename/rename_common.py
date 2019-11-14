#!/usr/bin/python3
import os
import sys

def get_files_in_dir(dir: str):
    return os.listdir(dir)

def get_folders_in_dir(dir: str):
    root, dirs, files = os.walk(dir)
    folders = []
    for folder in dirs:
        folders.append(os.path.join(root, folder))
    return folders

def rename_files_in_dir(remove_str: str, replace_str: str, dir: str):
    files = get_files_in_dir(dir)
    for f in files:
        if remove_str in f:
            newName = f.replace(remove_str, replace_str, 1)
            f = os.path.join(dir, f)
            newName = os.path.join(dir, newName)
            os.rename(f, newName)

def recursive_search_and_replace_str(remove_str: str, replace_str: str, dir: str):
    rename_files_in_dir(remove_str, replace_str, dir)
    files = get_folders_in_dir(dir)
    for file in files:
            newdir = os.path.join(dir, file)
            if os.path.isdir(newdir):
                recursive_search_and_replace_str(remove_str, replace_str, newdir)
