print()

# ------------------------------------------------------------------------------------------------ #
# COLLECTIONS MODULE
# ------------------------------------------------------------------------------------------------ #

# namedtuple()  # factory function for creating tuple subclasses with named fields
# deque         # list-like container with fast appends and pops on either end
# ChainMap      # dict-like class for creating a single view of multiple mappings
# Counter       # dict subclass for counting hashable objects
# OrderedDict   # dict subclass that remembers the order entries were added
# defaultdict   # dict subclass that calls a factory function to supply missing values
# UserDict      # wrapper around dictionary objects for easier dict subclassing
# UserList      # wrapper around list objects for easier list subclassing
# UserString    # wrapper around string objects for easier string subclassing

# ------------------------------------------------------------------------------------------------ #
# NAMED TUPLE
# Behaves like a normal tuple and same performance, additionally...
# Adds the ability to refer to items in the tuple by name as well as by index position

# ------------------------------------------------------------------------------------------------ #
# CREATE A NAMED TUPLE
from collections import namedtuple

# Duck = namedtuple('duck', ('mouth', 'feet'))  # type(Duck) = <class 'type'>
# duck = Duck('flat bill', 'webbed')            # type(duck) = <class '__main__.Duck'>
# print(duck)                                   # duck(mouth='flat bill', feet='webbed')
# print(duck.mouth)                             # flat bill
# print(duck.feet)                              # webbed


# for i in duck:                                # flat bill
#     print(i)                                  # webbed


# x = set(dir(duck))
# y = set(dir(tuple))
# result = x.difference(y)
# for i in result:                              # feet
#     if not i.startswith('_'):                 # mouth
#         print(i)


# ------------------------------------------------------------------------------------------------ #
# CREATE A NAMED TUPLE from a dictionary
# Duck = namedtuple('duck', 'neck, body')
# parts = {'neck': 'long', 'body': 'feathered'}
# duck2 = Duck(**parts)  # extracts keys and values from the "parts" dict and uses them as args
# print(duck2)           # duck(neck='long', body='feathered')
# print(duck2.neck)      # long
# print(duck2.body)      # feathered


# ------------------------------------------------------------------------------------------------ #
# NAMED TUPLES are immutable, but you can replace and return another named tuple
# duck3 = duck2._replace(neck='magnificent', body='waterproof')
# print(duck3)

# ------------------------------------------------------------------------------------------------ #
# NAMED TUPLE OPTIONS

# title_tupl = ('Healer', 'Warrior', 'Dragoon')
# title_list = ['Healer', 'Warrior', 'Dragoon']
# title_dict = {'Healer': 'Imago', 'Warrior': 'Nic', 'Dragoon': 'Xynto'}
#
# badonkadonks = namedtuple('badonkadonks', title_tupl)
# badonkadonks = namedtuple('badonkadonks', title_list)
# badonkadonks = namedtuple('badonkadonks', ('Healer', 'Warrior', 'Dragoon'))  # most readable
# badonkadonks = namedtuple('badonkadonks', 'Healer Warrior Dragoon')
#
# static = badonkadonks('Imago', 'Nic', 'Xynto')
# static = badonkadonks('Imago', 'Nic', 'Xynto')
# static = badonkadonks(**title_dict)
# print(static)            # badonkadonks(Healer='Imago', Warrior='Nic', Dragoon='Xynto')
#
# print()
# print(static[0])         # Imago
# print(static.Healer)     # Imago
# print(static.Warrior)    # Nic
# print(static.Dragoon)    # Xynto
# H, W, D = static         # Unpacking is supported
# print(H, W, D, sep='--') # Imago--Nic--Xynto
# print(H.upper())         # IMAGO
#
#
# print()
# # Iterate the namedtuple
# for i in static:
#     print(i.upper() if i[0] in 'aeiouAEIOU' else i.lower())


