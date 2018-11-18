
print()

from collections import OrderedDict
from pprint import pprint

# ------------------------------------------------------------------------------------------------ #
# DICTIONARY
# Mutable, Unordered, Iterable
# NOT a sequence

# WHEN TO USE A DICTIONARY:
# 1) When working with key : value pairs of data.
# 2) Fast Membership Testing using 'in' and 'not in'
# 3) When order doesnt matter

# IMPORTANT NOTES:
# KEYS must be unique and immutable:  Boolean, integer, float, tuple, string
# VALUES can repeat and be any data object or even a fuction or method
# If you have 2 KEYS that are the same, last one wins

# WAY IT WORKS:
# Each key is converted to a number called a "hash value" using a special hash function.
# The associated values are stored in an underlying list at the index location of their hash value.
# Accessing a value involves converting the key to a hash value then jumping to that index location in the list.


# ------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------ #
# DICTIONARY METHODS (START)
# ------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------ #


# clear(), copy(), fromkeys(), get(), items(), keys(), pop(), popitem(), setdefault(),
# update(), values()


# ------------------------------------------------------------------------------------------------ #
# REMOVE ALL ELEMENTS
# D = {'Brad': 38, 'Shane': 32, 'Kevin': 3}
# D.clear()
# print(D)  # {}


# ------------------------------------------------------------------------------------------------ #
# COPY A DICTIONARY
# D.copy()
# Returns a shallow copy
# D = {'Brad': 38, 'Shane': 32, 'Kevin': 3}
# E = D.copy()
# print(E)  # {'Shane': 32, 'Brad': 38, 'Kevin': 3}


# ------------------------------------------------------------------------------------------------ #
# CREATE NEW DICTIONARY from keys of seq and values set to value
# D.fromkeys(seq, value)
# X = {'Food': 'Bread', 'Sport': 'Hockey', 'Toy': 'Robot'}
# Y = []
# print(X)
# Z = X.fromkeys(X, Y)
# Y.append('Fun')
# print(Z)


# ------------------------------------------------------------------------------------------------ #
# RETURN THE VALUE OF A KEY
# D.get(key, default)
# To get value, OR argument if value doesn't exist
# D = {'Brad': 38, 'Shane': 32, 'Kevin': 3}
# print(D.get('Bob', '\nKey = not found'))


# ------------------------------------------------------------------------------------------------ #
# RETURN KEYS & VALUES
# D.items()
# Returns a "view object" of keys/values in D.  Meaning when the dict changes, the view reflects these changes
# D = {'Brad': 38, 'Shane': 32, 'Kevin': 3}
# print(D.items())  # dict_items([('Brad', 38), ('Shane', 32), ('Kevin', 3)])


# ------------------------------------------------------------------------------------------------ #
# RETURN ONLY KEYS
# D.keys()
# Returns a "view object" of the keys.  Meaning when the dict changes, the view reflects these changes
# D = {'Brad': 38, 'Shane': 32, 'Kevin': 3}
# print(D.keys())  # dict_keys(['Shane', 'Brad', 'Kevin'])


# ------------------------------------------------------------------------------------------------ #
# RETURN THE VALUE OF A KEY AND THEN REMOVE IT
# D.pop(key, default)
# If key is in the dictionary, remove it and return its value
# If key is not in the dictionary, a KeyError is raised.
# D = {'Brad': 38, 'Shane': 32, 'Kevin': 3}
# print(D.pop('Shane'))  # 32
# print(D)  # {'Kevin': 3, 'Brad': 38} ---> Shane: 32 has been removed
# def pop_D():
#     try:
#         print(D.pop('Bob'))
#     except KeyError:
#         print('Sorry Charlie')
# pop_D()


# ------------------------------------------------------------------------------------------------ #
# RETURN ARBITRARY KEY/VALUE PAIR AND THEN REMOVE IT
# D.popitem()
# Remove and return an arbitrary (key, value) pair from the dictionary
# Useful to destructively iterate over a dictionary, as often used in set algorithms
# D = {'Brad': 38, 'Shane': 32, 'Kevin': 3}
# print(D.popitem())   # ('Kevin', 3)


