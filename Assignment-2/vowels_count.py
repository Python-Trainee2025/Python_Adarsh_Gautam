# 2. Accept a word/sentence from the user and count how many vowels (a, e, i, o, u) are present in it.
user_input = input('Enter word or sentence: ')
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
counter = 0
for letter in user_input:
    if letter in vowels:
        counter += 1
print(f'{counter} vowel words were found')
