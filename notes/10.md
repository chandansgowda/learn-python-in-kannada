## **For Loops in Python**

In Python, a **`for` loop** is used to iterate over a sequence (like a list, tuple, string, or range) and execute a block of code repeatedly for each element in the sequence.

### **1. The Basic Structure of a `for` Loop**

A **`for` loop** allows you to repeat a block of code a fixed number of times, or once for each element in a sequence.

#### **Syntax**:
```python
for item in sequence:
    # Code to execute for each item in the sequence
```

#### **Example**:
Let’s print each name in a list of Kannada cities:

```python
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    print(city)
```

**Output**:
```
Bengaluru
Mysuru
Hubballi
Mangaluru
```

- Here, `cities` is a list, and the `for` loop iterates over each item (city) in that list.

### **2. Using `range()` with `for` Loops**

The `range()` function generates a sequence of numbers, which you can use in a `for` loop when you want to repeat a block of code a specific number of times.

#### **Syntax of `range()`**:
```python
range(start, stop, step)
```
- `start`: The starting value (inclusive).
- `stop`: The ending value (exclusive).
- `step`: The increment (optional, default is 1).

#### **Example**: Counting from 1 to 10
```python
for i in range(1, 11):
    print(i)
```

This loop will print the numbers from 1 to 10.

**Output**:
```
1
2
3
4
5
6
7
8
9
10
```

#### **Example**: Counting by 2s from 1 to 10
```python
for i in range(1, 11, 2):
    print(i)
```

This loop prints only the odd numbers between 1 and 10.

**Output**:
```
1
3
5
7
9
```

### **3. Looping Over Strings**

You can also loop over each character in a string using a `for` loop.

#### **Example**: Printing each character in a string
```python
name = "Karnataka"
for letter in name:
    print(letter)
```

**Output**:
```
K
a
r
n
a
t
a
k
a
```

This loop goes through the string `"Karnataka"` one character at a time.

### **4. Nested `for` Loops**

You can also have **nested `for` loops**, which means a loop inside another loop. This is useful when working with multi-level data, like lists inside lists.

#### **Example**: Multiplication Table

Let’s print the multiplication table from 1 to 5 using a nested `for` loop.

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()  # To print an empty line after each table
```

**Output**:
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10

...

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
```

Here, the outer loop controls the first number (`i`), and the inner loop controls the second number (`j`). Together, they generate the multiplication table.

### **5. Using `break` in a `for` Loop**

The `break` statement is used to exit a loop early when a certain condition is met.

#### **Example**: Stop the loop when you find a specific item
Let’s say you are searching for a specific city in a list:

```python
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    if city == "Hubballi":
        print(f"Found {city}!")
        break
    print(city)
```

In this case, the loop stops when it finds `"Hubballi"` and prints `"Found Hubballi!"`.

**Output**:
```
Bengaluru
Mysuru
Found Hubballi!
```

### **6. Using `continue` in a `for` Loop**

The `continue` statement is used to skip the current iteration of the loop and move on to the next one.

#### **Example**: Skip a specific item in a list
Let’s skip `"Hubballi"` while looping through the cities:

```python
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    if city == "Hubballi":
        continue
    print(city)
```

**Output**:
```
Bengaluru
Mysuru
Mangaluru
```

Here, `"Hubballi"` is skipped, and the loop continues with the next city.

### **7. Looping Through a List with `enumerate()`**

The `enumerate()` function allows you to loop over a sequence and get both the index and the value of each item.

#### **Example**: Displaying the index and value of each city
```python
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for index, city in enumerate(cities):
    print(f"City {index + 1}: {city}")
```

**Output**:
```
City 1: Bengaluru
City 2: Mysuru
City 3: Hubballi
City 4: Mangaluru
```

### **8. Using `else` with `for` Loops**

You can also use an **`else` clause** with a `for` loop. The code inside the `else` block will execute once the loop finishes, unless the loop is terminated by a `break` statement.

#### **Example**:
```python
for city in cities:
    print(city)
else:
    print("No more cities!")
```

**Output**:
```
Bengaluru
Mysuru
Hubballi
Mangaluru
No more cities!
```

In this case, after the loop has finished going through all the cities, it prints `"No more cities!"`.

### **9. Real-Life Example: Distributing Laddus**

Imagine you have 5 laddus to distribute among friends. You can use a `for` loop to give each friend one laddu.

```python
laddus = 5
friends = ["Rahul", "Sneha", "Aman", "Priya"]

for friend in friends:
    if laddus > 0:
        print(f"{friend} gets a laddu!")
        laddus -= 1
    else:
        print("No laddus left!")
```

**Output**:
```
Rahul gets a laddu!
Sneha gets a laddu!
Aman gets a laddu!
Priya gets a laddu!
No laddus left!
```

Here, the loop goes through the list of friends and distributes the laddus one by one.

---

### **Homework**

1. **Multiples of 3**:
   - Write a `for` loop that prints all multiples of 3 between 1 and 30.

2. **Sum of First 10 Numbers**:
   - Write a program using a `for` loop that calculates the sum of numbers from 1 to 10.

3. **Print Your Name Letter by Letter**:
   - Write a program that takes your name as input and prints each letter of your name using a `for` loop.

4. **Count Vowels in a String**:
   - Write a program that counts how many vowels are in a given string using a `for` loop.

---
