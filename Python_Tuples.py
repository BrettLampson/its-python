

# ------------------------------------------------------------------------------------------------ #
# TUPLES
# ------------------------------------------------------------------------------------------------ #

# Immutable, Ordered, Iterable

# WHEN TO USE A TUPLE:
# 1) Useful when data will not change
# 2) Faster than lists, because lists require more memory overhead
# 3) To be used in dictionaries as keys
# 4) When the data is structurally diverse

# IMPORTANT NOTES:
# Possible to change mutable data types within your tuple. Example changing list elements within your tuple.
# We can also retrieve a particular item in a list or tuple using the item access operator ([]),
# concatenate two lists or tuples using +, and append one to another using +=.

# ------------------------------------------------------------------------------------------------ #
# TUPLE METHODS
# ------------------------------------------------------------------------------------------------ #

# count(), index()


# ------------------------------------------------------------------------------------------------ #
# count()
# vowels = ('A', 'E', 'I', 'O', 'U', 'A', 'A', 'I', 'U')
# print(vowels.count())  # 3


# ------------------------------------------------------------------------------------------------ #
# index()
# vowels = ('a', 'e', 'i', 'o', 'u')
# print('The index of u =', vowels.index('u'))  # The index of u = 4


# ------------------------------------------------------------------------------------------------ #
# TUPLE METHODS END
# ------------------------------------------------------------------------------------------------ #
#


# ------------------------------------------------------------------------------------------------ #
# CREATING A TUPLE
# myTuple = ()                  # Empty tuple
# myTuple = 1,                  # Must still use the comma after the 1, otherwise its <class 'int'>
# myTuple = (1, 2, 3)           # Comma use tells this is a tuple, parentheses are optional
# myTuple = tuple(myList)       # Constructor


# ------------------------------------------------------------------------------------------------ #
# TUPLE Unpacking
# food = 'chicken', 'rice', 'asparagus'
# protein, carbohydrate, vegetable = food  # tuple reference must be on right side
# print(protein)        # chicken
# print(carbohydrate)   # rice
# print(vegetable)      # asparagus
# print(food)           # ('chicken', 'rice', 'asparagus') remains unchanged


# ------------------------------------------------------------------------------------------------ #
# NAMED TUPLE defined
# A subclass of Tuple
# Behaves like a normal tuple and same performance, additionally...
# Adds the ability to refer to items in the tuple by name as well as by index position
# This allows us to create aggregates of data items


# ------------------------------------------------------------------------------------------------ #
# NAMED TUPLE
# from collections import namedtuple
# Duck = namedtuple('Duck', 'bill tail') # Syntax for a namedtuple <class 'type'>
# duck = Duck('wide orange', 'long') # this is a <class '__main__.Duck'>
# print(duck)                        # Duck(bill='wide orange', tail='long')
# print(duck.bill)                   # wide orange
# print(duck.tail)                   # long

# ------------------------------------------------------------------------------------------------ #
# NAMED TUPLE from a dictionary
# parts = {'bill': 'wide orange', 'tail': 'long'}
# duck2 = Duck(**parts)  # keyword argument that extracts keys and values from the parts dict and uses them as args
# print(duck2)

# ------------------------------------------------------------------------------------------------ #
# NAMED TUPLES are immutable, but you can replace and return another named tuple
# duck3 = duck2._replace(tail='magnificent', bill='ferocious')
# print(duck3)

# ------------------------------------------------------------------------------------------------ #
# NAMED TUPLE
# from collections import namedtuple
# Role = namedtuple('Role', ['Healer', 'Warrior', 'Dragoon'])  # Syntax for a namedtuple
# BDonks = Role('Imago', 'Nic', Dragoon='Xynto')  # ---- Instantiate with positional or keyword arguments ----
# print(BDonks)           # Static_Members(Imago='Healer', Nic='Warrior', Xynto='Dragoon')
# print(BDonks[0])        # Imago -- <class 'str'>
# print(BDonks.Healer)    # Imago -- <class 'str'>
# print(BDonks[1])        # Nic -- <class 'str'>
# print(BDonks[2])        # Xynto -- <class 'str'>
#
# PRM = Role('Imago', 'Prophecy', 'Folgar')
# print(PRM)              # Role(Healer='Imago', Warrior='Prophecy', Dragoon='Folgar')
# print(type(PRM))        # <class '__main__.Role'>
# print(PRM.Dragoon)      # Folgar
# H, W, D = BDonks        # Unpacking is supported
# print(H, W, D)          # Imago Nic Xynto
# print(PRM.Healer + PRM.Warrior)  # ImagoProphecy


# ------------------------------------------------------------------------------------------------ #
# NAMED TUPLE
# Sale = collections.namedtuple("Sale", "productid customerid date quantity price")


# ------------------------------------------------------------------------------------------------ #
# ITERATING TUPLE with multiple variables
# import math
# mytupl = ((3, 4), (5, 12), (28, 45))
# for x, y in mytupl:
    # print(math.hypot(x, y))
    # print(x)                # 3 5 28
    # print(x, y)             # 3 4
                              # 5 12
                              # 28 45
# z = x + y                   # x, y assigned to 28 and 45 respectively because it was last item in the iteration.
# print('x + y =', z)


# ------------------------------------------------------------------------------------------------ #
# ITERATING a sequence of tuples of varying length
# characteristics = [
#     ('brett', 38, 'male'),
#     ('shaina', 'female'),
#     ('kayden', 3)
# ]
# def do_brett(age, sex):
#     print('brett', age, sex)
#
# def do_shaina(sex):
#     print('shaina', sex)
#
# def do_kayden(age):
#     print('kayden', age)
#
# print('Results:')
# for tag, *args in characteristics:
#     if tag == 'brett':
#         do_brett(*args)
#     elif tag == 'shaina':
#         do_shaina(*args)
#     else:
#         do_kayden(*args)
# Results:
# brett 38 male
# shaina female
# kayden 3

# ------------------------------------------------------------------------------------------------ #
# ...

# records = [
#     ('foo', 1, 2),
#     ('bar', 'hello'),
#     ('foo', 3, 4),
# ]
#
#
# def do_foo(x, y):
#     print('foo', x, y)
#
# def do_bar(s):
#     print('bar', s)
# print('Results:')
# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)
# Results:
# foo 1 2
# bar hello
# foo 3 4



# ?????????????????????????????
# ----- NAMED TUPLE ----- #
# Named tuples are especially useful for assigning field names to result tuples returned by the csv or sqlite3 modules:

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
# ?????????????????????????????