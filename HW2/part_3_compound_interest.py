def amount_owed(principal, annual_rate, years):
    """
    principal = initial money owed
    annual_rate = interest rate per year
    years = how many years since initial loan
    """
    return principal * (1 + annual_rate) ** years

