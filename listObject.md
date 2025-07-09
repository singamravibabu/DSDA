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


