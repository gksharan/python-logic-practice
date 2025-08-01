def reverse_words_in_sentence(sentence):
    """
    Reverses the order of words in a given sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The sentence with the order of words reversed.
    """
    # Split the sentence into a list of words, reverse the list,
    # and then join the words back into a single string.
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

# Get input from the user, convert it to uppercase, and call the function.
user_input = input("Enter a sentence: ")
reversed_sentence = reverse_words_in_sentence(user_input.upper())
print(reversed_sentence)