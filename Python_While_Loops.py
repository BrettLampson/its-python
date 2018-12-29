print()

# ------------------------------------------------------------------------------------------------ #
# WHILE LOOP
# ------------------------------------------------------------------------------------------------ #
# Use a while loop when:
# 1) When we can't create a proper iterator to step through the items.
# 2) During interactions with human users, when data isn't there until we get input.

# Example: Validate registrants password.
# pw_text = str(input('Enter A New Password: '))
# conf__pw_text = str(input('Confirm Your New Password: '))
# if pw_text == conf__pw_text:
    # password check complete


# ------------------------------------------------------------------------------------------------ #
# WHILE LOOP
# ------------------------------------------------------------------------------------------------ #
# Password lockout after 5 failed attempts
# import sys
# guesses = 5
# while guesses > 0:
#     print('You have', guesses, 'guesses')
#     askPass = str(input('Enter Password: '))
#     if askPass.lower() != "brett":
#         print("...invalid password")
#         guesses -= 1
#     else:
#         print("Access Granted")
#         run_this = input('What program should I run?: ')
#         # if run_this in my_tuple_of_programs:
# pw_fail_email = input('Please enter your email address to answer security questions:')
# print(input('Press any key to quit'))
# sys.exit()


# ------------------------------------------------------------------------------------------------ #
# WHILE LOOP
# ------------------------------------------------------------------------------------------------ #
# Check for something and 'break' as soon as its found
# numbers = [1, 4, 13, 41]
# position = 0
# while position < len(numbers):
#     number = numbers[position]
#     # Check for an even number
#     if number % 2 == 0:
#         print('Even number detected:', number, 'at index', position, '\n...my job is finished.')
#         break
#     position += 1
# else:  # break not called
#     print('No even number found')


# ------------------------------------------------------------------------------------------------ #
# WHILE LOOP
# ------------------------------------------------------------------------------------------------ #
# Fibonacci Sequence up to (n)
# def fib(n):
#     a, b = 0, 1
#     while b < n:
#         print(b, end=' ')
#         a, b = b, a + b
# fib(56)
# # # 1 1 2 3 5 8 13 21 34 55


# ------------------------------------------------------------------------------------------------ #
# WHILE LOOP
# ------------------------------------------------------------------------------------------------ #
# # Create a list from user input (type 'stop' to quit)
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
# ------------------------------------------------------------------------------------------------ #
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
# ------------------------------------------------------------------------------------------------ #
# # Loop until something occurs, but not sure when?  Infinite while loop with break.
# email_list = set()
# while True:
#     email_entry = str(input("Enter an email address [type q to 'quit']: "))
#     if email_entry == 'q':
#         print('Your session has ended.')
#         break
#     else:
#         email_list.add(email_entry)
#         print("The email you've added is ", email_entry)
#         print(email_list, end='\n')


# ------------------------------------------------------------------------------------------------ #
# WHILE LOOP
# ------------------------------------------------------------------------------------------------ #
