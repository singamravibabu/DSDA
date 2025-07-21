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

5. startswith(substring)
    Returns True if the string starts with the specified substring; otherwise returns False.

6. endswith(substring)
    Returns True if the string ends with the specified substring; otherwise returns False.

7. lower()
    Converts all the letters in a string to lowercase.

8. upper()
    Converts all the letters in a string to uppercase.

9. title()
    Converts the string to a title case and returns it.

10. lstrip()
    Strips the whitespaces from the left and returns the string.

11. rstrip()
    Strips the whitespaces from the right and returns the string.

12. strip()
    Strips the whitespaces from both sides and returns the string.

13. ljust(width)
    Returns a left-justified string with spaces add to fill out the width.

14. rjust(width)
    Returns a right-justified string with spaces add to fill out the width.

15. center(width)
    Returns a centered string with spaces add to fill out the width.


#### The find() method of a string
```
str.find(substring[, start[, end]])
```

- Searches for the substring and returns the index of the first occurance or -1 if the substring isn't found.
- The optional `start` and `end` parameters let us set the starting and ending indexes for the search.


#### The replace() method of a string

```
str.replace(old, new[, num])
```

- Returns a new string with occurances of the old substring replaced by the new substring.
- The optional `num` parameter specifies the maximum number of occurances to be replaced.


#### The split() method of a string
```
split([delimiter][, num])
```

- A delimiter is a character that's used to divide a string into multiple substrings and returns a list of these substrings.
- By default, the delimiter is whitespace.
- The second parameter specifies the number of occurances to replace.

