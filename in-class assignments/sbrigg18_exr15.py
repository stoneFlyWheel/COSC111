def build_word_counts(text):
    word_dict = {}

    word_list = text.split()
    # shamelessly stolen from the internet v
    stop_words = ["the", "and", "a", "to", "of", "in", "that", "it", "is", "was", "he", "for", "on", "are", "as", "with", "his", "they", "be", "at"]

    for word in word_list:
        word = word.lower().strip(".,!?;:\"'()")

        if word in stop_words:
            continue

        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict


# ----- Driver code (no need to modify)  -----

# the way provided on canvas doesn't work for my computer :( sorry
infile = open("COSC111/in-class assignments/input.txt", "r")
text = infile.read()
infile.close()

word_counts = build_word_counts(text)

# Sort the (word, count) pairs by count, highest first
sorted_counts = sorted(word_counts.items(), key=lambda pair: pair[1],reverse=True)

print("Top 10 most common words:")
for word, count in sorted_counts[:10]:
    print(word, ":", count)