# Create a list of lists for student and 3 scores (4x7 matrix)
students_scores = [
    ['Alice', 85, 90, 88],
    ['Bob', 92, 88, 95],
    ['Charlie', 78, 85, 80],
    ['David', 90, 92, 91],
    ['Eva', 88, 84, 90],
    ['Frank', 82, 79, 85],
    ['Grace', 95, 91, 89]
]

import csv

with open('z_scores.csv', 'w', newline='') as file:
    file_writer = csv.writer(file)
    file_writer.writerows(students_scores)