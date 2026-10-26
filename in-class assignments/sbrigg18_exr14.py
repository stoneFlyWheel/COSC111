words = ["apple", "banana", "apple", "orange", "banana", "apple"]

def dict_builder(word_list):
    word_counter = {}

    for word in word_list:
        # if you've already counted the word
        if word in word_counter:
            word_counter[word] += 1
        # if it's new
        else:
            word_counter[word] = 1
    return word_counter

print(dict_builder(words))