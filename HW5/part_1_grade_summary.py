# part A ---------

def grade_summary(scores):
    min = scores[0]
    max = scores[0]

    for score in range(0, len(scores)):
        if scores[score] < min:
            min = scores[score]
        if scores[score] > max:
            max = scores[score]

    total = 0
    for score in range(0, len(scores)):
        total += scores[score]

    average = total / len(scores)

    answer = [min, max, average]
    print(answer)

grade_summary([72, 85, 90, 64, 58, 95, 81, 88])
grade_summary([100, 92, 85, 78, 90])

# part B ---------

running = True
while running:
    scores = []
    score = input("Enter a score (or 'done' to finish): ")

    while score != "done":
        scores.append(int(score))
        score = input("Enter a score (or 'done' to finish): ")

    print("Grade summary:")
    grade_summary(scores)
    running = False