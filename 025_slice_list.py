numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

# first two elements
print(numbers[0:2])  # Output: [5, 10]

# first two elements
print(numbers[:2])   # Output: [5, 10]

# starting from index 4 to the end
print(numbers[4:])   # Output: [25, 30, 35, 40, 45, 50, 55, 60]

# from index 0 to index 4, not including index 4, but alternatively elements
print(numbers[0:4:2])  # Output: [5, 15]

# all elements in reverse order
print(numbers[::-1])