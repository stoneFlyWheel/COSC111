def build_bigrams(words):
    bigrams = []

    for i in range(len(words) - 1):
        pair = (words[i], words[i+1])
        bigrams.append(pair)

    return bigrams

# had to modify this so my computer didn't throw a fit
file = open("COSC111/in-class assignments/input2.txt", "r", encoding="utf-8")
text = file.read()
file.close()


word_list = text.split()

bigrams = build_bigrams(word_list)

#4) print out results (code is given, but you may need to adjust variable names if you used different ones)
print("Total words:", len(word_list))
print("Total bigrams:", len(bigrams))

print("Some of the bigrams:")
for bigram in bigrams[1000:1010]:
    print(bigram)