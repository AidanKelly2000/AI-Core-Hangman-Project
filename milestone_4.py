import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for letters in range(len(self.word))]
        self.num_letters = len(self.word)
        self.list_of_guesses = []
        word_list = ["mangoes", "bananas", "grapes", "strawberries", "oranges"]

    def check_guess(self):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            for letter in self.word:
                if letter == guess:
                    position = self.word.find(letter)
                    self.word_guessed[position] = letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):

        while True:
            guess = input("Please enter a single letter: ")
            if len(guess) == 1 and guess.isalpha():
                break
            elif guess in self.list_of_guesses:
                print("You already tried that letter")

            else:
                check_guess(guess)
        self.list_of_guesses.extend([guess])


Hangman.ask_for_input()

   
   