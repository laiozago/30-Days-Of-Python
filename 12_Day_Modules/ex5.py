"""Write a function list_of_rgb_colors which returns any number of RGB colors in an array."""

from random import randint

def list_of_rgb_colors(num):
    return [f"rgb({', '.join(str(randint(0, 255)) for _ in range(3))})" for _ in range(num)]