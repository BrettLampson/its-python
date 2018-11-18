
# ------------------------------------------------------------------------------------------------ #
# STRINGS
# ------------------------------------------------------------------------------------------------ #

# Immutable, Iterable
# Python 3 strings are immutable sequences of Unicode characters
# Python 3 bytes object is a sequence of integers values from 0 to 256.
# Use bytes when dealing with binary data, such as reading from a binary data file


# ------------------------------------------------------------------------------------------------ #
# IMPORT
# ------------------------------------------------------------------------------------------------ #

import string
import re
import unicodedata
import collections
import sys

# ------------------------------------------------------------------------------------------------ #
# STRING ESCAPE SEQUENCES

# \' single quote
# \" double quote
# \a bell
# \f formfeed
# \n linefeed
# \r carriage return
# \t horizontal tab
# \b backspace
# \v Vertical tab
# \\ the backslash character
# \u, \U, \N{} Unicode Character
# \x hex-encoded byte


# ------------------------------------------------------------------------------------------------ #
# STRING METHODS
# ------------------------------------------------------------------------------------------------ #
# capitalize(), casefold(), center(), count(), encode(), endswith(), expandtabs(),
# find(), format(), format_map(), index(), isalnum(), isalpha(), isdecimal(), isdigit(),
# isidentifier(), islower(), isnumeric(), isprintable(), isspace(), istitle(), isupper(),
# join(), ljust(), lower(), lstrip(), maketrans(), partition(), replace(), rfind(),
# rindex(), rjust(), rpartition(), rsplit(), rstrip(), split(), splitlines(), startswith(),
# strip(), swapcase(), title(), translate(), upper(), zfill()
# ------------------------------------------------------------------------------------------------ #
# s.capitalize()
# Return a copy of the string with its first character capitalized and the rest lowercase.

# s = 'Brad lampson'
# print(s.capitalize())
# Brad lampson


# ------------------------------------------------------------------------------------------------ #
# s.casefold()
# Casefold is similar to lowercase but more aggressive

# s = 'Brad lampson'
# print(s.casefold())
# Brad lampson


# ------------------------------------------------------------------------------------------------ #
# s.center(width[, fillchar])
# Return centered in a string of length width.
# Padding is done using the fillchar (default is an ASCII space)

# s = 'Brad lampson'
# print(s.center(21, '-'))
#  ----Brad lampson----


# ------------------------------------------------------------------------------------------------ #
# s.count(sub[, start[, end]])
# Counts the 'r' values from index "start" 1 to "end" 18

# s = 'mississippi'
# print(len(s))              # 11
# print(s.count('s', 1, 7))  # 4
# print(s.count('p'))        # 2


# ------------------------------------------------------------------------------------------------ #
# s.encode(encoding="utf-8", errors="strict")
# Return an encoded version of the string as a bytes object

# s = "Babe Ruth, Yankees"
# print(s.encode('utf-8'))
# b'Babe Ruth, Yankees'


# ------------------------------------------------------------------------------------------------ #
# s.endswith(suffix[, start[, end]])

# s = "Babe Ruth, Yankees"
# print(s.endswith('Yankees'))       # True
# print(len(s))                      # 18
# print(s.endswith('kees', 11, 18))  # True

# OR
# If you need to check against multiple choices,
# simply provide a tuple of possibilities to startswith() or endswith():


# filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
# check_filenames = [name for name in filenames if name.endswith(('.c', '.h'))]
# print(check_filenames)  # ['foo.c', 'spam.c', 'spam.h']
#
# check_any = any(name.endswith('.py') for name in filenames)
# print(check_any)        # True
#
# If you happen to have the choices specified in a list or set,
# just make sure you convert them using tuple() first.  Tuple is req'd

# ------------------------------------------------------------------------------------------------ #
# s.expandtabs(tabsize=8)
# noticeable only if \t is in string. Multiples of 8 or number specified
# Return a copy of the string where all tab characters are replaced by one or more spaces (8 default)

# s = "Babe Ruth\tYankees"
# print(s.expandtabs(3))
# Babe Ruth   Yankees


# ------------------------------------------------------------------------------------------------ #
# s.find(sub[, start[, end]])
# Return the FIRST index of substring 'sub' found within the slice.

