# Python is a dynamically Typed Language.
## No need to tell which type of data at the time of declaration.

# Understanding Variables & Data Types

This section covers how Python stores data, the strict rules for naming containers, best practices for writing clean code, and a breakdown of Python's built-in data types.

---

## 1. What are Variables?
Variables are named containers used to store data values that can be referenced, used, and manipulated throughout a program. 

*   A variable is created the moment you first assign a value to it using the assignment operator (`=`).
*   **Lecture Example:**
    ```python
    name = "Alice"
    age = 25
    height = 5.6
    ```

---

## 2. Variable Naming Rules
Python has strict rules regarding what you can name a variable. Breaking these rules will cause a syntax error:
*   Variable names can only contain alphanumeric characters and underscores (`a-z`, `A-Z`, `0-9`, and `_`).
*   Variable names **must start with a letter or an underscore** (they cannot start with a number).
*   Variable names are **case-sensitive** (`age`, `Age`, and `AGE` are three completely different variables).
*   **Avoid using Python keywords** as variable names because they are reserved for the language's core functions (e.g., do not name variables `print`, `if`, `else`, or `while`).

### Best Practices for Readability
*   Use descriptive names that clearly reflect the purpose of the variable (e.g., use `user_age` instead of just `a`).
*   Use lowercase letters for standard variable names.
*   Separate multiple words using underscores for readability—this style is called **snake_case** (e.g., `first_name`, `total_amount`).

---

## 3. Built-in Data Types in Python
Python automatically detects the type of data you assign to a variable. The core built-in data types include:

| Data Type | Type Code | Description & Lecture Examples |
| :--- | :--- | :--- |
| **Integers** | `int` | Whole numbers, positive or negative, without decimals (e.g., `10`, `-5`). |
| **Floats** | `float` | Floating-point numbers containing one or more decimals (e.g., `3.14`, `-0.001`). |
| **Strings** | `str` | Text data enclosed in either single or double quotes (e.g., `"Hello"`, `'Python'`). |
| **Booleans** | `bool` | Logical values representing either `True` or `False`. |
| **Lists** | `list` | Ordered, mutable (changeable) collections of items (e.g., `[1, 2, 3]`). |
| **Tuples** | `tuple` | Ordered, immutable (unchangeable) collections of items (e.g., `(1, 2, 3)`). |
| **Sets** | `set` | Unordered, unindexed collections of unique elements (e.g., `{1, 2, 3}`). |
| **Dictionaries** | `dict` | Unordered collections of key-value pairs used to store mapped data (e.g., `{"name": "Alice", "age": 25}`). |

---

## 4. Checking Data Types
If you are ever unsure what data type a variable holds, Python provides a built-in function to inspect it.
*   Use the **`type()`** function to check the exact data type of a value or variable.

```python
print(type(10))       # Output: <class 'int'>
print(type("Hello"))  # Output: <class 'str'>