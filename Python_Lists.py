

# ---------------------------------------------------------------------------------------------- #
# LISTS
# ---------------------------------------------------------------------------------------------- #
# Mutable, Ordered, Iterable

# WHEN TO USE A LIST:
# 1) To track by sorted order (sortable)
# 2) To modify a sequence (add, remove, modify)
# 3) To count repetitions (dict also good)

# IMPORTANT NOTES:
# Best performance: items are added / removed using append() / pop()
# Worst performance: Using remove(), Searching index() or using in for membership testing
# Lists provide fast searching if sort() was used then using a binary search (bisect module) to find items


# ---------------------------------------------------------------------------------------------- #
# LIST METHODS
# ---------------------------------------------------------------------------------------------- #
# L = [2, 4, 6]
# ---------------------------------------------------------------------------------------------- #

# L.append('omg')             #  Adds 'omg' to end of list L
# [2, 4, 6, 'omg']


# L.clear()                   # Clears all items from list L
# []


# L = [2, 4, 6]
# Z = L.copy()                # Copies a list, so Z == L is True
# Z = [2, 4, 6]


# L.count(4)                  # Returns the number of times 4 appears in L
# 1


# L.extend([8, 10])           # Extends L to include new list items [8, 10]
# [2, 4, 6, 8, 10]
# L += [12, 14]               # OR the L += equivalent
# [2, 4, 6, 8, 10, 12, 14]


# L.index(x, start, end)      # Returns the index value of 1st occurrence of x
# L.index(6)
#  2
# L.index(2, 1, 3)            # Look for 2, include index 1 up to but not including index 3
# ValueError: 2 is not in list


# L.insert(i, x)              # Inserts x at index i, so that L[i] == x
# L.insert(0, 99)             # At index 0, i'm inserting 99
# [99, 2, 4, 6]


# L.pop()                     # REMOVES and RETURNS the last item in L
# 6
# L.pop(0)                    # REMOVES and RETURNS whatever's at index 0
# 2


# L.remove(x)                 # Removes the leftmost occurrence of x in L
# L.remove(4)                 # if no 4 exists, raises a ValueError
# [2, 6]


# L.reverse()                 # Reverses the order of the elements in L
# [6, 4, 2]
# L[::-1]                     # Equivalent to L.reverse()
# [6, 4, 2]


# L.sort()
# L = ['Brad', '_under', 'brad', 'Art', '341']
# L.sort(key=str.lower, reverse=False)
# ['341', '_under', 'Art', 'brad', 'Brad']

# Notice key=str.lower
# sort() replaces object "in place" and does not create a new object.
# sorted() doesn't replace object "in place", creates a new object.

# L = [55, 11, 44, 00, 22, 33]
# L.sort(reverse=True)
# [55, 44, 33, 22, 11, 0]


# ---------------------------------------------------------------------------------------------- #
# LIST METHODS END
# ---------------------------------------------------------------------------------------------- #

# sorted()
# L = ['two', 'Two', 2.0, -1, '_Two', '0003', '0002', '002']

# First convert all items to strings in order to sort
# L = [str(i) for i in L]
# print(L)
# L = ['two', 'Two', '2.0', '-1', '_Two', '0003', '0002', '002']

# or Don't convert them to strings, but sort AS IF they were all strings
# L = sorted(L, key=str)
# print(L)
# [-1, '0002', '0003', '002', 2.0, 'Two', '_Two', 'two']

# Second, specify sort key.  This example is all lower case and remove leading 0's.
# L = sorted(L, key=lambda x: str(x).strip('0*').lower())
# print(L)
# ['-1', '0002', '002', '2.0', '0003', '_Two', 'Two', 'two']

# ---------------------------------------------------------------------------------------------- #
# SORT BY THE SECOND DIGIT OF EACH STRING in a list
# custom = ['a4', 'd1', 'b3', 'c2']
# solution = sorted(custom, key=lambda s: s[1])
# ['d1', 'c2', 'b3', 'a4']

# ---------------------------------------------------------------------------------------------- #
# SORT NESTED SEQUENCES
# student_tuples = [
#         ('john', 'A', 15),
#         ('jane', 'B', 12),
#         ('dave', 'B', 10),
# ]

