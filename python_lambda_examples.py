# ==============================================================================
# This script demonstrates different uses of Python lambda functions.
# A lambda function is a small, anonymous function defined with the 'lambda' keyword.
# It can take any number of arguments, but can only have one expression.
# ==============================================================================

# --- Example 1: Checking a number's sign ---
# A lambda function to determine if a number is positive, negative, or zero.
# It uses a conditional expression (ternary operator) to achieve this in one line.
check_sign = lambda num: "positive" if num > 0 else "negative" if num < 0 else "zero"

print("--- Checking Number Signs ---")
print(f"The number 3 is: {check_sign(3)}")
print(f"The number -9 is: {check_sign(-9)}")
print(f"The number 0 is: {check_sign(0)}")

# --- Example 2: Checking for even or odd numbers ---
# A simple lambda function to check if a number is even or odd.
check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"

print("\n--- Checking Even or Odd ---")
print(f"The number 4 is: {check_even_odd(4)}")
print(f"The number 7 is: {check_even_odd(7)}")

# --- Example 3: Using lambdas in a list comprehension ---
# This creates a list of lambda functions. Each lambda function remembers the
# value of 'x' from the loop and returns x multiplied by 10 when called.
# 'arg=x' is a crucial part of this. It captures the current value of x
# for each lambda, preventing all functions from using the final value of x.
print("\n--- List of Lambda Functions ---")
lambda_list = [lambda arg=x: arg * 10 for x in range(1, 5)]

# Iterate through the list of functions and call each one.
for func in lambda_list:
    print(f"Result: {func()}")
