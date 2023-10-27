import random

# Create a list containing the names of your 5 favorite fruits. Assign this list to a variable called word_list.

word_list = ["apple", "banana", "strawberry", "grapes", "watermelon"]

# Print out the newly created list to the standard output (screen).

print(word_list)

word = random.choice(word_list)

print(word)

guess = input("Please Enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input.")