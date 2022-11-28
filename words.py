def print_upper_words(words, start_letters):
    """Print out each word in upper case on a new line"""

    for word in words:
        if word.upper().startswith(tuple(start_letters)):
            print(word.upper())