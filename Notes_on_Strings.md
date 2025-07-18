# WORKING WITH STRINGS
- Python uses unicode to store the characters in strings.
- Function to find a unicode value for a character:
    - ord('char')
- Function to find a character for a unicode value:
    - chr(unicode)
- The len(str) returns an integer for the length of the specified string.

#### Accessing characters in a string
- `str[index]`
- If we use an index that doesn't exists in the string, Python raises an IndexError that indicates that the index is out of range.

#### Strings are immutable
- A string is immutable, which means that we can't change its characters.
- If we attempt to do that, Python raises a TypeError.

#### Slicing a string
- `str[start:end:step]`
- String is sliced similar to a list object.

#### Duplicating a string
- Duplicating a string works same as duplicating a string.
    - `str * int`
    - `int * str`
    - `str * float`     # this is not possible
    - `float * str`     # this is not possible
    - `str * complex`   # this is not possible
    - `complex * str`   # this is not possible

#### Searing a string
- substring in string
    If the substring is in string it returns True; otherwise returns False.
    - `str1 in str2`

#### Looping through characters in a string
```
for char in str:
    statement(s)
```


### String methods
1. isalpha()
    Returns True if all the characters are alphabetic letters; otherwise False.
2. islower()
    Returns True if all the characters are lowercase letters; otherwise False.
3. isupper()
    Returns True if all the characters are uppercase letters; otherwise False.
4. isdigit()
    Returns True if all the characters are numeric; otherwise returns False.