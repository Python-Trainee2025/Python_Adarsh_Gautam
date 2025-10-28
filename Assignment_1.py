
# Assignment 1:

# 1. Take input from user for two words, and check if they are anagrams (anagram example: listen and silent -> both contain the same number and set of alphabets)
def check_anagram():
    word = input("Enter two words separated by space: ")
    word1, word2 = word.lower().split()

    if sorted(word1) == sorted(word2):
        print("The two words are anagram")
    else:
        print("The two words are not anagram")


# 2. Get input from user and check if it is palindrome
def check_palindrome():
    word = input("Enter a word: ")
    if word[::-1] == word:
        print("The word is palindrome")
    else:
        print("The word is not palindrome")



# 3. Input a sentence or a paragraph from user and extract how many unique words are used and display the count
def check_unique_words():
    sentence = input("Enter a sentence:")
    words = sentence.lower().split()
    unique_words = set(words)

    print(f"Unique words: {len(unique_words)}")
    print(f"total words: {len(words)}")
    print(f"Unique words: {unique_words}")




# 4. Create a dictionary with a person's name and contact info for a small company,
# take the input from a user to search for a user using their name, return the number
# (example user will search for 'Ram' and if user exists, their phone number is returned)
def search_employee_contact_info():
    employee_info = {
        "employee_1": {
            "name": "Ron blake",
            "contact_number": 9845816874
        },
        "employee_2": {
            "name": "John Doe",
            "contact_number": 9845914871
        },
        "employee_3": {
            "name": "Ram Upreti",
            "contact_number": 9845927462
        }
    }
    name = input("Enter a name: ")

    found = False
    for employee in employee_info.values():
        if employee["name"].lower() == name.lower():
            print(f"Employee {employee['name']} contact number: {employee['contact_number']}")
            found = True
            break

    if not found:
        print(f"{name} does not exist")

while True:
    print(f"Select the function:")
    print("1. Check Anagram")
    print("2. Check Palindrome")
    print("3. Check Unique Words")
    print("4. Fetch contact info of employee")
    print("0. Exit")

    choice = int(input("Enter your choice:"))

    match choice:
        case 1:
            check_anagram()
        case 2:
            check_palindrome()
        case 3:
            check_unique_words()
        case 4:
            search_employee_contact_info()
        case 0:
            break
        case _:
            print("Wrong choice")