# from operator import itemgetter, attrgetter, methodcaller

# print(sorted(student_tuples, key=itemgetter(2)))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# ---------------------------------------------------------------------------------------------- #
# CREATE A LIST
# empty = []
# from_list_comp_evens = [i for i in range(11) if i % 2 == 0]
# from_nested_tuple = list(('lol', -17, ('albert', 33), 33.4))
# from_range = list(range(1, 6))
# from_dict = list(dict(Brad=38, Shane=32))
# from_split = 'one two three four five'.split()

# can_be_mixed_data_types = [89.5, [], {}, 3*3, ('He', 'Man'), 'amazon.com']
# can_be_nested = ['Brad', 38, [1978, 'male', 'white']]

# ---------------------------------------------------------------------------------------------- #
# CREATE A LIST from(input) until "stop" is typed
# data_list = []
# while True:
#     num = input("Enter some data or type 'stop' to quit: ")
#     if num == 'stop':
#         break
#     elif num == '\"stop\"':
#         break
#     elif num == "\'stop\'":
#         break
#     data_list.append(num)
#     print('Your current list: ', data_list)
# print("\nOk I've stopped the program.")
# print('Here are all of your list elements:')
# print(data_list)
# for item in data_list:
#     print(type(item))

# ADD
# L = [2, 4, 6]
# L.append('omg')
# L += ['added']
# L.extend([8, 10])
# L.insert(0, 99)
# L.insert(16, 99)
#
# REMOVE
# L = [2, 4, 6, 'omg', 'added']
# L.remove('omg')
# L.pop()
# L.pop(0)
#
# MODIFY
# L = [2, 4, 6, 'added']
# L[3]='modified'
#
# GET VALUE
# L = [3, 4, [55, 66], 7]
# L[1]  # 4
# L[2][1]  # 66

# ---------------------------------------------------------------------------------------------- #
# ADDING TO A LIST
# L = [1, 2] + [3, 4]  # becomes [1, 2, 3, 4]
# L.append(5)          # becomes [1, 2, 3, 4, 5]
# L.extend([6, 7])     # becomes [1, 2, 3, 4, 5, 6, 7]
# L.insert(0, 99)      # becomes [99, 1, 2, 3, 4, 5, 6, 7]
# L += ['added']       # becomes [99, 1, 2, 3, 4, 5, 6, 7, 'added']


# ---------------------------------------------------------------------------------------------- #
# CREATE A LIST from user input with a max of 3 items, then print the list
# user_list = []
# max_length = 3
# while len(user_list) < max_length:
#     item = str(input('Enter some data: '))
#     user_list.append(item)
# print('Here\'s your 3 item list: ', user_list)


# ---------------------------------------------------------------------------------------------- #
# CREATE A LIST FROM A LIST COMPREHENSION that multiplies each number in range by 10
# [x*10 for x in range(11)]
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# ---------------------------------------------------------------------------------------------- #
# GET VALUES by index / slice / stride
# L[include : up to and excluding]
# L = [2, 4, 6, 8, 10]
# print(L[3])         # 8
# print(L[1:3])       # [4, 6] returns items in index 1 to 3, INCLUDING 3
# print(L[:])         # [2, 4, 6, 8, 10]
# print(L[::2])       # [2, 6, 10] returns items skipping (stepping) by 2
# print(L[::3])       # [2, 8] returns items skipping (stepping) by 3
# print(L[::-1])      # [10, 8, 6, 4, 2] returns items backwards

# ---------------------------------------------------------------------------------------------- #
# GET INDEX of specified value
# a_list = [4, 'lol', 'Richard', 23.55, 'three']
# print(a_list.index('three'))  # 4
# ValueError:  if item is NOT in the list


# ---------------------------------------------------------------------------------------------- #
# CHANGE VALUE
# a_list = [2, 4, 6, 8, 10]
# a_list[2] = 66   # Change whatever index 2 is to 66
# print(a_list)    # [2, 4, 66, 8, 10]


