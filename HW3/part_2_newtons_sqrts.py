# part A --------

def newton_sqrt(x, a, tolerance=0.0001):
    x2 = ((x + a) / x) / 2

    if abs(x2*x2 - a) < tolerance:
        return x2
    else:
        newton_sqrt(x2, a, tolerance=0.0001)

print(newton_sqrt(25, 1)) # approximately 5.0
print(newton_sqrt(2, 1)) # approximately 1.4142...
print(newton_sqrt(100, 50)) # approximately 10.0 