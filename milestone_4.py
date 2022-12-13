import random # importing the random module from the python library

word_list = ['Apple', 'Banana', 'Strawberry', 'Orange', 'Pear'] # list of fruit
word = random.choice(word_list) # randomly chooses a fruit from the list
word_guessed = ['_']    # list of letters of the word - e.g: if the word is apple it should display 5 underscore '_, _, _, _, _'
num_letters = 26    # number of letter that has not been guessed
num_lives = 5   # number of lives starting from 5 
list_of_guesses = []    # this is an empty list where it will store letter that have already been guessed

class Hangman():    # hangman class
    def __int__(self, word_list, num_lives=5):  # setting up the initialiser and the attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word
        self.num_letters = len(set(word))
        self.list_of_guesses = []
        self.word_guessed = ['_'] * len(set(word))