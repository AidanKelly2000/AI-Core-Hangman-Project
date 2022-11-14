# AI-Core-Hangman-Project

## Milestone 1
- Set up Github to start using it to create repositories for projects

## Milestone 2

- This milestone began by creating a python file "milestone_2.py" which was then added to the remote repo.

- Then a list of fruits was created using pythons built in list function, it was assigned the variable "word_list".

- In order to begin the coding of Hangman, the import "random" was implemented, this is used to randomly select a word from the "word_list" variable.

- After this, the user is asked to input a letter which was assigned the variable "guess", this guess was passed to an if statement which determined whether the guess was   adequate. For a guess to be adequate it had to be a string length of one and alphabetic, if this condition was met, the user was told "Good guess!" which printed to the terminal. Anything else was given the printed statement "Oops! That is not a valid input." alerting the user that they didnt meet the conditions of the input. 

- The final step of milestone 2 was to create this README.md file, in order to log all of the stages of creating this Hangman game.

## Milestone 3

- Two functions were defined, one checked if the guess was correct. If the guess was correct the program said "Good guess! {guess} is in the word." if not it would say "Sorry, {guess} is not in the word. Try again.". This check_guess function takes in the randomly selected word from word_list, and then checks if the guessed letter is in that word.

- The second function defines the conditions of the guess input, the function was called "ask_for_input". This function tells the user if the guess meets the requirements of the game i.e. is it a single alphabetic input.

- Finally the check_guess function was called within the ask_for_input function, but not in the while loop. Then outside of the function the ask_for_input function was called, and the code was tested to make sure it worked.

## Milestone 4

- add description of milestone_4.py