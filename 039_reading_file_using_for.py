with open('zcode.txt', 'r') as file:
    for line in file:
        print(line, end='')  # end='' prevents adding an extra newline)