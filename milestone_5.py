import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word, self.word_guessed, self.num_letters = self.initialize_game()
        self.list_of_guesses = []

    def initialize_game(self):
        word = random.choice(self.word_list).lower()
        word_guessed = ['_' for _ in word]
        num_letters = len(set(word))
        return word, word_guessed, num_letters

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.update_word_guessed(guess)
        else:
            self.reduce_lives()
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def update_word_guessed(self, guess):
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
                self.num_letters -= 1

    def reduce_lives(self):
        self.num_lives -= 1

    def ask_for_input(self):
        while self.num_lives > 0 and self.num_letters > 0:
            guess = input("Enter a single letter: ")
            if not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)

        if self.num_letters == 0:
            print(f"Congratulations. You won the game! The word was '{self.word}'.")
        else:
            print(f"You lost! The word was '{self.word}'.")

    def play_game(self):
        self.ask_for_input()

# Example usage
if __name__ == "__main__":
    word_list = ["apple", "banana", "orange", "strawberry", "mango"]
    game = Hangman(word_list)
    game.play_game()






