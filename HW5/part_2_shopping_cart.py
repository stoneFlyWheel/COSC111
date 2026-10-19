item_names  = ["apple", "bread", "milk", "eggs"]
item_prices = [3.00, 5.50, 4.25, 3.10]

def cart_total(names, prices):
    total = 0
    for price in range(len(names)):
        total += prices[price]
    print(total)

def most_expensive_item(names, prices):
    max = prices[0]
    index = 0
    for price in range(len(names)):
        if prices[price] > max:
            max = prices[price]
            index = price

    print(names[index])

def apply_discount(names, prices, discount_percent):
    new_prices = prices[:]
    for price in range(len(names)):
        new_prices[price] = new_prices[price] * (1 - (discount_percent / 100))

    print(new_prices)

cart_total(item_names, item_prices)
most_expensive_item(item_names, item_prices)
apply_discount(item_names, item_prices, 10)
print(item_prices)