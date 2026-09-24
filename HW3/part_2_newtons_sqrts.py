import math

# part A --------

def newton_sqrt(a, x, tolerance=0.0001):
    global total_guesses
    total_guesses += 1
    x2 = (x + (a / x)) / 2

    if abs(x2*x2 - a) < tolerance:
        print(f"Approximate square root of {a} is {x2}")
        print(f"Total guesses: {total_guesses}")
        return x2
    else:
        return newton_sqrt(a, x2, tolerance=0.0001)

print(newton_sqrt(25, 1)) # approximately 5.0
print(newton_sqrt(2, 1)) # approximately 1.4142...
print(newton_sqrt(100, 50)) # approximately 10.0 

# part B --------

def is_close(a, b, tolerance=0.0001):
    if abs(a - b) < tolerance:
        return True
    else:
        return False
    
print(is_close(newton_sqrt(2, 1), math.sqrt(2))) # True

# if you start with a bad initial guess, it'll take a really long time
# to get the right answer! it'll still converge, but will take more time
# to process