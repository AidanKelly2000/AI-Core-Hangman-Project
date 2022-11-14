import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for x in range(len(self.word))]
        self.num_letters = len(self.word)
        self.list_of_guesses = []
        word_list = ["mangoes", "bananas", "grapes", "strawberries", "oranges"]
        # does putting a list in the initialiser work? 

    def check_guess(self, guess):
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

        self.list_of_guesses += [guess]


    def ask_for_input(self):

        while True:
            guess = input("Please enter a single letter: ")
            if len(guess) != 1 and guess != guess.isalpha():   # How do i get it so that the if statement works
                print("Invalid letter. Please, enter a single alphabetical character.")
                
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            else:
                game.check_guess(guess)    # Is this running correct
                self.list_of_guesses += [guess]


game = Hangman
game.ask_for_input()

