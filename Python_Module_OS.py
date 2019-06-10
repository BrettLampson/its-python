# ------------------------------------------------------------------------------------------------ #
# OS Module
# ------------------------------------------------------------------------------------------------ #

import os
import time
from pprint import pprint


# IMPORTANT NOTES:
# Windows file paths use (\)
# OSX and Linux file paths use (/)
# print(os.path.join('C:\\', 'Users', 'Brett', 'Documents', 'My CLIENTS'))
# C:\Users\Brett\Documents\My CLIENTS


# ------------------------------------------------------------------------------------------------ #
# GET CURRENT WORKING DIRECTORY (CWD)

print(os.getcwd())  # /Brett/Dropbox/Python Subjects


# ------------------------------------------------------------------------------------------------ #
# CHANGE CWD

# root_dir = '/Brett/Dropbox'
# working_dir = '/Python Subjects'
# os.chdir(root_dir + working_dir)
# print(os.getcwd())  # /Brett/Dropbox/Python Subjects


# ------------------------------------------------------------------------------------------------ #
# ASSIGN CWD AND LIST OF ITEMS IN CWD

# cwd = os.getcwd()
# print(os.listdir(cwd))


# ------------------------------------------------------------------------------------------------ #
# VERIFY THAT A FILE OR DIRECTORY EXISTS

# print(os.path.exists('star.txt'))                # True


# ------------------------------------------------------------------------------------------------ #
# VERIFY TYPE IS A FILE OR DIRECTORY

# print(os.path.isfile('star.txt'))                # True
# print(os.path.isfile('Python Subjects Child'))   # False
# print(os.path.isdir('ffxiv macros'))             # True


# ------------------------------------------------------------------------------------------------ #
# RETURN LAST MODIFIED TIME

# print(os.path.getmtime('/Brett/Dropbox/Python Subjects'))  # 1491836922.2779684


# ------------------------------------------------------------------------------------------------ #
# CREATE A NEW DIRECTORY IN THE CWD
# Notes:  If the directory already exists, FileExistsError is raised.

# os.mkdir('/Brett/Dropbox/Python Subjects/FolderName-AP')   # Absolute Path
# os.mkdir('FolderName-RP')  # Relative Path


# ------------------------------------------------------------------------------------------------ #
# CREATE A FOLDER TREE
# NOTE: You must change cwd if you use relative path
# NOTE: Like mkdir(), but makes all intermediate-level directories needed to contain the leaf directory.

# os.makedirs('Parent/Child_1/Child_of_Child_1')                                  # Relative Path
# os.makedirs('/Brett/Dropbox/Python Subjects/Parent2/Child_2/Child_of_Child_2')  # Absolute Path


# ------------------------------------------------------------------------------------------------ #
# RENAME THE FOLDER
# Example: os.rename(old, new)

# os.mkdir('/Brett/Dropbox/Python Subjects/FolderName-AP')
# time.sleep(2)
# os.rename('FolderName-AP', 'I just renamed you')


# ------------------------------------------------------------------------------------------------ #
# RENAME first 6 characters if ALL files in a directory

files = os.listdir()
pprint(files)
old = 'subj'
new = 'Python'
for file in files:
    if file.startswith(old):
        os.rename(file, new + file[len(old):])


# ------------------------------------------------------------------------------------------------ #
# REMOVE A FILE

# Delete the file path
# time.sleep(2)
# os.remove('for_delete.txt')


# ------------------------------------------------------------------------------------------------ #
# REMOVE THE FOLDER

# Remove the folder specified (note: will NOT remove if folder has contents)
# os.rmdir(r'\I just renamed you')


# ------------------------------------------------------------------------------------------------ #
# RELATIVE PATH TO ABSOLUTE PATH

# print(os.path.abspath(r'.\FolderName-RP'))   # .\ required and inserts cwd in front


# ------------------------------------------------------------------------------------------------ #
# DIR NAME AND BASE NAME
# fpath = 'C:\\Users\\Brett\\AppData\\Local\\Programs\\Python\\Python35\\python.exe'
# print(os.path.dirname(fpath))   # C:\Users\Brett\AppData\Local\Programs\Python\Python35
# print(os.path.basename(fpath))  # python.exe
# print(os.path.split(fpath))     # ('C:\\Users\\Brett\\AppData\\Local\\Programs\\Python\\Python35', 'python.exe')


# ------------------------------------------------------------------------------------------------ #
# GET FILE SIZE (in bytes)

# print(os.path.getsize('sunshine.txt'))  # 164 bytes


# ------------------------------------------------------------------------------------------------ #
# SPLIT PATH NAME AND FILE NAME

# print(os.path.split(r'C:\MyScripts\Python Subjects\subj-Import OS.py'))
# ('C:\\MyScripts\\Python Subjects', 'subj-Import OS.py')

