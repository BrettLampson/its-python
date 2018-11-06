
import os

# ------------------------------------------------------------------------------------------------ #
# SET
# ------------------------------------------------------------------------------------------------ #

# Mutable, Unordered, Iterable
# NOT a sequence

# # WHEN TO USE A SET:
# 1) Removing duplicates from a sequence
# 2) Fast Membership Testing (in, not in)
# 3) Ensure we don't process duplicate data
# 4) Comparisons using (union, intersect, etc) operations
# 5) Can be dictionary values ----- most common use of a set ----- key: {'set', 'values', 'go', 'here'}
# 6) When order doesn't matter


# IMPORTANT NOTES:
# Hashable objects may be added to sets; meaning any objects having __hash__() special method.
# All immutable data types, such as float, frozenset, int, str, and tuple can be added to sets.
# Mutable data types such as dict, list, and set are NOT hashable and can't be added to sets.


# ------------------------------------------------------------------------------------------------ #
# SET METHODS
# ------------------------------------------------------------------------------------------------ #

# add(), clear(), copy(), difference(), difference_update(), discard()
# intersection(), intersection_update(),isdisjoint(), issubset(), issuperset()
# pop(), remove(), symmetric_difference(), symmetric_difference_update(), union(), update()


# ------------------------------------------------------------------------------------------------ #
# S.add()

# S = {7.12, 'Brett', 0, -34, ('66', 99)}
# S.add('xoxo')
# print(S)     # {0, 'xoxo', 7.12, 'Brett', ('66', 99), -34}


# ------------------------------------------------------------------------------------------------ #
# S.clear()

# S = {7.12, 'Brett', 0, -34, ('66', 99)}
# S.clear()    # S is now an empty set
# print(S)


# ------------------------------------------------------------------------------------------------ #
# S.copy()

# S = {7.12, 'Brett', 0, -34, ('66', 99)}
# S1 = S.copy()   # Shallow copy
# print(S1)       # {0, ('66', 99), 'Brett', -34, 7.12}
# print(S == S1)  # True


# ------------------------------------------------------------------------------------------------ #
# S.difference()

# S = {1, 2, 3, 4, 5, 6}
# S2 = {2, 4, 6}
# S3 = S.difference(S2)  # Creates a new set in memory of S that is NOT IN S2
# S3 = S - S2            # Pythonic
# print(S3)              # {1, 3, 5}
# def difference(l1):
#     """ return the list with duplicate elements removed """
#     return list(set(l1))


# ------------------------------------------------------------------------------------------------ #
# S.difference_update()

# S = {1, 2, 3, 4, 5, 6}
# S2 = {2, 4, 6}
# S.difference_update(S2)   # If it's in S2 then remove it from S
# S -= S2                   # Pythonic AND faster than S.difference() because it DOES NOT create a new set
# print(S)                  # {'Brett', ('66', 99), -34}


# ------------------------------------------------------------------------------------------------ #
# S.discard()

# Remove an element from a set.
# If the element is not a member, do nothing.
# my_set = {1, 3, 4, 5, 6}
# my_setS.discard(3)
# print(my_set)  # {1, 4, 5, 6}
# my_set.discard(999)
# print(my_set)  # {1, 4, 5, 6}


# ------------------------------------------------------------------------------------------------ #
# S.intersection()

# Returns ALL items in BOTH sets
# S = {1, 2, 3, 4, 5, 6}
# S2 = {2, 4, 6}
# S3 = S.intersection(S2)
# S3 = S & S2
# print(S3)  # {2, 4, 6}
# def intersection(l1, l2):
#     """ return the intersection of two lists """
#     return list(set(l1) & set(l2))


# ------------------------------------------------------------------------------------------------ #
# S.intersection_update()

# Update a set with the intersection of itself and another.
# S = {1, 2, 3, 4, 5, 6}
# S2 = {2, 4, 6}
# S.intersection_update(S2)
# S &= S2
# print(S)


# ------------------------------------------------------------------------------------------------ #
# S.isdisjoint()

# Return True if two sets have a null intersection.
# HE = {'yo', 'mtv', 'raps'}
# SHE = {2, 'di', 'yo'}
# print(S.isdisjoint(S2))  # False because 'yo' is in both.


# ------------------------------------------------------------------------------------------------ #
# S.issubset()

# S.issubset(S2)  # Return True if S is in S2
# S <= S2
# S = {20, 40, 80, 120}
# S2 = {20, 40, 80, 100, 120, 140}
# print(S2.issubset(S))  # True


# ------------------------------------------------------------------------------------------------ #
# S.issuperset()

# S >= S2  # Return True if S2 is in S
# S = {20, 40, 80, 100}
# S2 = {20, 40, 80}
# print(S >= S2)  # True


# ------------------------------------------------------------------------------------------------ #
# S.pop()

# Remove and return an arbitrary set element.
# Raises KeyError if the set is empty.
# S = {20, 40, 80, 100}
# print(S.pop())
# print(S)


# ------------------------------------------------------------------------------------------------ #
# S.remove()

# Remove an element from a set; it must be a member.
# If the element is not a member, raise a KeyError.
# S = {20, 40, 80, 100}
# S.remove(80)
# print(S)


