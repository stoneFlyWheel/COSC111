# 3.1 - Distance and Speed ---------

distance_miles = 150
time_hours = 2.5

# Calculate speed_mph
speed_mph = distance_miles / time_hours

print("Speed (mph):", speed_mph)

# Convert to kilometers per hour (1 mile = 1.60934 km)
distance_km = 150 * 1.60934
speed_kph = distance_km / time_hours

print("Speed (kph):", speed_kph)

# Distance traveled in 4 hours
distance_in_4_hours = speed_mph * 4

print("Distance in 4 hours (miles):", distance_in_4_hours)

# 3.2 - Rectangle Calculator ---------

length = 15.5
width = 8.25

# Calculate perimeter
perimeter = (length * 2) + (width * 2)

# Calculate area
area = length * width

print("Rectangle length:", length, "inches")
print("Rectangle width:", width, "inches")
print("Perimeter:", perimeter, "inches")
print("Area:", area, "square inches")