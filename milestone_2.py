import random

word_list = ['Apple', 'Banana', 'Strawberry', 'Orange', 'Pear']
word = random.choice(word_list)

print(word)

guess = input("Please enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    ("Oops! That is not a valid input!")
