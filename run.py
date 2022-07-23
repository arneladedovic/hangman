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

def get_word():
    """
    Function that gets a random word from words.py.
    """
    word = random.choice(word_list)
    return word.upper()

def menu():
    """
    Menu with options to see rules or start game.
    """
    print('Press 1 to see the rules')
    print('Press 2 to start the game')

    option = input('Enter number: \n')

    if option == "1":
        rules()
    elif option == "2":
        play()
    else:
        print('Please enter 1 or 2.')
        menu()

def main():
    """
    Main function that runs the game
    """
    logo()
    word = get_word()

main()