import csv

with open('z_scores.csv', 'r', newline='') as f:
    f_reader = csv.reader(f)
    for row in f_reader:
        print(row)