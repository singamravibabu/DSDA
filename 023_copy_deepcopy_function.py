# Create a list of 6 names
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']

import copy
new_names = copy.deepcopy(names)

# modify the names and new_names list
names[0] = "Anand"
new_names[1] = "Praveen"

# print both lists
print("Original names list:", names)
print("Deep copied names list:", new_names)
