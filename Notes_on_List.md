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

> When we pass an immutable object to a function, the function can use the argument name to create a new object. But then, it must return that object to make it available to the calling code.

> When we pass a mutable object like a list to a function, the function can change the object. In that case the function doesn't need to return the object to the calling code because it already has a varaible that refers to the object.


### List of lists
- A Python list of lists is a list in which the items are other lists.
- Then, to access the item in the list of lists, we use two indexes.
- A list of lists is also called as two-dimensional list (matrix), and we can think of the data as columns within rows.
