# WORKING WITH DICTIONARIES
> Unlike a list, which is an ordered collection of items, a dictionary is an unordered collection of items. As a result, there's no guarantee that the item in a dictionary remain in the same order.

- In a dictionary, each item consists of a key/value pair where each value in the dictionary is indexed by a unique key.

```
dictionary_name = {key1:value1, key2:value2, key3:value3, ...}
```

- The key can be any immutable data type, but its usually a string.
- In some languages, dictionaries are called associative arrays.

##### Getting items from a dictionay
```
dictionary_name[key]
```

- If the key doesn't exist in the dictionary then it throws a KeyError.


##### Adding an item to a dictionary
```
dictionary_name[newKey] = value
```

##### Checking whether a key is in a dictionary
```
key in dictionary_name
```

If key in dictionary it returns True; otherwise reutrns False.


#### Prevent KeyError using get() method

```
dictionary_name.get(key[, default])
```

- If the specified key exists, this method returns its value.
- Otherwise, this method returns None or the default value if it is specified.

#### Delete items from dictionary

- We can use the `del` keyword or the `pop()` and `clear()` methods to delete items from a dictionary.

```
del dictionary_name[key]
```

```
pop(key[, defaul_value])

Returns the value of the specified key and deletes the key/value pair from the dicionary.
The optional second argument is a value to return if the key doesn't exist.
```

```
clear()

Deletes all items from a dictionary.
```

