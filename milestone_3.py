import random

word_list = ['apple', 'banana', 'Strawberry', 'Orange', 'Pear']
word = random.choice(word_list)

while True:
    guess = input("Please enter a single letter: ")
    if len(guess) == 1 and guess.isalpha():
        if guess in word:
            print(f"Good guess ,{guess}, is in the word.")
            break
        else:
            print(f"Sorry, {guess} is not in the word")
    print(word)
    print('\n')
