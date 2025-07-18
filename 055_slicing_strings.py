# Give examples of string slicing in Python using str[start:end:step] syntax
# Example 1: Basic slicing
my_string = "Hello, World!"
# Slicing from index 0 to 4 (exclusive)
sliced_string1 = my_string[0:5]
print(sliced_string1)  # Output: "Hello"

# Example 2: Slicing with step
sliced_string2 = my_string[0:12:2]
print(sliced_string2)  # Output: "Hlo ol"

# Example 3: Slicing with negative indices
sliced_string3 = my_string[-6:-1]
print(sliced_string3)  # Output: "World"

# Example 4: Slicing the entire string
sliced_string4 = my_string[:]
print(sliced_string4)  # Output: "Hello, World!"

# Example 5: Slicing with a negative step
sliced_string5 = my_string[::-1]
print(sliced_string5)  # Output: "!dlroW ,olleH"

# Example 6: Slicing with start and end only
sliced_string6 = my_string[7:12]
print(sliced_string6)  # Output: "World"

# Example 7: Slicing with start, end, and step
sliced_string7 = my_string[7:12:1]
print(sliced_string7)  # Output: "World"

# Example 8: Slicing with start and step
sliced_string8 = my_string[7::2]
print(sliced_string8)  # Output: "Wrl"

# Example 9: Slicing with end and step
sliced_string9 = my_string[:12:3]
print(sliced_string9)  # Output: "Hlo"

# Example 10: Slicing with all parameters
sliced_string10 = my_string[0:12:3]
print(sliced_string10)  # Output: "Hl"
