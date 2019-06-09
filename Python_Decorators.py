
print('-'*49)
# ------------------------------------------------------------------------------------------------ #
# DECORATORS

# Used to modify an existing function without changing its source code
# A decorator is a function that takes a function or method
# as its argument and returns a decorated version, that is, a version of the
# function or method that is modified in some way. A decorator is indicated by
# preceding its name with an at symbol (@).

# 


# # FUNCTION USED WHEN DECORATING
# def details(func):
#     def new_function(*args, **kwargs):
#         print('Running Function: ', func.__name__)
#         print('Positional arguments: ', args)
#         print('Keyword arguments: ', kwargs)
#         result = func(*args, **kwargs)
#         print('Result: ', result)
#         return result
#     return new_function


# # DECORATE IT
# @details
# def thingsInCar(*args, **kwargs):
#     return(args, kwargs)
# thingsInCar('work clothes', perm_1='phone charger')


# # DECORATE IT
# @details
# def add_numbers(a, b):
#     return a + b
# add_numbers(144, 6)
# # RESULT
# Running Function:  add_numbers
# Positional arguments:  (144, 6)
# Keyword arguments:  {}
# Result:  150