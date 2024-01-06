"""FUNÇÃO PARA GERAR 6 NUMEROS ALEATORIOS ENTRE 1-60"""
from random import sample

def sorteio_6_numeros():
    return sample(list(range(1,61)),6)

print(sorteio_6_numeros())