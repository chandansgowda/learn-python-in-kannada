## **Input/Output, String Manipulation, and Comments**

### **1. Input and Output in Python**

#### **1.1 Input from the User:**
In Python, we use the `input()` function to take input from the user. The data entered by the user is always received as a string, so if you want to use it as a different data type (e.g., integer or float), you'll need to convert it using type conversion functions like `int()` or `float()`.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert input to integer
```

#### **1.2 Output to the Console:**
The `print()` function is used to display output to the console. You can use it to display text, variables, or results of expressions.

```python
print("Hello, " + name + "! You are " + str(age) + " years old.")
```

You can also use **f-strings** (formatted string literals) for more readable code:
```python
print(f"Hello, {name}! You are {age} years old.")
```

---

### **2. String Manipulation**

Strings are sequences of characters. Python provides many useful methods to manipulate strings.

#### **2.1 Common String Operations:**

- **Concatenation**: Joining two or more strings together using the `+` operator.
  ```python
  first_name = "John"
  last_name = "Doe"
  full_name = first_name + " " + last_name
  print(full_name)  # Output: "John Doe"
  ```

- **Repetition**: Repeating a string multiple times using the `*` operator.
  ```python
  greeting = "Hello! " * 3
  print(greeting)  # Output: "Hello! Hello! Hello! "
  ```

#### **2.2 String Methods:**
- `upper()`: Converts a string to uppercase.
- `lower()`: Converts a string to lowercase.
- `strip()`: Removes leading and trailing spaces from a string.
- `replace(old, new)`: Replaces a substring with another string.

```python
message = "  Hello, World!  "
print(message.strip())  # Output: "Hello, World!"
print(message.upper())  # Output: "HELLO, WORLD!"
print(message.replace("World", "Python"))  # Output: "Hello, Python!"
```

#### **2.3 Accessing String Characters:**
You can access individual characters in a string using **indexing**. Python uses zero-based indexing, so the first character has an index of 0.

```python
text = "Python"
print(text[0])  # Output: P
print(text[2])  # Output: t
```

You can also use **negative indexing** to start counting from the end of the string.
```python
print(text[-1])  # Output: n
print(text[-3])  # Output: h
```

#### **2.4 Slicing Strings:**
You can extract a portion (substring) of a string using slicing.

```python
text = "Python Programming"
print(text[0:6])  # Output: Python (extracts from index 0 to 5)
print(text[:6])  # Output: Python (same as above)
print(text[7:])  # Output: Programming (from index 7 to the end)
```

---

### **3. Comments in Python**

Comments are ignored by the Python interpreter and are used to explain the code or leave notes for yourself or others. They do not affect the execution of the program.

- **Single-line comments** start with `#`:
  ```python
  # This is a single-line comment
  print("Hello, World!")
  ```

- **Multi-line comments** can be written using triple quotes (`"""` or `'''`). These are often used to write detailed explanations or temporarily block sections of code:
  ```python
  """
  This is a multi-line comment.
  It can span multiple lines.
  """
  print("Hello, Python!")
  ```

---

### **4. Escape Sequences**
Escape sequences are special characters in strings that start with a backslash (`\`). They are used to represent certain special characters.

Some commonly used escape sequences:
- `\n`: New line
- `\t`: Tab space
- `\\`: Backslash

#### **Example:**
```python
print("Hello\nWorld")  # Output: 
# Hello
# World

print("Hello\tPython")  # Output: Hello    Python
```

---

### **Homework**

1. **Simple Greeting Program**:
   Write a Python program that asks the user for their name and age, then prints a personalized greeting message. Use both the `+` operator and f-strings for output.

   **Example**:
   ```python
   Enter your name: Alice
   Enter your age: 25
   Output: Hello, Alice! You are 25 years old.
   ```

2. **String Manipulation Exercise**:
   Write a Python program that:
   - Takes a sentence as input from the user.
   - Prints the sentence in all uppercase and lowercase.
   - Replaces all spaces with underscores.
   - Removes leading and trailing whitespace.

   **Example**:
   ```python
   Input: "   Python is awesome!   "
   Output:
   Uppercase: "PYTHON IS AWESOME!"
   Lowercase: "python is awesome!"
   Replaced: "___Python_is_awesome!___"
   Stripped: "Python is awesome!"
   ```

3. **Character Counter**:
   Write a Python program that:
   - Asks the user for a string.
   - Prints how many characters are in the string, excluding spaces.

   **Example**:
   ```python
   Input: "Hello World"
   Output: "Number of characters (excluding spaces): 10"
   ```

4. **Escape Sequence Practice**:
   Write a Python program that uses escape sequences to print the following output:

   **Example**:
   ```
   Hello
       World
   This is a backslash: \
   ```

---
