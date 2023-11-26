# milestone_5.py

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """Initialize the Hangman game."""
        self.word_list = word_list
        self.word = self.pick_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def pick_random_word(self):
        """Pick a random word from the word list."""
        return random.choice(self.word_list)

    def check_guess(self, guess):
        """Check if the guessed letter is in the word and update game state."""
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.update_word_guessed(guess)

            if self.num_letters == 0:
                self.end_game("Congratulations! You guessed the word.")

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

            if self.num_lives == 0:
                self.end_game(f"Game over! The word was: {self.word}")

    def ask_for_input(self):
        """Ask the user to guess a letter and validate the input."""
        while self.num_letters > 0 and self.num_lives > 0:
            guess = input("Guess a letter: ")

            if not self.is_valid_guess(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self.already_guessed(guess):
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess.lower())

        if self.num_letters == 0:
            self.end_game(f"Congratulations! You guessed the word: {''.join(self.word_guessed)}")
        else:
            self.end_game(f"Sorry, you ran out of lives. The word was: {self.word}")

    def update_word_guessed(self, guess):
        """Update the word_guessed list based on the correct guess."""
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
                self.num_letters -= 1

    def is_valid_guess(self, guess):
        """Check if the guess is a single alphabetical character."""
        return guess.isalpha() and len(guess) == 1

    def already_guessed(self, guess):
        """Check if the guess has already been tried."""
        return guess.lower() in self.list_of_guesses

    def end_game(self, message):
        """Print the end-of-game message and exit the game."""
        print(message)
        exit()

def play_game(word_list):
    """Run the Hangman game."""
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

# Example use:
word_list = ['apple', 'banana', 'orange', 'grape']
play_game(word_list)
