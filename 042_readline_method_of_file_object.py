with open('zcode.txt', 'r') as f_obj:
    l1 = f_obj.readline()  # Reads the first line of the file
    l2 = f_obj.readline()  # Reads the second line of the file
    l3 = f_obj.readline()  # Reads the third line of the file
    print(l1, l2, l3, sep="", end='')