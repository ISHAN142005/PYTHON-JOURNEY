# Python Foundations: Escape Sequences

This reference sheet covers what escape sequences are, how they function inside string data types, and the common escape codes used in Python development.

---

## 1. What is an Escape Sequence?
An **Escape Sequence** is a sequence of characters that does not represent itself when used inside a string literal. Instead, it translates into a special character or action that would otherwise be difficult, hidden, or illegal to type directly into a string (such as starting a new line or adding tab spacing).

*   **The Escape Character:** In Python, escape sequences always begin with a backslash (`\`).
*   **How it Works:** The backslash acts as an "escape signal" telling the Python interpreter: *"Hey, do not print the next character normally. Treat it as a special formatting rule instead."*

---

## 2. Common Escape Sequences Reference Table

When you render your Markdown preview in VS Code (`Ctrl + Shift + V`), this table will organize the most frequently used escape markers:

| Escape Sequence | Technical Name | Resulting Action / Output |
| :--- | :--- | :--- |
| **`\n`** | Newline | Breaks the current line of text and moves the cursor to the beginning of the next line. |
| **`\t`** | Horizontal Tab | Inserts a standard keyboard tab space (usually equivalent to 4 standard spaces). |
| **`\\`** | Backslash | Prints a single literal backslash (`\`) character without triggering an escape flag. |
| **`\"`** | Double Quote | Allows you to print a double quotation mark inside a string that is wrapped in double quotes. |
| **`\'`** | Single Quote | Allows you to print a single quotation mark/apostrophe inside a string wrapped in single quotes. |

---

## 3. Practical Code Examples

Copy these examples into your `.py` scripts to test how they execute in the terminal:

### A. Moving Text to a New Line (`\n`)
```python
# Instead of using two separate print statements, \n splits the sentence instantly.
print("Hello\nWorld!")

# Output:
# Hello
# World!