# ------------------------------------------------------------------------------------------------ #
# RETURN VALUE if key in dictionary, if NOT in dictionary insert key/value pair and return its value
# D.setdefault(key, default)
# If key is in the dictionary, return its value. If not, insert key with a value of default and return default
# D = {'Brad': 38, 'Shane': 32, 'Kevin': 3}
# D.setdefault('Marsha', 40)
# print(D)                      # Since 'Marsha' not in D, it's key/value is added and 40 is returned
# D.setdefault('Brad', 40)     # Since 'Brad' is in D, its value 38 is returned
# print(D)


# ------------------------------------------------------------------------------------------------ #
# UPDATE/OVERWRITE DICTIONARY KEYS/VALUES
# D.update(other)
# Update the dictionary with the key/value pairs from other, overwriting existing keys
# D = {'Brad': 38, 'Shane': 32, 'Kevin': 3}
# D1 = {'Marsha': 40, 'Ryan': 39, 'Brad': 39}
# D.update(D1)
# print(D)  # {'Brad': 39, 'Marsha': 40, 'Ryan': 39, 'Kevin': 3, 'Shane': 32}


# ------------------------------------------------------------------------------------------------ #
# UPDATE/OVERWRITE DICTIONARY KEYS/VALUES
# Can be used to combine 2 dictionaries
# D.update(kwarg)
# D = {'Brad': 38, 'Shane': 32, 'Kevin': 3}
# D.update(Marsha=40, Ryan=39, Brad=39)
# print(D)  # {'Shane': 32, 'Ryan': 39, 'Marsha': 40, 'Brad': 38, 'Kevin': 3}


# ------------------------------------------------------------------------------------------------ #
# RETURNS ALL VALUES from dictionary
# D.values()
# Returns a "view object" of the dictionary values
# D = {'Brad': 38, 'Shane': 32, 'Kevin': 3}
# print(D.values())  # dict_values([32, 3, 38])


# ------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------ #
# DICTIONARY METHODS (END)
# ------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
# CREATE A DICTIONARY

# a = {'Name': 'Brad', 'Age': 38}                      # Manually
# b = dict(Name='Brad', Age=38)                        # Constructor
# c = dict(zip(('Name', 'Age'), ('Brad', 38)))         # From a zipped tuple
# d = dict(zip(['Name', 'Age'], ['Brad', 38]))         # From a zipped list
# print(a == b == c == d)                          # True


# ------------------------------------------------------------------------------------------------ #
# CREATE A DICTIONARY from a tuple using ZIP()

# tup1 = ('Name', 'Age', 'Sex')
# tup2 = ('Brad', 38, 'Male')
# dict1 = dict(zip(tup1, tup2))
# print(dict1)
# # {'Name': 'Brad', 'Age': 38}
#
# tuple1 = ('Name', 'Age'), ('Brad', 38)
# dict2 = dict(zip(tuple1[0], tuple1[1]))
# print(dict2)
# # {'Name': 'Brad', 'Age': 38}


# ------------------------------------------------------------------------------------------------ #
# ADD a new KEY: VALUE

# D = dict(Brad=38, Shane=32, Kevin=3)
# D['Ollie']=0
# print(D)
# # {'Brad': 38, 'Shane': 32, 'Kevin': 3, 'Ollie': 0}


# ------------------------------------------------------------------------------------------------ #
# MODIFY existing VALUE

# D = dict(Brad=38, Shane=332, Kevin=33)
# D['Shane']=34
# D['Kevin']=3
# print(D)
# # {'Kevin': 3, 'Shane': 34, 'Brad': 38}
#
# # If Key doesn't exist, it's added
# D['Ollie']=1
# print(D)
# # {'Brad': 38, 'Shane': 34, 'Kevin': 3, 'Ollie': 1}


# ------------------------------------------------------------------------------------------------ #
# DELETE A KEY: VALUE pair, keep the rest

# myDict = {'Brad': 38, 'Shane': 32, 'Kevin': 3}
# del myDict['Brad']
# # {'Kevin': 3, 'Shane': 32}

# ------------------------------------------------------------------------------------------------ #
# DELETE ALL KEYS

# myDict = {}
# myDict.clear()


# ------------------------------------------------------------------------------------------------ #
# GET A VALUE

# D = {'Brad': 38, 'Shane': 3434, 'Kevin': 33}
# D['Brad']
# 38


# ------------------------------------------------------------------------------------------------ #
# ITERATING to GET ALL VALUES

