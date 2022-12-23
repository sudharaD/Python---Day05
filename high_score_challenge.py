import random

max = 0

student_scores = input("Enter student scores: ").split()

print(student_scores)

for i in student_scores:
    if max < int(i):
        max = int(i)


print(f"Highest score: {max}")

del max

print(max(student_scores))

print("============================================")

scores = []
max_score = 0

for i in range(20):
    scores.append(random.randint(0, 100))

print(scores)

for i in scores:
    if max_score < i:
        max_score = i


print(f"Highest score: {max_score}")
print(max(scores))