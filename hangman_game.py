import random

def print_hangman(turns):
    HMpics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
              "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
              "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
              "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
              "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
              "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
              "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]

    print(HMpics[6 - turns])

def hangman():
    words = ["hello", "world", "python", "hangman", "code"]
    word = random.choice(words)
    word_letters = set(word)
    guessed_letters = set()
    turns = 6

    print("\nLet's play Hangman!")
    while turns > 0:
        display_word = "".join([letter if letter in guessed_letters else "_ " for letter in word])
        print(display_word)

        if set(word) == guessed_letters:
            print("You got it! The word was:", word)
            break

        letter = input("Guess a letter: ").lower()

        if letter in guessed_letters:
            print("You already guessed that!")
            continue
        else:
            guessed_letters.add(letter)

        if letter in word_letters:
            print("Good guess!")
        else:
            turns -= 1
            print("Nope")
            print_hangman(turns)
        
        print("Letters guessed:", " ".join(guessed_letters))

    if turns == 0:
        print("He died rip :(")
        print("The word was:", word)

hangman()
