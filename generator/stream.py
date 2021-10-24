"""Generates random sentences."""

from random import choice, randint
from string import ascii_letters, digits
import datetime 

def generate_random_sentence() -> dict:
    """Create a fake sentence."""
    letters = ascii_letters+'            '
    stringLength = randint(0, 50)
    sentence = ''.join(choice(letters) for i in range(stringLength))
    players = ['player1', 'player2']
    return {
        'time':str(datetime.datetime.now().time() ),
        'player': choice(players),
        'sentence': sentence
    }
