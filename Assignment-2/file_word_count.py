# 3. Read a text file and count the number of words in it. Handle the case where the file might not exist.
try:
    with open('assignment.txt', 'r') as file:
        content = file.read()
        words = content.split()
        count = len(words)
        print(f"There are {count} words in this file.")
except FileNotFoundError:
    print("File not found.")
