# This script creates a simple command-line calculator.

def main():
    """
    The main function to run the basic calculator application.
    """
    print("Welcome to the Basic Calculator! 🧮")

    try:
        # Get the first number from the user
        num1 = float(input("Enter first number: "))

        # Get the operator from the user
        operator = input("Enter operator (+, -, *, /): ")

        # Get the second number from the user
        num2 = float(input("Enter second number: "))

        result = 0 # Initialize result variable

        # Perform calculation based on the operator
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # Handle division by zero
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return # Exit the function if division by zero
            else:
                result = num1 / num2
        else:
            # Handle invalid operator
            print("Error: Invalid operator. Please use +, -, *, or /.")
            return # Exit the function for invalid operator

        # Print the final result
        print("Result:", result)

    except ValueError:
        # Catch errors if the user enters non-numeric input for numbers
        print("Error: Invalid number entered. Please enter numeric values.")
    
    print("\nThank you for using the calculator! ✨")

# This ensures that the 'main' function runs when the script is executed directly.
if __name__ == "__main__":
    main()
