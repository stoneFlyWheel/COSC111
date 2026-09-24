# part A --------

def compound_interest(principal, rate, years):
    return principal * (1 + rate) ** years

print(compound_interest(1000, 0.05, 10)) # approximately 1628.89
print(compound_interest(500, 0.02, 0)) # 500.0 

# part B --------

print("---")

years = 0

def years_to_double(principal, rate):
    global years

    if compound_interest(principal, rate, years) < 2 * principal:
        years += 1
        return years_to_double(principal, rate)
    else:
        result = years
        years = 0
        return f"Years to double: {result}"

print(years_to_double(1000, 0.07)) # 11 (rule of 72 estimate: ~72/7 ≈ 10.3, rounds up to 11)
print(years_to_double(1000, 0.10))