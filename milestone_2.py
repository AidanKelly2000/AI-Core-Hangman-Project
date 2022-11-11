import random

# Creating a list of favourite fruits and assigning to the variable word_list

word_list = ["Mangoes", "Bananas", "Grapes", "Strawberries", "Oranges"]
print(word_list)

# Selects a random word from the list of fruits "word_list", and prints it to terminal

word = random.choice(word_list)
print(word)

guess = input("Please enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")










