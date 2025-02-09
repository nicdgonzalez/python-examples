# Variables

In Python, variables are used to store data values. Think of a variable as a
container that holds a value that you can reference and manipulate throughout
your program.

For example:

```python
age = 25
name = "Nic"
```

Here, `age` is a variable that holds the integer `25`, and `name` is a variable
that holds the string `"Nic"`.

## Declaring a variable

Variables in Python don't need an explicit type. As long as the value has the
attributes the target needs, it is perfectly valid. To declare a variable,
simply assign a value to it using the assignment operator (`=`).

```python
x = 10  # Automatically knows `x` is an integer.
message = "Hello, World!"  # Automatically knows `message` is a string.
```

## Types of variables

1. `int` (Integer): Whole numbers.
   ```python
   age = 20
   ```
1. `float` (Floating point): Decimal numbers.
   ```python
   distance_mm = 135.42
   ```
1. `str` (String): Text data enclosed in quotes.
   ```python
   name = "Snoopy"
   ```
1. `bool` (Boolean): `True` or `False`.
   ```python
   is_active = True
   ```
1. `list`: A dynamic collection of values in a specific order.
   ```python
   months = ["January", "February", "March", "April", "May", ..., "December"]
   ```
1. `dict` (Dictionary): A collection of key-value pairs.
   ```python
   user = {"name": "Alice", "occupation": "Integrity Knight", "age": 19}
   ```
1. ...there are also other built-in types like `tuples`, `set`, etc., but these
   are the most common ones. You can even write your own custom data types.

## Variable names

Here are some tips for naming your variables in Python:

- Choose names that describe the purpose of the variable. For example, `age`,
  `height`, and `weight` are better than generic names like `x`, `y`, or `z`.
- Avoid using reserved keywords (e.g., `if`, `else`, `while`, etc.) or built-in
  types as variable names (`int`, `list`, `str`, etc.), as one will not let you
  and the other would override the built-in values.
- Use `snake_case` for your variable names. This is the convention most Python
  programmers follow as it is recommended by the official Python style guide
  ([PEP 8]).
- Variable names should be descriptive, yet concise. For example, `name` is
  better than `name_of_user`.

Of course, rules are meant to be broken. There will be cases where it may be
better to have single-letter variable names. Use your own judgement to ensure
your code is nice, readable, and maintainable.

[pep 8]: https://peps.python.org/pep-0008/
