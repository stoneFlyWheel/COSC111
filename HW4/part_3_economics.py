# part A --------

def find_break_even_month(cashflows):
    total = 0
    for month in range(len(cashflows)):
        total += cashflows[month]
        if total > 0:
            return month
    return -1

flows = [-500, -200, -100, 150, 300, 400]
flows2 = [-600, -100, -200, 150, 300, 400, 1000]
print(find_break_even_month(flows)) # 5
print(find_break_even_month(flows2)) # 6


# part B --------
 
def years_to_double(principal, rate):
    years = 0
    current_value = principal
    while current_value < 2 * principal:
        current_value += current_value * rate
        years += 1
    return years

print(years_to_double(1000, 0.07)) # 11
print(years_to_double(1000, 0.10)) # 8 
print(years_to_double(1000, 0.15)) # 5

# the non-recursive version was much easier to reason out! this one is also
# safer for big numbers/years, since it only runs one function, not a bajillion