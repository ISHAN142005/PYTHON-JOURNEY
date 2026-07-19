# Taking User Input

This section explains how to make your Python programs interactive by accepting inputs directly from the user via the keyboard.

---

## 1. Using the `input()` Function
The `input()` function pauses program execution and waits for the user to type something into the terminal and press Enter.

*   **Crucial Rule:** By default, the `input()` function **always returns the data as a string (`str`)**, even if the user types a number.
*   **Data Conversion:** If you need to perform mathematical operations on the input, you must explicitly convert (typecast) it to an integer or a float.

---

## 2. Practical Example

The following example showcases how to capture standard text input and how to instantly wrap the input function inside `int()` to capture numerical data:

```python
# Capturing text data (stays as a string automatically)
name = input("Enter your name: ")

# Capturing numerical data (wrapped in int() to convert the string immediately)
age = int(input("Enter your age: "))

# Printing the result using an f-string (formatted string literal)
print(f"Hello {name}, you are {age} years old.")