# s = "Babe Ruth, Yankees"
# print(s.find('eee'))  # -1 ValueErrorraised, which means no string was found.
# print(s.find('e'))    # 3 is the index of the first occurrence, no other occurrences are returned.


# ------------------------------------------------------------------------------------------------ #
# s.format(*args, **kwargs)

# f = 7.03
# s = 'upper'
# n = 42
# s1 = s + ' {bling} and lower {0}'.format('blah', bling='BLAH')
# print(s1)
# upper BLAH and lower blah

# a = '{} {} {}'.format(f, s, n)
# 7.03 string 42

# b = '{2} {0} {1}'.format(f, s, n)
# print(b)
# 42 7.03 string

# b1 = '{0} x {0} = {1}'.format(3, 3*3)
# 3 x 3 = 9

# c = '{f} {s} {n}'.format(f='3.07', s=s, n='24')
# print(c)
# 7.03 string 42

# c1 = 'The {animal} waited patiently on the {0}'.format('chair', animal='cat')
# print(c1)

# utensils = ['chopsticks', 'fork', 'shovel']
# power_tools = ['whip', 'stapler', 'long sword', 'bow']
# c3 = 'I use a {0[1]} to eat spaghetti, not a {1[2]}'.format(utensils, power_tools)
# print(c3)
# # I use a fork to eat spaghetti, not a long sword

# # In this dictionary, 0 is d and {1} is OLD CHEESE
# d = {'f': 7.03, 'n': 42, 's': 'string'}
# d1 = '{0[f]} {0[s]} {0[n]} {1}'.format(d, 'OLD CHEESE')  # 7.03 string 42 OLD CHEESE
# print(d1)
# print(type(d.get('f')))

# # Positional arguments
# e = '{0:f} {1:s} {2:d}'.format(f, s, n)  # 7.030000 string 42
# print(e)

# # Named arguments
# f = '{f:f} {s:s} {n:d}'.format(f=7.03, s='string', n=42)  # 7.030000 string 42

# # Specify decimal places
# g = '{0:.3f} {1:s} {2:d}'.format(7.03, 'string', 42)  # 7.030 string 42
# print(a, b, c, d, e, f, g, sep='\n')

# # F-STRINGS, aka "string interpolation"
# name = 'Brad'
# age = '39'
# print(f'My name is {name} and I am {age} years old')
# print('My name is {name} and I am {age} years old')
# print('My name is {name} and I am {age} years old'.format(name='Brad', age='40'))

# # Using **locals() to feed .format()
# one = 'Brad'
# two = 'Python'
# print('{one} likes programming in {two}'.format(**locals()))


# ------------------------------------------------------------------------------------------------ #
# s.format_map(mapping)

# class Default(dict):
#     def __missing__(self, key):
#         return key
# print('{name} was born in {country}'.format_map(Default(name='Guido')))
# Guido was born in country


# ------------------------------------------------------------------------------------------------ #
# s.index(sub[, start[, end]])
# Like find(), but raise ValueError when the substring is not found.

# s = "Babe Ruth, Yankees"
# print(s.index('z'))  # ValueError: substring not found


# ------------------------------------------------------------------------------------------------ #
# s.isalnum
# Return true if all characters in the string are alphanumeric and there is at least one character

# s = "Babe Ruth, Yankees"
# print(s.isalnum())  # False


# ------------------------------------------------------------------------------------------------ #
# s.isalpha()
# Return true if all characters in the string are alphabetic and there is at least one character

# s = "BabeRuthYankees"
# print(s.isalpha())  # False, because of the spaces and the comma ","


# ------------------------------------------------------------------------------------------------ #
# s.isdecimal()
# Return true if all characters in the string are decimal characters and there is at least one character
# Formally a decimal character is a character in the Unicode General Category "Nd"

# s = '314159'
# print(s.isdecimal())  # True   0, 1, 2, 3, 4, 5, 6, 7, 8, 9 are all Base-10 numbers


# ------------------------------------------------------------------------------------------------ #
# s.isdigit()
# Return true if all characters in the string are digits and there is at least one character, false otherwise.
# Digits = decimal characters and digits that need special handling, such as the compatibility superscript digits.
# Formally, a digit is a character that has the property value Numeric_Type=Digit or Numeric_Type=Decimal.

