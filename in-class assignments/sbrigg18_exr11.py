with open("COSC111/in-class assignments/dracula.txt", "r") as file:
    for line in file:
        for word in line.split():
            if word.lower() == "dracula":
                print(word)