"""
This module illustrates how to write good functions.

It uses the simple doctest module to check the functions.

In general, try to write functions that return a value (or values).

If the fuction does something else (e.g. prints to the console),
it's called a 'side effect'.

Writing functions is critical.
Being able to write good, testable functions is very valuable skill.

Uses:
- doctest - to make sure our custom functions are correct

Define unit tests:
 - Show what SHOULD happen (will test this with doctest)
 - Use interactive Python style to illustrate desired behavior.

>>> add_two(1,2)
3

>>> add_two("hello"," world")
'hello world'

>>> add_triangle_list( [3,4,5] )
12

>>> add_any(1,1,1,1,1,1,1,1)
8

>>> add_any_with_keywords(a=1,b=2)
3
"""

import doctest

# define some custom functions

def add_two(first, second):
    """Return the sum of any two arguments."""
    sum = first + second
    return sum


def add_triangle_list(list_triangle):
    """Return the sum of three numbers in a list."""
    sum = 0
    for value in list_triangle:
        sum = sum + value
    return sum


def add_any(*args):
    """Return the sum of numbers, using built-in *args."""
    sum = 0
    for x in args:
        sum += x  # Use the popular and concise version of sum = sum + x
    return sum


def add_any_with_keywords(**kwargs):
    """Return the sum of numbers, using built-in keyword args, **kwargs."""
    sum = 0
    for value in kwargs.values():  # use values() - name doesn't matter
        sum += value  # Use the popular and concise version of sum = sum + x
    return sum


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # -------------------------------------------------------------
    # Call some functions and execute code!

    print()
    print(f"add_two(5,5) = {add_two(5,5)}")
    print()
    print(f"add_triangle_list([5,5,5) = {add_triangle_list([5,5,5])}")
    print()
    print(f"add_any(2)       = {add_any(2)}")
    print(f"add_any(2,2)     = {add_any(2,2)}")
    print(f"add_any(2,2,2)   = {add_any(2,2,2)}")
    print(f"add_any(2,2,2,2) = {add_any(2,2,2,2)}")
    print()
    print(f"add_any_with_keywords(a=8,b=2) = {add_any_with_keywords(a=8,b=2)}")
    print()
    print("===========================================================")
    print("Running doctest.testmod() function to unit test our code")
    print("===========================================================")
    print()
    doctest.testmod()
    print()
    print("===========================================================")
    print("If you don't see any results, all tests passed.")
    print("===========================================================")
    print("Run with the -v flag to show results regardless.")
    print("Hit up arrow (to get last command) and add space -v")
    print("===========================================================")
