"""
In Python, arrays are called tuples. They can be declared like so:

    foo = (42, 69, 1337)

Tuples are an immutable data type. You can not change the values once they have
been declared. The following would throw a TypeError:

    foo[0] = 7

You can get the length of a tuple using the built-in `len()` function.

    size = len(foo)  # 3
"""

foo = (42, 69, 1337)

# Problem 1: Comment out the following line so the program can continue.
foo[0] = 7

# Problem 2: Use a built-in function to print the length of the tuple.
size = ???(foo)

print(f"The length of foo is: {size}")
assert size == 3
