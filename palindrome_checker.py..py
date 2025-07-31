def is_palindrome(text):
    """
    Checks if a given string is a palindrome.

    A palindrome is a word, phrase, or sequence that reads the same backward as forward.
    This function compares the original string with its reverse to determine if it's a palindrome.

    Args:
        text (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Normalize the string by removing spaces and converting to lowercase for a more robust check.
    # For a simple check, you can use `return text == text[::-1]`
    # We will use a more robust check to handle phrases.
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]


def main():
    """
    Prompts the user for a string and checks if it's a palindrome.
    """
    user_string = input("Enter a string: ")

    if is_palindrome(user_string):
        print(f"'{user_string}' is a palindrome.")
    else:
        print(f"'{user_string}' is not a palindrome.")


if __name__ == "__main__":
    main()