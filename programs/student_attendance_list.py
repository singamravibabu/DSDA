# List of all enrolled students
students = [
    "Aarav", "Bhavana", "Chaitanya", "Divya", "Eshwar"
]

# Empty list for present students
present_students = []

# Empty list for absent students
absent_students = []

# Function to mark attendance
def mark_attendance(present_list):
    for student in students:
        if student in present_list:
            present_students.append(student)
        else:
            absent_students.append(student)

# Function to display attendance summary
def show_attendance():
    print("\nTotal Students:", students)
    print("Present Students:", present_students)
    print("Absent Students:", absent_students)

# Real-life usage: Suppose these students are present today
today_present = ["Aarav", "Divya", "Eshwar"]

# Mark attendance
mark_attendance(today_present)

# Show summary
show_attendance()
