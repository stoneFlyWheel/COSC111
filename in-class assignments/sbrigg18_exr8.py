import sys

def is_even(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

def classify_number(n):
    message = ""

    if n == 0:
        message += "zero"
    else:
        if n > 0:
            message += "positive "
        elif n < 0:
            message += "negative "
        message += is_even(n)

    return message

running = True
while running:
    num = input("please enter a number: ")
    try:
        num = int(num)
        running = False
    except:
        print("Invalid input. Please enter a valid number.")

print(classify_number(num))