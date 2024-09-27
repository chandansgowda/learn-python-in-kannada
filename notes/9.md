## **While Loops in Python**

A **loop** is a programming structure that repeats a set of instructions as long as a specified condition is True. In Python, the **`while` loop** allows you to repeatedly execute a block of code as long as the condition is True.

### **1. The Basic Structure of a `while` Loop**

The `while` loop repeatedly executes a block of code as long as the condition is `True`.

#### **Syntax**:
```python
while condition:
    # Code to execute as long as condition is True
```

#### **Example**:
Let’s print numbers from 1 to 5 using a `while` loop.

```python
i = 1
while i <= 5:
    print(i)
    i += 1  # Incrementing i by 1 after each iteration
```

- The loop starts with `i = 1` and checks if `i <= 5`.
- As long as this condition is `True`, it prints the value of `i` and increases it by 1 (`i += 1`).
- The loop ends when `i` becomes 6, as the condition `i <= 5` becomes `False`.

**Output**:
```
1
2
3
4
5
```

### **2. Common Example: Counting Sheep**

Let’s relate this to a common example: Imagine you're counting sheep to fall asleep.

```python
sheep_count = 1
while sheep_count <= 10:
    print(f"Sheep {sheep_count}")
    sheep_count += 1
```

This prints `"Sheep 1"`, `"Sheep 2"`, and so on, until `"Sheep 10"`. After that, the loop stops.

### **3. Avoiding Infinite Loops**

A **`while` loop** can run indefinitely if the condition is always `True`. To prevent this, ensure that the condition eventually becomes `False`.

#### **Example of an Infinite Loop**:
```python
i = 1
while i <= 5:
    print(i)
    # Forgot to update i, so the condition remains True forever!
```

In this case, the loop will keep printing `1` forever because `i` is never incremented, so the condition `i <= 5` will always be `True`.

To avoid this, make sure to **update the variable** that controls the condition within the loop.

### **4. Using `break` to Exit a `while` Loop**

You can use the `break` statement to exit a loop when a certain condition is met.

#### **Example**:
Let’s stop counting sheep after 5 sheep, even though the condition allows counting up to 10:

```python
sheep_count = 1
while sheep_count <= 10:
    print(f"Sheep {sheep_count}")
    if sheep_count == 5:
        print("That's enough counting!")
        break
    sheep_count += 1
```

- The loop stops after `"Sheep 5"` because of the `break` statement, even though the condition was `sheep_count <= 10`.

**Output**:
```
Sheep 1
Sheep 2
Sheep 3
Sheep 4
Sheep 5
That's enough counting!
```

### **5. Using `continue` to Skip an Iteration**

The `continue` statement is used to skip the current iteration and move on to the next one.

#### **Example**:
Let’s say you want to skip counting sheep that are number 4:

```python
sheep_count = 1
while sheep_count <= 5:
    if sheep_count == 4:
        sheep_count += 1
        continue
    print(f"Sheep {sheep_count}")
    sheep_count += 1
```

Here, when `sheep_count` is 4, the `continue` statement skips printing `"Sheep 4"`, and the loop continues with `sheep_count = 5`.

**Output**:
```
Sheep 1
Sheep 2
Sheep 3
Sheep 5
```

### **6. Using `while` Loops for User Input**

You can use a `while` loop to repeatedly ask the user for input until they provide valid data.

#### **Example**:
Let’s ask the user for a PIN until they enter the correct one:

```python
pin = ""
correct_pin = "1234"
while pin != correct_pin:
    pin = input("Enter your PIN: ")
    if pin != correct_pin:
        print("Incorrect PIN. Try again.")
print("PIN accepted. You can proceed.")
```

- The loop keeps running until the user enters the correct PIN.
- If the user enters an incorrect PIN, they are prompted to try again.

### **7. Real-life Example: KSRTC Bus Seats Availability**

Let’s say you want to simulate a KSRTC bus seat booking system. The bus has 5 available seats. Each time a seat is booked, the available seats decrease.

```python
available_seats = 5

while available_seats > 0:
    print(f"{available_seats} seats available.")
    booking = input("Do you want to book a seat? (yes/no): ").lower()
    
    if booking == "yes":
        available_seats -= 1
        print("Seat booked!")
    else:
        print("No booking made.")

print("All seats are booked!")
```

Here, the loop keeps running until all seats are booked. It checks the available seats and asks the user if they want to book one. The loop stops when there are no more seats available.

**Output Example**:
```
5 seats available.
Do you want to book a seat? (yes/no): yes
Seat booked!
4 seats available.
Do you want to book a seat? (yes/no): yes
Seat booked!
...
1 seats available.
Do you want to book a seat? (yes/no): yes
Seat booked!
All seats are booked!
```

### **8. Nested `while` Loops**

You can also nest `while` loops inside each other. This can be useful in more complex scenarios, such as checking multiple conditions or dealing with multi-level data.

#### **Example**:
Let’s simulate a snack machine that allows users to buy snacks as long as both the machine has snacks and the user has money:

```python
snacks_available = 3
money = 10

while snacks_available > 0 and money > 0:
    print(f"Snacks available: {snacks_available}. Money: ₹{money}")
    buy = input("Do you want to buy a snack for ₹5? (yes/no): ").lower()
    
    if buy == "yes" and money >= 5:
        snacks_available -= 1
        money -= 5
        print("Snack purchased!")
    else:
        print("No purchase made.")
        
print("Either snacks are sold out or you are out of money.")
```

This loop will continue as long as there are snacks available and the user has money. Once one condition is no longer True, the loop stops.

---

### **Homework**

1. **Basic Counting with `while` Loop**:
   - Write a program that counts from 1 to 10 using a `while` loop.

2. **Odd Numbers Printer**:
   - Create a program that prints all odd numbers between 1 and 20 using a `while` loop.

3. **Ticket Booking Simulation**:
   - Write a program that simulates a bus ticket booking system. The bus has 8 seats. Each time a seat is booked, the available seats decrease. When there are no seats left, the loop stops and displays a message saying "All seats are booked."

4. **Countdown Timer**:
   - Write a program that counts down from 10 to 1 using a `while` loop and prints "Happy New Year!" after the countdown is over.

---