# Role = namedtuple('Role', ['Healer', 'Warrior', 'Dragoon'])
# PRM = Role('Imago', 'Prophecy', 'Folgar')
# print(PRM)              # Role(Healer='Imago', Warrior='Prophecy', Dragoon='Folgar')
# print(PRM.Healer)       # Imago
# print(PRM.Warrior)      # Prophecy
# print(PRM.Dragoon)      # Folgar
# print(PRM.Healer + PRM.Warrior.upper())  # ImagoPROPHECY


# ------------------------------------------------------------------------------------------------ #
# NAMED TUPLE
# Named tuples are especially useful for assigning field names to result tuples returned by the csv or sqlite3 modules:

# # WIP
# EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
# import csv
# for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
#     print(emp.name, emp.title)
#
# import sqlite3
# conn = sqlite3.connect('/companydata')
# cursor = conn.cursor()
# cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
# for emp in map(EmployeeRecord._make, cursor.fetchall()):
#     print(emp.name, emp.title)
# # ?????????????????????????????



# """
# Keep a limited history of last few items seen during iteration,
# this is a perfect use of collections.deque
# Below code performs a simple text match on a sequence of lines and yields the
# matching line along with the previous N lines of context when found
# """
# from collections import deque
# def search(lines, pattern, history=5):
#     previous_lines = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line, previous_lines
#         previous_lines.append(line)

# Example use on a file
# if __name__ == '__main__':
#     with open('somefile.txt') as f:
#         for line, prevlines in search(f, 'python', 5):
#             for pline in prevlines:
#                 print(pline, end='')
#             print(line, end='')
#             print('-'*20)


# ------------------------------------------------------------------------------------------------ #
# DEQUE (pronounced "deck")
# ------------------------------------------------------------------------------------------------ #
# WHEN TO USE A DEQUE ---------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------ #
# If you are constantly adding and removing items from either end of a list
# like a FIFO data structure.

# from collections import deque
# d = deque('abc')                 # Make a new deque(list) with three items
# for elem in d:                   # iterate over the deque's elements
#     print(elem.upper())
#                                  # A
#                                  # B
#                                  # C
#
# d.append('d')                    # add a new entry to the right side
# print(d)                         # deque(['a', 'b', 'c', 'd'])
#
# d.appendleft('aa')               # add a new entry to the left side
# print(d)                         # deque(['aa', 'a', 'b', 'c', 'd'])
#
# print(d.pop())                   # return and remove the rightmost item
#                                  # 'd'
#
# print(d.popleft())               # return and remove the leftmost item
#                                  # 'aa'
#
# print(list(d))                   # list the contents of the deque
#                                  # ['a', 'b', 'c'] assign to variable to convert to list obj
#
# print(d[0])                      # peek at leftmost item
#                                  # 'a'
#
# print(d[-1])                     # peek at rightmost item
#                                  # 'c'
#
# print(list(reversed(d)))         # list the contents of a deque in reverse
#                                  # ['c', 'b', 'a']
#
# 'b' in d                         # search the deque
#                                  # True
#
# d.extend('def')                  # # add multiple elements at once
# print(d)                         # deque(['a', 'b', 'c', 'd', 'e', 'f'])
#
# d.extend(['extended'])           # add a string element, you must use [] brackets
# print(d)                         # deque(['a', 'b', 'c', 'd', 'e', 'f', 'extended'])
#
# d.rotate(1)                      # right rotation -- brings last item to first
# print(d)                         # deque(['extended', 'a', 'b', 'c', 'd', 'e', 'f'])
#
# d.rotate(-1)                     # left rotation -- brings first item to last
# print(d)                         # deque(['a', 'b', 'c', 'd', 'e', 'f', 'extended'])
#
# print(deque(reversed(d)))        # make a new deque in reverse order
#                                  # deque(['extended', 'f', 'e', 'd', 'c', 'b', 'a'])
#
# d.clear()                        # empty the deque
# print(d)                         # deque([])
#
# d.pop()                          # cannot pop from an empty deque
#                                  # Traceback (most recent call last):
#                                  #     File "<pyshell#6>", line 1, in -toplevel-
#                                  #         d.pop()
#                                  # IndexError: pop from an empty deque
#
# d.extendleft('abc')              # extendleft() reverses the input order
# print(d)                         # deque(['c', 'b', 'a'])


