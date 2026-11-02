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

text = "The cat sat on the mat. The cat was happy!"
freq = word_frequency(text)
print(freq)