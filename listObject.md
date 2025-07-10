# WORKING WITH LISTS
> A list is a collection of items.

##### The syntax for creating a list
list_name = [item1, item2, item3, ...]

##### We can use the repetition operator (*) to repeat the items int he list
*[item] * int*


##### Referring an item in a list
> To refer an item in a list, we use an index, where 0 refers the first item, 1 refers the second item, 2 refers to the third item, and so on.

> We can also use negative values for an index, where -1 refers to the last item in the list, -2 refers to the second last item, -3 refers to the third last item, and so on.

```
list_name[index]
```

### List methods
> We can use te list methods to add and remove the items in a list.

1. append(item)
> Appends the specified item to the end of the list.

2. insert(index, item)
> Inserts the specified item at the specified index.

3. remove(item)
> Removes the first item in the list that is equal to the specified item.
> If item isn't found, this method raises a ValueError.

4. index(item)
> Returns the index of the first occurance of the specified item in the list.
> If item isn't found, this method raises a ValueError.

5. pop([index])
> If no index argument is specified, this method get the last time from the list and removes it. Otherwise, this method gets the item specified at the index and removes it.

### Built-in function
```
len(list)
```
> Returns the number of items in the list.


### Membership: 'in' keyword
```
item in list
```
> If the item is in the list it returns True; otherwise return False.


### Looping through items in a list
```
for item in list:
    statement(s)
```

> For each item you can run the statement(s).


### Mutable and Immutable 
> **Immutable types:** str, int, bool, float, tuple
> **Mutable types:** list, dict, set