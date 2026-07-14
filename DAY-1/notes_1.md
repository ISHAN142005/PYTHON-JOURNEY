# Python Syntax Rules & Foundations

This note covers the core structural rules of Python as explained in the lecture, focusing on block structures, code statements, and comments.

---

## 1. Core Python Syntax Rules

### 1. Indentation
Unlike other programming languages that use curly brackets `{}` to group code, Python uses **indentation** (spaces or tabs) to define blocks of code.

*   **Best Practice:** Ideally, use **4 spaces** for indentation.
*   **Lecture Example:**
    ```python
    if(a > 3):
        print("a is greater than 3") # The spaces before print are the indentation
    ```

### 2. Whitespace
Python is highly sensitive to whitespace. You must ensure consistent indentation throughout your entire code block to avoid running into an `IndentationError`.

### 3. Statements
Each individual line of code is considered a statement.
*   **Lecture Example:**
    ```python
    print("Hello Harry")
    print("I am good")
    print(3)
    ```
*   *Note on Style:* While you can write multiple statements on a single line using a semicolon `;` (e.g., `print("A"); print("B")`), it is **not recommended** in standard Python development because it reduces code readability.

### 4. Comments
Comments are text entries that Python completely ignores during execution. They are used to document your code logic.
*   **Single-line comments:** Created using the hash symbol (`#`).
    ```python
    # This is a single-line comment
    ```
*   **Multi-line comments:** Created by wrapping text inside triple quotes (`'''` or `"""`).
    ```python
    ''' 
    This is a 
    multi-line comment 
    '''
    ```

---

## 2. Additional Instructor Notes

*   **Versatility:** Python is globally known for being a versatile and incredibly beginner-friendly programming language.
*   **Environment Setup:** The first critical step to writing good code is properly setting up Python and choosing the right IDE (like **VS Code**, which is used throughout this tutorial series).
*   **Precision:** While Python's syntax is relatively simple and English-like, it requires careful, disciplined attention to your indentation and whitespace layout.
*   **Starting Small:** It is always best to start with small, simple programs—like printing `"Hello, World!"`—to build confidence and get completely comfortable with the fundamentals before moving forward.