"""Write a function generate_colors which can generate any number of hexa or rgb colors."""

from ex4 import list_of_hexa_colors
from ex5 import list_of_rgb_colors

def generate_colors(tipo,quantidade):
    if tipo.lower() == 'rgb':
        return list_of_rgb_colors(quantidade)
    elif tipo.lower() == 'hexa':
        return list_of_hexa_colors(quantidade)
        
print(generate_colors('rgB',3))