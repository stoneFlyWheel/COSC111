def word_frequency(text):
    words = []

    for word in text.lower().split():
        word = word.strip(".,!?;:\"'()")
        words.append(word)

    word_counter = {}

    for word in words:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    return word_counter

def most_common_word(freq):
    freq_list = list(freq.items())
    # freq_list indexes are tuples, like ("the", 3). to get an integer for max, i have
    # to get an index inside the index
    max = freq_list[0][1]
    # similarly here, for the actual word
    most_freq_word = freq_list[0][0]

    for item in range(len(freq_list)):
        # if the frequency is bigger than the current max
        if freq_list[item][1] > max:
            max = freq_list[item][1]
            most_freq_word = freq_list[item][0]

    return most_freq_word

# to make things easier on me, LOL
def print_examples(text):
    freq = word_frequency(text)

    print(freq)
    print(most_common_word(freq))

text = "The cat sat on the mat. The cat was happy!"
text2 = "We looked! Then we saw him step in on the mat! We looked! And we saw him! The Cat in the Hat!"

print_examples(text)
print_examples(text2)