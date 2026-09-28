# for letter in "Hello, World!":
    # print(letter, end = " ")
"""
select = "SPOCK"
select = select.lower()
if select == "spock":
    select = select[0].upper() + select[1:]
print(select)
"""

with open("COSC111/in-class work/word.txt", "r") as file:
    content = file.read()
    print(content)