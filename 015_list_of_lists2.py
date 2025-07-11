# Create a list of lists with 5 rows and 4 columns: students and their marks (three marks)
students_marks = [
    ['Alice', 85, 90, 88],
    ['Bob', 78, 82, 80],
    ['Charlie', 92, 95, 93],
    ['David', 70, 75, 72],
    ['Eve', 88, 84, 90]
]

'''
# Print the list of students and their marks
for student in students_marks:
    print(student)

print()'''

# looping through each item from a list of lists
for student in students_marks:
    for item in student:
        print(item, end="\t")
    print()
