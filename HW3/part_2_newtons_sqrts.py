# part A --------

def newton_sqrt(a, x, tolerance=0.0001):
    x2 = (x + (a / x)) / 2

    if abs(x2*x2 - a) < tolerance:
        print(f"Approximate square root of {a} is {x2}")
        return x2
    else:
        return newton_sqrt(a, x2, tolerance=0.0001)

print(newton_sqrt(25, 1)) # approximately 5.0
print(newton_sqrt(2, 1)) # approximately 1.4142...
print(newton_sqrt(100, 50)) # approximately 10.0 