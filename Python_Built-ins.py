

# ------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------ #
# BUILT-INS -------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------ #

# abs(), all(), any(), ascii(), bin(), bool(), bytearray(), bytes(), callable(), chr(), 
# classmethod(), compile(), complex(), delattr(), dict(), dir(), divmod(), enumerate(), eval(), 
# exec(), filter(), float(), format(), frozenset(), getattr(), globals(), hasattr(), hash(), help(),
# hex(), id(), input(), int(), isinstance(), issubclass(), iter(), len(), list(), locals(), map(),
# max(), memoryview(), min(), next(), object(), oct(), open(), ord(), pow(), print(), property(), 
# range(), repr(), reversed(), round(), set(), setattr(), slice(), sorted(), staticmethod(), str(), 
# sum(), super(), tuple(), type(), vars(), zip()


# ------------------------------------------------------------------------------------------------ #
# abs(x)

# # Return the absolute value of a number. The argument may be an integer or a floating point number.
# print(abs(-4.44))  # 4.44


# ------------------------------------------------------------------------------------------------ #
# all(iterable)

# # Return True if all elements of the iterable are true (or if the iterable is empty).
# def all(iterable):
#     for item in iterable:
#         if not item:              # look up truthy and falsy
#             return False
#     return True

# print(all([3, 2.99, -56, 0.00]))  # False


# ------------------------------------------------------------------------------------------------ #
# any(iterable)

# # Return True if any element of the iterable is true. If the iterable is empty, return False.
# print(any({3, 11, 'nothing', 0}))  # True


# ------------------------------------------------------------------------------------------------ #
# ascii(object)

# As repr(), return a string containing a printable representation of an object, but escape the
# non-ASCII characters in the string returned by repr() using \x, \u or \U escapes.
# This generates a string similar to that returned by repr() in Python 2.
# x = ['something', 'nothing', '€ Euro']
# print(ascii(x))  # ['something', 'nothing', '\u20ac Euro']
# print(repr(x))   # ['something', 'nothing', '€ Euro']


# ------------------------------------------------------------------------------------------------ #
# bin(x)

# Convert an integer number to a binary string prefixed with “0b”. The result is a valid
# Python expression. If x is not a Python int object, it has to define an __index__() method
# that returns an integer.
# print(bin(3))    # 0b11
# print(bin(4))    # 0b100


# ------------------------------------------------------------------------------------------------ #
# bool(x)
# Return a Boolean value, i.e. one of True or False. x is converted using the standard truth
# testing procedure. If x is false or omitted, this returns False; otherwise it returns True.
# x = 4
# y = 0
# print(bool(x))  # True
# print(bool(y))  # False

# ------------------------------------------------------------------------------------------------ #
# breakpoint(*args, **kws)
# This function drops you into the debugger at the call site. Specifically, it calls
# sys.breakpointhook(), passing args and kws straight through. By default, sys.breakpointhook()
# calls pdb.set_trace() expecting no arguments. In this case, it is purely a convenience function
# so you don’t have to explicitly import pdb or type as much code to enter the debugger. However,
# sys.breakpointhook() can be set to some other function and breakpoint() will automatically call
# that, allowing you to drop into the debugger of choice.


# ------------------------------------------------------------------------------------------------ #
# bytearray([source[, encoding[, errors]]])
# Return a new array of bytes. The bytearray class is a mutable sequence of integers in the
# range 0 <= x < 256. It has most of the usual methods of mutable sequences, described in
# Mutable Sequence Types, as well as most methods that the bytes type has, see Bytes and
# Bytearray Operations.

# x = [0, 1, 2, 3, 4, 5]
# print(bytearray(x))  # bytearray(b'\x00\x01\x02\x03\x04\x05')


# ------------------------------------------------------------------------------------------------ #
# bytes([source[, encoding[, errors]]])
# Return a new “bytes” object, which is an immutable sequence of integers in the range 0 <= x < 256.
# bytes is an immutable version of bytearray – it has the same non-mutating methods and the same
# indexing and slicing behavior.
# Accordingly, constructor arguments are interpreted as for bytearray().
# Bytes objects can also be created with literals, see String and Bytes literals.


# ------------------------------------------------------------------------------------------------ #
# callable(object)
# Return True if the object argument appears callable, False if not. If this returns true, it is
# still possible that a call fails, but if it is false, calling object will never succeed.
# Note that classes are callable (calling a class returns a new instance); instances are
# callable if their class has a __call__() method.


# ------------------------------------------------------------------------------------------------ #
# chr(i)
# Return the string representing a character whose Unicode code point is the integer i.
# For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'.
# This is the inverse of ord().
# The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16).
# ValueError will be raised if i is outside that range.


# ------------------------------------------------------------------------------------------------ #
# classmethod()


# ------------------------------------------------------------------------------------------------ #
# compile()


# ------------------------------------------------------------------------------------------------ #
# complex()


# ------------------------------------------------------------------------------------------------ #
# delattr(object, name)
# This is a relative of setattr(). The arguments are an object and a string. The string must be
# the name of one of the object’s attributes. The function deletes the named attribute, provided
# the object allows it. For example, delattr(x, 'foobar') is equivalent to del x.foobar.


