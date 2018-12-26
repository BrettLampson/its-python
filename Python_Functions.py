
# ---------------------------------------------------------------------------------------------- #
# FUNCTIONS


# WHEN TO USE A FUNCTION:
# When you want to reuse a chunk of code, just pass in new arguments
# Functions can do 2 things:  define it, and call it
# Functions have 2 primary roles:
# 1) Maximizing code reuse, minimizing redundancy
# 2) Procedural decomposition, subtasking out chunks.
#    Easier to implement subtasks in isolation, than all at once.  Also helps when refactoring.

# FIRST CLASS CITIZENS
# Functions: you can:
# 1) Assign them to variables, example:  x = function(argument)
# 2) Use them as arguments to other functions
# 3) Return them from functions
# 4) Other: nest def statements inside if statements, while loops and other def statements


# General Syntax
# def functionName(parameters):
#     """
#     Docstring
#     """
#     Suite


# ---------------------------------------------------------------------------------------------- #
# FUNCTIONS used as MODULES

# def lol():
#     print('Laughing Out Loud')
#
# def col():
#     print('Crying Out Loud')
#
# def sol():
#     print('Screaming Out Loud')
#
# def pol():
#     print('Passed Out Loud')

# save as outloud.py
# save in .../site-packages
# at work this is /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages
# open a new python file

# import outloud
# call it using outloud.lol()

# from outloud import lol
# call it using lol()


# ---------------------------------------------------------------------------------------------- #
# FUNCTION ARGUMENTS should be intuitive to use
# def func(positional, keyword=value, *args, **kwargs):
#     pass
# 1) Positional = arguments are mandatory and have no default values. (
# 2) Keyword = arguments are optional and have default values.
# 3) args = arbitrary argument list is optional and has no default values. *
# 4) kwargs =  arbitrary keyword argument dictionary is optional and has no default values.

from pprint import pprint

# Positional arguments
def my_dinner(protein, side1, side2):
    return {'Protein': protein, 'Side1': side1, 'Side2': side2}
pprint(my_dinner('Chicken', 'Broccoli', 'Potatoes'))


# Keyword arguments
def my_dinner(protein='Steak', side1='Potatoes', side2='Asparagus'):
    return {'Protein': protein, 'Side1': side1, 'Side2': side2}
# Notice keyword arg side2(Asparagus) is added when only 2 of 3 paramaters used
pprint(my_dinner('Chicken', 'Rice'))
# {'Protein': 'Chicken', 'Side1': 'Rice', 'Side2': 'Asparagus'}


# Positional AND Keyword arguments
def my_dinner(restaurant, protein, *sides, **drinks):
    print('\nReceipt: \n')
    return {'Restaurant': restaurant, 'Protein': protein, 'Sides': sides, 'Drinks': drinks}
pprint(my_dinner('subway', 'chicken', 'rice', 'beans', beer='amber', wine='merlot', other='water'))


# ---------------------------------------------------------------------------------------------- #
# FUNCTION with mixed arguments
# def suspect(height_ft, weight_lbs, ethnicity='unknown'):
#     return {'Height': height_ft, 'Weight': weight_lbs, 'Ethnicity': ethnicity}
# print(suspect(5.11, 180))         # 2 arguments given, so a default ethnicity parameter will be added
# print(suspect(6.2, 300, 'white')) # if you give all 3 arguments, default is NOT used


# ---------------------------------------------------------------------------------------------- #
# FUNCTION
# def ask_ok(question, retries=4, complaint='yes or no, please'):
#     while True:
#         ok = (input(question))
#         if ok in ('yes', 'Yes', 'YES'):
#             print(ok.title(), 'Please!')
#             return True
#         if ok in ('no', 'No', 'NO'):
#             print(ok.title(), 'Thanks!')
#             return False
#         else:
#             print(complaint)
#         retries -= 1
#         if retries < 0:
#             raise OSError('Uncooperative jerk!')
# print(dir())  # Notice that our function 'ask_ok' is listed in dir() now.
# ask_ok('Do you like me? ', 2, 'I Accept = "yes" or "no"')


# ---------------------------------------------------------------------------------------------- #
# FUNCTION that makes a dictionary
# def myDict(x, y):
#     return {'x': x, 'y': y}
# print(myDict('Brett', 'Shaina'))


# import sys
#
# def ask_ok(question, retries=4, complaint='yes or no'):
#     while True:
#         ok = (input(question))
#         if ok in ('yes', 'Yes', 'YES'):
#             print('Are you 100% sure?')
#             return True
#         if ok in ('no', 'No', 'NO'):
#             print(ok.title(), '?'.lstrip(), "You're not very adventurous...")
#             return False
#         else:
#             print('\n---', complaint, '---')
#         retries -= 1
#         print(retries, 'more attempts..\n')
#         if retries == 0:
#             print("This isn't working.. good-bye!")
#             sys.exit()
# ask_ok('Are you ready for this?  ')  # <----  function call


