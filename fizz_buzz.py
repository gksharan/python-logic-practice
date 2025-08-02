#This function implements the FizzBuzz logic, checking for divisibility by 3, 5, or both.
def fizz_buzz(number):
    """Returns 'Fizz', 'Buzz', 'FizzBuzz', or the number itself."""
    if (number % 3 == 0) and (number % 5 == 0):
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

if __name__ == "__main__":
    # Example usage:
    print(fizz_buzz(3))
    print(fizz_buzz(5))
    print(fizz_buzz(15))
    print(fizz_buzz(7))