# ---------------------------------------------------------------------------------------------- #
# DELETE a value at index provided
# L = [2, 4, 6, 8, 10]
# del L[2]  # Delete value at index 2
# print(L)  # [2, 4, 8, 10]
# del L[2:]
# print(L)  # [2, 4]
# del L[8]  # IndexError: list assignment out of range


# ---------------------------------------------------------------------------------------------- #
# REMOVE a specific value
# Use remove() when you don't know the index
# L = [2, 4, 6, 8, 10, 4, 6, 4]
# L.remove(4)   # Removes the first occurrence of 4 in L
# print(L)      # [2, 6, 8, 10, 4, 6, 4]
# L.remove(12)  # ValueError: list.remove(x): x not in list


# ---------------------------------------------------------------------------------------------- #
# REMOVING values using pop()
# # Use pop() when you want use the removed value in some way
# L = [2, 4, 6, 8, 10]
# La = ['lol', 'omg']
# La.append(L.pop(1))  # The 1 argument pops the item from index 1.
# print(La)            # ['lol', 'omg', 4]


# ---------------------------------------------------------------------------------------------- #
# CONCATENATING 2 lists into 1
# a_list = [2, 4, 6, 8, 10]
# b_list = [11, 22, 33]
# c_list = a_list + b_list
# print(c_list)   # [2, 4, 6, 8, 10, 11, 22, 33]


# ---------------------------------------------------------------------------------------------- #
# ITERATING A LIST with range(len())
# a_list = ['one', 'two', 'three', 'four']
# for i in range(len(a_list)):
#     print(a_list[i])  # important to use [] here


# ---------------------------------------------------------------------------------------------- #
# ITERATING list to find something
# L = ['one', 'two', 'three', 'four']
# lookup = input('What do you want to find?: ')
# if lookup in L:
#     print('Yes, I found:', lookup)
# else:
#     print(lookup, 'was not found.')


# ---------------------------------------------------------------------------------------------- #
# ITERATING list to find something until found
# L = ['one', 'two', 'three', 'four']
# for item in L:
#     lookup = input('What do you want to find?: ')
#     if lookup not in L:
#         print(lookup, 'was not found.')
#         continue
#     else:
#         print('Yes, I found:', lookup)
#         break

# ---------------------------------------------------------------------------------------------- #
# LIST creation using while loop
# userList = []
# maxLengthList = 3
# while len(userList) < maxLengthList:
#     item = str(input('Enter item to your list: '))
#     userList.append(item)
#     print(userList)
# print('Here\'s your list: ')
# print(userList)


# ---------------------------------------------------------------------------------------------- #
# MEMBERSHIP TESTING in a list
# # Check if value "in" OR "not in" list L
# L = [2, 4, 6, 8, 10]
# print(6 in L)   # True
# print(99 in L)  # False


# ---------------------------------------------------------------------------------------------- #
# TESTING TRUTHY AND FALSY in a list
# # Check if "any" values are equal
# L = [0, 2, 4, 6, 6, 8, 10]
# print(any(L))   # True
# print(all(L))   # False, because int 0 is False


# ---------------------------------------------------------------------------------------------- #
# ASSIGNMENT UNPACKING
# ffxiv = ['Shar', 'Nic', 'Imago', 'Stara', 'Kite', 'Gray', 'Xynto', 'Sel']
# MT, OT, MH, OH, NIN, MCH, DRG, SMN = ffxiv
# tanks = [MT, OT]
# healers = [MH, OH]
# dps = [NIN, MCH, DRG, SMN]
# print('Tanks =', tanks)       # Tanks = ['Shar', 'Nic']
# print('Healers =', healers)   # Healers = ['Imago', 'Stara']
# print('DPS =', dps)           # DPS = ['Kite', 'Gray', 'Xynto', 'Sel']
# print(NIN, 'is a NIN')        # Kite is a NIN


# ---------------------------------------------------------------------------------------------- #
# ASSIGNMENT UNPACKING using SPLIT()
# path = 'C:\Program Files (x86)\SquareEnix\FINAL FANTASY XIV - A Realm Reborn\game\\ffxiv.exe'
# *directories, executable = path.split("\\")
# print(directories)  # ['C:', 'Program Files (x86)', 'SquareEnix', 'FINAL FANTASY XIV - A Realm Reborn']
# print(executable)   # ffxiv.exe


