def print_upper_words(words, start_letters):
    """Print out each word in upper case on a new line"""

    for word in words:
        for letter in start_letters:
            if word.upper().startswith(letter.upper()):
                print(word.upper())


