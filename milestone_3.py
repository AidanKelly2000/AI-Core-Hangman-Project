import random

# Creating while loop so the user will be continually asked for more letters
word_list = ["mangoes", "bananas", "grapes", "strawberries", "oranges"]
print(word_list)

# Selects a random word from the list of fruits "word_list", and prints it to terminal
word = random.choice(word_list)
print(word)

while True:
    guess = input("Please enter a single letter: ")
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")


