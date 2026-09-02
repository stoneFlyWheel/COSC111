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