# def search(lines, pattern, history=5):
#     previous_lines = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line, previous_lines
#         previous_lines.append(line)


# ------------------------------------------------------------------------------------------------ #
# ORDERED DICT
# ------------------------------------------------------------------------------------------------ #
from collections import OrderedDict

# An OrderedDict is a dict that remembers the order that keys were first inserted.
# If a new entry overwrites an existing entry, the original insertion position is left unchanged.
# Deleting an entry and reinserting it will move it to the end.
# ordered dictionaries also support reverse iteration using reversed()
# Be aware that the size of an OrderedDict is more than twice as large as a normal dictionary due to
# the extra linked list that’s created.

# ------------------------------------------------------------------------------------------------ #
# ORDERED DICT METHODS (not available in the regular dictionary)
# ------------------------------------------------------------------------------------------------ #

# ------------------------------------------------------------------------------------------------ #
# OrderedDict.popitem()

# The popitem() method for ordered dictionaries returns and removes a (key, value) pair.
# The pairs are returned in LIFO order if last is true or FIFO order if false.


# ------------------------------------------------------------------------------------------------ #
# OrderedDict.fromkeys()

# Move an existing key to either end of an ordered dictionary.
# The item is moved to the right end if last is true (the default) or to the beginning if last is false.
# Raises KeyError if the key does not exist:

# d = OrderedDict.fromkeys('abc')
# d.move_to_end('b')
# print(d)
# print(''.join(d.keys()))  # 'acb'
# d.move_to_end('b', last=False)
# print(''.join(d.keys()))  # 'bac'


# ------------------------------------------------------------------------------------------------ #
# ORDERED DICT

# d = OrderedDict()
# d['One'] = 1
# d['Two'] = 2
# print(d)  # OrderedDict([('One', 1), ('Two', 2)])
# od = {k: v for k, v in d.items()}
# print(od)  # {'One': 1, 'Two': 2}


# ------------------------------------------------------------------------------------------------ #
# ORDERED DICT


# d = collections.OrderedDict()
# print(type(d))
# d['first'] = 1
# d['second'] = 2
# d['third'] = 3
# d['fourth'] = 4
# print(d)
#
# for key in d:
#     print(key, d[key])


# ------------------------------------------------------------------------------------------------ #
# OrderedDict


# def ordd():
#     d = {'a': 1, 'b': 2,'c': 3}
#     print(d)
#     d1 = OrderedDict(d)
#     print(d1, type(d1))  # (’a’, 1), (’b’, 2), (’c’, 3)
# ordd()    # OrderedDict([('a', 1), ('b', 2), ('c', 3)])


# ------------------------------------------------------------------------------------------------ #
# DEFAULT DICT
# from collections import defaultdict

# Specifies a default value for new keys.
# Its argument is a function.  Also you can use lambda
# pairs = defaultdict(lambda: 'Missing...')
# pairs['A'] = 'Apple'
# pairs['C'] = 'Cake'
# print(pairs['A'])
# print(pairs['B'])
# print(pairs['C'])

# for key, value in pairs:
#     if key not in d1:
#         d1[key] = []
#     d1[key].append(value)
# print(d1)
# {'b': [2], 'c': [3], 'a': [1]}

# ------------------------------------------------------------------------------------------------ #
# Default Factory list
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = defaultdict(list)
# for key, value in s:
#     d[key].append(value)
# print(d)
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

# ------------------------------------------------------------------------------------------------ #
# Default Factory integer
# s = 'mississippi'
# d = defaultdict(int)
# for k in s:
#     d[k] += 1
#
# print(sorted(d.items()))
#  [('i', 4), ('m', 1), ('p', 2), ('s', 4)]
