# part A --------

def first_reading_over_threshold(readings, threshold):
    index = 0
    while index < len(readings):
        if readings[index] > threshold:
            return index
        index += 1
    return -1

data = [12.1, 14.5, 15.0, 22.7, 18.3, 30.1]
print(first_reading_over_threshold(data, 20)) # 3
print(first_reading_over_threshold(data, 50)) # -1 
print(first_reading_over_threshold(data, 10))

# part B --------

def estimate_sqrt(a, x, tolerance=0.0001):
    while abs(x*x - a) >= tolerance:
        x = (x + a/x) / 2
    return x

print(estimate_sqrt(25, 1)) # approximately 5.0
print(estimate_sqrt(2, 1)) # approximately 1.4142... 
print(estimate_sqrt(100, 3)) 

# this while loop version uses much less data! while the recursive one was cooler,
# this one is shorter and more to the point, as well as more efficient.