# D = {'Brad': 38, 'Shane': 3434, 'Kevin': 33}
# D1 = {D[item] for item in D}
# D2 = {item for item in D.values()}


# ------------------------------------------------------------------------------------------------ #
# MEMBERSHIP TESTING

# D = {'Shane': 34, 'Kevin': 3, 'Brad': 38}
# 'Birds' in D     # False
# 'Brad' in D     # True
# 34 in D.values() # True


# ------------------------------------------------------------------------------------------------ #
# CALCULATING min, max and warnings

# prices = {
#        'ACME': 45.23,
#        'AAPL': 612.78,
#        'IBM': 205.55,
#        'HPQ': 37.20,
#        'FB': 10.75
# }
#
# # In order to perform useful calculations on the dictionary contents, it is often
# # useful to invert the keys and values of the dictionary using zip().
# # For Example:
# min_price = min(zip(prices.values(), prices.keys()))  # (10.75, 'FB')
# max_price = max(zip(prices.values(), prices.keys()))  # (612.78, 'AAPL')
#
#
# # Sorted by values after being inverted
# prices_sorted = sorted(zip(prices.values(), prices.keys()))
# pprint(prices_sorted)
#
# # # -|-|- Be AWARE that zip() creates an iterator that can only be consumed once.
# prices_and_names = zip(prices.values(), prices.keys())
# print(min(prices_and_names))  # OK
# print(min(prices_and_names))  # ValueError: max() arg is an empty sequence
#
# # -|-|- Make an object and you can reuse it.
# y = min(prices_and_names)
# print(y)
# print(y)


# ------------------------------------------------------------------------------------------------ #
# FIND COMMONALITIES BETWEEN 2 DICTIONARIES

# D = {'Brad': 38, 'Shane': 32, 'Kevin': 3}
# E = {'Ollie': 1, 'Shane': 32, 'Unknown': 0}
#
# # & Common Keys
# print(D.keys() & E.keys())    # {'Shane'}
#
# # - Keys in D, but not in E
# print(D.keys() - E.keys())    # {'Kevin', 'Brad'}
#
# # ^ Unique Keys
# print(D.keys() ^ E.keys())    # {'Kevin', 'Brad', 'Ollie', 'Unknown'}
#
# # | All Keys
# print(D.keys() | E.keys())    # {'Ollie', 'Brad', 'Kevin', 'Shane', 'Unknown'}
#
# # & Common Items and so forth...
# print(D.items() & E.items())  # {('Shane', 32)}


# ------------------------------------------------------------------------------------------------ #
# DICTIONARY COMPREHENSIONS ---------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------ #

# # {keyexpression: valueexpression for key, value in iterable}
# # {keyexpression: valueexpression for key, value in iterable if condition}
# #
# # Example Dictionary Comprehension
# D = {'a': 1, 'b': 2, 'c': 3}
# x = {key: value for key, value in D.items() if key in 'acdc'}
# print(x)


# ------------------------------------------------------------------------------------------------ #
# CREATE A NEW DICTIONARY WITH CERTAIN KEYS REMOVED

# DICTIONARY COMPREHENSION
# D = {'Brad': 38, 'Shane': 32, 'Kevin': 3}
# E = {key:D[key] for key in D.keys() - {'z', 'Brad', 'Shane'}}
# print(E)  # {'Kevin': 3}  notice 'z' was in there, but didn't cause error


# ------------------------------------------------------------------------------------------------ #
# DICTIONARY COMPREHENSION return FILE NAME & SIZE from dropbox python subjects
# Create a dictionary where key is filename in the current directory and value is file size.

# import os
# from pprint import pprint
#
# print(os.getcwd())  # /Brad/Dropbox/Python Subjects
#
# # DICTIONARY COMPREHENSION printing directory file list, sorted by file size
# file_size_and_file = {os.path.getsize(name): name  for name in os.listdir(os.getcwd())}
# pprint(file_size_and_file)
#
#
# # LIST COMP printing directory file list, sorted by file size
# lcomp = [(str(os.path.getsize(name)).rjust(10, '.'), name) for name in os.listdir(os.getcwd())]
# lcomp.sort(reverse=True)
# pprint(lcomp)
#
#
# # LIST COMP printing directory file list, sorted by file size
# lcomp = [(name, os.path.getsize(name)) for name in os.listdir(os.getcwd())]
# lcomp.sort(key=lambda name: name[1], reverse=True)
# pprint(lcomp)


