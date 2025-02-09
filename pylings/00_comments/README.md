# Comments

Comments are ignored by the interpreter at runtime. They are primarily used to
write notes that explain the code to yourself or others.

Let's go over the different types of comments you may encounter.

## Single-line comments

Single-line comments are lines that start with a '#'.

```python
# This is a single-line comment!
```

## Inline comments

Inline comments also start with a '#', but they aren't on their own line.

```python
timeout_ms = 5 * 1000  # Multiply by 1000 to convert seconds into milliseconds.
```

## Multi-line comments

Python doesn't have built-in syntax for multi-line comments, but you can use
triple quotes (single or double) to achieve the same effect (or you can also
use multiple single-line comments).

```python
'''
Multi-line comments are great when you need to provide a longer explanation
or if you want to temporarily disable a block of code during development.
'''

# Alternatively, you can also use multiple single-line comments as shown here:
# This is the first line of the comment.
# This is the second line.
# Continue as necessary to describe your code.
```
