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
        message += str(is_even(n))

    return message


# Test cases (no need to change anything below this line)
print(classify_number(0))   # should print "zero"
print(classify_number(4))   # "positive even"
print(classify_number(-7))  # "negative odd"
print(classify_number(-10)) # "negative even"