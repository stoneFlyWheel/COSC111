# step 1
scores = [72, 85, 90, 64, 58, 95, 81]

# step 2
for score in scores:
    print(score) 

# step 3
total = 0
for score in scores:
    total += score
average = total / len(scores)
print("Average:", average)

# step 4
highest = scores[0]
lowest = scores[0]
for score in scores:
    if scores[score] >= highest:
        highest = scores[score]
    if scores[score] <= lowest:
        lowest = scores[score]

print("Highest:", highest)
print("Lowest:", lowest)

# step 5
scores.append(88)
print(scores)

# extra credit!
passing_count = 0
failing_count = 0
for score in scores:
    if score >= 75:
        passing_count += 1
    else:
        failing_count += 1

print("Passing:", passing_count)
print("Failing:", failing_count)

# discussion

# 1
# indexing into a list is quite similar to indexing into a string! however,
# it's different in that the individual values of a list can be changed, while
# the individual characters of a string cannot be changed. 

# 2
# it gives me an index error: list index out of range. this is because scores
# doesn't have a 10th index, so when i try to call it, python doesn't know where
# to look for it.