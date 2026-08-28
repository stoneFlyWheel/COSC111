import math
miles = '123'
kilometers = int(miles) * 1.61
hours = 2
average_speed = int(miles) / hours
average_speed_km = kilometers / hours

print('Trip distance:', miles, 'miles')
print('Trip distance in km:', kilometers, 'km')
# print('Average speed: 61.5 mph')
print('Average speed:', average_speed, 'mph')
print('Rounded speed:', round(average_speed)) # prints an integer 
print('Average speed in km:', average_speed_km, 'kph')
print('Rounded speed:', round(average_speed_km, 1))