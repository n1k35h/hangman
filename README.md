# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

In the milestone_2.py file, on the 1st line I have imported a module called random, which will get an element randomly from a list

On line 3, I have created a variable called word_list and in this list it contains various fruit
word_list = ['Apple', 'Banana', 'Strawberry', 'Orange', 'Pear']

On line 4, this is where the import random module come in play, I have assigned a variable called word and in this variable I have a random.choice function, which is a function sequence that will get a word at random from the list created in word_list variable.

On line 6, variable guess is created for user input, where it will ask for a user to enter a letter of the randomly chosen word  

On line 7 to 12, it has couple of if statement, first if statement instructs the length of user guessed character to equal to 1 character and the character should be an alphabet - guess.isalpha(). Second if statement from 8 to 11 instruct that if the guess letter is in the word then print out "Good guess" else "Oops! That is not a valid input!". Line 12 prints out the word of the game.

In the milestone_3.py file, it contains 2 defined function, which are check_guess and ask_for_input. 
In the check_guess function guess is passed as a parameter as an argument. Line 7 is to make sure that the guess letter that user inputted is in lowercase - guess.lower().On line 8 to 12, it has couple of if statement, first if statement instructs the length of user guessed character to equal to 1 character and the character should be an alphabet - guess.isalpha(). Second if statement from 9 to 12 instruct that if the guess letter is in the word then print out f"Good guess ,{guess}, is in the word." else f"Sorry, {guess} is not the word". {guess} is the letter that the user inputted. 

In the ask_for_input funtion, is where user input the letter of the randomly chosen word. Line 15, calls the check_guess(word) function and takes the word variable as an argument. Line 16, is where user will input their chosen letter of the randomly chosen word. Line 17 to 25 contains a while loop, where on line 17 the condition is True: if the criteria is met. 

On line 27, the ask_for_input is called to run the code.

In the milestone_4.py file, it contains a class method for Hangman with 3 defined function - __init__, check_guess and ask_for_input

