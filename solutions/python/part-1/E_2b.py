"""Exam scores

The following dictionary stores four students' exam scores for a given course:
`d = {'Adam':95, 'Lisa':85, 'Bart':59, 'Paul': 74}`.

Calculate the average, max, and min scores.
"""

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}

sum = 0.0
max_score = list(d.values())[0]
min_score = list(d.values())[0]
for _, i in d.items():
    sum += i
    if i > max_score:
        max_score = i
    if i < min_score:
        min_score = i
        print(min_score)
print("Average score is:", sum / len(d))
print("Max score is:", max_score, max(d.values()))
print("Min score is:", min_score, min(d.values()))
