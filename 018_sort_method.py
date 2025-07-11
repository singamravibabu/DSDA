# Create a list with items to sort
items = ["mango", "apple", "banana",
          "kiwi", "orange", "grape", "Pear",
          'peach', "watermelon", "cherry",
          "blueberry", "strawberry", "kiwi",
          'guava', "papaya", "pineapple", "pear"]

# Sort the list items
# items.sort()
# print(items)

# Sort the list items
items.sort(key=str.lower)   # str.upper
print(items)
