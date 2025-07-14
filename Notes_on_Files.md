# WORKING WITH FILES

Two typse of files:
1. Text
    - Contains one or more lines that contain text characters.
    - In a text file, each line ends with a newline character (\n).
    - On Windows, this character is sometimes preceded by a carriage return character (\r).
    - Common types:
        - TXT files
        - CSV files
        - JSON files
        - XML files
        - HTML files

2. Binary
    - Any file that isn't a text file.
    - Many binary file formats contain parts that can be interpreted as text.
    - However, binary files typically contain sequences of bytes that are intended to be interpreted as something other than text characters.
    - Common types:
        - Compiled program files (.exe, .msi)
        - Images files (jpg, jpeg, png)
        - Audio files
        - Video files
        - Database files
        - Compressed files


### Sequence of file operations
1. Open the file
2. Write data to the file or read data frm the ile
3. Close the file


### Opening a file
- When we open a file, we create a file object.
- Then, we can use the methods of the file object to work with the file.

#### open() function
```
open(file, mode)
```

- `file` is filenames including path if the file and program is not in the same directory
- `mode` the purpose of opening a file
    1. r - Read
        - If the file doesn't exist, this mode causes a file not found error.
    2. w - Write
        - If the file doesn't exist, this mode creates a new file.
        - If the file exists, this mode overwrites the existing file.
    3. a - Append
    4. b - Binary
