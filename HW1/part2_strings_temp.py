# 2.1 - String Operations ---------

# Create a variable called first_name
first_name = "sage"

# Create a variable called last_name
last_name = "briggs"

# Concatenate them into full_name (include a space)
full_name = last_name + first_name

# Use len() to find the length of full_name
# Store in name_length
name_length = len(full_name)

# Repeat your first name 3 times (no spaces)
# Store in repeated_name
repeated_name = first_name * 3

# (Harder) Repeat your first name 3 times with commas
# Example: "Alex,Alex,Alex"
# Store in repeated_with_commas
repeated_with_commas = ((first_name + ",") * 3)
repeated_with_commas = repeated_with_commas[:-1]

print("Full name:", full_name)
print("Length:", name_length)
print("Repeated:", repeated_name)
print("Repeated with commas:", repeated_with_commas)

# 2.2 - Temperature Conversion ---------

# Given temperature in Fahrenheit
temp_f = 72

# Convert to Celsius
# Store in temp_c
temp_c = (temp_f - 32) * (5/9)

print(temp_f, "degrees Fahrenheit is", temp_c, "degrees Celsius")

# Convert Celsius to Fahrenheit
celsius = 101
# store in fahrenheit
fahrenheit = (celsius * (9/5)) + 32

print(celsius, "degrees Celsius is", fahrenheit, "degrees Fahrenheit")

# Round the Fahrenheit result to the nearest whole number
# name the variable rounded_f
rounded_f = round(fahrenheit)

print("Rounded Fahrenheit:", rounded_f)