# set variables
units_in_stock = 340
daily_usage = 25
lead_time_days = 6
safety_stock = 50
# variables for obj. 19 -----
products = ["Widget A", "Widget B", "Widget C"]
stock_levels = [300, 120, 264]
usage_rates = [10, 50, 15]

def compute_reorder_point(daily_usage, lead_time_days, safety_stock):
    reorder_point = daily_usage * lead_time_days + safety_stock
    return reorder_point

def needs_reorder(units_in_stock, reorder_point):
    return units_in_stock <= reorder_point

def check_product(product_name, units_in_stock, daily_usage, lead_time_days, safety_stock):
    reorder_point = compute_reorder_point(daily_usage, lead_time_days, safety_stock)
    print(product_name + ":", "reorder point =", str(reorder_point) + ",", "in stock =", str(units_in_stock) + ",", "reorder needed =", needs_reorder(units_in_stock, reorder_point))

# example case
check_product("ExampleProduct(tm)", units_in_stock, daily_usage, lead_time_days, safety_stock)

# go forth!
for index in range(0, 3):
    check_product(products[index], stock_levels[index], usage_rates[index], lead_time_days, safety_stock)

# it's risky to do so because it's far harder to debug complex functions with many unknowns
# than to debug on a constrained test case!