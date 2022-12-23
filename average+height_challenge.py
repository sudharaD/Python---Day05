import random

heights = []
total_of_heights = 0

for i in range(0, 10):  # => 10
    height = random.uniform(135.0, 180.1)
    heights.append(round(height, 1))

for student_height in heights:
    total_of_heights += student_height

average_height = round(total_of_heights / 10, 2)

print(f"Average height is {average_height}")