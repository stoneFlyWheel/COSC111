scores = [72, 85, 90, 64, 58, 95, 81, 88]

# find average
average = sum(scores) / len(scores)
print(f"average: {average}")

# sort the scores
sorted_scores = sorted(scores)
print(f"sorted scores: {sorted_scores}")

# find min and max scores
print(f"min score: {sorted_scores[0]}")
print(f"max score: {sorted_scores[-1]}")

# discussion:
# 1.
# sorted(), the function, does not change the original list! it creates a copy that is then sorted.
# 2.
# however, .sort(), the method, does change the original list in place. no copies are made. 