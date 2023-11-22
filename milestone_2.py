import random
# milestone_2.py

# Step 1: Create a list containing the names of your 5 favorite fruits.
favorite_fruits = ["Apple", "Banana", "Orange", "Strawberry", "Mango"]

# Step 2: Assign this list to a variable called word_list.
word_list = favorite_fruits

word = random.choice(word_list)

guess = input("Enter a single letter: ")

if len(guess) == 1 and guess.isalpha():  # Step 1: Check if the length is 1 and the input is alphabetical.
    print("Good guess!")  # Step 2: Print a message for a valid input.
else:
    print("Oops! That is not a valid input")
    


# Step 3: Print out the newly created list to the standard output (screen).
print(word_list)
print(word)
