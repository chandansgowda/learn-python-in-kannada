# 🧩 Homework Solutions for 5.md (Lists in Python)

# -----------------------------------------
# 1️⃣ List Manipulation Exercise
# -----------------------------------------

# Step 1: Create a list of 5 items
items = ["apple", "banana", "cherry", "date", "fig"]
print("Original list:", items)

# Step 2: Add a new item to the end
items.append("grape")
print("After adding an item at the end:", items)

# Step 3: Add another item at the second position
items.insert(1, "kiwi")
print("After inserting 'kiwi' at second position:", items)

# Step 4: Remove the third item from the list
items.pop(2)
print("After removing the third item:", items)


# -----------------------------------------
# 2️⃣ Reverse and Sort a List
# -----------------------------------------

# Step 1: Create a list of numbers
numbers = [10, 3, 7, 2, 9, 1]
print("\nOriginal numbers list:", numbers)

# Step 2: Sort the list in descending order
numbers.sort(reverse=True)
print("Sorted in descending order:", numbers)

# Step 3: Reverse the sorted list
numbers.reverse()
print("After reversing the sorted list:", numbers)
