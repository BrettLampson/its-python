

# ------------------------------------------------------------------------------------------------ #
# FIBONACCI sequence up to "n" - "WHILE loop"

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
# fib(56)                   # 0 1 1 2 3 5 8 13 21 34 55 (prints up to 56)


# ------------------------------------------------------------------------------------------------ #
# FIBONACCI sequence returns "n" results then stops - "FOR loop"

# def fib2(n):
#     a, b = 0, 1
#     for i in range(0, n):
#         print(a)
#         a, b = b, a + b
# fib2(10)                  # 0 1 1 2 3 5 8 13 21 34 (prints 10 results)


# ------------------------------------------------------------------------------------------------ #
# Recursion

# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# for n in range(1, 35):
#     print(n, ':', fibonacci(n))

# ------------------------------------------------------------------------------------------------ #
# Memoization.  Store values for recent function calls so that
# future calls don't have to repeat the work.

# fibonacci_cache = {}
#
#
# def fibonacci(n):
#     # if we have cached the value, then return it
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]
#
#     # Compute the Nth term
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacci(n-1) + fibonacci(n-2)
#
#     # Cache the value and return it
#     fibonacci_cache[n] = value
#     return value
#
#
# for n in range(1, 35):
#     print(n, ':', fibonacci(n))

