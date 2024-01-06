"""Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated."""

from random import choices
from string import ascii_lowercase, digits

def user_id_gen_by_user():
    num_caracteres = int(input('Quantos digitos em cada usuario gerado? '))
    quantidade = int(input('Quantos usuarios quer gerar? '))
    caracteres = digits + ascii_lowercase
    user_id = []
    for _ in range(0,quantidade):
        user_id.append(''.join(choices(caracteres, k=num_caracteres)))
    return user_id

print(user_id_gen_by_user())