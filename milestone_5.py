import random

class Hangman:

    def __init__(self, word_list = ["mangoes", "bananas", "grapes", "strawberries", "oranges"], num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for x in range(len(self.word))]
        self.num_letters = len(self.word)
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for letter in self.word:
                if letter == guess:
                    position = self.word.find(letter)
                    print(position)
                    self.word_guessed[position] = letter
                    print(self.word_guessed)
            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

        self.list_of_guesses += [guess]


    def ask_for_input(self):

        while True:
            guess = input("Please enter a single letter: ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
                
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            else:
                print(self.word_guessed)
                self.check_guess(guess)
                self.list_of_guesses += [guess]

def play_game():
    game = Hangman(["cherries", "bananas", "figs", "strawberries", "blueberries"], 7)

    while True:
        if game.num_lives == 0:
            print("You lost!")
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")



play_game()
# game = Hangman()  # if you pass a new list and a new number of lives in the parenthesis of this object's(game) class, it will overwrite the pre defined parameters in the classes initialiser 
# game.ask_for_input()