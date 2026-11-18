# Operators in Python — Homework Solutions

# -----------------------------------------------
# 1. Logical Operator Practice
# -----------------------------------------------

# Take two numbers as input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Both greater than 10
if num1 > 10 and num2 > 10:
    print("✅ Both numbers are greater than 10.")
else:
    print("❌ Both numbers are not greater than 10.")

# At least one less than 5
if num1 < 5 or num2 < 5:
    print("✅ At least one number is less than 5.")
else:
    print("❌ Neither number is less than 5.")

# The first is not greater than the second
if not (num1 > num2):
    print("✅ The first number is not greater than the second.")
else:
    print("❌ The first number is greater than the second.")


# -----------------------------------------------
# 2. Comparison Operator Challenge
# -----------------------------------------------

age = int(input("\nEnter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# -----------------------------------------------
# 3. Membership Operator Exercise
# -----------------------------------------------

text = input("\nEnter a string: ")

# Check if 'a' is in the string
if 'a' in text:
    print("✅ The letter 'a' is present in the string.")
else:
    print("❌ The letter 'a' is not present in the string.")

# Check if "Python" is not in the string
if "Python" not in text:
    print("✅ The word 'Python' is not found in the string.")
else:
    print("❌ The word 'Python' is found in the string.")


# -----------------------------------------------
# 4. Bitwise Operator Task
# -----------------------------------------------

a = int(input("\nEnter first integer (a): "))
b = int(input("Enter second integer (b): "))

print("\nBitwise AND (a & b):", a & b)
print("Bitwise OR (a | b):", a | b)
print("Bitwise XOR (a ^ b):", a ^ b)
print("Left shift a by 2 positions (a << 2):", a << 2)
print("Right shift b by 1 position (b >> 1):", b >> 1)
