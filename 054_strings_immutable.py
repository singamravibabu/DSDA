city = 'hyderabad'


# 1. Accessing a character (this works)
print(f"The character at index 0 is: {city[0]}")

# 2. Attempting to assign a new value to an index (this will fail)
print("\nAttempting to change city[0] to 'm'...")
try:
    city[0] = 'm'
except TypeError as e:
    print(f"Caught an expected error: {e}")
    print("This confirms that strings are immutable; you cannot change them in place.")

# 3. The correct way to "change" a string is to create a new one.
new_city = 'm' + city[1:]
print(f"\nTo get the desired result, we create a new string: '{new_city}'")
