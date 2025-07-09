# Create a list with 8 indian names with duplicates
names = ["Aarav", "Vivaan", "Aditya", "Sunder", "Rohan", "Aarav", "Vivaan", "Aditya"]
print(names)

# Remove the first occurrence of "Aarav"
names.remove("Aarav")
print(names)

# Remove the first occurrence of "Aditya"
names.remove("Aditya")
print(names)

# Remove the "Aditya" again
names.remove("Aditya")
print(names)

# Remove an item that does not exist
names.remove("Praveen")
