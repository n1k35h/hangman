import random # importing the random module from the python library

word_list = ['Apple', 'Banana', 'Strawberry', 'Orange', 'Pear'] # list of fruit
word = random.choice(word_list)

class Hangman():    # hangman class
    def __init__(self, word_list, num_lives=5):  # setting up the initialiser and the attributes
        self.word = word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)  # '_' = underscore will display depending on the length of the word 
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess): # defining the check_guess and taking the guess parameter as an argument
        guess.lower()   # putting the users input as lower case
        if len(guess) == 1 and guess.isalpha(): # this is a if statement where users input is 1 character length long and its an alphabetical input
            if guess in word:   # another if statement where guess is in the word
                print(f"Good guess ,{guess}, is in the word.")  # if it is then print this statement
    
    def ask_for_input(self):    # defining the ask_for_input function, where user input their guess for the word
        guess = input("Please enter a single letter: ") # this takes the users input and once entered it will take the users input into a while loop
        
        while True: # if the while loop condition is True
            if len(guess) != 1 and guess.isalpha(): # this is a if statement where users input is 1 character length long and its an alphabetical input
                if guess not in word:   # another if statement where guess is in the word
                    print("Invalid letter. Please, enter a single alphabetical character.") # if it isn't then print this statement
                    
                elif guess in self.list_of_guesses:
                    print("You already tried that letter!")

                else:
                    self.check_guess(guess)   # this calls the check_guess function and takes in the word variable
                    self.list_of_guesses += guess

game = Hangman(word_list, num_lives=5)
game.ask_for_input()
