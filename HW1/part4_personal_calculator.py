# 4.1 - Your (my) Personal Calculator ---------

# calculate savings from not buying books
# Description: show how much i DO NOT need more books

# ---------------------

# variables
book_count = 24
books_to_read = 9
avg_book_cost = 17.00
monthly_budget = 100.00

# calculations

# buy three new books
three_book_budget = monthly_budget - (3 * avg_book_cost)

# buy six new books (this number is negative! i account for this in the printed statements)
six_book_budget = abs(monthly_budget - (6 * avg_book_cost))

# print results!

print("--- DO NOT BUY MORE BOOKS calculator :) ---")
print("look, you already have " + str(book_count) + " in your room, and " + str(books_to_read) + " new books to read. isn't that enough??")
print("books are expensive! they cost $" + str(avg_book_cost) + "0, on average, and you only have $" + str(monthly_budget) + "0 to spend on fun stuff.")
print("if you bought 3 more books, you'd have $" + str(three_book_budget) + "0 left to spend on other, necessary things. y'know, like food?")
print("if you bought 6 more books, you'd have -$" + str(six_book_budget) + "0 left. what are you going to do with that???")
