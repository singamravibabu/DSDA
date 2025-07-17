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
3. Close the file (every file that is opened must be closed)


### Opening a file
- When we open a file, a file object is created.
- Then, we can use the methods of the file object to work with the file.

#### open() function
```
open(file, mode)
```

- `file` is filename including path if the file and program is not in the same directory
- `mode` the purpose of opening a file
    1. r - Read
        - If the file doesn't exist, this mode causes a file not found error.
    2. w - Write
        - If the file doesn't exist, this mode creates a new file.
        - If the file exists, this mode overwrites the existing file.
    3. a - Append
        - If the file doesn't exist, this mode creates a new file.
        - If the file exists, this mode appends the data to the end of the file.
    4. b - Binary
        - Use for the bnary files along with 'rb' or 'wb' mode.
    
#### close() function
- As told, every open file must be closed.
- To close a file use `close()` method

```
f = open('example.txt', 'r')
print(f.read())
f.close()
```

#### with statement
- When file is open using `with` statement, then it closes automatically.
- After executing the block of statements in `with` statement, the file is automatically closed.

#### Writing to a file
- To write data to a text file, we can use the write() method of the file object.

```
file_obj.write(string)
```


#### Reading from a file
- To read from a text file, we can use a `for` statement to iterate through the lines in the file object.
- Or, we can call the read methods of the file object.
- There are three read methods of the file object
    - read()
        * reads the entire file and returns its contents as string
    - readlines()
        * reads the entire file and returns its contents as a list of strings, where each string is a line in the file
    - readline()
        * reads a single line from the file and returns it as a string


## WORKING WITH CSV FILES
- A comma-separated values (CSV) file stores tabular data in a text form.
- Within this file, each lineis a row that ends with a new line character, and each row contains one or more columns are typically separated by commas.
- Rows and columns can also be referred to as records and fields.
- To work with CSV file in Python, we can use (import) the `csv` module.

### Writing Data to a CSV file
- To write data to a CSV file, we use the writer() function of the `csv` module to get writer object.

#### The writer() function of the CSV module
```
writer(file)
```
- Returns a CSV writer object for the file.
- The writer object converts the data into comma-seperated values
- After using the writer object we use writerows() method of the writer object.

#### The writerows() method of the CSV object
- Write all specified rows to the file specified by the writer object using the CSV format specified by the writer object.

**Note:** When we open a CSV file or reading or writing, we typically specified an argument name `newline` with a vale of an empty string. this enables universal newlines mode, so that reading and writing operations work correctly in all operating systems.

### Reading Data from a CSV file
- To read data from a CSV file, we use the reader() function of the `csv` module to create reader object. Then, we can use a `for` statement with reader object to read the data in the file.

#### The reader() function of the CSV
```
reader(file)
```
- Returns a CSV reader object for the file.
- The reader gets the data from the CSV file.


## WORKING WITH BINARY FILES
- We can use methods of the `pickle` module to work with binary files.
- It can be used to dump (write) an object like a list to a file and to load (read) an object like a list from a binary file.

### Two methods of the pickle module
- dump(object, bfile)
    - Writes the specified object to the binary file.
- load(bfile)
    - Reads the object from the binary file.

