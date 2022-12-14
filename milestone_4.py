import random # importing the random module from the python library

class Hangman():    # hangman class
    def __init__(self, word_list, num_lives=5):  # setting up the initialiser and the attributes
        self.word = word = random.choice(word_list)
        self.word_guessed = "_" * len(set(word))  # '_' = underscore will display depending on the length of the word 
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
