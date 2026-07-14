# 🧩 3.md — Homework Solutions

# -----------------------------
# Simple Greeting Program
# -----------------------------
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # converting input to integer

# Using + operator
print("Hello, " + name + "! You are " + str(age) + " years old.")

# Using f-string
print(f"Hello, {name}! You are {age} years old.")


# -----------------------------
# String Manipulation Exercise
# -----------------------------
sentence = input("Enter a sentence: ")

# Applying string methods
uppercase_sentence = sentence.upper()
lowercase_sentence = sentence.lower()
replaced_sentence = sentence.replace(" ", "_")
stripped_sentence = sentence.strip()

print("Uppercase:", uppercase_sentence)
print("Lowercase:", lowercase_sentence)
print("Replaced:", replaced_sentence)
print("Stripped:", stripped_sentence)


# -----------------------------
# Character Counter
# -----------------------------
text = input("Enter a string: ")
count = len(text.replace(" ", ""))  # removes spaces and counts remaining characters

print(f"Number of characters (excluding spaces): {count}")


# -----------------------------
# Escape Sequence Practice
# -----------------------------
print("Hello\n\tWorld")
print("This is a backslash: \\")

