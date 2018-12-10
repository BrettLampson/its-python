
# ---------------------------------------------------------------------------------------------- #
# LAMBDA FUNCTION
# ---------------------------------------------------------------------------------------------- #
# A simple 1 line function
# does not use def or return function, these are implicit
# They are syntactically restricted to a single expression.
# WHEN TO USE LAMBDA:  Lambda functions can be used wherever function objects are required.


# ---------------------------------------------------------------------------------------------- #
# LAMBDA if we want to double x

# f = lambda x: x * 2               # where "x": is the parameter and '2 * x' is the return
# print(f(12))                      # 24


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
# LIST COMP printing directory file list, sorted by file size

# lcomp = [(name, os.path.getsize(name)) for name in os.listdir(os.getcwd())]
# lcomp.sort(key=lambda name: name[1], reverse=True)
# pprint(lcomp)