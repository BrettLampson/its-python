
print('-'*50)
# ------------------------------------------------------------------------------------------------ #
# DECORATORS

# Used to modify an existing function without changing its source code
# A decorator is a function that takes a function or method
# as its argument and returns a decorated version, that is, a version of the
# function or method that is modified in some way. A decorator is indicated by
# preceding its name with an at symbol (@).


# def document_it(func):
#     def new_function(*args, **kwargs):
#         print('Running Function: ', func.__name__)
#         print('Positional arguments: ', args)
#         print('Keyword arguments: ', kwargs)
#         result = func(*args, **kwargs)
#         print('Result: ', result)
#         return result
#     return new_function

# @document_it  # <---- DECORATOR
# def add_numbers(a, b):
#     return a + b

# add_numbers(3, 2)


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

# # NOT DECORATED
# def thingsInCar(*args, **kwargs):
#     print(args, kwargs)
# thingsInCar('subway receipt', permanent1='phone charger', permanent2='car seat')
#
# # DECORATE IT
# @details
# def thingsInCar(*args, **kwargs):
#     return(args, kwargs)
# thingsInCar('subway receipt', permanent1='phone charger', permanent2='car seat')
#
# # DECORATE IT
# @details
# def add_numbers(a, b):
#     return a + b
# add_numbers(144, 6)