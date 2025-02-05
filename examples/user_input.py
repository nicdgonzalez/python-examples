"""
# Taking user input

In Python, you can take input from the user using the `input()` function.

## Example

>>> name = input("Enter your name: ")
>>> print("Hello, " + name)

## Explanation

The line `input("Enter your name: ")` displays the text inside the parenthesis
to the user via the terminal then waits for the user to type something and
press ENTER. The value entered is stored as a string in the `name` variable.

The following line `print("Hello, " + name)` first adds the two strings
together (e.g., if the user enters "Nic" and then presses ENTER, the final
string would look like "Hello, Nic") then displays the result to the user.

Run this file to see for yourself!
"""

name = input("Enter your name: ")
print("Hello, " + name)
