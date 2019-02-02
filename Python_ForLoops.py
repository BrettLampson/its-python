print()
# ------------------------------------------------------------------------------------------------ #
# FOR LOOPS


# ------------------------------------------------------------------------------------------------ #
# PRINT ALL METHODS IN A MODULE (except anything starting with '__')
# for i in dir(list):
#     if not i.startswith('__'):
#         print(i)


# ------------------------------------------------------------------------------------------------ #
# PRINTS sequence item IF GREATER IN LENGTH THAN char_limit
# char_limit = 6
# x = ['imago', 'nic', 'xyntolinx', 'starabella']
# for item in x:
#     if len(item) > char_limit:
#         print(item)


# ------------------------------------------------------------------------------------------------ #
# RETURN the LENGTH of each sequence item in list
# x = ['imago', 'nic', 'xyntolinx', 'starabella']
# for item in x:
#     print(item, '=', len(item), 'characters long')


# ------------------------------------------------------------------------------------------------ #
# Returns all numbers in range divisible by 7
# for n in range(1, 50):
#     if n % 7 == 0:
#         print(n)

# LIST COMPREHENSION Returns all numbers in range divisible by 7
# x = [n for n in range(1, 51) if n % 7 == 0]
# print(x)

# [7, 14, 21, 28, 35, 42, 49]


# ------------------------------------------------------------------------------------------------ #
# LIST COMPREHENSION
# Returns all numbers from 0-50, counting by 7s, starting with greater than 10
# b = [n for n in range(0, 51, 7) if n >= 10]
# print(b)
# # [14, 21, 28, 35, 42, 49]


# ------------------------------------------------------------------------------------------------ #
# LIST COMPREHENSION
# Returns the number squared in range 100 that also is perfectly divisible by 30.
# comp_list = [x*x for x in range(100) if x % 30 == 0]
# print(comp_list)
# [0, 900, 3600, 8100] which are numbers 30, 60, 90


# ------------------------------------------------------------------------------------------------ #
# LIST COMPREHENSION
# Returns all perfect squares in range of 101
# perfectSquares = [x*x for x in range(1, 60) if x*x < 101]
# print(perfectSquares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# ------------------------------------------------------------------------------------------------ #
# FOR LOOP
# Builds a new list from names that start with a vowel
# names = ['Bob', 'Ellen', 'Rick',
#          'Abigale', 'Rick', 'Elsa',
#          'Greg', 'Isla', 'Allen']
# NamesStartingVowel = []
# for name in names:
#     if name[0] in 'AEIOU':
#         NamesStartingVowel.append(name)
# print(NamesStartingVowel)
# ['Ellen', 'Abigale', 'Elsa', 'Isla', 'Allen']


# ------------------------------------------------------------------------------------------------ #
# FOR LOOP
# Comprehension that removes vowels from a string
# fav_player = 'Kirby Puckett'
# remove_vowels = [item for item in fav_player if item.lower() not in 'aeiou']
# print(remove_vowels)
# #['K', 'r', 'b', 'y', ' ', 'p', 'c', 'k', 't', 't']


# ------------------------------------------------------------------------------------------------ #
# FOR LOOP
# Comprehension sample
# alist = [c.upper() for c in 'pizza']
# print(alist)
# # ['P', 'I', 'Z', 'Z', 'A']


# ------------------------------------------------------------------------------------------------ #
# ITERATE "LISTS" WITH ZIP()
# Iterate over several sequences with ZIP() when order matters
# days = ['MON', 'TUE', 'WED', 'THU', 'FRI']
# tasks = ['strings', 'lists', 'dictionaries', 'sets', 'loops']
# lunches = ['jersey mikes', 'pizza', 'qfc', 'bbq', 'spicy chicken']
# clock_out = ['6:01', '6:02', '5:01', '6:03', '5:02']
#
# for day, task, lunch, clock in zip(days, tasks, lunches, clock_out):
#     print(day, ': task =', task, '| lunch =', lunch, '| clock out', clock)


# ------------------------------------------------------------------------------------------------ #
# ITERATE "SETS" WITH ZIP()
# Iterate over several sequences with ZIP() when order does NOT matter
# days = ['MON', 'TUE', 'WED', 'THU', 'FRI']
# music_genres = {'hiphop', 'classical', 'edm', 'dubstep', 'pop'}
# dutys = {'raiding alexander', 'moogle quests', 'zurvanEx', 'expert roulette', 'crafting'}
#
# for day, music_genre, duty in zip(days, music_genres, dutys):
#     print(day, ': listen to', music_genre, '>>> work on', duty)


# ------------------------------------------------------------------------------------------------ #
# BREAK AND CONTINUE

# If break is executed, it immediately terminates the for loop, not even the post-code is executed.
# If continue is executed in a for loop, it caused the remainder of the body to be skipped, and
# the loop proceeds as normal with the next item in the sequence.


# ------------------------------------------------------------------------------------------------ #
# FOR/ELSE LOOP with a break statement

# Have an optional else clause which most of us are unfamiliar with.
# The else clause executes when the loop completes normally.  This means
# the loops didn't encounter any break.

