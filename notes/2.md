## **Python Basics - 1**

### **1. Variables in Python**
Variables in Python are used to store data values. They are created when you assign a value to them, and you don’t need to declare their type (Python is dynamically typed).

#### **Syntax for Variable Assignment:**
```python
x = 5  # Assigning an integer value to the variable x
y = "Hello"  # Assigning a string value to the variable y
```

#### **Variable Naming Rules:**
- Variable names can contain letters (a-z, A-Z), numbers (0-9), and underscores (_).
- Variable names must start with a letter or an underscore.
- Variable names are case-sensitive (`Name` and `name` are different).

#### **Example:**
```python
age = 25
name = "John"
is_student = True
```

### **2. Data Types in Python**
Python has various built-in data types. Some common ones are:
- **int**: For integers (e.g., 1, -3, 100)
- **float**: For floating-point numbers (e.g., 3.14, -0.001)
- **str**: For strings (e.g., "Hello", "Python")
- **bool**: For boolean values (True or False)

#### **Type Checking:**
You can use the `type()` function to check the type of a variable.
```python
x = 10
print(type(x))  # Output: <class 'int'>
```

### **3. Type Conversion**
Python allows you to convert between data types using functions like `int()`, `float()`, `str()`, etc.

#### **Example:**
```python
x = "10"  # x is a string
y = int(x)  # Convert string to integer
z = float(y)  # Convert integer to float
print(z)  # Output: 10.0
```

### **4. Arithmetic Operators**
Python supports basic arithmetic operations like addition, subtraction, multiplication, division, and more.

#### **Common Operators:**
- `+` (Addition)
- `-` (Subtraction)
- `*` (Multiplication)
- `/` (Division)
- `//` (Floor Division)
- `%` (Modulus)
- `**` (Exponentiation)

#### **Examples:**
```python
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333...
print(a // b)  # Output: 3 (Floor Division)
print(a % b)  # Output: 1 (Modulus)
print(a ** b)  # Output: 1000 (Exponentiation)
```

### **5. Assigning Values to Multiple Variables**
Python allows you to assign values to multiple variables in a single line.

#### **Example:**
```python
x, y, z = 10, 20, 30
print(x)  # Output: 10
print(y)  # Output: 20
print(z)  # Output: 30
```

You can also assign the same value to multiple variables in one line:
```python
x = y = z = 100
print(x, y, z)  # Output: 100 100 100
```

### **6. Variable Reassignment**
You can change the value of a variable at any point in your program.

#### **Example:**
```python
x = 5
print(x)  # Output: 5
x = 10
print(x)  # Output: 10
```

---

### **Homework**

1. **Arithmetic Practice:**
   Write a Python program that performs basic arithmetic operations (addition, subtraction, multiplication, and division) on two numbers. Define the two numbers as variables within the code and print the results for each operation.

2. **Swap Two Variables:**
   Write a Python program that swaps the values of two variables with and without using a third variable.

3. **Build in Public:**
   Create a post on Linkedin/X and share that you learn variables and data types in python and its day 1. (Use #engineeringinkannada and mention me)

---

