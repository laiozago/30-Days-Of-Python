"""Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples)."""

from random import choices
from string import hexdigits

def list_of_hexa_colors(num):    
    return [f"#{''.join(choices(hexdigits.lower(), k=6))}" for _ in range(num)]
