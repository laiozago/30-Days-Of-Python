"""Writ a function which generates a 
six digit/character 16e2h0 random_user_id."""

from string import digits,ascii_lowercase
from random import choices

def random_user_id():
    digitos = digits+ascii_lowercase
    return ''.join(choices(digitos, k=6))

print(random_user_id())