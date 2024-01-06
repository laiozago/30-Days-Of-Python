"""Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each)."""

from random import randint
def rgb_color_gen():
    return [randint(0,255) for _ in range(3)]

for _ in range(10):
    print(rgb_color_gen())