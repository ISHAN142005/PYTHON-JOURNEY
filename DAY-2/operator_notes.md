# Types of Operators

## Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

- `+` — Addition
- `-` — Subtraction
- `*` — Multiplication
- `/` — Division
- `%` — Modulus (Remainder)
- `**` — Exponentiation
- `//` — Floor Division

### Example

```python
print(10 + 5)   # Output: 15
print(10 ** 2)  # Output: 100
```

---

## Comparison Operators

Comparison operators are used to compare two values and return either `True` or `False`.

- `==` — Equal
- `!=` — Not Equal
- `>` — Greater Than
- `<` — Less Than
- `>=` — Greater Than or Equal To
- `<=` — Less Than or Equal To

### Example

```python
print(10 > 5)    # Output: True
print(10 == 5)   # Output: False
```

---

## Logical Operators

Logical operators are used to combine conditional statements.

- `and`
- `or`
- `not`

### Example

```python
print(True and False)  # Output: False
print(True or False)   # Output: True
print(not True)        # Output: False
```

---

## Assignment Operators

Assignment operators are used to assign values to variables.

- `=` — Assign
- `+=` — Add and Assign
- `-=` — Subtract and Assign
- `*=` — Multiply and Assign
- `/=` — Divide and Assign
- `%=` — Modulus and Assign
- `**=` — Exponentiate and Assign
- `//=` — Floor Divide and Assign

### Example

```python
x = 10
x += 5  # Equivalent to x = x + 5
print(x)  # Output: 15
```

---

## Membership Operators

Membership operators are used to test whether a value exists in a sequence.

- `in`
- `not in`

### Example

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)  # Output: True
```

---

## Identity Operators

Identity operators are used to compare the memory locations of two objects.

- `is`
- `is not`

### Example

```python
x = 10
y = 10

print(x is y)  # Output: True
```

---

# Summary

- Variables store data, and Python supports multiple data types.
- Typecasting allows you to convert between data types.
- Use `input()` to take user input and `print()` to display output.
- Comments and escape sequences help make your code more readable.
- Python provides a variety of operators for performing operations on data.