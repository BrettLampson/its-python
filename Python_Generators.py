
from pprint import pprint

# ---------------------------------------------------------------------------------------------- #
# LIST COMPS VS. GENERATORS AND GENERATOR EXPRESSIONS
# LIST COMPS are a one-trick pony: they build lists.  To fill other sequence types use GENEXPS
# The mere presence of the yield statement in a function turns it into a generator

# ---------------------------------------------------------------------------------------------- #
# CARTESIAN PRODUCT (means built from all items) aka 'All Scenarios'

# colors = ['black', 'white']
# sizes = ["s", "m", "l"]
#
# list_comp = [(color, size) for color in colors for size in sizes]
# pprint(list_comp)
# print('-'*50)


# ---------------------------------------------------------------------------------------------- #
# CHANGING THE ORDER OF (COLOR, SIZE) TO (SIZE, COLOR) CHANGES RETURN ORDER

# list_comp2 = [(size, color) for color in colors for size in sizes]
# pprint(list_comp2)
# print('-'*50)


# ---------------------------------------------------------------------------------------------- #
# GENERATOR EXPRESSIONS save memory because they yield items 1 by 1 using interator protocol.
# Same syntax as listcomps, but use () instead of [].

# symbols = '^@%#*%$'
# t = ((symbol, ord(symbol)) for symbol in symbols)
# # print(next(t))
# for element in t:
#     print(element)
#
# print(type(t)) # <class 'generator'>


# ---------------------------------------------------------------------------------------------- #
# CREATING A CUSTOM ITERATION PATTERN that’s different than the usual built- in functions
# GENERATOR FUNCTION

# def frange(start, stop, increment):
#     x = start
#     while x < stop:
#         yield x
#         x += increment


# ---------------------------------------------------------------------------------------------- #
# Find the index of every word in a string
# GENERATOR FUNCTION

# def index_words_iter(text):
#     if text:
#         yield 0
#     for index, letter in enumerate(text):
#         if letter == ' ':
#             yield index + 1


# ---------------------------------------------------------------------------------------------- #
# GENERATOR EXPRESSION transformation and reduction

# nums = [1, 2, 3, 4, 5]
# s = sum(x * x for x in nums)

# ---------------------------------------------------------------------------------------------- #
# GENERATOR EXPRESSION Determine if any .py files exist in a directory

# import os
# files = os.listdir('/Brett/Dropbox/Python Subjects')
# if any(name.endswith('.py') for name in files):
#     print('There be python!')
# else:
#     print('Sorry, no python.')


# ---------------------------------------------------------------------------------------------- #
# GENERATOR EXPRESSION Output a tuple as CSV
# s = ('ACME', 50, 123.45)
# print(','.join(str(x) for x in s))


# ---------------------------------------------------------------------------------------------- #
# GENERATOR EXPRESSION Data reduction across fields of a data structure

# portfolio = [
#         {'name':'GOOG', 'shares': 50},
#         {'name':'YHOO', 'shares': 75},
#         {'name':'AOL', 'shares': 20},
#         {'name':'SCOX', 'shares': 65}]

# min_shares = min(s['shares'] for s in portfolio)


# ---------------------------------------------------------------------------------------------- #
# GENERATOR EXPRESSION Alternative: Returns {'name': 'AOL', 'shares': 20}

# portfolio = [
#         {'name':'GOOG', 'shares': 50},
#         {'name':'YHOO', 'shares': 75},
#         {'name':'AOL', 'shares': 20},
#         {'name':'SCOX', 'shares': 65}]
#
# min_shares = min(portfolio, key=lambda s: s['shares'])
# print(min_shares)