# ---------------------------------------------------------------------------------------------- #
# SWAP values
# a, b = 'Alice', 'Bob'
# a, b = b, a
# print(a, b)  # Bob Alice


# ---------------------------------------------------------------------------------------------- #
# FIND ANY INTEGERS in an iterable and their index position
# L = ['string', 3.14, 121, 'sneeze', (100-50)]
# for index, item in enumerate(L):
#     if type(item) is int:
#         print('Position', index, '=', item)
# Position 2 = 121
# Position 4 = 50


# ---------------------------------------------------------------------------------------------- #
# COMBINE LIST ITEMS into a single string separated by a '|'
# Combine list values into 1 string
# ffxiv = ['Imago', 'Prophecy', 'Folgar']
# separator = '|'
# ffxiv_joined = separator.join(ffxiv)
# print(ffxiv_joined)
# Imago|Prophecy|Folgar


# ---------------------------------------------------------------------------------------------- #
# NESTED TUPLE and LIST combined
# t = 'Imago Dei', 'Gray Embers', 'Kite Waffle'
# l = ['Deltascape: 1.0', 'Deltascape: 2.0', 'Deltascape: 3.0', 'Deltascape: 4.0']
# for tuple_item in t:
#     print(tuple_item.upper())
#     for list_item in l:
#         print(list_item.rjust(18, ' '))
# IMAGO DEI
#    Deltascape: 1.0
#    Deltascape: 2.0
#    Deltascape: 3.0
#    Deltascape: 4.0
# GRAY EMBERS
#    Deltascape: 1.0
#    Deltascape: 2.0
#    Deltascape: 3.0
#    Deltascape: 4.0
# KITE WAFFLE
#    Deltascape: 1.0
#    Deltascape: 2.0
#    Deltascape: 3.0
#    Deltascape: 4.0


# ---------------------------------------------------------------------------------------------- #
# ZIP()

# Q = ['name', 'age', 'sex', 'ethnicity']
# A = ['Shane', '38', 'female']
# T1 = tuple([(q, a) for q, a in zip(Q, A)])  # <class 'tuple'>
# L1 = [(q, a) for q, a in zip(Q, A)]         # <class 'list'>
# D1 = {k:v for k, v in zip(Q, A)}            # <class 'dict'>

# ---------------------------------------------------------------------------------------------- #
# ITERATE multiple sequences using zip()
# days = ['Tuesday', 'Thursday']
# times = ['6:00pm', '9:00pm']
# hours = ['2', '1']
# for day, time, hour in zip(days, times, hours):
#     print(day, 'we raid at', time, 'for', hour, 'hour(s)')
# Tuesday we raid at 6:00 for 2 hour(s)
# Thursday we raid at 9:00 for 1 hour(s)


# ---------------------------------------------------------------------------------------------- #
# LIST COMPREHENSIONS
# [expression for item in iterable]
# [expression for item in iterable if condition]
# [expression for item in iterable if condition1 and condition2]
# [expression for item1 in iterable1 and item2 in iterable2]

# The Google Python Style Guide advocates that list comprehensions should only be used for simple cases,
# when each portion fits in one line (no multiple for clauses or filter expressions)

# ---------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------------------------- #
# LIST COMPREHENSION to find any integers in an iterable
# L = ['string', 3.14, 121, 'sneeze', (100-50)]
# x = [x for x in L if type(x) is int]
# print(x)
# [121, 50]


# ---------------------------------------------------------------------------------------------- #
# LIST COMPREHENSION to find any integers in an iterable
# L = ['string', 3.14, 121, 'sneeze', (100-50)]
# x = [i for i in L if type(i) is int]
# print(x)
# [121, 20]


# ---------------------------------------------------------------------------------------------- #
# LIST COMPREHENSION n to the power of 3 (1x1x1, 2x2x2, 3x3x3...)
# L = [n ** 3 for n in range(1, 11)]
# print(L)
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


