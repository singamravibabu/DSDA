# All registered participants (students + employees)
participants = [
    "Student1", "Student2", "Employee1", "Student3", "Employee2", "Employee3"
]

# Participants who attempted the exam
attempted = ["Student1", "Employee1", "Student3", "Employee3"]

# Participants who passed (from those who attempted)
passed = ["Student1", "Employee3"]

# Empty lists to track status
not_attempted = []
failed = []

# Determine who did NOT attempt the exam
for person in participants:
    if person not in attempted:
        not_attempted.append(person)

# Determine who attempted but FAILED
for person in attempted:
    if person not in passed:
        failed.append(person)

# Show summary
print("\nAll Participants:", participants)
print("Attempted Exam:", attempted)
print("Passed Exam:", passed)
print("Failed Exam:", failed)
print("Not Attempted:", not_attempted)
