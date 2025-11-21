import random

def escolher(lista1: list, lista2: list):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    intersecao = conjunto1.intersection(conjunto2)
    return list(intersecao)

lista1 = [random.randint(1,5) for _ in range(3)]
lista2 = [random.randint(1,5) for _ in range(3)]

resposta = escolher(lista1, lista2)
print(escolher)