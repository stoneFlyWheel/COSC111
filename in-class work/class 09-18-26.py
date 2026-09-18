x = 12345

# last digit
last_digit = x % 10
print(last_digit)

# last two digits
last_two_digits = x % 100
print(last_two_digits)

# clock duration
start = 11 # am
duration = 3 # hours
end = (duration + start) % 12
print(end)