# ---------------------------------------------------------------------------------------------- #
# LIST COMPREHENSION with if conditional (print even numbers)
# evens = [num for num in range(11) if num % 2 == 0]
# print(evens)  # [2, 4, 6, 8, 10]
# odds = [num for num in range(11) if num % 2 == 1]
# print(odds)   # [1, 3, 5, 7, 9]



# ---------------------------------------------------------------------------------------------- #
# LIST COMPREHENSION returns list of letters in a string
# L = [c for c in 'pizza']
# print(L)
# ['p', 'i', 'z', 'z', 'a']


# ---------------------------------------------------------------------------------------------- #
# LIST COMPREHENSION returns list of letters in a string to upper case elements
# L = [c.upper() for c in 'pizza']
# print(L)
# ['P', 'I', 'Z', 'Z', 'A']


# ---------------------------------------------------------------------------------------------- #
# Convert a LIST COMPREHENSION of integers into a single string
# a = [i*14 for i in range(0,15)]
# print(a)
# # [0, 14, 28, 42, 56, 70, 84, 98, 112, 126, 140, 154, 168, 182, 196]
# b = [str(i) for i in a]
# print(b)
# # ['0', '14', '28', '42', '56', '70', '84', '98', '112', '126', '140', '154', '168', '182', '196']
# c = ''.join(b)  # note '-'.join(b) will add a dash between each item
# print(c)
# # '014284256708498112126140154168182196'


# ---------------------------------------------------------------------------------------------- #
# LIST COMPREHENSION that changes lower case to upper case
# L = ['wa', 'or', 'ca', 'az', 'nm', 'tx']
# upp_L = [c.upper() for c in L]
# print(upp_L)
# ['WA', 'OR', 'CA', 'AZ', 'NM', 'TX']

# ---------------------------------------------------------------------------------------------- #
# LIST COMPREHENSION that returns a list of positive numbers only
# L = [-3, 0, 1, 6, -4, -1, -8, 7, 6, 6, 3]
# positive_L = [item for item in L if item > 0]
# print(positive_L)
# # [1, 6, 7, 6, 6, 3]


# ---------------------------------------------------------------------------------------------- #
# LIST COMPREHENSION that removes vowels from a string
# astring = 'Kirby Puckett'
# astring_nv = [item for item in astring if item.lower() not in 'aeiou']
# print(astring_nv)
# ['k', 'r', 'b', 'y', ' ', 'p', 'c', 'k', 't', 't']


# ---------------------------------------------------------------------------------------------- #
# LIST COMPREHENSION that contains if/else and conditional statements
# The IF / Else expression must come before the for loop.
# L = [1, 2, 3, 4]
# L1 = [x**2 if x % 2 else x**3 for x in L]
# print(L1)  # [1, 8, 9, 64]


# ---------------------------------------------------------------------------------------------- #
# LIST COMPREHENSION determine leap years
# leaps = [x for x in range(1900, 1941)
#          if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)]
# print(leaps)  # [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940]


# ---------------------------------------------------------------------------------------------- #
# LIST COMPREHENSION NESTED
# nestedL = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# nestedLC = [c for v in nestedL for c in v]
# print(nestedLC)
# How it works:
# The first loop produces the inner lists 1 by 1, as v,
# and each inner list v is iterated over as c to be added to the list being created.


# ---------------------------------------------------------------------------------------------- #
# LIST COMPREHENSION NESTED (example below)
# codes = []
# for sex in "MF":               # Male, Female
#     for size in "SMLX":        # Small, Medium, Large, eXtra large
#         if sex == "F" and size == "X":
#             continue
#         for color in "BGW":    # Black, Gray, White
#             codes.append(sex + size + color)

# ---------------------------------------------------------------------------------------------- #
# LIST COMPREHENSION NESTED
# codes = [s + z + c for s in "MF" for z in "SMLX" for c in "BGW"
#         if not (s == "F" and z == "X")]


# ---------------------------------------------------------------------------------------------- #
# LIST COMPREHENSION WITH A FOR LOOP
# l = [1, 2, 3, 4, 5, 6]
# print([x * 2 for x in l])                     # [2, 4, 6, 8, 10, 12]
# print([x % 2 for x in l])                     # [1, 0, 1, 0, 1, 0]
# print([x * 2 if x % 2 else x*3 for x in l])   #


