# ==============================================================================
# Demonstrates basic Stack operations using a Python list.
# A stack follows the Last-In, First-Out (LIFO) principle.
# ==============================================================================

# Initialize an empty list to act as a stack.
stack = []

# --- PUSH operation ---
# The 'append()' method adds elements to the top of the stack.
print("--- Pushing elements onto the stack ---")
stack.append(1)
stack.append(2)
stack.append(3)

print("Initial stack:", stack)

# --- POP operation ---
# The 'pop()' method removes and returns the last element added to the stack.
print("\n--- Popping elements from the stack ---")
popped_element = stack.pop()
print("Popped element:", popped_element)
print("Stack after first pop:", stack)

popped_element = stack.pop()
print("Popped element:", popped_element)
print("Stack after second pop:", stack)