# ------------------------------------------------------------------------------------------------ #
# S.symmetric_difference()

# Return all unique values when comparing both sets.
# A = {1, 2, 3, 4}
# B = {3, 4, 5}
# print(A.symmetric_difference(B))
# print(A ^ B)  #  {1, 2, 3, 6, 7, 8}


# ------------------------------------------------------------------------------------------------ #
# S.symmetric_difference_update()

# Update a set with the symmetric difference of itself and another.
# A = {1, 2, 3, 4}
# B = {3, 4, 5}
# print(A.symmetric_difference_update(B))  # None
# A.symmetric_difference_update(B)
# print(A.symmetric_difference_update(B))
# print(A)    # {1, 2, 3, 6, 7, 8}


# ------------------------------------------------------------------------------------------------ #
# S.union()

# Return/combine all elements of both sets.
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# A | B  # Union  {1, 2, 3, 4, 5, 6, 7, 8}
# print(S)
# def union(l1, l2):
#     """ return the union of two lists """
#     return list(set(l1) | set(l2))


# ------------------------------------------------------------------------------------------------ #
# S.update()

# Update a set with the union of itself and others.
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# A.update(B)
# print(A)  # {1, 2, 3, 4, 5, 6, 7, 8}


# ------------------------------------------------------------------------------------------------ #
# Union, Intersection, Difference, Symmetric Difference

# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# A | B  # Union  {1, 2, 3, 4, 5, 6, 7, 8}
# A & B  # Intersection {4, 5}
# A - B  # Difference {1, 2, 3}
# A ^ B  # Symmetric Difference {1, 2, 3, 6, 7, 8}


# ------------------------------------------------------------------------------------------------ #
# SET METHODS END
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
# CREATE a set

# s = set()                                          # Empty set
# s = {22, 33, 44, (55, 66)}                         # Set
# s = set(['lol', 'omg', 99, 34.5, 99])              # from a List
# s = set((7, 'Brett', 7, -34, ('66', 99), 7))       # from a Tuple
# dict = {'Brett': 38, 'Shaina': 34, 'Kayden': 3}    # Dictionary for below
# dict_keys = set(dict)                              # from a Dictionary (Returns keys only)
# dict_values = set(dict.values())                   # from a Dictionary (Returns values only)
# print(dict_keys, dict_values)


# ------------------------------------------------------------------------------------------------ #
# Membership testing "in" and "not in"
#
# s = {7, 'Brett', 0, -34, ('66', 99), 'Dog'}
# print(('66', 99) in s)
# True
# print(-34 not in s)
# # False


# ------------------------------------------------------------------------------------------------ #
# SET COMPREHENSION that multiplies each item by 10

# A = {1, 2, 3, 4, 5}
# B = {x*10 for x in A}
# print(B)  # {40, 10, 20, 50, 30}


# ------------------------------------------------------------------------------------------------ #
# SET COMPREHENSION that returns all files in cwd that start with 'subj' name

# import os
# print(os.getcwd())
# my_cwd = os.getcwd()
# cwdList = os.listdir(my_cwd)
# for x in cwdList:
#     if x.lower().startswith("subj"):
#         print(x)


# ------------------------------------------------------------------------------------------------ #
# SET Comprehension

# # Printing ODD numbers ( % 2 == 1)
# odd = {item for item in range(10) if item % 2 == 1}
# print(odd)
# # {1, 3, 5, 9, 7}

# ------------------------------------------------------------------------------------------------ #
# Printing EVEN numbers ( % 2 == 0)

# even = {item for item in range(10) if item % 2 == 0}
# print(even)
# # {0, 8, 2, 4, 6}

# ------------------------------------------------------------------------------------------------ #
# SET Iteration

# {expression for item in iterable}
# {expression for item in iterable if condition}
# # Just like list comprehensions, the iterable used in a set comprehension can
# # itself be a set comprehension (or any other kind of comprehension), so quite
# # sophisticated set comprehensions can be created.
# set comprehension that returns all files in cwd that end in .htm or html

# print(os.getcwd())
# myCwd = os.getcwd()
# os.listdir(myCwd)
# cwdList = os.listdir(myCwd)
# html = {x for x in cwdList if x.lower().endswith((".py", ".html"))}
# print(html, ">>> THIS is a", type(html))


# ------------------------------------------------------------------------------------------------ #
# SET MEMBERSHIP TESTING THEN DOING SOMETHING
# keys are named mixed drinks, values are ingredients as sets

# drinks = {
#     'black russian': {'vodka', 'kahlua'},
#     'martini': {'vodka', 'vermouth'},
#     'manhattan': {'rye', 'vermouth', 'bitters'}
# }
#
# # drinks that contain vodka
# for name, contents in drinks.items():
#     if 'vodka' in contents:
#         print(name)
#
# # drinks that contain kahlua OR bitters
# for name, contents in drinks.items():
#     if contents & {'kahlua', 'bitters'}:
#         print(name)


# ------------------------------------------------------------------------------------------------ #
# FROZEN SETS

# Frozen sets are immutable objects that only support methods and operators that produce
# a result without affecting the frozen set or sets to which they are applied.
