#! python3
# /usr/bin/env


# ------------------------------------------------------------------------------------------------ #
# ARGV

# ------------------------------------------------------------------------------------------------ #
# WHEN TO USE A ---------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------ #
# 1)
# 2)
# 3)

# IMPORTANT NOTES:
# The argv is the argument variable, (a standard name in programming) that holds the arguments
# you pass in to your Python script when you run it.


# ------------------------------------------------------------------------------------------------ #
# RUN this on the command line:
# Brett$ cd 'Dropbox/Python Subjects'
# Boss:Python Subjects Brett$ python3.7 Python_Argv.py Love Friendships Purpose

# from sys import argv
# script, first, second, third = argv
#
# print('Script Name = ', script)
# print('Most Important = ', first)
# print('Then Comes = ', second)
# print('Last But Not Least = ', third)


# ------------------------------------------------------------------------------------------------ #
# RUNNING A SCRIPT FROM COMMAND LINE (win + r)
#! python3
# change directory to where the script is located
# type this with 2 arguments as follows (no commas):
# pchange.py 49.95 53.95

# (The code for pchange.py)
#! python3

# import sys
#
# def pchange(old, new):
#     """
#     Finds the percentage change from old number to new number.
#     Written in the command line as follows:
#     pchange.py 22.95 29.95
#     """
#     old_num = float(old)
#     new_num = float(new)
#     formula = float(((new_num - old_num) / old_num) * 100)
#     print('The percentage change from', old, 'to', new, 'is {0:.2f}%'.format(formula))
#
# if __name__ == '__main__':
#     pchange(float(sys.argv[1]), (sys.argv[2]))
#
# print(input('Press [Enter] to exit'))
# sys.exit()


# ------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------ #
# UNDER CONSTRUCTION ----------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------ #


