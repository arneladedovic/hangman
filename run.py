import random
from words import word_list


def logo():
    """
    Game-Logo
    Made by: https://www.ascii-art-generator.org/
    """
    print("""
    _|    _|    _|_|    _|      _|    _|_|_|  _|      _|    _|_|    _|      _|
    _|    _|  _|    _|  _|_|    _|  _|        _|_|  _|_|  _|    _|  _|_|    _|
    _|_|_|_|  _|_|_|_|  _|  _|  _|  _|  _|_|  _|  _|  _|  _|_|_|_|  _|  _|  _|
    _|    _|  _|    _|  _|    _|_|  _|    _|  _|      _|  _|    _|  _|    _|_|
    _|    _|  _|    _|  _|      _|    _|_|_|  _|      _|  _|    _|  _|      _|
    """)


def menu():
    """
    Menu with options to see rules or start game.
    """
    print('Press 1 to see the rules')
    print('Press 2 to start the game')

    option = input('Enter number: \n')

    if option == "1":
        game_rules()
    elif option == "2":
        play()
    else:
        print('Please enter 1 or 2.')
        menu()


def game_rules():
    """
    Rules for the game.
    """
    print('Rules of the game\n')
    print(
        """
        Enter a letter from A to Z:\n
        If the letter is correct, it will show in the word.\n
        If it's not in the word, you loose a life.\n
        The game is over if you reach 0 lives
        or win by getting all letters right!\n
        """
    )
    print('GOOD LUCK')
    input('Press Enter to return to the menu!\n')
    menu()


def get_word():
    """
    Function that gets a random word from words.py.
    """
    word = random.choice(word_list)

    return word.upper()


def play(word):
    """
    Plays the game.
    Checks if player guessed right or wrong.
    Credits for inspiration: https://www.youtube.com/watch?v=m4nEnsavl6w
    """
    word_completion = "_" * len(word)
    print(word_completion)
    guessed = False
    guessed_letters = []
    tries = 6

    while not guessed and tries > 0:
        print(f"Already guessed: {guessed_letters}")
        guess = input('Guess a letter:')
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You have already guessed {guess}. Try another letter!")
            elif guess not in word:
                print(f"{guess} is not in the word. Try again!")
                tries -= 1
                if tries == 0:
                    print("""
                    --------
                    |      |
                    |      O
                    |     /|\\
                    |      |
                    |     / \\
                    -
                    """)
                if tries == 1:
                    print("""
                    --------
                    |      |
                    |      O
                    |     /|\\
                    |      |
                    |     /
                    -
                    """)
                    print(f"You have {tries} live(s) left.")

                if tries == 2:
                    print("""
                    --------
                    |      |
                    |      O
                    |     /|\\
                    |      |
                    |
                    -
                    """)
                    print(f"You have {tries} live(s) left.")

                if tries == 3:
                    print("""
                    --------
                    |      |
                    |      O
                    |     /|
                    |      |
                    |
                    -
                    """)
                    print(f"You have {tries} live(s) left.")

                if tries == 4:
                    print("""
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |
                    -
                    """)
                    print(f"You have {tries} live(s) left.")

                if tries == 5:
                    print("""
                    --------
                    |      |
                    |      O
                    |
                    |
                    |
                    -
                    """)
                    print(f"You have {tries} live(s) left.")

                if tries == 6:
                    print("""
                    --------
                    |      |
                    |
                    |
                    |
                    |
                    -
                    """)
                    print(f"You have {tries} live(s) left.")

                guessed_letters.append(guess)
            else:
                print(f"Nice, {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [
                    i for i, letter in enumerate(word) if letter == guess
                    ]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        else:
            print("Not a valid guess, please try again!")
        print(word_completion)
        print("\n")

    if guessed:
        print("You guessed the word. Congratulations, you win!")
    else:
        print(f"You lose... The word was: {word}.")


def main():
    """
    Main function that runs the game
    """
    logo()
    menu()
    game_rules()
    word = get_word()
    play(word)


main()
