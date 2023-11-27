import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = self.pick_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def pick_random_word(self):
        return random.choice(self.word_list)

    def check_guess(self, guess):
        """Check if the guessed letter is in the word."""
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
                    self.num_letters -= 1

            # Check if the word is fully guessed
            if self.num_letters == 0:
                print(f"Congratulations! You guessed the word: {''.join(self.word_guessed)}")
                

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

            # Check if the player ran out of lives
            if self.num_lives == 0:
                print(f"Game over! The word was: {self.word}")
                

    def ask_for_input(self):
        """Ask the user to guess a letter and validate the input."""
        while self.num_letters > 0 and self.num_lives > 0:
            guess = input("Guess a letter: ")

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess.lower() in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess.lower())

        if self.num_letters == 0:
            print(f"Congratulations! You guessed the word: {''.join(self.word_guessed)}")
        else:
            print(f"Sorry, you ran out of lives. The word was: {self.word}")

# Example
word_list = ['apple', 'banana', 'orange', 'grape']
hangman_game = Hangman(word_list)

# ask_for_input method test
hangman_game.ask_for_input()