# print('314159'.isdigit())   # True
# print('3.14159'.isdigit())  # False
# print('3-14159'.isdigit())  # False
# print('3 14159'.isdigit())  # False
# print('abcdef'.isdigit())   # False


# ------------------------------------------------------------------------------------------------ #
# s.isidentifier()
# Returns True if s is non empty and is a valid identifier.
# Valid identifiers = upper and lowercase letters, underscore and 0 through 9 (can't be first character).

# print('x'.isidentifier())          # True
# print('__Hello__'.isidentifier())  # True
# print('00322'.isidentifier())      # False
# print('X'.isidentifier())          # False


# ------------------------------------------------------------------------------------------------ #
# s.islower()

# s = "Babe Ruth, Yankees"
# print(s.islower())  # False


# ------------------------------------------------------------------------------------------------ #
# s.isnumeric()

# s = "Babe Ruth, Yankees"
# print(s.isnumeric())  # False


# ------------------------------------------------------------------------------------------------ #
# s.isprintable()
# Return true if all characters in the string are printable or the string is empty, false otherwise

# s = "Babe Ruth, Yankees"
# print(s.isprintable())  # True


# ------------------------------------------------------------------------------------------------ #
# s.isspace()
# Return true if only whitespace characters in the string and there is at least one character, false otherwise

# s = ' '
# print(s.isspace())  # True


# ------------------------------------------------------------------------------------------------ #
# s.istitle()

# s = 'Babe Ruth, Yankees'
# print(s.istitle())  # True
# s1 = 'Babe Ruth, yankees'
# print(s1.istitle())  # False


# ------------------------------------------------------------------------------------------------ #
# s.isupper()

# s = 'Brad LAMPSON'
# print(s.isupper())  # True
# s1 = 'Brad lampson'
# print(s1.isupper())  # False


# ------------------------------------------------------------------------------------------------ #
# s.join(iterable)
# Returns a STRING with char fill between elements

# print(', '.join(['cat', 'dog', 'mouse']))            # cat, dog, mouse
# print(' '.join(['cat', 'dog', 'mouse']))             # cat dog mouse
# print('-'.join(['cat', 'dog', 'mouse']))             # cat-dog-mouse
# print(''.join(['cat', 'dog', 'mouse']))              # catdogmouse
# print(''.join(reversed(['cat', 'dog', 'mouse'])))    # mousedogcat

# ------------------------------------------------------------------------------------------------ #
# s.ljust(width[, fillchar])

# s = 'Babe'
# print(s.ljust(10))       # 'Babe      ' adds 6 spaces, because "Babe" already 4 spaces
# print(s.ljust(10, '.'))  # 'Babe......' adds optional fillchar


# ------------------------------------------------------------------------------------------------ #
# s.lower()

# s = 'BaBE'
# print(s.lower())  # babe


# ------------------------------------------------------------------------------------------------ #
# s.lstrip([chars])


# ------------------------------------------------------------------------------------------------ #
# s.maketrans(x[, y[, z]])

# vow = 'aeiou'
# num = '12345'
# transtbl = str.maketrans(vow, num)   # or you could plug strings in as args
# s = 'Brad Lampson'
# print(s.translate(transtbl))         # br2tt l1mps4n


# ------------------------------------------------------------------------------------------------ #
# s.partition(sep)
# Splits 's' into three strings s = (head, m, tail), where head is 1st, m is 2nd, tail is 3rd

# s = 'Roses-Red-Violets-Blue'
# print(s.partition('-'))
# ('Roses', '-', 'Red-Violets-Blue')

# for i in s.split(' '):
#     print(i.ljust(13, '.'), len(i), 'characters')
# Roses........ 5 characters
# are.......... 3 characters
# Red.......... 3 characters
# Violets...... 7 characters
# are.......... 3 characters
# Blue......... 4 characters


# ------------------------------------------------------------------------------------------------ #
# s.replace(old, new[, count])

