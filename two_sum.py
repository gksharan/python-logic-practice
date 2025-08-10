# Function to solve the Two Sum problem
def two_sum(nums, target):
    # Go through each number in the list
    for i in range(len(nums)):
        # Go through the numbers after it
        for j in range(i + 1, len(nums)):
            # Check if the two numbers add up to the target
            if nums[i] + nums[j] == target:
                # If yes, return their indexes
                return [i, j]

# Example input
nums = [3,1,5,6]
target = 9

# Call the function and store result
result = two_sum(nums, target)

# Print the result
print("Indexes of numbers that add up to
