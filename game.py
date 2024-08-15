import random
from words import list

def choose_word():
    word = random.choice(list)
    return word.upper()

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def draw_hangman(incorrect_guesses):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        ---------
        """
    ]
    print(stages[incorrect_guesses])

def play_hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    tries = 6

    print("🕵️‍♂️ Get ready to save the stickman! Guess wisely, or watch him swing! Let's play Hangman")

    while incorrect_guesses < tries:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        draw_hangman(incorrect_guesses)

        # Check if only one guess is left
        if tries - incorrect_guesses == 1:
            print("⚠️ Hurry up! The man is about to be hanged! You only have one guess left!")

        guess = input("Guess a letter: ").upper()

        # Validate the guess
        if len(guess) != 1:
            print("Please enter only one letter.")
            continue
        elif not guess.isalpha():
            print("Please enter a valid letter (A-Z or a-z).")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            if set(word) <= guessed_letters:
                print(f"🎉 Congratulations! You saved the man and guessed the word: {word}")
                break
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {tries - incorrect_guesses} guesses left.")

    
    if incorrect_guesses == tries:
        draw_hangman(incorrect_guesses)
        print(f"\nYou've run out of guesses. The word was: {word}. Better luck next time!")

# Run the Hangman game
play_hangmanhangman()