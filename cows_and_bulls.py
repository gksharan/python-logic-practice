import random

def get_secret_number():
    """Generates a random 4-digit number."""
    # Ensure the number does not have repeating digits for a more traditional game.
    digits = list('0123456789')
    random.shuffle(digits)
    return ''.join(digits[:4])

def get_user_guess():
    """Prompts the user for a valid 4-digit number guess."""
    while True:
        guess = input("Guess a 4-digit number: ")
        if guess.isdigit() and len(guess) == 4:
            return guess
        else:
            print("Invalid input. Please enter a 4-digit number.")

def check_cows_and_bulls(secret, guess):
    """
    Checks the user's guess against the secret number and returns the
    number of bulls and cows.
    """
    bulls = 0
    cows = 0
    secret_list = list(secret)
    guess_list = list(guess)

    # First, find the bulls and remove them to avoid double-counting.
    i = 0
    while i < len(secret_list):
        if secret_list[i] == guess_list[i]:
            bulls += 1
            secret_list.pop(i)
            guess_list.pop(i)
        else:
            i += 1

    # Then, find the cows from the remaining digits.
    for digit in guess_list:
        if digit in secret_list:
            cows += 1
            secret_list.remove(digit)

    return bulls, cows

def play_game():
    """The main game loop for Cows and Bulls."""
    print("🔒 A secret 4-digit number has been generated!")
    secret_number = get_secret_number()

    # Uncomment the next line for testing/debugging
    # print(f"DEBUG: The secret number is {secret_number}")

    while True:
        user_guess = get_user_guess()
        bulls, cows = check_cows_and_bulls(secret_number, user_guess)

        print(f"🐂 Bulls: {bulls}, 🐮 Cows: {cows}")

        if bulls == 4:
            print("Congratulations! You've guessed the correct number!")
            break

if __name__ == "__main__":
    play_game()