# ------------------------------------------------------------------------------------------------ #
# dict()


# ------------------------------------------------------------------------------------------------ #
# dir()


# ------------------------------------------------------------------------------------------------ #
# divmod(a, b)
# Take two (non complex) numbers as arguments and return a pair of numbers consisting of their
# quotient and remainder when using integer division. With mixed operand types, the rules for
# binary arithmetic operators apply. For integers, the result is the same as (a // b, a % b).
# For floating point numbers the result is (q, a % b), where q is usually math.floor(a / b)
# but may be 1 less than that. In any case q * b + a % b is very close to a, if a % b is
# non-zero it has the same sign as b, and 0 <= abs(a % b) < abs(b).

# print(divmod(12, 4))  # (3, 0)


# ------------------------------------------------------------------------------------------------ #
# enumerate(iterable, start=0)
# Return an enumerate object. iterable must be a sequence, an iterator, or some other object
# which supports iteration. The __next__() method of the iterator returned by enumerate()
# returns a tuple containing a count (from start which defaults to 0) and the values obtained
# from iterating over iterable.

# s = 'string'
# t = ('t', 'u', 'p', 'l', 'e')
# l = ['l', 'i', 's', 't']
# st = {'s', 'e', 't'}
# d = {'d': 0, 'i': 1, 'c': 2, 't': 3}

# # specifing a second argument starts counting at that number
# for item in enumerate(d, 1):
#     print(item)


# ------------------------------------------------------------------------------------------------ #
# eval()


# ------------------------------------------------------------------------------------------------ #
# exec()


# ------------------------------------------------------------------------------------------------ #
# filter()


# ------------------------------------------------------------------------------------------------ #
# float()


# ------------------------------------------------------------------------------------------------ #
# format()


# ------------------------------------------------------------------------------------------------ #
# frozenset()


# ------------------------------------------------------------------------------------------------ #
# getattr()


# ------------------------------------------------------------------------------------------------ #
# globals()


# ------------------------------------------------------------------------------------------------ #
# hasattr()


# ------------------------------------------------------------------------------------------------ #
# hash()


# ------------------------------------------------------------------------------------------------ #
# help()


# ------------------------------------------------------------------------------------------------ #
# hex()


# ------------------------------------------------------------------------------------------------ #
# id()


# ------------------------------------------------------------------------------------------------ #
# input()


# ------------------------------------------------------------------------------------------------ #
# int()


# ------------------------------------------------------------------------------------------------ #
# isinstance()


# ------------------------------------------------------------------------------------------------ #
# issubclass()


# ------------------------------------------------------------------------------------------------ #
# iter()


# ------------------------------------------------------------------------------------------------ #
# len()


# ------------------------------------------------------------------------------------------------ #
# list()


# ------------------------------------------------------------------------------------------------ #
# locals()


# ------------------------------------------------------------------------------------------------ #
# map()


# ------------------------------------------------------------------------------------------------ #
# max()


# ------------------------------------------------------------------------------------------------ #
# memoryview()


# ------------------------------------------------------------------------------------------------ #
# min()


# ------------------------------------------------------------------------------------------------ #
# next()


# ------------------------------------------------------------------------------------------------ #
# object()


# ------------------------------------------------------------------------------------------------ #
# oct()


# ------------------------------------------------------------------------------------------------ #
# open()


# ------------------------------------------------------------------------------------------------ #
# ord()


# ------------------------------------------------------------------------------------------------ #
# pow()


# ------------------------------------------------------------------------------------------------ #
# print()


# ------------------------------------------------------------------------------------------------ #
# property()


# ------------------------------------------------------------------------------------------------ #
# range()


# ------------------------------------------------------------------------------------------------ #
# repr()


# ------------------------------------------------------------------------------------------------ #
# reversed()


# ------------------------------------------------------------------------------------------------ #
# round()


# ------------------------------------------------------------------------------------------------ #
# set()


# ------------------------------------------------------------------------------------------------ #
# setattr()


# ------------------------------------------------------------------------------------------------ #
# slice()

# foo = 'abcdefghijklmnopqrstuvwxyz1234567890'
# bar = ['one', 'two', 'three', 'four', 'five']
#
# alphabet = slice(0, 26)   # abcdefghijklmnopqrstuvwxyz
# numbers = slice(26, 38)   # 1234567890
# bar_none = slice(1, 4)    # ['two', 'three', 'four']
#
# print(alphabet)

# for i in alphabet:
#     print(i)

# ------------------------------------------------------------------------------------------------ #
# sorted()


# ------------------------------------------------------------------------------------------------ #
# staticmethod()


# ------------------------------------------------------------------------------------------------ #
# str()


# ------------------------------------------------------------------------------------------------ #
# sum()


# ------------------------------------------------------------------------------------------------ #
# super()


# ------------------------------------------------------------------------------------------------ #
# tuple()


# ------------------------------------------------------------------------------------------------ #
# type()


# ------------------------------------------------------------------------------------------------ #
# vars()


# ------------------------------------------------------------------------------------------------ #
# zip()