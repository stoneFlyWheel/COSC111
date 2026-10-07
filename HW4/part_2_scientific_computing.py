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