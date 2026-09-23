# part A --------

def word_stats(text):
    word_list = text.split(" ")

    # find word count
    word_count = len(word_list)

    # find average word length
    total_letters = 0
    for word in word_list:
        total_letters += len(word)

    average_word_length = round(total_letters / word_count, 2)

    # find longest word
    biggest = word_list[0]
    for index in range(0, len(word_list)):
        if len(word_list[index]) > len(biggest):
            biggest = word_list[index]

    # format answer
    answer = {
        "word count:": word_count,
        "average word length": average_word_length,
        "longest word:": biggest
    }

    return answer

sample = "To be or not to be that is the question"
print(word_stats(sample)) 

# part B --------

def classify_sentence(sentence):
    # declare variables
    word_list = sentence.split()
    sentence_length = len(word_list)

    last_word = word_list[-1]
    # this looks silly, but this is the only way i could get it to work!
    last_word_list = list(str(last_word))

    # what i'm going to return
    answer = ""

    # get prefix
    if last_word_list[-1] == "?":
        answer += "question - "
    elif last_word_list[-1] == "!":
        answer += "exclamation - "
    else:
        pass

    # get length
    if sentence_length < 5:
        answer += "short"
    elif 5 <= sentence_length <= 10:
        answer += "medium"
    else:
        answer += "long"

    return answer

print(classify_sentence("What to do today?"))
print(classify_sentence("What a wonderful day it is today!"))
print(classify_sentence("The beautiful Persian calico cat sat on the long, hairy, headstrong mat."))

# reflection
# if i were to write one long conditional, if i made a mistake on one part of the logic,
# i'd have to rewrite 5 versions of the same thing! plus, it's more complicated to read,
# and it doesn't look as clean as doing it with two conditionals.