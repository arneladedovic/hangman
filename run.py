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

def main():
    """
    Main function that runs the game
    """
    logo()
    word = get_word()

main()