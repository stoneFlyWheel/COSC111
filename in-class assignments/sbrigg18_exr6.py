def print_word_lengths(text):
    total_word_length = 0

    # prints: word #_of_letters
    for word in text.split():
        print(word, len(word))
        total_word_length += len(word)

    print("Total letters:", total_word_length)

# calls

print_word_lengths("The quick brown fox jumped over the lazy dog")
print("---")
print_word_lengths("According to all known laws of aviation")