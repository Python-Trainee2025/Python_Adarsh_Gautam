import csv
from logging import exception
# 5. Read a .csv file and print each row. Handle file not found and other parsing errors if needed
try:
    with open('test.csv', 'r') as csvfile:
        reader = csv.reader(open('test.csv'))
        next(reader)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File not found")
except exception as e:
    print(f"Something went wrong{e}")