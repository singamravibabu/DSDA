# Using functins we see the difference between mutable and immutable objects

def double_the_number(value):
    value = value * 2
    return value

value1 = 25
value2 = double_the_number(value1)
print(value1)
print(value2)


def add_to_list(list, item):
    list.append(item)

cities = ['London', 'Paris', 'New York']
add_to_list(cities, 'Tokyo')
print(cities)
