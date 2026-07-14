# Homework: Tuples and Sets in Python

# -------------------------------
# 1️. Tuple Operations
# -------------------------------

# Create a tuple with 5 elements
my_tuple = (10, 20, 30, 40, 50)
print("Original tuple:", my_tuple)

# Try to modify one of the elements (This will raise an error)
try:
    my_tuple[1] = 100
except TypeError as e:
    print("Error when trying to modify tuple:", e)

# Perform slicing on the tuple to extract the second and third elements
sliced_tuple = my_tuple[1:3]
print("Sliced tuple (2nd and 3rd elements):", sliced_tuple)

# Concatenate the tuple with another tuple
another_tuple = (60, 70)
combined_tuple = my_tuple + another_tuple
print("Concatenated tuple:", combined_tuple)


# -------------------------------
# 2️. Set Operations
# -------------------------------

# Create two sets of favorite fruits
my_fruits = {"apple", "banana", "cherry"}
friends_fruits = {"mango", "banana", "grape"}

# Find union, intersection, and difference
print("\nUnion of fruits:", my_fruits | friends_fruits)
print("Intersection of fruits:", my_fruits & friends_fruits)
print("Difference (my fruits - friend's):", my_fruits - friends_fruits)

# Add a new fruit to your set
my_fruits.add("orange")
print("After adding orange:", my_fruits)

# Remove a fruit using remove() and discard()
my_fruits.remove("banana")  # removes banana
print("After remove('banana'):", my_fruits)

# discard() doesn’t raise an error if fruit doesn’t exist
my_fruits.discard("pineapple")
print("After discard('pineapple') (no error even if not present):", my_fruits)

# Try removing non-existing fruit using remove() → raises error
try:
    my_fruits.remove("pineapple")
except KeyError as e:
    print("Error when using remove() on non-existing element:", e)


# -------------------------------
# 3️. Tuple and Set Comparison
# -------------------------------

# Create a list of elements
my_list = [1, 2, 3, 3, 2]

# Convert it into both a tuple and a set
my_tuple_from_list = tuple(my_list)
my_set_from_list = set(my_list)

print("\nTuple from list:", my_tuple_from_list)
print("Set from list:", my_set_from_list)

# Try adding new elements
# Tuples are immutable, sets are mutable
try:
    my_tuple_from_list += (4,)
    print("Tuple after adding element using +:", my_tuple_from_list)
except TypeError as e:
    print("Error adding element to tuple:", e)

my_set_from_list.add(4)
print("Set after adding element:", my_set_from_list)

# Observation: Tuples allow duplicates and are immutable.
# Sets remove duplicates and are mutable.
