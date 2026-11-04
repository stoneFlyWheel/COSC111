# this is from part 1
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

def compare_texts(text1, text2):
    common_set = {}
    unique_set = {}

    text1_freq = word_frequency(text1)
    text2_freq = word_frequency(text2)

