"""
# Writing custom functions

A function is a named block of code that performs a specific task. It can take
inputs (called parameters), process them, and return output. Functions help to
organize code, improve readability, and allow for code reuse.

## Example

>>> def add(x, y):
...     return x + y
>>>
>>> total = add(1, 2)
>>> print("Your total is: " + total)  # Your total is: 3

## Explanation

A function is defined using the `def` keyword followed by a name and a set of
parameters defined in parenthesis. In the example above, we defined a function
named "add" that takes (2) parameters, `x` and `y`. The output of the function
is determined by the `return` statement. Whatever is `return`ed by the function
becomes the value of variable, so in this case `total` will hold the value of
whatever `x + y` is.

Try the example for yourself!
"""


def convert_to_celcius(f):
    return (f - 32) / (9 / 5)


temperatures = (66, 62, 62, 62, 65, 76, 80, 76)

for temperature_f in temperatures:
    temperature_c = convert_to_celcius(f=temperature_f)
    print(f"{temperature_f:.1f}°F ({temperature_c:.1f}°C)")
