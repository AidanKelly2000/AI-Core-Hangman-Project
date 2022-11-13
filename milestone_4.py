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

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")