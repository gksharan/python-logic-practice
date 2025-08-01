import random
import string

def generate_weak_password():
    """Generates a weak password by combining two random words."""
    words = ["apple", "monkey", "blue", "car", "tree"]
    return random.choice(words) + random.choice(words)

def generate_strong_password():
    """Generates a strong, 12-character password with a mix of characters."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(12))

def main():
    """Main function to prompt the user and generate the password."""
    strength = input("Weak or strong password? ").lower()

    if strength == "weak":
        password = generate_weak_password()
    elif strength == "strong":
        password = generate_strong_password()
    else:
        print("Invalid input. Please choose 'weak' or 'strong'.")
        return

    print("Your password is:", password)

if __name__ == "__main__":
    main()