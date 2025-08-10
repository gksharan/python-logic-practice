# ==============================================================================
# This script provides a simple solution to the classic "Two Sum" problem.
# The goal is to find two numbers in a list that add up to a specific target
# and return their indices.
# ==============================================================================

from typing import List, Optional

def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Finds the indices of two numbers in a list that sum to a target value.

    This solution uses a brute-force approach with nested loops.

    Args:
        nums (List[int]): A list of integers to search through.
        target (int): The integer target sum.

    Returns:
        Optional[List[int]]: A list containing the indices of the two numbers
                             if found, otherwise None.
    """
    # The outer loop iterates through each number in the list.
    for i in range(len(nums)):
        # The inner loop iterates through the numbers that come *after* the current number.
        # This prevents checking the same pair twice and a number with itself.
        for j in range(i + 1, len(nums)):
            # Check if the sum of the two numbers equals the target.
            if nums[i] + nums[j] == target:
                # If a pair is found, immediately return their indices.
                return [i, j]

    # If no pair is found after checking all combinations, return None.
    return None

# --- Main execution block ---
# This block runs the code when the script is executed directly.
if __name__ == "__main__":
    # Define the input list of numbers and the target.
    numbers_list = [3, 1, 5, 6]
    target_sum = 9

    # Call the function to find the result.
    result_indices = two_sum(numbers_list, target_sum)

    # Print the output in a user-friendly format.
    if result_indices:
        print(f"The numbers at indices {result_indices} (which are {numbers_list[result_indices[0]]} and {numbers_list[result_indices[1]]}) add up to the target of {target_sum}.")
        print("Indexes of numbers that add up to target:", result_indices)
    else:
        print("No two numbers in the list add up to the target.")
