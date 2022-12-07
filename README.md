# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

In the milestone_2.py file, on the 1st line I have imported a module called random, which will get an element randomly from a list

On line 3, I have created a variable called word_list and in this list it contains various fruit
word_list = ['Apple', 'Banana', 'Strawberry', 'Orange', 'Pear']

On line 4, this is where the import random module come in play, I have assigned a variable called word and in this variable I have a random.choice function, which is a function sequence that will get a word at random from the list created in word_list variable.

On line 6, print(word) will call out and run the code, this will output a random fruit from the word_list.  

On line 8, is an input() function where an user guess a single letter in a word

Between line 10 to 13, is a if statement where a user guessed letter is a single letter and its an alphabet and that is true then the outcome should display "Good Guess" and if its not a valid letter or number then the output should display "Oops! That is not a valid input!"
