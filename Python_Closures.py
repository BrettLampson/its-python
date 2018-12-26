

# ------------------------------------------------------------------------------------------------ #
# CLOSURES

# Wikipedia:  A closure is a record storing a function together with an environment: a mapping
# associating each free variable of the function with the value or storage location to which
# the name was bound when the closure was created.
# A closure, unlike a plain function, allows the function to access those captured variables
# through the closure's reference to them, even when the function is invoked outside their scope.

# WHEN TO USE A CLOSURE:


# ------------------------------------------------------------------------------------------------ #
# CLOSURE

# # PYTHON VERSION
# def outer_func():
#     message = 'Hello from the inner function'
#
#     def inner_func():
#         print(message)
#
#     return inner_func    # closure
#
# my_func = outer_func()   # initialize the function by assigning it to a variable
# print(my_func.__name__)  # <function outer_func.<locals>.inner_func at 0x000000000123F730>
# my_func()


# # JAVASCRIPT VERSION
# function outerFunc() {
#   let message = 'Hello from the inner function'
#
#   function innerFunc() {
#     console.log(message)
#   }
#   return innerFunc;
# }
# let myFunc = outerFunc();
# console.log(myFunc.name);
# myFunc();
