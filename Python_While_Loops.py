

# ------------------------------------------------------------------------------------------------ #
# WHILE LOOP
# ------------------------------------------------------------------------------------------------ #

# When to use a while loop
# Most of the time a for loop provides all the iteration controls we need.  There are
# a few situations when we need a while loop.  Including:
# 1) When we can't create a proper iterator to step through the items.
# 2) During interactions with human users, when data isn't there until we get input.
# Example: prompt user for their password.
# pw_text = str(input('Enter Password: '))
# conf__pw_text = str(input('Enter Password: '))
# if pw_text == conf__pw_text:
#     do something


# ------------------------------------------------------------------------------------------------ #
# WHILE LOOP
# import sys
# guesses = 0
# while guesses < 5:
#     print('Tries remaining =', 5 - guesses)
#     askPass = input('Guess my name: ')
#     if askPass.lower() != "brett":
#         print("No, sorry")
#         guesses += 1
#         continue
#     else:
#         break
# print("Good Job! That's my name!")
# print(input('Press any key to quit'))
# sys.exit()


# ------------------------------------------------------------------------------------------------ #
# WHILE LOOP
# # Use this loop to check for something and 'break' as soon as its found.
# numbers = [1, 2, 3]
# position = 0
# while position < len(numbers):
#     number = numbers[position]
#     if number % 2 == 0:
#         print('Found even number', number)
#         break
#     position += 1
# else: # break not called
#     print('No even number found')


# ------------------------------------------------------------------------------------------------ #
# WHILE LOOP
# def fib(n):
#     a, b = 0, 1
#     while b < n:
#         print(b, end=' ')
#         a, b = b, a + b
# fib(56)
# # 1 1 2 3 5 8 13 21 34 55


# ------------------------------------------------------------------------------------------------ #
# WHILE LOOP
# # Create a list from user input (while loop)
# num_list = []
# while True:
#     num = str(input('Enter a number' + ' or type "stop" to quit: \n>>> '))
#     if num == 'stop':
#         break
#     num_list += [num]
# print('This is the list: ', num_list)
# # This is the list:  ['3', '6', '9', 'no more']


# ------------------------------------------------------------------------------------------------ #
# WHILE LOOP
# # List of 3 items from user input (*****)
# userList = []
# maxLengthList = 3
# while len(userList) < maxLengthList:
#     item = str(input('Enter item to your list: '))
#     userList.append(item)
# print('Here\'s your list: ', userList)
# # Here's your list:  ['brett', 'shaina', 'kayden']


# ------------------------------------------------------------------------------------------------ #
# WHILE LOOP
# # Loop until something occurs, but not sure when?  Infinite while loop with break.
# email_list = []
# while True:
#     email_entry = str(input("Enter an email address [type q to 'quit']: "))
#     if email_entry == 'q':
#         print('Your session has ended.')
#         break
#     else:
#         email_list.append(email_entry)
#         print("The email you've added is ", email_entry)
#         print(email_list, end='\n')


