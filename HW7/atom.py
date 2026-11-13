import random
import string

REACTOR_CORPUS = """
The reactor core contains fuel rods submerged in coolant. The coolant removes heat
from the fuel rods and carries it to the steam generator. Control rods absorb
neutrons and slow the fission reaction inside the reactor core. When control rods
are inserted the reactor power decreases. When control rods are withdrawn the
reactor power increases. The operator monitors reactor power, coolant temperature,
and pressure inside the containment building. If the coolant temperature rises too
quickly the operator may initiate a scram to shut down the reactor safely. A scram
inserts all control rods immediately to stop the fission reaction. The steam
generator produces steam that spins a turbine connected to a generator. The
generator produces electricity for the power grid. Safety systems monitor
radiation levels throughout the plant at all times. The containment building
prevents radioactive material from escaping into the environment.
"""

KEYWORD_RESPONSES = {
    # i added two new entries here
    "reactor": "A nuclear reactor widely defines converting heat from radioactive "
             "material into electricity.",
    "uranium": "Uranium is a material that's used in nuclear reactors. It has to "
             "be enriched in order to be more productive.",
    "scram": "A SCRAM immediately inserts all control rods to shut down the "
             "reactor as quickly as possible.",
    "meltdown": "A meltdown happens if fuel overheats and damages its cladding. "
                "Multiple safety systems exist to prevent this from occurring.",
    "coolant": "Coolant removes heat from the reactor core and carries it to "
               "the steam generator.",
    "turbine": "Steam from the steam generator spins a turbine, which is "
               "connected to an electrical generator.",
    "hello": "Hello! I'm ATOM, a reactor operations assistant. Ask me about "
             "the reactor, coolant, control rods, or a scram.",
}

FALLBACK_RESPONSE = ("I'm not sure about that. Try asking about the reactor, "
                      "coolant, control rods, or a scram.")


def clean_words(text):
    """Return a list of lowercase words from text, with punctuation removed."""

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


def build_successor_map(words):
    """Return a dict mapping each word to a list of words that followed it."""

    # make bigrams
    bigrams = []

    for i in range(len(words) - 1):
        pair = (words[i], words[i + 1])
        bigrams.append(pair)

    # use bigrams
    successors = {}
    
    for word, next_word in bigrams:
        if word in successors:
            successors[word].append(next_word)
        else:
            successors[word] = [next_word]
    
    return successors



def generate_text(successors, start_word, num_words):
    """Generate a string of num_words words, starting at start_word, by
    repeatedly choosing a random successor."""

    target_word = start_word
    babble = ""

    for word in range(num_words):
        babble = babble + target_word + " "

        if successors[target_word] != "":
            target_word = random.choice(successors[target_word])
        else:
            break

    return babble


def get_response(user_input, successors):
    """Decide how ATOM should respond to the user's input."""

    clean_input = clean_words(user_input)

    # prioritizing keyword reponses
    for word in clean_input:
        if word in KEYWORD_RESPONSES:
            return KEYWORD_RESPONSES[word]

    for word in clean_input:
        if word in successors:
            return generate_text(successors, word, 9)

    return FALLBACK_RESPONSE


def main():
    words = clean_words(REACTOR_CORPUS)
    successors = build_successor_map(words)

    print("ATOM: Hello, I'm ATOM, your reactor operations assistant.")
    print("ATOM: Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("ATOM: Goodbye. Stay safe out there.")
            break
        response = get_response(user_input, successors)
        print("ATOM:", response)


if __name__ == "__main__":
    main()