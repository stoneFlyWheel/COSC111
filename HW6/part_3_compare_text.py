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
    common_set = set()
    unique_set = set()

    text1_freq = word_frequency(text1)
    text2_freq = word_frequency(text2)

    for word in text1_freq:
        if word in text2_freq:
            common_set.add(word)
        else:
            unique_set.add(word)

    for word in text2_freq:
        if word not in text1_freq:
            unique_set.add(word)

    return (common_set, unique_set)

text1 = "the quick brown fox jumps over the lazy dog"
text2 = "the lazy cat sleeps all day"
common, unique = compare_texts(text1, text2)
print("Common words:", common)
print("Unique words:", unique)