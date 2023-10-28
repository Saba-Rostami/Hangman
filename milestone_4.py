import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = [] 

    def check_guess(self, guess):
        guess = guess.lower()   # Converts the guessed letter to lowercase 
        if guess in self.word:   # Checks if the letter is in the randomly chosen word
            print(f"Good guess! {guess} is in the word.")
            for index in range(len(self.word)):  # replaces _ with the letter 
                if self.word[index] == guess:
                    self.word_guessed[index] = guess
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
        
    def ask_for_input(self):
        while True:
            guess = input("Please enter a letter: ")    # Asks the user to enter a letter
            if len(guess) != 1 or not guess.isalpha():   # Checks if the letter is not one single letter and is an alphabet
                print("Invalid letter. Please, enter a single alphabetical character.")  
            elif guess in self.list_of_guesses:   # Checks if the letter is in the list of already guessed letters
                print("You already tried that letter!") 
            else:
                self.list_of_guesses.append(guess)  # Add the guess to the list of guesses.
                self.check_guess(guess)  # Call the check_guess method with the guess as an argument.
                if self.num_letters == 0:
                    break  # If all letters are guessed, exit the loop.

hangman = Hangman(["apple", "banana", "watermelon", "strawberry", "grape"])
hangman.ask_for_input()
