print()

# ---------------------------------------------------------------------------------------------- #
# IF / ELIF / ELSE
# ---------------------------------------------------------------------------------------------- #
# If and Else statements ONLY check whether a condition is True or False.
# You can test True, False, ==, !=, <, >, <=, >=, in, not in... and expressions that evaluate to True or False
# Boolean operators = and, or, not
# Indentation determines how the if and else sections are paired.
# Note:  boolean operators have lower "precedence" than the chunks of code that
# ...they're comparing.  This means the chunks are calculated first, then compared.
# ...The best way to avoid "precedence" confusion is add parenthesis (3 < x) and (x > 9).
# x = 5
# y = 9
# print(3 < x and x > 9)
# print((3 < x) and (x > 9))


# True and True    # True
# True and False   # False
# False and False  # False
# True or False    # True
# False or True    # True

# x or y	   # if x is false, then y, else x (It only evaluates the second argument if the first one is false.)
# x and y	   # if x is false, then x, else y (It only evaluates the second argument if the first one is true.)
# not x	       # if x is false, then True, else False


# ---------------------------------------------------------------------------------------------- #
# If the element isn't a boolean.
# The following are "falsy"

# False    # boolean False
# None     # null
# 0        # zero integer
# 0.0      # 0.0 float
# ''       # empty string
# []       # empty list
# ()       # empty tuple
# {}       # empty dict
# set()    # empty set
# range(0) # empty range


# ---------------------------------------------------------------------------------------------- #
# ANY() AND ALL()
# +-----------------------------------------+---------+---------+
# |                                         |   any   |   all   |
# +-----------------------------------------+---------+---------+
# | All Truthy values                       |  True   |  True   |
# +-----------------------------------------+---------+---------+
# | All Falsy values                        |  False  |  False  |
# +-----------------------------------------+---------+---------+
# | One Truthy value (all others are Falsy) |  True   |  False  |
# +-----------------------------------------+---------+---------+
# | One Falsy value (all others are Truthy) |  True   |  False  |
# +-----------------------------------------+---------+---------+
# | Empty Iterable                          |  False  |  True   |
# +-----------------------------------------+---------+---------+


# ANY() Return True if any element of the iterable is true. If the iterable is empty, return False.
# ALL() Return True if all elements of the iterable are true (or if the iterable is empty).
# L = [1, 16, 0, 7, 0]
# print(any(L))  # True
# print(all(L))  # False


# ---------------------------------------------------------------------------------------------- #
# BREAK / CONTINUE
# "Break" jumps out of the closest enclosed loop and executes the next code block outside of the loop.
# Generally avoid break statements, use it only when it makes your code simpler or clearer.
# "Continue" jumps immediately to the loop condition, thus continuing with the next iteration of the loop.
# "pass" does nothing at all: an empty statement placeholder.


# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

# for num in range (2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found a number", num)


# ---------------------------------------------------------------------------------------------- #
# EXAMPLES

# # order is important, otherwise you get mixed results.
# age = 60
# if age <= 4:
#     price = 0.00
# elif age < 60:
#     price = 15.00
# else:
#     price = 10.00
# print('Your admission cost is $', str(price))
# # Your admission cost is $ 10.00


# ---------------------------------------------------------------------------------------------- #
# CONDITIONAL EXPRESSION

# food = input('What is your fav food?: ')
# food = food.lower()
# print('Yuck' if food == 'olives' else 'Yummy')


# ---------------------------------------------------------------------------------------------- #
# GENERAL SYNTAX

# while True:
#     item = get_next_item()
#     if not item:
#         break
#     process_item(item)"



# ---------------------------------------------------------------------------------------------- #
# CRAPS GAME

# dice = die_1 + die_2
# if dice in (2, 3, 12):
#     game.craps()
# elif dice in (7, 11):
#     game.winner()
# elif dice in (4, 5, 6, 8, 9, 10):
#     game.point(die)
#
# # else crash option used as a catch-all
# else:
#     raise Exception('Design Problem Here: not all conditions accounted for')


# ---------------------------------------------------------------------------------------------- #
# ASK FOR UN AND PW
# while True:
#     name = input('What is the access ID? ')
#     if name != '007':
#         print('You do not have access here, begone...')
#         continue
#     pw = input('\nHello 007, what is the password? ')
#     if pw == 'swordfish':
#         break  # WIP needing to get ask only for PW again.
# print('Access Granted...')