# # WIP
# def file_size_and_file(dir):
#     for name in os.listdir(dir):
#         print(name)
#
# file_size_and_file(os.getcwd())


# ------------------------------------------------------------------------------------------------ #
# DICTIONARY COMPREHENSION from a list of tuples

# dial_codes = [
#     (86, 'China'),
#     (91, 'India'),
#     (1, 'United States'),
#     (7, 'Russia')
#     ]
#
# dc = {country: code for code, country in dial_codes}
# print(dc)  # {'China': 86, 'India': 91, 'United States': 1, 'Russia': 7}


# ------------------------------------------------------------------------------------------------ #
# DICTIONARY COMPREHENSION to get ALL KEY: VALUE

# c = {'Shane': 34, 'Kevin': 3, 'Brad': 38}
# c1 = {k: v for k, v in c.items()}
# print(c1)
#
# d = {'Brad': ('caucasian', 'male', 38)}
# d1 = {k: (v[1], v[2]) for k, v in d.items()}
# print(d1)


# ------------------------------------------------------------------------------------------------ #
# ITERATING to get each KEY: VALUE

# d = {'Shane': 34, 'Kevin': 3, 'Brad': 38}
# for item in d:                     # Iterate only keys
#     print(item, d[item])           # Print key and key value i.e item, d[item]
#
#
# d = {'Shane': 34, 'Kevin': 3, 'Brad': 38}
# for k, v in d.items():             # Iterate key/value pairs
#     print(k, v)                    # Print all key/value pairs


# ------------------------------------------------------------------------------------------------ #
# ITERATING sort by keys in descending order

# d = {'C': 34, 'A': 3, 'B': 38, 'D': 20}
# for key in sorted(d.keys()):
#     print(key, d[key], sep=' = ')
# A = 3
# B = 38
# C = 34
# D = 20


# ------------------------------------------------------------------------------------------------ #
# ITERATING sort by keys in descending order using a generator

# d = {'C': 34, 'A': 3, 'B': 38, 'D': 20}
#
# # GENERATOR
# def items_in_key_order(d):
#     for key in sorted(d):
#         yield key, d[key]
#
# # ITERATING over this generator one by one using NEXT
# iiko = items_in_key_order(d)
# print(next(iiko))  # ('A', 3)
# print(next(iiko))  # ('B', 38)
# print(next(iiko))  # ('C', 34)
# print(next(iiko))  # ('D', 20)
#
# # ITERATING over this generator using a FOR LOOP
# for i in items_in_key_order(d):
#     print(i)
# # ('A', 3)
# # ('B', 38)
# # ('C', 34)
# # ('D', 20)


# ------------------------------------------------------------------------------------------------ #
# ITERATING A DICTIONARY sort by values in ascending order

# d = {'C': 34, 'A': 3, 'B': 38, 'D': 20}
#
# for k, v in sorted(d.items(), key=lambda x: x[1]):
#     print(k, v)


# ------------------------------------------------------------------------------------------------ #
# ITERATE TO SWAP KEYS WITH VALUES
# Swap keys: values with a dictionary comprehension

# d = {'Shane': 34, 'Kevin': 3, 'Brad': 38}
# inverted_d = {v: k for k, v in d.items()}
# print(d)
# print(inverted_d)


# ------------------------------------------------------------------------------------------------ #
# ADD A NEW KEY/VALUE IF "NOT IN" EXISTING DICTIONARY

# d = {'Shane': 34, 'Brad': 38}
# if 'Kevin' not in d:
#     d['Kevin'] = 3
#     print(d)
# {'Kevin': 3, 'Shane': 34, 'Brad': 38}


# ------------------------------------------------------------------------------------------------ #
# ITERATE to sort KEYS in descending order

# d = {1: 'I', 5: 'V', 3: 'III', 2: 'II', 4: 'IV'}
#
# print(sorted(d))
#
# for item in reversed(sorted(d)):  # ONLY sequences work with reversed()
#     print(item, d[item])


# ------------------------------------------------------------------------------------------------ #
# ITERATE to get KEYS and VALUES in descending order

