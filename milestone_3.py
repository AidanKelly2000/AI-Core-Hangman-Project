# Creating while loop so the user will be continually asked for more letters
"""
guess = input("Please enter a single letter: ")

while len(guess) == 1 and guess.isalpha():
    input("Please enter another single letter: ")
"""

while True:
    guess = input("Please enter a single letter: ")
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

