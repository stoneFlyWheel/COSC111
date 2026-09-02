def amount_owed(principal, annual_rate, years):
    """
    principal = initial money owed
    annual_rate = interest rate per year
    years = how many years since initial loan
    """
    return principal * (1 + annual_rate) ** years

print("if i'm loaned $25,000, and have a yearly rate of 0.06 APR, then i owe", round(amount_owed(principal = 25000, annual_rate = 0.06, years = 5), 2), "dollars after 5 years.")

def total_interest(principal, annual_rate, years):
    return amount_owed(principal, annual_rate, years) - principal

print("the total interest i paid in addition to my $25,000 is", round(total_interest(principal = 25000, annual_rate = 0.06, years = 5), 2), "dollars.")
# the precondition for annual_rate is that it can't be more than 1! and most often values over 0.5 are way, way too high.
# it also can't be negative, since that means the bank pays /you/ interest, which they hate
# the postcondition for amount_owed is that it won't exceed principal * (1 + 0.5) ** years,
# since the precondition is that annual_rate can't exceed 0.5.

# it's better to have 