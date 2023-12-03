#FOR CSV MODULE

import csv
print("OUTPUT-1")
with open('data1.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
print("OUTPUT-2")
with open('data2.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