# d = {'C': 34, 'A': 3, 'F': 19, 'B': 38, 'D': 20, 'E': 9}
#
# import operator
#
# reverse_sort_d_by_key = sorted(d.items(), key=operator.itemgetter(0), reverse=True)
# print(reverse_sort_d_by_key)
#
# sort_d_by_value = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
# print(sort_d_by_value)
#
#
# # OR
#
#
# def val(elem):
#     return elem[1]
#
# for key, value in sorted(d.items(), key=val, reverse=True):
#     print(value, key, sep=' - ')


# ------------------------------------------------------------------------------------------------ #
# ITERATE to count OCCURRENCES OF LETTERS
#  Create a dictionary using comprehension of a frequency string
# {key_expression: value_expression for expression in iterable}

# word = 'abracadabra'
# print(set(word))
# count_letters = {letter: word.count(letter) for letter in set(word)}
# print(count_letters)
# {'b': 2, 'r': 2, 'c': 1, 'a': 5, 'd': 1}



# ------------------------------------------------------------------------------------------------ #
# ITERATE to count word occurrences in a List
# (Page 110 in 'automate the boring stuff')
# L = ['lol', 'omg', 'ftw', 'afk', 'afk', 'bff', 'omg', 'afk']
# count = {}
# for word in L:
#     count.setdefault(word, 0)  #
#     count[word] += 1
# print(count)  # {'ftw': 1, 'afk': 3, 'lol': 1, 'bff': 1, 'omg': 2}
# ------------------------------ #
# --SAME AS ABOVE using pprint-- #
# ------------------------------ #
# import pprint
# some_list = ['lol', 'omg', 'ftw', 'afk', 'afk', 'bff', 'omg', 'afk']
# new_list = {}
# for word in some_list:
#     new_list.setdefault(word, 0)
#     new_list[word] = new_list[word] + 1 # or count[word] += 1
#
# pprint.pprint(new_list, indent=1, width=1)


# ------------------------------------------------------------------------------------------------ #
# ITERATE TO COUNT WORDS IN A STRING and print a frequency dictionary
# Frequency String, counting occurrences
# s = 'Brad Brad Brad Shane Shane Kevin'
# words = s.split()
# print(words)  # ['Brad', 'Brad', 'Brad', 'Shane', 'Shane', 'Kevin']
# d = {}
# for w in words:
#     if w in d:
#         d[w] += 1
#     else:
#         d[w] = 1
# print(d)


# ------------------------------------------------------------------------------------------------ #
# Function that prints a frequency dictionary
# s = 'Brad Brad Shane Shane Kevin Ollie'
# def make_freq_dict(s):
#     """
#     Accept 1 string argument and return a dictionary whose keys are the words of s,
#     and whose values are the counts of those words.
#     """
#     words = s.split()   # words = ['Brad', 'Brad', 'Shane', 'Shane', 'Kevin', 'Ollie']
#     d = {}              # d = {}
#     for w in words:
#         if w in d:      # Is name in list already?
#             d[w] += 1   # If yes add 1 to the value
#         else:
#             d[w] = 1    # If no add new name and set its value equal to 1
#     print(d)            # {'Brad': 2, 'Shane': 2, 'Kevin': 1, 'Ollie': 1}
# make_freq_dict(s)


# ------------------------------------------------------------------------------------------------ #
# DICTIONARY AS CACHES
# Data structure that stores results to avoid recalculating those results over and over.

# Suppose you have a function that takes 3 integers as arguments and returns a result.

# trio_cache = {}
# def trio(a, b, c):
#     if (a, b, c) in trio_cache:
#         return trio_cache[(a, b, c)]
#     else:
#         mean = (a + b + c) / 3
#         return mean
#
# print(trio(4, 2, 1))


# ------------------------------------------------------------------------------------------------ #
# Functions used to emulate switch/case statements

# def dispatch_if(operator, x, y):
#     if operator == 'add':
#         return x + y
#     elif operator == 'sub':
#         return x - y
#     elif operator == 'mul':
#         return x * y
#     elif operator == 'div':
#         return x / y
#     else:
#         return None
#
#
# def dispatch_dict(operator, x, y):
#     return {
#         'add': lambda: x + y,
#         'sub': lambda: x - y,
#         'mul': lambda: x * y,
#         'div': lambda: x / y,
#     }.get(operator, lambda: None)()


