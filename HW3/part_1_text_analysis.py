# part A

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

print(word_stats("to be or not to be, that is the question"))