# ---------------------------------------------------------------------------------------------- #
# NESTED LIST COMPREHENSIONS

# 3x4 matrix implemented as a list of 3 lists of length 4

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
#
# OK USEAGE
# transposed = [[row[i] for row in matrix] for i in range(4)]
# # Equivalent to:
# transposed2 = []
# for i in range(4):
#     transposed2.append([row[i] for row in matrix])
#
# # BEST USAGE
# transposed = list(zip(*matrix))
#
# print(transposed)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


# ---------------------------------------------------------------------------------------------- #
# USING LISTS AS STACKS

# stack  = [1, 2, 3, 4, 5]
# stack.append(6)
# stack.append(7)
# # [1, 2, 3, 4, 5, 6, 7]
# print(stack.pop())
# # 7
# [1, 2, 3, 4, 5, 6]
# stack.pop()
# # 6
# [1, 2, 3, 4, 5]


# ---------------------------------------------------------------------------------------------- #
# USING LISTS AS QUEUES WITH COLLECTIONS.DEQUE (Deque is short for double ended queue)
# List-like container for fast appends and pops on either end of the deque.

# from collections import deque
# queue = deque([2, 4, 6, 8, 10])  # deque([2, 4, 6, 8, 10])
# queue.append(12)                 # deque([2, 4, 6, 8, 10, 12])
# print(queue.popleft())           # returns 2 and deque([4, 6, 8, 10, 12])
# print(queue.pop())               # returns 12 and deque([4, 6, 8, 10])


# ---------------------------------------------------------------------------------------------- #
# A MORE EFFICIENT SEARCH USING A BINARY SEARCH

# hay = [2, 25, 7, 1, 0.5, 122, 47, 41, 60, 12]
#
# def binary_search(needle, haystack):
#     imin, imax = 0, len(haystack)
#     while True:
#         if imin >= imax:
#             return -1
#         midpoint = (imin + imax) // 2
#         if haystack[midpoint] > needle:
#             imax = midpoint
#         elif haystack[midpoint] < needle:
#             imin = midpoint + 1
#         else:
#             return midpoint
#
# binary_search(47, hay)


# ---------------------------------------------------------------------------------------------- #
# A MORE EFFICIENT SEARCH (SIMPLIFIED) USING BISECT
# import bisect
# import random

# def find_closest(haystack, needle):
#     # bisect.bisect_left will return the first value in the haystack that is greater than the needle
#     i = bisect.bisect_left(haystack, needle)
#     if i == len(haystack):
#         return i - 1
#     elif haystack[i] == needle:
#         return i
#     elif i > 0:
#         j = i - 1
#         # since we know the value is larger than needle (and vise versa for the value at j), we
#         # don't need to use absolute values here
#         if haystack[i] -  needle > needle - haystack[j]:
#             return j
#     return i
#
# import_numbers = []
# for i in xrange(10):
#     new_number = random.randint(0, 1000)
#     bisect.insort(import_numbers, new_number)
#
# # important_numbers will already be in order because we inserted new elements with bisect.insort
# print(import_numbers)
#
# closest_index = find_closest(import_numbers, -250)
# print('closest value to -250: ', import_numbers[closest_index])
#
# closest_index = find_closest(import_numbers, 500)
# print('closest value to 500: ', import_numbers[closest_index])
#
# closest_index = find_closest(import_numbers, 1100)
# print('closest value to 1100: ', import_numbers[closest_index])


# ---------------------------------------------------------------------------------------------- #
# REMOVE DUPLICATES FROM A HASHABLE SEQUENCE WHILE PRESERVING ORDER

# def dedupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)
#
# # USE
# a = [1, 5, 2, 1, 9, 1, 5, 10]
# print(list(dedupe(a)))
# # [1, 5, 2, 9, 10]


# ---------------------------------------------------------------------------------------------- #
# REMOVE DUPLICATES FROM A NON-HASHABLE SEQUENCE WHILE PRESERVING ORDER

