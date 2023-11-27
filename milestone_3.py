import random

def check_guess(guess, secret_word):
    """Check if the guessed letter is in the word."""
    # Step 2: Convert the guess into lower case.
    guess = guess.lower()

    # Step 3: Check if the guess is in the word.
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    """Ask the user to guess a letter and validate the input."""
    while True:
        # Step 2: check if the input is a valid guess into this function block.
        guess = input("Guess a letter: ")

        # Step 3: Check guess is a single alphabetical character.
        if guess.isalpha() and len(guess) == 1:
            # Step 4: If the guess passes the checks, break out of the loop.
            print("You guessed:", guess)
            break
        else:
            # If the guess does not pass checks, print error message.
            print("Invalid letter. Please, enter a single alphabetical character.")

    # Step 5: Outside the while loop, call check_guess function to check if guess in word.
    check_guess(guess, secret_word)

# Secret word
secret_word = "apple"

# Step 6: Outside  function, call the ask_for_input function to test code.
ask_for_input()
