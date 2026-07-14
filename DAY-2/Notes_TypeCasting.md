# Typecasting in Python

This section covers how to change the data type of a variable dynamically using Python's built-in conversion utilities.

---

## 1. What is Typecasting?
Typecasting (also known as type conversion) is the process of explicitly converting a value from one data type to another. This is crucial when you need to perform operations that require matching data types (e.g., converting user input strings into integers for calculations).

### Core Typecasting Functions:
*   **`int()`** : Converts a compatible value to an integer.
*   **`float()`** : Converts a compatible value to a floating-point number.
*   **`str()`** : Converts any value to a string representation.
*   **`bool()`** : Converts a value to a boolean (`True` or `False`).

---

## 2. Practical Examples

### Convert String to Integer
Useful when taking numerical inputs from a web form or terminal prompt (which always arrive as strings).
```python
num_str = "10"
num_int = int(num_str)  # Converts the characters "10" into the actual number 10
print(num_int)          # Output: 10
print(type(num_int))    # Output: <class 'int'>