# ---------------------------------------------------------------------------------------------- #
# FUNCTIONS
# # GATHER POSITIONAL ARGUMENTS WITH *
# def printArgs(*args, **kwargs):
#     return 'Positional Arguments Found! : ', args
#     return 'Keyword Arguments Found! : ', kwargs

# printArgs('AEIOU', 'AND', 'SOMETIMES', 'Y')

# ---------------------------------------------------------------------------------------------- #
# FUNCTIONS
# def gatherArgsInList(*args):
#     result = []
#     result.append(args)
#     return result
# print(gatherArgsInList('hello', 'I am Brett', 'I am', 38))
# [('hello', 'I am Brett', 'I am', 38)]
# print(result) # Causes an error because "result" is NOT a global variable
# # NameError: name 'result' is not defined

# ---------------------------------------------------------------------------------------------- #
# FUNCTIONS
# def kaydenisms(*args):
#     print('Funny things Kayden says:\n', args)
# x = kaydenisms('garbo truck', 'I yuh yuh', 'alrrrighty')
# print(type(x))
# # <class 'NoneType'>
# # ('garbo truck', 'I yuh yuh', 'alrrrighty')

# ---------------------------------------------------------------------------------------------- #
# FUNCTIONS
# # GATHER KEYWORD ARGUMENTS WITH **
# def print_kwargs(**kwargs):
#     print('Keyword arguments:', kwargs)
# print(print_kwargs(dad='Brett', mom='Shaina', son='Kayden'))
# # Keyword arguments: {'son': 'Kayden', 'dad': 'Brett', 'mom': 'Shaina'}
# # None

# ---------------------------------------------------------------------------------------------- #
# FUNCTIONS
# def extendList(val, mylist=[]):
#     mylist.append(val)
#     return mylist
# print(extendList('Hello'))  # ['Hello']
# print(extendList('Everyone'))  # ['Hello', 'Everyone']

# IMPORTANT NOTES:


# ---------------------------------------------------------------------------------------------- #
# LAMBDA FUNCTION
# ---------------------------------------------------------------------------------------------- #
# A simple 1 line function
# does not use def or return function, these are implicit
# They are syntactically restricted to a single expression.
# Semantically, they are just syntactic sugar for a normal function definition.
# WHEN TO USE LAMBDA:  Lambda functions can be used wherever function objects are required.


# ---------------------------------------------------------------------------------------------- #
# LAMBDA if we want to double x
# dubx = lambda x: 2 * x                 # where "x": is the parameter and '2 * x' is the return
# print(dubx(12))                        # 24


# ---------------------------------------------------------------------------------------------- #
# LAMBDA vs. FUNCTION if we want to add x and y
# x_y_added = lambda x, y: x + y         # where 'x, y': are the parameters and 'x + y' is the return
# print(x_y_added(3, 4))                 # 7
#
# def x_y_added(x, y):
#     return x + y
# print(x_y_added(3, 4))                 # 7


# ---------------------------------------------------------------------------------------------- #
# LAMBDA vs. FUNCTION if we want the max of x, y and assign to mx
# mx = lambda x, y: x if x > y else y    # where 'x, y': are the parameters and x if x > y else y is the return
# print(mx(8, 5))                        # 8
#
# def mx(x, y):
#     if x > y:
#         return x
#     else:
#         return y
# print(mx(8, 5))                        # 8


# ---------------------------------------------------------------------------------------------- #
# LAMBDA in a function
# def first_tier(a):
#     return lambda x: x / a
#
# halved = first_tier(2)     # the argument "2" corresponds to the parameter "a" in x / a
# print(halved(24))          # the argument "6" corresponds to the parameter "x" in x / a
# 12.0

# ---------------------------------------------------------------------------------------------- #
# FUNCTION
# def extendList(val, list=[]):
#     list.append(val)
#     return list

# def extract_from_tag(tag, line):
#     opener = "<" + tag + ">"
#     closer = "</" + tag + ">"
#     try:
#         i = line.index(opener)
#         start = i + len(opener)
#         j = line.index(closer, start)
#         return line[start:j]
#     except ValueError:
#         return None

# ---------------------------------------------------------------------------------------------- #
# GENERATOR FUNCTIONS
# ---------------------------------------------------------------------------------------------- #

# "yield" sends a result back to the caller, and remembers where it left off.


# def myrange(first=0, last=10, step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step
# genObj = myrange(15, 100, 15)  # this is the generator object

# ----- Option 1 to iterate ----- #
# for x in genObj:
#     print(x, end=' ')    # 15 30 45 60 75 90

# ----- Option 2 to iterate ----- #
# wrapList = list(genObj)
# print(wrapList)        # [15, 30, 45, 60, 75, 90]