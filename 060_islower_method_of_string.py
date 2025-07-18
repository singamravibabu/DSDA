# The islower() method simple examples, without function definition
# The islower() method checks if all characters in a string are lowercase
# and returns True if they are, otherwise it returns False.

# Example 1: All characters are lowercase
string1 = "hello world"
print(string1.islower())  # Output: True

# Example 2: Contains uppercase characters
string2 = "Hello World"
print(string2.islower())  # Output: False

# Example 3: Empty string
string3 = ""
print(string3.islower())  # Output: False

# Example 4: String with numbers and special characters
string4 = "hello123!"
print(string4.islower())  # Output: True

# Example 5: Mixed case with special characters
string5 = "hello World!"
print(string5.islower())  # Output: False

# Example 6: String with only special characters
string6 = "!@#$%^&*()"
print(string6.islower())  # Output: True

# Example 7: String with whitespace
string7 = "   "
print(string7.islower())  # Output: True
