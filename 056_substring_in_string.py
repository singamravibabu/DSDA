# checking for substring in a string
msg = 'Hello world! We are Python coders.'

# The original code was formatted for an interactive shell like IDLE.
# To run it as a script in VS Code, we use print() to display the boolean result.
# The 'in' operator returns True if a substring is found, otherwise False.

# Case-sensitive search for an exact match at the beginning
print(f"Is 'Hello' in msg? {'Hello' in msg}")

# Case-sensitive search will fail for a different case
print(f"Is 'hello' in msg? {'hello' in msg}")

# Substring can be anywhere in the string
print(f"Is 'code' in msg? {'code' in msg}")

# Substring can include spaces
print(f"Is 'e a' in msg? {'e a' in msg}")

# A non-existent substring
print(f"Is 'a b' in msg? {'a b' in msg}")

# Searching for a substring and checking using 'if' statement
if 'Python' in msg:
    print("Found 'Python' in msg!")
else:
    print("Did not find 'Python' in msg.")