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
    max = freq_list[0][1]
    most_freq_word = freq_list[0][0]

    for item in range(len(freq_list)):
        if freq_list[item][1] > max:
            max = freq_list[item][1]
            most_freq_word = freq_list[item][1]

    return most_freq_word

text = "The cat sat on the mat. The cat was happy!"
freq = word_frequency(text)
print(freq)
print(most_common_word(freq))