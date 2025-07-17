# Create a list of Indian student names
students = ['Aarav', 'Vivaan', 'Aditya', 'Vihaan', 'Arjun']

# Write the list to a file named 'zstudents.txt'
with open('zstudents.txt', 'w') as file:
    for student in students:
        file.write(student + '\n')
        