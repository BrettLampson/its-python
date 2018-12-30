# ------------------------------------------------------------------------------------------------ #
# COMMAND LINE MAC
# ------------------------------------------------------------------------------------------------ #

# which python3 - shows where python3 is located on this machine
# type python3 - shows where python3 is located (works if using aliases)
# exit() - closes python in the terminal and starts command line
# clear - clears all typing, starting with clean terminal
# echo $PATH - shows the system looks for programs


# ------------------------------------------------------------------------------------------------ #
# VIEW PATH SYSTEM VARIABLE
# echo %PATH


# ------------------------------------------------------------------------------------------------ #
# PATHS PYTHON LOOKS IN FOR FILES AND PACKAGES

# /usr/local/bin:
# /usr/bin:
# /bin:
# /usr/sbin:
# /sbin


# ------------------------------------------------------------------------------------------------ #
# USING MULTIPLE VERSIONS OF PYTHON INSTALLED MAC OSX
# -m means

# python2.7 -m pip install SomePackage        #specifically Python 2.7
# python3   -m pip install SomePackage        #default Python 3
# python3.6 -m pip install SomePackage        #specifically Python 3.6

# python -m pip install SomePackage==1.0.4    # specific version
# python -m pip install 'SomePackage>=1.0.4'  # minimum version


# ------------------------------------------------------------------------------------------------ #
# LIST OF INSTALLED PACKAGES
# pip list


# ------------------------------------------------------------------------------------------------ #
# RETURN PACKAGE VERSION
# py -3 -m django --version


# ------------------------------------------------------------------------------------------------ #
# UPGRADING PACKAGES
# python -m pip install --upgrade SomePackage
# python3.7 -m pip install --upgrade SomePackage


# ------------------------------------------------------------------------------------------------ #
# RUNNING A SCRIPT FROM COMMAND LINE (win + r)
#! python3
# change directory to where the script is located
# type this with 2 arguments as follows (no commas):
# python3.7 percent_of.py 49.95 53.95

# (The code for percent_of.py)
#! python3

# import sys
#
#
# def percent_of(percent, number):
#     """Returns the percentage of a number provided
#     example:
#     python3 percent_of.py 50 60
#     returns 50% of 60 is 30
#     """
#     percent = float(percent)
#     number = float(number)
#     x = float(number / (100 / percent))
#     print('{1:.2f}% of ${2:.2f} is ${0:.2f}'.format(x, percent, number))
#
#
# if __name__ == '__main__':
#     percent_of(float(sys.argv[1]), (sys.argv[2]))


# ------------------------------------------------------------------------------------------------ #
# INSTALLING USING .WHL (WHEEL)
# Wheel files have all dependencies in the file.  More thorough installation method.

# python -m pip install C:\wheel_file_location
# python3.7 -m pip install C:\wheel_file_location


