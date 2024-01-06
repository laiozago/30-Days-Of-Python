"""Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique."""

from string import digits
from random import sample

def random_seven():
    return sorted(sample(digits,7))

print(random_seven())