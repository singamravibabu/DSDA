new_list = []
with open('zcode.txt', 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        new_list.append(line)
print(new_list)