# s = "Babe Ruth, Yankees"
# s = s.replace('Babe Ruth', 'Mickey Mantle')
# print(s)  # "Mickey Mantle, Yankees" now assigned to s1, s remains unchanged.


# ------------------------------------------------------------------------------------------------ #
# s.rfind(sub[, start[, end]])
# Return the highest index in the string where substring sub is found within the slice.

# s = "Babe Ruth, Yankees"
# print(s.rfind('a'))  # 12 is the highest index occurrence


# ------------------------------------------------------------------------------------------------ #
# s.rindex(sub[, start[, end]])
# Like rfind(), but raise ValueError when the substring is not found.

# s = "Babe Ruth, Yankees"
# print(s.rindex('z'))  # ValueError: substring not found


# ------------------------------------------------------------------------------------------------ #
# s.rjust(width[, fillchar])
# Return the string right justified. Padded using the specified fillchar (space is default).

# s = "Babe Ruth, Yankees"
# print(s.rjust(len(s)+3, '>'))     # adds 3 '>' >>>Babe Ruth, Yankees


# ------------------------------------------------------------------------------------------------ #
# s.rpartition(sep)
# Splits 's' at the last occurrence of sep, and return a 3-tuple containing the part before the separator,
# the separator itself, and the part after the separator.
# If the separator is not found, return a 3-tuple containing two empty strings, followed by the string itself.

# s = 'Roses-Red-Violets-Blue'
# print(s.rpartition('-'))
# ('Roses-Red-Violets', '-', 'Blue')


# ------------------------------------------------------------------------------------------------ #
# s.rsplit(sep=None, maxsplit=-1)
# Return a list of the words in the string, using sep as the delimiter string.
# If maxsplit is given, at most maxsplit splits are done, the rightmost ones.
# If sep is not specified or None, any whitespace string is a separator.
# Except for splitting from the right, rsplit() behaves like split() which is described in detail below.

# s = 'Babe Ruth, baseball player'
# print(s.rsplit(sep=s[9:15]))   # ['Babe Ruth', 'ball player']
# print(s.rsplit(',', 1)[0])     # Babe Ruth

# ------------------------------------------------------------------------------------------------ #
# s.rstrip([chars])
# Return a copy of the string with trailing characters removed.
# If omitted or None, chars argument defaults to removes whitespace.
# The chars argument is not a suffix; rather, all combinations of its values are stripped.

# s = 'Babe Ruth, baseball player'
# print(len(s))
# s = s.rstrip()         # 'Babe Ruth, baseball player'
# print(len(s))
# print(s.rstrip('yer'))  # 'Babe Ruth, baseball pla'


# ------------------------------------------------------------------------------------------------ #
# s.split(sep=None, maxsplit=-1)
# -----When no delimiter is specified, a "space" is default----- #

# s = 'Babe Ruth, baseball player'
# string_to_list = s.split(',')  # Tells python to split the string on the comma ','
# print(string_to_list)          # ['Babe Ruth', ' baseball player']
# print(len(string_to_list))     # 2
# print(type(string_to_list))


# ------------------------------------------------------------------------------------------------ #
# s.split(sep=None, maxsplit=-1)
# When the delimiter is inconsistent throughout the string do this
# The  ";"   ","   "\s"  inside brackets are the delimiters. \s means match any whitespace character

# line = 'asdf fjdk; afed, fjek,asdf,   foo'
# import re
# line2 = re.split(r'[;,\s]\s*', line)
# print(line2)  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']


# ------------------------------------------------------------------------------------------------ #
# s.splitlines([keepends])
# Return a list of the lines in the string, breaking at line boundaries

# s = 'Brad Lampson'
# s = 'Brad\nLamp\nson'
# print(s.splitlines())               # ['Brad', 'Lamp', 'son']
# print(s.splitlines(keepends=True))  # ['Brad\n', 'Lamp\n', 'son']


# ------------------------------------------------------------------------------------------------ #
# s.startswith(prefix[, start[, end]])

# s = 'Babe Ruth, was a great baseball player'
# print(s.startswith('Babe'))  # True


# ------------------------------------------------------------------------------------------------ #
# s.strip([chars])
# Notes: empty() will remove ONLY white spaces.
# Notes: full() will not remove any chars if surrounded by unlisted chars.
# Example:  'abcba'.strip('c') will not remove c since a or b are in place.

