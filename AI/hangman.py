# Importing the random module to use its functions for generating random choices
import random

# Function to display the hangman stages based on the number of attempts left
def display_hangman(attempts):
    # List of strings representing the hangman stages from final state to initial state
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    # Returning the hangman stage that corresponds to the current number of attempts
    return stages[attempts]

# Function that encapsulates the hangman game logic
def hangman():
    # List of possible words to guess
    words = ['python', 'java', 'kotlin', 'javascript']
    # Randomly selecting a word from the list of words
    word_to_guess = random.choice(words)
    # Creating a list of underscores representing the letters of the word to guess
    guessed_word = ['_'] * len(word_to_guess)
    # Setting the number of attempts a player has
    attempts = 6
    # Set to keep track of guessed letters
    guessed_letters = set()

    # Printing a welcome message
    print("Welcome to Hangman!")

    # Loop until the player has no attempts left
    while attempts > 0:
        # Display the current hangman stage
        print(display_hangman(attempts))
        # Display the current state of the guessed word
        print("\n" + " ".join(guessed_word))
        # Display the number of attempts remaining
        print(f"Attempts remaining: {attempts}")
       
        # Prompting the player to guess a letter
        guess = input("Guess a letter: ").lower()
       
        # Checking if the input is valid (single letter and alphabetic)
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
       
        # Checking if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
       
        # Adding the guessed letter to the set of guessed letters
        guessed_letters.add(guess)
       
        # If the guessed letter is in the word to guess
        if guess in word_to_guess:
            # Updating the guessed word with the correct letter in the correct positions
            for idx, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[idx] = guess
            # If there are no more underscores, the player has guessed the word correctly
            if '_' not in guessed_word:
                print("\n" + " ".join(guessed_word))
                print("Congratulations! You guessed the word!")
                break
        else:
            # Decreasing the number of attempts left if the guess was incorrect
            attempts -= 1
            print(f"Incorrect guess. The letter '{guess}' is not in the word.")
   
    # If the player has run out of attempts, displaying the final hangman stage and the correct word
    if attempts == 0:
        print(display_hangman(attempts))
        print(f"Game over! The word was '{word_to_guess}'.")

# Starting the hangman game by calling the hangman function
hangman()
