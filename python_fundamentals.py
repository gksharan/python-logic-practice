# This script demonstrates fundamental Python concepts including:
# - Basic printing
# - Variable assignment and f-strings
# - Function definition with type hints
# - List creation and iteration
# - Using a main execution block for organization

def add_numbers(a: int, b: int) -> int:
    """
    Adds two integer numbers and returns their sum.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers.
    """
    # This function now only calculates and returns the sum,
    # making it more reusable. The printing is handled by the caller.
    return a + b

def greet_users(names: list[str]):
    """
    Iterates through a list of names and prints a personalized greeting for each.

    Args:
        names (list[str]): A list of strings, where each string is a name.
    """
    for name in names:
        print(f'Hello {name} 👋')

def main():
    """
    The main function to run the script's demonstrations.
    """
    # 1. Basic Output and Variables
    print("Hello world! 🌍")

    user_name = 'Roy'
    user_age = 20
    print(f'My Name is {user_name}, and my age is {user_age} years old.')

    # 2. Function Usage
    print('\n--- Demonstrating Function Usage ---')
    # Call the add_numbers function and print the returned result
    result1 = add_numbers(10, 20)
    print(f'Adding 10 + 20 we get: {result1}')

    result2 = add_numbers(19, 90)
    print(f'Adding 19 + 90 we get: {result2}')

    # 3. List and Loop Iteration
    print('\n--- Demonstrating List Iteration ---')
    # A list of names with type hint for clarity
    names_list: list[str] = ['Kavya', 'Pratishka', 'Padma', 'Madu', 'Dhu', 'Akku', 'Aavi', 'Abin']
    greet_users(names_list)

# This block ensures that `main()` is called only when the script is executed directly,
# not when it's imported as a module into another script.
if __name__ == '__main__':
    main()
