def letter_frequency(text):
    letter_list = []

    for word in text.lower().split():
        letters = list(word)
        
        for letter in letters:
            if letter not in list("1234567890.,!?;:\"'()"):
                letter_list.append(letter)
    
    letter_counter = {}

    for letter in letter_list:
        if letter in letter_counter:
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1

    return letter_counter

def vowel_percentage(freq):
    vowel_list = ["a", "e", "i", "o", "u", "y"]
    num_of_values = 0
    num_of_vowels = 0

    for letter, num in freq.items():
        if letter in vowel_list:
            num_of_vowels += num

        num_of_values += num

    vowel_percent = (num_of_vowels / num_of_values) * 100
    return round(vowel_percent, 1)

def run_my_functions(text):
    freq = letter_frequency(text)
    print(freq)
    print(vowel_percentage(freq))

text = "Hello world!"
text2 = "Salutations, Earth!"

run_my_functions(text)
run_my_functions(text2)