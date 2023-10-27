import random

# Create a list containing the names of your 5 favorite fruits. Assign this list to a variable called word_list.

word_list = ["apple", "banana", "strawberry", "grapes", "watermelon"]

# Print out the newly created list to the standard output (screen).

print(word_list)

word = random.choice(word_list)

print(word)

def check_guess(guess):

    if guess.isalpha() and len(guess) == 1:
        guess = guess.lower()
        if guess in word:
            return f"Good guess! {guess} is in the word."
        else: 
            return f"Sorry, {guess} is not in the word. Try again."
    else:
        return f"Sorry, {guess} is not in the word. Try again."

def ask_for_input():
    
    while True:
        guess = input("Please Enter a single letter: ")
        result = check_guess(guess)
        print(result)
        if guess in word:
            break
            

ask_for_input()

