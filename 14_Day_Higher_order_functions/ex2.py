"""
Use map to create a new list by changing each country to uppercase in the countries list
"""

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

countries_upper = list(map(lambda palavra: palavra.upper(),countries))

"""
Use map to create a new list by changing each number to its square in the numbers list
"""

squares = list(map(lambda num: num**2,numbers))


"""
Use map to change each name to uppercase in the names list
"""

names_upper = list(map(lambda name: name.upper(),names))


"""
Use filter to filter out countries containing 'land'.
"""

countries_with_land = list(filter(lambda countrie: 'land' in countrie,countries))


"""
Use filter to filter out countries having exactly six characters.
"""

countries_with_6_letters = list(filter(lambda countrie: len(countrie) == 6,countries))

"""
Use filter to filter out countries containing six letters and more in the country list.
"""

countries_with_6_letters_or_more = list(filter(lambda countrie: len(countrie) >= 6,countries))


"""
Use filter to filter out countries starting with an 'E'
"""

countries_starting_with_e = list(filter(lambda countrie: countrie[0].upper() == 'E',countries))


"""
Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
map countries to upper case and filter countries that starts with S
"""

countries_starting_with_s_and_to_upper_case = list(filter(lambda countrie: countrie[0] == 'S',map(lambda countrie: countrie.upper(),countries)))


"""
Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
"""

def get_string_lists(lst):
    only_strings = filter(lambda item: type(item)==str,lst)
    return list(only_strings)


"""
Use reduce to sum all the numbers in the numbers list.
"""

from functools import reduce

soma_da_lista = reduce(lambda num1,num2: int(num1)+int(num2),numbers)

"""
Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
"""

frase = reduce(lambda x,y: x+', '+y,countries)
frase = frase + ' are north European countries.'


