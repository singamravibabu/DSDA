# Create a list of 10 fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry", 
          "fig", "grape", "honeydew", "kiwi", "lemon"]
print("Original list:", fruits)

# remove last item using pop method
last_item = fruits.pop()
print("Last item removed:", last_item)
print("Updated list:", fruits)

# remove the last item using pop method
last_item = fruits.pop()
print("Last item removed:", last_item)
print("Updated list:", fruits)

# remove item at index 2 using pop method
item_at_index_2 = fruits.pop(2)
print("Item at index 2 removed:", item_at_index_2)
print("Updated list:", fruits)