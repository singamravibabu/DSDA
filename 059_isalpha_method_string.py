# The isalpha method simple examples, without function definition
# The isalpha method checks if all characters in a string are alphabetic

# Example 1: Using isalpha on a simple string
s = "HelloWorld"
print(s.isalpha())  # Output: True

# Example 2: Using isalpha on a string with spaces
s = "Hello World"
print(s.isalpha())  # Output: False

# Example 3: Using isalpha on a string with numbers
s = "Hello123"
print(s.isalpha())  # Output: False

# Example 4: Using isalpha on a string with special characters
s = "Hello@World"
print(s.isalpha())  # Output: False

# Example 5: Using isalpha on an empty string
s = ""
print(s.isalpha())  # Output: True
