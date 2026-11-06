def clean_words(text):
    """
    Takes a string of text and returns a list of lowercase words
    with punctuation removed.
    """

    punctuation = ".,!?;:\"'"
    words = []

    for word in text.split():
        word = word.lower()
        cleaned = ""

        for char in word:
            if char not in punctuation:
                cleaned += char

        if cleaned != "":
            words.append(cleaned)

    return words

   

def build_bigrams(words):
    bigrams = []

    for i in range(len(words) - 1):
        pair = (words[i], words[i + 1])
        bigrams.append(pair)

    return bigrams


def build_successor_map(bigrams):
    successors = {}

    for word, next_word in bigrams:
        if word in successors:
            successors[word].append(next_word)
        else:
            successors[word] = [next_word]

    return successors

def main():
    file = open("COSC111/in-class assignments/input2.txt", "r", encoding="utf-8")
    text = file.read()
    file.close()

    words = clean_words(text)
    bigrams = build_bigrams(words)
    successors = build_successor_map(bigrams)


    print("Total words:", len(words))
    print("Total bigrams:", len(bigrams))
    print()

    for word in ["the", "to", "was", "were"]:
        if word in successors:
            print(word, "->", successors[word][:10])

        else:
            print(word, "not found in text")

if __name__ == "__main__":
    main()

# 1
# connector words and pronouns (such as "with," "the," and "he") tend to have super long successor lists
# because they can be used in a variety of sentences. obscure words like "austere," or, well, "obscure,"
# don't have as long successor lists because less sentences use them

# 2
# if you can get an accurate handle on what's the most likely word to come next, random.choice()
# has a better chance of producing something readable!

# 3
# it wouldn't read them correctly, and there would be a lot of duplicates. plus random.choice() would
# random punctuation everywhere!