# s = 'Babe Ruth, baseball player'
# print(s.strip('Baberylp '))
# Ruth, bas

# t = 'www.example.com'
# print(t.strip('w.come'))
# xampl


# ------------------------------------------------------------------------------------------------ #
# s.swapcase()

# s = 'BABIES r US'
# print(s.swapcase())  # babies R us


# ------------------------------------------------------------------------------------------------ #
# s.title()

# s = 'Brad lampson'
# print(s.title())  # Brad Lampson


# ------------------------------------------------------------------------------------------------ #
# s.translate(table)

# alpha = 'aeiou'
# numer = '12345'
# transtbl = str.maketrans(alpha, numer)  # or you could plug strings in as args
# s = 'Brad lampson'
# print(s.translate(transtbl))  # br2tt l1mps4n


# ------------------------------------------------------------------------------------------------ #
# s.upper()

# s = 'Brad lampson'
# print(s.upper())  # Brad LAMPSON


# ------------------------------------------------------------------------------------------------ #
# s.zfill(width)

# num = '75'
# print(num.zfill(5))  # 00075


# ------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------ #
# STRING METHODS END
# ------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
# CREATE A STRING

# s = 'Brad Lampson'
# s = str(2 + 3)
# s = ' '.join(['Brad', 'Lampson'])
# print(s)


# ------------------------------------------------------------------------------------------------ #
# MEMBERSHIP TESTING USING 'in' & 'not in'

# s = "Babe Ruth, Yankees"
# print('abe' in s)   # True
# print('ruth' in s)  # False (case sensitive)


# ------------------------------------------------------------------------------------------------ #
# CONCATENATING STRINGS

# m = 'Mickey Mantle'
# w = 'Willie Mays'
# print(m + ' and', w)              # Mickey Mantle and Willie Mays
# m += ' played for the Yankees'    # Mickey Mantle played for the Yankees
# m = m[:6] + w[-5:]                # Mickey Mays


# ------------------------------------------------------------------------------------------------ #
# REPLICATION WITH *
# augmented assignment replication with *=

# print('-'*50+'\n'+str('  -  '*10)+'\n'+'-'*50)


# ------------------------------------------------------------------------------------------------ #
# ENUMERATE() ON A STRING

# for item in enumerate('Lampson'):
#     print(item)


# ------------------------------------------------------------------------------------------------ #
# SLICING
# ------------------------------------------------------------------------------------------------ #
# [include : exclude]
# [include : exclude : step]

# test = '0123456789'
# print(len(test))             # 10
# print(test[-1])              # prints where test[0] == test[-10]
# print(test[13])              # gives an IndexError traceback: string index out of range
# print(test[0] == test[-10])  # True

# test = "Light Ray"
# for i in enumerate(test):
#     print(i)
# print(test[:-1])             # 'Light Ra'
# print(test[:])               # 'Light Ray'
# print(test[:8])              # 'Light Ra'
# print(test[1:8])             # 'ight Ra'
# print(test[::2])             # 'LgtRy'
# print(test[::-1])            # "yaR thgiL' reverses the sequence


# ------------------------------------------------------------------------------------------------ #
# STRIDE
# ------------------------------------------------------------------------------------------------ #
# [START: END: STEP]
# [START(include) : END(exclude) : STEP]

# s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(s[::2])       # [0, 2, 4, 6, 8, 10]
# print(s[::4])       # [0, 4, 8]
# print(s[1::2])      # [1, 3, 5, 7, 9]
# print(s[-1:6:-1])   # [10, 9, 8, 7]


# ------------------------------------------------------------------------------------------------ #
# Conversions CHR and ORD

# print(chr(36))   # $
# print(ord('$'))  # 36


# ------------------------------------------------------------------------------------------------ #
# SEP and END DIFFERENCES

# v = "Babe Ruth"
# w = "Willie Mays"
# print(v, w, sep=' -- ')   # Mickey Mantle -- Willie Mays
# print(v, w, end=' -- ')   # Mickey Mantle Willie Mays --


# ------------------------------------------------------------------------------------------------ #
# UNICODE, BYTES, STRINGS

