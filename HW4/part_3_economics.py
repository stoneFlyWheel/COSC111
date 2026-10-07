# part A --------

def find_break_even_month(cashflows):
    total = 0
    for month in range(len(cashflows)):
        total += cashflows[month]
        if total > 0:
            return month
    return -1

flows = [-500, -200, -100, 150, 300, 400]
print(find_break_even_month(flows)) # 5(note: we start indexing at 0, not 1)
# cumulative totals by month: -500, -700, -800, -650, -350, 50 -> turns positive at month 5
 