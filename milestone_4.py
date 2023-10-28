import random

class Hangman:
    def __init__(self, word_list, num_lives=5):

        """
        Initialize a new Hangman game instance.

        Args:
            word_list (list): A list of words from which the secret word is chosen.
            num_lives (int, optional): The number of lives or incorrect guesses allowed. Default is 5.

        Attributes:
            word_list (list): The list of words to choose from.
            num_lives (int): The initial number of lives.
            word (str): The secret word to be guessed.
            word_guessed (list): A list representing the progress of guessing the word.
            num_letters (int): The number of unique letters in the secret word.
            list_of_guesses (list): A list to store all guessed letters.
        """

        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = [] 

    def check_guess(self, guess):

        """
        Check if the guessed letter is in the secret word and update game state.

        Args:
            guess (str): The letter guessed by the player.

        Prints:
            - "Good guess! {guess} is in the word." if the guess is correct.
            - "Sorry, {guess} is not in the word. Try again." if the guess is incorrect.
        
        Updates:
            - Modifies word_guessed to reveal correct guesses.
            - Decreases num_lives for incorrect guesses.
        """

        guess = guess.lower()    
        if guess in self.word:   
            print(f"Good guess! {guess} is in the word.")
            for index in range(len(self.word)):  
                if self.word[index] == guess:
                    self.word_guessed[index] = guess
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
        

    def ask_for_input(self):

        """
        Prompt the player for a letter and handle the input validation and game loop.

        Prints:
            - "Invalid letter. Please, enter a single alphabetical character" for invalid input.
            - "You already tried that letter!" for repeated guesses.
            - "Congratulations! You guessed the word" if all letters are correctly guessed.
            - "Sorry, you're out of lives. The word was: {word}" if the player runs out of lives.
        """

        while self.num_lives > 0:
            guess = input("Please enter a letter: ")   
            if len(guess) != 1 or not guess.isalpha():   
                print("Invalid letter. Please, enter a single alphabetical character.")  
            elif guess in self.list_of_guesses:  
                print("You already tried that letter!") 
            else:
                self.list_of_guesses.append(guess)  
                self.check_guess(guess) 
                if self.num_letters == 0:
                    break

hangman = Hangman(["apple", "banana", "watermelon", "strawberry", "grape"])
hangman.ask_for_input()