# ------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------ #
# TERMINAL COMMAND LIST (MAC)
# ------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------ #
#
# |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
# DIRECTORY RELATED COMMANDS
# |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
#
# -----------------------------------------------------------
# pwd
# CURRENT WORKING DIRECTORY
#
#
# -----------------------------------------------------------
# cd [directory]
# CHANGE DIRECTORY TO [directory]
#
#
# -----------------------------------------------------------
# cd
# GO BACK TO ROOT DIRECTORY
#
#
# -----------------------------------------------------------
# cd -
# GO BACK 1 LEVEL AND RETURNS THE PATH
#
#
# -----------------------------------------------------------
# cd ..
# GO BACK 1 LEVEL
#
#
# -----------------------------------------------------------
# cd ../../
# GO BACK 2 LEVELS
#
#
# -----------------------------------------------------------
# ls -d i*
# SHOWS ALL DIRECTORIES STARTING WITH ’i’ (case sensitive)
#
#
# -----------------------------------------------------------
# ls
# LIST DIRECTORY CONTENTS
#
#
# -----------------------------------------------------------
# ls -a
# LISTING INCLUDING HIDDEN FILES
#
#
# -----------------------------------------------------------
# ls -l
# LONG LISTING
#
#
# -----------------------------------------------------------
# ls -la
# LONG LISTING AND HIDDEN FILES
#
#
# -----------------------------------------------------------
# ls -lh
# LONG LISTING WITH HUMAN READABLE FILE SIZES
#
#
# -----------------------------------------------------------
# ls -R
# ENTIRE CONTENTS OF DIR RECURSIVELY (DIR AND DIR CONTENTS)
#
#
# -----------------------------------------------------------
# mkdir
# CREATE NEW DIRECTORY
#
#
# -----------------------------------------------------------
# mkdir [name] && cd [name]
# MAKE DIR AND MOVE INTO IT
#
#
# -----------------------------------------------------------
# mkdir -p [dir]/[dir]
# CREATE NEW DIRECTORY
#
#
# -----------------------------------------------------------
# rm -R [dir]
# REMOVE A DIRECTORY (ONLY EMPTY)
#
#
# -----------------------------------------------------------
# rmdir [dir]
# REMOVE A DIRECTORY AND ITS CONTENTS
#
#
# -----------------------------------------------------------
# rm -r --[dir or file]
# REMOVE A DIRECTORY or FILE AND ITS CONTENTS
#
#
# -----------------------------------------------------------
# rm -rf --[dir or file]
# REMOVE A DIRECTORY or FILE AND CONTENTS (caution can't undo)
#
#
# |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
# BASIC UTILITIES
# |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
# -----------------------------------------------------------
# man &UTIL
# MANUAL GETS INFO FOR HOW TO USE ANY UTILITY
#
#
# -----------------------------------------------------------
# less [file name]
# MANUAL GETS INFO FOR HOW TO USE ANY UTILITY
#
#
# -----------------------------------------------------------
# history n
# SHOWS STUFF TYPED LIMITED TO LAST n ITEMS
#
#
# -----------------------------------------------------------
# touch [file name]
# CREATE A NEW FILE
#
#
# -----------------------------------------------------------
# cat
# CONCATENATE TO SCREEN
#
#
# -----------------------------------------------------------
# rm -r [file name]
# REMOVE FILE
#
#
# -----------------------------------------------------------
# rm -rf [file name]
# FORCEFULLY REMOVE *CAUTION*
#
#
# -----------------------------------------------------------
# mv [file name] [dir name]
# MOVES A FILE INTO A DIR
#
#
# -----------------------------------------------------------
# mv [file name] [new file name]
# RENAME A FILE
#
#
# -----------------------------------------------------------
# pbcopy < [file name]
# COPIES FILE CONTENTS TO CLIPBOARD
#
#
# -----------------------------------------------------------
# clear
# CLEARS THE SCREEN KEEPING HISTORY ABOVE
#
#
# -----------------------------------------------------------
# command + k
# CLEARS THE SCREEN DELETES HISTORY ABOVE
#
#
# -----------------------------------------------------------
# ctrl + c
# KILLS WHATEVER YOU’RE RUNNING
#
#
# -----------------------------------------------------------
# cp [source] [destination]
# COPY FILE FROM SOURCE TO DESTINATION
#
#
# -----------------------------------------------------------
# open [file name]
# OPENS A FILE
#
#
# -----------------------------------------------------------
# top
# DISPLAYS ACTIVE PROCESSES (q to quit)
#
#
# -----------------------------------------------------------
# vim [file name]
# OPENS THE FIE USING VIM EDITOR
#
#
# -----------------------------------------------------------
# find [dir] -name [search_pattern]
# SEARCH FOR FILES. find /Users -name “file.txt.”
#
#
# -----------------------------------------------------------
# grep [search_pattern] [file name]
# SEARCH ALL LINES FOR SEARCH PATTERN.  grep “Brett” file.txt
#
#
# -----------------------------------------------------------
# grep -r [search_pattern] [dir]
# RECURSIVE SEARCH ALL FILES IN A DIR FOR SEARCH PATTERN
#
#
# -----------------------------------------------------------
# grep -v [search_pattern] [file]
# SEARCH ALL LINES THAT DO NOT CONTAIN SEARCH PATTERN
#
#
# -----------------------------------------------------------
# mdfind [search_pattern]
# SPOTLIGHT SEARCH FOR FILES(NAMES, CONTENT, METADATA, ETC)
#
#
# -----------------------------------------------------------
# mdfind -onlyin [dir] -name [pattern]
# SPOTLIGHT SEARCH FOR FILES NAMED LIKE PATTERN IN A DIR