# -------------------------------------------------------------------------------------
# Dictionary Comprehension keys that start with provide letter
# D = {'Uno': 1, 'Dos': 2, 'Tres': 3, 'umbrella': 5}
#
# key_found = {k: v for k, v in D.items() if k.upper().startswith('T')}
# print(key_found)

# -------------------------------------------------------------------------------------
# Function that returns all key: value pairs that start with provided letter
# D = {'Uno': 1, 'Dos': 2, 'Tres': 3, 'umbrella': 5}
#
# def key_starts_with(letter: str, dict):
#     """Returns all dictionary key: value pairs whose keys start with letter provided"""
#     kv_dict = {}
#     for k, v in dict.items():
#         if k.startswith(letter.lower()):
#             kv_dict[str(k)] = v
#         elif k.startswith(letter.upper()):
#             kv_dict[str(k)] = v
#     print(len(kv_dict), 'found starting with:', letter.upper())
#     return kv_dict
#
#
# print(key_starts_with('u', D))


# ------------------------------------------------------------------------------------------------ #
# OrderedDict
# ------------------------------------------------------------------------------------------------ #

# def ordd():
#     d = {'a': 1, 'b': 2,'c': 3}
#     print(d)
#     d1 = OrderedDict(d)
#     print(d1, type(d1))  # (’a’, 1), (’b’, 2), (’c’, 3)
# ordd()    # OrderedDict([('a', 1), ('b', 2), ('c', 3)])


# ------------------------------------------------------------------------------------------------ #
# WARNING:  UNDER CONSTRUCTION ------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------ #
#

# ------------------------------------------------------------------------------------------------ #
# DICTIONARY
# Counting the number of occurrences of each unique word in a file
# import string
# import sys
# words = {}
# strip = string.whitespace + string.punctuation + string.digits
# for line in open('star.txt'):
#     for word in line.lower().split():
#         word = word.strip(strip)
#         if len(word) > 2:
#             words[word] = words.get(word, 0) + 1
# for word in sorted(words):
#     print("'{0}' occurs {1} times".format(word, words[word]))

# x = dir(string)
# for item in x:
#     if not item.startswith('_'):
#         print(item)

# print(help(string.whitespace))


# d = OrderedDict.fromkeys('abc')
# d.move_to_end('b')
# print(d)
# print(''.join(d.keys()))  # 'acb'
# d.move_to_end('b', last=False)
# print(''.join(d.keys()))  # 'bac'


# ------------------------------------------------------------------------------------------------ #
# Iterate over the data in groups based on the value of a
# particular field, such as date

# from pprint import pprint
#
# rows = [
#     {'address': '5412 N CLARK', 'date': '07/01/2018'},
#     {'address': '5148 N CLARK', 'date': '07/04/2018'},
#     {'address': '5800 E 158TH', 'date': '07/02/2018'},
#     {'address': '2122 N CLARK', 'date': '07/03/2018'},
#     {'address': '5645 N RAVEN', 'date': '07/02/2018'},
#     {'address': '1060 W ADDLE', 'date': '07/02/2018'},
#     {'address': '4801 N BROAD', 'date': '07/01/2018'},
#     {'address': '1039 W GRAND', 'date': '07/04/2018'},
# ]

# # pprint(rows)
#
# from operator import itemgetter
# from itertools import groupby
#
# # First sort by the desired field first
# rows.sort(key=itemgetter('date'))
#
#
# # Second iterate in groups
# for date, items in groupby(rows, key=itemgetter('date')):
#     print(date)
#     for i in items: print(' ', i)

# 07/01/2018
#   {'address': '5412 N CLARK', 'date': '07/01/2018'}
#   {'address': '4801 N BROAD', 'date': '07/01/2018'}
# 07/02/2018
#   {'address': '5800 E 158TH', 'date': '07/02/2018'}
#   {'address': '5645 N RAVEN', 'date': '07/02/2018'}
#   {'address': '1060 W ADDLE', 'date': '07/02/2018'}
# 07/03/2018
#   {'address': '2122 N CLARK', 'date': '07/03/2018'}
# 07/04/2018
#   {'address': '5148 N CLARK', 'date': '07/04/2018'}
#   {'address': '1039 W GRAND', 'date': '07/04/2018'}

print()