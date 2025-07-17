with open('zcode.txt', 'r') as f:
    lines = f.readlines()
    # print(lines)  # Print the list of lines read from the file
    print(lines[0], end="")  # Print the first line without adding an extra newline
    print(lines[1], end="")  # Print the second line without adding an extra
    