# container = [1, 3, 55, 21, 98, 75, 32]
#
# for item in container:
#     if item == 33:
#         # Found it!
#         print(item, 'was found')
#         break
# else:
#     # Didn't find anything..
#     print("Didn't find anything...")


# ---------------------------------------------------------------------------------------------- #
# NESTED FOR LOOP checking for matching items between 2 lists
# look_in = 'love hate black white'.split()
# look_for = 'red white blue'.split()
# for key in look_for:
#     for item in look_in:
#         if item == key:
#             print('found', key)
#             break
#     else:
#         print('nothing...', key)
# print('\nprocess complete.')


# for item in look_for:
#     if item in look_in:
#         print(item, 'is a match!')



# ------------------------------------------------------------------------------------------------ #
# NESTED FOR LOOP
# one = ['1a', '1b', '1c']     # Tier 1
# two = ['2a', '2b', '2c']     # Tier 2

# for a in one:
#     print(a)                 # Tier 1
#     for b in two:
#         print(b)             # Tier 2

# 1a
# 2a
# 2b
# 2c
# 1b
# 2a
# 2b
# 2c
# 1c
# 2a
# 2b
# 2c


# ------------------------------------------------------------------------------------------------ #
# NESTED FOR LOOP
# one = ['1a', '1b', '1c']     # Tier 1
# two = ['2a', '2b', '2c']     # Tier 2

# for a in one:
#     for b in two:
#         print(a)  # Tier 1
#         print(b)  # Tier 2

# 1a
# 2a
# 1a
# 2b
# 1a
# 2c
# 1b
# 2a
# 1b
# 2b
# 1b
# 2c
# 1c
# 2a
# 1c
# 2b
# 1c
# 2c


# ------------------------------------------------------------------------------------------------ #
# NESTED FOR LOOP
# t = 'Imago Dei', 'Gray Embers', 'Kite Waffle'
# l = ['Deltascape: 1.0', 'Deltascape: 2.0', 'Deltascape: 3.0', 'Deltascape: 4.0']
# for ele in t:
#     print(ele.upper())
#     for ele in l:
#         print(ele.rjust(18, ' '))


# ------------------------------------------------------------------------------------------------ #
# NESTED FOR LOOP
# for x in range(2):   # This loop is essentially saying do the bottom loop twice
#     for x in range(1, 10):
#         print(x, end=', ')
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9,


# ------------------------------------------------------------------------------------------------ #
# NESTED FOR LOOP
# NESTED for loop
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         print(n, 'is a prime number')


# ------------------------------------------------------------------------------------------------ #
# NESTED FOR LOOP
# fruits = ['apple', 'pear', 'banana']
# for fruit in fruits:
#     for letter in fruit:
#         print(letter, end='.')
#     print()
# ...
# a.p.p.l.e.
# p.e.a.r.
# b.a.n.a.n.a.


# ------------------------------------------------------------------------------------------------ #
# FOR LOOP
# divisor = 1
# for item in range(1, 25, 3):
#     divisor += 1
#     ans_div = item / divisor
#     ans_fdiv = item // divisor
#     ans_modulo = item % divisor
#     print(item, 'divided by', divisor, '=', ans_div)
#     print(item, 'divided by', divisor, '(floor) =', ans_fdiv)
#     print(item, ' % ', divisor, '=', ans_modulo)
# ...
# 1 divided by 2 = 0.5
# 1 divided by 2 (floor) = 0
# 1  %  2 = 1
# 4 divided by 3 = 1.3333333333333333
# 4 divided by 3 (floor) = 1
# 4  %  3 = 1
# 7 divided by 4 = 1.75
# 7 divided by 4 (floor) = 1
# 7  %  4 = 3
# 10 divided by 5 = 2.0
# 10 divided by 5 (floor) = 2
# 10  %  5 = 0
# 13 divided by 6 = 2.1666666666666665
# 13 divided by 6 (floor) = 2
# 13  %  6 = 1
# 16 divided by 7 = 2.2857142857142856
# 16 divided by 7 (floor) = 2
# 16  %  7 = 2
# 19 divided by 8 = 2.375
# 19 divided by 8 (floor) = 2
# 19  %  8 = 3
# 22 divided by 9 = 2.4444444444444446
# 22 divided by 9 (floor) = 2
# 22  %  9 = 4


# import os
# cur_dir = '/Users/brettlampson/Documents/Pictures/BULLBOXER PHOTOS'
# def print_directory_contents(sPath):
#     """
#     This function takes the name of a directory
#     and prints out the paths files within that
#     directory as well as any files contained in
#     contained directories.
#
#     This function is similar to os.walk. Please don't
#     use os.walk in your answer. We are interested in your
#     ability to work with nested structures.
#     """
#     os.chdir(sPath)
#     dir1 = os.listdir(sPath)
#     for i in dir1:
#         print(i)
#         if os.path.isdir(cur_dir + '/' + i):
#             print(i, 'is a folder containing....')
#             os.chdir(cur_dir + '/' + i)
#             for i in os.listdir(os.getcwd()):
#                 print(i)
# print_directory_contents(cur_dir)  # FUNCTION CALL