# bytes and bytearrays: sequences of 8-bit integers, used for binary data.
# strings: sequences of Unicode characters, used for text data.

# Example, a function that takes a python unicode character
# look up its name and looks up the character again from the name.

# Unicodedata module
# def unicode_test(value):
#     import unicodedata
#     name = unicodedata.name(value)     # Returns the name assigned to the character chr as a string
#     value2 = unicodedata.lookup(name)  # Look up character by name.
#     print(f"Value={value2}, Name={name}")
#
# unicode_test('A')        # Value=A, Name='LATIN CAPITAL LETTER A'
# unicode_test('$')        # Value=$, Name='DOLLAR SIGN'
# unicode_test('!')        # Value=!, Name='EXCLAMATION MARK'
# unicode_test('\u00a9')   # Value=©, Name='COPYRIGHT SIGN'
# unicode_test('\u00a2')   # Value=¢, Name=CENT SIGN

# import unicodedata
# print(unicodedata.name('&'))     # AMPERSAND
# test = unicodedata.name('&')
# print(unicodedata.lookup(test))  # &

# python uses UTF-8 text encoding
# If you're copying and pasting strings from a website
# be sure the source is encoded in UTF-8 format
# otherwise it will cause an exception with an invalid byte sequence


# ------------------------------------------------------------------------------------------------ #
# USING SLICE() BUILT-IN FUNCTION

# foo = 'abcdefghijklmnopqrstuvwxyz1234567890'
# bar = ['one', 'two', 'three', 'four', 'five']
#
# alphabet = slice(0, 26)   # abcdefghijklmnopqrstuvwxyz
# alph = str(foo[alphabet])
# print(alph)
#
# numbers = slice(26, 38)   # 1234567890
# numb = int(foo[numbers])
# print(numb)
#
# bar_none = slice(1, 4)    # ['two', 'three', 'four']
# print(bar[bar_none])


# ------------------------------------------------------------------------------------------------ #
# WIP USING STRIP()

# The program below counts all the unique words in a file:

import collections
import string
import sys
import os

# print(os.getcwd())
# 
# def count_unique_word():
#     words = collections.defaultdict(int)
#     strip = string.whitespace + string.punctuation + string.digits + "\"'"
#     for filename in sys.argv[1:]:
#        with open(filename) as file:
#            for line in file:
#               for word in line.lower().split():
#                   word = word.strip(strip)
#                   if len(word) > 2:
#                       words[word] = words.get(word,0) +1
#     for word in sorted(words):
#        print("'{0}' occurs {1} times.".format(word, words[word]))

# count_unique_word()


# ------------------------------------------------------------------------------------------------ #
# COUNTING WORD OCCURRENCES IN A STRING

# sentence = 'to be or not to be'
# occurrences = {}
# for word in sentence.split():
#     occurrences[word] = occurrences.get(word, 0) + 1
#
# for word in occurrences:
#     print('The word', '"' + word + '"', 'occurs', str(occurrences[word]) + 'x' + ' in', '"' + sentence + '"')


# ------------------------------------------------------------------------------------------------ #
# ENCODING SEQUENCES
# ------------------------------------------------------------------------------------------------ #

# You encode a string to bytes:
# encode()


# ------------------------------------------------------------------------------------------------ #
# DECODING SEQUENCES
# ------------------------------------------------------------------------------------------------ #

# WIP


# ------------------------------------------------------------------------------------------------ #
# THE STRING MODULE
# ------------------------------------------------------------------------------------------------ #

# from string import Template
#
# s = Template('$who likes $what')
# print(s.substitute(who='tim', what='kung pao'))
# # 'tim likes kung pao'
#
# # d = dict(who='Tim')
# # print(Template('$who likes $what').safe_substitute(d))
# # # 'tim likes $what'
#
# # d = dict(who='Tim', what='something')  # what='something' fixes the KeyError
# # print(Template('$who likes $what').substitute(d))
# # KeyError: 'what'
#
# d = dict(who='Tim')
# print(Template('Give $who $100').substitute(d))
# # ValueError: Invalid placeholder in string: line 1, col 11


# ------------------------------------------------------------------------------------------------ #
# END
